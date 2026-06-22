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
WORKFLOW_STATES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "workflow-states.md"
EXECUTION_MODES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "execution-modes.md"
CREATIVE_PRODUCTION_BRANCH = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "creative-production-branch.md"
ASSET_ATLAS_FLOW = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "asset-atlas-flow.md"
FLUTTER_UIUX_TO_ARCHITECTURE = REPO_ROOT / "skills" / "flutter-uiux-to-architecture" / "SKILL.md"

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

GLOBAL_STYLE_ONLY_SNIPPETS = [
    "Global Style-Only Design Boundary",
    "global_style_scheme",
    "global_style_experience_image",
    "Product Design:ideate",
    "theme_and_style_only",
    "no_global_page_design_draft",
    "non_page_design_evidence",
    "page_design_deferred_to_module_stage",
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

HARD_RULE_GLOBAL_STYLE_ONLY_SNIPPETS = [
    "Do not generate shared/global representative page sketches",
    "global_style_experience_image",
    "non_page_design_evidence=true",
    "global_style_scheme.status=selected",
    "theme_and_style_only=true",
    "no_global_page_design_draft",
    "page_design_deferred_to_module_stage=true",
    "Module effect images are mandatory",
]

PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS = [
    "`shared_design_direction` / `design_recommendation_ready` -> `Product Design:ideate`",
    "global_style_experience_image",
    "module representative sketch",
    "module final effect image",
    "select or revise a Product Design-generated candidate",
    "$imagegen` background removal",
]

HARD_RULE_PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS = [
    "Do not bypass `@product-design` visual ideation",
    "global_style_experience_image",
    "module representative sketch",
    "module final effect image direction",
    "Do not generate the module final effect image through `gpt-image-2-generator`",
    "Do not use `@product-design` as a replacement for atlas background-removal",
    "deterministic runtime asset preparation",
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

ROUTING_GLOBAL_STYLE_ONLY_SNIPPETS = [
    "Do not generate global page design drafts",
    "global_style_experience_image",
    "non_page_design_evidence=true",
    "global_style_scheme.status=selected",
    "theme_and_style_only=true",
    "page_design_deferred_to_module_stage=true",
    "Global design may define theme tokens",
]

ROUTING_PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS = [
    "route the shared/global scope to `Product Design:ideate`",
    "`global_style_experience_image` through `Product Design:ideate`",
    "route the module representative sketch to `Product Design:ideate`",
    "route the module final effect-image direction pass to `Product Design:ideate`",
    "select or revise a Product Design-generated candidate",
    "keep atlas background removal plus slicing on the deterministic asset path",
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

WORKFLOW_GLOBAL_STYLE_ONLY_RECORD_SNIPPETS = [
    "global_style_scheme",
    "global_style_experience_image",
    "theme_style_scope",
    "theme_and_style_only",
    "non_page_design_evidence",
    "no_global_page_design_draft",
    "page_design_deferred_to_module_stage",
]

WORKFLOW_STATE_GLOBAL_STYLE_ONLY_SNIPPETS = [
    "global_style_scheme.status=selected",
    "global_style_experience_image",
    "theme_and_style_only=true",
    "no_global_page_design_draft=true",
    "non_page_design_evidence=true",
    "page_design_deferred_to_module_stage=true",
    "Global effect-image states are legacy-only",
    "not page design evidence",
]

WORKFLOW_MINIMAL_COPY_RECORD_SNIPPETS = [
    "minimal_default_copy_contract",
    "explanatory_copy_budget",
    "visible_explanation_count",
    "disclosure_destination",
    "explanation_overload",
]

MANUAL_IMAGE_REVIEW_SNIPPETS = [
    "manual image review",
    "human review result",
    "user confirmation or revision feedback",
]

GUIDANCE_SNIPPETS = [
    "recognition over explanation",
    "visual state over descriptive paragraphs",
    "progressive disclosure over always-visible explanation",
    "first screenful",
]

WHOLE_IMAGE_ELEMENT_SNIPPETS = [
    "semantically unified visual unit",
    "one whole asset",
    "multiple decorative fragments",
    "shared silhouette, texture, lighting, and hierarchy",
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

    def test_hard_rules_keep_global_design_style_only(self) -> None:
        """硬规则必须阻止全局阶段重新进入页面级设计稿链路。"""
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_GLOBAL_STYLE_ONLY_SNIPPETS:
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

    def test_orchestrator_limits_global_design_to_theme_and_style_scheme(self) -> None:
        """编排器必须阻止全局阶段产出页面设计稿，只允许冻结主题和风格方案。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in GLOBAL_STYLE_ONLY_SNIPPETS:
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

    def test_routing_blocks_global_page_design_drafts(self) -> None:
        """路由规则必须把全局设计限制为主题和风格方案，不生成页面级设计稿。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_GLOBAL_STYLE_ONLY_SNIPPETS:
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

    def test_workflow_record_tracks_global_style_only_boundary(self) -> None:
        """工作流记录必须保存全局只定主题和风格方案的边界。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_GLOBAL_STYLE_ONLY_RECORD_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_states_keep_global_design_style_only(self) -> None:
        """状态表必须把全局设计定义为风格方案，而不是页面稿链路。"""
        content = WORKFLOW_STATES.read_text(encoding="utf-8")
        for snippet in WORKFLOW_STATE_GLOBAL_STYLE_ONLY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_record_tracks_minimal_default_copy_contract(self) -> None:
        """工作流记录必须保存默认界面的少解释文案合同。"""
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in WORKFLOW_MINIMAL_COPY_RECORD_SNIPPETS:
            self.assertIn(snippet, content)


    def test_hard_rules_split_product_design_from_runtime_asset_chain(self) -> None:
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_orchestrator_prefers_product_design_for_direction_images(self) -> None:
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_uses_product_design_for_direction_images_only(self) -> None:
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_PRODUCT_DESIGN_IMAGE_POLICY_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_skill_removes_old_generator_assignment_for_direction_images(self) -> None:
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        self.assertIn("Pre-confirmation module representative sketches should go through `Product Design:ideate`", content)
        self.assertIn("select or revise a Product Design-generated candidate", content)
        self.assertNotIn("Representative sketch requests must go through local `$imagegen`", content)
        self.assertNotIn("before calling `gpt-image-2-generator`", content)
        self.assertNotIn("If `gpt-image-2-generator` or its required environment cannot generate the required final effect images", content)

    def test_execution_modes_follow_product_design_for_direction_images(self) -> None:
        content = EXECUTION_MODES.read_text(encoding="utf-8")
        self.assertIn("generate it through `Product Design:ideate`", content)
        self.assertIn("Product Design-owned final effect-image direction pass", content)
        self.assertIn("select or revise the Product Design-generated candidate", content)
        self.assertNotIn("generate the representative sketch through local `$imagegen`", content)
        self.assertNotIn("generate the required final effect images through `gpt-image-2-generator`", content)

    def test_creative_production_branch_no_longer_assigns_direction_images_to_legacy_generators(self) -> None:
        content = CREATIVE_PRODUCTION_BRANCH.read_text(encoding="utf-8")
        self.assertIn("Product Design:ideate owns the pre-confirmation sketch stage", content)
        self.assertIn("Product Design-owned final effect-image direction pass", content)
        self.assertNotIn("local `$imagegen` owns the pre-confirmation sketch stage", content)
        self.assertNotIn("`gpt-image-2-generator` owns the post-confirmation final image stage", content)

    def test_workflow_record_contract_tracks_new_direction_image_path(self) -> None:
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        self.assertIn("representative Product Design sketch exists when required", content)
        self.assertIn("selected final effect-image direction path was actually available", content)
        self.assertIn("selected Product Design candidate", content)
        self.assertNotIn("representative local `$imagegen` sketch exists when required", content)
        self.assertNotIn("`gpt-image-2-generator` for that branch was actually available", content)

    def test_generated_images_no_longer_require_product_design_qa_pass(self) -> None:
        orchestrator = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        routing = ROUTING_RULES.read_text(encoding="utf-8")
        record = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        for snippet in MANUAL_IMAGE_REVIEW_SNIPPETS:
            self.assertIn(snippet, orchestrator + routing + record)
        self.assertNotIn("automatic `@product-design` QA pass against the active brief and frozen visual constraints", orchestrator)
        self.assertNotIn("run one automatic `@product-design` QA pass", routing)
        self.assertNotIn("one automatic `@product-design` QA pass also ran for that image", record)

    def test_asset_and_architecture_rules_preserve_whole_image_elements(self) -> None:
        atlas_flow = ASSET_ATLAS_FLOW.read_text(encoding="utf-8")
        architecture = FLUTTER_UIUX_TO_ARCHITECTURE.read_text(encoding="utf-8")
        hard_rules = HARD_RULES.read_text(encoding="utf-8")
        combined = atlas_flow + architecture + hard_rules
        for snippet in WHOLE_IMAGE_ELEMENT_SNIPPETS:
            self.assertIn(snippet, combined)


if __name__ == "__main__":
    unittest.main()
