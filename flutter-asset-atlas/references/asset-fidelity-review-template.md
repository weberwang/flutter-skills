# Asset Fidelity Review Template

Use this before high-fidelity Pencil restoration or Flutter UI implementation when visual assets are required.

## Review Context

- Page or module:
- Approved mockup:
- Global design freeze:
- Page design freeze:
- Asset atlas:
- Slicing manifest:
- Asset inventory:
- Target background:
- Review evidence:

## Per-Asset Review

| Asset ID | Mockup role | Exported file | Match verdict | Tolerance | Required fixes |
|---|---|---|---|---|---|

## Visual Checks

- Cropping:
- Alignment:
- Color:
- Global style consistency:
- Page-level constraint compliance:
- Duplicate generation avoided:
- Background handling:
- Transparent post-processing:
- Transparency:
- Alpha edge or halo:
- Shadow or glow preservation:
- Tested backgrounds:
- Resolution and exact `2x` verification against each bitmap's logical display size:
- Dark mode:
- Loading fallback:
- Error fallback:

## Verdict

- Pass / Pass with deviations / Fail:
- Approved deviations:
- Blocking fixes:
- Reviewer:
- Date:

## Gate

- Fail blocks Pencil high-fidelity restoration and Flutter UI implementation.
- Missing global/page design-freeze compliance blocks approval.
- Unjustified duplicate generation blocks approval.
- Missing background decision or visible background halo blocks approval for composited assets.
- Missing transparent-background post-processing evidence blocks approval for transparent or masked raster assets.
- Pass with deviations must list every accepted mismatch and its reason.
