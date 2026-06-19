# Asset Atlas Flow

Use this reference before shared HTML interactive prototype work or module HTML interactive prototype work whenever the approved visual evidence includes one page whose regions cannot be restored faithfully enough in code and therefore need bitmap assets that stay very close to the effect image.

## Goal

Turn one approved page into one reusable atlas packet that downstream prototypes can consume directly.

This flow sits after effect-image confirmation and before prototype generation. It is not a design-direction workflow. It is a resource-normalization workflow.

## Entry Conditions

Enter this flow when one or more of these are true:

- a shared shell or module page includes a visual region whose final look cannot be restored faithfully enough with code
- empty, error, loading, or other status imagery must stay very close to the approved effect image instead of being redrawn from generic code primitives
- the approved design would lose important fidelity if the region were rebuilt only from standard components, vectors, gradients, or library icons

If the prototype can be built faithfully enough from standard vectors, shapes, gradients, tokens, and library icons, skip this flow.

Do not enter this flow for image regions that are only schematic placeholders and whose real content will be created later from runtime data. Those regions should stay as placeholders in the prototype contract.

## Required Inputs

Before atlas preparation begins, make sure these inputs are explicit:

- approved source effect image or approved source screenshots for the current page
- atlas scope: `shared` or `module`
- current page name
- target atlas output directory for that page
- the current `docs/project/assets/global-asset-catalog.json`
- whether any candidate asset is already known to be reusable

If the catalog is missing, repair or initialize it from `global-asset-catalog-contract.md` before classifying reuse.

## Internal Flow

1. Read the current global asset catalog first.
2. Work on one page at a time. Identify every visual region in the current page that truly needs bitmap fidelity.
3. If the page belongs to a module, compare the current page effect image against the active module `impl.md` and the page's required state set first. If `error`, `empty`, `loading`, permission, or other page-local states are required but not yet represented strongly enough for atlas or prototype work, supplement those missing states before finalizing the page checklist.
4. Remove placeholder-only regions first. If a region is only a visual stand-in for runtime-created data content, record it as a placeholder contract and keep it out of atlas generation.
5. For every remaining visual region, first decide whether Flutter SDK standard capabilities alone can restore it faithfully enough without adding new bitmap assets.
6. Classify the current page into three written groups before atlas generation:
   - `bitmap_required`
   - `flutter_native`
   - `placeholder_only`
7. Only the regions inside `bitmap_required` may continue into atlas generation. Regions inside `flutter_native` must stay as Flutter-native implementation targets. Regions inside `placeholder_only` must stay as runtime placeholders.
8. Classify each `bitmap_required` asset by `name`, `semantic`, and `usage_scenarios`:
   - `reusable`
   - `candidate_reuse`
   - `shared_only`
   - `module_only`
9. If any asset is `candidate_reuse`, stop and request confirmation.
10. Present the written current-page checklist plus the remaining new bitmap list for the current page and stop for explicit confirmation before atlas generation.
11. Write one TexturePacker-compatible `texturepacker.json` for the current page atlas.
12. Use that same `texturepacker.json` to request one transparent-background atlas PNG for the current page through `gpt-image-2-generator`. Do not crop the atlas out of the effect image.
13. Slice the atlas strictly by the confirmed `texturepacker.json`.
14. Update the global asset catalog with:
   - atlas owner
   - reuse status
   - slice output paths
   - any confirmed cross-module reuse
15. Allow prototype work only after atlas confirmation and slice export are complete.

## Flutter-Native Standard

Treat a region as `flutter_native` only when Flutter SDK standard capabilities can restore it faithfully enough without adding new bitmap assets.

Typical Flutter-native candidates:

- standard buttons and button shells
- standard icons
- regular cards and labels
- normal rounded rectangles
- simple borders, shadows, gradients, and fills
- ordinary text presentation

Do not mark a region `flutter_native` if those same capabilities would still lose the approved paper texture, watercolor texture, sticker feel, torn edge, complex illustration fidelity, or other critical visual character.

## Shared Scope Rules

Shared page atlas work is for:

- shared shell imagery
- shared state imagery
- shared badges, logos, or decorative resources
- shared bitmap assets reused by multiple modules

Suggested paths:

- `docs/project/assets/global-asset-catalog.json`
- `docs/project/assets/shared/<page-name>/texturepacker.json`
- `docs/project/assets/shared/<page-name>/<page-name>-atlas.png`
- `docs/project/assets/shared/<page-name>/slices/`

## Module Scope Rules

Module page atlas work is for:

- bitmap assets unique to one module
- module-specific state illustrations
- module-specific imagery that cannot reuse a shared slice
- page-local states that the module `impl.md` requires even when the first approved effect image did not yet show them clearly enough

Suggested paths:

- `docs/project/modules/<module>/assets/<page-name>/texturepacker.json`
- `docs/project/modules/<module>/assets/<page-name>/<page-name>-atlas.png`
- `docs/project/modules/<module>/assets/<page-name>/slices/`

## TexturePacker Contract

The atlas JSON must be compatible with TexturePacker-style frame metadata and should remain stable enough for later re-slicing.

At minimum, preserve:

- `frames`
- `meta`
- `frame`
- `rotated`
- `trimmed`
- `spriteSourceSize`
- `sourceSize`

The cutting script must use this JSON as the slicing contract. Do not let the slicing step guess coordinates by image analysis after confirmation.

## Atlas Rules

- Atlas PNG output must keep a transparent background.
- Do not bake the page background into the atlas.
- Do not mix unrelated scopes into one atlas without an explicit reason.
- Do not create duplicate bitmap assets when a reusable slice already exists.
- Do not auto-merge semantically similar assets when the reuse decision is still ambiguous.
- Do not include placeholder-only regions whose real content will be drawn or assembled later from runtime data.
- Do not turn a region into a bitmap asset when code can already restore it faithfully enough.

## Prototype Rules

- Shared prototypes must directly reference shared slices.
- Module prototypes must directly reference shared slices or module slices.
- Do not continue prototype work with screenshot crops or unsliced atlas regions once this flow is required.
- Placeholder-only regions are allowed to remain placeholders in the prototype, but they must not be treated as atlas assets.

## Output Contract

Produce for the current page:

- one written decision checklist containing `bitmap_required`, `flutter_native`, and `placeholder_only`
- updated `docs/project/assets/global-asset-catalog.json`
- one confirmed `texturepacker.json` for that page
- one transparent atlas PNG for that page
- one exported slice directory for that page

## Routing Outcome

Use one of these outcomes:

- `advanced`: the current page's bitmap list was confirmed, and its atlas JSON, atlas PNG, and slice outputs all exist and are confirmed
- `blocked`: reuse confirmation, atlas confirmation, or required atlas artifacts are missing
- `not_executed`: the atlas preparation did not actually run

## Hard Rules

- Do not enter shared HTML interactive prototype work when shared atlas preparation is required but incomplete.
- Do not enter module HTML interactive prototype work when module atlas preparation is required but incomplete.
- Do not bypass the global asset catalog.
- Do not approve an atlas with a non-transparent background.
- Do not generate an atlas before the current page's bitmap list is explicitly confirmed.
- Do not batch-generate multiple page atlases in one step.
- Do not slice from unconfirmed geometry.
- Do not assume the first module effect image already covers every required page-local state. Repair missing state coverage before freezing the page atlas checklist.
