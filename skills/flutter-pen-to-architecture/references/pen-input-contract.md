# Pencil Input Contract

## Purpose

Define what input quality is required before this skill can make reliable Flutter architecture recommendations.

## Preferred Input Order

1. `.pen` file structure
2. Pencil MCP node tree
3. Pencil MCP variables
4. Pencil MCP layout snapshots or structural geometry summaries
5. Screenshots only as supporting evidence, never as the primary source

## Minimum Acceptable Input

Use the skill normally when you have:

- at least one `.pen` file or an MCP node tree
- enough screen structure to identify major page regions
- enough styling clues to infer typography and color groupings

If reusable component instances or variables are present, treat them as higher-confidence signals than screenshots or absolute coordinates.

## When Input Is Strong Enough For Global Analysis

Proceed with whole-system analysis when most of the following are available:

- multiple related screens or a single `.pen` document with multiple top-level flows
- reusable instances or repeated structural patterns
- variables or clearly repeated style values
- navigation or shell clues

In this mode, bias toward extracting a shared token system and component families first.

## When Input Is Only Strong Enough For Partial Analysis

Downgrade the output when:

- only one screen is available
- variables are absent
- node names are noisy or non-semantic
- repeated components cannot be identified confidently
- dark-theme clues do not exist

In this case, output:

- `前提假设`
- `待确认项`
- `局部结论`

Do not pretend the design system is fully known.

## Unsupported Primary Inputs

Do not treat these as the main trigger for this skill:

- raw screenshots without structure
- textual design descriptions without `.pen` or MCP data
- visual moodboards with no layout or interaction context

If the user only has those inputs, recommend a design-direction skill first or explain that the output will be approximate.

## Special Handling Rules

- Prefer semantic structure over geometry.
- Prefer repeated patterns over isolated edge cases.
- Prefer variables and instances over manual visual guessing.
- If two data sources conflict, trust `.pen` structure and reusable-instance relationships before screenshot appearance.

## Asset Fallback

- Prefer `.pen` embedded assets.
- Use Pencil MCP only when `.pen` does not provide enough exportable image data.
- 如果发生同名资源覆盖，需要在结果中显式标记，方便后续 Flutter 还原核对来源与最新版本。
