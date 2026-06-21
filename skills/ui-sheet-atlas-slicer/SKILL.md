---
name: ui-sheet-atlas-slicer
description: Use when a confirmed UI-only atlas bundle already exists and the workflow now needs one generic, config-driven slicing step that reads the atlas config, cuts the atlas into files, and emits a slice result manifest before later Pencil or implementation work continues.
---

# UI Sheet Atlas Slicer

## Overview

Slice a confirmed `UI-only` atlas through one generic script.

This skill does not generate effect images, atlas images, or atlas configs. It consumes an already-confirmed atlas bundle, runs the bundled slicer script, and outputs:

- one file per exported slice
- one slice result manifest
- one summary of skipped or failed slices

## When To Use

- A previous node already produced:
  - effect image
  - `UI-only` atlas
  - atlas manifest
  - atlas slicing config
- The atlas bundle is already explicit enough to cut without guessing.
- The workflow wants a deterministic slicing stage before Pencil design or other downstream restoration work.

Do not use this skill when:

- the atlas config does not exist yet
- the atlas bundle is still pending confirmation
- the workflow wants final runtime asset generation instead of atlas cutting

## Required Inputs

- atlas image path
- atlas config path
- output directory
- whether overwrite is allowed

If any required input is missing, return `blocked`.

## Workflow

1. Confirm that the atlas bundle is already accepted for the active scope.
2. Review the atlas config for:
   - path validity
   - output directory
   - slice ids
   - slice bounds
   - export flags
3. Run the generic slicer script:

```bash
rtk python skills/ui-sheet-atlas-slicer/scripts/slice_atlas.py --config <config-path>
```

4. Read the slice result manifest.
5. Report:
   - exported slice count
   - skipped slice count
   - failed slice count
   - output paths
6. Return control to the orchestrator for the next node.

## Output Contract

Return:

- `receipt_status`
- `atlas_config_path`
- `slice_output_dir`
- `slice_manifest_path`
- `exported_slice_count`
- `skipped_slice_count`
- `failed_slice_count`
- `blockers`

## Hard Rules

- Do not invent slice bounds during execution. Use only the provided config.
- Do not enter bitmap-regeneration mode in this skill.
- Do not merge multiple slices into one file.
- Do not silently skip failed slices without recording them in the result manifest.
- Do not overwrite existing outputs unless the caller explicitly allows it.

