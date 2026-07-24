#!/usr/bin/env python3
"""合并已验收的并行任务，并清理对应 worktree 与本地分支。"""

import argparse
import importlib.util
import os
import subprocess
import sys
from pathlib import Path


# 校验脚本文件名含连字符，只能按路径加载。
_validator_spec = importlib.util.spec_from_file_location(
    "task_state_validator", Path(__file__).with_name("validate-task-state.py")
)
if _validator_spec is None or _validator_spec.loader is None:
    raise RuntimeError("无法加载任务状态校验器")
_validator_module = importlib.util.module_from_spec(_validator_spec)
_validator_spec.loader.exec_module(_validator_module)
parse_restricted_yaml = _validator_module.parse_restricted_yaml
validate_task_state = _validator_module.validate_task_state


class WorkflowError(RuntimeError):
    """表示并行任务不满足自动收尾条件。"""


def run_git(repository: Path, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """运行 Git，并把失败转换为可操作的流程错误。"""
    command = ["git", "-C", str(repository), *arguments]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if check and completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "未知 Git 错误"
        raise WorkflowError(f"Git 命令失败：{' '.join(command)}\n{detail}")
    return completed


def load_state(state_file: Path) -> dict[str, object]:
    """读取并校验短生命周期的并行任务状态。"""
    try:
        data = parse_restricted_yaml(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WorkflowError(f"无法读取任务状态：{error}") from error

    errors = validate_task_state(data)
    if errors:
        raise WorkflowError("任务状态无效：\n" + "\n".join(f"- {error}" for error in errors))
    return data


def ensure_task_worktree(
    repository: Path,
    state_file: Path,
    task_worktree: Path,
    task_branch: str,
    candidate_commit: str,
) -> None:
    """确认待清理 worktree 正在检出已验收候选分支。"""
    if not task_worktree.exists():
        raise WorkflowError("任务 worktree 不存在")

    actual_root = Path(
        run_git(task_worktree, "rev-parse", "--show-toplevel").stdout.strip()
    ).resolve()
    if os.path.normcase(str(actual_root)) != os.path.normcase(str(task_worktree)):
        raise WorkflowError("任务 worktree 路径不是其 Git 工作目录根路径")
    if run_git(task_worktree, "branch", "--show-current").stdout.strip() != task_branch:
        raise WorkflowError("任务 worktree 未检出状态文件记录的分支")
    if run_git(task_worktree, "rev-parse", "HEAD").stdout.strip() != candidate_commit:
        raise WorkflowError("任务分支 HEAD 与已验收候选提交不一致")

    state_relative = state_file.relative_to(repository).as_posix()
    if run_git(
        task_worktree,
        "ls-files",
        "--error-unmatch",
        "--",
        state_relative,
        check=False,
    ).returncode == 0:
        raise WorkflowError("任务分支不得提交短生命周期状态文件")


def merge_candidate(
    repository: Path,
    integration_branch: str,
    base_commit: str,
    candidate_commit: str,
) -> None:
    """校验候选基线并创建一次无快进合并。"""
    already_merged = run_git(
        repository,
        "merge-base",
        "--is-ancestor",
        candidate_commit,
        integration_branch,
        check=False,
    ).returncode == 0
    if already_merged:
        return

    actual_base = run_git(
        repository, "merge-base", integration_branch, candidate_commit
    ).stdout.strip()
    if actual_base != base_commit:
        raise WorkflowError("记录的基线不是候选分支与当前集成分支的共同基线")

    run_git(repository, "diff", "--check", f"{base_commit}..{candidate_commit}")
    merged = run_git(
        repository,
        "merge",
        "--no-ff",
        "--no-edit",
        candidate_commit,
        check=False,
    )
    if merged.returncode != 0:
        # 无论 Git 是否已建立 MERGE_HEAD，都让原生命令决定是否存在可撤销合并。
        run_git(repository, "merge", "--abort", check=False)
        detail = merged.stderr.strip() or merged.stdout.strip() or "未知 Git 错误"
        raise WorkflowError(f"候选合并失败，已尝试撤销半完成合并：\n{detail}")


def finish_task(state_file: Path, repository: Path, integration_branch: str) -> None:
    """合并并行任务，清理临时资源后删除运行期状态。"""
    try:
        state_relative = state_file.relative_to(repository)
    except ValueError as error:
        raise WorkflowError("任务状态文件必须位于 Controller 工作目录内") from error
    if state_relative.parts[:2] != (".codex-workflow", "tasks"):
        raise WorkflowError("任务状态文件必须位于 .codex-workflow/tasks")

    data = load_state(state_file)
    acceptance = data.get("acceptance")
    if str(data.get("state", "")) != "reviewing":
        raise WorkflowError("自动收尾只接受 reviewing 状态")
    if not isinstance(acceptance, dict) or acceptance.get("verdict") != "approved":
        raise WorkflowError("自动收尾需要 acceptance.verdict 为 approved")
    if run_git(repository, "branch", "--show-current").stdout.strip() != integration_branch:
        raise WorkflowError("Controller 必须停留在指定集成分支")

    task_branch = str(data["branch"])
    task_worktree = Path(str(data["worktree"])).resolve()
    candidate_commit = str(data["candidate_commit"])
    ensure_task_worktree(
        repository,
        state_file,
        task_worktree,
        task_branch,
        candidate_commit,
    )
    merge_candidate(
        repository,
        integration_branch,
        str(data["base_commit"]),
        candidate_commit,
    )

    run_git(repository, "worktree", "remove", "--", str(task_worktree))
    run_git(repository, "branch", "-d", "--", task_branch)
    state_file.unlink()
    print(f"并行任务 {data['id']} 已合并并清理；候选提交：{candidate_commit}")


def main() -> int:
    """解析参数并以稳定退出码报告收尾结果。"""
    parser = argparse.ArgumentParser(description="合并并清理并行 Flutter 任务")
    parser.add_argument("state_file", type=Path)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--integration-branch", required=True)
    args = parser.parse_args()

    try:
        finish_task(
            args.state_file.resolve(),
            args.repository.resolve(),
            args.integration_branch,
        )
    except (OSError, WorkflowError) as error:
        print(f"自动收尾失败：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
