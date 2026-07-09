# Asset Atlas Template

Use this after page-level high-fidelity mockup approval and design freeze.

## Context

- Page or module:
- Approved mockup:
- Global design freeze:
- Page design freeze:
- Wireframe spec:
- Flutter target asset root:
- Decision: Required / N/A
- Decision reason:

## Reuse Check

| Asset need | Existing candidate | Source path | Reuse verdict | Reason |
|---|---|---|---|---|

## Production Decision

Use this order before generating new images: reuse existing, adapt existing, generate variant from existing source, generate new single asset with product-design or image generation tools, generate atlas/contact sheet, export from an approved Pencil asset node, extract from approved mockup with explicit approval.

| Asset ID | Decision | Source tool or origin | Why new or changed | Global freeze constraints | Page freeze constraints | Background handling |
|---|---|---|---|---|---|---|

## Bitmap Source Policy

| Asset ID | Default source | Product-design or imagegen evidence | Pencil export allowed | Pencil export reason | Mockup extraction approval |
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

| Asset ID | Source type | Source path or prompt | Tool or origin | Background prompt constraint | Reference image | Selected output | Rejected outputs | License status | Owner |
|---|---|---|---|---|---|---|---|---|---|

## Flutter Mapping

| Asset ID | Flutter path | Used by screen/state | Widget or component | Light mode | Dark mode |
|---|---|---|---|---|---|

## Open Decisions

- 

## Gate

- All required visual assets have a source or generation plan.
- New generation references global and page design-freeze constraints.
- New bitmap generation uses product-design or image generation tools by default; Pencil export is allowed only for approved production asset nodes.
- Every generated or exported asset has a background handling decision before generation.
- Assets that require transparency but arrive with a non-transparent background have a completed Background Transparentization Work Node.
- Transparent or masked assets have post-processing and target-background QA recorded.
- Every new generated asset has a reuse check and a reason existing assets were insufficient.
- Assets that are not required are marked replaceable or removed from implementation scope.
- Unknown license status blocks implementation.
