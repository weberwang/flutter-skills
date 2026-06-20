---
name: flutter-uiux-to-architecture
description: Use when frozen Flutter UI/UX RD, implementation RD, Pencil design sources, restoration contracts, image-backed design guidance, theme artifacts, visual evidence, and structured module design-source packets must be translated into Flutter-facing tokens, assets, reusable components, screen architecture, and implementation boundaries.
---

# Flutter UIUX To Architecture

## Overview

Turn frozen UI/UX design-source artifacts into a Flutter-facing implementation architecture. This skill consumes the confirmed Pencil-backed module design-source packet, paired UI/UX RD, implementation RD, Pencil-to-Flutter restoration contract, global guidelines, theme freeze files, image-backed design constraints, and visual evidence.

It ends at architecture and implementation guidance. It does not write page code and does not reopen design decisions.

Module architecture in this workflow must assume that the frozen module design already considered the real target platform and that premium/high-fidelity quality is a non-negotiable implementation input, not an optional polish pass.

In the default workflow, this skill also decides whether a visual should be implemented natively in Flutter or produced as a project bitmap asset for later consumption, and it must output a page-level `display_restoration_blueprint` so downstream Flutter implementation does not re-interpret the frozen Pencil design source or any optional HTML supplement ad hoc.

It must not treat preview images as the only source of truth for concrete Flutter implementation choices. Preview images provide visual structure clues, but final Flutter decisions must combine preview evidence with `ui-ux.md`, `impl.md`, state semantics, and architecture constraints.

## Required Inputs

- Active module name and workflow state.
- Paired module `ui-ux.md` and `impl.md`.
- Frozen Pencil design file path.
- Confirmed Pencil-to-Flutter restoration contract.
- Confirmed module design-source packet or freeze card.
- Confirmed freeze decision from `flutter-design-freeze-gate`.
- Image-backed design packet or consolidated design packet from the approved screenshot and reference-image flow.
- `global-design-guidelines.md` when available.
- `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` when available.
- Verified `platform_identifier` for the target validation surface. Use explicit values such as `android_emulator`, `android_device`, `ios_simulator`, `ios_device`, `windows_desktop`, `macos_desktop`, `linux_desktop`, `web_browser`, or `custom`.
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
3. Verify the design-source packet references image-backed design constraints, visual evidence, frozen theme values, component freeze decisions, and state matrix.
4. Verify `platform_identifier` is explicit enough for downstream architecture and validation. Do not proceed into implementation-facing architecture with only a behavior baseline like `ios_hig` when the real target surface is Android emulator, Windows desktop, or Web browser.
4.1 Verify that the frozen module design packet already considered platform-specific behavior that materially affects implementation: safe areas, touch targets, hover/focus, back navigation, density, gesture discoverability, desktop or web pointer expectations, and motion posture.
5. Verify the display evidence pack is complete enough for fidelity-critical regions. If the page contains dense, branded, layered, scroll-reactive, or overlay-heavy areas and only a single broad preview exists, return a blocker instead of allowing image-only guessing.
5.1 If key states such as empty, error, permission, loading, disabled, success, locked, or premium materially change hierarchy, composition, or emotional tone, require state-specific visual evidence or an equally explicit frozen state-visual contract instead of inferring those states from the main preview alone.
6. Extract Flutter theme roles from the global guideline and theme files without recalculating their meaning.
7. Map typography, spacing, radius, color, elevation, icon posture, motion, and CTA emphasis into maintainable Flutter token categories.
8. Separate global tokens from module-scoped tokens. Global theme values remain authoritative; module tokens may only alias global roles, define component-local semantics, or introduce scoped values that the frozen module design-source packet explicitly allows.
9. Decompose UI into reusable layers: primitives, composite widgets, business widgets, page sections, shells, overlays, and state zones.
10. Plan screen architecture by flow: route entry, page scaffold, scroll regions, sticky regions, state ownership, loading/error/empty boundaries, and interaction feedback.
11. Decide asset handling from visual evidence: generated assets, static images, icons, illustrations, textures, or Flutter-native drawing.
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
14. Produce a page-level `display_restoration_blueprint` that turns the frozen Pencil-backed design source plus architecture output into an implementation contract. At minimum, map:
   - `region_id` to the intended Flutter widget/container structure
   - route scaffold, scroll container, list container, sticky container, and overlay host ownership
   - bottom spacing ownership, including whether it comes from `SafeArea`, frozen `bottom action area`, frozen `sticky footer`, approved scroll content inset, or `none`
   - each important state to its visible slot, replacement rule, and loading/error/empty presentation boundary
   - the visual-language strategy for each important state, including whether that state is led by imagery, illustration, placeholder structure, CTA framing, badge/icon language, or intentionally minimal copy
   - asset bindings, including which regions must use approved exported assets
   - interaction ownership, including which gestures, taps, sheets, tabs, or inline controls belong to which region
   - parity checkpoints for fidelity-critical regions so implementation and later review compare the same structure
15. Classify each visual decision as `preserve_faithfully`, `flutterize`, or `simplify`, and explain the implementation reason.
16. Add frozen design-quality implementation guardrails for presentation code: hierarchy, spacing rhythm, typography ladder, contrast, CTA salience, anti-template composition, and motion restraint.
16.1 Add premium implementation guardrails for presentation code: preserve the high-confidence, high-fidelity feel of the frozen design through disciplined spacing, typography precision, restrained depth, platform-appropriate interaction feedback, and refusal to flatten fidelity-critical regions for convenience.
17. Produce an architecture output pack that `flutter-init`, sibling `flutter-dev`, and `flutter-project-guardrails` can consume directly.

## Hard Rules

- Do not use subjective style guidance to override frozen UI/UX intent.
- Do not treat `platform_baseline` as proof of a verified target validation surface.
- Do not derive a desktop, browser, simulator, or device target from guesswork when `platform_identifier` is still missing.
- Do not downgrade a frozen premium design into a generic platform skin during architecture mapping. Platform adaptation must preserve the intended quality bar rather than dilute it.
- Do not proceed as if the display contract is high-fidelity when the evidence pack cannot actually support fidelity-critical regions.
- Do not invent theme values when `light-theme-freeze.yaml` or `dark-theme-freeze.yaml` exists; map them into Flutter instead.
- Do not let module-scoped tokens override global token names, global theme roles, or cross-module component semantics.
- Do not promote a module-scoped token into the global theme unless the workflow returns to shared design-source control and freezes that global change explicitly.
- Do not treat visual evidence as more authoritative than the confirmed design-source packet when they conflict.
- Do not silently fill missing detail with tasteful guesses when the visual region is fidelity-critical.
- Do not treat premium quality as decorative extras that can be deferred after architecture. If the premium or high-fidelity requirement is not implementable with current evidence, return a blocker.
- Do not treat a single main page preview as enough when key states still need independent visual language decisions.
- Do not decide scroll, list, sticky, overlay, or relative-layout behavior from preview images alone when the UI/UX or implementation docs define stronger semantics.
- Do not hand off display-layer implementation without a concrete `display_restoration_blueprint`; the frozen Pencil design source is a design source, not a self-executing Flutter page.
- Do not allow page-level manual bottom padding as a visual fix. Bottom spacing must come only from the frozen `display_restoration_blueprint`, such as `SafeArea`, frozen `bottom action area`, frozen `sticky footer`, or an explicitly approved scroll content inset.
- Do not default empty, error, permission, or other non-happy states to a small explanatory card plus long copy when the frozen design intent expects a stronger visual-language treatment.
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
- `display_restoration_blueprint`
- `non_native_visual_fallbacks`
- `design_implementation_guardrails`
- `fidelity_vs_flutterization`
- `implementation_boundaries`
- `flutter_init_inputs`
- `risks_and_open_questions`

## Pressure Scenarios

- User asks "where is the Pen file": explain that the updated default workflow requires a frozen Pencil design source and uses it as the primary design file.
- Visual preview and UI/UX RD disagree: block and route to `flutter-design-source-control`.
- Theme files are missing but required by the freeze packet: block and route to `design-preview-to-global-guidelines`.
- Developer wants to simplify a hero or CTA in code: classify whether the simplification is allowed; otherwise route to `flutter-design-source-control`.
- The UI looks polished but changes the primary task path: block; image-backed design guidance cannot override task guidance.
- The main preview exists but the empty or error state clearly needs a different composition: block and require state-specific visual evidence or a frozen state-visual contract instead of inventing a card-plus-copy fallback.
- The effect image contains a texture, illustration, layered composite, or branded bitmap treatment that Flutter should not rebuild natively: record it in `asset_strategy`, mark it under `non_native_visual_fallbacks`, and direct downstream implementation to use `$imagegen` plus project asset ingestion.
- The preview visually looks like a list or stacked layout, but `ui-ux.md` defines different interaction semantics: follow documented semantics, not image-only guesswork, or block if the sources truly conflict.
