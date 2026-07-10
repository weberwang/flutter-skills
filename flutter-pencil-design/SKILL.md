---
name: flutter-pencil-design
description: Use when a Flutter workflow needs Pencil .pen files, low-fidelity wireframes, high-fidelity Pencil visual restoration, editable design handoff, wireframe review, screenshots, layout snapshots, or text specs derived from Pencil after Flutter project initialization.
---

# Flutter Pencil Design

## Overview

Use this skill after Flutter project initialization when Pencil is used for module/page low-fidelity structure or page-level high-fidelity visual restoration during module implementation. Low-fidelity Pencil structure comes before page-level high-fidelity mockups. Pencil can carry the approved visual target for a concrete page, but implementation agents must receive reviewed text specifications and handoff constraints instead of raw Pencil images as the only spec.

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
4. If the high-fidelity restoration track is needed, confirm Wireframe Review, `docs/design/wireframe-spec.md`, approved high-fidelity mockup, and `docs/design/design-freeze.md` exist.
5. If the approved mockup has required visual assets, confirm `docs/design/asset-atlas.md`, `docs/design/asset-slicing-manifest.md`, `docs/design/asset-inventory.md`, and `docs/design/asset-fidelity-review.md` exist before restoring high-fidelity visuals. Required generated assets must cite global and page design-freeze constraints.
6. Read current Pencil context through Pencil tools.
7. Verify every target screen or state frame is exactly `390 x 844 px`, then capture screenshots or layout snapshots.
8. Fill [references/pencil-intake-template.md](references/pencil-intake-template.md).
9. For low-fidelity structure, run Wireframe Review with [references/wireframe-review-template.md](references/wireframe-review-template.md).
10. Convert the reviewed wireframe into text specs with [references/wireframe-spec-template.md](references/wireframe-spec-template.md).
11. After page-level mockup approval, classify Pencil high-fidelity restoration as Required or Not required using the rules below.
12. For required high-fidelity visual restoration, recreate or inspect the approved page direction in Pencil and fill [references/pencil-hifi-restoration-template.md](references/pencil-hifi-restoration-template.md).
13. Extract Flutter handoff constraints with [references/pencil-flutter-handoff-template.md](references/pencil-flutter-handoff-template.md).
14. Reference asset atlas artifacts instead of redefining asset sources in Pencil docs.

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
- Do not silently skip high-fidelity restoration; record Required or Not required with a reason.
- Convert Pencil evidence into text specs before it reaches implementation agents.
- Use `docs/design/design-freeze.md` as the source of truth for visual constraints; use `docs/design/pencil-hifi-restoration.md` to record how Pencil carries those constraints.
- Record image assets through `flutter-asset-atlas`; Pencil docs should reference reuse, generation, slicing, license, Flutter path, and fidelity evidence rather than inventing those details.
- Export bitmap assets from Pencil only when the node is recorded in `flutter-asset-atlas` as an approved production asset source. Do not export whole-page Pencil screenshots as production bitmaps by default.
- Record uncertainties instead of guessing hidden interactions.
- Do not infer extra app features from decorative design elements.
- If the design conflicts with product scope, ask which source governs before implementing.

## Gate

Do not implement from raw Pencil screenshots. Do not accept a Pencil screen or state frame as workflow evidence unless its node dimensions are exactly `390 x 844 px`. Do not generate a page-level high-fidelity mockup until Pencil intake, Wireframe Review, and `docs/design/wireframe-spec.md` exist. Do not restore high-fidelity Pencil visuals when required visual assets lack reuse check, production decision, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, asset atlas, slicing manifest, inventory, and fidelity review. Do not implement a Pencil-sourced screen until page-level high-fidelity approval, the Pencil high-fidelity restoration decision, required restoration evidence, asset evidence when required, and Flutter handoff constraints are written.
