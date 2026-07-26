# Asset Manifest

Maintain one `docs/design/pages/<page-name>/asset-manifest.md` for each page with fixed visual assets. This is an internal production and audit artifact. Never present its table, mapping, notes, dimensions, or source decisions to the user during bitmap confirmation; the user sees only the numbered overlay image.

## Confirmation Evidence

- Page:
- Frozen page image path:
- Frozen page image SHA-256:
- Numbered overlay path: `.codex-workflow/visuals/pages/<page-name>/bitmap-confirmation-v<version>.png`
- Overlay version:
- Overlay SHA-256:
- Confirmed numbers:
- User decision:
- Confirmation time:
- Overall fidelity verdict:

## Internal Number Mapping

| No. | Visual role | Placements/states | Box bounds | 100% match evidence | Decision/source/license | Crop/background/effects | Logical/output size | Flutter path | Status/fidelity |
|---|---|---|---|---|---|---|---|---|---|
| | | | x/y/w/h on frozen image | | reuse / adapt / generate / export / extract | transparent / retained / mask; shadow/glow handling | logical; exact 2x pixels | | planned / confirmed / produced / pass / blocked |

Rules:

- Use the same number for repeated placements of one shared asset; list every placement and state.
- Use different numbers for distinct states or visually different outputs.
- Keep production details internal even when the user excludes or revises a number.
- Record only the selected source, required prompt hash, failure reason, license, output, fallback, and fidelity result.
- A material change to membership, numbered bounds, placement/state coverage, crop, source, background handling, size, or production verdict invalidates the affected number and requires a new overlay version.
- Keep unselected candidates, repeated prompts, and intermediate exports transient.
