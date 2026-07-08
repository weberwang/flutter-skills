"""验证高质量品牌视觉提示词的公共部分已沉淀为工作流可复用约束。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DESIGN_GUIDANCE = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "design-quality-guidance.md"
DESIGN_TEMPLATE = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "design-md-template.md"
README = REPO_ROOT / "README.md"

DESIGN_GUIDANCE_SNIPPETS = [
    "Brand Visual World Extraction",
    "playful energy and premium creative-tech polish",
    "high-saturation bright color",
    "clean geometric form",
    "modern typography system",
    "dynamic visual rhythm",
    "light surreal image posture",
    "product obsession",
    "visual experimentation",
    "packaging exploration",
    "editorial photography",
    "immersive retail",
    "cross-platform brand application",
]

DESIGN_TEMPLATE_SNIPPETS = [
    "## Brand Visual World",
    "brand_world_prompt_packet",
    "core_tension",
    "playful_premium_balance",
    "visual_language",
    "world_building_surfaces",
    "approachable_but_art_directed",
]

README_SNIPPETS = [
    "高质量品牌视觉提示词应先抽取公共品牌世界约束",
    "不要把品牌稿件里的项目私有名词直接硬编码到下游工作流",
]


class BrandVisualPromptReuseTest(unittest.TestCase):
    """验证品牌视觉提示词的公共层已经可复用。"""

    def test_design_guidance_contains_reusable_brand_visual_world_rules(self) -> None:
        """设计指引必须收敛通用品牌视觉世界约束。"""
        content = DESIGN_GUIDANCE.read_text(encoding="utf-8")
        for snippet in DESIGN_GUIDANCE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_design_template_exposes_brand_visual_world_packet(self) -> None:
        """DESIGN 模板必须暴露品牌视觉世界包结构。"""
        content = DESIGN_TEMPLATE.read_text(encoding="utf-8")
        for snippet in DESIGN_TEMPLATE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_readme_mentions_prompt_reuse_rule(self) -> None:
        """README 必须给协作者写明品牌提示词复用原则。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
