#!/usr/bin/env python3
"""校验协作流程使用的受限 YAML 任务状态文件。"""

import argparse
import re
import sys
from pathlib import Path


VALID_STATES = {
    "planned",
    "claimed",
    "implementing",
    "reviewing",
    "integrating",
    "accepted",
    "blocked",
}
VALID_ACCEPTANCE_VERDICTS = {"pending", "approved", "changes_requested"}
VALID_CLEANUP_STATES = {"pending", "completed"}
REQUIRED_ROOT_KEYS = {
    "id",
    "state",
    "owner",
    "lease",
    "base_commit",
    "branch",
    "worktree",
    "write_scope",
    "inputs",
    "reports",
    "acceptance",
    "integration",
    "blocker",
}


# 仅解析本 skill 模板使用的两层 YAML，避免为流程校验新增第三方运行时依赖。
def parse_restricted_yaml(content: str) -> dict[str, object]:
    """将任务状态模板允许的标量和二层映射解析为字典。"""
    result: dict[str, object] = {}
    section: dict[str, str] | None = None

    for raw_line in content.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        line = re.sub(r"\s+#.*$", "", line)
        indent = len(line) - len(line.lstrip(" "))
        key, separator, value = line.strip().partition(":")
        if not separator or not key:
            raise ValueError(f"无法解析 YAML 行：{raw_line}")

        normalized = value.strip().strip('"')
        if indent == 0:
            if normalized:
                result[key] = normalized
                section = None
            else:
                section = {}
                result[key] = section
        elif indent == 2 and section is not None:
            section[key] = normalized
        else:
            raise ValueError(f"不支持的 YAML 缩进：{raw_line}")

    return result


# 状态校验在任务认领和迁移时阻止缺失的隔离与可追溯性信息进入共享账本。
def validate_task_state(data: dict[str, object]) -> list[str]:
    """返回所有不符合协作协议的状态文件错误。"""
    errors: list[str] = []
    missing = REQUIRED_ROOT_KEYS - data.keys()
    if missing:
        errors.append(f"缺少根字段：{', '.join(sorted(missing))}")

    task_id = str(data.get("id", ""))
    state = str(data.get("state", ""))
    if not task_id:
        errors.append("id 不能为空")
    if state not in VALID_STATES:
        errors.append(f"state 必须是以下值之一：{', '.join(sorted(VALID_STATES))}")

    reports = data.get("reports")
    if not isinstance(reports, dict):
        errors.append("reports 必须是映射")
    elif task_id:
        expected_prefix = f"docs/tasks/{task_id}/"
        for name in ("implementer", "review", "visual_qa", "evidence_manifest"):
            path = str(reports.get(name, ""))
            if not path.startswith(expected_prefix):
                errors.append(f"reports.{name} 必须位于 {expected_prefix}")

    if state != "planned":
        for key in ("owner", "base_commit", "branch", "worktree"):
            if not str(data.get(key, "")):
                errors.append(f"{state} 状态需要 {key}")
        if not str(data.get("branch", "")).startswith("codex/"):
            errors.append("可写任务分支必须以 codex/ 开头")
        if str(data.get("write_scope", "[]")) in {"", "[]"}:
            errors.append("可写任务必须声明非空 write_scope")

        lease = data.get("lease")
        if not isinstance(lease, dict):
            errors.append("可写任务需要 lease 映射")
        else:
            for key in ("holder", "issued_at", "expires_at"):
                if not str(lease.get(key, "")):
                    errors.append(f"可写任务需要 lease.{key}")

    acceptance = data.get("acceptance")
    if not isinstance(acceptance, dict):
        errors.append("acceptance 必须是映射")
    else:
        verdict = str(acceptance.get("verdict", ""))
        if verdict not in VALID_ACCEPTANCE_VERDICTS:
            errors.append(
                "acceptance.verdict 必须是以下值之一："
                f"{', '.join(sorted(VALID_ACCEPTANCE_VERDICTS))}"
            )
        if verdict == "approved":
            for key in ("approved_by", "approved_at"):
                if not str(acceptance.get(key, "")):
                    errors.append(f"acceptance.verdict 为 approved 时需要 acceptance.{key}")

    integration = data.get("integration")
    if not isinstance(integration, dict):
        errors.append("integration 必须是映射")
    else:
        cleanup = str(integration.get("cleanup", ""))
        if cleanup not in VALID_CLEANUP_STATES:
            errors.append(
                "integration.cleanup 必须是以下值之一："
                f"{', '.join(sorted(VALID_CLEANUP_STATES))}"
            )

        if state in {"integrating", "accepted"}:
            if not str(integration.get("merged_commit", "")):
                errors.append(f"{state} 状态需要 integration.merged_commit")
            if not isinstance(acceptance, dict) or str(acceptance.get("verdict", "")) != "approved":
                errors.append(f"{state} 状态需要 acceptance.verdict 为 approved")

        if state == "accepted" and cleanup != "completed":
            errors.append("accepted 状态需要 integration.cleanup 为 completed")

    return errors


# 入口只输出可直接用于任务状态迁移门禁的诊断，便于 Controller 安全重试。
def main() -> int:
    """读取状态文件并以非零状态码报告协议违规。"""
    parser = argparse.ArgumentParser(description="校验 Flutter 协作任务状态文件")
    parser.add_argument("state_file", type=Path)
    args = parser.parse_args()

    try:
        data = parse_restricted_yaml(args.state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"状态文件无效：{error}", file=sys.stderr)
        return 1

    errors = validate_task_state(data)
    if errors:
        for error in errors:
            print(f"状态文件无效：{error}", file=sys.stderr)
        return 1

    print(f"任务状态有效：{data['id']} ({data['state']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
