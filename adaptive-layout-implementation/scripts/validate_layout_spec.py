#!/usr/bin/env python3
"""确定性验证两阶段布局规格的结构、关系复算和证据元数据。"""

from __future__ import annotations

import argparse
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


COMMON_FIELDS = (
    "phase", "page", "regions", "breakpoints", "content", "system_avoidance",
    "scroll", "text_behavior", "overlays", "implementation", "invariants",
    "implementation_signals", "evidence_matrix",
)
SIGNALS = {"Stack", "Positioned", "fixed_width", "fixed_height", "floating", "single_line_truncation", "handwritten_breakpoint"}
H_TYPES = {"start", "end", "center", "intentionally-offset"}
V_TYPES = {"top", "bottom", "center", "intentionally-offset"}
ABSOLUTE_RELATION = re.compile(r"^\s*[xy]\s*=")
RELATION_OPERATOR = re.compile(r"(?:==|<=|>=|<|>)")
SEMANTIC_REFERENCE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*(?:\.[A-Za-z_][A-Za-z0-9_-]*)*$")
COORDINATE_REFERENCE = re.compile(r"^\s*(?:left|top|right|bottom|x|y)\s*:", re.IGNORECASE)
SHA256 = re.compile(r"^[0-9a-f]{64}$")
CODE_SHA = re.compile(r"^[0-9a-f]{40,64}$")
ORIENTATIONS = {"portrait", "landscape"}
LOCALES = {"default", "longest_copy"}
SAFE_AREAS = {"zero", "nonzero"}
ACTION_STATES = {"default", "disabled", "submitting"}
OVERLAY_BEHAVIORS = {"fixed", "floating", "pinned", "docked"}


class ValidationErrors:
    """累积错误，保证一次验证能返回全部确定性缺口。"""

    def __init__(self) -> None:
        self.items: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        """条件失败时记录错误。"""
        if not condition:
            self.items.append(message)


def mapping(value: Any) -> dict[str, Any]:
    """把未知 YAML 节点安全收窄为映射。"""
    return value if isinstance(value, dict) else {}


def sequence(value: Any) -> list[Any]:
    """把未知 YAML 节点安全收窄为列表。"""
    return value if isinstance(value, list) else []


def text(value: Any) -> bool:
    """判断字段是否为非空文本。"""
    return isinstance(value, str) and bool(value.strip())


def number(value: Any) -> bool:
    """判断字段是否为有限数值且排除布尔值。"""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def semantic_relation(value: Any) -> bool:
    """判断关系式是否引用语义节点/边界并包含可比较运算符。"""
    return text(value) and "." in value and bool(RELATION_OPERATOR.search(value)) and not bool(ABSOLUTE_RELATION.match(value))


def validate_anchor(value: Any, path: str, errors: ValidationErrors) -> None:
    """验证锚点使用语义参照，而不是裸坐标或空映射。"""
    anchor = mapping(value)
    errors.require(text(anchor.get("relation")), f"{path}.relation is required")
    reference = anchor.get("reference")
    errors.require(
        isinstance(reference, str)
        and bool(SEMANTIC_REFERENCE.fullmatch(reference.strip()))
        and not bool(COORDINATE_REFERENCE.match(reference)),
        f"{path}.reference must be a stable semantic identifier or dotted boundary",
    )


def validate_regions(spec: dict[str, Any], errors: ValidationErrors) -> None:
    """验证页面区域及双轴锚点。"""
    regions = sequence(spec.get("regions"))
    errors.require(bool(regions), "regions must be non-empty")
    for index, raw in enumerate(regions):
        region = mapping(raw)
        path = f"regions[{index}]"
        errors.require(text(region.get("id")), f"{path}.id is required")
        errors.require(text(region.get("role")), f"{path}.role is required")
        anchors = mapping(region.get("anchors"))
        for axis in ("horizontal", "vertical"):
            axis_anchors = mapping(anchors.get(axis))
            errors.require(bool(axis_anchors), f"{path}.anchors.{axis} is required")
            for name, anchor in axis_anchors.items():
                validate_anchor(anchor, f"{path}.anchors.{axis}.{name}", errors)
        sizes = mapping(region.get("size"))
        errors.require(bool(sizes), f"{path}.size is required")
        for tier in ("min", "preferred", "max"):
            size = mapping(sizes.get(tier))
            errors.require("width" in size and "height" in size, f"{path}.size.{tier} requires width and height")
        for dimension in ("width", "height"):
            values = [mapping(sizes.get(tier)).get(dimension) for tier in ("min", "preferred", "max")]
            if all(number(item) for item in values):
                errors.require(values[0] <= values[1] <= values[2], f"{path}.size.{dimension} must satisfy min <= preferred <= max")


def validate_common(spec: dict[str, Any], errors: ValidationErrors) -> tuple[set[str], set[str]]:
    """验证 sketch 与 fidelity 共用的结构合同。"""
    for field in COMMON_FIELDS:
        errors.require(field in spec, f"{field} is required")
    page = mapping(spec.get("page"))
    errors.require(text(page.get("id")), "page.id is required")
    for field in ("min_width", "max_width", "min_height", "max_height"):
        errors.require(number(page.get(field)) and page[field] > 0, f"page.{field} must be positive")
    if all(number(page.get(field)) for field in ("min_width", "max_width")):
        errors.require(page["min_width"] <= page["max_width"], "page width range is invalid")
    if all(number(page.get(field)) for field in ("min_height", "max_height")):
        errors.require(page["min_height"] <= page["max_height"], "page height range is invalid")
    errors.require({"portrait", "landscape"} <= set(sequence(page.get("orientations"))), "page.orientations must include portrait and landscape")
    validate_regions(spec, errors)
    breakpoints = sequence(spec.get("breakpoints"))
    errors.require(bool(breakpoints), "breakpoints must be non-empty")
    breakpoint_by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(breakpoints):
        item = mapping(raw)
        for field in ("id", "axis", "reason", "change", "fallback"):
            errors.require(text(item.get(field)), f"breakpoints[{index}].{field} is required")
        errors.require(item.get("axis") in {"width", "height"}, f"breakpoints[{index}].axis must be width or height")
        errors.require(number(item.get("value")) and item["value"] > 0, f"breakpoints[{index}].value must be positive")
        errors.require(bool(sequence(item.get("preserves"))), f"breakpoints[{index}].preserves must be non-empty")
        if text(item.get("id")):
            errors.require(item["id"] not in breakpoint_by_id, f"duplicate breakpoint id: {item['id']}")
            breakpoint_by_id[item["id"]] = item
    for field in ("content", "system_avoidance", "scroll", "text_behavior", "implementation"):
        errors.require(bool(mapping(spec.get(field))), f"{field} must be a non-empty mapping")
    content = mapping(spec.get("content"))
    errors.require(number(content.get("max_width")) and content["max_width"] > 0, "content.max_width must be positive")
    columns = mapping(content.get("columns"))
    for field in ("min", "preferred", "max", "min_item_width"):
        errors.require(number(columns.get(field)) and columns[field] > 0, f"content.columns.{field} must be positive")
    if all(number(columns.get(field)) for field in ("min", "preferred", "max")):
        errors.require(columns["min"] <= columns["preferred"] <= columns["max"], "content.columns must satisfy min <= preferred <= max")
    for group in ("gutter", "margins"):
        values = mapping(content.get(group))
        for field in ("min", "preferred", "max"):
            errors.require(number(values.get(field)) and values[field] > 0, f"content.{group}.{field} must be positive")
        if all(number(values.get(field)) for field in ("min", "preferred", "max")):
            errors.require(values["min"] <= values["preferred"] <= values["max"], f"content.{group} must satisfy min <= preferred <= max")
    errors.require(text(content.get("insufficient_width_fallback")), "content.insufficient_width_fallback is required")
    avoidance = mapping(spec.get("system_avoidance"))
    for field in ("safe_area", "system_bars", "keyboard", "fold", "split"):
        errors.require(bool(mapping(avoidance.get(field))), f"system_avoidance.{field} is required")
    scroll = mapping(spec.get("scroll"))
    for axis in ("vertical", "horizontal"):
        axis_scroll = mapping(scroll.get(axis))
        for field in ("owner", "semantics", "narrow_height_fallback"):
            errors.require(text(axis_scroll.get(field)), f"scroll.{axis}.{field} is required")
    text_behavior = mapping(spec.get("text_behavior"))
    errors.require({"default", "longest_copy"} <= set(sequence(text_behavior.get("localization"))), "text_behavior.localization must include default and longest_copy")
    for field in ("rtl", "wrap", "growth"):
        errors.require(text(text_behavior.get(field)), f"text_behavior.{field} is required")
    text_scale = mapping(text_behavior.get("text_scale"))
    default_scale = text_scale.get("default")
    large_scale = text_scale.get("large")
    errors.require(number(default_scale) and default_scale > 0, "text_behavior.text_scale.default must be positive")
    errors.require(number(large_scale) and large_scale > 1, "text_behavior.text_scale.large must be greater than 1")
    if number(default_scale) and number(large_scale):
        errors.require(not math.isclose(default_scale, large_scale), "text_behavior text scales must differ")
    errors.require(text_behavior.get("critical_actions_allow_truncation") is False, "critical actions must not allow truncation")
    overlays = sequence(spec.get("overlays"))
    for index, raw in enumerate(overlays):
        overlay = mapping(raw)
        path = f"overlays[{index}]"
        for field in ("id", "behavior", "occlusion", "keyboard_fallback", "narrow_height_fallback"):
            errors.require(text(overlay.get(field)), f"{path}.{field} is required")
        errors.require(overlay.get("behavior") in OVERLAY_BEHAVIORS, f"{path}.behavior must be fixed, floating, pinned, or docked")
        validate_anchor(overlay.get("anchor"), f"{path}.anchor", errors)
        hit_target = mapping(overlay.get("hit_target"))
        for field in ("min_width", "min_height"):
            errors.require(number(hit_target.get(field)) and hit_target[field] > 0, f"{path}.hit_target.{field} must be positive")
    implementation = mapping(spec.get("implementation"))
    for field in ("breakpoint_resolver", "root_layout"):
        errors.require(text(implementation.get(field)), f"implementation.{field} is required")
    primitives = sequence(implementation.get("constraint_primitives"))
    errors.require(bool(primitives) and all(text(primitive) for primitive in primitives), "implementation.constraint_primitives must be a non-empty string list")
    invariants = sequence(spec.get("invariants"))
    errors.require(bool(invariants), "invariants must be non-empty")
    invariant_tests: set[str] = set()
    for index, raw in enumerate(invariants):
        item = mapping(raw)
        errors.require(text(item.get("id")) and text(item.get("relation")), f"invariants[{index}] requires id and relation")
        tests = sequence(item.get("test_ids"))
        errors.require(bool(tests) and all(text(test) for test in tests), f"invariants[{index}].test_ids must be non-empty")
        invariant_tests.update(test for test in tests if text(test))
    cases = sequence(mapping(spec.get("evidence_matrix")).get("cases"))
    errors.require(bool(cases), "evidence_matrix.cases must be non-empty")
    executed: set[str] = set()
    edge_offsets: dict[str, set[int]] = defaultdict(set)
    matrix_values: dict[str, set[Any]] = defaultdict(set)
    heights_by_width: dict[float, set[float]] = defaultdict(set)
    for index, raw in enumerate(cases):
        case = mapping(raw)
        path = f"evidence_matrix.cases[{index}]"
        for field in ("id", "orientation", "locale", "safe_area", "action_state"):
            errors.require(text(case.get(field)), f"{path}.{field} is required")
        errors.require(case.get("orientation") in ORIENTATIONS, f"{path}.orientation is invalid")
        errors.require(case.get("locale") in LOCALES, f"{path}.locale is invalid")
        errors.require(case.get("safe_area") in SAFE_AREAS, f"{path}.safe_area is invalid")
        errors.require(case.get("action_state") in ACTION_STATES, f"{path}.action_state is invalid")
        for field in ("width", "height", "text_scale"):
            errors.require(number(case.get(field)), f"{path}.{field} must be numeric")
        for field in ("orientation", "locale", "safe_area", "action_state", "text_scale"):
            matrix_values[field].add(case.get(field))
        if number(case.get("width")) and number(case.get("height")):
            heights_by_width[float(case["width"])].add(float(case["height"]))
        tests = sequence(case.get("test_ids"))
        errors.require(bool(tests) and all(text(test) for test in tests), f"{path}.test_ids must be a non-empty string list")
        executed.update(test for test in tests if text(test))
        edge = mapping(case.get("breakpoint_edge"))
        if text(edge.get("id")) and edge.get("offset") in (-1, 0, 1):
            edge_offsets[edge["id"]].add(edge["offset"])
            breakpoint = breakpoint_by_id.get(edge["id"])
            errors.require(breakpoint is not None, f"{path}.breakpoint_edge.id is unknown")
            if breakpoint is not None and number(breakpoint.get("value")):
                axis = breakpoint.get("axis")
                errors.require(axis in {"width", "height"}, f"breakpoint {edge['id']} axis must be width or height")
                if axis in {"width", "height"} and number(case.get(axis)):
                    expected = breakpoint["value"] + edge["offset"]
                    errors.require(math.isclose(case[axis], expected, abs_tol=1e-9), f"{path}.{axis} must equal breakpoint value + offset ({expected})")
    errors.require(invariant_tests <= executed, "every invariant test_id must execute in evidence_matrix")
    errors.require({"portrait", "landscape"} <= matrix_values["orientation"], "evidence_matrix must cover portrait and landscape")
    errors.require({"default", "longest_copy"} <= matrix_values["locale"], "evidence_matrix must cover default and longest_copy")
    errors.require({"zero", "nonzero"} <= matrix_values["safe_area"], "evidence_matrix must cover zero and nonzero safe areas")
    errors.require({"default", "disabled", "submitting"} <= matrix_values["action_state"], "evidence_matrix must cover all critical action states")
    if number(default_scale) and number(large_scale):
        errors.require({default_scale, large_scale} <= matrix_values["text_scale"], "evidence_matrix must cover declared default and large text scales")
    errors.require(any(len(heights) > 1 for heights in heights_by_width.values()), "evidence_matrix must cover same width with different heights")
    for raw in sequence(spec.get("breakpoints")):
        breakpoint = mapping(raw)
        identifier = breakpoint.get("id")
        errors.require(text(identifier), "every breakpoint requires id")
        if text(identifier):
            errors.require(edge_offsets[identifier] == {-1, 0, 1}, f"breakpoint {identifier} requires b-1/b/b+1 evidence")
    return invariant_tests, executed


def validate_optical(optical: dict[str, Any], path: str, errors: ValidationErrors) -> None:
    """验证几何中心、可见光学中心及偏移证据。"""
    for field in ("offset_x", "offset_y"):
        errors.require(number(optical.get(field)), f"{path}.{field} must be numeric")
    errors.require(text(optical.get("node_or_container_center")), f"{path}.node_or_container_center is required")
    errors.require(text(optical.get("visible_optical_center")), f"{path}.visible_optical_center is required")
    errors.require(optical.get("unresolved") is False, f"{path}.unresolved must be false")
    nonzero = any(number(optical.get(field)) and not math.isclose(optical[field], 0, abs_tol=1e-9) for field in ("offset_x", "offset_y"))
    if nonzero:
        errors.require(text(optical.get("evidence")), f"{path}.evidence is required for non-zero optical offset")


def validate_geometry(geometry: dict[str, Any], path: str, errors: ValidationErrors) -> None:
    """验证 target/Flutter 边界并复算中心。"""
    for side in ("target", "flutter"):
        item = mapping(geometry.get(side))
        for field in ("x", "y", "width", "height", "center_x", "center_y", "reference_center_x", "reference_center_y"):
            errors.require(number(item.get(field)), f"{path}.{side}.{field} must be numeric")
        for field in ("width", "height"):
            errors.require(number(item.get(field)) and item[field] > 0, f"{path}.{side}.{field} must be positive")
        if all(number(item.get(field)) for field in ("x", "width", "center_x")):
            errors.require(math.isclose(item["center_x"], item["x"] + item["width"] / 2, abs_tol=1e-6), f"{path}.{side}.center_x must be recomputable")
        if all(number(item.get(field)) for field in ("y", "height", "center_y")):
            errors.require(math.isclose(item["center_y"], item["y"] + item["height"] / 2, abs_tol=1e-6), f"{path}.{side}.center_y must be recomputable")


def validate_alignments(spec: dict[str, Any], errors: ValidationErrors) -> set[str]:
    """验证 fidelity 的 target↔Flutter 关键对齐合同。"""
    alignments = sequence(spec.get("critical_alignments"))
    errors.require(bool(alignments), "fidelity critical_alignments must be non-empty")
    test_ids: set[str] = set()
    identifiers: set[str] = set()
    flutter_keys: set[str] = set()
    for index, raw in enumerate(alignments):
        item = mapping(raw)
        path = f"critical_alignments[{index}]"
        for field in ("id", "element", "flutter_key", "reference", "reference_flutter_key"):
            errors.require(text(item.get(field)), f"{path}.{field} is required")
        if text(item.get("id")):
            errors.require(item["id"] not in identifiers, f"duplicate critical alignment id: {item['id']}")
            identifiers.add(item["id"])
        if text(item.get("flutter_key")):
            errors.require(item["flutter_key"] not in flutter_keys, f"duplicate critical alignment flutter_key: {item['flutter_key']}")
            flutter_keys.add(item["flutter_key"])
        relations = mapping(item.get("relations"))
        for axis, accepted in (("horizontal", H_TYPES), ("vertical", V_TYPES)):
            relation = mapping(relations.get(axis))
            errors.require(relation.get("type") in accepted, f"{path}.relations.{axis}.type is invalid")
            for side in ("target", "flutter"):
                value = relation.get(side)
                errors.require(semantic_relation(value), f"{path}.relations.{axis}.{side} must contain a semantic boundary expression and relation operator")
        geometry = mapping(item.get("geometry"))
        validate_geometry(geometry, f"{path}.geometry", errors)
        delta = mapping(item.get("delta"))
        tolerance = item.get("tolerance_logical_px")
        errors.require(number(tolerance) and 0 <= tolerance <= 1, f"{path}.tolerance_logical_px must be between 0 and 1")
        target = mapping(geometry.get("target"))
        flutter = mapping(geometry.get("flutter"))
        for axis, center, reference in (("horizontal", "center_x", "reference_center_x"), ("vertical", "center_y", "reference_center_y")):
            errors.require(number(delta.get(axis)), f"{path}.delta.{axis} must be numeric")
            fields = (target.get(center), target.get(reference), flutter.get(center), flutter.get(reference), delta.get(axis))
            if all(number(value) for value in fields):
                expected = (fields[2] - fields[3]) - (fields[0] - fields[1])
                errors.require(math.isclose(fields[4], expected, abs_tol=1e-6), f"{path}.delta.{axis} must equal Flutter/target relative-center difference")
                if number(tolerance):
                    errors.require(abs(fields[4]) <= tolerance, f"{path}.delta.{axis} exceeds tolerance")
        validate_optical(mapping(item.get("optical")), f"{path}.optical", errors)
        evidence = mapping(item.get("evidence"))
        for field in ("target_screenshot", "flutter_screenshot", "actual_measurement_output"):
            errors.require(text(evidence.get(field)), f"{path}.evidence.{field} is required")
        ids = sequence(item.get("test_ids"))
        errors.require(bool(ids) and all(text(value) for value in ids), f"{path}.test_ids must be non-empty")
        test_ids.update(value for value in ids if text(value))
        parity_ids = sequence(item.get("parity_case_ids"))
        errors.require(bool(parity_ids) and all(text(value) for value in parity_ids), f"{path}.parity_case_ids must be non-empty")
    return test_ids


def validate_parity(spec: dict[str, Any], errors: ValidationErrors) -> set[str]:
    """验证视觉 parity case 对单一冻结目标及候选快照的绑定。"""
    cases = sequence(spec.get("parity_cases"))
    errors.require(bool(cases), "fidelity parity_cases must be non-empty")
    identifiers: set[str] = set()
    for index, raw in enumerate(cases):
        item = mapping(raw)
        path = f"parity_cases[{index}]"
        for field in ("id", "state", "orientation", "target_sha256", "candidate_code_sha", "target_screenshot", "flutter_screenshot"):
            errors.require(text(item.get(field)), f"{path}.{field} is required")
        errors.require(isinstance(item.get("target_sha256"), str) and bool(SHA256.fullmatch(item["target_sha256"])), f"{path}.target_sha256 must be a 64-character lowercase SHA-256")
        errors.require(isinstance(item.get("candidate_code_sha"), str) and bool(CODE_SHA.fullmatch(item["candidate_code_sha"])), f"{path}.candidate_code_sha must be a 40-64 character lowercase commit/content SHA")
        errors.require(item.get("orientation") in {"portrait", "landscape"}, f"{path}.orientation must be portrait or landscape")
        viewport = mapping(item.get("viewport"))
        errors.require(number(viewport.get("width")) and viewport["width"] > 0, f"{path}.viewport.width must be positive")
        errors.require(number(viewport.get("height")) and viewport["height"] > 0, f"{path}.viewport.height must be positive")
        if text(item.get("id")):
            errors.require(item["id"] not in identifiers, f"duplicate parity case id: {item['id']}")
            identifiers.add(item["id"])
    return identifiers


def validate_signals(spec: dict[str, Any], invariant_tests: set[str], executed: set[str], errors: ValidationErrors) -> set[str]:
    """验证实现信号，并返回需人工关注的信号名称。"""
    attention: set[str] = set()
    for index, raw in enumerate(sequence(spec.get("implementation_signals"))):
        item = mapping(raw)
        signal = item.get("signal")
        errors.require(signal in SIGNALS, f"implementation_signals[{index}].signal is invalid")
        for field in ("reason", "boundary", "fallback"):
            errors.require(text(item.get(field)), f"implementation_signals[{index}].{field} is required")
        test_ids = sequence(item.get("test_ids"))
        errors.require(bool(test_ids) and all(text(test_id) for test_id in test_ids), f"implementation_signals[{index}].test_ids is required")
        declared = {test_id for test_id in test_ids if text(test_id)}
        errors.require(declared <= invariant_tests, f"implementation_signals[{index}].test_ids must be declared by invariants")
        errors.require(declared <= executed, f"implementation_signals[{index}].test_ids must execute in evidence_matrix")
        if signal == "Positioned":
            errors.require(text(item.get("viewport_scope")), f"implementation_signals[{index}].viewport_scope is required")
        if signal in SIGNALS:
            attention.add(signal)
    return attention


def validate(spec: dict[str, Any]) -> tuple[list[str], set[str]]:
    """执行完整验证并返回错误与实现关注信号。"""
    errors = ValidationErrors()
    invariant_tests, executed = validate_common(spec, errors)
    phase = spec.get("phase")
    errors.require(phase in {"sketch", "fidelity"}, "phase must be sketch or fidelity")
    if phase == "sketch":
        # sketch 不得预填未来视觉证据，避免把尚未发生的 parity 伪装为已验证事实。
        errors.require("critical_alignments" not in spec, "sketch must not contain critical_alignments")
        errors.require("parity_cases" not in spec, "sketch must not contain parity_cases")
    elif phase == "fidelity":
        alignment_tests = validate_alignments(spec, errors)
        parity_ids = validate_parity(spec, errors)
        executed = {test for case in sequence(mapping(spec.get("evidence_matrix")).get("cases")) for test in sequence(mapping(case).get("test_ids")) if text(test)}
        errors.require(alignment_tests <= executed, "every critical alignment test_id must execute in evidence_matrix")
        for index, raw in enumerate(sequence(spec.get("critical_alignments"))):
            bound = set(sequence(mapping(raw).get("parity_case_ids")))
            errors.require(bool(bound) and bound <= parity_ids, f"critical_alignments[{index}] references unknown parity case")
    attention = validate_signals(spec, invariant_tests, executed, errors)
    return errors.items, attention


def main() -> int:
    """读取 YAML、运行验证并输出 CI 可用结果。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", type=Path, help="layout-spec.yaml path")
    args = parser.parse_args()
    try:
        loaded = yaml.safe_load(args.spec.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        print(f"[FAIL] cannot read {args.spec}: {exc}")
        return 1
    if not isinstance(loaded, dict):
        print("[FAIL] specification root must be a mapping")
        return 1
    errors, attention = validate(loaded)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print(f"[PASS] {args.spec}")
    if attention:
        print(f"implementation_attention={','.join(sorted(attention))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
