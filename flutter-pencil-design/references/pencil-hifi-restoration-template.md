# Pencil High-Fidelity Restoration Template

Use this during the page design gate after Wireframe Review when Pencil must carry the approved high-fidelity visual direction for a concrete module or page. This document records how the selected mockup and design-freeze constraints were restored into editable Pencil frames.

## Source Evidence

- Restoration decision: Required / Not required
- Decision reason:
- Selected frozen high-fidelity mockup: `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`
- Mockup candidate ID / SHA-256 / confirmation time:
- Mockup review:
- Design-freeze:
- Wireframe text spec:
- Visual source of truth: selected high-fidelity mockup and page design freeze
- Wireframe scope: page structure, states, and interactions only
- Module or page task:
- Asset inventory:
- Target Pencil frame or node IDs:
- Required frame size: `390 x 844 px`
- Verified frame dimensions:
- Exported Pencil screenshot:
- Layout snapshot:

## Visual Restoration

| Visual area | Source requirement | Pencil restoration | Evidence |
|---|---|---|---|
| Layout density | | | |
| Color roles | | | |
| Typography roles | | | |
| Spacing and rhythm | | | |
| Radius and surfaces | | | |
| Icons | | | |
| Images or bitmaps | | | |
| Component states | | | |

## Separate Bitmap Generation Review

Decompose the selected mockup with [bitmap-decomposition-standard.md](bitmap-decomposition-standard.md) before Pencil restoration. Decide content ownership before bitmap eligibility. Use `N/A: native Flutter/UI/data` when a separate bitmap is not needed. Do not use a whole-page mockup crop or representative runtime data as an asset source.

### Visual Coverage Audit

Run the ownership pass, then scan back-to-front and top-left to bottom-right. Include backgrounds, low-opacity or clipped decorations, overlays, textures, every icon placement/state, logos, and illustration fragments.

| Region | Layer order | Visible element | Content owner | Runtime-variable | Classification | Asset identity or N/A | Mockup evidence | Coverage status |
|---|---|---|---|---|---|---|---|---|

Coverage verdict:

- Unowned visible elements: `0` / list
- Runtime-data visuals incorrectly marked for export: `0` / list
- Missing background decorations: `0` / list
- Missing icon placements or states: `0` / list

| Unit | Classification | Mockup evidence | 100%-match evidence | Native Flutter exact-match verdict | Separate asset verdict | Required decision | Review reason |
|---|---|---|---|---|---|---|---|

Review recommendations:

- Use `N/A: native Flutter/UI/data` only for a non-resource UI or data unit that has recorded exact-match evidence.
- Reuse, adapt, approved Pencil-node export, or mockup extraction is allowed only when the resource's silhouette, crop, color, texture, lighting, and transparency match the approved mockup 100% and its production-source approval is recorded.
- For any icon, image, illustration, logo, texture, or other resource that lacks 100%-match evidence, the required decision is `generate`; generate the dedicated bitmap and send it through the asset atlas.
- Do not approve a near-match system icon, Flutter component, existing asset, or full-page mockup crop as a substitute for a required resource.
- Treat charts, progress visuals, avatars, user photos, maps, remote thumbnails, QR codes, barcodes, signatures, and other runtime-derived imagery as data plus a UI renderer. Do not export them from the mockup. Split any fixed frame, overlay, watermark, mask texture, or decoration into its own UI or bitmap unit.
- Allow repeated icon placements to share one asset identity, but record every placement and state in the coverage audit.

## Data Restoration

Do not create, extract, or request a bitmap for a data unit. Restore text as editable Pencil content and other runtime-derived visuals as explicit representative placeholders with a documented Flutter renderer, loading state, and fallback.

| Data field or runtime visual | Representative value | Pencil placeholder node | UI renderer | Loading and fallback | Flutter data source | Evidence |
|---|---|---|---|---|---|---|

## Unresolved Design Questions

Record facts that cannot be established from the approved mockup or existing artifacts. Do not guess them. An unresolved material question blocks approval and Flutter handoff for its affected unit.

| Question | Affected unit | Available evidence | Decision needed | Blocks approval or handoff | Resolution |
|---|---|---|---|---|---|

## Asset Restoration

| Asset | Source | Pencil node or export | Flutter path | Fidelity requirement |
|---|---|---|---|---|

## Constraints for Flutter

- Must match:
- May adapt:
- Must not infer:
- Responsive constraints:
- Accessibility constraints:

## Deviations

| Deviation | Reason | Approved by | Flutter impact |
|---|---|---|---|

## Approval

- Restoration verdict: Approved / Needs iteration
- Frame dimensions verified as `390 x 844 px`: Yes / No
- Blocking issues:
- Follow-up required:
