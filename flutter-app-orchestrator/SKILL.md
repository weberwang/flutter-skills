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

0. Run `grilling` before PRD confirmation. When no PRD exists, grill the product assumptions before `flutter-product-spec`; when PRD artifacts already exist, grill their decisions, gaps, conflicts, and dependencies before continuing. Do not proceed until the user explicitly confirms shared understanding and `docs/product/grilling-log.md` records the result.
0.1. Before starting or approving any decision-bearing stage, assess whether scope, priority, tradeoffs, risks, acceptance criteria, or dependencies remain for the user to decide. If so, re-enter `grilling`, record the user's confirmation, then continue from the interrupted stage. Do not invoke it for factual discovery, deterministic work, or already confirmed low-risk execution.
1. Define the product with `flutter-product-spec`, including the first-value moment, safe-to-try conditions, trust evidence, product character, and measurable activation conditions.
1.1. After the PRD artifacts are complete, conduct market analysis and save `docs/product/market-analysis.md` before global visual exploration.
2. Draft global UX/UI goals, flows, states, navigation model, and design-system direction with `flutter-ux-ui-quality`. The brief must show how the first-value moment is reached, how the user can safely try the product, and how the visual system conveys the approved product character without using decoration as a substitute for clarity. Use [references/global-visual-direction-prompt-template.md](references/global-visual-direction-prompt-template.md) to create and save `docs/design/prompts/global-visual-direction-prompt.md`, which defines the three-direction comparison and its PRD and market-analysis alignment. Use the PRD and `docs/product/market-analysis.md` to recommend exactly three candidate directions for effect-image generation; derive categories from the product, market opportunity, category conventions, and differentiation opportunities, so the template examples are optional references rather than a fixed set. When the exploration needs a representative page to generate effect images, choose it autonomously from the highest-priority PRD user task, high-value moment, first-value proof, and information needed to distinguish the directions; record the selected page and rationale in the global prompt file. Do not use the global template as the image-generation prompt. Instead, fill [references/page-hifi-mockup-prompt-template.md](references/page-hifi-mockup-prompt-template.md) for each recommended candidate direction in the generation context, without saving a page-prompt file, then use it to generate comparable images. Keep the representative page, device, information structure, copy, data, and state identical across all directions; vary only the approved visual-direction fields. Trace every product claim, task, state, content constraint, and acceptance criterion to the PRD artifacts and market-analysis findings; document the product-design-principle check in the global prompt file. Run `@product-design user-context` preflight followed by `@product-design get-context` and `@product-design ideate` to produce the three recommended directions and their effect images. List the candidates and wait for the user to explicitly choose and confirm one; do not select a direction automatically.
3. Confirm global UX/UI direction with high-fidelity effect images using `flutter-hifi-mockup`. After the effect-image batch is complete, automatically dispatch exactly one Effect Image Reviewer with the images, product brief, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Use Apple Human Interface Guidelines as the interaction baseline. Present two separate sections inline: product-design issues with concrete fixes, then premium-feel improvements; list the candidate directions with their combined review results, then wait for the user to choose and confirm one direction and whether to apply the proposed changes. Do not save the review as a repository artifact. Do not revise, select, or freeze a direction until the user explicitly confirms it. Use `@product-design image-to-code` only when the selected visual target has interaction ambiguity that needs a review-only prototype. This confirms visual direction and design-system intent only; the resulting global design freeze and representative-page effect images must not confirm any later page mockup, page design freeze, or implementation readiness.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split modules and build order with `flutter-implementation-plan`; the plan must account for module dependencies, page interaction order, and the global verification platform scope.

### Module Delivery

7. Execute tasks with `flutter-subagent-delivery`; each UI module or page task must first create a low-fidelity Pencil structure, pass Wireframe Review, and convert it into text specs. Before generating any page-level effect image, use [references/page-hifi-mockup-prompt-template.md](references/page-hifi-mockup-prompt-template.md) to create and save `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`. Trace every page task, module, state, copy, data, interaction, and visual constraint to the PRD and approved design artifacts; document the product-design-principle check in the same file; then use that saved prompt file to generate the page-level high-fidelity effect image. After the image is complete, automatically dispatch exactly one Effect Image Reviewer with the image, wireframe spec, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Use Apple Human Interface Guidelines as the interaction baseline and present product-design issues with concrete fixes separately from premium-feel improvements. Do not save the review as a repository artifact. Do not revise, approve, or freeze the page design until the user explicitly approves changes or explicitly accepts the current result.
8. Before deciding visual-asset work or restoring an approved high-fidelity effect image into Pencil, analyze each restorable layer or atomic unit and record one mutually exclusive category in `docs/design/pencil-hifi-restoration.md`: bitmap, UI, or data. Split composite elements into their bitmap, UI, and data units before classification. Restore data with editable text and representative placeholders that preserve the approved information hierarchy, text length, and layout; production data is not required for visual restoration, and a data unit must never trigger bitmap generation or extraction. Before proceeding, record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess asset provenance, font or icon sources, component states, crop rules, or hidden interactions. For every bitmap, record its source, crop, size, background treatment, and target node, then require a 100% match of the approved visual content; only documented rasterization or scaling tolerance is allowed. For every UI unit, record the native-Flutter feasibility reason and expected implementation approach. Use native Flutter when it can reproduce the unit exactly; otherwise record the bitmap-fill requirement and generate the required bitmap before restoration. Confirm the native-Flutter decision with implementation screenshot or golden evidence. Do not generate a bitmap for UI that native Flutter can reproduce exactly.
9. After the analysis identifies a bitmap or bitmap-fill requirement, use `flutter-asset-atlas` for its reuse check, production decision, generation or enhancement, slicing, export, inventory, and fidelity review. New bitmap generation must use product-design or image generation tools by default and follow the global design freeze and page design freeze. Treat bitmap enhancement as a design change: replace the corresponding asset in the design draft, preserve the approved layout and constraints, and record the updated design evidence before implementation. When the analysis identifies no bitmap or bitmap fill, record `N/A: no bitmap or exported visual assets` in the task brief and `.codex-workflow/progress.md`.
10. Decide whether Pencil high-fidelity restoration is required. Restore the page in Pencil when required, including every bitmap and bitmap fill identified by the analysis, then implement the Flutter page from text specs and handoff artifacts.
11. Review delivery with `flutter-quality-review`; for user-facing UI flows, run `@product-design audit` against screenshots before the final UX/UI verdict.
12. Check store and business release readiness with `flutter-release-readiness`.
13. After a task passes its required checks and is explicitly confirmed, remove task-scoped temporary files, invalid or expired artifacts, and superseded unselected design drafts. Before deletion, verify that each candidate is not referenced by the current approved design, implementation, required workflow evidence, or user-provided source assets. Preserve the selected design, final assets, and required evidence; record deleted paths and any `N/A` cleanup decision in `.codex-workflow/progress.md`.
14. After cleanup, list exactly one next task.

## Required Artifacts

Create or update these files in the target app repo:

- `docs/product/product-brief.md`
- `docs/product/grilling-log.md`
- `docs/product/mvp-scope.md`
- `docs/product/user-stories.md`
- `docs/product/market-analysis.md`
- `docs/design/user-flows.md`
- `docs/design/screen-spec.md`
- `docs/design/ui-quality-gates.md`
- `docs/design/mockup-brief.md`
- `docs/design/prompts/global-visual-direction-prompt.md`
- `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`
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

- No PRD confirmation, UX/UI direction, technical design, implementation plan, or delivery work before the initial `grilling` pass has recorded the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md`.
- Before approving or executing a decision-bearing stage with unresolved scope, priority, tradeoffs, risks, acceptance criteria, or dependencies, re-enter `grilling` and record the user's explicit confirmation; do not block factual discovery, deterministic work, or already confirmed low-risk execution.
- No implementation before MVP scope and screen states exist.
- No UX/UI direction approval before the product brief defines a testable first-value moment, safe-to-try conditions, trust evidence, and product character; visual treatment must not be used to conceal an unresolved value or trust problem.
- No implementation before the Flutter project has the fixed plugin stack and a generated `flutter-dev` skill path recorded in `docs/architecture/flutter-init.md`.
- No implementation planning before `docs/architecture/verification-platforms.md` records the global platform scope, required evidence, and unsupported platforms with `N/A: <reason>`.
- No UX/UI approval from text alone; high-value screens require selected high-fidelity effect images or an explicit "no mockup needed" decision.
- No global visual direction approval before `@product-design ideate` provides three market-informed reviewable directions, the candidates are listed for the user, and the user's explicit selected direction is recorded. Do not select a direction automatically.
- No global effect-image generation before `docs/product/market-analysis.md` exists and `docs/design/prompts/global-visual-direction-prompt.md` is populated from the global prompt template, maps every product requirement to PRD artifacts and every direction rationale to market-analysis findings, and records the product-design-principle check.
- No representative-page effect-image generation during global visual exploration before the global prompt file records an autonomously selected representative page, its PRD-based rationale, and the shared device, information structure, copy, data, and state. Use the page high-fidelity prompt template for each candidate direction in the generation context; do not save a separate representative-page prompt file.
- No global visual direction approval before its completed effect-image batch has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. Review output is transient and must not be saved as a repository artifact.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, and page interaction order are recorded in `docs/plans/module-map.md`.
- No page implementation readiness from global high-fidelity direction alone; global mockups do not replace page-level design gates.
- The global design freeze is a reusable visual-system baseline only. Its representative-page effect images must not be reused as confirmation for a later page, including when that page has the same route or a similar state.
- No page-level high-fidelity mockup before the current page task has a low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- No page-level effect-image generation before `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md` exists, is populated from the prompt template, maps every page requirement to the PRD and approved design artifacts, and records the product-design-principle check.
- Do not generate or approve an effect image whose formal prompt invents a feature, user goal, content, state, commercial claim, or visual exception that conflicts with the PRD or approved product-design principles.
- No page design approval or design freeze before the completed page-level effect image has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. Review output is transient and must not be saved as a repository artifact.
- Do not modify any effect image from an independent review without the user's explicit approval.
- No page UI implementation before the current page task has a reviewed low-fidelity structure, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/wireframe-spec.md`, page-level mockup approval, design freeze, and a recorded effect-image analysis that assigns every restorable layer or atomic unit to bitmap, UI, or data.
- No high-fidelity Pencil restoration approval or Flutter handoff for an affected unit while a material visual uncertainty is unresolved; record it and obtain a decision instead of guessing.
- No UI bitmap fill or asset generation before the analysis records why native Flutter cannot reproduce the UI unit exactly. No bitmap restoration may be accepted before its source, crop, size, background treatment, target Pencil node, and 100% visual-content match verdict are recorded; only documented rasterization or scaling tolerance is allowed.
- No high-fidelity Pencil restoration before required bitmap or bitmap-fill requirements have asset atlas evidence, or before a no-bitmap analysis has recorded the required `N/A` decision.
- No implementation from raw Pencil images; Pencil wireframes or high-fidelity restorations must be converted into text specs and `docs/design/pencil-flutter-handoff.md`.
- No asset generation without global design-freeze constraints and page design-freeze constraints.
- No enhanced bitmap may be handed to Flutter implementation before the same output is synchronized to the corresponding design-draft asset or Pencil node and the updated design evidence is recorded. A bitmap enhancement includes upscaling, cleanup, relighting, recoloring, background removal, compositing, retouching, or other pixel-level changes.
- No high-fidelity Pencil restoration or Flutter UI implementation when required illustrations, bitmaps, logos, textures, generated images, or visual exports lack reuse check, production decision, bitmap source policy, background handling, background transparentization when applicable, transparent post-processing when applicable, asset atlas, generation evidence when used, slicing manifest, asset inventory, Flutter path, license status, and fidelity review.
- No UI completion claim before screenshots or Flutter golden evidence exist.
- No user-facing UI completion before `flutter-quality-review` records an aesthetic verdict against the approved mockup and design-freeze constraints; Critical or Important aesthetic findings must be resolved or explicitly accepted.
- No user-facing UI completion claim before `@product-design audit` findings are resolved or explicitly accepted in the review record.
- No task completion before `fvm flutter analyze`, relevant tests, and the applicable evidence required by the global verification platform scope are reported or explicitly marked unavailable with a blocker.
- No next-task handoff before the confirmed task has completed its scoped cleanup or recorded `N/A` in `.codex-workflow/progress.md`.
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
- Restoring an approved effect image without first separating bitmap, UI, and data, or generating a UI bitmap before confirming that native Flutter cannot reproduce it exactly.
- Adding alternative state, result, JSON, or responsive-layout packages before checking the fixed stack.
- Running only unit tests for screen-heavy changes.
- Repeating platform scope in every task instead of maintaining `docs/architecture/verification-platforms.md` as the single source of truth.
- Claiming a platform is verified when its command, screenshot, golden, simulator, emulator, device, or browser evidence was not run or captured.
- Accepting vague words such as "premium", "simple", or "polished" without screen-level acceptance criteria.
- Retaining temporary files, invalid or expired artifacts, or superseded unselected design drafts after task confirmation without checking whether they are still required as approved or audit evidence.
