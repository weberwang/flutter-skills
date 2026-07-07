"""验证工作流减少确认环节的收敛规则不会漂移。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
EXECUTION_MODES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "execution-modes.md"
CONTROL_CONTRACTS = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "control-contracts.md"
PRESSURE_SCENARIOS = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "pressure-scenarios.md"
README = REPO_ROOT / "README.md"

WORKFLOW_SKILL_SNIPPETS = [
    "minimize confirmation churn",
    "do not ask the user to reconfirm the same deterministic downstream default",
]

EXECUTION_MODE_SNIPPETS = [
    "confirmation-minimization policy",
    "do not stop for a second confirmation that only repeats an already-frozen upstream decision",
    "collapse deterministic review gates into the same auto-advance loop",
    "first module final effect-image review when one validated default remains",
]

CONTROL_CONTRACT_SNIPPETS = [
    "Do not create a fresh human confirmation gate when the user already approved the only supported upstream direction and the new artifact only proves that deterministic route.",
    "Collapse stacked confirmations into one human decision when the later confirmations would not unlock any alternate downstream route.",
    "Keep human confirmation only for true branch selection, unresolved reuse ambiguity, external project binding, or final human visual acceptance.",
]

PRESSURE_SCENARIO_SNIPPETS = [
    'User says "reduce confirmation churn after the main direction is already approved": allow.',
    "Collapse follow-up review prompts when they only restate the same deterministic downstream default.",
    "Keep stopping only for real branch choice, external project binding, reuse ambiguity, or final human acceptance.",
]

README_SNIPPETS = [
    "尽量把多个连续确认收敛成一个真正需要你拍板的确认",
    "`--full-auto` 会继续自动吃掉“只剩一个默认选项”的人工门禁",
    "仍然必须停下的确认只有：方向分叉、Stitch 项目绑定、candidate_reuse、最终人工验收",
]


class WorkflowConfirmationOptimizationTest(unittest.TestCase):
    """验证减少确认环节时仍保留关键人工门禁。"""

    def test_workflow_skill_declares_confirmation_minimization_goal(self) -> None:
        """主技能文档必须声明减少重复确认的目标。"""
        content = WORKFLOW_SKILL.read_text(encoding="utf-8")
        for snippet in WORKFLOW_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_execution_modes_define_confirmation_minimization_policy(self) -> None:
        """执行模式文档必须定义如何自动消化重复确认。"""
        content = EXECUTION_MODES.read_text(encoding="utf-8")
        for snippet in EXECUTION_MODE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_control_contracts_limit_human_confirmation_to_real_choices(self) -> None:
        """控制合同必须限制人工确认只出现在真实分支决策上。"""
        content = CONTROL_CONTRACTS.read_text(encoding="utf-8")
        for snippet in CONTROL_CONTRACT_SNIPPETS:
            self.assertIn(snippet, content)

    def test_pressure_scenarios_allow_reducing_redundant_confirmation(self) -> None:
        """压力场景文档必须允许减少重复确认。"""
        content = PRESSURE_SCENARIOS.read_text(encoding="utf-8")
        for snippet in PRESSURE_SCENARIO_SNIPPETS:
            self.assertIn(snippet, content)

    def test_readme_explains_remaining_human_gates(self) -> None:
        """README 必须对协作者说明哪些确认不能省。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
