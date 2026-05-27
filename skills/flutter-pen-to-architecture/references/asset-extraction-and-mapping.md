# Asset Extraction And Mapping

## Purpose

Define how image-like design nodes are exported from Pencil MCP, how `exported assets` land in Flutter, and how `Flutter assets` should be mapped for downstream implementation.

## Export Nodes Workflow

1. Inspect candidate nodes through Pencil MCP structure and layout evidence.
2. Use `export_nodes` as the canonical export step.
3. Write exported files to `<projectRoot>/assets/images/` by default.
4. Use `png` as the default export format unless a task explicitly requires another format.
5. Produce a stable mapping from Pencil node context to Flutter consumption path.

## Export Rules

- 只导出确实需要位图保真的节点，例如插画、照片、复杂纹理、难以用 Flutter 组件复刻的混合视觉内容。
- 简单色块、基础图标、分割线、纯容器背景等优先保留为 Flutter 原生实现，不应为了省事全部转成图片。
- `exported assets` 指 `export_nodes` 真实落盘后的文件结果，必须能回溯到具体节点。
- `Flutter assets` 指 Flutter 工程中准备通过 `Image.asset(...)` 等方式消费的资源路径，默认位于 `assets/images/`。
- 若多个节点会生成相同文件名，应优先采用业务可读命名，并在映射结果中记录最终落盘路径，避免后续实现阶段混淆来源。
- 本文档只定义导出与映射规则，不要求自动修改 Flutter 工程文件。

## Mapping Requirements

每个导出结果都应同时保留设计侧语义和 Flutter 侧落点，便于后续判断资源是否该保留高保真、是否值得继续组件化。

## Output Fields

| 字段 | 说明 |
| --- | --- |
| `节点 ID` | Pencil MCP 中用于定位导出节点的稳定标识。 |
| `节点名称` | 节点当前名称；如果名称噪声较大，也应原样保留，方便人工回查。 |
| `导出文件绝对路径` | `export_nodes` 实际导出的绝对路径。 |
| `Flutter 相对路径` | 相对 Flutter 工程根目录的资源路径，默认形如 `assets/images/...`。 |
| `建议业务命名` | 面向业务语义的推荐文件名或资源名，用于减少纯视觉名称带来的歧义。 |
| `页面/组件归属` | 资源主要服务的页面、模块或组件。 |
| `建议用途` | 例如背景图、插画、卡片封面、品牌装饰、头像占位图等。 |
| `是否建议高保真使用` | 标记该资源是否应尽量保持设计稿导出效果，而不是继续 Flutter 化重绘。 |
| `备注` | 记录重名处理、裁切说明、透明通道、导出异常、替代实现建议等补充信息。 |
