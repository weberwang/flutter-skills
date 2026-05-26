---
name: flutter-prd-rd-writer
description: Use when turning a PRD into a complete Flutter研发文档, 技术方案, 开发设计文档, or 实施方案, especially when the output must cover Flutter architecture, package selection, best bundle recommendations, backend collaboration, and fullchain delivery concerns such as analytics, monitoring, rollout, and release risks.
---

# Flutter PRD RD Writer

## Overview

Turn a PRD into a complete研发文档 that a Flutter team can review and execute. Focus on architecture, module boundaries, package choices, best bundle recommendations, backend collaboration, and fullchain delivery readiness instead of generic advice.

## Quick Start

- If the input is a PRD, product requirement summary, feature brief, or demand note, start with requirement intake and gap analysis.
- If the user mainly needs package choices, architecture direction, or implementation scope from a PRD, still use the same flow. Do not skip the intake step.
- If the request mentions package combinations, best practices, or technical stacks, read `references/package-selection-and-best-bundles.md` before answering.
- If the request must cover analytics, monitoring, rollout, release, or cross-team delivery, read `references/fullchain-delivery-checklist.md` before answering.

## Workflow

1. Read the PRD and extract goals, users, flows, scope, constraints, and explicit non-goals.
2. Identify missing information that would change architecture, package selection, or delivery scope.
3. When information is missing, output `假设前提` and `待确认项` first.
4. Build the main研发文档 structure using `references/flutter-technical-solution-template.md`.
5. Choose package stacks by capability domain instead of recommending isolated packages.
6. Extend the document from Flutter client scope to backend collaboration, analytics, monitoring, security, rollout, and release readiness when the request requires fullchain coverage.
7. End with a recommended main plan, backup options, risks, and the top questions that should be confirmed next.

## Hard Rules

- 不要把输出写成泛泛建议，必须写成可交付研发文档。
- 不要因为 PRD 不完整就脑补细节，先写 `假设前提` 与 `待确认项`。
- 不要只给单一答案。关键技术决策必须写 `推荐方案`、`备选方案`、`取舍理由`。
- 不要把第三方包写成排行榜。每个能力域必须写 `最佳搭档` 与 `避免混搭`。
- 不要默认“最新就是最好”。优先稳定性、生态协同、维护活跃度、团队接入成本。
- 不要直接生成业务代码。这个 skill 的职责是产出研发文档和技术决策，不是实现代码。
- 如果某个包、服务或生态结论明显依赖当前状态，先基于官方文档或当前主页核实，再写进最终文档。

## Output Contract

输出结果至少应覆盖：

- PRD 需求理解
- 假设前提与待确认项
- 业务流程与页面范围
- 总体技术架构
- Flutter 客户端详细技术方案
- 第三方包选型与最佳搭档
- 后端协作与接口契约要求
- 数据与安全方案
- 埋点、监控与运营支持
- 测试与质量保障
- 实施计划与里程碑
- 风险清单与替代方案
- 最终结论

每个关键章节都应说明：

- 为什么推荐当前方案
- 不选哪些常见替代路径
- 当前选择的代价、限制或迁移成本

## Package Guidance

在包选型章节里，优先输出“能力域方案栈”，而不是一个个散列包名。统一采用以下结构：

```text
能力域：
推荐主方案：
推荐理由：
最佳搭档：
备选方案：
避免混搭：
接入注意事项：
升级/维护风险：
```

## References

- Read `references/prd-intake-and-gap-analysis.md` for requirement intake, gap analysis, and how to express assumptions.
- Read `references/flutter-technical-solution-template.md` for the default研发文档 structure and Flutter-specific章节写法.
- Read `references/package-selection-and-best-bundles.md` for capability domains, package stacks, best bundle logic, and avoid-mixing rules.
- Read `references/fullchain-delivery-checklist.md` for backend collaboration, analytics, monitoring, rollout, release, and delivery risks.
