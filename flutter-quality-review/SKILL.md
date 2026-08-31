---
name: flutter-quality-review
description: Use when the user explicitly asks to review or accept Flutter implementation, UI evidence, architecture, security, privacy, or release quality, or when flutter-app-orchestrator routes the accepted quality-review stage.
---

# Flutter Quality Review

只审核已进入范围的事实。先读[审核漏斗](references/review-funnel.md)决定深度和通道，再按需读取[审核 rubric](references/review-rubric.md)；不把窄审查扩大成发布审计。

## 输入

只加载 F1 或指定 F2 通道需要的路径：八字段任务契约、变更文件、F0 命令证据、`snapshot-id`、相关产品/设计/技术决策、页面 layout-spec/资产 manifest、以及该层级要求的平台烟测。没有 snapshot 或必要证据时返回 `NEEDS_CONTEXT`。

## 检查范围

- F1：范围、风险、验收追踪、输入指纹和 F0 证据；只选择实际触发的 Product、QA、technical、visual、Release 通道。
- F2：只读检查被分配的专业事实；UI 变化才检查语义合同、Code Sketch、冻结目标、资产、测量和同视口 parity。
- F3：确认有效通道覆盖当前 snapshot、阻塞已关闭、平台证据与集成条件满足；不重做 F2。

按需复用已有设计、服务和[关键对齐门禁](../adaptive-layout-implementation/references/critical-alignment-gate.md)。低保真截图只证明结构；局部烟测不得声称全平台通过。

## 输出

F1 返回 snapshot、变化维度、通道和理由；F2 按[统一返回契约](../flutter-implementation-plan/references/task-brief-template.md)返回发现、缺失证据和结论；F3 返回有效通道、关闭阻塞、剩余风险和最终 verdict。严重级别为 Critical、Important、Minor。

只有 Controller 在需要持久记录时写 `docs/tasks/<task-id>/review.md`。修复后只重跑失败或受影响命令，只重开输入指纹变化的通道。Markdown 不驱动状态、合并或发布；真机验收、外部写入和发布需单独授权。
