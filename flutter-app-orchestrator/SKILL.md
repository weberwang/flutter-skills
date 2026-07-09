---
name: flutter-app-orchestrator
description: Use when a user wants to build, redesign, commercialize, or ship a Flutter app with Codex, especially when the request spans product definition, UX/UI quality, architecture, implementation planning, subagent execution, review, or release readiness.
---

# Flutter App Orchestrator

## Overview

Use this as the entry point for commercial Flutter app delivery. The controller keeps scope tight, selects the next specialist skill, writes durable artifacts, and blocks delivery when quality gates are missing.

## Core Rule

Do not jump from idea to code. Move through product, UX/UI, technical design, implementation plan, delivery, review, and release gates. If the user asks for a shortcut, state the risk and keep the smallest safe gate that protects quality.

## Workflow

### Global Design

1. Define the product with `flutter-product-spec`.
2. Draft global UX/UI goals, flows, states, navigation model, and design-system direction with `flutter-ux-ui-quality`.
3. Confirm global UX/UI direction with high-fidelity effect images using `flutter-hifi-mockup`; this confirms visual direction and design-system intent only, not page-level implementation readiness.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split modules and build order with `flutter-implementation-plan`; the plan must account for module dependencies and page interaction order.

### Module Delivery

7. Execute tasks with `flutter-subagent-delivery`; each UI module or page task must first create a low-fidelity Pencil structure, pass Wireframe Review, convert it into text specs, then generate and approve a page-level high-fidelity effect image.
8. After page-level high-fidelity approval and design freeze, use `flutter-asset-atlas` when the page has required visual assets that need generation, slicing, export, inventory, or fidelity review.
9. Decide whether Pencil high-fidelity restoration is required. Restore the page in Pencil when required, then implement the Flutter page from text specs and handoff artifacts.
10. Review delivery with `flutter-quality-review`.
11. Check store and business release readiness with `flutter-release-readiness`.

## Required Artifacts

Create or update these files in the target app repo:

- `docs/product/product-brief.md`
- `docs/product/mvp-scope.md`
- `docs/product/user-stories.md`
- `docs/design/user-flows.md`
- `docs/design/screen-spec.md`
- `docs/design/ui-quality-gates.md`
- `docs/design/mockup-brief.md`
- `docs/design/mockup-review.md`
- `docs/design/pencil-intake.md`
- `docs/design/pencil-flutter-handoff.md`
- `docs/design/pencil-hifi-restoration.md`
- `docs/design/wireframe-review.md`
- `docs/design/wireframe-spec.md`
- `docs/design/pencil-parity-review.md`
- `docs/design/asset-atlas.md`
- `docs/design/asset-slicing-manifest.md`
- `docs/design/asset-fidelity-review.md`
- `docs/design/asset-inventory.md`
- `docs/design/design-freeze.md`
- `docs/architecture/flutter-init.md`
- `docs/architecture/technical-design.md`
- `docs/plans/module-map.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`
- `.codex-workflow/decisions.md`
- `.codex-workflow/risks.md`
- `docs/release/release-checklist.md`

Use [references/artifacts.md](references/artifacts.md) for the artifact contract.

## Hard Gates

- No implementation before MVP scope and screen states exist.
- No implementation before the Flutter project has the fixed plugin stack and a generated `flutter-dev` skill path recorded in `docs/architecture/flutter-init.md`.
- No UX/UI approval from text alone; high-value screens require selected high-fidelity effect images or an explicit "no mockup needed" decision.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, and page interaction order are recorded in `docs/plans/module-map.md`.
- No page implementation readiness from global high-fidelity direction alone; global mockups do not replace page-level design gates.
- No page-level high-fidelity mockup before the current page task has a low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- No page UI implementation before the current page task has a reviewed low-fidelity structure, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/wireframe-spec.md`, page-level mockup approval, design freeze, and required asset atlas evidence.
- No implementation from raw Pencil images; Pencil wireframes or high-fidelity restorations must be converted into text specs and `docs/design/pencil-flutter-handoff.md`.
- No high-fidelity Pencil restoration or Flutter UI implementation when required illustrations, bitmaps, logos, textures, generated images, or visual exports lack asset atlas, slicing manifest, asset inventory, Flutter path, license status, and fidelity review.
- No UI completion claim before screenshots or Flutter golden evidence exist.
- No task completion before `flutter analyze` and relevant tests are reported.
- No delivery completion while Critical or Important review findings remain open.
- No release claim before privacy, account, payment, crash reporting, analytics, and store checklist are checked or explicitly marked out of scope.

## Subagent Use

Use subagents for independent product, UX, architecture, review, and release checks. Do not dispatch multiple implementation agents against the same write scope. Read [references/subagent-map.md](references/subagent-map.md) before orchestrating subagents.

## Common Mistakes

- Treating a prototype as a commercial app.
- Letting the implementer self-approve UI quality.
- Treating a generated mockup as implementation truth without design-freeze constraints.
- Treating text-only UX/UI descriptions as sufficient for visual approval.
- Treating global high-fidelity direction as a substitute for page-level low-fidelity structure, Wireframe Review, and page mockup approval.
- Splitting modules only by code folders instead of product flow, data ownership, routing, and page interaction order.
- Generating page-level high-fidelity mockups before the page structure is reviewed and converted into text specs.
- Skipping asset atlas and slicing when the approved mockup contains required visual assets.
- Reading `.pen` files with normal filesystem tools instead of Pencil tools.
- Passing Pencil screenshots or restored Pencil frames directly to implementation agents instead of converting them into text specs.
- Skipping high-fidelity Pencil restoration when the user expects Pencil to carry the approved visual target.
- Treating bitmap or illustration details as implicit UI instead of tracked assets.
- Adding alternative state, result, JSON, or responsive-layout packages before checking the fixed stack.
- Running only unit tests for screen-heavy changes.
- Accepting vague words such as "premium", "simple", or "polished" without screen-level acceptance criteria.
