---
name: design-preview-to-pen
description: Use when preview comps, approved visual directions, image assets, or Pencil `.pen` rebuilds need a gated designer workflow; when a user wants preview-first design exploration, explicit approval, asset planning, visual parity review, or structured Pencil handoff.
---

# Design Preview To Pen

## Overview

Run a strict designer production workflow: clarify the brief, explore preview directions, critique and freeze one approved direction, plan reusable assets, rebuild the design structurally in Pencil, and verify visual parity. Bias toward maintainable Pencil structure and reusable assets, not a one-off flattened mockup.

## Designer Role

Act like a production designer moving an approved art direction into an editable design file. Preserve intent, hierarchy, and system decisions while allowing small engineering cleanup that improves maintainability.

## Quick Start

- If the user only wants visual exploration, stop after preview generation and do not enter Pencil.
- If the user already has an approved preview, skip discovery loops and start from the design freeze card plus asset plan.
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
10. Rebuild the approved direction in Pencil with variables first and sections second.
11. Compare the Pencil result against the approved preview, freeze card, and any frozen global guidance artifacts, then close remaining gaps.

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
- Convert the chosen direction into a design freeze card with immutable items, allowed engineering adjustments, icon and illustration handling, state scope, and acceptance criteria.
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

### 6. Visual Parity Review

- Read `references/acceptance-checklist.md`.
- Use `snapshot_layout` for structure checks and `get_screenshot` only after a meaningful section or full page is ready.
- Review parity against the approved preview, freeze card, and any frozen global guidance artifacts, not against an older draft.
- Close gaps in a controlled order: layout first, typography second, color and materials third, asset fit last.

## Hard Rules

- Do not extract assets or write to Pencil before explicit user approval of a preview direction.
- Do not generate preview comps outside `$gpt-image-2-generator`, and do not use any model other than `gpt-image-2`; if `gpt-image-2` is unavailable or cannot be confirmed, stop and surface the blocker.
- Do not treat a flattened preview as the final production artifact.
- Do not crop bitmap icons from a preview when a redraw or vector-safe replacement is practical.
- Do not rebuild an entire page as one image unless the user explicitly accepts a non-editable result.
- Do not let a pretty preview override the approved brief, art direction, state scope, or freeze card.
- Do not recalculate global theme roles or localize palette semantics when frozen theme files already exist.
- Do not skip designer critique between preview generation and approval.
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
- `consumed_global_freeze_artifacts`
- `asset_manifest`
- `pencil_rebuild_progress`
- `parity_gap_list`

## References

- Read `references/brief-and-gates.md` for the discovery checklist, freeze contract, and handoff gates.
- Read `references/preview-generation.md` for prompt structure, iteration policy, and preview naming.
- Read `references/asset-extraction.md` for asset classification and extraction strategy.
- Read `references/pencil-rebuild.md` for the Pencil MCP sequence, rebuild order, and connection fallback.
- Read `references/acceptance-checklist.md` for parity review and final acceptance criteria.
