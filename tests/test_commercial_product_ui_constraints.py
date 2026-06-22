"""验证商业产品 UI 的少字与视觉优先约束已写入工作流文档。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATOR_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "hard-rules.md"
DESIGN_GUIDANCE = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "design-quality-guidance.md"
ROUTING_RULES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "routing-rules.md"
WORKFLOW_RECORD_CONTRACT = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "workflow-record-contract.md"

ORCHESTRATOR_SNIPPETS = [
    "Commercial Product UI Constraint",
    "users scan, recognize, and act",
    "copy-compression check",
    "If all long explanatory copy disappeared",
]

COMMERCIAL_GATE_SNIPPETS = [
    "Commercial Product Surface Gate",
    "commercial_surface_gate",
    "first_screen_task_recognition",
    "primary_cta_dominance",
    "real_control_density",
    "reference_decision_inheritance",
    "revision_required",
]

COMMERCIAL_EXPLORATION_SNIPPETS = [
    "Commercial Design Exploration Window",
    "wide-before-freeze, narrow-after-freeze",
    "structure_recomposition_allowed",
    "direction_space_open",
    "freeze_boundary",
]

MOBBIN_STYLE_SNIPPETS = [
    "mandatory_mobbin_reference",
    "fixed_style_direction",
    "strong_hierarchy_contract",
    "style_single_source",
    "hierarchy_contrast_ladder",
]

MINIMAL_COPY_SNIPPETS = [
    "minimal_default_copy_contract",
    "explanatory_copy_budget",
    "one short helper line",
    "move explanation behind disclosure",
    "explanation_overload",
]

HARD_RULE_SNIPPETS = [
    "Do not allow first-screen product UI to depend on long explanatory copy",
    "Do not freeze a settings, dashboard, utility, or task surface if its primary understanding requires reading multiple descriptive text blocks.",
    "Do not keep subtitle, row-description, notice-card, and support-copy layers simultaneously when they repeat the same meaning.",
]

ROUTING_GATE_SNIPPETS = [
    "Do not accept a shared native HTML prototype",
    "Do not accept a generated representative sketch",
    "Do not accept a Pencil design source",
    "commercial_surface_gate.result=passed",
]

ROUTING_EXPLORATION_SNIPPETS = [
    "Do not lock the shared native HTML prototype",
    "commercial_design_exploration",
    "first-screen structure, module order, CTA placement",
    "After the exploration window closes",
]

ROUTING_MOBBIN_STYLE_SNIPPETS = [
    "Do not open commercial design exploration",
    "mandatory_mobbin_reference.status=complete",
    "fixed_style_direction.status=selected",
    "strong_hierarchy_contract.status=recorded",
]

ROUTING_MINIMAL_COPY_SNIPPETS = [
    "minimal_default_copy_contract.status=passed",
    "explanatory_copy_budget",
    "explanation_overload",
]

WORKFLOW_RECORD_SNIPPETS = [
    "commercial_surface_gate",
    "gate_owner",
    "failed_dimensions",
    "revision_target",
    "recorded before any downstream promotion",
]

WORKFLOW_EXPLORATION_RECORD_SNIPPETS = [
    "commercial_design_exploration",
    "selected_direction",
    "structure_recomposition_decisions",
    "freeze_boundary",
]

WORKFLOW_MOBBIN_STYLE_RECORD_SNIPPETS = [
    "mandatory_mobbin_reference",
    "reference_screen_evidence",
    "fixed_style_direction",
    "strong_hierarchy_contract",
    "hierarchy_contrast_ladder",
]

WORKFLOW_MINIMAL_COPY_RECORD_SNIPPETS = [
    "minimal_default_copy_contract",
    "explanatory_copy_budget",
    "visible_explanation_count",
    "disclosure_destination",
    "explanation_overload",
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

    def test_orchestrator_defines_commercial_surface_gate(self) -> None:
        """编排器必须定义可记录、可失败、可返工的商业产品界面门禁。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in COMMERCIAL_GATE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_orchestrator_defines_commercial_design_exploration_window(self) -> None:
        """编排器必须明确冻结前给足商业化设计探索空间，冻结后再收紧。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in COMMERCIAL_EXPLORATION_SNIPPETS:
            self.assertIn(snippet, content)

    def test_orchestrator_requires_mobbin_fixed_style_and_strong_hierarchy(self) -> None:
        """编排器必须把 Mobbin 参考、固定风格和强层次感作为设计前置约束。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in MOBBIN_STYLE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_orchestrator_limits_explanatory_copy_by_default(self) -> None:
        """编排器必须限制默认界面解释性文案数量。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in MINIMAL_COPY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_blocks_key_design_outputs_without_gate_pass(self) -> None:
        """关键设计产物没有通过商业产品界面门禁时不得继续下游流程。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_GATE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_keeps_design_space_open_before_html_lock(self) -> None:
        """路由规则必须在 HTML 原型锁定前保留商业化结构重组空间。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_EXPLORATION_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_blocks_design_without_mobbin_style_and_hierarchy(self) -> None:
        """路由规则必须阻断缺少 Mobbin、固定风格或强层次合同的设计推进。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_MOBBIN_STYLE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_blocks_explanation_overload(self) -> None:
        """路由规则必须阻断默认界面解释性文案过载。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_MINIMAL_COPY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_record_tracks_commercial_surface_gate_result(self) -> None:
        """工作流记录必须保存商业产品界面门禁结果和返工目标。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_RECORD_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_record_tracks_commercial_exploration_decisions(self) -> None:
        """工作流记录必须保存商业化探索选择和冻结边界。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_EXPLORATION_RECORD_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_record_tracks_mobbin_style_and_hierarchy_contracts(self) -> None:
        """工作流记录必须保存 Mobbin 证据、固定风格和强层次合同。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_MOBBIN_STYLE_RECORD_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_record_tracks_minimal_default_copy_contract(self) -> None:
        """工作流记录必须保存默认界面的少解释文案合同。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_MINIMAL_COPY_RECORD_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
