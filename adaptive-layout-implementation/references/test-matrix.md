# 参数化关系测试矩阵

证据矩阵是实施产物，与候选 SHA 无关；它描述必须运行的场景和绑定的 test id。验证器读取每个 case 的显式字段，不接受只写 `covers` 的摘要。

## 必须覆盖的维度

对每个结构断点 `b` 生成 `offset: -1, 0, +1` 的 case（即 `b-1/b/b+1`）。另外至少包含：

- 同一宽度的两个不同高度，包含一个窄高回退场景；
- `portrait` 与 `landscape`；
- 数值 `text_scale` 必须分别等于规格声明的 `text_behavior.text_scale.default` 与 `large`（大字号建议 `>= 1.3`）；
- `locale: default` 与 `locale: longest_copy`；
- `safe_area: zero` 与 `safe_area: nonzero`；
- 关键动作 `default`、`disabled`、`submitting`。

## 最小充分生成规则

先为每个断点边缘生成三条 case，再把方向、字号、语言、安全区和动作状态组合到高风险断点或同宽不同高 case；若规格声明某维度影响结构，则为该维度保留独立 case。每个 case 必须列出 `test_ids`，每条 invariant 的所有 test id 至少被一个 case 执行。

## 证据边界

关系测试应验证锚点、最小触控尺寸、可滚动到末项、无文本截断、无遮挡和断点结构；Golden 只在冻结的逻辑视口、方向、字号和系统 inset 下验证精确视觉。不得用一个手机截图替代关系矩阵。
