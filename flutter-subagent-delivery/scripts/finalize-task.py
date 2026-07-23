#!/usr/bin/env python3
"""安全合并已验收任务，并按隔离模式清理临时分支或 worktree。"""

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


def repository_root(repository: Path) -> Path:
    """解析当前 Git 工作目录根路径，确保后续路径检查使用真实位置。"""
    return Path(run_git(repository, "rev-parse", "--show-toplevel")).resolve()


def normalized_path(path: Path) -> str:
    """生成兼容 Windows 大小写规则的路径比较键。"""
    return os.path.normcase(str(path.resolve()))


def ensure_task_reports(repository: Path, candidate_commit: str, reports: object) -> None:
    """确认已验收候选提交包含必需报告，避免依赖特定工作目录。"""
    if not isinstance(reports, dict):
        raise WorkflowError("任务状态缺少 reports 映射")

    for name in ("review",):
        report = str(reports.get(name, "")).replace("\\", "/")
        report_path = Path(report)
        if report_path.is_absolute() or ".." in report_path.parts:
            raise WorkflowError(f"reports.{name} 必须是仓库内相对路径")
        if not git_succeeds(repository, "cat-file", "-e", f"{candidate_commit}:{report}"):
            raise WorkflowError(f"候选提交缺少必需报告：reports.{name} ({report})")


def ensure_valid_branch_name(repository: Path, branch: str, label: str) -> None:
    """使用 Git 自身的引用校验阻断异常参数和错误分支名。"""
    if not branch or branch.startswith("-"):
        raise WorkflowError(f"{label}分支不能为空或以 - 开头")
    run_git(repository, "check-ref-format", "--branch", branch)


def branch_checkout_path(repository: Path, branch: str) -> Path | None:
    """返回本地分支当前注册的工作目录；未检出时返回空。"""
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
            if current_path and current_branch == expected_branch:
                return Path(current_path).resolve()
            current_path = ""
            current_branch = ""

    return None


def worktree_matches_branch(repository: Path, task_worktree: Path, branch: str) -> bool:
    """确认待删除路径确实是该仓库中任务分支关联的 worktree。"""
    checkout = branch_checkout_path(repository, branch)
    return checkout is not None and normalized_path(checkout) == normalized_path(task_worktree)


def prepare_integration_branch(
    repository: Path,
    task_branch: str,
    integration_branch: str,
    isolation: str,
) -> None:
    """按隔离模式定位集成分支；普通分支模式允许从任务分支安全切回。"""
    current_branch = run_git(repository, "branch", "--show-current")
    if isolation == "worktree":
        if current_branch != integration_branch:
            raise WorkflowError(
                "worktree 隔离模式要求 Controller 工作目录保持在集成分支"
            )
        return

    checkout = branch_checkout_path(repository, task_branch)
    if checkout is not None and normalized_path(checkout) != normalized_path(repository):
        raise WorkflowError("branch 隔离模式的任务分支不得检出到其他 worktree")
    if current_branch == task_branch:
        run_git(repository, "switch", integration_branch)
        return
    if current_branch != integration_branch:
        raise WorkflowError(
            f"当前分支为 {current_branch or 'detached HEAD'}，"
            f"不是任务分支 {task_branch} 或集成分支 {integration_branch}"
        )


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
    """只提交任务状态，保留工作区中其他任务或用户的暂存改动。"""
    try:
        relative_state = state_file.relative_to(repository)
    except ValueError as error:
        raise WorkflowError("任务状态文件必须位于集成仓库内") from error

    # 使用 --only 隔离状态提交，避免把用户已有的暂存改动混入自动收尾提交。
    run_git(repository, "add", "--", str(relative_state))
    run_git(
        repository,
        "commit",
        "--only",
        "-m",
        f"chore(workflow): {stage} {task_id}",
        "--",
        str(relative_state),
    )


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
    # 让 Git 临时保存可暂存的既有改动，合并后恢复，避免把脏工作区当成流程门禁。
    command = [
        "git",
        "-C",
        str(repository),
        "merge",
        "--autostash",
        "--no-ff",
        "--no-edit",
        task_branch,
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode == 0:
        return

    if git_succeeds(repository, "rev-parse", "-q", "--verify", "MERGE_HEAD"):
        run_git(repository, "merge", "--abort")
    detail = completed.stderr.strip() or completed.stdout.strip() or "未知 Git 错误"
    raise WorkflowError(
        "任务分支自动合并失败，已撤销工作目录中的半完成合并；"
        f"请由任务所有者修复分支后重试。\n{detail}"
    )


def cleanup_task_checkout(
    repository: Path,
    isolation: str,
    task_worktree: Path | None,
    branch: str,
    remote: str | None,
) -> None:
    """只删除已合并任务对应的分支，以及按需创建的 worktree。"""
    if isolation == "worktree" and task_worktree is not None and task_worktree.exists():
        if not worktree_matches_branch(repository, task_worktree, branch):
            raise WorkflowError("任务 worktree 未注册为指定任务分支；拒绝删除该路径")
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
    repository_path: Path,
    integration_branch: str,
    remote: str | None,
) -> None:
    """执行普通分支或 worktree 模式的可重试合并与清理。"""
    repository = repository_root(repository_path)
    if repository != repository_path:
        raise WorkflowError("--repository 必须指向当前 Git 工作目录根路径")
    try:
        state_file.relative_to(repository)
    except ValueError:
        raise WorkflowError("任务状态文件必须位于 Controller 工作目录内")

    ensure_valid_branch_name(repository, integration_branch, "集成")

    data = load_and_validate(state_file)
    task_id = str(data["id"])
    state = str(data["state"])
    isolation = str(data["isolation"])
    acceptance = data["acceptance"]
    integration = data["integration"]
    if not isinstance(acceptance, dict) or acceptance.get("verdict") != "approved":
        raise WorkflowError("自动收尾要求独立验收已将 acceptance.verdict 设为 approved")
    if not isinstance(integration, dict):
        raise WorkflowError("任务状态缺少 integration 映射")
    if state not in {"reviewing", "integrating"}:
        raise WorkflowError("自动收尾只接受 reviewing 或可重试的 integrating 状态")

    task_branch = str(data["branch"])
    worktree_value = str(data["worktree"])
    task_worktree = Path(worktree_value).resolve() if worktree_value else None
    base_commit = str(data["base_commit"])
    candidate_commit = str(data["candidate_commit"])
    merged_commit = str(integration.get("merged_commit", ""))
    ensure_valid_branch_name(repository, task_branch, "任务")
    if task_branch == integration_branch:
        raise WorkflowError("任务分支不得与集成分支相同")

    if task_branch_tracks_state(repository, task_branch, state_file):
        raise WorkflowError("任务分支包含活动任务状态文件；请先移出并提交任务实现")
    prepare_integration_branch(repository, task_branch, integration_branch, isolation)

    if state == "reviewing":
        if isolation == "worktree" and (
            task_worktree is None
            or not task_worktree.exists()
            or not worktree_matches_branch(repository, task_worktree, task_branch)
        ):
            raise WorkflowError("worktree 隔离任务必须保留与任务分支匹配的 worktree")
        if not branch_exists(repository, task_branch):
            raise WorkflowError("任务本地分支不存在，无法自动合并")
        if run_git(repository, "rev-parse", task_branch) != candidate_commit:
            raise WorkflowError("任务分支 HEAD 与已验收候选提交不一致；请完成受影响范围复审")
        ensure_task_reports(repository, candidate_commit, data.get("reports"))
        run_git(repository, "cat-file", "-e", f"{base_commit}^{{commit}}")
        if not branch_is_merged(repository, base_commit, integration_branch):
            raise WorkflowError("任务基线不是当前集成分支祖先；请先由 Controller 解决集成顺序")
        if not branch_is_merged(repository, base_commit, task_branch):
            raise WorkflowError("任务基线不是任务分支祖先")
        if branch_is_merged(repository, task_branch, integration_branch):
            raise WorkflowError("任务分支已进入集成分支，但状态仍为 reviewing；请先修复状态记录")

        run_git(repository, "diff", "--check", f"{base_commit}..{task_branch}")
        merge_task_branch(repository, task_branch)
        merged_commit = run_git(repository, "rev-parse", "HEAD")
        write_state_transition(state_file, "integrating", merged_commit, "pending")
        load_and_validate(state_file)
    else:
        if not merged_commit:
            raise WorkflowError("integrating 状态缺少 integration.merged_commit")
        run_git(repository, "cat-file", "-e", f"{merged_commit}^{{commit}}")
        if not branch_is_merged(repository, merged_commit, integration_branch):
            raise WorkflowError("记录的合并提交不在当前集成分支；拒绝清理任务资源")

    cleanup_task_checkout(repository, isolation, task_worktree, task_branch, remote)
    write_state_transition(state_file, "accepted", merged_commit, "completed")
    load_and_validate(state_file)
    commit_state_record(repository, state_file, task_id, "accept")
    print(
        f"任务 {task_id} 已合并：{merged_commit}；"
        f"{isolation} 隔离资源已清理，仅最终 accepted 状态已提交"
    )


def main() -> int:
    """解析 Controller 参数并输出可直接用于恢复流程的失败信息。"""
    parser = argparse.ArgumentParser(description="自动合并并清理 Flutter 协作任务")
    parser.add_argument("state_file", type=Path, help="Controller 工作目录内的任务状态文件")
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--integration-branch", required=True)
    parser.add_argument(
        "--remote",
        help="已推送临时分支的远端名；提供后才删除对应远端分支",
    )
    args = parser.parse_args()

    try:
        finish_task(
            args.state_file.resolve(),
            args.repository.resolve(),
            args.integration_branch,
            args.remote,
        )
    except WorkflowError as error:
        print(f"自动收尾失败：{error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
