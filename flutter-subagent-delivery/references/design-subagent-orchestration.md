# Design Subagent Orchestration

## 角色

| 角色 | 核心职责 | 禁止事项 |
|---|---|---|
| UX/UI Lead / Page Contract Agent | 输出语义合同、状态、交互、响应式边界、无障碍、ownership，并选择 Code Sketch Level | 写页面代码、自审结构实现 |
| Code Sketch Agent（Flutter Engineer） | 在生产 Flutter 骨架实现中性草图、稳定 key、Widget/关系测试与结构证据 | 建一次性重复页、冻结最终视觉、自审放行 |
| Code Sketch Reviewer（独立 QA/UX） | 只读审阅不可变 candidate、sketch spec hash、测试和截图 hash | 修改候选、与 producer 使用同一 agent |
| Page High-Fidelity Agent | Code Sketch Review 后生成 transient 高保真候选 | 持久化未冻结候选、改变语义合同 |
| Effect Image Reviewer | 独立审阅候选的产品/视觉质量与合同变化 | 修改、选择或冻结候选 |
| Bitmap Decomposition / Asset Agents | 在 asset manifest 完成 ownership、覆盖、编号确认和生产 | 在 design decision 复制明细、未确认即生产 |
| Fidelity Implementer | 在同一生产骨架重构高保真 UI，升级同一 layout-spec | 用绝对叠层覆盖旧草图凑像素 |
| Visual QA Reviewer | 对 fidelity spec、实际测量和 target/Flutter 同视口截图做独立复核 | 用 validator、Golden 或单独目测替代完整 gate |

## 顺序

preflight → Page Contract Agent → `phase: sketch` layout-spec validator → Code Sketch Agent → analyze/Widget/关系测试 → 风险需要的确定性截图 → 独立 Code Sketch Reviewer → 高保真生成/审阅/用户冻结 → 高保真目标与合同回对 → bitmap decomposition/覆盖审计/编号确认/资产生产或 N/A → 同一 layout-spec 升级 `phase: fidelity` → 同一 Flutter 骨架还原 → fidelity validator/实际 Widget measurement/target↔Flutter screenshot parity → Visual QA → F0/F1/F2/F3。

合同回对发现范围、状态、导航语义、滚动 owner、断点、无障碍或 data/UI/asset ownership 变化时，返回 Page Contract 与 Code Sketch 阶段更新并独立重审。

所有写作用不重叠 scope 串行交接。冻结、用户确认、审阅收敛和 canonical decision 只由 Controller 记录。
