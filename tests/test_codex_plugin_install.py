"""验证 Codex 插件封装与本地安装脚本的最小冒烟测试。"""

from __future__ import annotations

import json
import subprocess
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "flutter-skills"
PLUGIN_MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_MANIFEST = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
INSTALL_SCRIPT = REPO_ROOT / "scripts" / "install-codex-plugin.ps1"
SOURCE_SKILLS_ROOT = REPO_ROOT / "skills"


class CodexPluginInstallTest(unittest.TestCase):
    """验证仓库是否具备可安装的 Codex 插件骨架。"""

    def test_plugin_files_exist(self) -> None:
        """插件清单、市场清单与安装脚本都必须存在。"""
        self.assertTrue(PLUGIN_MANIFEST.is_file(), "缺少插件清单 plugin.json")
        self.assertTrue(MARKETPLACE_MANIFEST.is_file(), "缺少 marketplace.json")
        self.assertTrue(INSTALL_SCRIPT.is_file(), "缺少安装脚本 install-codex-plugin.ps1")

    def test_install_script_syncs_skills(self) -> None:
        """安装脚本应把源码 skills 同步到插件目录。"""
        subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(INSTALL_SCRIPT),
                "-SkipCodexInstall",
            ],
            cwd=str(REPO_ROOT),
            check=True,
        )

        source_skill_names = sorted(
            path.name for path in SOURCE_SKILLS_ROOT.iterdir() if path.is_dir()
        )
        plugin_skills_root = PLUGIN_ROOT / "skills"
        plugin_skill_names = sorted(
            path.name for path in plugin_skills_root.iterdir() if path.is_dir()
        )

        self.assertEqual(source_skill_names, plugin_skill_names)
        self.assertTrue((plugin_skills_root / source_skill_names[0] / "SKILL.md").is_file())

    def test_marketplace_points_to_plugin(self) -> None:
        """市场清单必须暴露 flutter-skills 插件入口。"""
        payload = json.loads(MARKETPLACE_MANIFEST.read_text(encoding="utf-8"))
        plugin_entry = next(
            (item for item in payload.get("plugins", []) if item.get("name") == "flutter-skills"),
            None,
        )
        self.assertIsNotNone(plugin_entry, "marketplace.json 未注册 flutter-skills")
        self.assertEqual(
            plugin_entry["source"]["path"],
            "./plugins/flutter-skills",
        )


if __name__ == "__main__":
    unittest.main()
