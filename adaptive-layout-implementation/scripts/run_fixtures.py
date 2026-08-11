#!/usr/bin/env python3
"""运行布局规格夹具，验证正例、负例和实现信号提示。"""

from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any

import yaml

# 兼容从仓库根目录或 scripts 目录启动，确保能加载同目录验证器。
sys.path.insert(0, str(Path(__file__).parent))
from validate_layout_spec import validate


def _load(path: Path) -> dict[str, Any]:
    """读取夹具或规格 YAML。"""
    with path.open("r", encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must be a mapping")
    return value


def _resolve(root: dict[str, Any], path: str) -> tuple[dict[str, Any], str]:
    """解析点号路径，返回父映射和末级键。"""
    parts = path.split(".")
    parent: Any = root
    for part in parts[:-1]:
        if isinstance(parent, list):
            parent = parent[int(part)]
        else:
            parent = parent[part]
    if not isinstance(parent, dict):
        raise ValueError(f"mutation parent is not a mapping: {path}")
    return parent, parts[-1]


def _mutate(spec: dict[str, Any], mutation: dict[str, Any]) -> None:
    """执行有限的 remove/set/append/duplicate 操作，保持夹具声明可审阅。"""
    parent, key = _resolve(spec, mutation["path"])
    operation = mutation["op"]
    if operation == "remove":
        parent.pop(key, None)
    elif operation == "set":
        parent[key] = mutation.get("value")
    elif operation == "append":
        target = parent.get(key)
        if not isinstance(target, list):
            raise ValueError(f"append target is not a list: {mutation['path']}")
        target.append(mutation.get("value"))
    elif operation == "duplicate":
        target = parent.get(key)
        if not isinstance(target, list):
            raise ValueError(f"duplicate target is not a list: {mutation['path']}")
        source_index = mutation.get("source_index", 0)
        target.append(copy.deepcopy(target[source_index]))
    else:
        raise ValueError(f"unknown mutation operation: {operation}")


def run_fixture(path: Path) -> bool:
    """运行单个夹具并比较预期退出状态及提示信号。"""
    descriptor = _load(path)
    source_path = (path.parent / descriptor["source"]).resolve()
    spec = _load(source_path)
    for mutation in descriptor.get("mutations", []):
        _mutate(spec, mutation)
    errors, attention = validate(spec)
    passed = not errors
    expected = descriptor.get("expected") == "pass"
    attention_ok = sorted(attention) == sorted(descriptor.get("expected_attention", []))
    result = passed == expected and attention_ok
    label = "PASS" if result else "FAIL"
    detail = "valid" if passed else "; ".join(errors)
    print(f"[{label}] {path.name}: {detail}")
    if attention:
        print(f"  implementation_attention={','.join(sorted(attention))}")
    return result


def main() -> int:
    """运行 fixtures 目录下全部 YAML 夹具。"""
    fixture_dir = Path(__file__).with_name("fixtures")
    paths = sorted(fixture_dir.glob("*.yaml"))
    if not paths:
        print("[FAIL] no fixtures found")
        return 1
    return 0 if all(run_fixture(path) for path in paths) else 1


if __name__ == "__main__":
    raise SystemExit(main())
