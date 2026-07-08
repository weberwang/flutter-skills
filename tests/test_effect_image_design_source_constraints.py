"""验证效果图作为设计稿与切图唯一视觉输入源的约束不会漂移。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
WORKFLOW_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "hard-rules.md"
DESIGN_GUIDANCE = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "design-quality-guidance.md"
EFFECT_IMAGE_TO_PENCIL = REPO_ROOT / "skills" / "effect-image-to-pencil-design" / "SKILL.md"
EFFECT_IMAGE_TO_ATLAS = REPO_ROOT / "skills" / "effect-image-to-ui-sheet-atlas" / "SKILL.md"

README_SNIPPETS = [
    "效果图是后续设计稿生成与分层切图的唯一视觉输入源",
    "拒绝飞机稿",
    "拒绝广告营销化表达",
    "后续会用于正式产品资源切图",
]

WORKFLOW_SKILL_SNIPPETS = [
    "effect-image-backed design execution",
    "the approved effect image is the only visual input source",
    "later atlas preparation and design-file generation",
]

HARD_RULE_SNIPPETS = [
    "Do not treat ad creative, marketing compositions, or flighty concept mock output as valid product effect-image evidence.",
    "Do not keep decorative detail in a product effect image when it adds no functional value, no hierarchy value, and no brand value.",
    "Every accepted decorative treatment in a product effect image must strengthen function recognition, hierarchy separation, brand memory, or state feedback.",
    "Do not replace an approved effect-image-backed design route with prototype screenshots or speculative redesign input.",
]

DESIGN_GUIDANCE_SNIPPETS = [
    "flighty concept mock treatment",
    "If an image feels flashy before it feels shippable as a product screen, reject it.",
    "visual experience must still serve product-task clarity",
    "Reject decorative detail that has no functional, hierarchical, or brand value.",
    "strengthen functional recognition",
    "strengthen hierarchy separation",
    "strengthen brand memory",
    "strengthen state feedback",
    "treat it as invalid decoration and remove it",
]

PENCIL_SKILL_SNIPPETS = [
    "Treat the approved effect image as the only visual input source for later design-file generation on this route.",
    "Do not fill missing layout, style, or asset decisions from prototype screenshots, ad references, or marketing redraws.",
]

ATLAS_SKILL_SNIPPETS = [
    "The approved effect image remains the only visual slicing-source baseline for this atlas route.",
    "The atlas outputs are expected to be cut and used in the shipped product, so every cell must stay faithful to the approved effect image.",
]


class EffectImageDesignSourceConstraintsTest(unittest.TestCase):
    """验证效果图链路不会漂移成广告稿或多输入拼接。"""

    def test_readme_explains_effect_image_as_only_visual_input(self) -> None:
        """README 必须给协作者写清效果图链路的新口径。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_skill_locks_effect_image_backed_visual_input(self) -> None:
        """工作流主技能必须声明效果图链路只有一个视觉输入源。"""
        content = WORKFLOW_SKILL.read_text(encoding="utf-8")
        for snippet in WORKFLOW_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_hard_rules_block_marketing_or_speculative_image_inputs(self) -> None:
        """硬规则必须阻断广告化和投机式视觉输入。"""
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_design_guidance_rejects_flashy_non_product_images(self) -> None:
        """设计指引必须要求视觉体验服务产品体验。"""
        content = DESIGN_GUIDANCE.read_text(encoding="utf-8")
        for snippet in DESIGN_GUIDANCE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_pencil_skill_uses_effect_image_as_only_visual_input(self) -> None:
        """Pencil 设计源技能必须把效果图当成唯一视觉输入源。"""
        content = EFFECT_IMAGE_TO_PENCIL.read_text(encoding="utf-8")
        for snippet in PENCIL_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_atlas_skill_keeps_effect_image_as_product_slicing_baseline(self) -> None:
        """atlas 技能必须声明切图基线只能来自批准效果图。"""
        content = EFFECT_IMAGE_TO_ATLAS.read_text(encoding="utf-8")
        for snippet in ATLAS_SKILL_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
