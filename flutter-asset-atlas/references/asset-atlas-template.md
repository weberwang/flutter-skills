# Asset Atlas Template

Use this after page-level high-fidelity mockup approval and design freeze. The approved mockup must be the frozen image persisted under `.codex-workflow/visuals/pages/<page-name>/`.

## Context

- Page or module:
- Approved frozen mockup:
- Mockup candidate ID / SHA-256 / confirmation time:
- Global design freeze:
- Page design freeze:
- Wireframe spec:
- Page decomposition and separate-bitmap review:
- Flutter target asset root:
- Decision: Required / N/A
- Decision reason:

## Reuse Check

| Asset need | Existing candidate | Source path | Reuse verdict | Reason |
|---|---|---|---|---|

## Separate Bitmap Review Trace

Carry forward every bitmap unit from `pencil-hifi-restoration.md`; `N/A: native Flutter/UI/data` means no asset-atlas entry is required for that unit.

| Unit | Mockup evidence | 100%-match evidence | Separate asset verdict | Asset ID or N/A reason | Review status |
|---|---|---|---|---|---|

## Decomposition Coverage Intake

- Unowned visible elements: `0` / list
- Runtime-data visuals marked for export: `0` / list
- Missing background decorations: `0` / list
- Missing icon placements or states: `0` / list

| Runtime-derived visual excluded from assets | Data source | Flutter renderer | Representative placeholder | Loading and fallback | Fixed treatment split into UI/bitmap |
|---|---|---|---|---|---|

## Production Decision

Use this order before generating new images: reuse existing, adapt existing, generate variant from existing source, generate a new single asset with the available image-generation capability, generate atlas/contact sheet, export from an approved Pencil asset node, extract from an approved mockup with explicit approval.

| Asset ID | Decision | Source tool or origin | Why new or changed | Global freeze constraints | Page freeze constraints | Background handling |
|---|---|---|---|---|---|---|

## Pre-Slicing User Confirmation

Present this complete table inline before generating, adapting, extracting, exporting, transparentizing, or slicing any bitmap.

- Confirmation table version:
- User decision: Pending / Confirmed / Revision requested
- Confirmed by:
- Confirmation time:

| Asset ID | Visible role | Placements and states | Production verdict | Proposed source | Crop and clipped-content rule | Background / transparency / mask / shadow / glow | Logical size | Required output size | Risk | Proposed action |
|---|---|---|---|---|---|---|---|---|---|---|

Any material row change invalidates confirmation for that row. Present the revised table and wait for explicit reconfirmation.

## Bitmap Source Policy

| Asset ID | Default source | Image-generation evidence | Pencil export allowed | Pencil export reason | Mockup extraction approval |
|---|---|---|---|---|---|

## Background Handling

| Asset ID | Required background | Transparency needed | Removal or masking method | Edge risk | Reason |
|---|---|---|---|---|---|

## Background Transparentization Work Node

| Asset ID | Required | Method | Source file | Working output | Removed background | Mask or threshold | Preserved effects | Reject or continue |
|---|---|---|---|---|---|---|---|---|

## Transparent Background Post-Processing

| Asset ID | Required | Matte color removed | Alpha cleanup method | Edge decontamination | Shadow/glow handling | Target backgrounds tested |
|---|---|---|---|---|---|---|

## Asset Groups

| Group | Assets | Purpose | Source | Export strategy | Required |
|---|---|---|---|---|---|

## Generation Or Source Plan

| Asset ID | Source type | Source path or prompt | Tool or origin | Logical display size | Required 2x pixel size | Verified pixel size | Background prompt constraint | Reference image | Selected output | Rejected outputs | License status | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

For generated assets, keep source traceability outside the model prompt. Build the actual prompt with [image-prompt-principles.md](../../flutter-hifi-mockup/references/image-prompt-principles.md) and record its compact final form below.

| Asset ID | Outcome and role | Essential frozen traits | Edge/background non-negotiables | Creative freedom left open | Output requirement | Material avoid items | Final compact prompt |
|---|---|---|---|---|---|---|---|

## Flutter Mapping

| Asset ID | Flutter path | Used by screen/state | Widget or component | Light mode | Dark mode |
|---|---|---|---|---|---|

## Open Decisions

- 

## Gate

- All required visual assets have a source or generation plan.
- Every decomposed visual resource has a 100%-match evidence record and a separate-asset review verdict. An unmatched icon, image, illustration, logo, texture, or bitmap must use `generate` and complete dedicated bitmap generation.
- The coverage intake has zero unowned visible elements, zero runtime-data export candidates, zero missing background decorations, and zero missing icon placements or states.
- Runtime-derived visuals are excluded from asset generation and record their renderer, placeholder, loading state, and fallback; any fixed surrounding treatment is split independently.
- The complete pre-slicing table was shown inline and explicitly confirmed; its version, decision, and confirmation time are recorded.
- Every produced, extracted, exported, transparentized, or sliced asset matches a currently confirmed row.
- New generation references global and page design-freeze constraints.
- New bitmap generation uses the available image-generation capability by default; Pencil export is allowed only for approved production asset nodes.
- Every newly generated concrete bitmap records its logical display size and passes the exact `2x` decoded-dimension check; only full-screen bitmaps use `780 x 1688 px`.
- Every generated or exported asset has a background handling decision before generation.
- Assets that require transparency but arrive with a non-transparent background have a completed Background Transparentization Work Node.
- Transparent or masked assets have post-processing and target-background QA recorded.
- Every new generated asset has a reuse check and a reason existing assets were insufficient.
- Assets that are not required are marked replaceable or removed from implementation scope.
- Unknown license status blocks implementation.
