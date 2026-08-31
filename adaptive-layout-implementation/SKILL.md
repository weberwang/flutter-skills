---
name: adaptive-layout-implementation
description: Use when the user explicitly asks to define or validate a responsive Flutter layout specification, breakpoint contract, scrolling rule, or target-to-Flutter relationship, or when flutter-app-orchestrator routes the accepted layout stage.
---

# Adaptive Layout Implementation

每个页面只维护一个 `docs/design/pages/<page-name>/layout-spec.yaml`。先以 `phase: sketch` 表达语义结构与关系证据；冻结高保真目标后把同一文件升级为 `phase: fidelity`。`phase` 不是运行时状态或合并信号。

## 流程

1. 从已审页面语义合同复制 [sketch 模板](assets/layout-spec-template.yaml)，填写区域、锚点、断点、内容容器、系统避让、滚动 owner、文本增长与 `text_behavior.line_break` 角色合同、叠层、实现约束、不变量和 `evidence_matrix`。
2. sketch 阶段禁止写 `critical_alignments` 或 `parity_cases`，避免伪造未来证据。运行 `node scripts/validate-layout-spec.js <layout-spec.yaml>` 后才实现 Code Sketch。
3. 在生产 Flutter 骨架中实现并执行实际 Widget 关系测试。文本断行测试必须覆盖最长文案与大字号的组合，并按正文、标题/关键文案、控件标签和原子文本分别验证；结构门禁通过后才按风险生成截图，截图不能替代关系测试。
4. 高保真目标冻结并与语义合同回对后，参考 [fidelity 模板](assets/layout-spec-fidelity-template.yaml) 升级同一文件，补充 target↔Flutter `critical_alignments` 与 `parity_cases`。
5. 每个 parity case 只绑定一个明确冻结的 viewport/state/orientation/target SHA 和 candidate code SHA；没有冻结目标的视口不得声称 parity。spec hash 由 Code Sketch Review、任务审阅或 Visual QA 外部记录，禁止写回 spec 造成自引用。
6. 运行 validator、实际 Widget 测量测试、target/Flutter 同视口截图复核和独立 Visual QA。validator 只证明 schema、中心复算、delta、容差和证据元数据，不证明实际视觉一致。

## 资源

- 字段和两阶段规则：[layout-spec.md](references/layout-spec.md)
- 执行顺序：[implementation-workflow.md](references/implementation-workflow.md)
- Flutter 适配：[flutter-adapter.md](references/flutter-adapter.md)
- 测试覆盖：[test-matrix.md](references/test-matrix.md)
- 关键对齐门禁：[critical-alignment-gate.md](references/critical-alignment-gate.md)
