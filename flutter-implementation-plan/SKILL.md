---
name: flutter-implementation-plan
description: Use when the user explicitly asks for Flutter implementation planning, scoped tasks, acceptance criteria, or verification, or when flutter-app-orchestrator routes the accepted implementation-planning stage.
---

# Flutter Implementation Plan

把已接受的产品、设计和技术事实压缩成可实施的模块顺序与任务。风险、拓扑和工件规则分别由[风险分级](../flutter-subagent-delivery/references/task-risk-tiers.md)、[审核漏斗](../flutter-quality-review/references/review-funnel.md)和[工件矩阵](../flutter-app-orchestrator/references/artifacts.md)维护。

## 输入

- 已接受的产品 brief、UI spec、技术设计和模块边界。
- 页面语义合同；有自适应页面时使用 `adaptive-layout-implementation` 的 `layout-spec.yaml`。
- 现有项目结构、依赖、跨模块契约和平台验证范围。

## 规划规则

1. 以产品责任、路由/数据 ownership、业务流等级和页面交互顺序划分模块；跨模块先建立契约。
2. 一个任务只交付一个垂直切片或隔离基础；模块进入可实施状态时再细化函数、状态、验收路径和 brief。
3. 每个任务都填写[八字段任务契约](references/task-brief-template.md)。普通单代理在对话中传递；只有跨角色、高风险持久上下文或用户要求才创建 Markdown brief。
4. 默认当前分支的 checkout、单写者、顺序执行。其他分支、worktree、提交、PR 或并行写入仅在用户明确授权后规划，且写范围必须互斥。
5. 只列出实际需要的实现角色和 F2 通道；不要预先组装全团队。UI 任务按需包含 layout-spec、关系测试和截图/golden 证据。
6. 任务验证区分 F0 命令、共享基础烟测、关键业务流主目标烟测和最终平台矩阵；不能把局部证据写成全平台通过。

## 输出

- `docs/plans/module-map.md`
- `docs/plans/modules/<module-name>-scope.md`
- `docs/plans/implementation-plan.md`
- 条件性 `docs/tasks/<task-id>/brief.md`

使用本目录的 module map、module scope、implementation plan 和 task brief 模板；不创建占位工件或运行时状态。

## Gate

没有明确范围、验收条件、确认事实或可执行验证命令时暂停规划并返回 `NEEDS_CONTEXT`。正式审核前必须先获得测试等级选择并完成真实 F0；物理真机、发布和外部写入不自动发生。
