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
1. After the controller completes product questioning and records confirmed decisions, dispatch the Product/UX agent to draft `flutter-product-spec` artifacts, including the first-value moment, safe-to-try conditions, trust evidence, product character, measurable activation conditions, and a visual expression preset derived from category and audience via [../flutter-ux-ui-quality/references/visual-expression-presets.md](../flutter-ux-ui-quality/references/visual-expression-presets.md). The controller validates traceability and retains approval authority.
1.1. After the PRD artifacts are complete, dispatch the Market analysis agent to produce `docs/product/market-analysis.md` before global visual direction positioning.
1.2. After the product brief records the derived preset and before global visual direction positioning, ensure the light visual interrogation from the preset reference has been completed once (at most three questions, one at a time). If `flutter-product-spec` already recorded grilling-log answers and product-brief mirrors, do not re-ask; otherwise run it now. Do not create a per-page visual interrogation stage.
2. Dispatch the Product/UX agent to draft global UX/UI goals, flows, states, navigation model, and screen specifications with `flutter-ux-ui-quality`. Then dispatch the Global direction agent to use [references/global-visual-direction-prompt-template.md](references/global-visual-direction-prompt-template.md) transiently and define exactly three market-informed visual-system positions that satisfy the active preset mix. Dispatch a separate Global direction reviewer before the controller presents the three definitions to the user. No subagent may generate a page/screen image, recommend or select a direction, persist a freeze, or infer approval. The controller alone records the user's choice and advances to the freeze gate.
3. Freeze only the selected global visual-system direction. Run the Global Direction Freeze Gate one decision at a time: confirm the direction, acceptance of its signature and implementation-cost commitment, restatable signature or N/A reason, any `pin` / `raise` / `loosen` override, and explicit freeze intent. Re-enter full `grilling` only when the audit finds a new, conflicting, or unresolved decision; otherwise record why repeated full grilling is N/A. After confirmation, write `docs/design/prompts/global-visual-direction-prompt.md` and `docs/design/global-design-freeze.md`. The global freeze is a cross-page positioning baseline only: it contains no frozen page image and approves no module, page layout, page state, effect image, or implementation.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split coarse module boundaries and build order with `flutter-implementation-plan`; derive business-flow levels from the end-to-end user flow, module dependencies, and known page interaction order. Each known module and page must have a level, and delivery must complete and verify one level before advancing to the next; the plan must also account for the global verification platform scope. Do not prematurely freeze the detailed function and page task list for every module at this stage.

### Module Delivery

7. Execute modules with `flutter-subagent-delivery` and [references/subagent-map.md](references/subagent-map.md). The controller performs module questioning and confirmation, then dispatches the Module planner. Use `docs/design/app-design.pen` as the only project `.pen` file and serialize every subagent that can write it. For each UI page, dispatch the Page structure agent to select Full, Lightweight, or Reuse with [wireframe-level-standard.md](../flutter-pencil-design/references/wireframe-level-standard.md), then a separate Wireframe reviewer, the Page high-fidelity agent, and a separate Effect Image Reviewer in sequence. Require a reviewed semantic contract at every level, but require Pencil evidence only for Full. Require the Page high-fidelity agent to keep traceability in planning evidence and send only the compact final prompt defined by [image-prompt-principles.md](../flutter-hifi-mockup/references/image-prompt-principles.md). The controller alone presents candidates, records the user's selection/change disposition, persists the selected image, and freezes the page.
8. After page freeze, dispatch the Bitmap decomposition agent to apply [bitmap-decomposition-standard.md](../flutter-pencil-design/references/bitmap-decomposition-standard.md), write the ownership classification and coverage audit, and return unresolved facts. The agent must not generate or cut assets. The controller validates the zero-count gates before advancing.
9. When bitmap work is required, dispatch the Asset planning agent to prepare reuse decisions and the complete pre-slicing table. The controller presents the table and waits for explicit user confirmation. Only after confirmation dispatch the Asset production agent to produce confirmed rows, inventory, manifests, and fidelity evidence; reconfirm affected rows after material changes. Record `N/A: no bitmap or exported visual assets` when applicable.
10. When high-fidelity Pencil restoration is required, dispatch the Pencil restoration agent with the frozen page, restoration analysis, and confirmed assets. Validate its parity and Flutter handoff before dispatching the Implementer.
11. Dispatch independent Task reviewer and Visual QA agents for delivery review. For user-facing UI flows, dispatch the product-design audit role against screenshots before the controller records the final UX/UI verdict.
12. After every business-flow level is complete and all module/page functionality and high-fidelity restoration are implemented, run the final device runtime validation for every platform in `docs/architecture/verification-platforms.md`. Record device, emulator, simulator, browser, or desktop evidence only in this final integration stage.
13. Check store and business release readiness with `flutter-release-readiness`.
14. After a task passes its required checks and is explicitly confirmed, remove task-scoped temporary files, invalid or expired artifacts, and superseded unselected design drafts. Before deletion, verify that each candidate is not referenced by the current approved design, implementation, required workflow evidence, or user-provided source assets. Preserve the selected design, final assets, and required evidence; record deleted paths and any `N/A` cleanup decision in `.codex-workflow/progress.md`.
15. After cleanup, list exactly one next task.

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
- `docs/design/app-design.pen` as the only project `.pen` file
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
- `docs/plans/modules/<module-name>-scope.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`
- `.codex-workflow/decisions.md`
- `.codex-workflow/risks.md`
- `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` for a frozen page target
- `docs/release/release-checklist.md`

Use [references/artifacts.md](references/artifacts.md) for the artifact contract.

## Hard Gates

- No PRD confirmation, UX/UI direction, technical design, implementation plan, or delivery work before the initial `grilling` pass has recorded the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md`.
- When subagent tools are available, no delegable design-production stage may be silently executed by the controller instead of its assigned Product/UX, Market, Global direction, Page structure, Page high-fidelity, Bitmap decomposition, Asset planning/production, Pencil restoration, or Visual QA subagent. Record an explicit downgrade only when subagent tools are unavailable.
- No design producer may review or approve its own output. No subagent may ask the user for decisions, infer confirmation, select a candidate, or freeze/unfreeze an artifact.
- No project design may be written to a `.pen` file other than `docs/design/app-design.pen`. No two agents that can modify Pencil may run concurrently, even when their assigned node scopes differ.
- Before approving or executing a decision-bearing stage with unresolved scope, priority, tradeoffs, risks, acceptance criteria, or dependencies, re-enter `grilling` and record the user's explicit confirmation; do not block factual discovery, deterministic work, or already confirmed low-risk execution.
- No implementation before MVP scope and screen states exist.
- No UX/UI direction approval before the product brief defines a testable first-value moment, safe-to-try conditions, trust evidence, product character, and a derived visual expression preset; visual treatment must not be used to conceal an unresolved value or trust problem, and task clarity must not be lowered to satisfy expression.
- No global visual direction positioning before the light visual interrogation for the derived preset has been asked once and recorded, with signature and implementation-cost commitments mirrored in the product brief.
- No implementation before the Flutter project has the fixed plugin stack and a generated `flutter-dev` skill path recorded in `docs/architecture/flutter-init.md`.
- No implementation planning before `docs/architecture/verification-platforms.md` records the global platform scope, required evidence, and unsupported platforms with `N/A: <reason>`.
- Do not perform or claim device, emulator, simulator, browser, or desktop runtime verification during an individual module or page task. Defer it until all business-flow levels, module/page functionality, and required high-fidelity restoration are complete.
- No page UX/UI approval from text alone; high-value screens require selected page-level effect images or an explicit "no mockup needed" decision. This does not require an effect image for the global direction definition.
- No global visual direction freeze before exactly three market-informed direction definitions satisfy the active preset mix, the user selects one, and the Global Direction Freeze Gate confirms its signature, implementation-cost commitment, override, and freeze intent. Do not select automatically.
- Never generate or persist a page, representative-page, module, or screen effect image during global direction positioning. The global prompt and freeze define a visual system only; `.codex-workflow/visuals/global/` is forbidden.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, page interaction order, and business-flow levels for modules and pages are recorded in `docs/plans/module-map.md`.
- No module function refinement, page-function refinement, task brief, page design gate, or implementation before that module has completed its implementation-stage `grilling` pass, the user's explicit shared-understanding confirmation is appended to `docs/product/grilling-log.md`, and `docs/plans/modules/<module-name>-scope.md` records the confirmed included functions and non-goals.
- Module-level grilling must happen just in time when the module first becomes eligible for implementation. A global PRD confirmation or earlier implementation plan does not substitute for this gate.
- No task in a later business-flow level may start until every required task, acceptance path, and cross-module contract in the preceding level has passed or is explicitly accepted. Same-level work may run in parallel only when the module map marks it parallel-safe.
- No page implementation readiness from the global direction definition alone; it does not replace module effect-image interrogation or page-level design gates.
- The global design freeze is a reusable visual-system baseline only and contains no effect image.
- No module page effect-image generation before the module's function/page refinement and Module Effect-Image Interrogation Gate are confirmed and recorded. Do not repeat the gate per page unless a new visual or cost decision appears.
- No page-level high-fidelity mockup before the current page task records a justified Full, Lightweight, or Reuse level, passes independent Wireframe Review, and has `docs/design/wireframe-spec.md`. Require low-fidelity Pencil evidence only for Full; Lightweight may use a text contract and Reuse may use an approved-pattern delta contract.
- No page-level effect-image generation before a transient formal prompt prepared from the page prompt template maps every page requirement to the PRD and approved design artifacts, records the active expression preset and page-type budget dial, and records the product-design-principle check. Persist it only after freeze confirmation.
- No image generation from the full planning worksheet, PRD mapping, design rationale, exhaustive component specification, or accumulated avoid list. The actual prompt must be the shortest coherent version that preserves outcome, essential structure/content, approved direction, true non-negotiables, and output requirements; it must contain no duplicate or contradictory instruction and must leave non-frozen secondary details open.
- Do not generate or approve an effect image whose formal prompt invents a feature, user goal, content, state, commercial claim, or visual exception that conflicts with the PRD or approved product-design principles.
- No page design approval or design freeze before the completed page-level effect image has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements judged against the active expression preset and page-type budget dial rather than universal restraint, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. On full-budget or wow-required pages, missing restatable signature is a blocking Important finding unless explicitly accepted. Review output is transient and must not be saved as a repository artifact.
- No page visual write before explicit page freeze confirmation. At freeze, persist the exact selected image under `.codex-workflow/visuals/pages/<page-name>/` before any related page prompt, brief, design-freeze, or ledger write; record the frozen path, candidate ID, decoded dimensions, SHA-256, and confirmation time.
- Do not modify any effect image from an independent review without the user's explicit approval.
- No page UI implementation before the current page task has a reviewed low-fidelity semantic contract, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- For high-fidelity generation and Pencil restoration, the selected page-level effect image and page design freeze control all visual details. A low-fidelity contract may define scope, required content, priority, tasks, states, navigation, interactions, outcomes, accessibility meaning, and ownership, but must not freeze or override exact geometry, containers, whitespace, component silhouettes, image ratios/crops, or decoration placement.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/wireframe-spec.md`, page-level mockup approval, design freeze, and a recorded effect-image analysis that assigns every restorable layer or atomic unit to bitmap, UI, or data.
- No high-fidelity Pencil restoration approval or Flutter handoff for an affected unit while a material visual uncertainty is unresolved; record it and obtain a decision instead of guessing.
- No UI bitmap fill or asset generation before the analysis records why native Flutter cannot reproduce the UI unit exactly. No bitmap restoration may be accepted before its source, crop, size, background treatment, target Pencil node, and 100% visual-content match verdict are recorded; only documented rasterization or scaling tolerance is allowed.
- No icon, image, illustration, logo, texture, or other visual resource may be restored with a near match. When its approved visual content cannot be verified as a 100% match, the task must generate a dedicated bitmap and complete the asset-atlas and fidelity-review flow before Pencil restoration or Flutter implementation.
- No page decomposition may enter Pencil restoration or Flutter implementation until every bitmap unit has a recorded separate-asset review verdict: reuse, adapt, generate, approved Pencil-node export, explicit mockup extraction, or `N/A: native Flutter/UI/data`.
- No decomposition may pass while a runtime-data visual is marked for bitmap export, a visible element lacks ownership, or a background decoration or icon placement/state is absent from the coverage audit.
- No bitmap generation, adaptation, extraction, export, transparentization, or slicing before the complete pre-slicing table is shown inline and explicitly confirmed. A material row change invalidates confirmation for that row and blocks work until reconfirmed.
- No high-fidelity Pencil restoration before required bitmap or bitmap-fill requirements have asset atlas evidence, or before a no-bitmap analysis has recorded the required `N/A` decision.
- No implementation from raw Pencil images; Pencil wireframes or high-fidelity restorations must be converted into text specs and `docs/design/pencil-flutter-handoff.md`.
- No asset generation without global design-freeze constraints and page design-freeze constraints.
- No enhanced bitmap may be handed to Flutter implementation before the same output is synchronized to the corresponding design-draft asset or Pencil node and the updated design evidence is recorded. A bitmap enhancement includes upscaling, cleanup, relighting, recoloring, background removal, compositing, retouching, or other pixel-level changes.
- No high-fidelity Pencil restoration or Flutter UI implementation when required illustrations, bitmaps, logos, textures, generated images, or visual exports lack reuse check, production decision, bitmap source policy, background handling, background transparentization when applicable, transparent post-processing when applicable, asset atlas, generation evidence when used, slicing manifest, asset inventory, Flutter path, license status, and fidelity review.
- No UI completion claim before screenshots or Flutter golden evidence exist.
- No user-facing UI completion before `flutter-quality-review` records an aesthetic verdict against the approved mockup and design-freeze constraints; Critical or Important aesthetic findings must be resolved or explicitly accepted.
- No user-facing UI completion claim before `@product-design audit` findings are resolved or explicitly accepted in the review record.
- No task completion before `fvm flutter analyze`, relevant tests, and required non-runtime design evidence are reported or explicitly marked unavailable with a blocker. Runtime platform evidence is a final-integration gate, not a module/page-task gate.
- No final delivery or release-readiness claim before every in-scope platform has completed its final device, emulator, simulator, browser, or desktop runtime validation after all modules and pages are implemented.
- No next-task handoff before the confirmed task has completed its scoped cleanup or recorded `N/A` in `.codex-workflow/progress.md`.
- No delivery completion while Critical or Important review findings remain open.
- No release claim before privacy, account, payment, crash reporting, analytics, and store checklist are checked or explicitly marked out of scope.

## Subagent Use

Use subagents for delegable product/UX drafting, market analysis, visual-direction production and review, page structure, wireframe review, high-fidelity generation and review, bitmap decomposition, asset planning and production, Pencil restoration, implementation, visual QA, architecture, and release checks. The controller retains user interaction, decisions, freezes, conflict resolution, sequencing, and integration. Do not dispatch agents against overlapping write scopes. Read [references/subagent-map.md](references/subagent-map.md) and [design-subagent-orchestration.md](../flutter-subagent-delivery/references/design-subagent-orchestration.md) before dispatch.

## Common Mistakes

- Treating a prototype as a commercial app.
- Letting the implementer self-approve UI quality.
- Treating a generated mockup as implementation truth without design-freeze constraints.
- Generating an effect image without a formal transient prompt traced to the PRD and product-design principles, or writing that prompt and candidate visual files before the user confirms a freeze.
- Adding attractive but unscoped features, data, user goals, or visual exceptions to a prompt when they are absent from the PRD.
- Treating text-only UX/UI descriptions as sufficient for visual approval.
- Generating a representative-page or other effect image during global direction positioning.
- Treating the global direction freeze as a substitute for module effect-image interrogation, a reviewed low-fidelity semantic contract, Wireframe Review, or page mockup approval.
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
- Creating separate `.pen` files for pages, modules, fidelity stages, candidates, temporary work, exports, backups, or restorations instead of organizing them as sections and stable nodes in `docs/design/app-design.pen`.
- Passing Pencil screenshots or restored Pencil frames directly to implementation agents instead of converting them into text specs.
- Skipping high-fidelity Pencil restoration when the user expects Pencil to carry the approved visual target.
- Treating bitmap or illustration details as implicit UI instead of tracked assets.
- Restoring an approved effect image without first separating bitmap, UI, and data, or generating a UI bitmap before confirming that native Flutter cannot reproduce it exactly.
- Adding alternative state, result, JSON, or responsive-layout packages before checking the fixed stack.
- Running only unit tests for screen-heavy changes.
- Repeating platform scope in every task instead of maintaining `docs/architecture/verification-platforms.md` as the single source of truth.
- Claiming a platform is verified when its command, screenshot, golden, simulator, emulator, device, or browser evidence was not run or captured.
- Accepting vague words such as "premium", "simple", or "polished" without screen-level acceptance criteria.
- Defaulting every product to restrained professional visuals instead of deriving a visual expression preset from category and audience.
- Skipping the one-time light visual interrogation before global exploration, or running a per-page visual interrogation stage.
- Skipping the module effect-image interrogation before page effect generation, or mechanically repeating it for every page without a new decision.
- Freezing a global direction that lacks a restatable signature when the preset requires one.
- Retaining temporary files, invalid or expired artifacts, or superseded unselected design drafts after task confirmation without checking whether they are still required as approved or audit evidence.
