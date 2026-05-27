# flutter-pen-to-architecture 图片资源导出扩展设计文档（已废弃）

> 状态：已废弃
>
> 替代文档：`docs/superpowers/specs/2026-05-27-flutter-pen-to-architecture-mcp-export-design.md`

## 废弃原因

- 旧方案依赖 `export_pen_assets.mjs` 解析 `.pen`
- 旧方案依赖 `ensure_flutter_assets.mjs` 自动修改 `pubspec.yaml`
- 当前方案已统一切换为通过 `Pencil MCP` 的 `export_nodes` 直接导出节点
- `pubspec.yaml` 在当前方案中只检查与提示，不再自动修改

## 历史备注

这份文档仅保留为脚本方案历史记录，不再作为当前实现依据。
