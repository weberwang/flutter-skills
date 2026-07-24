# 并行写入协作协议

本协议只用于多个可写分支必须同时执行的任务。普通、高风险和发布任务如果顺序执行，使用普通分支或 PR，不创建任务状态或 worktree。

## 隔离与所有权

- Controller 先确认集成分支和共同基线，再创建并行任务。
- 每个写入者使用一个 `codex/<task-id>` 分支、一个持续复用的 worktree 和一个互不重叠的写范围。
- 依赖、路由、主题、代码生成配置、共享状态容器和 `docs/design/app-design.pen` 必须串行并由唯一写入者负责。
- 只读探索和独立审查可以并行，不需要 worktree 或任务状态。

## 状态与派发

Controller 是 `.codex-workflow/tasks/<task-id>.yaml` 和 `.codex-workflow/progress.md` 的唯一写入者。状态按 `planned → claimed → implementing → reviewing` 迁移；阻塞时使用 `blocked`，修复后返回 `implementing`。

派发前记录风险、租约、共同基线、分支、worktree、唯一写范围和验证状态，并运行 `scripts/validate-task-state.py`。状态文件保持未提交；任务分支不得携带它。范围、权威输入、非目标和验证命令留在任务简报，不复制到状态文件。

## 验证与审查

1. 实现者在固定 worktree 中完成静态检查、相关测试、审计命令和已知回归夹具。
2. 确定性检查未通过时保持 `implementing`，不创建正式审查快照。
3. 检查通过后提交候选并转为 `reviewing`。
4. 所需审查针对同一候选并行执行，结论写入 `docs/tasks/<task-id>/review.md` 的具名小节。
5. 修复继续使用原 worktree，并只重新派发覆盖受影响事实的审阅者。选择规则见 [task-risk-tiers.md](task-risk-tiers.md)。

## 集成与清理

- 所有必需审查批准候选后，Controller 在集成分支运行 `finalize-task.py <state> --repository <工作目录> --integration-branch <分支>`。
- 脚本只确认 worktree、候选提交、共同基线和 `git diff --check`，然后合并、删除本地 worktree 与任务分支，并删除运行期状态文件。
- 合并冲突会触发 `git merge --abort`；任务所有者在原 worktree 修复后重试。
- 推送、PR 和远端分支清理由正常授权流程处理，不属于本地收尾脚本。
- 完成后在 `review.md` 或账本记录合并与业务流冒烟，再删除已完成任务的账本行。

## 验证层级

- 任务：静态分析、相关测试、任务审计脚本、回归夹具、必要的截图或 golden。
- 业务流等级：合并后执行集成冒烟。
- 最终集成或发布：执行 `docs/architecture/verification-platforms.md` 的完整平台矩阵。
