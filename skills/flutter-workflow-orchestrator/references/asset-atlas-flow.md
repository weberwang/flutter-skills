# Asset Resource Flow

Use this reference after mandatory shared or module Pencil design review is accepted, whenever the approved visual evidence still includes one page whose confirmed post-review regions cannot be restored faithfully enough in code and therefore need bitmap assets that stay very close to the effect image.

## Goal

Turn one approved page into a reusable runtime asset set that downstream prototypes and Flutter implementation can consume directly, whether that final set comes from accepted atlas slices, supplemental standalone bitmaps, or a controlled mix of both.

This flow sits after effect-image confirmation plus Pencil review acceptance, and before prototype generation. It is not a design-direction workflow. It is a resource-normalization workflow.

Each qualifying page should already have a matching `UI-only transparent sheet atlas` generated during the effect-image step. That atlas is a standard runtime-oriented resource atlas source. When its accepted slice outputs already satisfy the page's runtime contract, they may replace separate per-resource regeneration.

Mechanical background processing must be skipped when atlas input is already transparent. Rule-based background removal is allowed only for solid-color backgrounds; non-solid backgrounds must not be processed to transparent. Model-based transparency repair by sending the atlas image back through `gpt-image-2-generator` edit fallback remains allowed when the workflow explicitly requires that fallback.

## Entry Conditions

Enter this flow when one or more of these are true:

- a shared shell or module page includes a visual region whose final look cannot be restored faithfully enough with code
- empty, error, loading, or other status imagery must stay very close to the approved effect image instead of being redrawn from generic code primitives
- the approved design would lose important fidelity if the region were rebuilt only from standard components, vectors, gradients, or library icons

If the prototype can be built faithfully enough from standard vectors, shapes, gradients, tokens, and library icons, skip this flow.

Do not enter this flow for image regions that are only schematic placeholders and whose real content will be created later from runtime data. Those regions should stay as placeholders in the prototype contract.

## Required Inputs

Before resource generation begins, make sure these inputs are explicit:

- approved source effect image or approved source screenshots for the current page
- matching atlas image for the same page
- matching atlas manifest for the same page
- resource scope: `shared` or `module`
- current page name
- target output directory for that page
- the current `docs/project/assets/global-asset-catalog.json`
- whether any candidate asset is already known to be reusable

If the catalog is missing, repair or initialize it from `global-asset-catalog-contract.md` before classifying reuse.

## Internal Flow

1. Read the current global asset catalog first.
2. Work on one page at a time. Identify every visual region in the current page that truly needs bitmap fidelity.
3. Verify that the page already has a matching `UI-only transparent sheet atlas` plus a cut-ready manifest from the effect-image step. The atlas must keep only stable UI regions, use transparent background, and exclude runtime-data regions.
4. Before any background cleanup step, classify the current atlas or slice input as `transparent`, `solid_color`, or `non_solid`. If it is already transparent, stop background processing. Only solid-color backgrounds may be processed to transparent by rule-based cleanup. If the atlas still needs transparent output and the workflow requires the model fallback, the atlas image may be sent back through `gpt-image-2-generator` edit mode instead.
5. If the page belongs to a module, compare the current page effect image against the active module `impl.md` and the page's required state set first. If `error`, `empty`, `loading`, permission, or other page-local states are required but not yet represented strongly enough for resource or prototype work, supplement those missing states before finalizing the page checklist.
6. Remove `placeholder_only` regions first. If a region is only a visual stand-in for runtime-created data content, record it as a placeholder contract and keep it out of image generation. Atlas-only helper labels such as `data_excluded_placeholder` are allowed, but they must still stay out of bitmap generation.
5. For every remaining visual region, first decide whether Flutter SDK standard capabilities alone can restore it faithfully enough without adding new bitmap assets.
6. Classify the current page into three written groups before generation:
   - `bitmap_required`
   - `flutter_native`
   - `placeholder_only`
7. Only the regions inside `bitmap_required` may continue into image generation. Regions inside `flutter_native` must stay as Flutter-native implementation targets. Regions inside `placeholder_only` must stay as runtime placeholders.
8. Before any new generation request is allowed, check the current global asset catalog plus the approved output paths it references. If an approved image already exists for the same `name`, `semantic`, and `usage_scenarios`, reuse that file directly and remove the region from new generation scope.
9. Classify each remaining `bitmap_required` asset by `name`, `semantic`, and `usage_scenarios`:
   - `reusable`
   - `candidate_reuse`
   - `shared_only`
   - `module_only`
10. If any asset is `candidate_reuse`, stop and request confirmation.
11. Present the written current-page checklist plus the remaining new bitmap list for the current page and stop for explicit confirmation before generation.
12. First prefer accepted atlas-slice outputs when they already satisfy the page's runtime contract. Only the still-missing assets should continue into standalone generation.
13. Generate each approved supplemental bitmap asset independently through `$imagegen`. Do not regenerate slices that are already accepted as runtime-ready atlas outputs.
14. Save each final runtime asset as its own final file, whether it came from atlas slicing or from supplemental standalone generation. Decide whether the output should be transparent or background-baked from the frozen design intent: use transparency when the asset must float over runtime surfaces, and keep a baked background only when that background is part of the intended asset.
15. Update the global asset catalog with:
   - record type
   - asset owner
   - reuse status
   - final output path
   - generation stage
   - any confirmed cross-module reuse
16. Allow prototype work only after the approved asset files already exist and are confirmed.

This same catalog is also the workflow's generated-image record table. Shared or module bitmap assets generated in this flow must be written into it immediately, and any already-approved representative sketches or effect images that this page depends on should already be present there before generation continues.

## Flutter-Native Standard

Treat a region as `flutter_native` only when Flutter SDK standard capabilities can restore it faithfully enough without adding new bitmap assets.

Typical Flutter-native candidates:

- standard buttons and button shells
- standard icons
- regular cards and labels
- normal rounded rectangles
- simple borders, shadows, gradients, and fills
- ordinary text presentation

Do not mark a region `flutter_native` if those same capabilities would still lose the approved paper texture, watercolor texture, sticker feel, torn edge, complex illustration fidelity, or other critical visual character.

## Shared Scope Rules

Shared page resource work is for:

- shared shell imagery
- shared state imagery
- shared badges, logos, or decorative resources
- shared bitmap assets reused by multiple modules

Suggested paths:

- `docs/project/assets/global-asset-catalog.json`
- `docs/project/assets/shared/<page-name>/`

## Module Scope Rules

Module page resource work is for:

- bitmap assets unique to one module
- module-specific state illustrations
- module-specific imagery that cannot reuse a shared asset
- page-local states that the module `impl.md` requires even when the first approved effect image did not yet show them clearly enough

Suggested paths:

- `docs/project/modules/<module>/assets/<page-name>/`

## Resource Rules

- Every generated asset must decide its background mode from the frozen design intent instead of assuming transparency blindly.
- Do not bake the page background into an asset unless the frozen design explicitly treats that background as part of the resource.
- If an atlas or slice input is already transparent, do not run background processing again.
- Only solid-color backgrounds may be processed to transparent by automatic or rule-based cleanup. Gradient, textured, photographic, or other non-solid backgrounds must stay out of automatic background removal, but they may still use the explicit `gpt-image-2-generator` edit fallback when the workflow requires model-based transparency repair.
- Do not mix unrelated visual regions into one generated asset without an explicit reason.
- Do not create duplicate bitmap assets when a reusable asset already exists.
- Do not auto-merge semantically similar assets when the reuse decision is still ambiguous.
- Do not include `placeholder_only` regions whose real content will be drawn or assembled later from runtime data.
- Do not include runtime-data regions inside cut-safe atlas slices. Those runtime-data regions must remain placeholders or `data_excluded_placeholder` markers in the atlas workflow.
- Do not turn a region into a bitmap asset when code can already restore it faithfully enough.

## Prototype Rules

- Shared prototypes must directly reference shared generated asset files.
- Module prototypes must directly reference shared generated asset files or module generated asset files.
- Do not continue prototype work with screenshot crops once this flow is required.
- `placeholder_only` regions are allowed to remain placeholders in the prototype, but they must not be treated as generated assets.

## Output Contract

Produce for the current page:

- one written decision checklist containing `bitmap_required`, `flutter_native`, and `placeholder_only`
- one verified `UI-only transparent sheet atlas` plus cut-ready manifest
- updated `docs/project/assets/global-asset-catalog.json`
- one confirmed set of generated asset files for that page

## Routing Outcome

Use one of these outcomes:

- `advanced`: the current page's bitmap list was confirmed, and its generated asset files all exist and are confirmed
- `blocked`: reuse confirmation, asset confirmation, or required asset files are missing
- `not_executed`: the resource generation did not actually run

## Hard Rules

- Do not finalize shared freeze when shared resource generation is required but incomplete.
- Do not finalize `pencil_restoration_ready` or module implementation-side restoration when module resource generation is required but incomplete.
- Do not bypass the global asset catalog.
- Do not treat the page as resource-ready when the matching `UI-only transparent sheet atlas` or its cut-ready manifest is missing.
- Do not call `$imagegen` for a bitmap asset before checking whether the catalog already points to an approved reusable image for the same semantic and usage scenario.
- Do not approve a generated asset with the wrong background mode for its intended usage. Transparent assets should stay transparent, and background-baked assets should be used only when the frozen design explicitly requires that background.
- Do not run background removal on already transparent atlas inputs.
- Do not process non-solid backgrounds to transparent.
- Do not generate assets before the current page's bitmap list is explicitly confirmed.
- Do not batch multiple distinct supplemental standalone assets into one generated image file.
- Do not assume the first module effect image already covers every required page-local state. Repair missing state coverage before freezing the page bitmap checklist.
