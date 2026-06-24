---
name: effect-image-to-ui-sheet-atlas
description: Use when a confirmed shared or module final effect image must be analyzed together with its prompt to identify non-Flutter-standard visuals, then generate one solid-background, rectangular-cell, non-overlapping UI atlas plus manifest and slicing config before the workflow can enter background removal, atlas slicing, or later Pencil restoration.
---

# Effect Image To UI Sheet Atlas

## Overview

Produce one workflow-ready bundle for a shared or module page:

- final effect image
- approved atlas extraction analysis
- approved solid-background UI-only atlas
- chosen background-key color record
- atlas manifest
- atlas slicing config

This skill is the visual-asset preparation node. It owns the page-level atlas bundle that must be reviewed before later Pencil or implementation work continues. After the atlas extraction analysis is confirmed, it may use `Product Design:ideate` to render the approved solid-background atlas image. It does not perform the actual slicing step, it does not remove atlas backgrounds itself, and it does not replace later Pencil design execution.

This atlas bundle is not a raw crop-pack of the whole page. First analyze the confirmed effect image together with the original image-generation prompt and frozen visual constraints, identify the visuals that Flutter SDK standard capabilities cannot reproduce faithfully enough, explicitly exclude dynamic-data-driven regions, choose one least-conflicting flat background color from the preset atlas background palette, and only after that confirmed analysis generate one solid-background UI atlas whose cells are rectangular and non-overlapping.

## When To Use

- A page has already passed the upstream direction or contract gate strongly enough to generate implementation-facing image evidence.
- The workflow now needs one reviewable bundle that includes the final effect image plus the approved atlas extraction analysis, solid-background atlas image, chosen background-key color, atlas manifest, and atlas slicing config for that page.
- The workflow needs one solid-background atlas for the non-standard-library regions of that page.
- The next step will consume the confirmed solid atlas in background removal, slicing, Pencil, or later implementation work.

Do not use this skill when:

- the page is still in broad visual direction exploration
- the page contract is not frozen enough to generate implementation-facing image evidence
- the workflow only needs code-native restoration and no generated runtime atlas for that page

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
3. Analyze the approved effect image together with the original prompt and frozen visual constraints before composing any atlas-generation prompt.
4. Classify page visuals into:
   - `flutter_native`
   - `atlas_required`
   - `placeholder_only`
5. Produce a written atlas extraction analysis that lists every UI-layer visual that must enter the atlas, with source region, target use, surface group, target cell bounds, restore bounds, match priority, and exclusion reason for visuals that stay out of the atlas.
6. For module scope, split `atlas_required` visuals into one small serial UI loop per page:
   - `page_base`
   - `overlay_ui`
7. Keep only `atlas_required` visuals in atlas scope. Do not pack visuals that Flutter SDK standard capabilities can already restore faithfully enough, and do not pack any region whose real content must be generated later from runtime data.
8. Inside that small loop, always process `page_base` first, then `overlay_ui` such as modal, dialog, bottom sheet, action sheet, or other overlay surfaces for the same page.
9. In manual mode, stop for explicit analysis confirmation before atlas generation. Do not generate the atlas before the confirmed extraction list exists.
10. Choose one flat background-key color from the preset atlas background palette before atlas generation. The chosen color must minimize conflict with the approved atlas visuals and must be recorded explicitly for downstream removal.
11. Rewrite the confirmed atlas extraction analysis into one atlas-generation prompt. That prompt must consume the precomputed cell list exactly as approved; it must not ask the image model to decide atlas scope, cell count, layout, or background color.
12. Generate one solid-background rectangular-cell UI atlas through `Product Design:ideate`.
13. Validate the generated atlas for cell completeness, silhouette fidelity, edge integrity, rectangular-cell boundaries, non-overlap, and flat single-color background consistency.
14. Build an atlas manifest and slicing config that record:
   - page name
   - scope
   - frozen viewport
   - background-key color
   - cell ids
   - atlas cell bounds
   - restore bounds in the design source
   - classification
   - surface group
   - runtime-data exclusions
   - source visual summary
   - prerequisite surface group when one exists
   - atlas path
15. Complete manual image review on the generated atlas image and record the human review result before treating the atlas bundle as workflow-valid evidence.
16. Present the bundle for confirmation:
   - effect image
   - atlas extraction analysis
   - atlas image
   - chosen background-key color
   - atlas manifest
   - atlas slicing config
17. Stop for confirmation in manual mode. Do not enter background removal or slicing before this confirmation.

## Asset Rules

- Keep only stable UI layers in the approved atlas scope.
- Exclude runtime-data regions and dynamic-data-generated visuals from atlas cells.
- Keep the atlas background flat and single-color in this step.
- Choose the atlas background color from the preset atlas background palette and prefer the least-conflicting option for the approved visuals.
- Preserve the frozen design width.
- The atlas config must preserve every approved cell's restore bounds and slice bounds.
- Record every excluded runtime-data region as `placeholder_only` or `data_excluded_placeholder`.
- Generate the atlas through `Product Design:ideate`, not by mechanically cropping the whole page screenshot.
- Every exportable visual must live inside one rectangular atlas cell.
- Do not place one visual across multiple cells unless the manifest explicitly declares a multi-cell contract.
- Do not let two exportable visuals overlap inside rectangular slicing bounds.
- Do not add an extra local background panel, backing plate, or fill behind a cell visual unless that background is part of the approved source visual itself.
- Do not add visible cell borders, keylines, divider strokes, or framing boxes unless the approved source visual itself contains that edge treatment.
- Do not remove the background inside this skill. Background removal belongs to the downstream `$imagegen` confirmation step.

## Atlas Prompt Template

Always assemble the atlas-generation prompt with this fixed structure:

```text
Use case: UI-only atlas generation
Primary request: Generate one solid-background UI atlas for <page_name> using only the confirmed atlas analysis input below
Atlas analysis input: <confirmed atlas analysis result>; all atlas scope, cell content, cell order, cell bounds, and fidelity requirements must come from this input only
Atlas purpose: <short visual purpose for this page atlas>
Background key color: <one chosen color from the preset atlas background palette>
Atlas cell plan:
- <cell_id> | group=<analysis-defined group> | visual=<single exportable UI-layer visual from the analysis result> | source_region=<source location described by the analysis result> | target_cell=<exact rectangular bounds or intended aspect ratio> | restore_bounds=<target placement bounds for design restoration> | padding=<minimum transparent padding> | match_priority=<shape|texture|shadow|edge|color>
Style/medium: <from confirmed analysis result>
Composition/framing: One solid-background atlas sheet only, centered content, no surrounding page layout
Lighting/mood: <from confirmed analysis result only when it affects atlas fidelity>
Color palette: <from confirmed analysis result>
Materials/textures: <from confirmed analysis result>
Constraints:
- Flat single-color background only
- UI-only atlas
- No whole-page screenshot composition
- Rectangular cells only
- No overlap between cells
- Keep each visual fully inside its own cell, including glow, blur, shadow, stroke, and texture edges
- Keep each cell visually consistent with the matching effect-image region, including source proportions, visual weight, texture density, border radius, shadow softness, and edge treatment
- Normalize each extracted UI-layer visual into a clean atlas cell without redesigning, simplifying, restyling, or inventing replacement artwork
- Keep each cell payload visually isolated on the sheet background only; do not invent a per-cell backdrop, card base, or extra background color block unless it belongs to the approved source visual
- Do not draw visible cell frames, keylines, separator strokes, or debug-style boxes around cell payloads unless those lines are part of the approved source visual
- Do not add visible labels, rulers, outlines, crop marks, or annotations
- Do not analyze, add, remove, merge, or reinterpret atlas scope inside this prompt; follow the confirmed atlas analysis exactly
- Do not infer or replace the provided background key color
- Do not use any external planning, delivery, or build-context wording to decide what to generate
Avoid:
- page mockup
- phone frame
- background scene
- decorative backdrop
- cropped edges
- crossed cells
- merged visuals
- repeated duplicates unless the confirmed analysis explicitly requests variants
- dynamic text or data content that is not listed as an exportable visual cell
```

Template rules:

- Keep the `Use case` line fixed as atlas generation.
- Keep the `Primary request` line explicit that the image model must generate one solid-background atlas sheet from the confirmed atlas analysis input.
- The `Atlas analysis input` line replaces all external guidance. All generated content must be grounded in that confirmed analysis result.
- The `Atlas purpose` line must describe the page atlas purpose only.
- The `Background key color` line must use the chosen preset color exactly and must not be omitted.
- The `Atlas cell plan` must enumerate every intended UI-layer cell payload with stable `cell_id`, `group`, `visual`, `source_region`, `target_cell`, `restore_bounds`, `padding`, and `match_priority` fields.
- The generated atlas visuals should stay as close as possible to the visual descriptions from the confirmed analysis result; do not let atlas generation reinterpret them as a new illustration set.
- The atlas prompt must not contain open-ended instructions such as "extract all UI layers" or "decide which visuals belong in the atlas"; those decisions belong to the prior atlas extraction analysis.
- The atlas prompt must not contain build-context wording as generation criteria.
- The `Composition/framing` and `Constraints` blocks must always preserve solid-background rectangular non-overlapping cell output.
- The `Avoid` block must always explicitly reject page mockups, device frames, visible labels, merged visuals, and crossed cells.
- If the atlas request retries, preserve the same template and append only blocker-specific repair notes.
- Background removal does not happen in this skill. After the solid atlas is confirmed, route to `$imagegen` for background transparency removal and confirm that result before slicing.

## Atlas Config Contract

The atlas config should be JSON and should contain:

```json
{
  "atlas_path": "docs/project/atlas/home/ui-sheet-atlas.png",
  "output_dir": "docs/project/atlas/home/slices",
  "page_name": "home",
  "scope": "shared",
  "background_key_color": "#8c3fec",
  "layout_mode": "rectangular_cells",
  "slice_mode": "minimum_cell_bounds",
  "cell_overlap": "forbidden",
  "slices": [
    {
      "id": "home-header-bg",
      "name": "header-bg",
      "x": 0,
      "y": 0,
      "width": 390,
      "height": 128,
      "restore_x": 0,
      "restore_y": 0,
      "restore_width": 390,
      "restore_height": 128,
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
- `atlas_analysis_path`
- `atlas_analysis_confirmed`
- `atlas_image_path`
- `background_key_color`
- `atlas_manifest_path`
- `atlas_config_path`
- `qa_result`
- `confirmation_required`
- `blockers`

## Hard Rules

- Do not enter runtime bitmap export mode in this skill.
- Do not skip atlas extraction analysis before atlas generation.
- Do not treat the atlas manifest or atlas config as optional.
- Do not bake runtime-data regions into cut-safe slices.
- Do not build the atlas by simply cropping the full page into arbitrary screenshot fragments.
- Do not include `flutter_native` visuals in atlas scope when Flutter SDK standard capabilities can already reproduce them faithfully enough.
- Do not include dynamic-data-generated visuals in atlas scope.
- Do not let overlay UI such as modal, dialog, or sheet enter processing order before the corresponding page-base visuals for that page are already settled.
- Do not invent an ad hoc atlas prompt shape. Use the fixed atlas prompt template and fill it with page-specific content.
- Do not generate the workflow atlas through `gpt-image-2-generator`.
- Do not generate the workflow atlas directly on a transparent background in this skill.
- Do not choose an ad hoc background color outside the preset atlas background palette.
- Do not continue into slicing before the downstream `$imagegen` background-removal result is confirmed.
- Atlas generation may use `Product Design:ideate` only after the atlas extraction analysis is explicitly confirmed.
- Do not ask the image model to decide atlas scope, cell count, or cell layout on its own.
- Do not place multiple exportable visuals into overlapping rectangular cells.
- Do not use `$imagegen` to infer slice bounds. Minimum-cell slicing must remain deterministic and config-driven.
- Do not change the frozen page width.
- Do not use this skill as a shortcut around later Pencil design execution.
- Do not decorate atlas cells with invented local backgrounds or visible framing lines that are not present in the approved source visual.
