---
name: flutter-uiux-to-architecture
description: Use when frozen Flutter UI/UX RD, implementation RD, taste direction, theme artifacts, visual evidence, and module design-source packets must be translated into Flutter-facing tokens, assets, reusable components, screen architecture, and implementation boundaries without requiring Pen or Pencil.
---

# Flutter UIUX To Architecture

## Overview

Turn frozen UI/UX design-source artifacts into a Flutter-facing implementation architecture. This skill replaces the default dependency on Pen/Pencil by consuming the confirmed module design-source packet, paired UI/UX RD, implementation RD, global guidelines, theme freeze files, taste constraints, and visual evidence.

It ends at architecture and implementation guidance. It does not write page code and does not reopen design decisions.

In the default workflow, this skill also decides whether a visual should be implemented natively in Flutter or produced as a project bitmap asset for later consumption.

It must not treat preview images as the only source of truth for concrete Flutter implementation choices. Preview images provide visual structure clues, but final Flutter decisions must combine preview evidence with `ui-ux.md`, `impl.md`, state semantics, and architecture constraints.

## Required Inputs

- Active module name and workflow state.
- Paired module `ui-ux.md` and `impl.md`.
- Confirmed module design-source packet or freeze card.
- Confirmed freeze decision from `flutter-design-freeze-gate`.
- Taste direction packet or consolidated design packet from `flutter-taste-router`.
- `global-design-guidelines.md` when available.
- `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` when available.
- Visual evidence: approved preview, screenshot pack, rendered mockups, or equivalent evidence.
- A display evidence pack for fidelity-critical regions whenever the module is visually sensitive. At minimum this should include:
  - one readable main preview for the full page or primary surface
  - detail previews for complex, dense, or branded regions
  - key state previews for loading, empty, error, disabled, success, or premium states when relevant
  - scroll-position evidence for long pages when hierarchy changes across the page
  - overlay, sticky, sheet, or modal evidence when those layers materially affect structure
- Global technical baseline and package stack.
- Target Flutter project root when assets or project-local paths must be mapped.

## High-Fidelity Display Contract

When the target module depends on static visual evidence for commercial quality or branded fidelity, produce a high-fidelity display contract instead of a loose reconstruction note.

The contract must identify:

- fidelity-critical regions such as hero areas, primary CTA clusters, branded illustration zones, layered surfaces, textured backgrounds, sticky headers, and depth-heavy cards
- the exact evidence source used for each critical region
- which regions must be `preserve_faithfully`, which may `flutterize`, and which may `simplify`
- which details are locked by design intent and must not be smoothed away during implementation
- which details are implementation-sensitive and therefore need asset fallback, layout anchoring, or extra review

## Workflow

1. Confirm the active module is at least `module_design_frozen` or has a pending confirmed design-source freeze.
2. Verify the paired UI/UX and implementation RD are no longer `split_draft`.
3. Verify the design-source packet references taste constraints, visual evidence, frozen theme values, component freeze decisions, and state matrix.
4. Verify the display evidence pack is complete enough for fidelity-critical regions. If the page contains dense, branded, layered, scroll-reactive, or overlay-heavy areas and only a single broad preview exists, return a blocker instead of allowing image-only guessing.
5. Extract Flutter theme roles from the global guideline and theme files without recalculating their meaning.
6. Map typography, spacing, radius, color, elevation, icon posture, motion, and CTA emphasis into maintainable Flutter token categories.
7. Separate global tokens from module-scoped tokens. Global theme values remain authoritative; module tokens may only alias global roles, define component-local semantics, or introduce scoped values that the frozen module design-source packet explicitly allows.
8. Decompose UI into reusable layers: primitives, composite widgets, business widgets, page sections, shells, overlays, and state zones.
9. Plan screen architecture by flow: route entry, page scaffold, scroll regions, sticky regions, state ownership, loading/error/empty boundaries, and interaction feedback.
10. Decide asset handling from visual evidence: generated assets, static images, icons, illustrations, textures, or Flutter-native drawing.
11. Classify each visually important element into one of these buckets:
   - `native_flutter`: should be reproduced directly with Flutter layout, paint, gradients, clipping, blur, animation, or composition.
   - `project_bitmap_asset`: should be generated as a bitmap asset and consumed by the app because native reconstruction would be brittle, too expensive, or visibly lower fidelity.
   - `existing_asset_reuse`: should reuse an already approved image or project asset instead of creating a new one.
12. If a visual belongs to `project_bitmap_asset`, specify the asset goal, expected file role, placement path, and why `$imagegen` is the correct fallback instead of forcing native code.
13. Produce a concrete display-layer implementation decision table for every important page region. At minimum, decide:
   - `region_id`
   - `visual_priority`: `fidelity_critical`, `high`, `normal`, or `supporting`
   - `scroll_decision`: `CustomScrollView`, `SingleChildScrollView`, `ListView`, `NestedScrollView`, fixed layout, or mixed
   - `list_decision`: `ListView.builder`, `SliverList`, `Column`, `GridView`, `SliverGrid`, `Wrap`, or not-a-list
   - `layout_decision`: `Column/Row`, `Stack`, `Overlay`, `CustomMultiChildLayout`, sliver composition, or mixed
   - `sticky_decision`: `SliverAppBar`, pinned sliver header, fixed footer, no sticky behavior, or mixed
   - `layout_anchor`: what neighboring edge, baseline, or region relationship must remain stable
   - `spacing_lock_rule`: which spacing relationships are visually locked and must not be normalized away
   - `text_overflow_rule`: wrap, clip, fade, ellipsis, scale, or redesign-blocked
   - `responsive_break_rule`: which layout changes are allowed across widths and which are not
   - `z_axis_rule`: layer ordering, blur, scrim, overlap, and depth behavior
   - `animation_source_of_truth`: frozen motion intent, preview evidence only, or explicit no-motion
   - `pixel_tolerance`: strict, tight, moderate, or flexible
   - `asset_decision`: native drawing/composition, existing asset reuse, or `$imagegen` fallback
   - `must_use_asset`: exact asset path or `none`
   - `must_not_flutterize`: `yes` or `no`
14. Classify each visual decision as `preserve_faithfully`, `flutterize`, or `simplify`, and explain the implementation reason.
15. Add taste implementation guardrails for presentation code: hierarchy, spacing rhythm, typography ladder, contrast, CTA salience, anti-template composition, and motion restraint.
16. Produce an architecture output pack that `flutter-init`, project-local `flutter-dev`, and `flutter-project-guardrails` can consume directly.

## Hard Rules

- Do not require `.pen`, Pen, Pencil MCP data, or external design-tool nodes in the default workflow.
- Do not use taste guidance to override frozen UI/UX intent.
- Do not proceed as if the display contract is high-fidelity when the evidence pack cannot actually support fidelity-critical regions.
- Do not invent theme values when `light-theme-freeze.yaml` or `dark-theme-freeze.yaml` exists; map them into Flutter instead.
- Do not let module-scoped tokens override global token names, global theme roles, or cross-module component semantics.
- Do not promote a module-scoped token into the global theme unless the workflow returns to shared design-source control and freezes that global change explicitly.
- Do not treat visual evidence as more authoritative than the confirmed design-source packet when they conflict.
- Do not silently fill missing detail with tasteful guesses when the visual region is fidelity-critical.
- Do not decide scroll, list, sticky, overlay, or relative-layout behavior from preview images alone when the UI/UX or implementation docs define stronger semantics.
- Do not force every design effect into native Flutter code when a bitmap asset is the more faithful and maintainable choice.
- Do not choose `$imagegen` for simple visuals that Flutter can reproduce cleanly with native code.
- Do not classify a fidelity-critical branded region as `simplify` unless design-source control explicitly approved that reduction.
- Do not convert every repeated shape into a reusable widget; extract only components that improve reuse, clarity, state coverage, or maintenance.
- Do not flatten module-specific business widgets into generic shared components unless the UI/UX RD says they are reusable.
- Do not ignore non-happy states. Architecture must cover ideal, empty, loading, error, permission, partial data, disabled, success, locked, or premium states when relevant.
- Do not generate Flutter page code here. Stop at tokens, assets, component architecture, screen plan, and implementation boundaries.
- Do not change global package or architecture decisions inherited from `flutter-prd-rd-writer`; record conflicts as blockers.

## Deliverables

Return:

- `input_summary`
- `consumed_design_artifacts`
- `display_evidence_pack`
- `high_fidelity_display_contract`
- `theme_token_mapping`
- `module_token_overlay`
- `asset_strategy`
- `component_decomposition`
- `screen_architecture`
- `state_architecture`
- `scroll_and_motion_architecture`
- `display_layer_decision_table`
- `non_native_visual_fallbacks`
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
- The effect image contains a texture, illustration, layered composite, or branded bitmap treatment that Flutter should not rebuild natively: record it in `asset_strategy`, mark it under `non_native_visual_fallbacks`, and direct downstream implementation to use `$imagegen` plus project asset ingestion.
- The preview visually looks like a list or stacked layout, but `ui-ux.md` defines different interaction semantics: follow documented semantics, not image-only guesswork, or block if the sources truly conflict.
