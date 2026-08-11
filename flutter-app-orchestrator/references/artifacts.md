# 最小工件矩阵

只为决策、可复现验证或跨角色交接创建工件。一个事实只能有一个权威位置；其他文档只链接，不复制字段、`N/A` 理由或证据摘要。

## 全局工件

| 工件 | 创建时机 | 权威内容 |
|---|---|---|
| `docs/product/product-brief.md` | 产品确认 | MVP、用户故事、验收、市场依据与产品性格 |
| `docs/product/grilling-log.md` | 用户作出关键决定 | 确认记录与尚未解决的决定 |
| `docs/design/ui-spec.md` | UX/UI 设计 | 流程、页面/状态和全局质量约束 |
| `docs/design/global-design-freeze.md` | 用户冻结方向 | 选定方向、签名、成本承诺和精简提示词哈希 |
| `docs/architecture/technical-design.md` | 技术门禁 | 架构、依赖能力档、API/服务边界、迁移恢复与风险决策 |
| `docs/architecture/flutter-init.md` | 项目初始化 | 已启用依赖能力档、启用原因与项目本地 `flutter-dev` 路径 |
| `docs/architecture/verification-platforms.md` | 技术设计 | 平台范围、分层烟测、完整矩阵命令和运行时证据 |
| `docs/plans/module-map.md` | 实施规划 | 模块、依赖、业务流等级和共享资源所有者 |
| `docs/plans/implementation-plan.md` | 实施规划 | 粗粒度里程碑和模块顺序 |
| `docs/plans/modules/<module-name>-scope.md` | 模块变为可实施时 | 已确认的功能、非目标、契约与验收路径 |

不要另建 MVP、用户故事、市场分析、流程、屏幕规格或 UI 质量门禁文档；这些是产品简报或 UI 规格中的章节。只有用户要求独立交付件时才拆出。

## 条件工件

| 条件 | 工件 | 必须包含 |
|---|---|---|
| 页面有 UI 决策 | `docs/design/pages/<page-name>/design-decision.md` | 语义契约、Code Sketch Level/审阅、冻结图 ID/哈希、合同回对、偏差与 Visual QA |
| 页面需要自适应布局实施 | `docs/design/pages/<page-name>/layout-spec.yaml` | 实施输入：目标视口、语义锚点、尺寸/断点、内容容器、系统避让、滚动/停靠、文本增长、不变量和参数化关系测试矩阵；不是运行时状态或合并信号 |
| 页面有固定视觉资产 | `docs/design/pages/<page-name>/asset-manifest.md` | 资产来源、许可、生产/背景/切图决定、Flutter 路径和保真结论 |
| 页面 Code Sketch | 生产 Flutter 页面与测试 | 中性生产骨架、稳定 key、关系测试与风险需要的截图 |
| 页面冻结 | `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` | 唯一选中原图 |
| 任务需要跨角色交接 | `docs/tasks/<task-id>/brief.md` | 目标、边界、唯一写范围、候选分支、验证命令与验收条件 |
| 任务需要持久化独立验收 | `docs/tasks/<task-id>/review.md` | 候选 SHA、F0 证据引用、F1 分诊、F2 结构化结论、失效记录与 F3 结果；仅 Controller 写入 |
| 发布 | `docs/release/release-checklist.md` | 仅发布范围内的证据和阻塞项 |

未满足条件时不创建占位文件，也不写 `N/A` 文档。所有流程状态、任务简报与审核/决策记录使用 Markdown，只用于决策、证据和结论留痕，不是运行期状态机、自动化输入或合并信号；视觉、设计和代码资产保持其原生格式。

## 交接规则

- 实现者先完成项目原生 F0 命令，再返回候选 SHA、变更文件、验证摘要和阻塞项；需要独立验收时，由 Controller 将证据引用写入 `review.md`。
- F2 审阅者只读候选并返回结构化结论，不直接写共享文件。Controller 是 `review.md` 唯一写入者，并记录作者、候选 SHA、覆盖事实、发现、结论和失效历史。
- ownership、覆盖审计、编号映射和资产生产明细只存到页面 `asset-manifest.md`；冻结决策只存页面 decision，不复制进任务简报或进度账本。
- 并行写入即使经用户明确授权，也只依赖普通分支、Markdown 任务简报和 Git/PR/CI 事实；不创建 YAML/JSON 状态，不自动合并。
- 截图、golden、命令输出和冻结图使用文件路径或 SHA 引用，不转写内容。
