---
name: flutter-asset-atlas
description: Use when a Flutter page or module has approved high-fidelity mockups with illustrations, bitmaps, generated images, logos, textures, backgrounds, visual atlases, slicing/export needs, asset inventories, or visual asset fidelity checks before Pencil restoration or Flutter UI implementation.
---

# Flutter Asset Atlas

## Overview

Use this skill after a page-level high-fidelity mockup is approved and before high-fidelity Pencil restoration or Flutter UI implementation when the page contains required visual assets. It prevents duplicate image generation, enforces global and page design-freeze constraints, and turns approved visual assets into Flutter-ready files with source, path, license, fallback, and fidelity evidence.

## Required Inputs

- Approved page-level high-fidelity mockup.
- Global design freeze, for example `docs/design/global-design-freeze.md` or the project-approved global design-freeze path.
- Page design freeze, for example `docs/design/design-freeze.md` or a page-scoped design-freeze path.
- `docs/design/wireframe-spec.md` for the page.
- Product and module context.
- Existing brand assets, licensed source files, generated images, or screenshots when present.
- Existing `docs/design/asset-inventory.md` and prior page/module asset inventories when present.
- Target Flutter asset conventions and `pubspec.yaml` location.

## Workflow

1. Confirm global design-freeze constraints and page design-freeze constraints exist before asset generation or extraction.
2. Audit the approved mockup for required visual assets: illustrations, bitmaps, photos, logos, textures, backgrounds, generated images, chart bitmaps, and custom icons.
3. Mark the asset track as Required or `N/A: no bitmap or exported visual assets`. Do not skip required assets because they look decorative if they affect brand, trust, conversion, or visual parity.
4. Run a reuse check against brand assets, existing app assets, previous generated assets, source files, and `docs/design/asset-inventory.md`.
5. Choose the production decision for each asset in this order: reuse existing asset, adapt existing asset, generate variant from existing source, generate new single asset with product-design or image generation tools, generate atlas/contact sheet, export from an approved Pencil asset node, or extract from approved mockup with explicit approval.
6. Decide background handling before generation or export: transparent background, retained full background, masked cutout, or non-transparent safe background for later removal. Record why.
7. Fill [references/asset-atlas-template.md](references/asset-atlas-template.md) with reuse decisions, production strategy, background strategy, and global/page freeze constraints.
8. Generate or collect source assets at production quality. Use the `390 x 844` logical design frame as the sizing reference and provide only `2x` raster resources. For each new concrete bitmap, record its logical display size, generate it at twice that width and height, and verify the decoded pixel dimensions before accepting it. Only a full-screen bitmap uses `780 x 1688 px`. Default to single-asset generation with product-design or image generation tools for new bitmaps; use atlas/contact sheet generation only when a coherent set must be reviewed together or sliced from one approved composite.
9. Run the Background Transparentization Work Node for assets that must become transparent but were generated, extracted, or sourced with a non-transparent background.
10. For transparent or masked assets, run transparent-background post-processing: alpha cleanup, matte or color-spill removal, edge decontamination, shadow/glow preservation, and target-background QA.
11. Slice or export assets and fill [references/asset-slicing-manifest-template.md](references/asset-slicing-manifest-template.md).
12. Update `docs/design/asset-inventory.md` with source, reuse decision, generation prompt when used, background handling, transparentization method, post-processing method, license, Flutter path, size, density, format, fallback, and review status.
13. Run fidelity review against the approved mockup, global design freeze, page design freeze, and target background, then fill [references/asset-fidelity-review-template.md](references/asset-fidelity-review-template.md).
14. Hand off the atlas, slicing manifest, asset inventory, and fidelity review to `flutter-pencil-design` and the Flutter task brief.

## Output Files

- `docs/design/asset-atlas.md`
- `docs/design/asset-slicing-manifest.md`
- `docs/design/asset-fidelity-review.md`
- `docs/design/asset-inventory.md`
- Exported assets under the target Flutter app asset directory, for example `assets/images/<module>/`.

For multiple pages, use page-scoped paths such as `docs/design/pages/<page-name>/asset-atlas.md` and keep the same contracts.

## Asset Rules

- Use SVG for scalable simple vector art when Flutter rendering and licensing allow it.
- Use PNG or WebP for transparent raster illustrations, textured backgrounds, and generated bitmaps.
- Use JPG only for photographic assets without transparency.
- Prefer direct single-image production for required new assets. Use atlas/contact sheet production only for style-consistent batches, multi-part illustrations, or explicitly approved composite slicing.
- Use product-design or image generation tools as the default source for new bitmap production. Record the tool, prompt, references, selected output, and rejected outputs.
- Provide only `2x` raster resources from the `390 x 844` logical design reference. Require each newly generated concrete bitmap to decode to exactly twice its recorded logical display width and height; use `780 x 1688 px` only for full-screen bitmaps.
- Use Pencil export only when the Pencil node is an approved production asset source, not when it is only a low-fidelity structure, high-fidelity restoration container, or screenshot of a page.
- Do not use Pencil screenshots, Pencil whole-page exports, or high-fidelity mockup crops as default production bitmap sources. Allow them only with explicit approval and a recorded reason.
- Reuse before generating. Every new generated image must record why existing assets were insufficient.
- Asset generation prompts must cite the global design freeze and the page design freeze. Do not generate from the page mockup alone.
- Decide the background before generation. If Flutter must composite the asset over variable surfaces, generate or export with transparent background from the start.
- Do not rely on late background removal for soft shadows, hairlines, glows, glass, translucent objects, or antialiased edges unless the removal method and edge tolerance are recorded.
- If a model cannot reliably generate transparent output, generate on a flat, high-contrast safe background and record the planned masking/removal method before accepting the asset.
- Transparent-background post-processing must be documented for every composited raster asset: removed matte color, alpha cleanup method, edge decontamination, shadow/glow preservation, padding, and target backgrounds tested.
- Validate transparent assets on checkerboard, light, dark, and actual page backgrounds before approval.
- Do not flatten shadows, glows, translucent glass, or antialiased edges into an opaque matte unless the asset is intentionally retained-background.
- Keep prompt, reference image, selected output, rejected outputs, and selection reason for each generated asset.
- Record the logical display size and `DPR=2` for every raster asset; do not generate separate `1x` or `3x` variants unless the user explicitly changes the resource policy.
- Record dark-mode variants when the asset changes meaning, contrast, or brand treatment.
- Record loading and error fallbacks for every required runtime-loaded asset.
- Do not use mockup screenshots as production assets unless explicitly approved as screenshot content.
- Do not trace or recreate third-party art without a license or replacement decision.
- Do not bury asset decisions inside design-freeze text; keep the inventory and slicing manifest explicit.

## Background Transparentization Work Node

Use this node only after source asset approval and before transparent-background post-processing.

1. Confirm the asset must be composited over Flutter UI instead of keeping its original background.
2. Choose the transparentization method: native transparent export, source-layer export, mask extraction, chroma or flat-background removal, manual alpha mask, or regeneration when the current source cannot be made clean.
3. Preserve the original source asset and write the transparent working file to a separate path.
4. Remove only the intended background; keep intentional shadows, glows, translucent surfaces, glass, antialiasing, and internal holes.
5. Record the method, threshold or mask source, removed background color, preserved effects, failure risk, and output path in the asset atlas and slicing manifest.
6. If the result has unrecoverable halo, clipped effects, broken semitransparency, or damaged details, reject transparentization and return to generation or source selection.

## Gate

Do not generate, extract, restore in Pencil, or implement Flutter UI for required visual assets when global design-freeze constraints, page design-freeze constraints, reuse check, production decision, background handling decision, background transparentization evidence when applicable, transparent-background post-processing evidence when applicable, generation evidence when used, logical display size plus verified `2x` decoded dimensions for every newly generated concrete bitmap, slicing/export manifest, inventory entries, Flutter paths, license status, and fidelity review are missing. If no exported assets are needed, record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
