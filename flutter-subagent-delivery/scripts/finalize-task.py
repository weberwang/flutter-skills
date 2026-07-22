#!/usr/bin/env python3
"""安全合并已验收任务，并清理对应 worktree 与临时分支。"""

import argparse
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

# 源校验脚本为保留命令行文件名使用连字符，需按文件路径加载而非普通模块导入。
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
    """表示自动收尾前置条件或 Git 操作未满足。"""


def run_git(repository: Path, *arguments: str, check: bool = True) -> str:
    """在指定仓库运行 Git，并在失败时返回可操作的诊断。"""
    command = ["git", "-C", str(repository), *arguments]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if check and completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip() or "未知 Git 错误"
        raise WorkflowError(f"Git 命令失败：{' '.join(command)}\n{detail}")
    return completed.stdout.strip()


def git_succeeds(repository: Path, *arguments: str) -> bool:
    """以退出码判断 Git 检查是否成立，避免把预期的不存在当作异常。"""
    completed = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )
    return completed.returncode == 0


def repository_root(worktree: Path) -> Path:
    """解析 worktree 的仓库根目录，确保后续路径检查使用真实位置。"""
    return Path(run_git(worktree, "rev-parse", "--show-toplevel")).resolve()


def normalized_path(path: Path) -> str:
    """生成兼容 Windows 大小写规则的路径比较键。"""
    return os.path.normcase(str(path.resolve()))


def require_clean_worktree(worktree: Path, label: str) -> None:
    """拒绝在含未提交改动的 worktree 上自动合并或删除。"""
    if run_git(worktree, "status", "--porcelain", "--untracked-files=all"):
        raise WorkflowError(f"{label} worktree 不干净；请先提交、转移或删除未提交改动后重试")


def require_clean_integration_worktree(integration_root: Path, state_file: Path) -> None:
    """只容许当前未提交任务状态存在，避免任务分支携带易冲突的活动状态。"""
    try:
        state_relative = state_file.relative_to(integration_root).as_posix()
    except ValueError as error:
        raise WorkflowError("任务状态文件必须位于 Controller 集成 worktree 内") from error

    unexpected: list[str] = []
    for line in run_git(
        integration_root, "status", "--porcelain", "--untracked-files=all"
    ).splitlines():
        path = line[3:].replace("\\", "/")
        if path != state_relative:
            unexpected.append(line)
    if unexpected:
        raise WorkflowError(
            "集成 worktree 除当前任务状态外仍有未提交改动：\n" + "\n".join(unexpected)
        )


def ensure_task_reports(task_worktree: Path, reports: object) -> None:
    """确认自动合并前存在包含快照和验证链接的独立验收记录。"""
    if not isinstance(reports, dict):
        raise WorkflowError("任务状态缺少 reports 映射")

    for name in ("review",):
        report = task_worktree / str(reports.get(name, ""))
        if not report.is_file():
            raise WorkflowError(f"任务分支缺少必需报告：reports.{name} ({report})")


def ensure_valid_branch_name(repository: Path, branch: str, label: str) -> None:
    """使用 Git 自身的引用校验阻断异常参数和错误分支名。"""
    if not branch or branch.startswith("-"):
        raise WorkflowError(f"{label}分支不能为空或以 - 开头")
    run_git(repository, "check-ref-format", "--branch", branch)


def worktree_matches_branch(repository: Path, task_worktree: Path, branch: str) -> bool:
    """确认待删除路径确实是该仓库中任务分支关联的 worktree。"""
    expected_path = normalized_path(task_worktree)
    expected_branch = f"refs/heads/{branch}"
    current_path = ""
    current_branch = ""

    for line in run_git(repository, "worktree", "list", "--porcelain").splitlines() + [""]:
        if line.startswith("worktree "):
            current_path = line.removeprefix("worktree ")
            current_branch = ""
        elif line.startswith("branch "):
            current_branch = line.removeprefix("branch ")
        elif not line:
            if current_path and normalized_path(Path(current_path)) == expected_path:
                return current_branch == expected_branch
            current_path = ""
            current_branch = ""

    return False


def replace_yaml_value(content: str, key: str, value: str, indent: int) -> str:
    """替换受限 YAML 中唯一的标量字段，同时保留其余人工记录。"""
    prefix = " " * indent + f"{key}:"
    lines = content.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            newline = "\r\n" if line.endswith("\r\n") else "\n"
            lines[index] = f"{prefix} {value}{newline}"
            return "".join(lines)
    raise WorkflowError(f"任务状态缺少可更新字段：{key}")


def write_state_transition(
    state_file: Path,
    state: str,
    merged_commit: str,
    cleanup: str,
) -> None:
    """原地写入收尾状态；该文件仅允许 Controller 自动化流程修改。"""
    content = state_file.read_text(encoding="utf-8")
    content = replace_yaml_value(content, "state", state, 0)
    content = replace_yaml_value(content, "merged_commit", merged_commit, 2)
    content = replace_yaml_value(content, "cleanup", cleanup, 2)
    state_file.write_text(content, encoding="utf-8")


def commit_state_record(repository: Path, state_file: Path, task_id: str, stage: str) -> None:
    """单独提交状态记录，避免将自动化元数据混入任务实现提交。"""
    try:
        relative_state = state_file.relative_to(repository)
    except ValueError as error:
        raise WorkflowError("任务状态文件必须位于集成仓库内") from error

    run_git(repository, "add", "--", str(relative_state))
    staged_files = run_git(repository, "diff", "--cached", "--name-only")
    if staged_files.splitlines() != [str(relative_state).replace("\\", "/")]:
        raise WorkflowError("状态提交暂存区包含非任务状态文件；请恢复干净集成 worktree 后重试")
    run_git(repository, "commit", "-m", f"chore(workflow): {stage} {task_id}")


def branch_exists(repository: Path, branch: str) -> bool:
    """检查本地任务分支是否仍存在。"""
    return git_succeeds(repository, "show-ref", "--verify", "--quiet", f"refs/heads/{branch}")


def branch_is_merged(repository: Path, branch_or_commit: str, integration_branch: str) -> bool:
    """判断任务分支或记录的合并提交是否已经进入集成分支。"""
    return git_succeeds(
        repository,
        "merge-base",
        "--is-ancestor",
        branch_or_commit,
        integration_branch,
    )


def merge_task_branch(repository: Path, task_branch: str) -> None:
    """创建无快进合并；冲突或钩子失败时撤销半完成合并以便任务分支修复。"""
    command = ["git", "-C", str(repository), "merge", "--no-ff", "--no-edit", task_branch]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode == 0:
        return

    if git_succeeds(repository, "rev-parse", "-q", "--verify", "MERGE_HEAD"):
        run_git(repository, "merge", "--abort")
    detail = completed.stderr.strip() or completed.stdout.strip() or "未知 Git 错误"
    raise WorkflowError(
        "任务分支自动合并失败，已撤销集成 worktree 中的半完成合并；"
        f"请由任务所有者修复分支后重试。\n{detail}"
    )


def cleanup_task_checkout(
    repository: Path,
    task_worktree: Path,
    branch: str,
    remote: str | None,
) -> None:
    """只删除已合并、已验证且属于任务分支的本地资源。"""
    if task_worktree.exists():
        if not worktree_matches_branch(repository, task_worktree, branch):
            raise WorkflowError("任务 worktree 未注册为指定任务分支；拒绝删除该路径")
        require_clean_worktree(task_worktree, "任务")
        run_git(repository, "worktree", "remove", "--", str(task_worktree))

    if branch_exists(repository, branch):
        run_git(repository, "branch", "-d", "--", branch)

    if remote:
        run_git(repository, "remote", "get-url", remote)
        remote_ref = f"refs/heads/{branch}"
        if git_succeeds(repository, "ls-remote", "--exit-code", "--heads", remote, remote_ref):
            run_git(repository, "push", remote, "--delete", branch)


def load_and_validate(state_file: Path) -> dict[str, object]:
    """读取状态文件并复用共享校验器阻止不完整状态进入收尾阶段。"""
    try:
        data = parse_restricted_yaml(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise WorkflowError(f"无法读取任务状态：{error}") from error

    errors = validate_task_state(data)
    if errors:
        raise WorkflowError("任务状态无效：\n" + "\n".join(f"- {error}" for error in errors))
    return data


def task_branch_tracks_state(repository: Path, branch: str, state_file: Path) -> bool:
    """检测任务分支是否错误纳入活动状态文件，避免合并时覆盖 Controller 状态。"""
    relative_state = state_file.relative_to(repository).as_posix()
    return git_succeeds(repository, "cat-file", "-e", f"{branch}:{relative_state}")


def finish_task(
    state_file: Path,
    integration_worktree: Path,
    integration_branch: str,
    remote: str | None,
) -> None:
    """执行可重试的合并、状态记录和任务 worktree/分支清理流程。"""
    integration_root = repository_root(integration_worktree)
    if integration_root != integration_worktree:
        raise WorkflowError("--integration-worktree 必须指向 Git worktree 根目录")
    try:
        state_file.relative_to(integration_root)
    except ValueError:
        raise WorkflowError("任务状态文件必须位于 Controller 集成 worktree 内")

    ensure_valid_branch_name(integration_root, integration_branch, "集成")
    current_branch = run_git(integration_root, "branch", "--show-current")
    if current_branch != integration_branch:
        raise WorkflowError(
            f"集成 worktree 当前分支为 {current_branch or 'detached HEAD'}，不是 {integration_branch}"
        )

    data = load_and_validate(state_file)
    task_id = str(data["id"])
    state = str(data["state"])
    acceptance = data["acceptance"]
    integration = data["integration"]
    if not isinstance(acceptance, dict) or acceptance.get("verdict") != "approved":
        raise WorkflowError("自动收尾要求独立验收已将 acceptance.verdict 设为 approved")
    if not isinstance(integration, dict):
        raise WorkflowError("任务状态缺少 integration 映射")
    if state not in {"reviewing", "integrating"}:
        raise WorkflowError("自动收尾只接受 reviewing 或可重试的 integrating 状态")

    task_branch = str(data["branch"])
    task_worktree = Path(str(data["worktree"])).resolve()
    base_commit = str(data["base_commit"])
    merged_commit = str(integration.get("merged_commit", ""))
    ensure_valid_branch_name(integration_root, task_branch, "任务")
    if task_branch == integration_branch:
        raise WorkflowError("任务分支不得与集成分支相同")

    require_clean_integration_worktree(integration_root, state_file)

    if state == "reviewing":
        if not task_worktree.exists() or not worktree_matches_branch(
            integration_root, task_worktree, task_branch
        ):
            raise WorkflowError("reviewing 任务必须保留与任务分支匹配的 worktree")
        if not branch_exists(integration_root, task_branch):
            raise WorkflowError("任务本地分支不存在，无法自动合并")
        if task_branch_tracks_state(integration_root, task_branch, state_file):
            raise WorkflowError("任务分支包含活动任务状态文件；请先由 Controller 重建隔离分支")
        require_clean_worktree(task_worktree, "任务")
        ensure_task_reports(task_worktree, data.get("reports"))
        run_git(integration_root, "cat-file", "-e", f"{base_commit}^{{commit}}")
        if not branch_is_merged(integration_root, base_commit, integration_branch):
            raise WorkflowError("任务基线不是当前集成分支祖先；请先由 Controller 解决集成顺序")
        if not branch_is_merged(integration_root, base_commit, task_branch):
            raise WorkflowError("任务基线不是任务分支祖先")
        if branch_is_merged(integration_root, task_branch, integration_branch):
            raise WorkflowError("任务分支已进入集成分支，但状态仍为 reviewing；请先修复状态记录")

        run_git(integration_root, "diff", "--check", f"{base_commit}..{task_branch}")
        merge_task_branch(integration_root, task_branch)
        merged_commit = run_git(integration_root, "rev-parse", "HEAD")
        write_state_transition(state_file, "integrating", merged_commit, "pending")
        load_and_validate(state_file)
        commit_state_record(integration_root, state_file, task_id, "integrate")
    else:
        if not merged_commit:
            raise WorkflowError("integrating 状态缺少 integration.merged_commit")
        run_git(integration_root, "cat-file", "-e", f"{merged_commit}^{{commit}}")
        if not branch_is_merged(integration_root, merged_commit, integration_branch):
            raise WorkflowError("记录的合并提交不在当前集成分支；拒绝清理任务资源")

    cleanup_task_checkout(integration_root, task_worktree, task_branch, remote)
    write_state_transition(state_file, "accepted", merged_commit, "completed")
    load_and_validate(state_file)
    commit_state_record(integration_root, state_file, task_id, "accept")
    print(
        f"任务 {task_id} 已合并：{merged_commit}；"
        "任务 worktree 与本地分支已清理，状态已提交为 accepted"
    )


def main() -> int:
    """解析 Controller 参数并输出可直接用于恢复流程的失败信息。"""
    parser = argparse.ArgumentParser(description="自动合并并清理 Flutter 协作任务")
    parser.add_argument("state_file", type=Path, help="集成 worktree 内的任务状态文件")
    parser.add_argument("--integration-worktree", type=Path, required=True)
    parser.add_argument("--integration-branch", required=True)
    parser.add_argument(
        "--remote",
        help="已推送临时分支的远端名；提供后才删除对应远端分支",
    )
    args = parser.parse_args()

    try:
        finish_task(
            args.state_file.resolve(),
            args.integration_worktree.resolve(),
            args.integration_branch,
            args.remote,
        )
    except WorkflowError as error:
        print(f"自动收尾失败：{error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
