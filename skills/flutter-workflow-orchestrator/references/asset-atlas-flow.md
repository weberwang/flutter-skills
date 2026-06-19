# Asset Atlas Flow

Use this reference before shared HTML interactive prototype work or module HTML interactive prototype work whenever the approved visual evidence includes bitmap assets that cannot be satisfied by a standard library alone.

## Goal

Turn approved shared or module visual evidence into one reusable atlas packet that downstream prototypes can consume directly.

This flow sits after effect-image confirmation and before prototype generation. It is not a design-direction workflow. It is a resource-normalization workflow.

## Entry Conditions

Enter this flow when one or more of these are true:

- a shared shell or module page needs custom icons, illustrations, avatars, textures, photos, or logos
- empty, error, loading, or other status imagery must be preserved as bitmap assets
- the approved design cannot be restored faithfully by a standard component or icon library alone

If the prototype can be built entirely from standard vectors, shapes, gradients, and library icons, skip this flow.

## Required Inputs

Before atlas preparation begins, make sure these inputs are explicit:

- approved source effect image or approved source screenshots
- atlas scope: `shared` or `module`
- target atlas output directory
- the current `docs/project/assets/global-asset-catalog.json`
- whether any candidate asset is already known to be reusable

If the catalog is missing, repair or initialize it from `global-asset-catalog-contract.md` before classifying reuse.

## Internal Flow

1. Read the current global asset catalog first.
2. Identify every bitmap asset needed by the target shared scope or module scope.
3. Classify each asset by `name`, `semantic`, and `usage_scenarios`:
   - `reusable`
   - `candidate_reuse`
   - `shared_only`
   - `module_only`
4. If any asset is `candidate_reuse`, stop and request confirmation.
5. Confirm the export list for the active atlas scope.
6. Write one TexturePacker-compatible `texturepacker.json` for the active atlas.
7. Generate one transparent-background atlas PNG for that same packet.
8. Slice the atlas strictly by the confirmed `texturepacker.json`.
9. Update the global asset catalog with:
   - atlas owner
   - reuse status
   - slice output paths
   - any confirmed cross-module reuse
10. Allow prototype work only after atlas confirmation and slice export are complete.

## Shared Scope Rules

Shared atlas work is for:

- shared shell imagery
- shared state imagery
- shared badges, logos, or decorative resources
- shared bitmap assets reused by multiple modules

Suggested paths:

- `docs/project/assets/global-asset-catalog.json`
- `docs/project/assets/shared/<atlas-name>/texturepacker.json`
- `docs/project/assets/shared/<atlas-name>/<atlas-name>.png`
- `docs/project/assets/shared/<atlas-name>/slices/`

## Module Scope Rules

Module atlas work is for:

- bitmap assets unique to one module
- module-specific state illustrations
- module-specific imagery that cannot reuse a shared slice

Suggested paths:

- `docs/project/modules/<module>/assets/<atlas-name>/texturepacker.json`
- `docs/project/modules/<module>/assets/<atlas-name>/<atlas-name>.png`
- `docs/project/modules/<module>/assets/<atlas-name>/slices/`

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

## Prototype Rules

- Shared prototypes must directly reference shared slices.
- Module prototypes must directly reference shared slices or module slices.
- Do not continue prototype work with screenshot crops, unsliced atlas regions, or temporary placeholder assets once this flow is required.

## Output Contract

Produce:

- updated `docs/project/assets/global-asset-catalog.json`
- one confirmed `texturepacker.json` per active atlas
- one transparent atlas PNG per active atlas
- one exported slice directory per active atlas

## Routing Outcome

Use one of these outcomes:

- `advanced`: atlas JSON, atlas PNG, and slice outputs all exist and are confirmed
- `blocked`: reuse confirmation, atlas confirmation, or required atlas artifacts are missing
- `not_executed`: the atlas preparation did not actually run

## Hard Rules

- Do not enter shared HTML interactive prototype work when shared atlas preparation is required but incomplete.
- Do not enter module HTML interactive prototype work when module atlas preparation is required but incomplete.
- Do not bypass the global asset catalog.
- Do not approve an atlas with a non-transparent background.
- Do not slice from unconfirmed geometry.
