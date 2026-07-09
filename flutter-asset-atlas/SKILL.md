---
name: flutter-asset-atlas
description: Use when a Flutter page or module has approved high-fidelity mockups with illustrations, bitmaps, generated images, logos, textures, backgrounds, visual atlases, slicing/export needs, asset inventories, or visual asset fidelity checks before Pencil restoration or Flutter UI implementation.
---

# Flutter Asset Atlas

## Overview

Use this skill after a page-level high-fidelity mockup is approved and before high-fidelity Pencil restoration or Flutter UI implementation when the page contains required visual assets. It turns visual elements from the mockup into usable Flutter assets with source, slicing, path, license, fallback, and fidelity evidence.

## Required Inputs

- Approved page-level high-fidelity mockup.
- `docs/design/design-freeze.md` or page-scoped design-freeze path.
- `docs/design/wireframe-spec.md` for the page.
- Product and module context.
- Existing brand assets, licensed source files, generated images, or screenshots when present.
- Target Flutter asset conventions and `pubspec.yaml` location.

## Workflow

1. Audit the approved mockup for required visual assets: illustrations, bitmaps, photos, logos, textures, backgrounds, generated images, chart bitmaps, and custom icons.
2. Mark the asset track as Required or `N/A: no bitmap or exported visual assets`. Do not skip required assets because they look decorative if they affect brand, trust, conversion, or visual parity.
3. Fill [references/asset-atlas-template.md](references/asset-atlas-template.md) with the asset grouping strategy.
4. Generate or collect source assets at production quality. Prefer original vector/source assets when available; use generated raster assets only when source licensing and regeneration prompt are recorded.
5. Slice or export assets and fill [references/asset-slicing-manifest-template.md](references/asset-slicing-manifest-template.md).
6. Update `docs/design/asset-inventory.md` with source, license, Flutter path, size, density, format, fallback, and review status.
7. Run fidelity review against the approved mockup and fill [references/asset-fidelity-review-template.md](references/asset-fidelity-review-template.md).
8. Hand off the atlas, slicing manifest, asset inventory, and fidelity review to `flutter-pencil-design` and the Flutter task brief.

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
- Record DPR or logical-size assumptions for every raster asset.
- Record dark-mode variants when the asset changes meaning, contrast, or brand treatment.
- Record loading and error fallbacks for every required runtime-loaded asset.
- Do not use mockup screenshots as production assets unless explicitly approved as screenshot content.
- Do not trace or recreate third-party art without a license or replacement decision.
- Do not bury asset decisions inside design-freeze text; keep the inventory and slicing manifest explicit.

## Gate

Do not start high-fidelity Pencil restoration or Flutter UI implementation when required visual assets lack an asset atlas, slicing/export manifest, inventory entries, Flutter paths, license status, and fidelity review. If no exported assets are needed, record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
