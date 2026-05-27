---
name: flutter-pen-to-architecture
description: Use when translating Pencil `.pen` design files or Pencil MCP structured output into a Flutter-oriented design architecture plan, especially when the task is to inspect structured design data through Pencil MCP, identify export nodes, selectively produce exported assets, verify Flutter assets wiring without changing project files, extract global design tokens, define light and dark themes, decompose reusable components, and decide what should be restored faithfully versus refactored to fit Flutter design philosophy instead of generating code directly.
---

# Flutter Pen To Architecture

## Overview

Turn `Pencil` design sources into a Flutter-facing implementation architecture instead of a node-by-node rebuild. Default to whole-project analysis: extract global tokens, derive light and dark themes, decompose reusable components, plan multi-screen page structure, and explain where high fidelity should yield to Flutter-native structure.

This skill stays architecture-focused for Flutter teams. It does not generate page code, and it does not turn design inspection into project-file mutation.

## Quick Start

- If the user provides `.pen` files or Pencil MCP output, start with global analysis instead of single-screen local optimization.
- If the input only covers one screen, still try to infer reusable tokens, shared shells, and component families before discussing that screen in isolation.
- If the user only wants visual direction refinement or Pencil prompt tuning, use `mobile-ui-design-coach` first instead of this skill.
- If variables, layout hierarchy, or component-instance relationships are missing, output `前提假设` and `待确认项` before giving conclusions.
- If the user asks for direct Flutter code, finish this architecture pass first or hand off the final summary to the downstream implementation skill.
- Prefer Pencil MCP as the primary intake path even when a `.pen` file exists locally.
- `建议业务命名`：when exported assets are necessary, describe a recommended business-facing name in the report, but keep the exported file name unchanged unless the user explicitly asks for renaming.

## Pencil MCP Intake Flow

1. Run `get_editor_state(include_schema: true)` first to confirm the active `.pen` document, node schema, page structure, and whether the MCP session already exposes enough context for architecture work.
2. Use `batch_get` to fetch only the pages, artboards, components, variables, and reusable sections that matter to the requested architecture scope.
3. Use `snapshot_layout` on key screens or repeated sections to capture layout relationships that are easier to reason about visually than from raw node trees alone.
4. Use `export_nodes` only for the export nodes that truly need raster export support in the Flutter plan, such as illustrations, brand textures, or image-heavy surfaces that should not be rebuilt as widgets.
5. Convert the gathered MCP output into Flutter-facing structure: tokens, themes, shell patterns, component families, state zones, and fidelity decisions.

Notes:

- 先拿到 schema，再按需抓节点，避免无边界地读整份设计。
- 导出只服务于架构判断和资源映射，不要把“能导出”误当成“必须整页导出”。

## Workflow

1. Identify the real input surface: active Pencil MCP document, available page ranges, variables, reusable components, layout hierarchy, missing structural data, and whether a Flutter project root is available.
2. Establish the MCP context with `get_editor_state(include_schema: true)` before making any architectural claim.
3. Narrow the analysis scope with `batch_get` so the result reflects business structure instead of an indiscriminate full-file dump.
4. Inspect important layout groupings with `snapshot_layout` when hierarchy alone does not explain spacing, alignment, or shell composition clearly.
5. Decide which visual elements should stay as export nodes that produce exported assets and which should become Flutter primitives or composite widgets.
6. If exported assets are required, use `export_nodes` selectively and record exactly which export nodes were exported, why they were exported, and where Flutter should consume the exported assets.
7. Check whether `pubspec.yaml` already declares the relevant Flutter assets directory, and report the finding; do not modify `pubspec.yaml`.
8. Scan the design system as a whole: page families, navigation shells, information hierarchy, repeated motifs, and semantic surfaces.
9. Extract design tokens for color, typography, spacing, radius, elevation, and status semantics.
10. Build a dual-theme strategy for light and dark instead of treating dark mode as a color inversion.
11. Decompose the UI into reusable layers: primitives, composite widgets, business widgets, and page sections.
12. Plan screen architecture across the whole flow: shells, content regions, state zones, overlays, and transitions between screens.
13. Classify key decisions into `建议高保真还原`, `建议 Flutter 化重构`, or `建议简化处理`, and explain why.
14. Produce an output pack that a Flutter team and `flutter-init` can consume directly, including MCP evidence, exported assets usage decisions, Flutter assets wiring findings, and implementation boundaries.

## Hard Rules

- Do not parse `.pen` ZIP contents manually.
- Do not depend on local export scripts.
- Do not modify `pubspec.yaml`.
- `do not modify \`pubspec.yaml\`` is a strict workflow rule, not a suggestion.
- Do not default to full-page export.
- Do not auto-rename exported files.
- Do not translate absolute coordinates or raw node hierarchy into Flutter layout literally.
- Do not treat every visual node as a reusable widget; only extract components that improve reuse, clarity, or maintenance.
- Do not treat dark mode as light mode with reversed colors.
- Do not preserve decorative effects by default; first decide whether they carry brand, hierarchy, grouping, or state meaning.
- Do not return generic design commentary. Always land on Flutter-facing tokens, themes, components, screen architecture, and implementation boundaries.
- Do not generate page code in this skill. This skill ends at architecture and implementation guidance.
- Do not assume a manifest-like fallback path outside the active Pencil MCP tool flow.
- For every meaningful visual or structural decision, explicitly mark whether it should be faithfully restored, Flutterized, or simplified.

Notes:

- 这里的“检查 pubspec”是为了识别 Flutter assets 接入阻塞，不是为了替用户自动修工程文件。
- 如果导出文件名不理想，只在报告里给出业务命名建议，不直接改名，避免后续映射漂移。

## Deliverables

Every result should cover at least:

- `输入摘要`
- `Pencil MCP 取数范围`
- `布局快照观察`
- `图片资源导出结果`
- `图片资源映射表`
- `Flutter 资源接入结果`
- `全局设计结构`
- `设计 Token 归纳`
- `亮色主题方案`
- `暗色主题方案`
- `组件拆解清单`
- `页面实现骨架`
- `高保真 / Flutter 化取舍说明`
- `实现边界建议`
- `可供 flutter-init 消费的规范摘要`
- `风险与待确认项`

For important exported assets, prefer a structured row with:

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

## Output Contract

The final output must help another Flutter-focused agent continue without re-reading the design tree. That means:

- Group tokens into maintainable categories instead of dumping raw style values.
- Distinguish theme-level decisions from component-level decisions.
- Separate global shell patterns from page-specific structure.
- State clearly what should go into `ThemeData`, what belongs in `ThemeExtension`, and what should stay inside feature widgets.
- State which export nodes came from `export_nodes`, which observations came from `snapshot_layout`, and which structural claims came from `batch_get`.
- State how export nodes became exported assets, and how exported assets map into Flutter assets.
- Call out whether Flutter assets registration already appears to be in place, but leave the project files untouched.
- End with a `flutter-init` summary that can be turned into project guardrails or implementation constraints.

## References

- Read `references/pen-input-contract.md` to decide whether the available Pencil MCP data are sufficient and how to downgrade safely when they are not.
- Read `references/asset-extraction-and-mapping.md` to decide which export nodes should become exported assets through MCP, how exported assets map into Flutter assets, and how naming guidance should be documented without silent renames.
- Read `references/design-token-extraction.md` to normalize raw design styles into Flutter-ready tokens.
- Read `references/dual-theme-strategy.md` to derive light and dark themes with semantic consistency.
- Read `references/component-decomposition.md` to decide which parts deserve reusable widgets and which should stay local to a screen.
- Read `references/screen-architecture-planning.md` to map multi-screen designs into shells, flows, and state regions.
- Read `references/fidelity-vs-flutterization.md` to explain what should remain visually faithful and what should be adapted for Flutter design philosophy.
- Read `references/output-blueprint.md` to keep the final answer structure stable and `flutter-init`-friendly.
