---
name: flutter-prd-rd-writer
description: Use when a user asks to turn a PRD, product requirement summary, feature brief, demand note, or business requirement into a global Flutter technical baseline, architecture decision, package selection, backend collaboration plan, or fullchain delivery plan before module-level detailed design.
---

# Flutter PRD RD Writer

## Overview

Turn product requirements into a reviewable global Flutter technical baseline. The output should help a Flutter team make architecture, package, backend collaboration, delivery, and release decisions without pretending that missing PRD details are already known.

This skill stays at global scope. It may name coarse capability areas, but it must not decompose the product into detailed modules or write per-module UI/UX and implementation RD documents.

## Start Here

If the upstream PRD comes from the orchestrator's strengthened PRD preparation flow, respect its template sections, completeness result, and handoff boundaries before proposing a technical baseline.

1. Read the PRD or requirement input first.
2. Read `references/prd-intake-and-gap-analysis.md` before proposing architecture or packages.
3. Decide whether the user needs a complete研发文档, a focused技术方案, or only a package-selection decision.
4. Load only the reference files needed for that output mode.
5. If the user also needs module splitting, produce the global baseline first, then hand off to `flutter-rd-module-splitter`.
6. Write the answer as an executable engineering document, not as generic advice.

## Reference Loading

Use the smallest useful reference set:

| Situation | Required reference |
| --- | --- |
| Any PRD or requirement input | `references/prd-intake-and-gap-analysis.md` |
| Complete研发文档 or architecture方案 | `references/flutter-technical-solution-template.md` |
| Package, stack, best bundle, or dependency choice | `references/package-selection-and-best-bundles.md` |
| Backend collaboration, analytics, monitoring, rollout, release, or delivery risk | `references/fullchain-delivery-checklist.md` |

## Response Modes

### Complete RD

Use when the user asks for a研发文档, 技术方案, 开发设计文档, or 实施方案. Build the document from `references/flutter-technical-solution-template.md` and cover all output contract sections unless the user explicitly narrows scope.

### Focused Decision

Use when the user asks about architecture direction, package stacks, implementation scope, or trade-offs. Still start with PRD intake, then answer the focused question with `推荐方案`, `备选方案`, and `取舍理由`.

### Gap Analysis

Use when the PRD is too incomplete to support a reliable方案. Output `假设前提` and `待确认项` first, then state which architecture, package, or delivery sections are blocked or assumption-based.

## Scope Boundary

Own these global decisions:

- Overall Flutter architecture direction.
- Package stack and best-bundle decisions.
- Backend collaboration model and API contract style.
- Data, security, analytics, monitoring, rollout, and release baseline.
- Coarse capability map when it helps explain the technical baseline.

Do not own these module-level details:

- Detailed module boundaries and module index.
- Per-module `ui-ux.md` or `impl.md` documents.
- Per-module page states, local data flow, route ownership, or acceptance gates.
- Module-specific implementation sequencing.

Use `flutter-rd-module-splitter` for module-level detailed design after this global baseline exists.

## Workflow

1. Extract product goal, user roles, core scenarios, business flow, scope, constraints, and explicit non-goals.
2. Identify gaps that would change architecture, package selection, backend contracts, security, analytics, rollout, or release scope.
3. If material gaps exist, put `假设前提` and `待确认项` before the main answer.
4. Select the response mode and load the references required by that mode.
5. Choose package stacks by capability domain instead of isolated package names.
6. Extend the Flutter client方案 to backend collaboration, data security, analytics, monitoring, rollout, and release readiness when fullchain delivery is relevant.
7. Keep module treatment at coarse capability level only.
8. End with the recommended main plan, backup options, concrete risks, top questions, and handoff notes for `flutter-rd-module-splitter`.

## Hard Rules

- 不要把输出写成泛泛建议，必须写成可评审、可执行的研发文档或技术决策。
- 不要因为 PRD 不完整就脑补细节，先写 `假设前提` 与 `待确认项`。
- 不要只给单一答案。关键技术决策必须写 `推荐方案`、`备选方案`、`取舍理由`。
- 不要把第三方包写成排行榜。每个能力域必须写 `最佳搭档` 与 `避免混搭`。
- 不要默认“最新就是最好”。优先稳定性、生态协同、维护活跃度、团队接入成本。
- 不要直接生成业务代码。这个 skill 的职责是产出研发文档和技术决策，不是实现代码。
- Do not split the product into detailed modules here. Module-level detailed design belongs to `flutter-rd-module-splitter`.
- Do not write paired UI/UX and implementation module documents here.
- 如果某个包、服务或生态结论明显依赖当前状态，先基于官方文档或当前主页核实，再写进最终文档。

Do not silently repair a weak PRD by inventing missing scope. If the upstream PRD is still structurally weak, say so explicitly with `假设前提` and `待确认项`.

## Output Contract

完整研发文档至少覆盖：

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
- Handoff notes for module splitting
- 最终结论

每个关键章节都应说明：

- 为什么推荐当前方案
- 不选哪些常见替代路径
- 当前选择的代价、限制或迁移成本

## Package Guidance

在包选型章节里，优先输出“能力域方案栈”，而不是散列包名。统一采用以下结构：

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

## Final Self-Check

Before answering, verify:

- Requirement gaps that affect decisions are listed before the main方案.
- Every critical decision has recommendation, alternative, and trade-off.
- Package choices are grouped by capability domain.
- Fullchain concerns are included when delivery, release, analytics, monitoring, or backend collaboration matters.
- Module discussion stays at coarse capability level and does not become module splitting.
- The final answer tells `flutter-rd-module-splitter` which global decisions must be inherited.
- Current ecosystem claims are verified when they could have changed recently.
