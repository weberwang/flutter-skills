---
name: flutter-hifi-mockup
description: Use when the user explicitly asks for a page high-fidelity target, visual exploration, mockup review, or design freeze after the code sketch stage, or when flutter-app-orchestrator routes the accepted high-fidelity stage.
---

# Flutter High-Fidelity Mockup

仅在 Code Sketch Review 通过后生成页面目标图。高保真目标是最终视觉来源，但不能静默改变已审语义合同、状态、导航、滚动、断点、无障碍或 ownership。

## 输入

- 已审页面语义合同、Code Sketch Level 与 Code Sketch Review。
- `phase: sketch` 的 `layout-spec.yaml`、外部 spec hash、关系测试和风险需要的截图证据。
- 全局视觉方向、产品/模块范围与页面真实内容要求。

## 流程

1. 冻结前在对话中临时准备 brief、prompt 和候选；不要把未选方案、prompt 或评审草稿写进仓库。
2. 方向清楚时生成一个候选；只有用户要求探索或存在实质取舍时生成两到三个。每张页面图必须精确 `780 x 1688 px`。
3. 高风险/核心/探索页安排与 producer 不同的只读 Effect Image Reviewer，检查任务层级、状态、可读性、无障碍、系统区域和全局方向。
4. Controller 获得用户明确选择后，把选中图持久化到 `.codex-workflow/visuals/pages/<page-name>/`，计算 SHA-256；随后才在 page design decision 写 candidate ID、hash、确认时间、约束与允许偏差。冻结前 brief/prompt/candidates 保持 transient。
5. 将冻结目标与已审语义合同/layout-spec(sketch)逐项回对。若范围、状态、导航语义、滚动 owner、断点、无障碍或 data/UI/asset ownership 改变，返回 UX/UI 与 Code Sketch 阶段更新并独立重审。
6. 回对通过后，调用 `flutter-asset-atlas` 完成 bitmap decomposition、覆盖审计、编号图确认和资产生产；`asset-manifest.md` 是明细唯一权威，design decision 只链接。
7. 将同一 layout-spec 升级 `phase: fidelity` 后在同一生产 Flutter 骨架高保真还原，并执行 target/Flutter parity 与独立 Visual QA。

## 禁止

不得把低保真截图当最终几何蓝图；不得在 Code Sketch Review 前生成页面目标；不得在用户冻结前写候选记录；不得在合同回对失败时继续资产或高保真实现；不得把资产 ownership/编号/覆盖明细复制到 design decision。
