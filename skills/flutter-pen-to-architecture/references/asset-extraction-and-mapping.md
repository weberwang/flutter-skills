# Asset Extraction And Mapping

## Purpose

Define which image resources should be exported, how they land in `assets/images/`, and how they should be consumed during Flutter restoration.

## Priority

1. Pencil MCP `export_nodes` output for selected design nodes
2. Existing project files under `assets/images/` when the asset has already been exported

## Export Rules

- 仅导出可直接参与 Flutter 还原的图片资源，不把普通视觉节点一律转成图片。
- 默认导出到 `assets/images/`，方便后续直接通过 `Image.asset(...)` 消费。
- 只能通过 Pencil MCP 访问 `.pen` 设计与导出节点，不要直接读取、解包或解析 `.pen` 文件。
- 使用 Pencil MCP `export_nodes` 导出选定节点，导出结果以 MCP 返回的绝对路径为准。
- 导出前读取或列出 `assets/images/`，导出后再次读取或核对 MCP 返回路径，记录同名覆盖行为。
- `pubspec.yaml` 通过读取文件、定向补丁和复读验证来接入 `assets/images/`，不需要本地脚本。

## Output Fields

- `原始资源标识`
- `Pencil 节点 ID`
- `导出文件`
- `MCP 返回路径`
- `Flutter 路径`
- `来源`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `是否发生同名覆盖`
- `备注`
