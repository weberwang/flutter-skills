#!/usr/bin/env python3
"""校验并行写入任务使用的受限 YAML 状态文件。"""

import argparse
import re
import sys
from pathlib import Path


VALID_STATES = {"planned", "claimed", "implementing", "reviewing", "blocked"}
VALID_RISK_TIERS = {"standard", "high", "release"}
VALID_VALIDATION_STATES = {"pending", "passed"}
VALID_ACCEPTANCE_VERDICTS = {"pending", "approved", "changes_requested"}
REQUIRED_ROOT_KEYS = {
    "id",
    "risk_tier",
    "state",
    "owner",
    "lease",
    "base_commit",
    "branch",
    "worktree",
    "write_scope",
    "validation",
    "candidate_commit",
    "review",
    "acceptance",
    "blocker",
}


# 仅解析模板实际使用的两层 YAML，避免为短生命周期状态引入第三方依赖。
def parse_restricted_yaml(content: str) -> dict[str, object]:
    """将允许的标量和二层映射解析为字典。"""
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

        raw_value = value.strip()
        normalized = raw_value.strip('"')
        if indent == 0:
            if raw_value == '""':
                result[key] = ""
                section = None
            elif normalized:
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


def validate_task_state(data: dict[str, object]) -> list[str]:
    """返回并行任务状态中所有不符合协议的错误。"""
    errors: list[str] = []
    missing = REQUIRED_ROOT_KEYS - data.keys()
    if missing:
        errors.append(f"缺少根字段：{', '.join(sorted(missing))}")

    task_id = str(data.get("id", ""))
    state = str(data.get("state", ""))
    validation = str(data.get("validation", ""))
    if not task_id:
        errors.append("id 不能为空")
    if str(data.get("risk_tier", "")) not in VALID_RISK_TIERS:
        errors.append(f"risk_tier 必须是以下值之一：{', '.join(sorted(VALID_RISK_TIERS))}")
    if state not in VALID_STATES:
        errors.append(f"state 必须是以下值之一：{', '.join(sorted(VALID_STATES))}")
    if validation not in VALID_VALIDATION_STATES:
        errors.append(
            "validation 必须是以下值之一："
            f"{', '.join(sorted(VALID_VALIDATION_STATES))}"
        )

    if state != "planned":
        for key in ("owner", "base_commit", "branch", "worktree"):
            if not str(data.get(key, "")):
                errors.append(f"{state} 状态需要 {key}")
        if not str(data.get("branch", "")).startswith("codex/"):
            errors.append("并行写入分支必须以 codex/ 开头")
        if str(data.get("write_scope", "[]")) in {"", "[]"}:
            errors.append("并行写入任务必须声明非空 write_scope")

        lease = data.get("lease")
        if not isinstance(lease, dict):
            errors.append("并行写入任务需要 lease 映射")
        else:
            for key in ("holder", "issued_at", "expires_at"):
                if not str(lease.get(key, "")):
                    errors.append(f"并行写入任务需要 lease.{key}")

    if state == "reviewing":
        if validation != "passed":
            errors.append("reviewing 状态需要 validation 为 passed")
        if not str(data.get("candidate_commit", "")):
            errors.append("reviewing 状态需要 candidate_commit")

    review = str(data.get("review", ""))
    if task_id and not review.startswith(f"docs/tasks/{task_id}/"):
        errors.append(f"review 必须位于 docs/tasks/{task_id}/")

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

    return errors


def main() -> int:
    """读取状态文件并以非零退出码报告协议错误。"""
    parser = argparse.ArgumentParser(description="校验并行 Flutter 任务状态文件")
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
