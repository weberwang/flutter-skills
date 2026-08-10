# 布局实施规格

`layout-spec.yaml` 是页面实现输入，不是运行时状态、合并信号或审查报告。它描述关系和行为，不复制截图坐标；任何固定值都必须有语义边界和回退。

## 必填结构

| 节点 | 要求 |
|---|---|
| `page` | `id`、最小/最大宽高、`orientations`（至少 portrait、landscape） |
| `regions` | 每个区域有 `id`、语义 `role`、`anchors.horizontal`、`anchors.vertical` 和 `size.min/preferred/max`；锚点必须引用父、viewport、safe-area 或另一个语义区域 |
| `breakpoints` | 每项有 `axis`、`value`、`reason`、`change`、`preserves`、`fallback`；值来自内容最低需求，不能只来自设备名称 |
| `content` | `max_width`、`columns`、`gutter`、`margins`，并说明列宽或列数不足时的回退 |
| `system_avoidance` | SafeArea、系统栏、键盘、fold、split 的事实来源、消费层和回退 |
| `scroll` | `vertical` 与 `horizontal` 各有唯一 `owner`、轴语义和窄高/窄宽回退；没有滚动也要显式写 `owner: none` |
| `text_behavior` | 本地化、RTL、文字缩放、换行、增长策略，以及关键动作禁止截断 |
| `overlays` | fixed/floating/pinned/docked 元素的锚点、占位/遮挡、命中区、键盘和窄高回退 |
| `implementation` | 共享 breakpoint resolver、根布局结构、使用的约束 primitives |
| `invariants` | 每条关系不变量有唯一 `id`、关系描述和参数化 `test_ids` |
| `evidence_matrix` | 每个 case 显式声明尺寸、方向、字号、语言、安全区、动作状态和测试 id；不得只填写 `covers` 标签 |

## 关系写法

- 水平方向使用 `start/end/center/width`，纵向使用 `top/bottom/center/height`；每个锚点写 `relation`、`reference` 和可变 `offset`/`token`。
- `reference` 必须是稳定语义边界（例如 `safe_area`, `content_column`, `header`），不要把 `left: 37` 或 `top: 420` 当作通用关系。
- 尺寸同时写 `min/preferred/max`；文本、主要操作和可增长区域不能用固定高度封死。
- 断点说明“触发条件 → 结构变化 → 保留的任务/状态 → 回退”，并由共享 resolver 统一消费。

## 实现信号登记

`implementation_signals` 允许以下信号：`Stack`、`Positioned`、`fixed_width`、`fixed_height`、`floating`、`single_line_truncation`、`handwritten_breakpoint`。每项必须写：

```yaml
- signal: Positioned
  reason: 徽标需要覆盖头像边界
  boundary: avatar bounds
  fallback: 移入标题尾部并保持语义
  test_ids: [badge_anchor_relation]
```

这表示需要在实现和测试中重点关注，并不自动否定规格。缺少依据或测试 id 时验证器才会失败。
