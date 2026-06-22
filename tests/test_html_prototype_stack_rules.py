"""验证 HTML 原型技术栈约束已写入关键工作流文档。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATOR_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
REFERENCE_TO_PROTOTYPE_SKILL = REPO_ROOT / "skills" / "reference-image-to-hifi-prototype" / "SKILL.md"
README = REPO_ROOT / "README.md"

EXPECTED_STACK_SNIPPETS = [
    "Vite + React + TypeScript",
    "Flutter restoration",
    "Vue",
    "HTML/CSS/JS",
]

REFERENCE_SKILL_SNIPPETS = [
    "Vite + React + TypeScript",
    "Do not default to Vue",
    "Do not default to plain HTML/CSS/JS",
]


class HtmlPrototypeStackRulesTest(unittest.TestCase):
    """验证 HTML 原型默认技术栈与取舍说明不会从文档中丢失。"""

    def test_orchestrator_mentions_default_html_prototype_stack(self) -> None:
        """编排器必须写明默认 HTML 原型技术栈与 Flutter 还原导向。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in EXPECTED_STACK_SNIPPETS:
            self.assertIn(snippet, content)

    def test_reference_image_skill_mentions_stack_defaults(self) -> None:
        """参考图转高保真原型技能必须写明推荐栈与禁用默认项。"""
        content = REFERENCE_TO_PROTOTYPE_SKILL.read_text(encoding="utf-8")
        for snippet in REFERENCE_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_readme_mentions_stack_comparison_guidance(self) -> None:
        """README 必须保留原型技术栈选择原则，方便后续协作对齐。"""
        content = README.read_text(encoding="utf-8")
        for snippet in EXPECTED_STACK_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
