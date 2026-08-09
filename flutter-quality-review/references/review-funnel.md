# F0-F3 审核漏斗

## 四级职责

| 级别 | 执行者 | 行为 | 输出 |
|---|---|---|---|
| F0 实际验证 | 实现者 | 执行项目原生分析、构建、测试、审计、迁移和回归命令 | 命令证据、候选 SHA、变更摘要 |
| F1 分诊 | Controller | 检查候选身份、范围、风险、验收追踪和证据，选择必要通道 | 必需 F2 通道及理由，或退回实现 |
| F2 只读审核 | 独立审阅者 | 只读同一候选的指定专业维度；互不依赖通道可并行 | 返回结构化结论，不写共享文件 |
| F3 收敛 | Controller | 确认必需结论覆盖有效候选、阻塞关闭、集成条件满足 | 批准、退回或阻塞 |

F0 不是命令清单或状态字段；必须实际执行项目原生命令。F1 只分诊，不代替专业审核。F3 只收敛，不重做 F2。

## 风险与通道

| 风险 | F2 最小要求 |
|---|---|
| `light` | 通常无，Controller 自检后 F3 |
| `standard` | 行为/验收变化启用 QA；其他按触发条件 |
| `high` | QA，加上导致升级的 Product、技术、视觉或 Release 通道 |
| `release` | QA、技术、Release；Product/视觉按变化触发 |

API 契约/版本、权限安全、幂等重试、迁移回滚、服务端测试、部署监控、备份恢复或客户端兼容变化触发技术通道；发布/生产变更同时触发 Release。若服务端实现不在范围内，只审核已记录的依赖、所有者和客户端边界。

## F2 返回结构

```text
Lane: Product / QA / technical / visual / Release
Candidate SHA:
Covered facts and evidence:
Findings:
- [Critical|Important|Minor] file:line — ...
Missing evidence:
Open questions:
Verdict: approved / changes_requested / blocked
```

视觉通道另加 aesthetic verdict。审阅者不得直接修改 `docs/tasks/<task-id>/review.md`。

## `review.md` 生命周期与单写者

仅在风险或交接需要持久审核时创建 `docs/tasks/<task-id>/review.md`，且 Controller 是从创建到关闭的唯一写入者：

1. F0 后创建：记录任务、候选 SHA、基线、diff 范围和命令证据引用。
2. F1 后记录：风险、变化维度、必需通道、触发理由和退回/派发结论。
3. F2 返回后引用：记录审阅者、时间、候选 SHA、覆盖事实、证据、发现和原始结论位置；不允许多个审阅者并行写同一文件。
4. 修复产生新 SHA：保留历史候选，明确哪些通道因覆盖事实变化而失效，重新绑定新结论。
5. F3 关闭：列出有效通道、已关闭阻塞、集成/CI 事实和最终结论。

`review.md` 只留存决策、证据与结论，不驱动状态机、自动合并或清理。

## 平台证据

- 共享基础后的代表性启动/路由/插件烟测可进入早期审核。
- 关键业务流后的主目标平台运行烟测可证明该流。
- 只有最终集成/发布完整矩阵可形成平台全量结论。
- 不得自动发起真机验收。

## 退回与集成

任何 Critical、未解决 Important、必需证据缺失或 `changes_requested` 都退回实现。新候选重跑 F0/F1，只重开覆盖事实变化的通道。

F3 批准不自动合并。合并前 Controller 仍须检查当前分支、候选 SHA、干净工作区、`git diff --check`、必需测试/CI、审核结论和授权，并通过标准 Git/PR/CI 集成。
