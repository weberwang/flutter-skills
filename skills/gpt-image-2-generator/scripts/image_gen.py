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
from typing import Dict, List, Optional, Tuple
from urllib import error, request

DEFAULT_MODEL = "gpt-image-2"
DEFAULT_SIZE = "auto"
DEFAULT_QUALITY = "medium"
DEFAULT_OUTPUT_FORMAT = "png"
DEFAULT_OUTPUT_PATH = "output/imagegen/output.png"
MAX_IMAGE_COUNT = 10
MIN_PIXELS = 655_360
MAX_PIXELS = 8_294_400
MAX_EDGE = 3840
MAX_RATIO = 3.0
ALLOWED_QUALITIES = {"low", "medium", "high", "auto"}
ALLOWED_OUTPUT_FORMATS = {"png", "jpeg", "jpg", "webp"}
ALLOWED_BACKGROUNDS = {"opaque", "auto", None}


def _die(message: str, code: int = 1) -> None:
    """输出错误并终止脚本。"""
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _read_prompt(prompt: Optional[str], prompt_file: Optional[str]) -> str:
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
    return ""


def _require_env(name: str) -> str:
    """读取必需环境变量。"""
    value = os.getenv(name, "").strip()
    if not value:
        _die(f"Environment variable {name} is required.")
    return value


def _parse_size(size: str) -> Optional[Tuple[int, int]]:
    """解析 WIDTHxHEIGHT 格式的尺寸字符串。"""
    match = re.fullmatch(r"([1-9][0-9]*)x([1-9][0-9]*)", size)
    if not match:
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


def _normalize_output_format(output_format: Optional[str]) -> str:
    """规范化输出格式名称。"""
    if not output_format:
        return DEFAULT_OUTPUT_FORMAT
    normalized = output_format.lower()
    if normalized not in ALLOWED_OUTPUT_FORMATS:
        _die("output-format must be png, jpeg, jpg, or webp.")
    return "jpeg" if normalized == "jpg" else normalized


def _validate_quality(quality: str) -> None:
    """校验生成质量参数。"""
    if quality not in ALLOWED_QUALITIES:
        _die("quality must be one of low, medium, high, or auto.")


def _validate_background(background: Optional[str]) -> None:
    """校验背景参数。"""
    if background not in ALLOWED_BACKGROUNDS:
        _die("background must be opaque or auto for gpt-image-2.")


def _build_endpoint(base_url: str) -> str:
    """根据环境变量拼出最终的生成接口地址。"""
    trimmed = base_url.rstrip("/")
    if trimmed.endswith("/images/generations"):
        return trimmed
    return f"{trimmed}/images/generations"


def _fields_from_args(args: argparse.Namespace) -> Dict[str, Optional[str]]:
    """提取用于结构化补全提示词的字段。"""
    return {
        "use_case": args.use_case,
        "scene": args.scene,
        "subject": args.subject,
        "style": args.style,
        "composition": args.composition,
        "lighting": args.lighting,
        "palette": args.palette,
        "materials": args.materials,
        "text": args.text,
        "constraints": args.constraints,
        "negative": args.negative,
    }


def _augment_prompt(args: argparse.Namespace, prompt: str) -> str:
    """按固定结构扩展提示词，减少多轮重写。"""
    if not args.augment:
        return prompt

    fields = _fields_from_args(args)
    sections: List[str] = []
    if fields["use_case"]:
        sections.append(f"Use case: {fields['use_case']}")
    sections.append(f"Primary request: {prompt}")
    if fields["scene"]:
        sections.append(f"Scene/background: {fields['scene']}")
    if fields["subject"]:
        sections.append(f"Subject: {fields['subject']}")
    if fields["style"]:
        sections.append(f"Style/medium: {fields['style']}")
    if fields["composition"]:
        sections.append(f"Composition/framing: {fields['composition']}")
    if fields["lighting"]:
        sections.append(f"Lighting/mood: {fields['lighting']}")
    if fields["palette"]:
        sections.append(f"Color palette: {fields['palette']}")
    if fields["materials"]:
        sections.append(f"Materials/textures: {fields['materials']}")
    if fields["text"]:
        sections.append(f'Text (verbatim): "{fields["text"]}"')
    if fields["constraints"]:
        sections.append(f"Constraints: {fields['constraints']}")
    if fields["negative"]:
        sections.append(f"Avoid: {fields['negative']}")
    return "\n".join(sections)


def _build_output_paths(
    out: str,
    output_format: str,
    count: int,
    out_dir: Optional[str],
) -> List[Path]:
    """根据单图或多图模式生成输出文件路径。"""
    suffix = "." + output_format

    if out_dir:
        base_dir = Path(out_dir)
        base_dir.mkdir(parents=True, exist_ok=True)
        return [base_dir / f"image_{index}{suffix}" for index in range(1, count + 1)]

    out_path = Path(out)
    if out_path.exists() and out_path.is_dir():
        out_path.mkdir(parents=True, exist_ok=True)
        return [out_path / f"image_{index}{suffix}" for index in range(1, count + 1)]

    if out_path.suffix == "":
        out_path = out_path.with_suffix(suffix)

    if count == 1:
        return [out_path]

    return [
        out_path.with_name(f"{out_path.stem}-{index}{out_path.suffix}")
        for index in range(1, count + 1)
    ]


def _decode_and_write(images: List[str], outputs: List[Path], force: bool) -> None:
    """将 base64 图片写入本地文件。"""
    for index, image_b64 in enumerate(images):
        if index >= len(outputs):
            break
        output = outputs[index]
        if output.exists() and not force:
            _die(f"Output already exists: {output} (use --force to overwrite)")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(base64.b64decode(image_b64))
        print(f"Wrote {output}")


def _print_payload(endpoint: str, payload: Dict[str, object], outputs: List[Path]) -> None:
    """打印 dry-run 结果，便于在真正请求前复核参数。"""
    preview = {
        "endpoint": endpoint,
        "outputs": [str(path) for path in outputs],
        **payload,
    }
    print(json.dumps(preview, indent=2, ensure_ascii=False))


def _request_generation(
    endpoint: str,
    api_key: str,
    payload: Dict[str, object],
    timeout_seconds: int,
) -> Dict[str, object]:
    """调用自定义 OpenAI 兼容接口发起生图请求。"""
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        endpoint,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            raw = response.read().decode(charset)
            return json.loads(raw)
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        _die(f"HTTP {exc.code} from image endpoint: {details}")
    except error.URLError as exc:
        _die(f"Failed to reach image endpoint: {exc.reason}")
    except json.JSONDecodeError as exc:
        _die(f"Response is not valid JSON: {exc}")
    return {}


def _extract_images(response: Dict[str, object]) -> List[str]:
    """从接口返回中提取 base64 图片数组。"""
    data = response.get("data")
    if not isinstance(data, list) or not data:
        _die(f"Unexpected response shape, expected a non-empty data array: {response}")

    images: List[str] = []
    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            _die(f"Unexpected item at data[{index - 1}]: {item}")
        b64_json = item.get("b64_json")
        if not isinstance(b64_json, str) or not b64_json.strip():
            _die(f"Missing b64_json at data[{index - 1}]: {item}")
        images.append(b64_json)
    return images


def _create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。"""
    parser = argparse.ArgumentParser(
        description="Generate images with gpt-image-2 via a custom OpenAI-compatible endpoint."
    )
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--background")
    parser.add_argument("--output-format")
    parser.add_argument("--output-compression", type=int)
    parser.add_argument("--moderation")
    parser.add_argument("--out", default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--out-dir")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--augment", dest="augment", action="store_true")
    parser.add_argument("--no-augment", dest="augment", action="store_false")
    parser.set_defaults(augment=True)

    parser.add_argument("--use-case")
    parser.add_argument("--scene")
    parser.add_argument("--subject")
    parser.add_argument("--style")
    parser.add_argument("--composition")
    parser.add_argument("--lighting")
    parser.add_argument("--palette")
    parser.add_argument("--materials")
    parser.add_argument("--text")
    parser.add_argument("--constraints")
    parser.add_argument("--negative")
    return parser


def main() -> int:
    """执行脚本主流程。"""
    parser = _create_parser()
    args = parser.parse_args()

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

    # 使用独立环境变量名，避免和通用 OpenAI SDK 约定发生混淆。
    base_url = _require_env("IMAGE_BASE_URL")
    api_key = _require_env("IMAGE_API_KEY")
    endpoint = _build_endpoint(base_url)

    payload: Dict[str, object] = {
        "model": DEFAULT_MODEL,
        "prompt": prompt,
        "n": args.n,
        "size": args.size,
        "quality": args.quality,
        "output_format": output_format,
    }
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

    # 这里先打印目标接口与耗时，便于在自定义网关场景下排查路由与性能问题。
    print(f"Calling {endpoint}", file=sys.stderr)
    started = time.time()
    response = _request_generation(endpoint, api_key, payload, args.timeout)
    images = _extract_images(response)
    _decode_and_write(images, outputs, args.force)
    print(f"Generation completed in {time.time() - started:.1f}s.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
