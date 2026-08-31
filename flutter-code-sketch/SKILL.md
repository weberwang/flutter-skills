---
name: flutter-code-sketch
description: Use when the user explicitly asks to implement or review a neutral code-first Flutter page sketch on the production skeleton, or when flutter-app-orchestrator routes the accepted code-sketch stage.
---

# Flutter Code Sketch

在生产 Flutter 骨架中实现中性、可测试的页面结构。此 skill 只负责草图实现、结构证据和独立审阅；`adaptive-layout-implementation` 统一定义 `layout-spec.yaml`、断点和验证规则。

## 前置条件

1. 先完成工程与进程 preflight，确认现有验证命令。新项目须先完成技术设计、Flutter 初始化、模块范围和任务简报；既有项目只读复用现状。
2. 要求 UX/UI Lead 提供页面语义合同、状态、交互、响应式边界，并按 [Code Sketch Level](references/code-sketch-level-standard.md) 选择 Full、Lightweight 或 Reuse。UX/UI Lead 不写页面代码。
3. 从 `adaptive-layout-implementation/assets/layout-spec-template.yaml` 创建项目唯一的页面 `layout-spec.yaml`，保持 `phase: sketch`，通过统一 validator 后再编码。

## 实现 Code Sketch

1. 由 Flutter Engineer 担任 Code Sketch Agent，在生产路由、状态模型和页面骨架中实现；禁止建立一次性重复页面。
2. 使用中性色、基础排版和简单占位内容表达层级、状态、导航、交互、滚动 owner、断点与系统避让；不要提前锁定最终几何、装饰或品牌材质。
3. 为稳定语义节点添加 Flutter key，并编写 Widget/关系测试覆盖合同不变量、断点边界、文本增长、滚动和系统避让。
4. 先运行 analyze 与 Widget/关系测试。结构门禁通过后才生成确定性截图；Lightweight 仅在风险要求时截图，Reuse 只有结构事实变化才完整重审。
5. 仅当导航、键盘、SafeArea、系统栏或插件行为必须运行时验证时，复用已健康的 runtime 实例；没有可复用实例才启动服务。真机验收必须获得用户明确授权。

## 组织独立审阅

1. 固定当前工作树 diff、`phase: sketch` 的 layout-spec、结构测试输出和截图哈希，并计算 `snapshot-id`；由任务审阅记录 spec hash，禁止把 spec 自身 SHA 写回 spec。
2. 派发与 producer 不同的只读 Code Sketch Reviewer，按 [审阅 rubric](references/code-sketch-review-rubric.md) 检查语义、状态、导航、滚动、断点、无障碍和系统避让。
3. 低保真截图只证明功能层级和结构事实，不约束高保真几何。进入高保真阶段后，草图 Golden 必须失效或被高保真证据替换。
4. 审阅不通过时回到同一生产骨架修复并重新计算 snapshot；不得由 producer 自审放行。

## 高保真交接

1. Code Sketch Review 通过后才生成、评审并由用户冻结高保真目标图。
2. 将冻结目标与已审语义合同及 sketch layout-spec 回对。若范围、状态、导航语义、滚动 owner、断点、无障碍或 data/UI/asset ownership 改变，回到语义/草图阶段更新并重审，不得静默继续。
3. 完成资产拆解和确认后，把同一 `layout-spec.yaml` 升级为 `phase: fidelity`；在同一 Flutter 骨架上正常重构实现，禁止用 `Stack/Positioned` 覆盖旧草图凑像素。
4. 最终通过 fidelity validator、实际 Widget 关系测量、target/Flutter 同视口截图 parity 和独立 Visual QA。validator 只证明规格结构与元数据，不证明实际视觉一致。

## 输出

- 页面语义合同与 Code Sketch Level 决策。
- `phase: sketch` 的同一个 `layout-spec.yaml` 及 validator 结果。
- 生产 Flutter 骨架、Widget/关系测试与风险选择的截图证据。
- 独立 Code Sketch Review：snapshot-id/diff、spec hash、截图 hash、结论与未决项。
