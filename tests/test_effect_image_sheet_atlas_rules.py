"""验证效果图伴生 UI-only 透明 atlas 规则不会从工作流文档中丢失。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
ORCHESTRATOR = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "SKILL.md"
ROUTING_RULES = (
    REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "routing-rules.md"
)
HARD_RULES = (
    REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "hard-rules.md"
)
ASSET_ATLAS_FLOW = (
    REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "asset-atlas-flow.md"
)
WORKFLOW_STATES = (
    REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "workflow-states.md"
)
CATALOG_CONTRACT = (
    REPO_ROOT
    / "skills"
    / "flutter-workflow-orchestrator"
    / "references"
    / "global-asset-catalog-contract.md"
)

README_SNIPPETS = [
    "sheet atlas",
    "透明背景",
    "只包含 UI 层",
]

ORCHESTRATOR_SNIPPETS = [
    "UI-only sheet atlas",
    "transparent background",
    "data_excluded_placeholder",
]

ROUTING_RULE_SNIPPETS = [
    "matching UI-only transparent atlas",
    "atlas manifest",
]

HARD_RULE_SNIPPETS = [
    "non-transparent atlas background",
    "runtime data layers into the atlas",
]

ASSET_ATLAS_FLOW_SNIPPETS = [
    "UI-only transparent sheet atlas",
    "runtime-data regions",
    "cut-ready manifest",
]

WORKFLOW_STATE_SNIPPETS = [
    "matching UI-only transparent atlas artifacts",
]

CATALOG_CONTRACT_SNIPPETS = [
    "sheet_atlas",
    "atlas_manifest",
]


class EffectImageSheetAtlasRulesTest(unittest.TestCase):
    """验证效果图伴生 atlas 的范围、透明背景和可切割约束。"""

    def test_readme_mentions_shared_and_module_sheet_atlas(self) -> None:
        """README 必须写明 atlas 的中文约束，方便协作时快速对齐。"""
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)

    def test_orchestrator_mentions_ui_only_transparent_atlas(self) -> None:
        """总技能文档必须冻结 atlas 的 UI-only、透明背景与数据排除规则。"""
        content = ORCHESTRATOR.read_text(encoding="utf-8")
        for snippet in ORCHESTRATOR_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_rules_require_atlas_with_effect_images(self) -> None:
        """路由规则必须要求效果图步骤同步产出 atlas 和 manifest。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_hard_rules_block_missing_or_opaque_atlas(self) -> None:
        """硬规则必须阻断不透明 atlas 和数据层混入 atlas。"""
        content = HARD_RULES.read_text(encoding="utf-8")
        for snippet in HARD_RULE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_asset_atlas_flow_mentions_manifest_and_data_exclusion(self) -> None:
        """asset atlas 参考文档必须声明透明 atlas、数据排除和切割清单。"""
        content = ASSET_ATLAS_FLOW.read_text(encoding="utf-8")
        for snippet in ASSET_ATLAS_FLOW_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_states_mentions_atlas_artifacts(self) -> None:
        """状态文档必须把 atlas 视作效果图证据的一部分。"""
        content = WORKFLOW_STATES.read_text(encoding="utf-8")
        for snippet in WORKFLOW_STATE_SNIPPETS:
            self.assertIn(snippet, content)

    def test_catalog_contract_mentions_atlas_records(self) -> None:
        """Catalog 契约必须允许记录 atlas 与 manifest 路径。"""
        content = CATALOG_CONTRACT.read_text(encoding="utf-8")
        for snippet in CATALOG_CONTRACT_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
