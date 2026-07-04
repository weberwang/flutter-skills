---
name: flutter-visual-enhancement-branch
description: Use when the first-pass Flutter implementation is already complete but review still proves that native restoration is insufficient, so the workflow must open the later visual-enhancement branch for atlas analysis, optional transparency removal, deterministic slicing, display evidence, Pencil reinforcement, and bitmap resource normalization.
---

# Flutter Visual Enhancement Branch

## Overview

This skill owns the later visual-enhancement branch.

`flutter-workflow` may decide when that branch is allowed to open and may persist the resulting stage updates, but it should not manage the branch-local sequencing itself anymore. Once the later refinement path is explicitly opened, route the active module to this skill and keep the branch logic here.

This skill exists for implementation-stage visual refinement only. It does not replace the first-pass module effect-image baseline, executable `impl.md`, native `HTML/CSS/JS` prototype, original mandatory Pencil design source, or the first-pass architecture and implementation path.

## Use When

- all target modules have already completed the first-pass functional implementation loop
- implementation review still shows fidelity-critical regions that Flutter-native restoration cannot reproduce faithfully enough
- the workflow explicitly reopens the later visual-enhancement branch for one active module
- the branch needs atlas analysis, atlas generation, optional atlas transparency removal, deterministic slicing, display-evidence confirmation, Pencil reinforcement, or supplemental bitmap normalization

Do not use this skill when:

- the workflow is still before the first-pass implementation loop
- the request is only for the module final effect image baseline
- the workflow still needs the original mandatory module Pencil design source rather than the later reinforcement pass
- the request is actually campaign / marketing / creative exploration that belongs to `Creative Production`

## Required Inputs

Before this skill runs, make sure the active module already has:

- confirmed module responsibility and primary-page scope
- approved module final effect image
- executable module `impl.md`
- accepted native `HTML/CSS/JS` module prototype
- accepted original mandatory Pencil design source
- completed first-pass implementation plus review evidence that justifies reopening visual refinement
- explicit page scope for the later refinement pass

When the branch includes atlas or bitmap work, also provide:

- source effect-image path
- source effect-image canvas size
- active module and page names
- target output directories
- current `docs/project/assets/global-asset-catalog.json`
- any already-approved atlas analysis, atlas manifest, slice manifest, or reusable asset paths when they already exist

If the branch cannot prove those prerequisites, return `blocked` instead of inventing missing context.

## Branch Ownership

This skill owns the page-by-page sequencing for:

1. atlas extraction analysis
2. solid-background atlas generation
3. optional `$imagegen` transparency removal
4. deterministic `ui-sheet-atlas-slicer` cutting
5. `display_evidence_pack_ready` confirmation
6. Pencil reinforcement through `effect-image-to-pencil-design`
7. asset reuse checks against `docs/project/assets/global-asset-catalog.json`
8. post-review bitmap list confirmation
9. standalone supplemental bitmap generation through `Product Design:ideate`
10. branch return into refreshed `pencil_restoration_ready`

`flutter-workflow` should only:

- decide whether this branch is allowed to open
- pass in the active module scope
- persist returned stage updates
- enforce cross-branch gates

## Managed Sequence

### 1. Atlas Analysis

- Route to `$effect-image-to-ui-sheet-atlas`.
- Confirm the approved effect image is still the visual source of truth.
- Keep atlas scope limited to non-standard-library visuals.
- Exclude runtime-data regions and keep them as `placeholder_only` or `data_excluded_placeholder`.
- In manual mode, stop for explicit confirmation before continuing.
- When confirmed, return `ui_sheet_atlas_analysis_ready`.

### 2. Solid Atlas Bundle

- Reuse the confirmed atlas analysis and cell plan exactly.
- Generate the solid-background atlas bundle through `Product Design:ideate`.
- Record the chosen preset background color, atlas manifest, and atlas slicing config.
- Keep atlas cells rectangular, non-overlapping, and faithful to the approved effect image.
- When confirmed, return `ui_sheet_atlas_ready`.

### 3. Optional Transparency Removal

- Decide whether the current runtime target actually requires transparency.
- If transparency is required and the atlas background is solid-color, route to `$imagegen`.
- If the atlas is already transparent, do not rerun background removal.
- If the atlas background is non-solid, block and regenerate the solid atlas first.
- When the transparent result is reviewed and confirmed, return `ui_sheet_atlas_transparent_ready`.

### 4. Deterministic Slicing

- Route to `$ui-sheet-atlas-slicer` with the confirmed atlas config.
- Use the transparent atlas when the previous step required transparency removal; otherwise slice from the confirmed solid atlas.
- Record the slice result manifest, exported count, skipped count, failed count, source effect-image canvas size, and per-cell source-region bounds.
- Do not accept any image-backed slice whose pixel size falls below its source-region size.
- When slicing succeeds, return `ui_sheet_atlas_slices_ready`.

### 5. Display Evidence Pack

- Confirm the current module has enough readable visual evidence for the later refinement pass.
- Include the main preview plus any required detail, scroll, state, or overlay evidence for the confirmed primary page.
- Do not expand into extra states unless explicit confirmation already added them to scope.
- When evidence is sufficient, return `display_evidence_pack_ready`.

### 6. Pencil Reinforcement

- Route to `effect-image-to-pencil-design` for one reinforcement pass on top of the original mandatory Pencil baseline.
- Keep the frozen design width unchanged.
- Do not let any Pencil page height fall below the frozen base design viewport height.
- Require compare -> visible-difference list -> focused repair -> human acceptance.
- Do not continue if the reinforced Pencil source lacks a compare report, repair receipt, or explicit human acceptance.

### 7. Supplemental Bitmap Normalization

- Work one module page at a time.
- Read `docs/project/assets/global-asset-catalog.json` before any new bitmap generation.
- Keep reuse decisions based on `name`, `semantic`, and `usage_scenarios`, not only filename similarity.
- Reuse approved assets directly when the semantic and usage scenario already match.
- Mark unresolved reuse as `candidate_reuse` and stop for confirmation.
- Present the remaining post-review bitmap list for explicit confirmation before generation.
- Prefer accepted atlas-slice outputs first.
- Generate only still-missing supplemental bitmap assets through `Product Design:ideate`.
- Complete manual image review on every new generated asset.
- Update the global asset catalog in the same branch step.
- When all required assets for the active page are approved and saved, continue to the next page.
- When the whole in-scope module page set is complete, return `module_asset_resources_ready`.

## Output Contract

Return:

- `routing_outcome`
- `active_module`
- `active_pages`
- `current_branch_step`
- `recommended_stage_update`
- `artifacts_written`
- `catalog_updates`
- `manual_review_status`
- `blockers`

Valid `routing_outcome` values:

- `advanced`
- `blocked`
- `not_executed`

## Hard Rules

- Do not open this branch before the first-pass module implementation loop has already completed.
- Do not let this branch redefine the approved module scope, executable `impl.md`, or confirmed native module prototype structure.
- Do not let this branch replace the original mandatory Pencil baseline; it may only reinforce it.
- Do not use `@product-design` as a replacement for atlas background-removal, atlas slicing, or deterministic runtime asset preparation.
- Do not generate the solid atlas through `gpt-image-2-generator`.
- Do not ask the image model to decide atlas scope, cell count, or background color.
- Do not add helper fills, helper borders, separator lines, crop guides, or decorative补画 to atlas cells.
- Do not bake runtime data layers into atlas cells or bitmap assets.
- Do not call `Product Design:ideate` for supplemental bitmap assets before checking the global asset catalog.
- Do not generate supplemental bitmap assets before the page-level bitmap list is explicitly confirmed.
- Do not return `pencil_restoration_ready` until the reinforced Pencil result and all required branch-local bitmap artifacts are already confirmed.
