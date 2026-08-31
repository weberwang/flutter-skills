---
name: flutter-ux-ui-quality
description: Use when the user explicitly asks to define or review Flutter UX/UI semantics, visual direction, responsive behavior, or accessibility, or when flutter-app-orchestrator routes the accepted UX/UI stage.
---

# Flutter UX/UI Quality

UX/UI Lead 负责页面语义与视觉输入，不写页面代码。

## 流程

1. 定义全局 UI spec、设计 token、导航语义、无障碍、内容策略与视觉方向。
2. 对每个页面输出语义合同：范围、内容优先级、状态、交互、结果、导航、滚动 owner、断点/重排、文本增长、SafeArea/键盘/系统栏、无障碍与 data/UI/asset ownership。
3. 依据 `flutter-code-sketch/references/code-sketch-level-standard.md` 选择 Full、Lightweight 或 Reuse 并记录理由。
4. 调用 `adaptive-layout-implementation` 创建 `phase: sketch` 的页面 `layout-spec.yaml`；此阶段不含未来视觉 parity 字段。
5. 由 Flutter Engineer 使用 `flutter-code-sketch` 在生产骨架实现中性草图、关系测试和风险选择的截图，再由独立 Code Sketch Reviewer 审阅。
6. Review 通过后调用 `flutter-hifi-mockup` 生成、评审并由用户冻结高保真目标。
7. 对冻结目标与语义合同/sketch spec 做合同回对。任何范围、状态、导航、滚动、断点、无障碍或 ownership 变化都返回更新并重审。
8. 需要资产时调用 `flutter-asset-atlas`；随后把同一 layout-spec 升级为 `phase: fidelity`，在同一骨架还原并进入独立 Visual QA。

## 完成条件

页面只有在风险选择的结构证据、高保真目标、资产证据（或 N/A）、fidelity validator、实际 Widget 关系测量、target/Flutter 同视口截图和独立 Visual QA 全部满足时完成。低保真截图只约束功能与层级，进入高保真后其 Golden 失效或被替换。
