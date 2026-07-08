"""验证人工决策节点会先收到多个推荐选项。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
CONTROL_CONTRACTS = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "control-contracts.md"
PRESSURE_SCENARIOS = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "pressure-scenarios.md"
README = REPO_ROOT / "README.md"

WORKFLOW_SKILL_SNIPPETS = [
    "human decision nodes must receive multiple recommended options first",
    "one primary recommendation",
    "why each option fits or risks the PRD",
]

CONTROL_CONTRACT_SNIPPETS = [
    "Before asking for a human decision on direction, style, reference band, or restoration tradeoff, present 2-3 recommended options first.",
    "Every option should include fit reason, risk, and recommendation strength.",
    "When one option is clearly strongest, mark it as the default recommendation instead of asking the human to start from a blank slate.",
    "decision_topic",
    "recommended_options",
    "fit_reason",
    "risks",
    "default_recommendation",
    "human_action_required",
    "title",
    "summary",
    "recommendation_strength",
]

PRESSURE_SCENARIO_SNIPPETS = [
    'User says "you decide the style, I do not care": do not collapse to one opaque answer.',
    "Present 2-3 recommended options with one primary recommendation, then ask the user to confirm or merge.",
]

README_SNIPPETS = [
    "人工负责拍板，但工作流必须先给出多个推荐选择",
    "不要让人工从空白开始定义风格、品牌张力或状态视觉语言",
    "人工决策节点统一输出：decision_topic、recommended_options、fit_reason、risks、default_recommendation、human_action_required",
    "推荐项至少包含：id、title、summary、fit_reason、risks、recommendation_strength",
]


class HumanDecisionRecommendationsTest(unittest.TestCase):
    """验证人工拍板前有结构化推荐选项。"""

    def test_workflow_skill_requires_recommendation_set_before_human_choice(self) -> None:
        """主技能文档必须声明人工决策前先给推荐集合。"""
        content = WORKFLOW_SKILL.read_text(encoding="utf-8")
        for snippet in WORKFLOW_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_control_contracts_define_multi_option_human_decision_rule(self) -> None:
        """控制合同必须把人工决策节点定义成多推荐输入。"""
        content = CONTROL_CONTRACTS.read_text(encoding="utf-8")
        for snippet in CONTROL_CONTRACT_SNIPPETS:
            self.assertIn(snippet, content)

    def test_pressure_scenarios_block_blank_human_style_decision(self) -> None:
        """压力场景必须阻止把风格决策直接甩给人工从零开始想。"""
        content = PRESSURE_SCENARIOS.read_text(encoding="utf-8")
        for snippet in PRESSURE_SCENARIO_SNIPPETS:
            self.assertIn(snippet, content)

    def test_readme_explains_human_decision_recommendation_flow(self) -> None:
        """README 必须写明人工决策前的推荐机制。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
