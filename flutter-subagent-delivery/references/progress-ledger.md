# Progress Ledger

仅在存在并行写入任务时创建 `.codex-workflow/progress.md`。它只提供 Controller 的当前视图；任务状态、页面决策与验收记录才是权威来源。

## 当前门禁

- 阶段：
- 当前门禁 / 状态：PENDING / BLOCKED / PASSED / WAIVED / STALE
- 负责人角色：
- 权威证据链接：
- Controller 验证时间：

## 任务索引

| ID | 风险 | 状态 | DRI / 验收人 | 分支 | 当前门禁 | 权威记录 |
|---|---|---|---|---|---|---|
| T01 | high | planned | | `codex/T01` | | `.codex-workflow/tasks/T01.yaml` |

## 当前阻塞项

| 严重级别 | 任务 | 决策或问题 | 所有者 | 下一步 |
|---|---|---|---|---|

## 规则

- 仅 Controller 更新本文件和任务状态文件。
- 只记录链接、状态和当前决策；不要复制任务范围、资产详情、Pencil 节点、提示词、测试输出或审阅发现。
- 本账本只索引并行写入任务；顺序任务无论风险等级都不创建占位条目。
- 每个状态文件只包含风险、DRI、验收人、租约、共同基线、候选提交、分支、worktree 和写范围；合并后删除状态文件与任务索引行。
- 每个页面设计事实只写入页面 `design-decision.md`；每个资产事实只写入页面 `asset-manifest.md`；每个验收事实只写入任务 `review.md`。
- 修复后只重新审阅受影响的覆盖范围；格式、链接或无语义文案变化通常只需重跑确定性检查。
- 业务流等级完成后记录一条集成冒烟链接；最终平台验证只写入 `docs/architecture/verification-platforms.md`。
