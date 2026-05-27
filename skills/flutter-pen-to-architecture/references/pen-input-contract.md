# Pencil Input Contract

## Purpose

Define the minimum Pencil MCP evidence required before this skill can produce reliable Flutter architecture and asset-export guidance.

## Canonical Input Model

- `.pen` 文件应被视为通过 Pencil MCP 打开的设计输入，而不是 ZIP 解析对象。
- 在没有 MCP 上下文的情况下，不应自行推断 `.pen` 内部结构、资源清单或节点关系。
- 结构、变量、布局和导出结果都以 Pencil MCP 返回内容为准。

## Core MCP Calls

1. `get_editor_state(include_schema: true)`
2. `batch_get`
3. `snapshot_layout`

以上调用构成分析主流程，承担不同职责，不能互相替代：

- `get_editor_state(include_schema: true)`：先拿到当前 `.pen` 编辑态与 schema，确认后续节点读取和分析参数合法。
- `batch_get`：批量读取页面、节点树、变量、实例关系与命名语义，是结构分析的主入口。
- `snapshot_layout`：在层级关系不足以表达真实布局时，补充区域划分、尺寸关系与关键视觉定位。

## Conditional MCP Calls

1. `export_nodes`

仅当输出需要生成 `exported assets` 与 `Flutter assets` 映射时，才执行这类按需调用：

- `export_nodes`：当分析结论确认某些节点需要位图资源时，用于执行导出并生成可追踪的输出文件。

## Preferred Input Order

1. 已通过 Pencil MCP 打开的 `.pen` 文档
2. 来自 `get_editor_state(include_schema: true)` 的编辑态与 schema
3. 来自 `batch_get` 的节点树、页面结构、变量与复用关系
4. 来自 `snapshot_layout` 的布局快照或结构几何摘要
5. 基于分析结果判断是否需要 `export_nodes`
6. 如需导出，再读取来自 `export_nodes` 的资源导出结果
7. 截图仅作为辅助证据，不能替代上述 MCP 输入

## Minimum Acceptable Input

Use the skill normally when you have:

- at least one `.pen` document opened in Pencil MCP
- `get_editor_state(include_schema: true)` 返回可用的编辑态与 schema
- enough `batch_get` structure to identify major page regions
- enough style or variable evidence to infer typography, color, and reuse boundaries
- `snapshot_layout` 已在需要几何确认的区域提供必要布局证据

在满足以上分析输入前，不应提前执行 `export_nodes`。如果存在可复用实例、变量或稳定命名，应将其视为比截图和绝对坐标更高置信度的输入。

## When Input Is Strong Enough For Global Analysis

Proceed with whole-system analysis when most of the following are available:

- multiple related screens or one `.pen` document with multiple top-level flows
- reusable instances or repeated structural patterns visible in `batch_get`
- variables or clearly repeated style values
- navigation, shell, or layout clues confirmed by `snapshot_layout`

In this mode, bias toward extracting shared tokens, shell structure, and component families first.

## When Input Is Only Strong Enough For Partial Analysis

Downgrade the output when:

- only one screen is available
- variables are absent
- node names are noisy or non-semantic
- repeated components cannot be identified confidently
- layout snapshots are missing where geometry matters

In this case, output:

- `前提假设`
- `待确认项`
- `局部结论`

Do not pretend the design system is fully known.

## Unsupported Primary Inputs

Do not treat these as the main trigger for this skill:

- raw screenshots without MCP structure
- textual design descriptions without `.pen` or Pencil MCP data
- visual moodboards with no layout or interaction context

If the user only has those inputs, explain that the output will be approximate and that Pencil MCP input is still preferred.

## Special Handling Rules

- Prefer semantic structure over geometry.
- Prefer repeated patterns over isolated edge cases.
- Prefer variables and instances over manual visual guessing.
- If two data sources conflict, trust `.pen` structure and reusable-instance relationships before screenshot appearance.
- 只有在确认节点需要真实图片资源时才调用 `export_nodes`，避免把可 Flutter 化的结构误导出为位图。
