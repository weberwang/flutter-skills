---
name: flutter-pen-to-architecture
description: Use when translating Pencil `.pen` design files or Pencil MCP design data into Flutter architecture plans, especially when assets, `pubspec.yaml`, tokens, themes, reusable components, screen structure, or fidelity-versus-Flutterization decisions are needed before implementation.
---

# Flutter Pen To Architecture

## Overview

Turn `Pencil` design sources into a Flutter-facing implementation architecture instead of a node-by-node rebuild. Default to whole-project analysis: extract global tokens, derive light and dark themes, decompose reusable components, plan multi-screen page structure, and explain where high fidelity should yield to Flutter-native structure.

## Quick Start

- If the user provides `.pen` files or Pencil MCP output, start with global analysis instead of single-screen local optimization.
- If the input only covers one screen, still try to infer reusable tokens, shared shells, and component families before discussing that screen in isolation.
- If the user only wants visual direction refinement or Pencil prompt tuning, use `mobile-ui-design-coach` first instead of this skill.
- If `global-design-guidelines.md`, `light-theme-freeze.yaml`, or `dark-theme-freeze.yaml` exist, consume them as frozen design-source inputs before re-deriving global design rules from `.pen`.
- If variables, layout hierarchy, or component-instance relationships are missing, output `assumptions` and `needs_confirmation` before giving conclusions.
- If the user asks for direct Flutter code, finish this architecture pass first or hand off the final summary to the downstream implementation skill.
- If the task includes a Flutter project, prefer Pencil MCP `export_nodes` for image assets before discussing how those assets should enter the restoration plan.

## Workflow

1. Identify the real input surface: `.pen` file path, MCP node tree, variables, layout, reusable instances, any frozen global-guideline artifacts, missing structural data, and whether a Flutter project root is available.
2. Access `.pen` data only through Pencil MCP; call `get_editor_state(include_schema: true)` before Pencil reads if the schema is not already loaded.
3. Resolve image assets first: identify the nodes that should become image assets, and avoid exporting ordinary layout nodes by default.
4. Before exporting, read or list the target `assets/images/` directory so overwrite behavior can be recorded.
5. Use Pencil MCP `export_nodes` to export selected node IDs into the Flutter project's `assets/images/`, then map returned absolute paths to Flutter paths like `assets/images/<file>`.
6. Read `pubspec.yaml`; if `assets/images/` is missing, update it with a targeted file patch and re-read the file to verify the registration.
7. Scan the whole design system first: page families, navigation shells, information hierarchy, repeated motifs, and semantic surfaces.
8. Extract design tokens for color, typography, spacing, radius, elevation, and status semantics.
9. Preserve any frozen global theme role names and values, then build the Flutter mapping strategy for light and dark instead of treating dark mode as a color inversion.
10. Decompose the UI into reusable layers: primitives, composite widgets, business widgets, and page sections.
11. Plan screen architecture across the whole flow: shells, content regions, state zones, overlays, scroll regions, sticky regions, and transitions between screens.
12. Classify key decisions into `preserve_faithfully`, `flutterize`, or `simplify`, and explain why.
13. Produce an output pack that a Flutter team and `flutter-init` can consume directly, including asset export and mapping results.

## Hard Rules

- Do not translate absolute coordinates or raw node hierarchy into Flutter layout literally.
- Do not treat every visual node as a reusable widget; only extract components that improve reuse, clarity, or maintenance.
- Do not treat dark mode as light mode with reversed colors.
- Do not preserve decorative effects by default; first decide whether they carry brand, hierarchy, grouping, or state meaning.
- Do not return generic design commentary. Always land on Flutter-facing tokens, themes, components, screen architecture, and implementation boundaries.
- Do not generate page code in this skill. This skill ends at architecture and implementation guidance.
- Do not rename, reinterpret, or recalculate frozen theme roles from `design-preview-to-global-guidelines`; only map them into Flutter theme layers.
- Do not read, unzip, or parse `.pen` files directly. Use Pencil MCP tools for `.pen` access and asset export.
- Do not depend on local export scripts for image export.
- Do not assume a tall design frame is enough to describe scrolling behavior; derive explicit Flutter scroll architecture from continuous frames or structured scroll notes when present.
- For every meaningful visual or structural decision, explicitly mark whether it should be faithfully restored, Flutterized, or simplified.

## Deliverables

Every result should cover at least:

- `input_summary`
- `consumed_frozen_design_artifacts`
- `asset_export_results`
- `asset_mapping`
- `flutter_asset_registration`
- `global_design_structure`
- `design_token_summary`
- `light_theme_strategy`
- `dark_theme_strategy`
- `component_decomposition`
- `screen_architecture`
- `scroll_architecture`
- `fidelity_vs_flutterization`
- `implementation_boundaries`
- `flutter_init_summary`
- `risks_and_open_questions`

For important components or sections, prefer a structured row with:

- `design_intent`
- `flutter_mapping`
- `fidelity_level`
- `theme_layer_usage`
- `reusable_component_decision`
- `risks_or_notes`

## Output Contract

The final output must help another Flutter-focused agent continue without re-reading the design tree. That means:

- Group tokens into maintainable categories instead of dumping raw style values.
- Distinguish theme-level decisions from component-level decisions.
- Distinguish values frozen upstream from values inferred locally from `.pen`.
- Separate global shell patterns from page-specific structure.
- State clearly what should go into `ThemeData`, what belongs in `ThemeExtension`, and what should stay inside feature widgets.
- End with a `flutter-init` summary that can be turned into project guardrails or implementation constraints.

## References

- Read `references/pen-input-contract.md` to decide whether the available `.pen` and MCP data are sufficient and how to downgrade safely when they are not.
- Read `references/asset-extraction-and-mapping.md` to decide which image resources should be exported, how they map into `assets/images/`, and how overwrite or verification behavior should be described.
- Read `references/design-token-extraction.md` to normalize raw design styles into Flutter-ready tokens.
- Read `references/dual-theme-strategy.md` to derive light and dark themes with semantic consistency.
- Read `references/component-decomposition.md` to decide which parts deserve reusable widgets and which should stay local to a screen.
- Read `references/screen-architecture-planning.md` to map multi-screen designs into shells, flows, and state regions.
- Read `references/fidelity-vs-flutterization.md` to explain what should remain visually faithful and what should be adapted for Flutter design philosophy.
- Read `references/output-blueprint.md` to keep the final answer structure stable and `flutter-init`-friendly.
