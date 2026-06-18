"""验证模块唯一归属与页面家族归并规则已写入关键文档。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_SPLITTER = REPO_ROOT / "skills" / "flutter-rd-module-splitter" / "SKILL.md"
ROUTING_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "routing-rules.md"

MODULE_SPLITTER_SNIPPETS = [
    "Each page family must have exactly one owning module.",
    "Do not split a list page, detail page, filter page, and state variants into different modules",
    "owned_page_families",
    "shared_surface_dependencies",
]

ROUTING_RULES_SNIPPETS = [
    "Before accepting a module split, verify that each page family has exactly one owning module.",
    "If two candidate modules still describe the same primary user job, same core data owner, and same state lifecycle, do not approve the split yet.",
]


class ModuleOwnershipRulesTest(unittest.TestCase):
    """验证模块拆分不会轻易漂成重复页面所有权。"""

    def test_module_splitter_mentions_unique_page_family_ownership(self) -> None:
        """模块拆分技能必须声明页面家族唯一归属。"""
        content = MODULE_SPLITTER.read_text(encoding="utf-8")
        for snippet in MODULE_SPLITTER_SNIPPETS:
            self.assertIn(snippet, content)

    def test_routing_rules_block_duplicate_module_ownership(self) -> None:
        """编排路由规则必须阻断重复页面职责拆分。"""
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_RULES_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
