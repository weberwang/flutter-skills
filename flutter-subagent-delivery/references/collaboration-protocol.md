# 团队协作协议

本协议只用于并发、多代理、`high` 或 `release` 可写任务。轻量任务和顺序执行的标准任务使用普通分支流程，不创建任务状态或 worktree。

## 任务隔离

- Controller 先确认真实集成分支和基线提交，再创建任务。
- 每个受控任务只创建一个 `codex/<task-id>` 分支和一个独立 worktree，并持续使用到最终验收或明确放弃。
- 修复和定向复审继续使用原 worktree；不得按审查轮次重建、合并或清理 worktree。
- 依赖、路由、主题、代码生成配置、共享状态容器和 `docs/design/app-design.pen` 必须有唯一写入者。
- 每个任务只保留 `docs/tasks/<task-id>/review.md` 作为验收记录；页面和资产事实分别保存在页面设计决策与资产清单中。

## 状态与派发

Controller 是 `.codex-workflow/tasks/<task-id>.yaml` 和 `.codex-workflow/progress.md` 的唯一写入者。状态按 `planned → claimed → implementing → reviewing → integrating → accepted` 迁移；阻塞时使用 `blocked`，修复后返回 `implementing`。

派发前记录任务风险、基线、租约、分支、worktree、唯一写入范围、权威输入和验证命令，并运行 `scripts/validate-task-state.py`。实现者和审阅者不得修改任务状态、账本、其他任务目录或集成分支。

活动状态文件只保留在 Controller 集成 worktree，任务分支不得携带自己的活动状态。自动收尾前，集成 worktree 除当前任务状态文件外必须干净。

## 先验证后审查

1. 实现者在原 worktree 中完成构建、静态检查、相关测试、审计命令和已知回归夹具。
2. 任一定义明确的命令仍失败时，任务保持 `implementing`；不得创建正式审查快照。
3. 所有确定性检查通过后，形成候选提交并转为 `reviewing`。
4. 所需 Product、QA、技术和视觉审查针对同一候选并行执行，结论写入同一 `review.md` 的具名小节。
5. 修复产生新候选后，仅重新派发覆盖受影响事实的审阅者。选择规则见 [task-risk-tiers.md](task-risk-tiers.md)。

不可变快照变化意味着旧快照不能证明新提交，但不等于所有审查维度都失效。未受影响的结论可在 `review.md` 中保留，并明确其覆盖范围和沿用依据。

## 集成与清理

- 所有必需审查批准最终候选后，Controller 仅运行一次 `finalize-task.py`。脚本检查状态、候选提交、报告、租约、基线和 `git diff --check`，合并任务分支，清理任务 worktree 和本地分支，并只提交最终接受状态；`integrating` 是失败重试状态，不再产生独立提交。
- 冲突会撤销半完成合并；任务所有者在原任务分支修复后重试，不创建替代 worktree。
- 只有团队授权时才使用 `--remote origin` 删除远端临时分支。
- 清理状态、链接或格式修正不启动新的产品或 QA 审查轮次。

## 验证层级

- 任务：静态分析、相关测试、任务审计脚本、回归夹具、必要的截图或 golden。
- 业务流等级：合并后执行集成冒烟，不把它登记为完整平台验证。
- 最终集成或发布：执行 `docs/architecture/verification-platforms.md` 中的完整平台矩阵。
