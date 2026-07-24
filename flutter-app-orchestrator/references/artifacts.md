# 最小工件矩阵

只为决策、可复现验证或跨角色交接创建工件。一个事实只能有一个权威位置；其他文档只链接，不复制字段、`N/A` 理由或证据摘要。

## 全局工件

| 工件 | 创建时机 | 权威内容 |
|---|---|---|
| `docs/product/product-brief.md` | 产品确认 | MVP、用户故事、验收、市场依据与产品性格 |
| `docs/product/grilling-log.md` | 用户作出关键决定 | 确认记录与尚未解决的决定 |
| `docs/design/ui-spec.md` | UX/UI 设计 | 流程、页面/状态和全局质量约束 |
| `docs/design/global-design-freeze.md` | 用户冻结方向 | 选定方向、签名、成本承诺和精简提示词哈希 |
| `docs/architecture/technical-design.md` | 技术门禁 | 架构、契约、数据与风险决策 |
| `docs/architecture/flutter-init.md` | 项目初始化 | 固定栈与项目本地 `flutter-dev` 路径 |
| `docs/architecture/verification-platforms.md` | 技术设计 | 平台范围、命令和最终运行时证据 |
| `docs/plans/module-map.md` | 实施规划 | 模块、依赖、业务流等级和共享资源所有者 |
| `docs/plans/implementation-plan.md` | 实施规划 | 粗粒度里程碑和模块顺序 |
| `docs/plans/modules/<module-name>-scope.md` | 模块变为可实施时 | 已确认的功能、非目标、契约与验收路径 |

不要另建 MVP、用户故事、市场分析、流程、屏幕规格或 UI 质量门禁文档；这些是产品简报或 UI 规格中的章节。只有用户要求独立交付件时才拆出。

## 条件工件

| 条件 | 工件 | 必须包含 |
|---|---|---|
| 页面有 UI 决策 | `docs/design/pages/<page-name>/design-decision.md` | 语义契约、线框级别/审阅、冻结图 ID/哈希、偏差、Pencil 决定与交接约束 |
| 页面有固定视觉资产 | `docs/design/pages/<page-name>/asset-manifest.md` | 资产来源、许可、生产/背景/切图决定、Flutter 路径和保真结论 |
| 需要可编辑 Pencil 交接 | `docs/design/app-design.pen` | 稳定页面/节点 ID；详情链接页面设计决策 |
| 页面冻结 | `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` | 唯一选中原图 |
| 多个可写分支同时执行 | `.codex-workflow/tasks/<task-id>.yaml` | 风险、验证、候选提交、租约、分支、worktree、范围和验收 |
| 任务需要持久化独立验收 | `docs/tasks/<task-id>/review.md` | 各审查维度的覆盖范围、快照、结论、测试/截图链接、发现与清理结果 |
| 发布 | `docs/release/release-checklist.md` | 仅发布范围内的证据和阻塞项 |

未满足条件时不创建占位文件，也不写 `N/A` 文档。顺序任务无论风险等级都不创建任务状态、进度账本条目或自动收尾记录。

## 交接规则

- 实现者先完成确定性验证，再返回提交 SHA、变更文件、验证摘要和阻塞项；需要独立验收时，这些信息写入 `review.md`，不再生成实现报告或证据清单。
- UI 审阅、视觉 QA 和技术验收写入同一 `review.md` 的具名小节；每个小节保留作者、快照和结论。
- 资产、Pencil 和冻结细节只存到对应页面工件，不复制进任务简报、进度账本或审阅报告。
- `.codex-workflow/progress.md` 只索引并行写入任务；合并后删除对应状态和索引行，以页面决策和审阅记录保留长期事实。
- 截图、golden、命令输出和冻结图使用文件路径或 SHA 引用，不转写内容。
