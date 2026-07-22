# Progress Ledger

创建 `.codex-workflow/progress.md`。它只提供 Controller 的当前视图；任务状态、页面决策与验收记录才是权威来源。

## 当前门禁

- 阶段：
- 当前门禁 / 状态：PENDING / BLOCKED / PASSED / WAIVED / STALE
- 负责人角色：
- 权威证据链接：
- Controller 验证时间：

## 任务索引

| ID | 状态 | DRI / 验收人 | 分支 | 当前门禁 | 权威记录 |
|---|---|---|---|---|---|
| T01 | planned | | `codex/T01` | | `.codex-workflow/tasks/T01.yaml` |

## 当前阻塞项

| 严重级别 | 任务 | 决策或问题 | 所有者 | 下一步 |
|---|---|---|---|---|

## 规则

- 仅 Controller 更新本文件和任务状态文件。
- 只记录链接、状态和当前决策；不要复制任务范围、资产详情、Pencil 节点、提示词、测试输出或审阅发现。
- 每个任务状态文件必须包含 DRI、独立验收人、租约、基线、分支、worktree、写范围与合并记录。
- 每个页面设计事实只写入页面 `design-decision.md`；每个资产事实只写入页面 `asset-manifest.md`；每个验收事实只写入任务 `review.md`。
- 任何实现或修复提交都会使旧审阅快照失效，必须重新审阅。
- 业务流等级完成后记录一条集成冒烟链接；最终平台验证只写入 `docs/architecture/verification-platforms.md`。
