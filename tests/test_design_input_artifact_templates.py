"""Verify the workflow exposes the minimal outward-facing design artifact set."""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_SKILL = REPO_ROOT / "skills" / "flutter-workflow" / "SKILL.md"
CONTROL_CONTRACTS = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "control-contracts.md"
WORKFLOW_RECORD = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "workflow-record-contract.md"
DESIGN_TEMPLATE = REPO_ROOT / "skills" / "flutter-workflow" / "references" / "design-md-template.md"
DESIGN_CONSTRAINT_TEMPLATE = (
    REPO_ROOT
    / "skills"
    / "flutter-workflow"
    / "references"
    / "design-constraint-package-template.md"
)
HUMAN_DECISION_TEMPLATE = (
    REPO_ROOT
    / "skills"
    / "flutter-workflow"
    / "references"
    / "human-decision-recommendation-template.md"
)


class DesignInputArtifactTemplatesTest(unittest.TestCase):
    """Verify the two outward-facing design templates and the internal state split."""

    def test_template_files_exist(self) -> None:
        """The workflow should ship dedicated templates for both outward-facing artifacts."""
        self.assertTrue(DESIGN_CONSTRAINT_TEMPLATE.exists())
        self.assertTrue(HUMAN_DECISION_TEMPLATE.exists())

    def test_workflow_skill_declares_minimal_design_input_artifact_set(self) -> None:
        """The main skill should describe the two outward-facing artifacts explicitly."""
        content = WORKFLOW_SKILL.read_text(encoding="utf-8")
        self.assertIn("## Design Input Artifact Set", content)
        self.assertIn("design_constraint_package.md", content)
        self.assertIn("human_decision_recommendation_package.md", content)
        self.assertIn("runtime workflow record as internal orchestrator state", content)

    def test_control_contracts_keep_design_artifacts_and_runtime_state_separate(self) -> None:
        """Control contracts should preserve the artifact split during routing."""
        content = CONTROL_CONTRACTS.read_text(encoding="utf-8")
        self.assertIn("## Design Input Artifact Contract", content)
        self.assertIn("The first two are outward-facing design collaboration artifacts.", content)
        self.assertIn("The runtime workflow record is internal orchestrator state.", content)

    def test_workflow_record_indexes_the_two_outward_facing_artifacts(self) -> None:
        """Workflow state should index these artifacts without becoming one of them."""
        content = WORKFLOW_RECORD.read_text(encoding="utf-8")
        self.assertIn("design constraint package path", content)
        self.assertIn("human decision recommendation package path", content)
        self.assertIn("Do not treat it as a substitute for outward-facing design artifacts", content)

    def test_design_md_template_consumes_but_does_not_replace_upstream_artifacts(self) -> None:
        """DESIGN.md should remain a downstream design-system packet."""
        content = DESIGN_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("consume the already decided design constraint package instead of replacing it", content)
        self.assertIn("consume resolved human decision recommendations instead of restating upstream decision scaffolding", content)
        self.assertIn("human_decision_recommendation_package.md", content)
        self.assertIn("stable downstream design system packet", content)


if __name__ == "__main__":
    unittest.main()
