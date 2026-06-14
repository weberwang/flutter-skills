"""验证 Riverpod 最小范围监听规则已写入关键技能文档。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GUARDRAILS_SKILL = REPO_ROOT / "skills" / "flutter-project-guardrails" / "SKILL.md"
FLUTTER_DEV_TEMPLATE_SKILL = (
    REPO_ROOT / "skills" / "flutter-init" / "assets" / "flutter-dev-template" / "SKILL.md"
)
EXPECTED_SNIPPETS = [
    "smallest watch scope",
    "refresh only the widget subtree",
    "instead of rebuilding the whole page",
]


class RiverpodBestPracticesTest(unittest.TestCase):
    """验证 Riverpod 局部刷新规则不会从主技能和模板技能中丢失。"""

    def test_guardrails_skill_mentions_small_watch_scope(self) -> None:
        """主 guardrails skill 必须包含最小范围监听刷新规则。"""
        content = GUARDRAILS_SKILL.read_text(encoding="utf-8")
        for snippet in EXPECTED_SNIPPETS:
            self.assertIn(snippet, content)

    def test_flutter_dev_template_mentions_small_watch_scope(self) -> None:
        """生成出来的 flutter-dev 模板也必须继承相同规则。"""
        content = FLUTTER_DEV_TEMPLATE_SKILL.read_text(encoding="utf-8")
        for snippet in EXPECTED_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
