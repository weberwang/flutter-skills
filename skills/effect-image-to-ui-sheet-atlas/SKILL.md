---
name: effect-image-to-ui-sheet-atlas
description: Use when a frozen shared or module page must produce one confirmed final effect image together with a UI-only atlas image, atlas manifest, and atlas slicing config before the workflow can enter an atlas slicing stage or later Pencil restoration.
---

# Effect Image To UI Sheet Atlas

## Overview

Produce one workflow-ready bundle for a shared or module page:

- final effect image
- `UI-only` transparent atlas
- atlas manifest
- atlas slicing config

This skill is the atlas-preparation node. It owns the page-level visual bundle that must be reviewed before the workflow enters the dedicated slicing stage. It does not perform the actual slicing step, and it does not replace later Pencil design execution.

## When To Use

- A page has already passed the upstream direction or contract gate strongly enough to generate implementation-facing image evidence.
- The workflow now needs one reviewable bundle that includes the final effect image plus the `UI-only` atlas and cut config.
- The next step must be a separate slicing node rather than ad hoc cutting inside the same image-generation step.

Do not use this skill when:

- the page is still in broad visual direction exploration
- the page contract is not frozen enough to generate implementation-facing image evidence
- the workflow only needs final runtime bitmap assets instead of a UI-only atlas bundle

## Required Inputs

- target scope: `shared` or `module`
- target page name
- frozen visual constraints for that page
- frozen base design viewport width and height
- page state requirements
- output directory for the effect image
- output directory for the atlas bundle
- confirmation policy for the current execution mode

If any required input is missing, return `blocked`.

## Workflow

1. Confirm the page is allowed to generate implementation-facing image evidence.
2. Generate or refresh the page effect image through the approved image-generation path.
3. Generate the matching `UI-only` atlas image from the same frozen page target.
4. Build an atlas manifest that records:
   - page name
   - scope
   - frozen viewport
   - slice ids
   - slice bounds
   - classification
   - runtime-data exclusions
5. Build a slicing config file that the downstream slicing skill can consume directly.
6. Run one automatic `@product-design` QA pass on the generated effect image before treating it as workflow-valid evidence.
7. Present the bundle for confirmation:
   - effect image
   - atlas image
   - atlas manifest
   - slicing config summary
8. Stop for confirmation in manual mode. Do not enter the slicing stage before this confirmation.

## Atlas Rules

- Keep only stable UI layers in the atlas.
- Exclude runtime-data regions from cut-safe slices.
- Use transparent background.
- Preserve the frozen design width.
- Keep the atlas aligned to the same page geometry as the effect image.
- Record every excluded runtime-data region as `placeholder_only` or `data_excluded_placeholder`.

## Slicing Config Contract

The slicing config should be JSON and should contain:

```json
{
  "atlas_path": "docs/project/atlas/home/ui-sheet-atlas.png",
  "output_dir": "docs/project/atlas/home/slices",
  "page_name": "home",
  "scope": "shared",
  "slices": [
    {
      "id": "home-header-bg",
      "name": "header-bg",
      "x": 0,
      "y": 0,
      "width": 390,
      "height": 128,
      "classification": "bitmap_required",
      "export": true,
      "background_mode": "transparent"
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
- Do not enter the downstream slicing stage before the atlas bundle is confirmed in manual mode.
- Do not change the frozen page width.
- Do not use this skill as a shortcut around later Pencil design execution.

