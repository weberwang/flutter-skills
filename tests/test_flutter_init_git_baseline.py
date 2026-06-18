"""验证 Flutter 初始化与工作流编排文档包含 git 基线自动化约束。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ORCHESTRATOR_SKILL = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "SKILL.md"
INIT_SKILL = REPO_ROOT / "skills" / "flutter-init" / "SKILL.md"
BOOTSTRAP_WORKFLOW = REPO_ROOT / "skills" / "flutter-init" / "references" / "bootstrap-workflow.md"
OUTPUT_CHECKLIST = REPO_ROOT / "skills" / "flutter-init" / "references" / "project-output-checklist.md"

ORCHESTRATOR_SNIPPETS = [
    "first call",
    "git status",
    ".gitignore",
]

INIT_SNIPPETS = [
    "git init",
    ".gitignore",
    ".agents",
    ".claude",
    ".dart_tool/",
    ".idea/",
    ".vscode/",
    "build/",
]


class FlutterInitGitBaselineTest(unittest.TestCase):
    """验证首次初始化时的 git 仓库与忽略文件约束不会从文档中丢失。"""

    def test_orchestrator_mentions_first_call_git_preflight(self) -> None:
        """编排器必须声明首次调用时要检查 git 状态与忽略文件基线。"""
        content = ORCHESTRATOR_SKILL.read_text(encoding="utf-8")
        for snippet in ORCHESTRATOR_SNIPPETS:
            self.assertIn(snippet, content)

    def test_flutter_init_skill_mentions_git_init_and_ignore_rules(self) -> None:
        """初始化 skill 必须声明 git 初始化与 .gitignore 幂等补齐要求。"""
        content = INIT_SKILL.read_text(encoding="utf-8")
        for snippet in INIT_SNIPPETS:
            self.assertIn(snippet, content)

    def test_bootstrap_workflow_mentions_git_baseline_steps(self) -> None:
        """初始化步骤文档必须包含 git 仓库与 .gitignore 的处理顺序。"""
        content = BOOTSTRAP_WORKFLOW.read_text(encoding="utf-8")
        for snippet in INIT_SNIPPETS:
            self.assertIn(snippet, content)

    def test_output_checklist_mentions_gitignore_completion(self) -> None:
        """交付检查清单必须覆盖 git 初始化和常见忽略项检查。"""
        content = OUTPUT_CHECKLIST.read_text(encoding="utf-8")
        for snippet in ("git init", ".gitignore", ".agents", ".claude", ".dart_tool/", "build/"):
            self.assertIn(snippet, content)


if __name__ == "__main__":
    unittest.main()
