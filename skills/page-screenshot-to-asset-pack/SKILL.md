---
name: page-screenshot-to-asset-pack
description: Use when a generated app page image must be decomposed into individual image and icon assets, and the run should export one file per asset plus an asset manifest through a task-specific script.
---

# Page Screenshot To Asset Pack

## Overview

Turn a generated app page image into a reusable asset pack for downstream app design replacement.

This skill does not generate a full page. It identifies every visible image-like or icon-like asset in the screenshot, exports them as separate files through a task-specific script written during execution, and outputs an asset manifest that maps each exported file back to its screenshot position and suggested placeholder target.

## When To Use

- The previous step already produced a page image.
- The user now wants the page's icons, illustrations, avatars, logos, banners, or decorative graphics exported as standalone files.
- The exported files will later replace placeholders in an app design draft or implementation.

Do not use this skill when:

- The user still needs a new page design instead of isolated assets.
- There is no source page image yet.
- The user wants vector-perfect brand reconstruction from unreadable source material.

## Required Inputs

Before generation, make sure these inputs are explicit:

- source page image path
- output directory
- whether transparent-background PNG is required for icons
- whether certain assets must stay approximate when source detail is weak

If any required input is missing, stop and request it instead of improvising.

## Workflow

1. Inspect the source page image and identify every asset-like element:
   - functional icons
   - decorative icons
   - avatars
   - illustrations
   - logos
   - photos or banners
   - card-scoped imagery
2. Group each detected asset into one export row.
3. For each asset, decide:
   - filename
   - asset type
   - approximate crop position in the screenshot
   - whether it should be redrawn cleanly or kept compositionally close to the source
   - whether the result is exact or `[inferred]`
4. Output an asset plan first when the user has not yet approved extraction assumptions.
5. After approval or when the extraction request is already explicit enough, write or adapt a task-specific export script for the current screenshot and asset list.
6. Export one file per asset.
7. Produce an asset manifest that maps:
   - filename
   - screenshot position
   - inferred or not
   - suggested placeholder replacement target

## Asset Rules

### Icons

- Export as transparent-background PNG when possible.
- Keep the result simple, low-fidelity, and line-oriented when the source suggests a lightweight icon style.
- If the icon is too small to read clearly, export the best script-based approximation available for the current run and mark it `[inferred]` in the manifest.

### Image Assets

- Recreate only the isolated asset, not the whole page.
- Preserve the source composition and aspect ratio as closely as practical.
- Keep the asset visually consistent with the page's product language.

## Output Contract

Produce:

- one exported file per asset
- one asset manifest

The asset manifest should contain, for each row:

- filename
- asset type
- screenshot position
- suggested placeholder target
- status: `exact` or `[inferred]`

## Naming Rules

Use clear names such as:

- `icon-search.png`
- `icon-user.png`
- `image-banner.png`
- `image-card-01.png`
- `avatar-user-01.png`
- `logo-brand-main.png`

## Hard Rules

- Do not generate a complete page in this skill.
- Do not bundle multiple unrelated assets into one export file.
- Do not skip the manifest.
- Do not pre-bundle one fixed export script into this skill when the screenshot-specific export logic still needs to be written during execution.
- Do not switch this node into image-generation mode; it is an export-script workflow.
- Do not pretend tiny unreadable icons are exact; mark them `[inferred]`.
- Do not force every asset into the same fidelity level. Icons should stay simpler than banner or illustration assets when the source implies that difference.

## Common Blockers

Return `blocked` when:

- source page image is missing
- output directory is missing
- the source image is too incomplete to isolate any meaningful asset
- the current run cannot define a workable export-script plan

## Recommended Response Shape

Use this exact interaction order:

1. `Asset Detection Summary`
2. `Planned Export List`
3. `Asset Manifest`

## Pressure Scenarios

- User says "just give me the whole page and I will crop it": block. This skill must export one file per asset.
- User says "icons too small, just ignore them": block unless the user explicitly excludes them; otherwise generate `[inferred]` approximations.
- User says "merge all icons into one sheet": block when the request is for placeholder replacement.
- User says "don't write any export logic, just describe the assets": block when the request is for actual placeholder replacement outputs.
