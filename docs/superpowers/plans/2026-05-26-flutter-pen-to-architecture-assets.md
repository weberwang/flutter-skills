# flutter-pen-to-architecture Assets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 `flutter-pen-to-architecture` 增加图片资源导出能力，使其能优先从 `.pen` 提取图片、在必要时回退到 `Pencil MCP` 资源引用、导出到 Flutter 项目的 `assets/images/`、自动补齐 `pubspec.yaml` 资源声明，并把这些图片纳入最终还原方案。

**Architecture:** 保持现有 skill 主体不拆分，在其下新增两个独立脚本和一个新的参考文档。`export_pen_assets.py` 只负责资源提取与导出，`ensure_flutter_assets.py` 只负责 Flutter 资源声明接入；`SKILL.md` 与现有 references 负责把这两段能力接回原有的设计解构流程与输出契约。

**Tech Stack:** Python 3.12, `unittest`, `zipfile`, `base64`, Markdown skill files, YAML-like text patching for `pubspec.yaml`

---

### Task 1: 搭建脚本与测试骨架

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/export_pen_assets.py`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.py`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.py`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.py`

- [ ] **Step 1: 先写 `ensure_flutter_assets.py` 的失败测试**

```python
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "ensure_flutter_assets.py"


class EnsureFlutterAssetsCliTests(unittest.TestCase):
    def test_missing_pubspec_returns_non_zero(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", temp_dir],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("pubspec.yaml", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: 运行 `ensure_flutter_assets.py` 测试，确认当前失败**

Run:
```powershell
rtk python -m unittest "skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.py" -v
```
Expected: FAIL，提示 `ensure_flutter_assets.py` 尚不存在或命令返回不符合预期。

- [ ] **Step 3: 再写 `export_pen_assets.py` 的失败测试**

```python
import base64
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "export_pen_assets.py"
PNG_BYTES = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9WnWZJ4AAAAASUVORK5CYII="
)


class ExportPenAssetsCliTests(unittest.TestCase):
    def test_exports_image_from_pen_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pen_path = root / "sample.pen"
            project_root = root / "flutter_app"
            (project_root / "assets" / "images").mkdir(parents=True)
            with zipfile.ZipFile(pen_path, "w") as bundle:
                bundle.writestr("images/hero.png", PNG_BYTES)

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pen-file",
                    str(pen_path),
                    "--project-root",
                    str(project_root),
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((project_root / "assets" / "images" / "hero.png").exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 4: 运行 `export_pen_assets.py` 测试，确认当前失败**

Run:
```powershell
rtk python -m unittest "skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.py" -v
```
Expected: FAIL，提示 `export_pen_assets.py` 尚不存在或没有导出图片。

### Task 2: 实现 `ensure_flutter_assets.py`

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.py`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.py`

- [ ] **Step 1: 写入最小可运行版本的 `ensure_flutter_assets.py`**

```python
from __future__ import annotations

import argparse
import sys
from pathlib import Path


ASSET_ENTRY = "    - assets/images/\n"


def ensure_assets_declared(project_root: Path) -> tuple[bool, str]:
    pubspec_path = project_root / "pubspec.yaml"
    if not pubspec_path.exists():
        raise FileNotFoundError(f"pubspec.yaml not found under {project_root}")

    content = pubspec_path.read_text(encoding="utf-8")
    if "    - assets/images/\n" in content or "    - assets/images/\r\n" in content:
        return False, "assets/images/ already declared"

    if "flutter:\n" not in content:
        content = f"{content.rstrip()}\n\nflutter:\n  assets:\n{ASSET_ENTRY}"
    elif "  assets:\n" not in content:
        content = content.replace("flutter:\n", f"flutter:\n  assets:\n{ASSET_ENTRY}", 1)
    else:
        content = content.replace("  assets:\n", f"  assets:\n{ASSET_ENTRY}", 1)

    pubspec_path.write_text(content, encoding="utf-8")
    return True, "assets/images/ added"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()
    try:
        changed, message = ensure_assets_declared(Path(args.project_root))
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: 补充幂等测试**

```python
    def test_adds_assets_images_once(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pubspec = root / "pubspec.yaml"
            pubspec.write_text("name: demo\nflutter:\n  uses-material-design: true\n", encoding="utf-8")

            first = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", temp_dir],
                capture_output=True,
                text=True,
            )
            second = subprocess.run(
                [sys.executable, str(SCRIPT), "--project-root", temp_dir],
                capture_output=True,
                text=True,
            )

            content = pubspec.read_text(encoding="utf-8")
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(content.count("assets/images/"), 1)
```

- [ ] **Step 3: 运行 `ensure_flutter_assets.py` 测试，确认通过**

Run:
```powershell
rtk python -m unittest "skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.py" -v
```
Expected: PASS，至少 2 个测试通过。

### Task 3: 实现 `export_pen_assets.py`

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/export_pen_assets.py`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.py`

- [ ] **Step 1: 写入支持 `.pen` ZIP 提取的最小实现**

```python
from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}


def export_from_pen_archive(pen_file: Path, output_dir: Path) -> list[dict[str, str]]:
    exported: list[dict[str, str]] = []
    with zipfile.ZipFile(pen_file) as bundle:
        for member in bundle.infolist():
            suffix = Path(member.filename).suffix.lower()
            if member.is_dir() or suffix not in IMAGE_SUFFIXES:
                continue
            target = output_dir / Path(member.filename).name
            with bundle.open(member) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            exported.append(
                {
                    "source_id": member.filename,
                    "file_name": target.name,
                    "flutter_path": f"assets/images/{target.name}",
                    "source": ".pen",
                    "status": "exported",
                }
            )
    return exported


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pen-file", required=True)
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()

    pen_file = Path(args.pen_file)
    project_root = Path(args.project_root)
    if not pen_file.exists():
        print(f".pen file not found: {pen_file}", file=sys.stderr)
        return 1

    output_dir = project_root / "assets" / "images"
    output_dir.mkdir(parents=True, exist_ok=True)
    exported = export_from_pen_archive(pen_file, output_dir)
    if not exported:
        print("No exportable images found in .pen archive", file=sys.stderr)
        return 1
    print(json.dumps({"exported": exported}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: 补充 MCP 回退与覆盖测试**

```python
    def test_falls_back_to_mcp_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            pen_path = root / "empty.pen"
            project_root = root / "flutter_app"
            manifest_path = root / "mcp_assets.json"
            (project_root / "assets" / "images").mkdir(parents=True)
            with zipfile.ZipFile(pen_path, "w"):
                pass
            manifest_path.write_text(
                json.dumps(
                    {
                        "assets": [
                            {
                                "id": "hero-banner",
                                "file_name": "hero-banner.png",
                                "data_base64": base64.b64encode(PNG_BYTES).decode("ascii"),
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--pen-file",
                    str(pen_path),
                    "--project-root",
                    str(project_root),
                    "--mcp-assets",
                    str(manifest_path),
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((project_root / "assets" / "images" / "hero-banner.png").exists())
```

- [ ] **Step 3: 把 MCP 回退和覆盖逻辑补进脚本**

```python
import base64


def export_from_mcp_manifest(manifest_file: Path, output_dir: Path) -> list[dict[str, str]]:
    payload = json.loads(manifest_file.read_text(encoding="utf-8"))
    exported: list[dict[str, str]] = []
    for asset in payload.get("assets", []):
        target = output_dir / asset["file_name"]
        target.write_bytes(base64.b64decode(asset["data_base64"]))
        exported.append(
            {
                "source_id": asset["id"],
                "file_name": target.name,
                "flutter_path": f"assets/images/{target.name}",
                "source": "Pencil MCP",
                "status": "exported",
            }
        )
    return exported
```

并把 CLI 参数补成：

```python
    parser.add_argument("--mcp-assets")
```

以及主逻辑改成：

```python
    exported = export_from_pen_archive(pen_file, output_dir)
    if not exported and args.mcp_assets:
        exported = export_from_mcp_manifest(Path(args.mcp_assets), output_dir)
```

- [ ] **Step 4: 运行 `export_pen_assets.py` 测试，确认通过**

Run:
```powershell
rtk python -m unittest "skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.py" -v
```
Expected: PASS，至少 2 个测试通过，覆盖 `.pen` 提取与 MCP 回退。

### Task 4: 更新 skill 文档与引用关系

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/agents/openai.yaml`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/pen-input-contract.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/output-blueprint.md`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/asset-extraction-and-mapping.md`

- [ ] **Step 1: 更新 `SKILL.md` 的触发描述与主流程**

把 frontmatter `description` 扩成同时覆盖：

```md
description: Use when translating Pencil `.pen` design files or Pencil MCP structured output into a Flutter-oriented design architecture plan, especially when the task is to export image assets into a Flutter project, register `assets/images/` in `pubspec.yaml`, extract global design tokens, define light and dark themes, decompose reusable components, and decide what should be restored faithfully versus refactored to fit Flutter design philosophy instead of generating code directly.
```

并把 `Workflow` 调整为包含：

- `.pen` / MCP 输入识别
- 图片资源导出
- `pubspec.yaml` 资源接入
- 设计解构与还原消费

- [ ] **Step 2: 新增图片映射参考文档**

写入以下结构：

```md
# Asset Extraction And Mapping

## Purpose

Define which image resources should be exported, how they land in `assets/images/`, and how they should be consumed during Flutter restoration.

## Priority

1. `.pen` embedded assets
2. Pencil MCP manifest fallback

## Output Fields

- `原始资源标识`
- `导出文件`
- `Flutter 路径`
- `来源`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`
```

- [ ] **Step 3: 更新 `pen-input-contract.md` 与 `output-blueprint.md`**

要求至少补入：

```md
## Asset Fallback

- Prefer `.pen` embedded assets.
- Use Pencil MCP only when `.pen` does not provide enough exportable image data.
```

以及：

```md
## Additional Output Sections

1. `图片资源导出结果`
2. `图片资源映射表`
3. `Flutter 资源接入结果`
```

- [ ] **Step 4: 更新 `agents/openai.yaml`**

把 `short_description` 改成：

```yaml
short_description: "Export Pencil image assets and map them into Flutter restoration guidance"
```

把 `default_prompt` 改成：

```yaml
default_prompt: "Use $flutter-pen-to-architecture to export image assets from Pencil .pen files into a Flutter project's assets/images/, register the folder in pubspec.yaml, and fold those assets into Flutter-oriented restoration guidance with tokens, themes, reusable components, and fidelity-versus-Flutterization decisions."
```

### Task 5: 端到端验证与收尾

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/**`

- [ ] **Step 1: 跑脚本单测**

Run:
```powershell
rtk python -m unittest discover "skills/flutter-pen-to-architecture/scripts/tests" -v
```
Expected: PASS，`test_export_pen_assets.py` 与 `test_ensure_flutter_assets.py` 全部通过。

- [ ] **Step 2: 跑占位符扫描**

Run:
```powershell
@'
from pathlib import Path

root = Path("skills/flutter-pen-to-architecture")
patterns = ["TO" + "DO", "TB" + "D", "待补充", "占位", "implement" + " later"]
hits = []
for path in root.rglob("*"):
    if path.is_file():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in patterns:
            if pattern in text:
                hits.append(f"{path}: {pattern}")
if hits:
    raise SystemExit("\n".join(hits))
print("no-placeholders")
'@ | python -
```
Expected: 输出 `no-placeholders`。

- [ ] **Step 3: 做一次脚本级 smoke test**

Run:
```powershell
@'
import base64
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9WnWZJ4AAAAASUVORK5CYII=")
with tempfile.TemporaryDirectory() as temp_dir:
    root = Path(temp_dir)
    pen = root / "demo.pen"
    project = root / "demo_flutter"
    project.mkdir()
    (project / "pubspec.yaml").write_text("name: demo\nflutter:\n  uses-material-design: true\n", encoding="utf-8")
    with zipfile.ZipFile(pen, "w") as bundle:
        bundle.writestr("assets/cover.png", png)
    subprocess.run([sys.executable, "skills/flutter-pen-to-architecture/scripts/export_pen_assets.py", "--pen-file", str(pen), "--project-root", str(project)], check=True)
    subprocess.run([sys.executable, "skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.py", "--project-root", str(project)], check=True)
    assert (project / "assets" / "images" / "cover.png").exists()
    assert "assets/images/" in (project / "pubspec.yaml").read_text(encoding="utf-8")
print("smoke-ok")
'@ | python -
```
Expected: 输出 `smoke-ok`。

- [ ] **Step 4: 人工复核 spec 覆盖**

检查以下内容都能在最终改动中直接对应：

- 两个脚本存在且职责分离
- `assets/images/` 被注册到 `pubspec.yaml`
- `.pen` 优先、`Pencil MCP` 回退成立
- 输出蓝图新增图片导出与映射部分
- 同名文件覆盖行为被文档与脚本明确说明
