---
name: flutter-uiux-to-architecture
description: Use when frozen Flutter UI/UX RD, implementation RD, taste direction, theme artifacts, visual evidence, and module design-source packets must be translated into Flutter-facing tokens, assets, reusable components, screen architecture, and implementation boundaries without requiring Pen or Pencil.
---

# Flutter UIUX To Architecture

## Overview

Turn frozen UI/UX design-source artifacts into a Flutter-facing implementation architecture. This skill replaces the default dependency on Pen/Pencil by consuming the confirmed module design-source packet, paired UI/UX RD, implementation RD, global guidelines, theme freeze files, taste constraints, and visual evidence.

It ends at architecture and implementation guidance. It does not write page code and does not reopen design decisions.

## Required Inputs

- Active module name and workflow state.
- Paired module `ui-ux.md` and `impl.md`.
- Confirmed module design-source packet or freeze card.
- Confirmed freeze decision from `flutter-design-freeze-gate`.
- Taste direction packet or consolidated design packet from `flutter-taste-router`.
- `global-design-guidelines.md` when available.
- `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` when available.
- Visual evidence: approved preview, screenshot pack, rendered mockups, or equivalent evidence.
- Global technical baseline and package stack.
- Target Flutter project root when assets or project-local paths must be mapped.

## Workflow

1. Confirm the active module is at least `module_design_frozen` or has a pending confirmed design-source freeze.
2. Verify the paired UI/UX and implementation RD are no longer `split_draft`.
3. Verify the design-source packet references taste constraints, visual evidence, frozen theme values, component freeze decisions, and state matrix.
4. Extract Flutter theme roles from the global guideline and theme files without recalculating their meaning.
5. Map typography, spacing, radius, color, elevation, icon posture, motion, and CTA emphasis into maintainable Flutter token categories.
6. Separate global tokens from module-scoped tokens. Global theme values remain authoritative; module tokens may only alias global roles, define component-local semantics, or introduce scoped values that the frozen module design-source packet explicitly allows.
7. Decompose UI into reusable layers: primitives, composite widgets, business widgets, page sections, shells, overlays, and state zones.
8. Plan screen architecture by flow: route entry, page scaffold, scroll regions, sticky regions, state ownership, loading/error/empty boundaries, and interaction feedback.
9. Decide asset handling from visual evidence: generated assets, static images, icons, illustrations, textures, or Flutter-native drawing.
10. Classify each visual decision as `preserve_faithfully`, `flutterize`, or `simplify`, and explain the implementation reason.
11. Add taste implementation guardrails for presentation code: hierarchy, spacing rhythm, typography ladder, contrast, CTA salience, anti-template composition, and motion restraint.
12. Produce an architecture output pack that `flutter-init`, project-local `flutter-dev`, and `flutter-project-guardrails` can consume directly.

## Hard Rules

- Do not require `.pen`, Pen, Pencil MCP data, or external design-tool nodes in the default workflow.
- Do not use taste guidance to override frozen UI/UX intent.
- Do not invent theme values when `light-theme-freeze.yaml` or `dark-theme-freeze.yaml` exists; map them into Flutter instead.
- Do not let module-scoped tokens override global token names, global theme roles, or cross-module component semantics.
- Do not promote a module-scoped token into the global theme unless the workflow returns to shared design-source control and freezes that global change explicitly.
- Do not treat visual evidence as more authoritative than the confirmed design-source packet when they conflict.
- Do not convert every repeated shape into a reusable widget; extract only components that improve reuse, clarity, state coverage, or maintenance.
- Do not flatten module-specific business widgets into generic shared components unless the UI/UX RD says they are reusable.
- Do not ignore non-happy states. Architecture must cover ideal, empty, loading, error, permission, partial data, disabled, success, locked, or premium states when relevant.
- Do not generate Flutter page code here. Stop at tokens, assets, component architecture, screen plan, and implementation boundaries.
- Do not change global package or architecture decisions inherited from `flutter-prd-rd-writer`; record conflicts as blockers.

## Deliverables

Return:

- `input_summary`
- `consumed_design_artifacts`
- `theme_token_mapping`
- `module_token_overlay`
- `asset_strategy`
- `component_decomposition`
- `screen_architecture`
- `state_architecture`
- `scroll_and_motion_architecture`
- `taste_implementation_guardrails`
- `fidelity_vs_flutterization`
- `implementation_boundaries`
- `flutter_init_inputs`
- `risks_and_open_questions`

## Pressure Scenarios

- User asks "where is the Pen file": explain that the default workflow consumes frozen UI/UX and visual evidence directly.
- Visual preview and UI/UX RD disagree: block and route to `flutter-design-source-control`.
- Theme files are missing but required by the freeze packet: block and route to `design-preview-to-global-guidelines`.
- Developer wants to simplify a hero or CTA in code: classify whether the simplification is allowed; otherwise route to `flutter-design-source-control`.
- The UI looks tasteful but changes the primary task path: block; taste cannot override task guidance.
