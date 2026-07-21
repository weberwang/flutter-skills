# 团队协作协议

在任何可写任务开始前，由 Controller 创建并认领任务状态文件。实现、修复、生成代码和资产的代理只能在该状态文件指定的分支与 worktree 中写入；审阅代理只写入自己的任务报告，不得修改实现分支。

## 任务隔离

- 每个可写任务使用 `codex/<task-id>` 分支和独立 worktree，基线为 Controller 记录的集成分支提交。
- 每个页面的设计产物写入 `docs/design/pages/<page-name>/`；全局设计产物仅写入 `docs/design/global/`。不得用全局同名文件承载页面状态。
- 每个任务的简报、实现报告、审阅、视觉 QA、证据清单和清理记录写入 `docs/tasks/<task-id>/`。任务完成后这些报告只追加，不覆盖其他任务记录。
- 依赖、路由、主题、代码生成配置、共享状态容器和生成文件为串行所有权；模块图必须明确其唯一写入任务。

## 状态与派发

Controller 是 `.codex-workflow/tasks/<task-id>.yaml` 和 `.codex-workflow/progress.md` 的唯一写入者。状态只能按 `planned → claimed → implementing → reviewing → accepted` 迁移；遇到阻塞使用 `blocked`，修复后回到 `implementing`。认领前检查租约、基线提交和写入范围；过期租约必须由 Controller 显式释放，不得由其他代理抢占。每次创建或迁移状态后运行 `python <flutter-subagent-delivery>/scripts/validate-task-state.py .codex-workflow/tasks/<task-id>.yaml`。

派发内容必须包含：任务 ID、状态文件、基线提交、分支/worktree、唯一写入范围、输入产物、输出路径、验证命令和非目标。代理不得修改任务状态、账本、其他任务目录或集成分支。

## 集成与证据

- 实现和修复在同一任务分支完成，并形成一个可审查提交；Controller 在合并前执行 `git diff --check`、审阅门禁和任务验证。
- Controller 将通过的任务合并到集成分支，记录提交 SHA、审阅报告和证据清单；冲突仅由对应任务所有者处理。
- 视觉冻结后，保留 `docs/tasks/<task-id>/evidence/visual-decision.md`，至少记录候选 ID、提示词哈希、评审结论、确认时间、冻结文件哈希和删除清单。可删除未选原图，但不得删除该最小审计记录。

## 验证层级

- 任务：静态分析、相关单元/组件测试、golden 或截图设计证据。
- 业务流等级：合并到集成分支后运行集成冒烟；这是一项回归检查，不得把它登记为全平台验证。
- 最终集成：执行 `docs/architecture/verification-platforms.md` 中的完整平台矩阵，并更新平台验证状态。
