# Output Blueprint

## Goal

Keep every result from this skill structurally stable so that human teams and downstream skills can consume it without re-parsing the design.

## Recommended Output Order

1. `输入摘要`
2. `全局设计结构`
3. `设计 Token 归纳`
4. `亮色主题方案`
5. `暗色主题方案`
6. `组件拆解清单`
7. `页面实现骨架`
8. `高保真 / Flutter 化取舍说明`
9. `实现边界建议`
10. `可供 flutter-init 消费的规范摘要`
11. `风险与待确认项`

## Required Row Schema

For important sections, components, or theme decisions, prefer a row or grouped bullets containing:

- `设计原意`
- `Flutter 落法`
- `是否高保真`
- `是否进入主题层`
- `是否抽成复用组件`
- `风险/备注`

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
