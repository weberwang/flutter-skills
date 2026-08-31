---
name: flutter-subagent-delivery
description: Use only when the user explicitly requests parallel writable Flutter tasks or worktrees; otherwise use the orchestrator's single-writer flow.
---

# Flutter Subagent Delivery

本 skill 只处理用户明确授权的并行可写任务或 worktree。普通任务默认由当前分支 checkout 中的一个写入者顺序完成，风险等级不改变拓扑。

## 交接

1. 先读[风险分级](references/task-risk-tiers.md)和[八字段任务契约](../flutter-implementation-plan/references/task-brief-template.md)。
2. Controller 记录明确授权、共同基线、互斥写入范围、所有者和项目原生命令；不得把完整会话粘进提示词。
3. 只有跨角色交接或用户要求时才创建 Markdown brief；不创建 YAML/JSON 状态、租约或自动化状态机。

## 执行与审核

1. 每个写入者只接收一个范围，依赖、路由、主题、生成文件、共享状态、迁移和单页 spec 保持单写者串行。
2. 获得测试等级授权后先实际执行 F0，再按[审核漏斗](../flutter-quality-review/references/review-funnel.md)进行 F1/F2/F3。
3. 审核者只读并返回统一结论；Controller 是持久 review 记录唯一写入者。普通审核以 snapshot 绑定，不强制提交。
4. 修复后只重跑失败或受影响命令，并重开输入指纹已变化的通道。

## 集成边界

分支、提交、PR、合并、worktree 清理、发布和任何外部写入都必须另有明确授权；Markdown 不驱动这些动作。早期烟测只能证明命名覆盖，完整平台矩阵由最终集成/发布承担，真机验收需单独授权。
