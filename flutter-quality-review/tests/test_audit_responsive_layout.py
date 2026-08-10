"""响应式审计脚本的标准库单元测试。"""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit-responsive_layout.py"
SPEC = importlib.util.spec_from_file_location("audit_responsive_layout", SCRIPT)
if SPEC is None or SPEC.loader is None:  # pragma: no cover - 测试夹具损坏时才会触发
    raise RuntimeError(f"无法加载审计脚本：{SCRIPT}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


TASK_CONTRACT = """
# Task Brief
- 响应式契约路径 / 版本：flutter-ux-ui-quality/references/responsive-layout-strategy.md@1.1
- 区域树：Root > Content
- 布局实现映射：100%；区域 → LayoutBuilder → Flex
- 结构断点：600px → 两列 → 保持状态 → 单列回退
- 允许叠层白名单：无
- 禁止坐标：不把 x/y 直译进实现
- 具体视口矩阵：390x844、600x900、840x900
- 大字体：1.5x；长文本：真实本地化
- 键盘：滚动到焦点；SafeArea：已验证
- Widget：通过；Golden：通过；响应式审计命令：已执行
- 映射完整性：100%
"""

PAGE_CONTRACT = """
# 页面设计决策
- 响应式契约路径 / 版本：flutter-ux-ui-quality/references/responsive-layout-strategy.md@1.1
- 页面区域树：Root > Header > Body
- 布局实现映射：区域 → LayoutBuilder → Flex；Flutter 原语建议：Flex
- 父子/兄弟约束：Header 与 Body 纵向兄弟
- 相对锚点：标题基线与操作组对齐
- 尺寸模式：内容自适应、最大宽度
- 流式/叠层边界：Body 流式；无叠层
- 结构断点：600px → 结构改变 → 回退
- 允许叠层白名单：无
- 禁止坐标：禁止画布 x/y
- 具体视口矩阵：390x844、840x900
- 大字体：1.5x；长文本：已验证
- 键盘：滚动到焦点；SafeArea：已验证
- Widget：通过；Golden：通过；审计命令：已执行
- 未决事实：无
"""


class ResponsiveAuditTests(unittest.TestCase):
    """覆盖主要反模式、叠层豁免和契约校验路径。"""

    def write_dart(self, root: Path, content: str) -> Path:
        """写入临时 Dart 文件并返回路径。"""
        path = root / "lib" / "screen.dart"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_clean_constraint_layout_passes(self) -> None:
        """正常的约束布局不应产生错误。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                Widget build(BuildContext context) {
                  return LayoutBuilder(builder: (context, constraints) {
                    return SafeArea(child: Column(children: [
                      Flexible(child: Text('可换行')),
                      Wrap(children: [TextButton(onPressed: null, child: Text('操作'))]),
                    ]));
                  });
                }
                """,
            )
            report = MODULE.audit(root)
            self.assertEqual(report.errors, [])

    def test_primary_position_and_scale_are_errors(self) -> None:
        """主结构坐标和整页缩放应阻止 F0。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                Widget build(BuildContext context) => Scaffold(
                  body: FittedBox(child: Stack(children: [
                    Positioned(left: 20, top: 10, child: Text('标题')),
                    Container(width: 200.w, height: 400.h),
                    Container(width: 200.w, height: 400.h),
                    Container(width: 200.w, height: 400.h),
                    final cardWidth = constraints.maxWidth / 2;
                  ])),
                );
                """,
            )
            report = MODULE.audit(root)
            codes = {finding.code for finding in report.errors}
            self.assertIn("PRIMARY_ABSOLUTE_POSITION", codes)
            self.assertIn("WHOLE_PAGE_SCALE", codes)
            self.assertIn("COORDINATE_SCALING", codes)

    def test_true_overlay_requires_chinese_exemption(self) -> None:
        """带中文原因的真实叠层豁免不应误报绝对定位。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                // 响应式审计豁免：真实浮动按钮叠层，契约记录边界和回退
                Widget build(BuildContext context) => Stack(children: [
                  Positioned(right: 16, bottom: 16, child: FloatingActionButton(onPressed: null)),
                ]);
                """,
            )
            report = MODULE.audit(root)
            self.assertNotIn("PRIMARY_ABSOLUTE_POSITION", {finding.code for finding in report.findings})

    def test_positioned_directional_is_scanned(self) -> None:
        """PositionedDirectional 的 start/end 坐标同样必须走叠层契约。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                Widget build(BuildContext context) => Stack(children: [
                  PositionedDirectional(start: 12, end: 12, child: Text('方向性叠层')),
                ]);
                """,
            )
            report = MODULE.audit(root)
            self.assertIn("PRIMARY_ABSOLUTE_POSITION", {finding.code for finding in report.errors})

    def test_media_query_size_of_is_cached_startup_error(self) -> None:
        """MediaQuery.sizeOf 与 MediaQuery.of.size 都不能缓存为启动尺寸。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                late final Size viewport = MediaQuery.sizeOf(context);
                void initState() {
                  super.initState();
                  final Size initial = MediaQuery.of(context).size;
                }
                """,
            )
            report = MODULE.audit(root)
            cached = [finding for finding in report.errors if finding.code == "CACHED_STARTUP_SIZE"]
            self.assertGreaterEqual(len(cached), 2)

    def test_multiline_fixed_height_text_is_scanned(self) -> None:
        """跨多行的 Container 固定高度包文本时应被识别。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_dart(
                root,
                """
                Widget build(BuildContext context) {
                  return Container(
                    padding: const EdgeInsets.all(8),
                    height: 180,
                    child: Text('可能换行的长文本'),
                  );
                }
                """,
            )
            report = MODULE.audit(root)
            self.assertIn("FIXED_TEXT_HEIGHT", {finding.code for finding in report.errors})

    def test_contract_validation_reports_missing_sections(self) -> None:
        """缺少响应式章节时应输出可定位的契约错误。"""
        with tempfile.TemporaryDirectory() as directory:
            brief = Path(directory) / "task-brief.md"
            brief.write_text("# Task Brief\n- 只有一张截图\n", encoding="utf-8")
            findings = MODULE.validate_contract(brief, "task")
            codes = {finding.code for finding in findings}
            self.assertIn("CONTRACT_REGION_TREE", codes)
            self.assertIn("CONTRACT_VERSION", codes)

    def test_complete_task_and_page_contracts_pass(self) -> None:
        """完整模板章节和当前版本应通过校验。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            brief = root / "task.md"
            page = root / "decision.md"
            brief.write_text(TASK_CONTRACT, encoding="utf-8")
            page.write_text(PAGE_CONTRACT, encoding="utf-8")
            report = MODULE.audit(root, brief, page, require_contract=True)
            self.assertEqual(report.errors, [])


if __name__ == "__main__":  # pragma: no cover - 由 unittest discover 调用
    unittest.main()
