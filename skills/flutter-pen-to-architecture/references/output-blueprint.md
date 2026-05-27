# Output Blueprint

## Goal

Keep every result from this skill structurally stable so that human teams and downstream skills can consume it without reopening the design tree.

## Recommended Output Order

1. `输入摘要`
2. `图片资源导出结果`
3. `图片资源映射表`
4. `Flutter 资源接入结果`
5. `全局设计结构`
6. `设计 Token 归纳`
7. `亮色主题方案`
8. `暗色主题方案`
9. `组件拆解清单`
10. `页面实现骨架`
11. `高保真 / Flutter 化取舍说明`
12. `实现边界建议`
13. `可供 flutter-init 消费的规范摘要`
14. `风险与待确认项`

## 图片资源导出结果

- 汇总 `export_nodes` 的执行结果，包括成功数量、失败数量、默认导出目录 `<projectRoot>/assets/images/`、默认格式 `png`。
- 对每个导出批次说明是否存在重名调整、人工命名修正或需要重新导出的异常情况。
- 这里只报告实际导出结果，不延伸声称 Flutter 工程已自动接入这些资源。

## 图片资源映射表

资源映射表应至少覆盖以下字段：

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

如果某些节点经过筛选后不导出，也应在备注中说明原因，例如“建议改用 Flutter 原生绘制”或“仅作为布局参考”。

## Flutter 资源接入结果

- 只报告 `pubspec.yaml` 中是否已声明相关 `Flutter assets`，例如“已声明”“未声明”“无法确认”。
- 明确区分“检查结果”和“修改动作”：这里不能声称已经修改 `pubspec.yaml`、移动文件或自动接入资源。
- 如果发现声明缺失，可以给出建议声明路径，但结果表述仍应保持为检查结论。

## Required Row Schema

For important sections, components, or theme decisions, prefer a row or grouped bullets containing:

- `设计原意`
- `Flutter 落法`
- `是否高保真`
- `是否进入主题层`
- `是否抽成复用组件`
- `风险/备注`

对于图片资源相关条目，至少补充以下判断：

- `建议用途`
- `是否建议高保真使用`
- `Flutter 资源接入状态`

## flutter-init Summary Contract

The `可供 flutter-init 消费的规范摘要` section should include at least:

- theme constraints
- token constraints
- component constraints
- page-shell constraints
- high-fidelity boundaries
- Flutterization boundaries

## Quality Bar

The final output should make these handoffs easy:

- a Flutter architect can decide shared theming structure
- a UI engineer can identify which widgets deserve reuse
- a project-guardrails skill can extract durable constraints
- an implementation skill can continue without reopening the design tree
