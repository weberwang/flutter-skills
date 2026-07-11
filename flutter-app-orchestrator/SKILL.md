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
2. Draft global UX/UI goals, flows, states, navigation model, and design-system direction with `flutter-ux-ui-quality`. Before generating any global effect image, use [references/global-visual-direction-prompt-template.md](references/global-visual-direction-prompt-template.md) to create and save `docs/design/prompts/global-visual-direction-prompt.md`. Trace every product claim, task, state, content constraint, and acceptance criterion to the PRD artifacts; document the product-design-principle check in the same file; then use that saved prompt file to generate three comparable global visual directions. Run `@product-design user-context` preflight followed by `@product-design get-context` and `@product-design ideate` to select one direction.
3. Confirm global UX/UI direction with high-fidelity effect images using `flutter-hifi-mockup`. After the effect-image batch is complete, automatically dispatch the Mockup reviewer subagent with the images, product brief, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Record the five highest-impact findings and concrete fixes in `docs/design/mockup-review.md`, then ask the user whether to apply the proposed changes. Do not revise, select, or freeze a direction until the user explicitly approves changes or explicitly accepts the current result. Use `@product-design image-to-code` only when the selected visual target has interaction ambiguity that needs a review-only prototype. This confirms visual direction and design-system intent only, not page-level implementation readiness.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split modules and build order with `flutter-implementation-plan`; the plan must account for module dependencies, page interaction order, and the global verification platform scope.

### Module Delivery

7. Execute tasks with `flutter-subagent-delivery`; each UI module or page task must first create a low-fidelity Pencil structure, pass Wireframe Review, and convert it into text specs. Before generating any page-level effect image, use [references/page-hifi-mockup-prompt-template.md](references/page-hifi-mockup-prompt-template.md) to create and save `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`. Trace every page task, module, state, copy, data, interaction, and visual constraint to the PRD and approved design artifacts; document the product-design-principle check in the same file; then use that saved prompt file to generate the page-level high-fidelity effect image. After the image is complete, automatically dispatch the Mockup reviewer subagent with the image, wireframe spec, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Record the five highest-impact findings and concrete fixes in `docs/design/mockup-review.md`, then ask the user whether to apply the proposed changes. Do not revise, approve, or freeze the page design until the user explicitly approves changes or explicitly accepts the current result.
8. After page-level high-fidelity approval and design freeze, use `flutter-asset-atlas` when the page has required visual assets that need reuse checks, generation, enhancement, slicing, export, inventory, or fidelity review. New bitmap generation must use product-design or image generation tools by default and follow the global design freeze and page design freeze. Treat bitmap enhancement as a design change: replace the corresponding asset in the design draft, preserve the approved layout and constraints, and record the updated design evidence before implementation.
9. Decide whether Pencil high-fidelity restoration is required. Restore the page in Pencil when required, including every generated or enhanced bitmap used by the approved page, then implement the Flutter page from text specs and handoff artifacts.
10. Review delivery with `flutter-quality-review`; for user-facing UI flows, run `@product-design audit` against screenshots before the final UX/UI verdict.
11. Check store and business release readiness with `flutter-release-readiness`.
12. After completing a task, list exactly one next task.

## Required Artifacts

Create or update these files in the target app repo:

- `docs/product/product-brief.md`
- `docs/product/mvp-scope.md`
- `docs/product/user-stories.md`
- `docs/design/user-flows.md`
- `docs/design/screen-spec.md`
- `docs/design/ui-quality-gates.md`
- `docs/design/mockup-brief.md`
- `docs/design/prompts/global-visual-direction-prompt.md`
- `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`
- `docs/design/mockup-review.md`
- `docs/design/global-design-freeze.md`
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
- `docs/architecture/verification-platforms.md`
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
- No implementation planning before `docs/architecture/verification-platforms.md` records the global platform scope, required evidence, and unsupported platforms with `N/A: <reason>`.
- No UX/UI approval from text alone; high-value screens require selected high-fidelity effect images or an explicit "no mockup needed" decision.
- No global visual direction approval before `@product-design ideate` provides three reviewable directions and one selected direction is recorded.
- No global effect-image generation before `docs/design/prompts/global-visual-direction-prompt.md` exists, is populated from the prompt template, maps every product requirement to PRD artifacts, and records the product-design-principle check.
- No global visual direction approval before its completed effect-image batch has an independent Mockup reviewer result, five prioritized findings or an explicit “no material issue” verdict, and the user's recorded decision to apply or decline the proposed changes.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, and page interaction order are recorded in `docs/plans/module-map.md`.
- No page implementation readiness from global high-fidelity direction alone; global mockups do not replace page-level design gates.
- No page-level high-fidelity mockup before the current page task has a low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- No page-level effect-image generation before `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md` exists, is populated from the prompt template, maps every page requirement to the PRD and approved design artifacts, and records the product-design-principle check.
- Do not generate or approve an effect image whose formal prompt invents a feature, user goal, content, state, commercial claim, or visual exception that conflicts with the PRD or approved product-design principles.
- No page design approval or design freeze before the completed page-level effect image has an independent Mockup reviewer result, five prioritized findings or an explicit “no material issue” verdict, and the user's recorded decision to apply or decline the proposed changes.
- Do not modify any effect image from an independent review without the user's explicit approval.
- No page UI implementation before the current page task has a reviewed low-fidelity structure, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/wireframe-spec.md`, page-level mockup approval, design freeze, and required asset atlas evidence.
- No implementation from raw Pencil images; Pencil wireframes or high-fidelity restorations must be converted into text specs and `docs/design/pencil-flutter-handoff.md`.
- No asset generation without global design-freeze constraints and page design-freeze constraints.
- No enhanced bitmap may be handed to Flutter implementation before the same output is synchronized to the corresponding design-draft asset or Pencil node and the updated design evidence is recorded. A bitmap enhancement includes upscaling, cleanup, relighting, recoloring, background removal, compositing, retouching, or other pixel-level changes.
- No high-fidelity Pencil restoration or Flutter UI implementation when required illustrations, bitmaps, logos, textures, generated images, or visual exports lack reuse check, production decision, bitmap source policy, background handling, background transparentization when applicable, transparent post-processing when applicable, asset atlas, generation evidence when used, slicing manifest, asset inventory, Flutter path, license status, and fidelity review.
- No UI completion claim before screenshots or Flutter golden evidence exist.
- No user-facing UI completion claim before `@product-design audit` findings are resolved or explicitly accepted in the review record.
- No task completion before `fvm flutter analyze`, relevant tests, and the applicable evidence required by the global verification platform scope are reported or explicitly marked unavailable with a blocker.
- No delivery completion while Critical or Important review findings remain open.
- No release claim before privacy, account, payment, crash reporting, analytics, and store checklist are checked or explicitly marked out of scope.

## Subagent Use

Use subagents for independent product, UX, architecture, review, and release checks. Do not dispatch multiple implementation agents against the same write scope. Read [references/subagent-map.md](references/subagent-map.md) before orchestrating subagents.

## Common Mistakes

- Treating a prototype as a commercial app.
- Letting the implementer self-approve UI quality.
- Treating a generated mockup as implementation truth without design-freeze constraints.
- Generating an effect image directly from an unsaved chat prompt instead of a formal prompt file traced to the PRD and product-design principles.
- Adding attractive but unscoped features, data, user goals, or visual exceptions to a prompt when they are absent from the PRD.
- Treating text-only UX/UI descriptions as sufficient for visual approval.
- Treating global high-fidelity direction as a substitute for page-level low-fidelity structure, Wireframe Review, and page mockup approval.
- Splitting modules only by code folders instead of product flow, data ownership, routing, and page interaction order.
- Generating page-level high-fidelity mockups before the page structure is reviewed and converted into text specs.
- Skipping asset atlas and slicing when the approved mockup contains required visual assets.
- Generating duplicate visual assets before checking existing brand, app, source, and inventory assets.
- Generating assets from the page mockup alone instead of global and page design-freeze constraints.
- Using Pencil whole-page screenshots or high-fidelity mockup crops as default bitmap sources instead of product-design or image generation output.
- Generating assets without deciding whether the output must be transparent, retained-background, or masked.
- Enhancing a bitmap only in the Flutter asset pipeline without replacing the corresponding asset in the design draft and capturing updated design evidence.
- Treating background transparentization as an implicit export step instead of a recorded work node with source, method, output, and reject/continue decision.
- Accepting transparent assets without alpha cleanup, edge halo checks, and target-background QA.
- Reading `.pen` files with normal filesystem tools instead of Pencil tools.
- Passing Pencil screenshots or restored Pencil frames directly to implementation agents instead of converting them into text specs.
- Skipping high-fidelity Pencil restoration when the user expects Pencil to carry the approved visual target.
- Treating bitmap or illustration details as implicit UI instead of tracked assets.
- Adding alternative state, result, JSON, or responsive-layout packages before checking the fixed stack.
- Running only unit tests for screen-heavy changes.
- Repeating platform scope in every task instead of maintaining `docs/architecture/verification-platforms.md` as the single source of truth.
- Claiming a platform is verified when its command, screenshot, golden, simulator, emulator, device, or browser evidence was not run or captured.
- Accepting vague words such as "premium", "simple", or "polished" without screen-level acceptance criteria.
