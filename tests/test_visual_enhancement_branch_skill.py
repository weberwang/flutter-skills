"""验证后置增强分支已经从 workflow 中拆成独立 skill 管理。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
WORKFLOW_AGENT = REPO_ROOT / "skills" / "flutter-workflow" / "agents" / "openai.yaml"
ROUTING_RULES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "routing-rules.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "hard-rules.md"
ENHANCEMENT_SKILL = REPO_ROOT / "skills" / "flutter-visual-enhancement-branch" / "SKILL.md"
ENHANCEMENT_AGENT = (
    REPO_ROOT
    / "skills"
    / "flutter-visual-enhancement-branch"
    / "agents"
    / "openai.yaml"
)
WORKFLOW_RECORD_CONTRACT = (
    REPO_ROOT
    / "skills"
    / "flutter-workflow"
    / "references"
    / "workflow-record-contract.md"
)
README = REPO_ROOT / "README.md"

WORKFLOW_DELEGATION_SNIPPETS = [
    "$flutter-visual-enhancement-branch",
    "not by `flutter-workflow`",
    "persist branch-local stage updates",
    "must explicitly mark which later page modules or module pages need the visual-enhancement branch",
]

ROUTING_DELEGATION_SNIPPETS = [
    "route the active module to `flutter-visual-enhancement-branch`",
    "stop managing branch-local sequencing inside `flutter-workflow`",
    "Do not restate or improvise the branch-local step order here.",
    "Do not open that later branch until the workflow record explicitly marks which later page modules or module pages must enter it.",
]

ENHANCEMENT_SKILL_SNIPPETS = [
    "atlas extraction analysis",
    "solid-background atlas generation",
    "optional `$imagegen` transparency removal",
    "deterministic `ui-sheet-atlas-slicer` cutting",
    "`display_evidence_pack_ready`",
    "Pencil reinforcement",
    "docs/project/assets/global-asset-catalog.json",
    "explicit workflow-record mark that names which module pages are entering the later visual-enhancement branch",
    "`Product Design:ideate`",
    "`pencil_restoration_ready`",
]

README_SNIPPETS = [
    "后置增强分支",
    "flutter-visual-enhancement-branch",
]


class VisualEnhancementBranchSkillTest(unittest.TestCase):
    """验证增强分支职责从 workflow 主技能中拆出。"""

    def test_workflow_skill_delegates_visual_enhancement_branch(self) -> None:
        content = WORKFLOW_SKILL.read_text(encoding="utf-8")
        for snippet in WORKFLOW_DELEGATION_SNIPPETS:
            self.assertIn(snippet, content)

    def test_workflow_agent_mentions_branch_handoff(self) -> None:
        content = WORKFLOW_AGENT.read_text(encoding="utf-8")
        self.assertIn("$flutter-visual-enhancement-branch", content)
        self.assertIn("instead of managing atlas preparation", content)

    def test_routing_rules_delegate_branch_sequence(self) -> None:
        content = ROUTING_RULES.read_text(encoding="utf-8")
        for snippet in ROUTING_DELEGATION_SNIPPETS:
            self.assertIn(snippet, content)

    def test_hard_rules_block_workflow_micromanaging_branch(self) -> None:
        content = HARD_RULES.read_text(encoding="utf-8")
        self.assertIn("Do not let `flutter-workflow` micromanage the later visual-enhancement path", content)
        self.assertIn("flutter-visual-enhancement-branch", content)
        self.assertIn(
            "Do not open the later visual-enhancement path without explicitly marking which module pages are entering that branch in the workflow record.",
            content,
        )

    def test_enhancement_skill_owns_branch_local_steps(self) -> None:
        content = ENHANCEMENT_SKILL.read_text(encoding="utf-8")
        for snippet in ENHANCEMENT_SKILL_SNIPPETS:
            self.assertIn(snippet, content)

    def test_enhancement_agent_exists(self) -> None:
        content = ENHANCEMENT_AGENT.read_text(encoding="utf-8")
        self.assertIn("Flutter Visual Enhancement Branch", content)
        self.assertIn("$flutter-visual-enhancement-branch", content)

    def test_workflow_record_contract_marks_branch_scope(self) -> None:
        content = WORKFLOW_RECORD_CONTRACT.read_text(encoding="utf-8")
        self.assertIn("visual_enhancement_scope", content)
        self.assertIn("candidate:<page list>|reason:<short reason>", content)
        self.assertIn("required:<page list>|reason:<short reason>", content)

    def test_readme_mentions_new_branch_skill(self) -> None:
        content = README.read_text(encoding="utf-8")
        for snippet in README_SNIPPETS:
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
