---
name: flutter-pencil-design
description: Use when a Flutter workflow needs Pencil .pen files, low-fidelity wireframes, high-fidelity Pencil visual restoration, editable design handoff, wireframe review, screenshots, layout snapshots, or text specs derived from Pencil after Flutter project initialization.
---

# Flutter Pencil Design

## Overview

Use this skill after Flutter project initialization when a page needs a reviewed low-fidelity semantic contract or page-level high-fidelity visual restoration. Keep every Pencil design for the project in the single canonical file `docs/design/app-design.pen`. Select Full, Lightweight, or Reuse with [references/wireframe-level-standard.md](references/wireframe-level-standard.md). Only Full requires a Pencil wireframe; every level requires a reviewed text contract. After approval, the selected page-level mockup and page design decision are the visual source of truth for Pencil restoration. Low-fidelity evidence constrains meaning and behavior, never final geometry or composition.

## Orchestrated Roles

In the full workflow, dispatch a Page structure agent to select and produce the page's Full, Lightweight, or Reuse contract, a separate Wireframe reviewer, a Bitmap decomposition agent after page freeze, and a Pencil restoration agent after confirmed asset evidence. Give Pencil-writing agents disjoint node scopes inside `docs/design/app-design.pen` and serialize every write to that shared file. Forbid scope changes, user decisions, self-review, and design freeze writes. The controller validates reports and owns every confirmation and freeze.

## Safety Rule

Do not read, grep, parse, copy, or edit `.pen` files with filesystem tools. Pencil files must be accessed only through Pencil MCP tools. If the Pencil tools are unavailable, stop and ask for the design to be exported as screenshots or another supported artifact.

Before any Pencil read, design, screenshot, export, or HTML action, call `get_editor_state(include_schema: true)` if the current Pencil schema is not already loaded in context.

## Single File Rule

- Use exactly one project design file: `docs/design/app-design.pen`.
- Put low-fidelity frames, approved high-fidelity restorations, states, reusable design primitives, and design-draft asset placements in that file.
- Organize the canvas with labeled module and fidelity sections. Name frames `<module>/<page>/<state>/<low|high>` and record their stable node IDs in page-scoped text artifacts.
- Do not create page-specific, module-specific, temporary, candidate, export, backup, or restoration `.pen` files.
- Serialize Page structure, Pencil restoration, and any asset-synchronization writes because node scopes are disjoint but the file is shared. Read-only reviewers may run after the relevant write completes.
- If multiple `.pen` files already exist, stop new Pencil writes, select `docs/design/app-design.pen` as the target, consolidate required frames through Pencil tools, verify the node inventory, and remove obsolete project-owned duplicates only through the confirmed cleanup flow. Never delete user-provided source files without explicit confirmation.

## Frame Size Rule

- Create every Pencil screen or state frame at exactly `390 x 844 px` for both low-fidelity wireframes and high-fidelity restoration.
- Verify the frame node width and height through Pencil tools before screenshot capture, Wireframe Review, high-fidelity approval, or Flutter handoff.
- Reject or resize non-compliant Pencil frames before they can become workflow evidence.

## Use Cases

- Existing Pencil file is a low-fidelity wireframe source.
- A module or page implementation task needs a reviewed semantic and interaction contract before high-fidelity effect image generation.
- A module or page implementation task has an approved high-fidelity mockup that must be restored into editable Pencil frames.
- Flutter implementation needs text specs derived from Pencil layout, navigation, and state structure.
- Flutter implementation needs visual restoration constraints derived from Pencil after mockup approval.
- A Pencil wireframe must be reviewed before it becomes a task brief input.

## Workflow

1. Confirm `docs/architecture/flutter-init.md` and the project-local `flutter-dev` path exist.
2. Confirm the current module or page task brief exists.
3. Confirm the page or state comes from `docs/plans/module-map.md`, then select Full, Lightweight, or Reuse with [references/wireframe-level-standard.md](references/wireframe-level-standard.md) and record the reason.
4. If the high-fidelity restoration track is needed, confirm the page `design-decision.md`, its approved frozen mockup under `.codex-workflow/visuals/pages/<page-name>/`, and matching candidate ID, SHA-256 and confirmation time.
5. If the approved mockup has required visual assets, confirm the page `asset-manifest.md` before restoring high-fidelity visuals. Required generated assets must cite global and page freeze constraints.
6. When Full, optional Pencil evidence, or high-fidelity restoration requires Pencil, confirm the active file is `docs/design/app-design.pen`, then read its current context through Pencil tools. Otherwise record the Pencil step as `N/A`.
7. For Full or any optional Pencil evidence, verify every target screen or state frame is exactly `390 x 844 px`, then capture screenshots or layout snapshots. For Lightweight or Reuse without Pencil evidence, record `N/A: <reason>`.
8. Record Pencil frame IDs or the one inapplicability reason in the page `design-decision.md`.
9. Write the semantic contract in the same page decision. Preserve scope, content priority, tasks, states, navigation, interactions, outcomes, accessibility meaning, and content ownership; do not freeze final geometry or visual composition.
10. Add the independent Wireframe Review verdict to the same page decision. Review semantic completeness and the selected level, not visual similarity or layout polish.
11. Decompose the selected page-level mockup with [references/bitmap-decomposition-standard.md](references/bitmap-decomposition-standard.md). First assign content ownership and split runtime data from its renderer and fixed treatment; then classify each atomic unit as bitmap, UI, or data. Never crop or generate a production bitmap from representative runtime data. Run the mandatory second visual sweep for backgrounds, edge and corner decoration, overlays, textures, every icon and state, logos, and clipped fragments, then record a coverage audit with zero unowned visible elements. For every fixed visual resource, record 100%-match evidence before assigning its separate-asset verdict. Reuse, adapt, approved Pencil-node export, or explicit mockup extraction is valid only with that evidence; otherwise assign `generate` and complete the asset-manifest flow.
12. Record unresolved visual facts in the restoration evidence before making assumptions. Include the affected unit, available evidence, the decision needed, and whether the uncertainty blocks approval or Flutter handoff for that unit.
13. After page-level mockup approval, classify Pencil high-fidelity restoration as Required or Not required using the rules below.
14. For required high-fidelity visual restoration, recreate the approved page effect image in Pencil and record the frame/node IDs, parity verdict and unresolved facts in the page decision. Do not derive high-fidelity visual details from the low-fidelity wireframe when they differ from the selected mockup or page freeze.
15. Add Flutter handoff constraints to the page decision.
16. Reference the page asset manifest instead of redefining asset sources in Pencil records.

## Restoration Decision

Mark Pencil high-fidelity restoration as Required when any condition applies:

- Commercial-critical screen: onboarding, home, paywall, checkout, dashboard, editor, or conversion path.
- Complex layout, dense hierarchy, custom component composition, or unusual responsive behavior.
- Required illustration, bitmap, generated image, logo treatment, texture, chart, or brand-heavy visual.
- Visual parity is explicitly requested by the user or recorded as a release acceptance criterion.
- Flutter implementation would otherwise rely on raw mockup interpretation instead of text handoff constraints.

Mark it Not required only when the page is simple, standard, low-risk, and its page decision provides sufficient freeze and handoff constraints. Record the decision and reason only in that page decision.

## Output Files

- `docs/design/app-design.pen` as the only project `.pen` file when Pencil is required
- `docs/design/pages/<page-name>/design-decision.md` for semantic contract, review, restoration, parity and Flutter handoff
- `docs/design/pages/<page-name>/asset-manifest.md` when required visual assets exist

Do not create standalone intake, wireframe, restoration, handoff or parity documents.

## Handoff Rules

- Treat Pencil as editable design evidence, not implementation code.
- Keep every Pencil design and restoration in `docs/design/app-design.pen`; page-scoped text evidence must reference frame/node IDs in that shared file rather than another `.pen` path.
- Keep every Pencil screen or state frame at exactly `390 x 844 px`; do not use a differently sized frame as reviewed design evidence.
- Require a reviewed low-fidelity semantic contract before page-level high-fidelity generation. Require Pencil evidence only for Full; allow Lightweight text contracts and Reuse delta contracts when the level standard permits them.
- Use Pencil high-fidelity restoration only for a concrete module or page after that page high-fidelity mockup is approved and recorded in its page decision.
- Treat the selected page-level mockup and page design decision as the visual source of truth for high-fidelity restoration. Use the wireframe contract only for scope, required content, priority, tasks, states, navigation, interactions, outcomes, accessibility meaning, and ownership. It must not dictate exact geometry, containers, whitespace, component silhouettes, image ratios, crops, or decoration placement.
- After decomposing the selected mockup, review every icon, image, illustration, logo, texture, and bitmap unit before restoration. A resource may reuse an existing source or native Flutter only with recorded 100%-match evidence; otherwise separate bitmap generation and asset-manifest review are mandatory. Never use a near-match system icon, Flutter component, existing asset, or full-page mockup crop as a substitute.
- Treat runtime-derived imagery as data even when it appears rasterized in the mockup. Record its renderer, placeholder, loading state, and fallback; split any fixed frame, overlay, watermark, or texture into a separate UI or bitmap unit.
- Do not approve decomposition until the visual sweep accounts for all background decorations and every icon placement and state. Repeated icons may share one asset identity but may not omit placement coverage.
- Do not silently skip high-fidelity restoration; record Required or Not required with a reason.
- Convert Pencil evidence into text specs before it reaches implementation agents.
- Use the page decision as the source of truth for visual constraints and how Pencil carries them.
- Restore data as editable text and representative placeholder values, never as generated or extracted bitmap assets. Keep the visual treatment of a data field in its containing UI specification.
- Record image assets through `flutter-asset-atlas`; Pencil records should link the asset manifest rather than copy source, license, path, or fidelity fields.
- Export bitmap assets from Pencil only when its manifest row records the node as an approved production asset source. Do not export whole-page Pencil screenshots as production bitmaps by default.
- Record uncertainties instead of guessing hidden interactions, asset provenance, font or icon sources, component states, crop rules, or layout behavior. An unresolved uncertainty blocks approval and Flutter handoff for its affected unit.
- Do not infer extra app features from decorative design elements.
- If the design conflicts with product scope, ask which source governs before implementing.

## Gate

Do not implement from raw Pencil screenshots. Do not create or write any project `.pen` file other than `docs/design/app-design.pen`, and do not concurrently dispatch two agents that can modify it. Do not accept a Pencil screen or state frame as workflow evidence unless its node dimensions are exactly `390 x 844 px`. Do not generate a page-level high-fidelity mockup until the wireframe level and reviewed semantic contract are in the page decision; require Pencil evidence only for Full or when optional Pencil evidence is used. Do not let high-fidelity review demand geometry parity with low-fidelity evidence. Do not restore high-fidelity Pencil visuals unless the selected page-level effect image has been explicitly frozen under `.codex-workflow/visuals/pages/<page-name>/` and the page decision records that exact path. Do not approve decomposition when any visible element lacks ownership, any runtime-data visual is marked for bitmap export, or any background decoration or icon placement/state is missing from the coverage audit. Do not restore an icon, image, illustration, logo, texture, or other visual resource unless it has 100%-match evidence or a generated bitmap that has passed the asset-manifest flow. Do not restore high-fidelity Pencil visuals when required visual assets lack their required manifest fields. Do not approve a restoration or hand off an affected unit while a material visual uncertainty remains unresolved. Do not implement a Pencil-sourced screen until page-level high-fidelity approval, the Pencil restoration decision, required asset evidence and Flutter handoff constraints are written in the page decision.
