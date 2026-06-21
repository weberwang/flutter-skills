#!/usr/bin/env python3
"""gpt-image-2 生图脚本。"""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Final
from urllib import error, request

DEFAULT_MODEL: Final[str] = "gpt-image-2"
DEFAULT_SIZE: Final[str] = "auto"
DEFAULT_QUALITY: Final[str] = "hd"
DEFAULT_OUTPUT_FORMAT: Final[str] = "png"
DEFAULT_OUTPUT_PATH: Final[str] = "output/imagegen/output.png"
MAX_IMAGE_COUNT: Final[int] = 10
MIN_PIXELS: Final[int] = 655_360
MAX_PIXELS: Final[int] = 8_294_400
MAX_EDGE: Final[int] = 3840
MAX_RATIO: Final[float] = 3.0
# 兼容上游约定的 quality 档位与别名，避免继续接受旧参数。
ALLOWED_QUALITIES: Final[set[str]] = {"standard", "1k", "hd", "2k", "4k", "ultra", "high"}
ALLOWED_OUTPUT_FORMATS: Final[set[str]] = {"png", "jpeg", "jpg", "webp"}
ALLOWED_BACKGROUNDS: Final[set[str | None]] = {"transparent", "opaque", "auto", None}
TASK_POLL_INTERVAL_SECONDS: Final[int] = 2
DOWNLOAD_USER_AGENT: Final[str] = "Mozilla/5.0"


def _die(message: str, code: int = 1) -> None:
    """输出错误并终止脚本。"""
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _read_prompt(prompt: str | None, prompt_file: str | None) -> str:
    """读取用户提供的提示词内容。"""
    if prompt and prompt_file:
        _die("Use --prompt or --prompt-file, not both.")
    if prompt_file:
        path = Path(prompt_file)
        if not path.exists():
            _die(f"Prompt file not found: {path}")
        return path.read_text(encoding="utf-8").strip()
    if prompt:
        return prompt.strip()
    _die("Missing prompt. Use --prompt or --prompt-file.")


def _require_env(name: str) -> str:
    """读取必需环境变量。"""
    value = os.getenv(name, "").strip()
    if not value:
        _die(f"Environment variable {name} is required.")
    return value


def _parse_size(size: str) -> tuple[int, int] | None:
    """解析 WIDTHxHEIGHT 格式尺寸。"""
    match = re.fullmatch(r"([1-9][0-9]*)x([1-9][0-9]*)", size)
    if match is None:
        return None
    return int(match.group(1)), int(match.group(2))


def _validate_size(size: str) -> None:
    """校验 gpt-image-2 支持的尺寸范围。"""
    if size == "auto":
        return
    parsed = _parse_size(size)
    if parsed is None:
        _die("size must be auto or WIDTHxHEIGHT, for example 1024x1024.")
    width, height = parsed
    long_edge = max(width, height)
    short_edge = min(width, height)
    total_pixels = width * height
    if width % 16 != 0 or height % 16 != 0:
        _die("gpt-image-2 size width and height must be multiples of 16.")
    if long_edge > MAX_EDGE:
        _die("gpt-image-2 size maximum edge length must be <= 3840.")
    if long_edge / short_edge > MAX_RATIO:
        _die("gpt-image-2 size long edge to short edge ratio must not exceed 3:1.")
    if total_pixels < MIN_PIXELS or total_pixels > MAX_PIXELS:
        _die("gpt-image-2 total pixels must be between 655,360 and 8,294,400.")


def _normalize_output_format(output_format: str | None) -> str:
    """规范化输出格式名称。"""
    if output_format is None:
        return DEFAULT_OUTPUT_FORMAT
    normalized = output_format.lower()
    if normalized not in ALLOWED_OUTPUT_FORMATS:
        _die("output-format must be png, jpeg, jpg, or webp.")
    if normalized == "jpg":
        return "jpeg"
    return normalized


def _validate_quality(quality: str) -> None:
    """校验生成质量参数。"""
    if quality not in ALLOWED_QUALITIES:
        _die("quality must be one of standard, 1k, hd, 2k, 4k, ultra, or high.")


def _validate_background(background: str | None) -> None:
    """校验背景参数。"""
    if background not in ALLOWED_BACKGROUNDS:
        _die("background must be transparent, opaque, or auto for gpt-image-2.")


def _build_endpoint(base_url: str) -> str:
    """根据环境变量拼出最终生成接口地址。"""
    trimmed = base_url.rstrip("/")
    if trimmed.endswith("/images/generations"):
        return trimmed
    return f"{trimmed}/images/generations"


def _augment_prompt(args: argparse.Namespace, prompt: str) -> str:
    """按固定结构拼接提示词。"""
    if not args.augment:
        return prompt
    sections = [f"Primary request: {prompt}"]
    for label, value in (
        ("Use case", args.use_case),
        ("Scene/background", args.scene),
        ("Subject", args.subject),
        ("Style/medium", args.style),
        ("Composition/framing", args.composition),
        ("Lighting/mood", args.lighting),
        ("Color palette", args.palette),
        ("Materials/textures", args.materials),
        ("Text (verbatim)", f'"{args.text}"' if args.text else None),
        ("Constraints", args.constraints),
        ("Avoid", args.negative),
    ):
        if value:
            sections.append(f"{label}: {value}")
    return "\n".join(sections)


def _build_output_paths(out: str, output_format: str, count: int, out_dir: str | None) -> list[Path]:
    """根据单图或多图模式生成输出路径。"""
    suffix = f".{output_format}"
    if out_dir:
        base_dir = Path(out_dir)
        base_dir.mkdir(parents=True, exist_ok=True)
        return [base_dir / f"image_{index}{suffix}" for index in range(1, count + 1)]
    out_path = Path(out)
    if out_path.exists() and out_path.is_dir():
        return [out_path / f"image_{index}{suffix}" for index in range(1, count + 1)]
    if out_path.suffix == "":
        out_path = out_path.with_suffix(suffix)
    if count == 1:
        return [out_path]
    return [out_path.with_name(f"{out_path.stem}-{index}{out_path.suffix}") for index in range(1, count + 1)]


def _print_payload(endpoint: str, payload: dict[str, object], outputs: list[Path]) -> None:
    """打印 dry-run 结果，便于在发送前复核。"""
    preview = {"endpoint": endpoint, "outputs": [str(path) for path in outputs], **payload}
    print(json.dumps(preview, indent=2, ensure_ascii=False))


def _request_json(
    url: str,
    api_key: str,
    timeout_seconds: int,
    *,
    method: str = "GET",
    payload: dict[str, object] | None = None,
) -> dict[str, object]:
    """发送 JSON 请求并解析 JSON 响应。"""
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Authorization": f"Bearer {api_key}"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    req = request.Request(url, data=body, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return json.loads(response.read().decode(charset))
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        _die(f"HTTP {exc.code} from image endpoint: {details}")
    except error.URLError as exc:
        _die(f"Failed to reach image endpoint: {exc.reason}")
    except json.JSONDecodeError as exc:
        _die(f"Response is not valid JSON: {exc}")


def _extract_sync_b64_images(response: dict[str, object]) -> list[bytes]:
    """从同步接口响应中提取图片字节。"""
    data = response.get("data")
    if not isinstance(data, list) or not data:
        _die(f"Unexpected response shape, expected a non-empty data array: {response}")
    image_bytes: list[bytes] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            _die(f"Unexpected item at data[{index}]: {item}")
        b64_json = item.get("b64_json")
        if not isinstance(b64_json, str) or not b64_json.strip():
            _die(f"Missing b64_json at data[{index}]: {item}")
        image_bytes.append(base64.b64decode(b64_json))
    return image_bytes


def _build_task_status_endpoint(base_url: str, task_id: str) -> str:
    """构造异步任务状态查询地址。"""
    trimmed = base_url.rstrip("/")
    if trimmed.endswith("/images/generations"):
        trimmed = trimmed[: -len("/images/generations")]
    return f"{trimmed}/tasks/{task_id}"


def _download_bytes(url: str, timeout_seconds: int) -> bytes:
    """下载异步任务完成后的最终图片。"""
    req = request.Request(url, headers={"User-Agent": DOWNLOAD_USER_AGENT}, method="GET")
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            return response.read()
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        _die(f"HTTP {exc.code} while downloading generated image: {details}")
    except error.URLError as exc:
        _die(f"Failed to download generated image: {exc.reason}")


def _extract_image_urls(task_response: dict[str, object]) -> list[str]:
    """从异步任务完成响应中提取图片 URL。"""
    data = task_response.get("data")
    if not isinstance(data, dict):
        _die(f"Unexpected async task response shape: {task_response}")
    result = data.get("result")
    if not isinstance(result, dict):
        _die(f"Missing async task result payload: {task_response}")
    images = result.get("images")
    if not isinstance(images, list) or not images:
        _die(f"Missing async task images payload: {task_response}")
    urls: list[str] = []
    for item in images:
        if not isinstance(item, dict):
            _die(f"Unexpected async image item: {item}")
        url_value = item.get("url")
        match url_value:
            case str() as single_url if single_url.strip():
                urls.append(single_url)
            case [str() as first_url, *rest]:
                del rest
                urls.append(first_url)
            case _:
                _die(f"Missing image URL in async task result: {item}")
    return urls


def _resolve_image_bytes(*, base_url: str, api_key: str, response: dict[str, object], timeout_seconds: int) -> list[bytes]:
    """统一处理同步 b64 响应与异步 task 响应。"""
    data = response.get("data")
    if isinstance(data, list) and data and all(
        isinstance(item, dict) and isinstance(item.get("b64_json"), str) and item.get("b64_json", "").strip()
        for item in data
    ):
        return _extract_sync_b64_images(response)
    if not isinstance(data, list) or not data or not isinstance(data[0], dict):
        _die(f"Unexpected response shape, expected a task response: {response}")
    task_id = data[0].get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        _die(f"Missing b64_json at data[0]: {data[0]}")
    task_endpoint = _build_task_status_endpoint(base_url, task_id)
    deadline = time.monotonic() + timeout_seconds
    # 某些兼容网关会先返回 task_id，这里轮询直到任务完成再下载图片。
    while time.monotonic() <= deadline:
        task_response = _request_json(task_endpoint, api_key, timeout_seconds)
        task_data = task_response.get("data")
        if not isinstance(task_data, dict):
            _die(f"Unexpected async task response shape: {task_response}")
        task_status = task_data.get("status")
        if not isinstance(task_status, str) or not task_status.strip():
            _die(f"Missing async task status in task response: {task_response}")
        normalized_status = task_status.lower()
        if normalized_status == "completed":
            return [_download_bytes(url, timeout_seconds) for url in _extract_image_urls(task_response)]
        if normalized_status in {"failed", "cancelled", "canceled"}:
            _die(f"Async image task {task_id} ended with status {task_status}: {task_response}")
        time.sleep(TASK_POLL_INTERVAL_SECONDS)
    _die(f"Timed out while waiting for async image task {task_id}.")


def _write_image_bytes(images: list[bytes], outputs: list[Path], force: bool) -> None:
    """将图片字节写入本地文件。"""
    for index, image_bytes in enumerate(images):
        if index >= len(outputs):
            break
        output = outputs[index]
        if output.exists() and not force:
            _die(f"Output already exists: {output} (use --force to overwrite)")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(image_bytes)
        print(f"Wrote {output}")


def _create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。"""
    parser = argparse.ArgumentParser(description="Generate images with gpt-image-2 via a custom OpenAI-compatible endpoint.")
    for flag in ("--prompt", "--prompt-file", "--background", "--output-format", "--moderation", "--out-dir", "--use-case", "--scene", "--subject", "--style", "--composition", "--lighting", "--palette", "--materials", "--text", "--constraints", "--negative"):
        parser.add_argument(flag)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--output-compression", type=int)
    parser.add_argument("--out", default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--augment", dest="augment", action="store_true")
    parser.add_argument("--no-augment", dest="augment", action="store_false")
    parser.set_defaults(augment=True)
    return parser


def main() -> int:
    """执行脚本主流程。"""
    args = _create_parser().parse_args()
    if args.n < 1 or args.n > MAX_IMAGE_COUNT:
        _die("--n must be between 1 and 10.")
    if args.output_compression is not None and not (0 <= args.output_compression <= 100):
        _die("--output-compression must be between 0 and 100.")
    if args.timeout < 1:
        _die("--timeout must be >= 1.")
    prompt = _augment_prompt(args, _read_prompt(args.prompt, args.prompt_file))
    output_format = _normalize_output_format(args.output_format)
    _validate_size(args.size)
    _validate_quality(args.quality)
    _validate_background(args.background)
    base_url = _require_env("IMAGE_BASE_URL")
    api_key = _require_env("IMAGE_API_KEY")
    endpoint = _build_endpoint(base_url)
    payload: dict[str, object] = {"model": DEFAULT_MODEL, "prompt": prompt, "n": args.n, "size": args.size, "quality": args.quality, "output_format": output_format}
    if args.background is not None:
        payload["background"] = args.background
    if args.output_compression is not None:
        payload["output_compression"] = args.output_compression
    if args.moderation is not None:
        payload["moderation"] = args.moderation
    outputs = _build_output_paths(args.out, output_format, args.n, args.out_dir)
    if args.dry_run:
        _print_payload(endpoint, payload, outputs)
        return 0
    print(f"Calling {endpoint}", file=sys.stderr)
    started = time.time()
    response = _request_json(endpoint, api_key, args.timeout, method="POST", payload=payload)
    images = _resolve_image_bytes(base_url=base_url, api_key=api_key, response=response, timeout_seconds=args.timeout)
    _write_image_bytes(images, outputs, args.force)
    print(f"Generation completed in {time.time() - started:.1f}s.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
