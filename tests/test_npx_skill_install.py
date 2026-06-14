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


if __name__ == "__main__":
    unittest.main()
