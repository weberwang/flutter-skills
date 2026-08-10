#!/usr/bin/env python3
"""确定性验证自适应布局实施规格。

验证器只检查规格的结构和显式矩阵字段，不扫描 Dart 源码，也不把实现信号
直接判为错误。这样实现者可以选择合适的 Flutter 原语，同时留下可复现依据。
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml


REQUIRED_TOP_LEVEL = (
    "page",
    "regions",
    "breakpoints",
    "content",
    "system_avoidance",
    "scroll",
    "text_behavior",
    "overlays",
    "implementation",
    "invariants",
    "implementation_signals",
    "evidence_matrix",
)
SIGNALS = {
    "Stack",
    "Positioned",
    "fixed_width",
    "fixed_height",
    "floating",
    "single_line_truncation",
    "handwritten_breakpoint",
}
ORIENTATIONS = {"portrait", "landscape"}
TEXT_SCALES = {"default", "large"}
LOCALES = {"default", "longest_copy"}
SAFE_AREAS = {"zero", "nonzero"}
ACTION_STATES = {"default", "disabled", "submitting"}


class ValidationErrors:
    """收集所有错误后统一输出，保证 CI 结果稳定且便于一次修复。"""

    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, message: str) -> None:
        self.items.append(message)

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.add(message)


def as_mapping(value: Any, path: str, errors: ValidationErrors) -> dict[str, Any]:
    """将 YAML 节点限制为映射，避免后续检查因类型错误崩溃。"""
    if not isinstance(value, dict):
        errors.add(f"{path} must be a mapping")
        return {}
    return value


def as_list(value: Any, path: str, errors: ValidationErrors) -> list[Any]:
    """将 YAML 节点限制为列表，同时保留可继续报告的空列表。"""
    if not isinstance(value, list):
        errors.add(f"{path} must be a list")
        return []
    return value


def non_empty_text(value: Any) -> bool:
    """判断字段是否为非空字符串。"""
    return isinstance(value, str) and bool(value.strip())


def positive_number(value: Any) -> bool:
    """判断尺寸或断点是否为正数。"""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def validate_page(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """验证页面目标尺寸和方向，防止实现只针对单一设备。"""
    page = as_mapping(spec.get("page"), "page", errors)
    errors.require(non_empty_text(page.get("id")), "page.id is required")
    for key in ("min_width", "max_width", "min_height", "max_height"):
        errors.require(positive_number(page.get(key)), f"page.{key} must be positive")
    if positive_number(page.get("min_width")) and positive_number(page.get("max_width")):
        errors.require(page["min_width"] <= page["max_width"], "page min_width must not exceed max_width")
    if positive_number(page.get("min_height")) and positive_number(page.get("max_height")):
        errors.require(page["min_height"] <= page["max_height"], "page min_height must not exceed max_height")
    orientation_values = as_list(page.get("orientations"), "page.orientations", errors)
    errors.require(all(isinstance(item, str) for item in orientation_values), "page.orientations must contain strings")
    orientations = {item for item in orientation_values if isinstance(item, str)}
    errors.require(ORIENTATIONS.issubset(orientations), "page.orientations must include portrait and landscape")


def validate_anchor(anchor: Any, path: str, errors: ValidationErrors) -> None:
    """验证单个锚点包含语义参照而不是裸坐标。"""
    mapping = as_mapping(anchor, path, errors)
    errors.require(non_empty_text(mapping.get("relation")), f"{path}.relation is required")
    reference = mapping.get("reference")
    errors.require(non_empty_text(reference), f"{path}.reference must name a semantic boundary")
    if isinstance(reference, str):
        errors.require(not any(token in reference.lower() for token in ("left:", "top:", "right:", "bottom:")), f"{path}.reference must not be a coordinate")


def validate_regions(spec: dict[str, Any], errors: ValidationErrors) -> set[str]:
    """验证区域的语义角色、双轴锚点和可增长尺寸。"""
    regions = as_list(spec.get("regions"), "regions", errors)
    errors.require(bool(regions), "regions must not be empty")
    ids: set[str] = set()
    for index, raw_region in enumerate(regions):
        path = f"regions[{index}]"
        region = as_mapping(raw_region, path, errors)
        region_id = region.get("id")
        errors.require(non_empty_text(region_id), f"{path}.id is required")
        if isinstance(region_id, str):
            errors.require(region_id not in ids, f"duplicate region id: {region_id}")
            ids.add(region_id)
        errors.require(non_empty_text(region.get("role")), f"{path}.role is required")
        anchors = as_mapping(region.get("anchors"), f"{path}.anchors", errors)
        for axis in ("horizontal", "vertical"):
            axis_anchors = as_mapping(anchors.get(axis), f"{path}.anchors.{axis}", errors)
            errors.require(bool(axis_anchors), f"{path}.anchors.{axis} must contain relative anchors")
            for anchor_name, anchor in axis_anchors.items():
                validate_anchor(anchor, f"{path}.anchors.{axis}.{anchor_name}", errors)
        sizes = as_mapping(region.get("size"), f"{path}.size", errors)
        for tier in ("min", "preferred", "max"):
            size = as_mapping(sizes.get(tier), f"{path}.size.{tier}", errors)
            errors.require("width" in size and "height" in size, f"{path}.size.{tier} requires width and height")
        if all(isinstance(sizes.get(tier), dict) for tier in ("min", "preferred", "max")):
            for dimension in ("width", "height"):
                values = [sizes[tier].get(dimension) for tier in ("min", "preferred", "max")]
                if all(isinstance(value, (int, float)) for value in values):
                    errors.require(values[0] <= values[1] <= values[2], f"{path}.size.{dimension} must satisfy min <= preferred <= max")
    return ids


def validate_breakpoints(spec: dict[str, Any], errors: ValidationErrors) -> dict[str, float]:
    """验证断点的触发条件和结构回退，并返回断点值供矩阵检查。"""
    breakpoints = as_list(spec.get("breakpoints"), "breakpoints", errors)
    errors.require(bool(breakpoints), "breakpoints must not be empty")
    values: dict[str, float] = {}
    for index, raw_breakpoint in enumerate(breakpoints):
        path = f"breakpoints[{index}]"
        breakpoint = as_mapping(raw_breakpoint, path, errors)
        identifier = breakpoint.get("id")
        errors.require(non_empty_text(identifier), f"{path}.id is required")
        if isinstance(identifier, str):
            errors.require(identifier not in values, f"duplicate breakpoint id: {identifier}")
        axis = breakpoint.get("axis")
        errors.require(axis in ("width", "height"), f"{path}.axis must be width or height")
        value = breakpoint.get("value")
        errors.require(positive_number(value), f"{path}.value must be positive")
        if isinstance(identifier, str) and isinstance(value, (int, float)):
            values[identifier] = float(value)
        for field in ("reason", "change", "preserves", "fallback"):
            if field == "preserves":
                preserve = breakpoint.get(field)
                errors.require(isinstance(preserve, list) and bool(preserve), f"{path}.preserves must be a non-empty list")
            else:
                errors.require(non_empty_text(breakpoint.get(field)), f"{path}.{field} is required")
    return values


def validate_content_and_system(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """验证内容容器、系统边界和文本增长策略。"""
    content = as_mapping(spec.get("content"), "content", errors)
    errors.require(positive_number(content.get("max_width")), "content.max_width must be positive")
    columns = as_mapping(content.get("columns"), "content.columns", errors)
    for key in ("min", "preferred", "max", "min_item_width"):
        errors.require(positive_number(columns.get(key)), f"content.columns.{key} must be positive")
    if all(isinstance(columns.get(key), (int, float)) for key in ("min", "preferred", "max")):
        errors.require(columns["min"] <= columns["preferred"] <= columns["max"], "content.columns must satisfy min <= preferred <= max")
    for key in ("gutter", "margins"):
        values = as_mapping(content.get(key), f"content.{key}", errors)
        for tier in ("min", "preferred", "max"):
            errors.require(positive_number(values.get(tier)), f"content.{key}.{tier} must be positive")
    errors.require(non_empty_text(content.get("insufficient_width_fallback")), "content.insufficient_width_fallback is required")

    system = as_mapping(spec.get("system_avoidance"), "system_avoidance", errors)
    for key in ("safe_area", "system_bars", "keyboard", "fold", "split"):
        entry = as_mapping(system.get(key), f"system_avoidance.{key}", errors)
        errors.require(bool(entry), f"system_avoidance.{key} is required")
    text = as_mapping(spec.get("text_behavior"), "text_behavior", errors)
    for key in ("localization", "rtl"):
        errors.require(text.get(key) is not None, f"text_behavior.{key} is required")
    scale = as_mapping(text.get("text_scale"), "text_behavior.text_scale", errors)
    errors.require(positive_number(scale.get("default")), "text_behavior.text_scale.default must be positive")
    errors.require(positive_number(scale.get("large")) and scale.get("large", 0) > 1, "text_behavior.text_scale.large must exceed 1")
    errors.require(scale.get("default") != scale.get("large"), "text_behavior.text_scale.default and large must differ")
    for key in ("wrap", "growth"):
        errors.require(non_empty_text(text.get(key)), f"text_behavior.{key} is required")
    errors.require(text.get("critical_actions_allow_truncation") is False, "critical actions must forbid truncation")


def validate_scroll(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """要求每个轴声明唯一 owner，即使该轴明确不滚动。"""
    scroll = as_mapping(spec.get("scroll"), "scroll", errors)
    for axis in ("vertical", "horizontal"):
        entry = as_mapping(scroll.get(axis), f"scroll.{axis}", errors)
        owner = entry.get("owner")
        errors.require(non_empty_text(owner), f"scroll.{axis}.owner is required; use none for an explicit non-scrolling axis")
        errors.require(non_empty_text(entry.get("semantics")), f"scroll.{axis}.semantics is required")
        errors.require(non_empty_text(entry.get("narrow_height_fallback")), f"scroll.{axis}.narrow_height_fallback is required")


def validate_overlays(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """验证固定、悬浮、吸顶和停靠层具有避让、命中和回退规则。"""
    overlays = as_list(spec.get("overlays"), "overlays", errors)
    for index, raw_overlay in enumerate(overlays):
        path = f"overlays[{index}]"
        overlay = as_mapping(raw_overlay, path, errors)
        errors.require(non_empty_text(overlay.get("id")), f"{path}.id is required")
        errors.require(overlay.get("behavior") in ("fixed", "floating", "pinned", "docked"), f"{path}.behavior must be fixed/floating/pinned/docked")
        validate_anchor(overlay.get("anchor"), f"{path}.anchor", errors)
        for key in ("occlusion", "keyboard_fallback", "narrow_height_fallback"):
            errors.require(non_empty_text(overlay.get(key)), f"{path}.{key} is required")
        hit = as_mapping(overlay.get("hit_target"), f"{path}.hit_target", errors)
        errors.require(positive_number(hit.get("min_width")) and positive_number(hit.get("min_height")), f"{path}.hit_target requires positive min_width/min_height")


def validate_implementation(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """验证共享断点、根布局和约束原语来源。"""
    implementation = as_mapping(spec.get("implementation"), "implementation", errors)
    for key in ("breakpoint_resolver", "root_layout"):
        errors.require(non_empty_text(implementation.get(key)), f"implementation.{key} is required")
    primitives = implementation.get("constraint_primitives")
    errors.require(isinstance(primitives, list) and bool(primitives), "implementation.constraint_primitives must be non-empty")


def validate_invariants(spec: dict[str, Any], errors: ValidationErrors) -> dict[str, set[str]]:
    """验证每条关系不变量都绑定参数化 test id。"""
    invariants = as_list(spec.get("invariants"), "invariants", errors)
    errors.require(bool(invariants), "invariants must not be empty")
    result: dict[str, set[str]] = {}
    invariant_ids: set[str] = set()
    for index, raw_invariant in enumerate(invariants):
        path = f"invariants[{index}]"
        invariant = as_mapping(raw_invariant, path, errors)
        identifier = invariant.get("id")
        errors.require(non_empty_text(identifier), f"{path}.id is required")
        if isinstance(identifier, str):
            errors.require(identifier not in invariant_ids, f"duplicate invariant id: {identifier}")
            invariant_ids.add(identifier)
        test_ids = invariant.get("test_ids")
        valid_test_ids = isinstance(test_ids, list) and bool(test_ids) and all(non_empty_text(item) for item in test_ids)
        errors.require(valid_test_ids, f"{path}.test_ids must be non-empty strings")
        if isinstance(identifier, str):
            result[identifier] = set(test_ids) if valid_test_ids else set()
        errors.require(non_empty_text(invariant.get("relation")), f"{path}.relation is required")
    return result


def validate_signals(spec: dict[str, Any], errors: ValidationErrors) -> dict[str, set[str]]:
    """验证实现信号的依据字段，并返回信号到 test id 的映射。"""
    signals = as_list(spec.get("implementation_signals"), "implementation_signals", errors)
    found: dict[str, set[str]] = {}
    for index, raw_signal in enumerate(signals):
        path = f"implementation_signals[{index}]"
        signal = as_mapping(raw_signal, path, errors)
        name = signal.get("signal")
        errors.require(isinstance(name, str) and name in SIGNALS, f"{path}.signal must be one of {sorted(SIGNALS)}")
        for key in ("reason", "boundary", "fallback"):
            errors.require(non_empty_text(signal.get(key)), f"{path}.{key} is required")
        ids = signal.get("test_ids")
        valid_ids = isinstance(ids, list) and bool(ids) and all(non_empty_text(item) for item in ids)
        errors.require(valid_ids, f"{path}.test_ids must be non-empty strings")
        if isinstance(name, str):
            found.setdefault(name, set()).update(ids if valid_ids else ())
    return found


def validate_matrix(spec: dict[str, Any], breakpoints: dict[str, float], invariant_tests: dict[str, set[str]], signal_tests: dict[str, set[str]], errors: ValidationErrors) -> None:
    """按显式字段验证最小充分矩阵，而不是信任 covers 标签。"""
    matrix = as_mapping(spec.get("evidence_matrix"), "evidence_matrix", errors)
    cases = as_list(matrix.get("cases"), "evidence_matrix.cases", errors)
    errors.require(bool(cases), "evidence_matrix.cases must not be empty")
    offsets: dict[str, set[int]] = defaultdict(set)
    dimensions_by_group: dict[str, set[tuple[float, float]]] = defaultdict(set)
    seen: dict[str, set[str]] = {"orientation": set(), "text_scale": set(), "locale": set(), "safe_area": set(), "action_state": set()}
    case_ids: set[str] = set()
    test_coverage: set[str] = set()
    text_scale_config = as_mapping(as_mapping(spec.get("text_behavior"), "text_behavior", errors).get("text_scale"), "text_behavior.text_scale", errors)
    default_scale = text_scale_config.get("default")
    large_scale = text_scale_config.get("large")
    for index, raw_case in enumerate(cases):
        path = f"evidence_matrix.cases[{index}]"
        case = as_mapping(raw_case, path, errors)
        identifier = case.get("id")
        errors.require(non_empty_text(identifier), f"{path}.id is required")
        if isinstance(identifier, str):
            errors.require(identifier not in case_ids, f"duplicate evidence case id: {identifier}")
            case_ids.add(identifier)
        errors.require(positive_number(case.get("width")) and positive_number(case.get("height")), f"{path}.width and height must be positive")
        orientation = case.get("orientation")
        errors.require(isinstance(orientation, str) and orientation in ORIENTATIONS, f"{path}.orientation must be portrait or landscape")
        if isinstance(orientation, str) and orientation in ORIENTATIONS:
            seen["orientation"].add(orientation)
        text_scale = case.get("text_scale")
        errors.require(isinstance(text_scale, (int, float)) and not isinstance(text_scale, bool), f"{path}.text_scale must be numeric")
        if isinstance(text_scale, (int, float)) and not isinstance(text_scale, bool):
            errors.require(text_scale in (default_scale, large_scale), f"{path}.text_scale must equal text_behavior.text_scale.default or large")
            if text_scale == default_scale:
                seen["text_scale"].add("default")
            elif text_scale == large_scale:
                seen["text_scale"].add("large")
            else:
                seen["text_scale"].add("other")
        locale = case.get("locale")
        errors.require(isinstance(locale, str) and locale in LOCALES, f"{path}.locale must be default or longest_copy")
        if isinstance(locale, str) and locale in LOCALES:
            seen["locale"].add(locale)
        safe_area = case.get("safe_area")
        errors.require(isinstance(safe_area, str) and safe_area in SAFE_AREAS, f"{path}.safe_area must be zero or nonzero")
        if isinstance(safe_area, str) and safe_area in SAFE_AREAS:
            seen["safe_area"].add(safe_area)
        action_state = case.get("action_state")
        errors.require(isinstance(action_state, str) and action_state in ACTION_STATES, f"{path}.action_state must be default/disabled/submitting")
        if isinstance(action_state, str) and action_state in ACTION_STATES:
            seen["action_state"].add(action_state)
        edge = case.get("breakpoint_edge")
        if edge is not None:
            edge_mapping = as_mapping(edge, f"{path}.breakpoint_edge", errors)
            breakpoint_id = edge_mapping.get("id")
            offset = edge_mapping.get("offset")
            known_breakpoint = isinstance(breakpoint_id, str) and breakpoint_id in breakpoints
            errors.require(known_breakpoint, f"{path}.breakpoint_edge.id must reference a breakpoint")
            errors.require(offset in (-1, 0, 1), f"{path}.breakpoint_edge.offset must be -1, 0, or +1")
            if known_breakpoint and offset in (-1, 0, 1):
                offsets[breakpoint_id].add(offset)
                edge_axis = next((item.get("axis") for item in as_list(spec.get("breakpoints"), "breakpoints", errors) if isinstance(item, dict) and item.get("id") == breakpoint_id), "width")
                actual = case.get("width" if edge_axis == "width" else "height")
                errors.require(isinstance(actual, (int, float)) and actual == breakpoints[breakpoint_id] + offset, f"{path} dimensions must equal breakpoint value plus offset")
        group = case.get("same_width_group")
        if group is not None and non_empty_text(group) and isinstance(case.get("width"), (int, float)) and isinstance(case.get("height"), (int, float)):
            dimensions_by_group[group].add((float(case["width"]), float(case["height"])))
        ids = case.get("test_ids")
        valid_ids = isinstance(ids, list) and bool(ids) and all(non_empty_text(item) for item in ids)
        errors.require(valid_ids, f"{path}.test_ids must be a non-empty list of strings")
        if valid_ids:
            test_coverage.update(ids)
    for breakpoint_id in breakpoints:
        errors.require(offsets[breakpoint_id] == {-1, 0, 1}, f"evidence_matrix must cover {breakpoint_id} at b-1, b, and b+1")
    errors.require(any(len({width for width, _ in dimensions}) == 1 and len({height for _, height in dimensions}) >= 2 for dimensions in dimensions_by_group.values()), "evidence_matrix must include same-width different-height cases")
    errors.require(seen["orientation"] == ORIENTATIONS, "evidence_matrix must cover portrait and landscape")
    errors.require(seen["text_scale"] == TEXT_SCALES, "evidence_matrix must cover default and large text scale")
    errors.require(seen["locale"] == LOCALES, "evidence_matrix must cover default and longest_copy locale")
    errors.require(seen["safe_area"] == SAFE_AREAS, "evidence_matrix must cover zero and nonzero safe area")
    errors.require(seen["action_state"] == ACTION_STATES, "evidence_matrix must cover default, disabled, and submitting actions")
    invariant_test_ids = set().union(*invariant_tests.values()) if invariant_tests else set()
    for invariant_id, test_ids in invariant_tests.items():
        missing = sorted(test_ids - test_coverage)
        errors.require(not missing, f"invariant {invariant_id} test ids missing from evidence_matrix: {', '.join(missing)}")
    for signal_name, test_ids in signal_tests.items():
        undeclared = sorted(test_ids - invariant_test_ids)
        errors.require(not undeclared, f"implementation signal {signal_name} references undeclared test ids: {', '.join(undeclared)}")
        unexecuted = sorted(test_ids - test_coverage)
        errors.require(not unexecuted, f"implementation signal {signal_name} test ids missing from evidence_matrix: {', '.join(unexecuted)}")


def validate(spec: dict[str, Any]) -> tuple[list[str], set[str]]:
    """执行完整校验并返回错误和 implementation_attention 信号。"""
    errors = ValidationErrors()
    for key in REQUIRED_TOP_LEVEL:
        errors.require(key in spec, f"missing top-level field: {key}")
    validate_page(spec, errors)
    validate_regions(spec, errors)
    breakpoints = validate_breakpoints(spec, errors)
    validate_content_and_system(spec, errors)
    validate_scroll(spec, errors)
    validate_overlays(spec, errors)
    validate_implementation(spec, errors)
    invariant_tests = validate_invariants(spec, errors)
    signals = validate_signals(spec, errors)
    validate_matrix(spec, breakpoints, invariant_tests, signals, errors)
    return errors.items, set(signals)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    """解析规格路径和可选 JSON 输出开关。"""
    parser = argparse.ArgumentParser(description="Validate an adaptive layout implementation specification")
    parser.add_argument("spec", type=Path, help="layout-spec.yaml path")
    parser.add_argument("--json", action="store_true", help="emit a machine-readable result")
    return parser.parse_args(list(argv))


def _resolve_fixture_path(root: dict[str, Any], path: str) -> tuple[dict[str, Any], str]:
    """解析夹具 mutation 的点号路径。"""
    parts = path.split(".")
    parent: Any = root
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if not isinstance(parent, dict):
        raise ValueError(f"mutation parent is not a mapping: {path}")
    return parent, parts[-1]


def _apply_fixture_mutation(spec: dict[str, Any], mutation: dict[str, Any]) -> None:
    """应用夹具声明的有限 mutation，便于直接验证负向样例。"""
    parent, key = _resolve_fixture_path(spec, mutation["path"])
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
    else:
        raise ValueError(f"unknown mutation operation: {operation}")


def load_spec(path: Path) -> dict[str, Any]:
    """读取普通规格，或展开 scripts/fixtures 下的可复现规格夹具。"""
    with path.open("r", encoding="utf-8") as handle:
        document = yaml.safe_load(handle)
    if not isinstance(document, dict):
        raise ValueError("root YAML value must be a mapping")
    if "source" not in document or "expected" not in document:
        return document
    source_path = (path.parent / document["source"]).resolve()
    with source_path.open("r", encoding="utf-8") as handle:
        source = yaml.safe_load(handle)
    if not isinstance(source, dict):
        raise ValueError(f"fixture source is not a mapping: {source_path}")
    for mutation in document.get("mutations", []):
        _apply_fixture_mutation(source, mutation)
    return source


def main(argv: Iterable[str] | None = None) -> int:
    """读取 YAML、运行验证并返回 CI 可用的退出码。"""
    args = parse_args(argv or sys.argv[1:])
    try:
        spec = load_spec(args.spec)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"[FAIL] cannot read {args.spec}: {exc}")
        return 1
    errors, signals = validate(spec)
    if errors:
        if args.json:
            print(yaml.safe_dump({"valid": False, "errors": errors}, allow_unicode=True, sort_keys=True))
        else:
            for error in errors:
                print(f"[FAIL] {error}")
        return 1
    attention = sorted(signals)
    if args.json:
        print(yaml.safe_dump({"valid": True, "implementation_attention": attention}, allow_unicode=True, sort_keys=True))
    else:
        print(f"[PASS] {args.spec}")
        if attention:
            print(f"implementation_attention={','.join(attention)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
