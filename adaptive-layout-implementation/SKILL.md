---
name: adaptive-layout-implementation
description: Define and implement framework-independent adaptive layout specifications before coding pages. Use for new or refactored responsive screens and any work involving Stack or Positioned, fixed dimensions, floating or docked controls, breakpoints, scrolling, SafeArea, keyboard, fold or split views, localization, RTL, or large text.
---

# Adaptive Layout Implementation

在编码前为每个页面创建可执行的 `layout-spec.yaml`，把布局关系、内容增长和系统边界写成约束；编码中按规格实现并登记需要关注的实现信号；交付前运行确定性验证和参数化关系测试。

## 实施流程

1. 从 design-decision、ui-spec 或技术方案提取语义区域和视觉约束，复制 [layout-spec-template.yaml](assets/layout-spec-template.yaml) 到 `docs/design/pages/<page-name>/layout-spec.yaml`。
2. 填写目标尺寸/方向、双轴相对锚点、尺寸范围、结构断点、内容列、系统避让、滚动所有权、文本增长、停靠回退、共享断点解析器和关系不变量。
3. 生成证据矩阵：显式覆盖每个断点的 `b-1/b/b+1`、同宽不同高、横竖屏、规格声明的默认/大字号数值、默认/最长文案、零/非零安全区及关键动作三态；每个不变量绑定参数化测试 id。
4. 若使用 `Stack/Positioned`、固定宽高、悬浮、单行截断或手写断点，在 `implementation_signals` 登记理由、边界/参照、回退和测试 id；完整登记后仍照常实现，不把信号当作自动错误。
5. 运行 `scripts/validate_layout_spec.py <layout-spec.yaml>`；通过后按 [implementation-workflow.md](references/implementation-workflow.md) 和 [flutter-adapter.md](references/flutter-adapter.md) 实现。缺少规格或验证失败时不要开始页面编码。
6. 交付前执行 [test-matrix.md](references/test-matrix.md) 的关系测试，并把规格路径、验证输出和测试证据交给实现计划与质量审阅流程。

## 资源导航

- 规格字段与不变量：[layout-spec.md](references/layout-spec.md)
- 编码前、中、后的执行顺序：[implementation-workflow.md](references/implementation-workflow.md)
- Flutter 约束、滚动和系统边界：[flutter-adapter.md](references/flutter-adapter.md)
- 参数化矩阵与最小充分覆盖：[test-matrix.md](references/test-matrix.md)
- 确定性验证器：`scripts/validate_layout_spec.py`
