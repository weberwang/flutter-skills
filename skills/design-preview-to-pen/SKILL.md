---
name: design-preview-to-pen
description: Use when preview comps, approved visual directions, image assets, or Pencil `.pen` rebuilds need a gated designer workflow; when a user wants preview-first design exploration, explicit approval, asset planning, visual parity review, or structured Pencil handoff.
---

# Design Preview To Pen

## Overview

Run a strict designer production workflow: clarify the brief, explore preview directions, critique and freeze one approved direction, plan reusable assets, rebuild the design structurally in Pencil, complete non-page-level reusable component design, and verify visual parity. Bias toward maintainable Pencil structure, reusable assets, and commercially strong typography hierarchy, contrast, and CTA clarity rather than a one-off flattened mockup.

## Designer Role

Act like a production designer moving an approved art direction into an editable design file. Preserve intent, hierarchy, and system decisions while allowing small engineering cleanup that improves maintainability. Treat a completed design draft as both finished page compositions and finished non-page-level reusable component design.

## Quick Start

- If the user only wants visual exploration, stop after preview generation and do not enter Pencil.
- If the user already has an approved preview, skip discovery loops and start from the design freeze card plus asset plan, unless the latest `visual-design-reviewer` score is below `90`, still requires changes, or the current draft is only the single allowed post-review revision that still cannot be treated as a passed review.
- If the user wants direct Pencil editing without preview exploration, use a Pencil-focused skill instead of this one.
- If the user provides `global-design-guidelines.md`, `light-theme-freeze.yaml`, or `dark-theme-freeze.yaml`, treat them as frozen upstream design-source artifacts and preserve them during rebuild.
- If the user provides a `mobile-ui-design-coach` packet or design freeze card, treat it as the upstream source of truth.
- If no platform rule is specified, use HIG as the default mobile behavior baseline.
- Preview comps must be generated with `gpt-image-2` through `$gpt-image-2-generator`; if that skill, its required environment, or the active image-generation surface cannot use or confirm `gpt-image-2`, stop before preview generation and report the blocker.
- If the Pencil desktop app is not connected, complete the pre-Pencil phases and stop before any MCP read or write call.

## Workflow

1. Clarify the design brief and acceptance gates.
2. Lock the platform baseline, defaulting to HIG behavior rules unless the user explicitly chooses another baseline.
3. Lock the art direction inputs: layout posture, density, palette, material language, type personality, icon posture, illustration posture, and motion role.
4. If `design-preview-to-global-guidelines` artifacts exist, consume them as the global source contract before generating or rebuilding anything.
5. Generate preview candidates by delegating every image-generation call to `$gpt-image-2-generator`, using `gpt-image-2`, a controlled prompt set, and one major variable per round.
6. Critique the previews against the brief, not only visual taste.
7. Wait for explicit user approval and record the design freeze card.
8. Build an asset and system plan before touching Pencil.
9. Extract, regenerate, or redraw assets by type instead of blindly slicing everything.
10. Rebuild the approved direction in Pencil with variables first, reusable component design second, and sections third.
11. Complete non-page-level component design for repeated controls, cards, bars, list items, dialogs, chips, and other shared building blocks, including names, states, and variant boundaries.
12. When a page scrolls beyond the fixed viewport, decide whether the scroll structure is clear enough from one frame; if not, provide continuous frames or an equivalent structured scroll specification before claiming the design draft is complete.
13. Compare the Pencil result against the approved preview, freeze card, any frozen global guidance artifacts, the required component set, and the scroll-structure expression.
14. When the design draft is complete enough to judge visually, dispatch `visual-design-reviewer` in a fresh subagent unless the current draft is only the single allowed post-review revision from the latest failed module review.
15. If the review score is below `90` or the review still requires changes during module implementation preparation, update the active module `ui/ux` doc to reflect the revised design intent and modify the current module design draft in Pen exactly once. After that single revision pass, stop the current review cycle and do not run `visual-design-reviewer` again unless the user explicitly restarts a new design cycle.
16. Only drafts that already hold a freeze-ready `visual-design-reviewer` result with score `>= 90` may continue freeze-facing handoff. A post-failure single revision without a new user-directed cycle does not count as a reviewed pass.

## Phase Rules

### 1. Brief And Gates

- Read `references/brief-and-gates.md`.
- Lock the page type, audience, platform, commercial goal, art direction, state scope, illustration posture, icon posture, and fidelity target.
- Produce a concise brief pack before generating any preview.
- Ask for approval when the brief still contains multiple plausible directions.

### 2. Preview Generation

- Read `references/preview-generation.md`.
- Route every preview-generation request through `$gpt-image-2-generator`, and keep the prompt set stable across iterations.
- Treat the preview model as a production constraint: do not substitute another image model for convenience.
- Generate one to three directions at a time. Change one major variable per round: layout, palette, illustration language, or density.
- Treat preview comps as communication artifacts, not as final production assets.
- After each round, summarize the deltas, critique each option against the brief, recommend one, and ask the user to choose, merge, or revise.

### 3. Approval Freeze

- Do not continue on implied approval. Wait for an explicit user decision.
- If `global-design-guidelines.md` exists, link the freeze card to that contract and do not restate or mutate global theme role definitions locally.
- Convert the chosen direction into a design freeze card with immutable items, allowed engineering adjustments, icon and illustration handling, module-level component freeze decisions, state scope, and acceptance criteria.
- If the user wants a hybrid of multiple previews, freeze that hybrid explicitly before asset work.

### 4. Asset Extraction

- Read `references/asset-extraction.md`.
- Classify every visual element before extraction:
  - text and layout: rebuild in Pencil, never flatten into a slice
  - icons: prefer vector redraw or clean re-generation, not bitmap crop
  - illustration: generate or extract as isolated transparent assets when needed
  - texture and background: export as raster only when Pencil structure cannot express them cleanly
- Keep an asset manifest with final filenames, source, replacement strategy, and where each asset will be placed in Pencil.

### 5. Pencil Rebuild

- Read `references/pencil-rebuild.md`.
- Before any other Pencil operation, call `pencil.get_editor_state(include_schema: true)`.
- If the Pencil app is disconnected, state the blocker clearly and stop the workflow at the preparation boundary.
- Rebuild in this order:
  1. page or frame skeleton
  2. design variables
  3. structural sections
  4. text and controls
  5. illustrations and icons
  6. decorative details
- Prefer `set_variables` before large `batch_design` passes so spacing, color, and typography stay maintainable.
- Add redline notes or named variables for decisions Flutter must preserve.
- Do not treat page-level completion as design-draft completion until the non-page-level reusable components are also designed in Pencil.
- Complete reusable component design for shared UI building blocks, including at least naming, structural boundaries, reusable variables, and key state or variant differences when the approved direction implies them.
- Use a fixed viewport frame as the default page shell, and treat long content as scroll structure instead of unconstrained page-height drift.

### 6. Component Design Completion

- Identify which non-page-level building blocks are shared across screens or sections, instead of leaving them embedded only inside page frames.
- Extract or rebuild those building blocks as maintainable reusable component structures in Pencil.
- Cover the component states or variants that downstream Flutter work would otherwise have to guess, such as primary versus secondary emphasis, selected versus default, enabled versus disabled, filled versus outline, or inline versus elevated posture.
- Freeze the module-level component decisions explicitly: which components are reusable, which states and variants are frozen now, which parts are immutable, and which engineering adjustments remain allowed.
- Ensure the component set is consistent with frozen global guidance artifacts when those artifacts exist.
- If a repeated building block is intentionally kept local, document why it is not promoted into a reusable component.

### 7. Scroll Expression Completion

- Continuous frames are not mandatory by default, but the scroll structure must be explicit enough that Flutter restoration does not depend on guesswork.
- If a single fixed-viewport frame cannot clearly express below-the-fold ordering, fixed versus scrolling regions, sticky behavior, or key scroll transitions, provide continuous frames.
- If continuous frames are not used, provide an equivalent structured scroll specification that names at least:
  - viewport shell
  - scrolling content regions
  - fixed top or bottom regions
  - sticky or pinned regions
  - the order of below-the-fold sections
- Use continuous frames or equivalent structured scroll specification whenever the page includes long-form content, multiple folds, sticky regions, nested scrolling, tab-linked scrolling, or other behavior that Flutter would otherwise have to infer.

### 8. Visual Parity Review

- Read `references/acceptance-checklist.md`.
- Use `snapshot_layout` for structure checks and `get_screenshot` only after a meaningful section or full page is ready.
- Review parity against the approved preview, freeze card, any frozen global guidance artifacts, the completed reusable component set, and the chosen scroll expression, not against an older draft.
- Close gaps in a controlled order: layout first, typography second, color and materials third, asset fit last.

## Hard Rules

- Do not extract assets or write to Pencil before explicit user approval of a preview direction.
- Do not generate preview comps outside `$gpt-image-2-generator`, and do not use any model other than `gpt-image-2`; if `gpt-image-2` is unavailable or cannot be confirmed, stop and surface the blocker.
- Do not treat a flattened preview as the final production artifact.
- Do not proceed toward freeze or handoff with a freeze-facing review score below `90`.
- Do not send a post-failure single-revision draft back into `visual-design-reviewer` automatically within the same correction cycle.
- Do not respond to a module-stage design review failure by restarting module splitting.
- Do not crop bitmap icons from a preview when a redraw or vector-safe replacement is practical.
- Do not rebuild an entire page as one image unless the user explicitly accepts a non-editable result.
- Do not let a pretty preview override the approved brief, art direction, state scope, or freeze card.
- Do not recalculate global theme roles or localize palette semantics when frozen theme files already exist.
- Do not skip designer critique between preview generation and approval.
- Do not treat page frames alone as a completed design draft; non-page-level reusable component design must also be finished.
- Do not claim a complete design draft is handoff-ready until `visual-design-reviewer` has checked the visual result in a fresh subagent and returned a score of at least `90`.
- Do not leave shared controls or repeated building blocks only inside page compositions when downstream Flutter implementation needs explicit reusable component design.
- Do not treat module-level reusable components as frozen implicitly; record their frozen scope, states, and allowed adjustments in the freeze artifacts.
- Do not assume a long page is self-explanatory just because the frame is taller; if Flutter could misread the scroll structure, add continuous frames or an equivalent structured scroll specification.
- Do not require continuous frames for every page when a single fixed viewport plus explicit scroll specification already makes the Flutter mapping unambiguous.
- Do not break HIG-baseline safe areas, tap targets, navigation, destructive actions, permission flows, readability, feedback, or accessibility.
- Do not call Pencil tools other than `get_editor_state(include_schema: true)` before the schema is loaded.
- Do not hide the Pencil connection blocker; surface it immediately when the app is unavailable.
- Do not claim parity without comparing against the approved preview and frozen source artifacts.

## Deliverables

Every substantial result should leave these artifacts in the conversation:

- `request_summary`
- `design_brief`
- `platform_baseline`
- `preview_options_summary`
- `design_critique`
- `freeze_card`
- `module_component_freeze`
- `consumed_global_freeze_artifacts`
- `asset_manifest`
- `pencil_rebuild_progress`
- `component_design_progress`
- `scroll_expression`
- `visual_design_review`
- `parity_gap_list`

## References

- Read `references/brief-and-gates.md` for the discovery checklist, freeze contract, and handoff gates.
- Read `references/preview-generation.md` for prompt structure, iteration policy, and preview naming.
- Read `references/asset-extraction.md` for asset classification and extraction strategy.
- Read `references/pencil-rebuild.md` for the Pencil MCP sequence, rebuild order, and connection fallback.
- Read `references/acceptance-checklist.md` for parity review and final acceptance criteria.
