"""验证商业产品 UI 的少字与视觉优先约束已写入工作流文档。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATOR_SKILL = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "SKILL.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "hard-rules.md"
DESIGN_GUIDANCE = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "design-quality-guidance.md"

ORCHESTRATOR_SNIPPETS = [
    "Commercial Product UI Constraint",
    "users scan, recognize, and act",
    "copy-compression check",
    "If all long explanatory copy disappeared",
]

HARD_RULE_SNIPPETS = [
    "Do not allow first-screen product UI to depend on long explanatory copy",
    "Do not freeze a settings, dashboard, utility, or task surface if its primary understanding requires reading multiple descriptive text blocks.",
    "Do not keep subtitle, row-description, notice-card, and support-copy layers simultaneously when they repeat the same meaning.",
]

GUIDANCE_SNIPPETS = [
    "recognition over explanation",
    "visual state over descriptive paragraphs",
    "progressive disclosure over always-visible explanation",
    "first screenful",
]


class CommercialProductUiConstraintsTest(unittest.TestCase):
    """验证商业产品 UI 约束不会从关键工作流文档中丢失。"""

    def test_orchestrator_mentions_commercial_ui_constraint(self) -> None:
        """编排器主文档必须声明商业产品 UI 的默认文案姿态。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in ORCHESTRATOR_SNIPPETS:
            self.assertIn(snippet, content)

    def test_hard_rules_block_explanatory_primary_surfaces(self) -> None:
        """硬规则必须阻断说明书式首屏和重复说明层。"""
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_design_guidance_mentions_commercial_copy_compression(self) -> None:
        """设计指引必须明确视觉优先、解释后置和首屏收口。"""
        content = DESIGN_GUIDANCE.read_text(encoding="utf-8")
        for snippet in GUIDANCE_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
