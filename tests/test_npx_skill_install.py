"""验证 npx 安装器会把 skills 安装到当前目录的 .agents/skills。"""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS_ROOT = REPO_ROOT / "skills"
NPX_COMMAND = "npx.cmd"


class NpxSkillInstallTest(unittest.TestCase):
    """验证本仓库可以作为 npx 安装器使用。"""

    def test_npx_install_copies_skills_to_current_directory(self) -> None:
        """npx 安装后，当前目录应生成完整的 .agents/skills 副本。"""
        with tempfile.TemporaryDirectory() as temp_dir:
            target_root = Path(temp_dir)

            subprocess.run(
                [
                    NPX_COMMAND,
                    "--yes",
                    "--package",
                    f"file:{REPO_ROOT}",
                    "flutter-skills",
                    "install",
                ],
                cwd=str(target_root),
                check=True,
            )

            installed_skills_root = target_root / ".agents" / "skills"
            source_skill_names = sorted(
                path.name for path in SOURCE_SKILLS_ROOT.iterdir() if path.is_dir()
            )
            installed_skill_names = sorted(
                path.name for path in installed_skills_root.iterdir() if path.is_dir()
            )

            self.assertEqual(source_skill_names, installed_skill_names)
            self.assertTrue((installed_skills_root / source_skill_names[0] / "SKILL.md").is_file())

    def test_npx_install_overwrites_same_skill_without_deleting_custom_entries(self) -> None:
        """更新安装时应覆盖同名 skill，但保留目标目录里的自定义内容。"""
        with tempfile.TemporaryDirectory() as temp_dir:
            target_root = Path(temp_dir)

            subprocess.run(
                [
                    NPX_COMMAND,
                    "--yes",
                    "--package",
                    f"file:{REPO_ROOT}",
                    "flutter-skills",
                    "install",
                ],
                cwd=str(target_root),
                check=True,
            )

            installed_skills_root = target_root / ".agents" / "skills"
            source_skill_dir = next(path for path in SOURCE_SKILLS_ROOT.iterdir() if path.is_dir())
            source_skill_file = source_skill_dir / "SKILL.md"
            installed_skill_file = installed_skills_root / source_skill_dir.name / "SKILL.md"
            custom_skill_file = installed_skills_root / "custom-skill" / "SKILL.md"

            custom_skill_file.parent.mkdir(parents=True, exist_ok=True)
            custom_skill_file.write_text("custom content\n", encoding="utf-8")
            # 先写入过期内容，验证二次安装会恢复成仓库内最新版本。
            installed_skill_file.write_text("stale content\n", encoding="utf-8")

            subprocess.run(
                [
                    NPX_COMMAND,
                    "--yes",
                    "--package",
                    f"file:{REPO_ROOT}",
                    "flutter-skills",
                    "install",
                ],
                cwd=str(target_root),
                check=True,
            )

            self.assertEqual(
                source_skill_file.read_text(encoding="utf-8"),
                installed_skill_file.read_text(encoding="utf-8"),
            )
            self.assertEqual("custom content\n", custom_skill_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
