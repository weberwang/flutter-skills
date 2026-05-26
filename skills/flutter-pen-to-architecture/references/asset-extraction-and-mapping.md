# Asset Extraction And Mapping

## Purpose

Define which image resources should be exported, how they land in `assets/images/`, and how they should be consumed during Flutter restoration.

## Priority

1. `.pen` embedded assets
2. Pencil MCP manifest fallback

## Export Rules

- 仅导出可直接参与 Flutter 还原的图片资源，不把普通视觉节点一律转成图片。
- 默认导出到 `assets/images/`，方便后续直接通过 `Image.asset(...)` 消费。
- 若目标目录已存在同名文件，默认覆盖，并在输出结果中记录覆盖行为，避免旧资源残留误导实现。
- 当 `.pen` 已提供足够的可导出图片时，不再额外混入 Pencil MCP 资源，降低来源混杂带来的追踪成本。

## Output Fields

- `原始资源标识`
- `导出文件`
- `Flutter 路径`
- `来源`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`
