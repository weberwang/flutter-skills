# Pencil High-Fidelity Restoration Template

Use this during the page design gate after Wireframe Review when Pencil must carry the approved high-fidelity visual direction for a concrete module or page. This document records how the selected mockup and design-freeze constraints were restored into editable Pencil frames.

## Source Evidence

- Restoration decision: Required / Not required
- Decision reason:
- Selected high-fidelity mockup:
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

Decompose the selected mockup before Pencil restoration. Use `N/A: native Flutter/UI/data` when a separate bitmap is not needed. Do not use a whole-page mockup crop as the default source.

| Unit | Classification | Mockup evidence | Native Flutter exact-match verdict | Separate asset verdict | Recommended decision | Review reason |
|---|---|---|---|---|---|---|

Review recommendations:

- Prefer `N/A: native Flutter/UI/data` for text, simple icons, standard components, gradients, shapes, and effects Flutter can reproduce exactly.
- Prefer reuse or adaptation when an approved, licensed source already satisfies the selected mockup.
- Recommend separate generation for approved illustrations, photos, textured or lit raster art, and complex bitmap fills that native Flutter cannot match exactly.
- Use approved Pencil-node export or mockup extraction only when their explicit production-source approval is recorded; otherwise generate the asset separately and send it through the asset atlas.

## Data Restoration

Do not create, extract, or request a bitmap for a data unit. Restore its approved visual treatment with an editable Pencil text node; use representative placeholder values only when production data is unavailable.

| Data field | Representative value | Pencil text node | Visual treatment source | Flutter data source | Evidence |
|---|---|---|---|---|---|

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
