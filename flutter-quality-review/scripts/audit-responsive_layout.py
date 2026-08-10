#!/usr/bin/env python3
"""扫描 Flutter 源码和任务工件中的响应式布局反模式。

脚本只使用 Python 标准库，目的是把页面契约和最容易回归的布局捷径
放进 F0 确定性检查。它不是 Dart 解析器：遇到复杂语法时宁可给出窄范围
提示，也不把普通的局部尺寸 token 误判成整页缩放。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


# 该版本必须与 responsive-layout-strategy.md、任务模板和 flutter-dev 一致。
CONTRACT_VERSION = "1.1"
GENERATED_SUFFIXES = (".g.dart", ".freezed.dart")
IGNORED_DIRECTORIES = {
    ".dart_tool",
    ".git",
    ".idea",
    ".gradle",
    "build",
    "node_modules",
    "Pods",
}
EXEMPTION_PATTERN = re.compile(r"响应式审计豁免\s*[:：]\s*(?P<reason>.+)|responsive-layout-exemption\s*:\s*(?P<english>.+)")
CHINESE_PATTERN = re.compile(r"[\u3400-\u9fff]")


@dataclass(frozen=True)
class Finding:
    """表示一条可定位、可分级的响应式审计发现。"""

    severity: str
    code: str
    path: str
    line: int
    message: str

    def format_text(self) -> str:
        """将发现格式化为稳定的命令行文本。"""
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"{self.severity.upper()} {location} [{self.code}] {self.message}"


@dataclass
class AuditReport:
    """保存一次源码和契约扫描的结果。"""

    files_scanned: int
    findings: list[Finding]
    contracts_checked: list[str]

    @property
    def errors(self) -> list[Finding]:
        """返回会阻止 F0 放行的错误发现。"""
        return [finding for finding in self.findings if finding.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        """返回不阻塞默认命令、但需要记录的警告发现。"""
        return [finding for finding in self.findings if finding.severity == "warning"]


def iter_dart_files(target: Path) -> list[Path]:
    """递归列出目标目录中的 Dart 源码，并排除生成物和构建缓存。"""
    target = target.resolve()
    if target.is_file():
        return [target] if target.suffix == ".dart" else []

    files: list[Path] = []
    for path in target.rglob("*.dart"):
        if any(part in IGNORED_DIRECTORIES for part in path.parts):
            continue
        if path.name.endswith(GENERATED_SUFFIXES):
            continue
        files.append(path)
    return sorted(files)


def read_utf8(path: Path) -> str:
    """读取文本并容忍外部项目中偶见的非 UTF-8 字节。"""
    return path.read_text(encoding="utf-8", errors="replace")


def has_exemption(lines: Sequence[str], line_number: int) -> bool:
    """检查目标行附近是否有带中文原因的窄范围叠层豁免。"""
    start = max(0, line_number - 3)
    end = min(len(lines), line_number + 2)
    for line in lines[start:end]:
        match = EXEMPTION_PATTERN.search(line)
        if not match:
            continue
        reason = (match.group("reason") or match.group("english") or "").strip()
        # 中文原因是为了让豁免表达业务意图，而不是给坐标捷径留后门。
        if len(reason) >= 4 and CHINESE_PATTERN.search(reason):
            return True
    return False


def line_number(lines: Sequence[str], index: int) -> int:
    """把零基索引转换成用户可读的一基行号。"""
    return index + 1


def scan_dart_file(path: Path, display_root: Path) -> list[Finding]:
    """扫描单个 Dart 文件中的布局反模式并返回定位发现。"""
    text = read_utf8(path)
    lines = text.splitlines()
    display_path = _display_path(path, display_root)
    findings: list[Finding] = []

    positioned_lines: list[int] = []
    coordinate_hits: list[int] = []
    breakpoint_lines: list[int] = []
    fixed_height_lines: list[int] = []

    for index, line in enumerate(lines):
        current_line = line_number(lines, index)
        if re.search(r"\bPositioned(?:Directional)?\s*\(", line):
            positioned_lines.append(index)
            window = "\n".join(lines[index : min(len(lines), index + 9)])
            if re.search(r"\b(?:left|top|right|bottom|start|end)\s*:", window) and not has_exemption(lines, index):
                findings.append(
                    Finding(
                        "error",
                        "PRIMARY_ABSOLUTE_POSITION",
                        display_path,
                        current_line,
                        "Positioned/PositionedDirectional 带坐标进入主结构；请改用父约束，或在页面契约中写明带中文原因的真实叠层豁免。",
                    )
                )

        if re.search(r"\b(?:FittedBox|Transform\.scale)\s*\(", line):
            surrounding = "\n".join(lines[max(0, index - 20) : min(len(lines), index + 21)])
            is_page_scale = bool(re.search(r"\b(?:Scaffold|CustomScrollView|NestedScrollView)\s*\(", surrounding))
            findings.append(
                Finding(
                    "error" if is_page_scale else "warning",
                    "WHOLE_PAGE_SCALE" if is_page_scale else "LOCAL_SCALE",
                    display_path,
                    current_line,
                    "整页缩放会掩盖约束和溢出；请让 LayoutBuilder/Flex/Wrap 等原语决定结构。"
                    if is_page_scale
                    else "局部缩放需确认不是用来修复布局溢出。",
                )
            )

        coordinate_pattern = re.compile(
            r"\b(?:left|right|top|bottom|start|end|width|height)\s*:\s*[^,\n]*(?:\.w\b|\.h\b|MediaQuery[^\n]*(?:width|height)|maxWidth\s*[*\/]|size\.(?:width|height)\s*[*\/])"
        )
        proportional_assignment_pattern = re.compile(
            r"\b(?:x|y|left|right|top|bottom|start|end|offset|position|width|height)\w*\s*=\s*[^;\n]*(?:MediaQuery[^\n]*(?:width|height)|constraints\.max(?:Width|Height)|max(?:Width|Height))\s*[*\/]"
        )
        if coordinate_pattern.search(line) or proportional_assignment_pattern.search(line):
            coordinate_hits.append(index)

        if re.search(r"\b(?:SizedBox|Container|ConstrainedBox)\s*\(", line):
            fixed_height_lines.append(index)

        if re.search(r"\b(?:maxWidth|maxHeight)\s*(?:<|>|<=|>=|==)\s*\d+(?:\.\d+)?", line):
            breakpoint_lines.append(index)

    if len(coordinate_hits) >= 3:
        first = coordinate_hits[0]
        findings.append(
            Finding(
                "error",
                "COORDINATE_SCALING",
                display_path,
                line_number(lines, first),
                f"检测到 {len(coordinate_hits)} 处坐标/尺寸比例缩放；禁止全坐标 .w/.h 或按画布比例复刻布局。",
            )
        )
    else:
        for index in coordinate_hits:
            findings.append(
                Finding(
                    "warning",
                    "COORDINATE_TOKEN",
                    display_path,
                    line_number(lines, index),
                    "局部 .w/.h 或比例尺寸需要确认是命名 token，而不是页面坐标；结构应由父约束决定。",
                )
            )

    _scan_fixed_text_height(lines, display_path, fixed_height_lines, findings)

    _scan_cached_startup_size(lines, display_path, findings)
    _scan_breakpoint_spread(lines, display_path, breakpoint_lines, findings)

    return findings


def _scan_cached_startup_size(
    lines: Sequence[str], display_path: str, findings: list[Finding]
) -> None:
    """识别在启动生命周期缓存 MediaQuery 尺寸的实现。"""
    size_access = r"MediaQuery(?:\.of\([^)]*\)\.size(?:\.(?:width|height))?|\.sizeOf\([^)]*\)(?:\.(?:width|height))?)"
    field_pattern = re.compile(
        rf"\b(?:late\s+final|final|late)\s+(?:Size|double)\s+\w+\s*=\s*{size_access}"
    )
    for index, line in enumerate(lines):
        if field_pattern.search(line):
            findings.append(
                Finding(
                    "error",
                    "CACHED_STARTUP_SIZE",
                    display_path,
                    line_number(lines, index),
                    "MediaQuery 尺寸被缓存为字段；窗口缩放、分屏或折叠时必须读取当前约束。",
                )
            )

    init_indices = [index for index, line in enumerate(lines) if "initState" in line]
    for init_index in init_indices:
        window = "\n".join(lines[init_index : min(len(lines), init_index + 24)])
        if re.search(size_access, window):
            findings.append(
                Finding(
                    "error",
                    "CACHED_STARTUP_SIZE",
                    display_path,
                    line_number(lines, init_index),
                    "initState 中读取并保存 MediaQuery.size 只反映启动视口；请在 build 的父约束中重新计算。",
                )
            )


def _scan_fixed_text_height(
    lines: Sequence[str], display_path: str, starts: Sequence[int], findings: list[Finding]
) -> None:
    """识别跨多行构造器中固定 height 包裹可变文本的窄范围反模式。"""
    reported: set[int] = set()
    for start in starts:
        depth = 0
        body: list[str] = []
        for index in range(start, min(len(lines), start + 25)):
            current = lines[index]
            body.append(current)
            depth += current.count("(") - current.count(")")
            if index > start and depth <= 0:
                break
        joined = "\n".join(body)
        if not re.search(r"(?<!max)height\s*:", joined):
            continue
        if not re.search(r"\bText(?:\.rich)?\s*\(", joined):
            continue
        if start in reported:
            continue
        reported.add(start)
        findings.append(
            Finding(
                "error",
                "FIXED_TEXT_HEIGHT",
                display_path,
                line_number(lines, start),
                "固定高度包住可变文本；请让文本自然换行并用约束/最小尺寸控制结构。",
            )
        )


def _scan_breakpoint_spread(
    lines: Sequence[str], display_path: str, breakpoint_lines: Sequence[int], findings: list[Finding]
) -> None:
    """提示同一文件内散落多个未命名结构断点。"""
    thresholds: set[str] = set()
    threshold_pattern = re.compile(r"\b(?:maxWidth|maxHeight)\s*(?:<|>|<=|>=|==)\s*(\d+(?:\.\d+)?)")
    for index in breakpoint_lines:
        match = threshold_pattern.search(lines[index])
        if match:
            thresholds.add(match.group(1))
    if len(thresholds) > 1:
        findings.append(
            Finding(
                "warning",
                "SCATTERED_BREAKPOINTS",
                display_path,
                line_number(lines, breakpoint_lines[0]),
                "同一文件散落多个断点阈值；请集中到命名 breakpoint resolver，并为每个阈值记录结构原因。",
            )
        )


def _display_path(path: Path, display_root: Path) -> str:
    """生成稳定的相对路径，便于把审计结果粘贴到评审记录。"""
    try:
        return path.resolve().relative_to(display_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def validate_contract(path: Path, kind: str, expected_version: str = CONTRACT_VERSION) -> list[Finding]:
    """验证 task brief 或 page decision 是否包含响应式交接必填章节。"""
    text = read_utf8(path)
    display_path = path.as_posix()
    required = _required_contract_markers(kind)
    findings: list[Finding] = []
    for code, label, alternatives in required:
        marker_line = _find_marker_line(text, alternatives)
        if marker_line is None or not _marker_line_has_value(marker_line, code):
            findings.append(
                Finding(
                    "error",
                    code,
                    display_path,
                    0,
                    f"缺少响应式契约章节“{label}”；不能以单张图或“见截图”替代。",
                )
            )

    version_pattern = re.compile(r"(?:响应式契约[^\n]*版本|responsive[- ]contract[^\n]*version|strategy[^\n]*@)\D*(\d+\.\d+)", re.IGNORECASE)
    versions = version_pattern.findall(text)
    if expected_version not in versions:
        findings.append(
            Finding(
                "error",
                "CONTRACT_VERSION",
                display_path,
                0,
                f"响应式契约版本必须为 {expected_version}，当前未找到一致版本。",
            )
        )
    return findings


def _find_marker_line(text: str, alternatives: Sequence[str]) -> str | None:
    """返回包含章节标记的首行；找不到时返回空值。"""
    for line in text.splitlines():
        if any(marker in line for marker in alternatives):
            return line
    return None


def _marker_line_has_value(line: str, code: str) -> bool:
    """判断章节行是否填写了内容，而不是只保留模板占位符。"""
    value = line.split(":", 1)[1] if ":" in line else line
    value = value.split("：", 1)[1] if "：" in value else value
    value = value.strip(" -*`\t")
    if not value or re.search(r"<[^>]+>|TODO|待填写|未填写|阻塞项\s*[:：]?\s*$", value, re.IGNORECASE):
        return False
    if code == "CONTRACT_MAPPING_COMPLETE" and re.fullmatch(r"100%\s*/\s*阻塞项?\s*[:：]?", value.strip("`")):
        return False
    return True


def _required_contract_markers(kind: str) -> list[tuple[str, str, tuple[str, ...]]]:
    """返回不同工件类型的最小章节标记集合。"""
    common = [
        ("CONTRACT_REGION_TREE", "区域树", ("区域树", "region tree")),
        ("CONTRACT_MAPPING", "布局实现映射", ("布局实现映射", "region-to-primitive", "Flutter 原语")),
        ("CONTRACT_BREAKPOINTS", "结构断点", ("结构断点", "breakpoint")),
        ("CONTRACT_OVERLAY", "允许叠层", ("允许叠层", "叠层白名单", "overlay whitelist")),
        ("CONTRACT_NO_COORDINATES", "禁止坐标", ("禁止坐标", "禁止将", "prohibited-coordinate")),
        ("CONTRACT_VIEWPORT_MATRIX", "具体视口矩阵", ("具体视口", "视口矩阵", "viewport matrix", "证据矩阵")),
        ("CONTRACT_LARGE_TEXT", "大字体", ("大字体", "large text")),
        ("CONTRACT_LONG_TEXT", "长文本", ("长文本", "long content")),
        ("CONTRACT_KEYBOARD", "键盘", ("键盘", "keyboard")),
        ("CONTRACT_SAFE_AREA", "SafeArea", ("SafeArea", "系统栏", "system inset")),
        ("CONTRACT_WIDGET_EVIDENCE", "Widget", ("Widget", "widget")),
        ("CONTRACT_GOLDEN_EVIDENCE", "Golden", ("Golden", "golden")),
        ("CONTRACT_AUDIT_COMMAND", "审计命令", ("审计命令", "audit")),
    ]
    if kind == "page":
        return common + [
            ("CONTRACT_PARENT_SIBLING", "父子/兄弟约束", ("父子/兄弟", "父子", "兄弟约束")),
            ("CONTRACT_RELATIVE_ANCHOR", "相对锚点", ("相对锚点", "relative anchor")),
            ("CONTRACT_SIZE_MODE", "尺寸模式", ("尺寸模式", "size mode")),
            ("CONTRACT_FLOW_OVERLAY", "流式/叠层边界", ("流式/叠层", "流式", "flow/overlay")),
            ("CONTRACT_FLUTTER_PRIMITIVE", "Flutter 原语建议", ("Flutter 原语建议", "原语")),
            ("CONTRACT_OPEN_FACTS", "未决事实", ("未决事实", "unresolved")),
        ]
    return common + [
        ("CONTRACT_PATH", "布局契约路径", ("布局契约路径", "响应式契约路径", "responsive contract path")),
        ("CONTRACT_MAPPING_COMPLETE", "映射完整性", ("映射完整性", "mapping completeness", "100%")),
    ]


def audit(
    target: Path,
    task_brief: Path | None = None,
    page_decision: Path | None = None,
    require_contract: bool = False,
    expected_version: str = CONTRACT_VERSION,
) -> AuditReport:
    """执行源码扫描和可选工件契约校验。"""
    target = target.resolve()
    files = iter_dart_files(target)
    display_root = target if target.is_dir() else target.parent
    findings: list[Finding] = []
    for path in files:
        findings.extend(scan_dart_file(path, display_root))

    contracts_checked: list[str] = []
    if task_brief:
        contracts_checked.append(task_brief.as_posix())
        try:
            findings.extend(validate_contract(task_brief, "task", expected_version))
        except OSError as error:
            findings.append(Finding("error", "CONTRACT_READ", task_brief.as_posix(), 0, f"无法读取任务简报：{error}"))
    if page_decision:
        contracts_checked.append(page_decision.as_posix())
        try:
            findings.extend(validate_contract(page_decision, "page", expected_version))
        except OSError as error:
            findings.append(Finding("error", "CONTRACT_READ", page_decision.as_posix(), 0, f"无法读取页面决策：{error}"))
    if require_contract and not (task_brief or page_decision):
        findings.append(Finding("error", "CONTRACT_REQUIRED", "<cli>", 0, "--require-contract 至少需要 --task-brief 或 --page-decision。"))
    return AuditReport(files_scanned=len(files), findings=findings, contracts_checked=contracts_checked)


def build_parser() -> argparse.ArgumentParser:
    """创建命令行参数解析器。"""
    parser = argparse.ArgumentParser(description="审计 Flutter 响应式布局反模式和页面契约")
    parser.add_argument("target", type=Path, help="Flutter 仓库或 Dart 文件路径")
    parser.add_argument("--task-brief", type=Path, help="可选：验证任务简报的响应式章节")
    parser.add_argument("--page-decision", type=Path, help="可选：验证页面设计决策的响应式章节")
    parser.add_argument("--require-contract", action="store_true", help="要求至少提供一种契约工件")
    parser.add_argument("--expected-version", default=CONTRACT_VERSION, help="期望的响应式契约版本（默认 1.1）")
    parser.add_argument("--fail-on-warning", action="store_true", help="把 warning 也作为失败退出")
    parser.add_argument("--json", action="store_true", dest="as_json", help="输出机器可读 JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """运行审计并以错误/警告数量返回稳定退出码。"""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        report = audit(
            args.target,
            args.task_brief,
            args.page_decision,
            args.require_contract,
            args.expected_version,
        )
    except OSError as error:
        print(f"响应式审计无法读取目标：{error}", file=sys.stderr)
        return 2

    if args.as_json:
        payload = asdict(report)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"响应式审计：扫描 {report.files_scanned} 个 Dart 文件，检查 {len(report.contracts_checked)} 个契约")
        for finding in report.findings:
            print(finding.format_text())
        print(f"结果：{len(report.errors)} 个错误，{len(report.warnings)} 个警告")

    if report.errors or (args.fail_on_warning and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
