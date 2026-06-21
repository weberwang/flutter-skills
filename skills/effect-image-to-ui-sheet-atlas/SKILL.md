---
name: effect-image-to-ui-sheet-atlas
description: Use when a confirmed shared or module final effect image must be analyzed together with its prompt to identify non-Flutter-standard visuals, then generate one transparent, rectangular-cell, non-overlapping UI atlas plus manifest and slicing config before the workflow can enter atlas slicing or later Pencil restoration.
---

# Effect Image To UI Sheet Atlas

## Overview

Produce one workflow-ready bundle for a shared or module page:

- final effect image
- `UI-only` transparent atlas
- atlas manifest
- atlas slicing config

This skill is the atlas-preparation node. It owns the page-level visual bundle that must be reviewed before the workflow enters the dedicated slicing stage. It does not perform the actual slicing step, and it does not replace later Pencil design execution. The target atlas is a standard runtime-oriented resource atlas whose later slice outputs may be applied directly in the product app when the accepted slice contract says they are app-ready.

This atlas is not a raw crop-pack of the whole page. First analyze the confirmed effect image together with the original image-generation prompt and frozen visual constraints, identify the visuals that Flutter SDK standard capabilities cannot reproduce faithfully enough, and then generate one transparent atlas containing only those extracted visuals.

## When To Use

- A page has already passed the upstream direction or contract gate strongly enough to generate implementation-facing image evidence.
- The workflow now needs one reviewable bundle that includes the final effect image plus the `UI-only` atlas and cut config.
- The workflow needs one runtime-oriented atlas that groups the non-standard-library visual assets for that page into a clean rectangular-cell layout.
- The next step must be a separate slicing node rather than ad hoc cutting inside the same image-generation step.

Do not use this skill when:

- the page is still in broad visual direction exploration
- the page contract is not frozen enough to generate implementation-facing image evidence
- the workflow only needs code-native restoration and no atlas-backed runtime assets for that page

## Required Inputs

- target scope: `shared` or `module`
- target page name
- confirmed final effect image path
- original confirmed effect-image prompt or resolved prompt packet
- frozen visual constraints for that page
- frozen base design viewport width and height
- page state requirements
- output directory for the effect image
- output directory for the atlas bundle
- confirmation policy for the current execution mode

If any required input is missing, return `blocked`.

## Workflow

1. Confirm the page is allowed to generate implementation-facing image evidence.
2. Confirm the final effect image is already approved for the current scope. Do not generate atlas content before effect-image confirmation.
3. Analyze the approved effect image together with the original prompt and frozen visual constraints.
4. Classify page visuals into:
   - `flutter_native`
   - `atlas_required`
   - `placeholder_only`
5. For module scope, split `atlas_required` visuals into one small serial UI loop per page:
   - `page_base`
   - `overlay_ui`
6. Keep only `atlas_required` visuals in atlas scope. Do not pack visuals that Flutter SDK standard capabilities can already restore faithfully enough.
7. Inside that small loop, always process `page_base` first, then `overlay_ui` such as modal, dialog, bottom sheet, action sheet, or other overlay surfaces for the same page.
8. Rewrite those `atlas_required` visuals into one atlas-generation prompt for `gpt-image-2-generator` using the fixed atlas prompt template below.
9. Generate one transparent `UI-only` atlas image whose cells are rectangular, separable, and non-overlapping.
10. Validate whether the generated atlas background is truly transparent.
11. If the atlas background is not transparent, rerun `gpt-image-2-generator` through the same `/images/generations` path with prompt text exactly `移除背景`, and pass the current atlas image back through `image_urls` as a base64 data-URI array so the model removes only the background while preserving the existing cell layout and visual content.
12. Build an atlas manifest that records:
   - page name
   - scope
   - frozen viewport
   - slice ids
   - slice bounds
   - classification
   - surface group
   - runtime-data exclusions
   - source visual summary
   - whether the cell is runtime-ready
   - prerequisite surface group when one exists
13. Build a slicing config file that the downstream slicing skill can consume directly.
14. Run one automatic `@product-design` QA pass on the generated effect image before treating it as workflow-valid evidence.
15. Present the bundle for confirmation:
   - effect image
   - atlas image
   - atlas manifest
   - slicing config summary
16. Stop for confirmation in manual mode. Do not enter the slicing stage before this confirmation.

## Atlas Rules

- Keep only stable UI layers in the atlas.
- Exclude runtime-data regions from cut-safe slices.
- Keep the atlas output transparent. If a transparency-repair pass is needed, use prompt text exactly `移除背景`.
- Preserve the frozen design width.
- Do not require the atlas to preserve the original whole-page layout or coordinates. It is a resource atlas, not a page screenshot.
- Treat the atlas as a standard resource-atlas source for downstream app use rather than as review-only evidence.
- Record every excluded runtime-data region as `placeholder_only` or `data_excluded_placeholder`.
- Generate the atlas through one prompt to `gpt-image-2-generator`, not by mechanically cropping the whole page screenshot.
- Every exportable visual must live inside its own rectangular cell.
- Rectangular cell bounds must not overlap each other.
- Leave enough transparent spacing between neighboring cells so rectangle cutting cannot cut through another visual.
- Do not place one visual across multiple cells unless the manifest explicitly declares a multi-cell asset contract.

## Atlas Prompt Template

Always assemble the atlas-generation prompt with this fixed structure:

```text
Use case: Runtime UI asset atlas for product app
Primary request: Generate one transparent UI atlas containing only the non-Flutter-standard visuals required for <page_name>
Subject: <concise list of atlas_required visuals, one item per intended cell>
Style/medium: <inherit from confirmed effect image and frozen visual system>
Composition/framing: One atlas sheet, front-facing, rectangular cell layout, one exportable visual per cell
Lighting/mood: <inherit only when it materially affects asset fidelity>
Color palette: <inherit from frozen palette direction>
Materials/textures: <inherit only the textures that truly belong to atlas_required visuals>
Constraints:
- Transparent background
- UI-only visuals
- No whole-page screenshot composition
- One visual per rectangular cell
- Cells must not overlap
- Leave transparent padding between cells for safe rectangle cutting
- Keep runtime-data regions out of the atlas
- Keep only visuals that Flutter SDK standard capabilities cannot reproduce faithfully enough
Avoid:
- page mockup
- phone frame
- background scene
- decorative backdrop
- overlapping visuals
- cropped edges
- merged cells
- runtime text data
```

Template rules:

- Keep the `Use case` line fixed as runtime atlas generation.
- Keep the `Primary request` line explicit about transparent background and non-Flutter-standard visuals.
- The `Subject` line must enumerate the intended cell payloads, not describe the whole page.
- The `Constraints` block must always preserve the rectangular-cell and non-overlap rules verbatim.
- The `Avoid` block must always explicitly reject page mockups, device frames, overlapping visuals, and merged cells.
- If the request retries, preserve the same template and append only blocker-specific repair notes.
- Transparency repair is the only exception to the template retry rule: use prompt text exactly `移除背景`, pass the current atlas image through `image_urls` as a base64 data-URI array, and keep the existing atlas layout as the reference to preserve.

## Slicing Config Contract

The slicing config should be JSON and should contain:

```json
{
  "atlas_path": "docs/project/atlas/home/ui-sheet-atlas.png",
  "output_dir": "docs/project/atlas/home/slices",
  "page_name": "home",
  "scope": "shared",
  "layout_mode": "rectangular_cells",
  "cell_overlap": "forbidden",
  "slices": [
    {
      "id": "home-header-bg",
      "name": "header-bg",
      "x": 0,
      "y": 0,
      "width": 390,
      "height": 128,
      "classification": "bitmap_required",
      "surface_group": "page_base",
      "requires_surface_group": null,
      "export": true,
      "background_mode": "transparent",
      "source_visual_summary": "non-standard layered metallic banner treatment",
      "runtime_ready": true
    }
  ]
}
```

The downstream slicing node may enrich the result manifest, but it must not require a second config format.

## Output Contract

Return:

- `receipt_status`
- `scope`
- `page_name`
- `effect_image_path`
- `atlas_image_path`
- `atlas_manifest_path`
- `atlas_config_path`
- `qa_result`
- `confirmation_required`
- `blockers`

## Hard Rules

- Do not enter runtime bitmap export mode in this skill.
- Do not treat the atlas manifest as optional.
- Do not skip the slicing config.
- Do not bake runtime-data regions into cut-safe slices.
- Do not treat an accepted atlas bundle as review-only when its slice contract is already app-usable.
- Do not build the atlas by simply cropping the full page into arbitrary screenshot fragments.
- Do not include `flutter_native` visuals in atlas scope when Flutter SDK standard capabilities can already reproduce them faithfully enough.
- Do not allow rectangular slice bounds to overlap.
- Do not let overlay UI such as modal, dialog, or sheet enter processing order before the corresponding page-base visuals for that page are already settled.
- Do not invent an ad hoc atlas prompt shape. Use the fixed atlas prompt template and fill it with page-specific content.
- Do not confirm an atlas bundle whose background is still non-transparent before the required prompt-only fallback has retried `gpt-image-2-generator` with `移除背景` plus the current atlas image in `image_urls`.
- Do not enter the downstream slicing stage before the atlas bundle is confirmed in manual mode.
- Do not change the frozen page width.
- Do not use this skill as a shortcut around later Pencil design execution.
