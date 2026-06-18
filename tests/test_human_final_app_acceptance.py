"""验证应用页面最终验收必须由人工放在工作流最后一步。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_STATES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "workflow-states.md"
ROUTING_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "routing-rules.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "hard-rules.md"
README = REPO_ROOT / "README.md"

WORKFLOW_STATE_SNIPPETS = [
    "final app-page acceptance must happen only at the end",
    "human visual inspection remains the final acceptance owner",
]

ROUTING_RULE_SNIPPETS = [
    "Do not treat `@product-design` `design-qa` as final acceptance of an app page.",
    "The final acceptance of app pages must happen only at the end of the workflow and only through explicit human visual inspection.",
]

HARD_RULE_SNIPPETS = [
    "Do not let any automatic helper, including `@product-design` `design-qa`, close final app-page acceptance by itself.",
    "Do not mark a module as fully accepted before the final human visual inspection step at the end of the workflow.",
]

README_SNIPPETS = [
    "最终验收",
    "人工验收",
]


class HumanFinalAppAcceptanceTest(unittest.TestCase):
    """验证应用页面最终验收的所有权与时序不会漂移。"""

    def test_workflow_states_mentions_human_final_acceptance(self) -> None:
        """状态机文档必须声明最终验收只在最后且由人工完成。"""
        content = WORKFLOW_STATES.read_text(encoding="utf-8")
        for snippet in WORKFLOW_STATE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_rules_block_non_human_final_acceptance(self) -> None:
        """路由规则必须阻断自动 helper 直接关闭最终验收。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_hard_rules_require_human_final_acceptance(self) -> None:
        """硬规则必须把最终验收归给人工。"""
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_readme_mentions_human_final_acceptance(self) -> None:
        """README 也应保留中文说明，方便协作对齐。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
