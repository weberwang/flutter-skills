#!/usr/bin/env python3
"""在冻结页面副本上绘制位图候选框和数字编号。"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


PALETTE = (
    "#FF3B30",
    "#007AFF",
    "#34C759",
    "#FF9500",
    "#AF52DE",
    "#00A7A7",
)


def parse_args() -> argparse.Namespace:
    """解析输入图、区域映射和输出路径。"""
    parser = argparse.ArgumentParser(
        description="Render numbered bitmap candidate boxes on a copy of a frozen page image."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--regions", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def load_regions(path: Path, image_size: tuple[int, int]) -> list[dict[str, Any]]:
    """读取并验证编号区域，防止越界、缺号或非矩形数据进入确认图。"""
    payload = json.loads(path.read_text(encoding="utf-8"))
    regions = payload.get("regions")
    if not isinstance(regions, list) or not regions:
        raise ValueError("regions must be a non-empty list")

    width, height = image_size
    numbers: set[int] = set()
    validated: list[dict[str, Any]] = []
    for index, item in enumerate(regions):
        if not isinstance(item, dict):
            raise ValueError(f"regions[{index}] must be an object")

        number = item.get("number")
        bounds = item.get("bounds")
        if not isinstance(number, int) or number < 1:
            raise ValueError(f"regions[{index}].number must be a positive integer")
        if (
            not isinstance(bounds, list)
            or len(bounds) != 4
            or any(not isinstance(value, int) for value in bounds)
        ):
            raise ValueError(f"regions[{index}].bounds must be [x, y, width, height]")

        x, y, box_width, box_height = bounds
        if x < 0 or y < 0 or box_width < 1 or box_height < 1:
            raise ValueError(f"regions[{index}] has invalid bounds")
        if x + box_width > width or y + box_height > height:
            raise ValueError(f"regions[{index}] exceeds image bounds")

        color = item.get("color") or PALETTE[(number - 1) % len(PALETTE)]
        if not isinstance(color, str):
            raise ValueError(f"regions[{index}].color must be a CSS hex color")

        numbers.add(number)
        validated.append({"number": number, "bounds": bounds, "color": color})

    expected = set(range(1, max(numbers) + 1))
    if numbers != expected:
        raise ValueError("distinct region numbers must be sequential from 1 without gaps")
    return validated


def load_font(size: int) -> ImageFont.ImageFont:
    """优先使用粗体系统字体，缺失时退回 Pillow 默认字体。"""
    for candidate in ("arialbd.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def render_overlay(
    source: Image.Image, regions: list[dict[str, Any]]
) -> Image.Image:
    """在复制图层上绘制高对比边框和数字徽标，不改动输入图对象。"""
    output = source.convert("RGBA").copy()
    draw = ImageDraw.Draw(output)
    scale = max(1.0, min(output.size) / 390.0)
    outer_width = max(5, round(3 * scale))
    inner_width = max(3, round(2 * scale))
    radius = max(15, round(12 * scale))
    font = load_font(max(18, round(15 * scale)))

    for region in regions:
        number = region["number"]
        x, y, box_width, box_height = region["bounds"]
        color = region["color"]
        right = x + box_width - 1
        bottom = y + box_height - 1

        # 先绘制白色外沿，再绘制彩色内沿，保证深浅背景上均可辨认。
        draw.rectangle(
            (x, y, right, bottom), outline="white", width=outer_width
        )
        inset = outer_width
        if box_width > inset * 2 and box_height > inset * 2:
            draw.rectangle(
                (x + inset, y + inset, right - inset, bottom - inset),
                outline=color,
                width=inner_width,
            )

        center_x = min(max(x + radius, radius), output.width - radius)
        center_y = min(max(y + radius, radius), output.height - radius)
        draw.ellipse(
            (
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
            ),
            fill=color,
            outline="white",
            width=max(2, round(2 * scale)),
        )

        label = str(number)
        label_box = draw.textbbox((0, 0), label, font=font)
        label_width = label_box[2] - label_box[0]
        label_height = label_box[3] - label_box[1]
        draw.text(
            (
                center_x - label_width / 2,
                center_y - label_height / 2 - label_box[1],
            ),
            label,
            font=font,
            fill="white",
        )

    return output


def sha256(path: Path) -> str:
    """计算输出文件哈希，供确认版本和内部清单绑定。"""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    """验证输入后生成保持原尺寸的 PNG 确认图。"""
    args = parse_args()
    if args.input.resolve() == args.output.resolve():
        raise ValueError("output must not overwrite the frozen input image")

    with Image.open(args.input) as source:
        regions = load_regions(args.regions, source.size)
        overlay = render_overlay(source, regions)
        original_size = source.size

    args.output.parent.mkdir(parents=True, exist_ok=True)
    overlay.save(args.output, format="PNG", optimize=False)
    with Image.open(args.output) as rendered:
        if rendered.size != original_size:
            raise RuntimeError("rendered overlay dimensions changed unexpectedly")

    print(json.dumps({"output": str(args.output), "sha256": sha256(args.output)}))


if __name__ == "__main__":
    main()
