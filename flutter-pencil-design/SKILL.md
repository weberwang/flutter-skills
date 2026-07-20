---
name: flutter-pencil-design
description: Use when a Flutter workflow needs Pencil .pen files, low-fidelity wireframes, high-fidelity Pencil visual restoration, editable design handoff, wireframe review, screenshots, layout snapshots, or text specs derived from Pencil after Flutter project initialization.
---

# Flutter Pencil Design

## Overview

Use this skill after Flutter project initialization when Pencil is used for module/page low-fidelity structure or page-level high-fidelity visual restoration during module implementation. Low-fidelity Pencil structure comes before page-level high-fidelity mockups. After approval, the selected page-level mockup and page design freeze are the visual source of truth for Pencil restoration; the wireframe remains a structural and interaction prerequisite. Pencil can carry the approved visual target for a concrete page, but implementation agents must receive reviewed text specifications and handoff constraints instead of raw Pencil images as the only spec.

## Orchestrated Roles

In the full workflow, dispatch a Page structure agent for low-fidelity Pencil/spec work, a separate Wireframe reviewer, a Bitmap decomposition agent after page freeze, and a Pencil restoration agent after confirmed asset evidence. Give each agent disjoint paths and forbid scope changes, user decisions, self-review, and design freeze writes. The controller validates reports and owns every confirmation and freeze.

## Safety Rule

Do not read, grep, parse, copy, or edit `.pen` files with filesystem tools. Pencil files must be accessed only through Pencil MCP tools. If the Pencil tools are unavailable, stop and ask for the design to be exported as screenshots or another supported artifact.

Before any Pencil read, design, screenshot, export, or HTML action, call `get_editor_state(include_schema: true)` if the current Pencil schema is not already loaded in context.

## Frame Size Rule

- Create every Pencil screen or state frame at exactly `390 x 844 px` for both low-fidelity wireframes and high-fidelity restoration.
- Verify the frame node width and height through Pencil tools before screenshot capture, Wireframe Review, high-fidelity approval, or Flutter handoff.
- Reject or resize non-compliant Pencil frames before they can become workflow evidence.

## Use Cases

- Existing Pencil file is a low-fidelity wireframe source.
- A module or page implementation task needs a low-fidelity structural wireframe before high-fidelity effect image generation.
- A module or page implementation task has an approved high-fidelity mockup that must be restored into editable Pencil frames.
- Flutter implementation needs text specs derived from Pencil layout, navigation, and state structure.
- Flutter implementation needs visual restoration constraints derived from Pencil after mockup approval.
- A Pencil wireframe must be reviewed before it becomes a task brief input.

## Workflow

1. Confirm `docs/architecture/flutter-init.md` and the project-local `flutter-dev` path exist.
2. Confirm the current module or page task brief exists.
3. For low-fidelity structure, confirm the page or state being structured comes from `docs/plans/module-map.md`.
4. If the high-fidelity restoration track is needed, confirm Wireframe Review, `docs/design/wireframe-spec.md`, an approved frozen high-fidelity mockup under `.codex-workflow/visuals/pages/<page-name>/`, and `docs/design/design-freeze.md` exist; verify that its candidate ID, SHA-256, and confirmation time match the freeze record.
5. If the approved mockup has required visual assets, confirm `docs/design/asset-atlas.md`, `docs/design/asset-slicing-manifest.md`, `docs/design/asset-inventory.md`, and `docs/design/asset-fidelity-review.md` exist before restoring high-fidelity visuals. Required generated assets must cite global and page design-freeze constraints.
6. Read current Pencil context through Pencil tools.
7. Verify every target screen or state frame is exactly `390 x 844 px`, then capture screenshots or layout snapshots.
8. Fill [references/pencil-intake-template.md](references/pencil-intake-template.md).
9. For low-fidelity structure, run Wireframe Review with [references/wireframe-review-template.md](references/wireframe-review-template.md).
10. Convert the reviewed wireframe into text specs with [references/wireframe-spec-template.md](references/wireframe-spec-template.md).
11. Decompose the selected page-level mockup with [references/bitmap-decomposition-standard.md](references/bitmap-decomposition-standard.md). First assign content ownership and split runtime data from its renderer and fixed treatment; then classify each atomic unit as bitmap, UI, or data. Never crop or generate a production bitmap from representative runtime data. Run the mandatory second visual sweep for backgrounds, edge and corner decoration, overlays, textures, every icon and state, logos, and clipped fragments, then record a coverage audit with zero unowned visible elements. For every fixed visual resource, record 100%-match evidence before assigning its separate-asset verdict. Reuse, adapt, approved Pencil-node export, or explicit mockup extraction is valid only with that evidence; otherwise assign `generate` and complete the asset-atlas flow.
12. Record unresolved visual facts in the restoration evidence before making assumptions. Include the affected unit, available evidence, the decision needed, and whether the uncertainty blocks approval or Flutter handoff for that unit.
13. After page-level mockup approval, classify Pencil high-fidelity restoration as Required or Not required using the rules below.
14. For required high-fidelity visual restoration, recreate the approved page effect image in Pencil and fill [references/pencil-hifi-restoration-template.md](references/pencil-hifi-restoration-template.md). Do not derive high-fidelity visual details from the low-fidelity wireframe when they differ from the selected mockup or page design freeze.
15. Extract Flutter handoff constraints with [references/pencil-flutter-handoff-template.md](references/pencil-flutter-handoff-template.md).
16. Reference asset atlas artifacts instead of redefining asset sources in Pencil docs.

## Restoration Decision

Mark Pencil high-fidelity restoration as Required when any condition applies:

- Commercial-critical screen: onboarding, home, paywall, checkout, dashboard, editor, or conversion path.
- Complex layout, dense hierarchy, custom component composition, or unusual responsive behavior.
- Required illustration, bitmap, generated image, logo treatment, texture, chart, or brand-heavy visual.
- Visual parity is explicitly requested by the user or recorded as a release acceptance criterion.
- Flutter implementation would otherwise rely on raw mockup interpretation instead of text handoff constraints.

Mark it Not required only when the page is simple, standard, low-risk, and `docs/design/design-freeze.md` plus `docs/design/pencil-flutter-handoff.md` are sufficient for implementation. Record the decision and reason in the task brief and progress ledger.

## Output Files

- `docs/design/pencil-intake.md`
- `docs/design/pencil-flutter-handoff.md`
- `docs/design/pencil-hifi-restoration.md` when Pencil restores approved high-fidelity visuals
- `docs/design/wireframe-review.md`
- `docs/design/wireframe-spec.md`
- `docs/design/pencil-parity-review.md`
- `docs/design/asset-atlas.md` when required visual assets exist
- `docs/design/asset-slicing-manifest.md` when required visual assets exist
- `docs/design/asset-fidelity-review.md` when required visual assets exist
- `docs/design/asset-inventory.md` when Pencil includes required visual assets
- exported screenshots, layout snapshots, or node assets recorded in `.codex-workflow/progress.md`

For multiple pages, use page-scoped paths such as `docs/design/pages/<page-name>/pencil-hifi-restoration.md` and keep the same contracts.

## Handoff Rules

- Treat Pencil as editable design evidence, not implementation code.
- Keep every Pencil screen or state frame at exactly `390 x 844 px`; do not use a differently sized frame as reviewed design evidence.
- Use Pencil low-fidelity wireframes first for structure, navigation, state coverage, and layout intent before page-level high-fidelity effect images are generated.
- Use Pencil high-fidelity restoration only for a concrete module or page after that page high-fidelity mockup is approved and converted into `docs/design/design-freeze.md`.
- Treat the selected page-level mockup and page design freeze as the visual source of truth for high-fidelity restoration. Use the wireframe only for page scope, structure, states, and interactions; record and resolve any conflict instead of allowing it to change the approved visual target.
- After decomposing the selected mockup, review every icon, image, illustration, logo, texture, and bitmap unit before restoration. A resource may reuse an existing source or native Flutter only with recorded 100%-match evidence; otherwise separate bitmap generation and asset-atlas review are mandatory. Never use a near-match system icon, Flutter component, existing asset, or full-page mockup crop as a substitute.
- Treat runtime-derived imagery as data even when it appears rasterized in the mockup. Record its renderer, placeholder, loading state, and fallback; split any fixed frame, overlay, watermark, or texture into a separate UI or bitmap unit.
- Do not approve decomposition until the visual sweep accounts for all background decorations and every icon placement and state. Repeated icons may share one asset identity but may not omit placement coverage.
- Do not silently skip high-fidelity restoration; record Required or Not required with a reason.
- Convert Pencil evidence into text specs before it reaches implementation agents.
- Use `docs/design/design-freeze.md` as the source of truth for visual constraints; use `docs/design/pencil-hifi-restoration.md` to record how Pencil carries those constraints.
- Restore data as editable text and representative placeholder values, never as generated or extracted bitmap assets. Keep the visual treatment of a data field in its containing UI specification.
- Record image assets through `flutter-asset-atlas`; Pencil docs should reference reuse, generation, slicing, license, Flutter path, and fidelity evidence rather than inventing those details.
- Export bitmap assets from Pencil only when the node is recorded in `flutter-asset-atlas` as an approved production asset source. Do not export whole-page Pencil screenshots as production bitmaps by default.
- Record uncertainties instead of guessing hidden interactions, asset provenance, font or icon sources, component states, crop rules, or layout behavior. An unresolved uncertainty blocks approval and Flutter handoff for its affected unit.
- Do not infer extra app features from decorative design elements.
- If the design conflicts with product scope, ask which source governs before implementing.

## Gate

Do not implement from raw Pencil screenshots. Do not accept a Pencil screen or state frame as workflow evidence unless its node dimensions are exactly `390 x 844 px`. Do not generate a page-level high-fidelity mockup until Pencil intake, Wireframe Review, and `docs/design/wireframe-spec.md` exist. Do not restore high-fidelity Pencil visuals unless the selected page-level effect image has been explicitly frozen under `.codex-workflow/visuals/pages/<page-name>/` and the page design freeze records that exact path. Do not approve decomposition when any visible element lacks ownership, any runtime-data visual is marked for bitmap export, or any background decoration or icon placement/state is missing from the coverage audit. Do not restore an icon, image, illustration, logo, texture, or other visual resource unless it has 100%-match evidence or a generated bitmap that has passed the asset-atlas flow. Do not restore high-fidelity Pencil visuals when required visual assets lack a separate-asset review verdict, reuse check, production decision, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, asset atlas, slicing manifest, inventory, and fidelity review. Do not approve a restoration or hand off an affected unit while a material visual uncertainty remains unresolved. Do not implement a Pencil-sourced screen until page-level high-fidelity approval, the Pencil high-fidelity restoration decision, required restoration evidence, asset evidence when required, and Flutter handoff constraints are written.
