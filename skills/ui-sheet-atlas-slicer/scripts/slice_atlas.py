#!/usr/bin/env python3
"""根据图集配置切出 UI atlas 切片。"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


def _die(message: str, code: int = 1) -> None:
    """输出错误并终止脚本。"""
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _load_image_module() -> Any:
    """延迟加载 Pillow，缺失时给出明确错误。"""
    try:
        from PIL import Image  # type: ignore
    except ImportError as exc:  # pragma: no cover - 运行环境依赖
        _die(f"Pillow is required for atlas slicing: {exc}")
    return Image


def _load_config(config_path: Path) -> dict[str, Any]:
    """读取并解析切图配置。"""
    if not config_path.exists():
        _die(f"Config file not found: {config_path}")
    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _die(f"Config file is not valid JSON: {exc}")


def _require_string(config: dict[str, Any], key: str) -> str:
    """读取必填字符串字段。"""
    value = config.get(key)
    if not isinstance(value, str) or not value.strip():
        _die(f"Config field '{key}' must be a non-empty string.")
    return value


def _require_slices(config: dict[str, Any]) -> list[dict[str, Any]]:
    """读取并校验切片列表。"""
    slices = config.get("slices")
    if not isinstance(slices, list) or not slices:
        _die("Config field 'slices' must be a non-empty array.")
    normalized: list[dict[str, Any]] = []
    for index, item in enumerate(slices):
        if not isinstance(item, dict):
            _die(f"Slice entry at index {index} must be an object.")
        normalized.append(item)
    return normalized


def _require_int(item: dict[str, Any], key: str, slice_id: str) -> int:
    """读取切片中的整数坐标字段。"""
    value = item.get(key)
    if not isinstance(value, int):
        _die(f"Slice '{slice_id}' field '{key}' must be an integer.")
    return value


def _build_output_path(output_dir: Path, item: dict[str, Any], default_ext: str) -> Path:
    """根据切片配置推导输出路径。"""
    explicit_output = item.get("output")
    if isinstance(explicit_output, str) and explicit_output.strip():
        return output_dir / explicit_output
    name = item.get("name") or item.get("id")
    if not isinstance(name, str) or not name.strip():
        _die("Each exported slice must provide 'name' or 'id'.")
    suffix = item.get("output_format")
    if isinstance(suffix, str) and suffix.strip():
        ext = suffix.lower().lstrip(".")
    else:
        ext = default_ext
    return output_dir / f"{name}.{ext}"


def _validate_bounds(
    *,
    atlas_width: int,
    atlas_height: int,
    x: int,
    y: int,
    width: int,
    height: int,
    slice_id: str,
) -> None:
    """校验切片范围是否落在图集内。"""
    if width <= 0 or height <= 0:
        _die(f"Slice '{slice_id}' width and height must be > 0.")
    if x < 0 or y < 0:
        _die(f"Slice '{slice_id}' x and y must be >= 0.")
    if x + width > atlas_width or y + height > atlas_height:
        _die(
            "Slice "
            f"'{slice_id}' bounds exceed atlas size: "
            f"atlas={atlas_width}x{atlas_height}, rect=({x},{y},{width},{height})."
        )


def _slice_atlas(
    *,
    atlas_path: Path,
    output_dir: Path,
    slices: list[dict[str, Any]],
    overwrite: bool,
) -> dict[str, Any]:
    """执行实际切图并输出结果清单。"""
    image_module = _load_image_module()
    if not atlas_path.exists():
        _die(f"Atlas image not found: {atlas_path}")
    output_dir.mkdir(parents=True, exist_ok=True)

    with image_module.open(atlas_path) as atlas_image:
        atlas_width, atlas_height = atlas_image.size
        default_ext = atlas_image.format.lower() if atlas_image.format else "png"
        results: list[dict[str, Any]] = []

        for item in slices:
            slice_id = str(item.get("id") or item.get("name") or "unknown")
            export = item.get("export", True)
            if not isinstance(export, bool):
                _die(f"Slice '{slice_id}' field 'export' must be boolean when provided.")

            record: dict[str, Any] = {
                "id": slice_id,
                "name": item.get("name"),
                "classification": item.get("classification"),
                "export": export,
            }

            if not export:
                record["status"] = "skipped"
                record["reason"] = "export_disabled"
                results.append(record)
                continue

            x = _require_int(item, "x", slice_id)
            y = _require_int(item, "y", slice_id)
            width = _require_int(item, "width", slice_id)
            height = _require_int(item, "height", slice_id)
            _validate_bounds(
                atlas_width=atlas_width,
                atlas_height=atlas_height,
                x=x,
                y=y,
                width=width,
                height=height,
                slice_id=slice_id,
            )

            output_path = _build_output_path(output_dir, item, default_ext)
            if output_path.exists() and not overwrite:
                _die(f"Output already exists: {output_path}. Use --overwrite to replace it.")
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # 只按配置切图，不在这里做额外推断或修图。
            cropped = atlas_image.crop((x, y, x + width, y + height))
            cropped.save(output_path)

            record.update(
                {
                    "status": "exported",
                    "output_path": str(output_path),
                    "bounds": {"x": x, "y": y, "width": width, "height": height},
                }
            )
            results.append(record)

    exported_count = sum(1 for item in results if item["status"] == "exported")
    skipped_count = sum(1 for item in results if item["status"] == "skipped")
    return {
        "atlas_path": str(atlas_path),
        "atlas_size": {"width": atlas_width, "height": atlas_height},
        "exported_slice_count": exported_count,
        "skipped_slice_count": skipped_count,
        "failed_slice_count": 0,
        "slices": results,
    }


def _write_result_manifest(result: dict[str, Any], manifest_path: Path) -> None:
    """写入切图结果 manifest。"""
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _create_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。"""
    parser = argparse.ArgumentParser(description="Slice a UI-only atlas according to atlas config.")
    parser.add_argument("--config", required=True, help="Atlas slicing config JSON path.")
    parser.add_argument(
        "--manifest-out",
        help="Optional explicit result manifest path. Defaults to <output_dir>/slice-result.json.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing slice outputs.")
    parser.add_argument("--dry-run", action="store_true", help="Only validate config and print summary.")
    return parser


def main() -> int:
    """执行脚本主流程。"""
    args = _create_parser().parse_args()
    config_path = Path(args.config)
    config = _load_config(config_path)

    atlas_path = Path(_require_string(config, "atlas_path"))
    output_dir = Path(_require_string(config, "output_dir"))
    slices = _require_slices(config)

    if args.dry_run:
        summary = {
            "atlas_path": str(atlas_path),
            "output_dir": str(output_dir),
            "slice_count": len(slices),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    result = _slice_atlas(
        atlas_path=atlas_path,
        output_dir=output_dir,
        slices=slices,
        overwrite=args.overwrite,
    )

    manifest_out = Path(args.manifest_out) if args.manifest_out else output_dir / "slice-result.json"
    _write_result_manifest(result, manifest_out)
    print(json.dumps({"manifest_path": str(manifest_out), **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
