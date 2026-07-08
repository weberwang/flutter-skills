#!/usr/bin/env python3
"""Create the project-local flutter-dev skill from the bundled template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Flutter project root")
    parser.add_argument(
        "--skills-dir",
        default=".",
        help="Directory under target where flutter-dev should be created",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    template = skill_dir / "assets" / "flutter-dev"
    if not template.exists():
        raise SystemExit(f"Missing template: {template}")

    target_root = Path(args.target).resolve()
    output_parent = (target_root / args.skills_dir).resolve()
    try:
        output_parent.relative_to(target_root)
    except ValueError:
        raise SystemExit("Refusing to write outside target project")

    output = output_parent / "flutter-dev"
    output.mkdir(parents=True, exist_ok=True)
    shutil.copy2(template / "SKILL.md", output / "SKILL.md")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
