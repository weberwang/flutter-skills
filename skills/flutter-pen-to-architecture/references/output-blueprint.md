# Output Blueprint

## Goal

Keep every result from this skill structurally stable so that human teams and downstream skills can consume it without re-parsing the design.

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

## Additional Output Sections

1. `图片资源导出结果`
2. `图片资源映射表`
3. `Flutter 资源接入结果`

## Required Row Schema

For important sections, components, or theme decisions, prefer a row or grouped bullets containing:

- `设计原意`
- `Flutter 落法`
- `是否高保真`
- `是否进入主题层`
- `是否抽成复用组件`
- `风险/备注`

对于图片资源映射，至少补充以下判断：

- `Pencil 节点 ID`
- `MCP 返回路径`
- `建议用途`
- `是否建议高保真使用`
- `是否发生同名覆盖`

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
