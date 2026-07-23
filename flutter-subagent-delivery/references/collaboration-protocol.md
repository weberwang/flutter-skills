# 团队协作协议

本协议用于需要持久任务状态或自动集成的 `standard`、`high`、`release` 和多代理可写任务。风险等级决定审查强度，隔离模式独立选择；轻量任务不创建任务状态。

## 任务隔离

- Controller 先确认真实集成分支和基线提交，再创建任务。
- 每个受控任务创建一个 `codex/<task-id>` 分支。单写者和顺序交接默认使用 `branch` 隔离。
- 只有多个分支需要同时写入时才使用 `worktree` 隔离。
- 修复和定向复审继续使用原任务分支；选择 worktree 时持续复用同一个，不得按审查轮次重建。
- 依赖、路由、主题、代码生成配置、共享状态容器和 `docs/design/app-design.pen` 必须有唯一写入者。
- 每个任务只保留 `docs/tasks/<task-id>/review.md` 作为验收记录；页面和资产事实分别保存在页面设计决策与资产清单中。

## 状态与派发

Controller 是 `.codex-workflow/tasks/<task-id>.yaml` 和 `.codex-workflow/progress.md` 的唯一写入者。状态按 `planned → claimed → implementing → reviewing → integrating → accepted` 迁移；阻塞时使用 `blocked`，修复后返回 `implementing`。

派发前记录任务风险、隔离模式、基线、租约、分支、唯一写入范围、权威输入和验证命令，并运行 `scripts/validate-task-state.py`。仅 worktree 模式记录 worktree 路径。实现者和审阅者不得修改任务状态、账本、其他任务目录或集成分支。

活动状态文件在任务分支创建后由 Controller 保持未提交；任务分支的提交历史不得携带它。任务开始时若工作区已有改动，实施者须将其作为任务上下文核对并纳入验证，不得误当作本任务新生成的改动。

## 先验证后审查

1. 实现者在原任务分支中完成构建、静态检查、相关测试、审计命令和已知回归夹具；worktree 只是可选检出目录。
2. 任一定义明确的命令仍失败时，任务保持 `implementing`；不得创建正式审查快照。
3. 所有确定性检查通过后，形成候选提交并转为 `reviewing`。
4. 所需 Product、QA、技术和视觉审查针对同一候选并行执行，结论写入同一 `review.md` 的具名小节。
5. 修复产生新候选后，仅重新派发覆盖受影响事实的审阅者。选择规则见 [task-risk-tiers.md](task-risk-tiers.md)。

不可变快照变化意味着旧快照不能证明新提交，但不等于所有审查维度都失效。未受影响的结论可在 `review.md` 中保留，并明确其覆盖范围和沿用依据。

## 集成与清理

- 所有必需审查批准最终候选后，Controller 仅运行一次 `finalize-task.py <state> --repository <工作目录> --integration-branch <分支>`。脚本检查状态、候选提交、报告、租约、基线和 `git diff --check`；branch 模式安全切回集成分支、用 Git 自动暂存机制保留可暂存的既有改动、合并并删除任务分支，worktree 模式额外验证并删除 worktree；最后只提交接受状态。
- 冲突会撤销半完成合并；任务所有者在原任务分支修复后重试，不创建替代分支或 worktree。
- 只有团队授权时才使用 `--remote origin` 删除远端临时分支。
- 清理状态、链接或格式修正不启动新的产品或 QA 审查轮次。

## 验证层级

- 任务：静态分析、相关测试、任务审计脚本、回归夹具、必要的截图或 golden。
- 业务流等级：合并后执行集成冒烟，不把它登记为完整平台验证。
- 最终集成或发布：执行 `docs/architecture/verification-platforms.md` 中的完整平台矩阵。
