# Bitmap Decomposition Standard

Use this standard after a page effect image is frozen and before Pencil high-fidelity restoration or asset-manifest work.

## Two Decisions, In Order

1. Determine content ownership: runtime data, runtime-rendered UI, or fixed production visual.
2. Only for a fixed production visual, decide whether it needs a bitmap asset.

Never infer asset eligibility from the fact that pixels are visible in the mockup. A screenshot may contain representative runtime content that must not become a bundled asset.

## Classification Rules

- **Data:** text, numbers, dates, chart values, progress values, user-generated content, avatars or photos supplied at runtime, remote map or media content, QR/barcode payloads, and any visual whose meaning changes with runtime data. Restore representative data without extracting or generating a production bitmap.
- **UI:** containers, controls, layout, masks, charts or QR/barcode renderers, deterministic shapes, and effects that Flutter can render. Split the renderer or visual treatment from its data payload.
- **Bitmap:** fixed production photography, illustration, logo artwork, texture, background decoration, custom icon artwork, or a UI fill that Flutter cannot reproduce exactly.

For a composite, split by ownership. Example: classify a chart's values as data, axes and plot renderer as UI, and a fixed paper texture behind it as bitmap.

## Data-Generated Bitmap Exclusion

Do not crop, generate, export, inventory, or bundle a bitmap merely because representative data appears rasterized in the effect image. This exclusion covers chart plots, progress visuals, avatars, user photos, maps, remote thumbnails, QR codes, barcodes, signatures, and other runtime-derived imagery. Record the data source, representative placeholder, renderer, loading state, and fallback instead.

If runtime content also has a fixed overlay, frame, watermark, mask texture, or decoration, split that fixed treatment into its own UI or bitmap unit. Do not merge it with the runtime content.

## Mandatory Visual Sweep

After the ownership pass, scan the frozen image a second time from back to front and top-left to bottom-right. Record every visible non-data treatment, including:

- full-page, sectional, edge, corner, clipped, and partially off-canvas backgrounds;
- patterns, grain, noise, glows, highlights, overlays, watermarks, masks, and fixed shadows;
- every navigation, action, status, badge, and decorative icon, including inactive and repeated instances;
- illustration fragments, logos, separators, custom bullets, and branded marks;
- visual treatments hidden behind cards or blended into similar colors.

Repeated uses of the same icon may share one asset identity, but every placement and state must appear in the coverage audit. Low opacity, clipping, or decorative purpose is never a reason to omit a unit.

## Coverage Gate

Create a coverage audit with region, layer order, visible element, content owner, runtime variability, classification, applicable asset identity, and evidence. Approval requires:

- zero visible elements without an owner;
- zero runtime-data visuals marked for bitmap export;
- every background decoration and icon accounted for;
- every bitmap candidate linked to exactly one production verdict;
- every repeated asset linked to all placements and states.

## Numbered Bitmap Overlay Confirmation Gate

After coverage passes and before any bitmap is generated, adapted, extracted, exported, transparentized, or sliced, create a confirmation copy of the exact frozen page image. Never draw on or replace the frozen source.

Annotate the confirmation copy as follows:

- Draw a tight, high-contrast rectangular outline around every proposed bitmap asset or bitmap fill.
- Place one stable numeric badge on or immediately outside each rectangle. Use `1`, `2`, `3`, and so on; show no asset names, descriptions, legends, arrows, dimensions, or other text on the image.
- Repeated placements of one shared asset use the same number on every placement. Distinct states or visually different outputs use different numbers.
- Box only fixed production bitmaps. Do not box runtime data, native Flutter UI, representative content, or whole containers merely because they contain a bitmap.
- Keep every visible candidate legible. When rectangles overlap, offset badges or use different high-contrast outline colors while keeping the numeric identity unambiguous.
- Preserve the frozen image dimensions and pixels outside the annotation layer.

Write the transient candidate overlay to `.codex-workflow/visuals/pages/<page-name>/bitmap-confirmation-v<version>.png`. Record its SHA-256 and the internal number-to-manifest mapping before presentation.

The Controller must present only the annotated image to the user. Do not output an inline table, asset list, legend, mapping, dimensions, production notes, or explanatory prose. A single short confirmation question is allowed. The user may confirm all numbered regions or identify numbers to exclude or revise.

After explicit confirmation, record the overlay version, path, SHA-256, confirmed numbers, user decision, and confirmation time in the page `asset-manifest.md`. Any later change to bitmap membership, numbered bounds, placement/state coverage, crop, source, background handling, dimensions, or production verdict invalidates the affected numbers and requires a newly rendered overlay version before work resumes.
