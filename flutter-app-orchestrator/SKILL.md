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
1. Define the product with `flutter-product-spec`, including the first-value moment, safe-to-try conditions, trust evidence, product character, measurable activation conditions, and a visual expression preset derived from category and audience via [../flutter-ux-ui-quality/references/visual-expression-presets.md](../flutter-ux-ui-quality/references/visual-expression-presets.md).
1.1. After the PRD artifacts are complete, conduct market analysis and save `docs/product/market-analysis.md` before global visual exploration.
1.2. After the product brief records the derived preset and before global visual exploration, ensure the light visual interrogation from the preset reference has been completed once (at most three questions, one at a time). If `flutter-product-spec` already recorded grilling-log answers and product-brief mirrors, do not re-ask; otherwise run it now. Do not create a per-page visual interrogation stage.
2. Draft global UX/UI goals, flows, states, navigation model, and design-system direction with `flutter-ux-ui-quality`. The brief must show how the first-value moment is reached, how the user can safely try the product, and how the visual system conveys the approved product character and expression preset without using decoration as a substitute for clarity. Use [references/global-visual-direction-prompt-template.md](references/global-visual-direction-prompt-template.md) to prepare a transient formal prompt that defines the three-direction comparison, its PRD and market-analysis alignment, and the active visual expression preset with required direction mix and scoring weights. Use the PRD, preset, and `docs/product/market-analysis.md` to recommend exactly three candidate directions and generate comparable effect images with the available image-generation capability. Keep the representative page, device, required content, copy, data, user task, and state identical across all directions so comparison remains fair; allow composition, grouping, visual rhythm, component silhouette, imagery, material, and motion intent to vary without changing product meaning. Do not require an external visual-design skill; if image generation is unavailable, record a blocker and do not fabricate visual evidence. Present the candidates and wait for the user to explicitly choose and confirm one; do not select a direction automatically.
3. Confirm global UX/UI direction with high-fidelity effect images using `flutter-hifi-mockup`. After the effect-image batch is complete, automatically dispatch exactly one Effect Image Reviewer with the images, product brief, active expression preset, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Use Apple Human Interface Guidelines as the interaction baseline. Present product-design issues and premium-feel improvements separately, then wait for the user to choose and confirm one direction. Record candidate IDs, prompt hashes, review verdict, confirmation time, and the selected image SHA-256 in `docs/tasks/<task-id>/evidence/visual-decision.md`; do not retain unselected raw images unless the user requests it. After confirmation, copy the exact selected image to `.codex-workflow/visuals/global/frozen-<slug>.png` first, then write `docs/design/global/` artifacts and ledger entries. Use an optional local review-only prototype only when a selected visual target has interaction ambiguity. This confirms visual direction and design-system intent only; it must not confirm a later page mockup, page design freeze, or implementation readiness.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split modules and build order with `flutter-implementation-plan`; derive business-flow levels from the end-to-end user flow, module dependencies, and page interaction order. Each module and page must have a level, and delivery must complete and verify one level before advancing to the next; the plan must also account for the global verification platform scope.

### Module Delivery

7. Execute tasks with `flutter-subagent-delivery`; each UI module or page task must first create a low-fidelity Pencil structure, pass Wireframe Review, and convert it into text specs. Keep page artifacts in `docs/design/pages/<page-name>/` and task evidence in `docs/tasks/<task-id>/`. Before generating a page-level effect image, prepare the page prompt transiently, including the active expression preset and page-type budget dial, then generate it with the available image-generation capability. Full-budget pages must pursue the preset signature; settings, forms, permissions, account, error, and legal pages dial decoration down while keeping system consistency. After the image is complete, dispatch exactly one Effect Image Reviewer with the image, wireframe spec, active preset, page-type dial, and review template. Do not revise, approve, or freeze the page design until the user explicitly approves changes or explicitly accepts the current result. After freeze confirmation, persist the exact selected image to `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` first, then write the page artifacts and visual-decision evidence with its candidate ID, decoded dimensions, SHA-256, prompt hash, review verdict, and confirmation time.
8. Use the selected page-level high-fidelity effect image and `docs/design/pages/<page-name>/design-freeze.md` as the sole visual source of truth for Pencil high-fidelity restoration; the wireframe remains a scope, structure, state, and interaction prerequisite only. Before deciding visual-asset work or restoring the approved image into Pencil, analyze each restorable layer or atomic unit and record one mutually exclusive category in `docs/design/pages/<page-name>/pencil-hifi-restoration.md`: bitmap, UI, or data. Split composite elements into their bitmap, UI, and data units before classification, then review each bitmap unit for a separate production asset decision. For every icon, image, illustration, logo, texture, or other visual resource, verify a 100% match to the approved visual content. Reuse, adapt, approved Pencil-node export, or explicit mockup extraction is allowed only when that exact-match evidence exists; otherwise the mandatory verdict is `generate`, followed by independent image generation, asset-atlas, and fidelity review. Never substitute a near match. Restore data with editable text and representative placeholders; data must never trigger bitmap generation or extraction. Record unresolved visual facts and native-Flutter feasibility in the page artifact before handoff.
9. After the analysis identifies a bitmap or bitmap-fill requirement, use `flutter-asset-atlas` for its reuse check, production decision, generation or enhancement, slicing, export, inventory, and fidelity review. New bitmap generation must use the available image-generation capability and follow the global and page design freeze. Treat bitmap enhancement as a design change: replace the corresponding asset in the design draft, preserve the approved layout and constraints, and record the updated design evidence before implementation. When the analysis identifies no bitmap or bitmap fill, record `N/A: no bitmap or exported visual assets` in the task brief and evidence manifest.
10. Decide whether Pencil high-fidelity restoration is required. Restore the page in Pencil when required, including every bitmap and bitmap fill identified by the analysis, then implement the Flutter page from text specs and handoff artifacts.
11. Review delivery with `flutter-quality-review`; for user-facing UI flows, run an independent visual-QA review against screenshots before the final UX/UI verdict.
12. After every business-flow level is complete and all module/page functionality and high-fidelity restoration are implemented, run the final device runtime validation for every platform in `docs/architecture/verification-platforms.md`. Record device, emulator, simulator, browser, or desktop evidence only in this final integration stage.
13. Check store and business release readiness with `flutter-release-readiness`.
14. After a task passes its required checks and is explicitly confirmed, remove only that task worktree's temporary files, invalid or expired artifacts, and superseded unselected design drafts. Before deletion, verify that each candidate is not referenced by the current approved design, implementation, required workflow evidence, or user-provided source assets. Preserve the selected design, final assets, and the task visual-decision record; record deleted paths and any `N/A` cleanup decision in `docs/tasks/<task-id>/evidence/manifest.md`.
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
- `docs/design/global/mockup-brief.md`
- `docs/design/global/prompts/visual-direction-prompt.md`
- `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`
- `docs/design/global/design-freeze.md`
- `docs/design/pages/<page-name>/pencil-intake.md`
- `docs/design/pages/<page-name>/pencil-flutter-handoff.md`
- `docs/design/pages/<page-name>/pencil-hifi-restoration.md`
- `docs/design/pages/<page-name>/wireframe-review.md`
- `docs/design/pages/<page-name>/wireframe-spec.md`
- `docs/design/pages/<page-name>/pencil-parity-review.md`
- `docs/design/pages/<page-name>/asset-atlas.md`
- `docs/design/pages/<page-name>/asset-slicing-manifest.md`
- `docs/design/pages/<page-name>/asset-fidelity-review.md`
- `docs/design/pages/<page-name>/asset-inventory.md`
- `docs/design/pages/<page-name>/design-freeze.md`
- `docs/architecture/flutter-init.md`
- `docs/architecture/verification-platforms.md`
- `docs/architecture/technical-design.md`
- `docs/plans/module-map.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`
- `.codex-workflow/decisions.md`
- `.codex-workflow/risks.md`
- `.codex-workflow/tasks/<task-id>.yaml`
- `docs/tasks/<task-id>/brief.md`
- `docs/tasks/<task-id>/evidence/manifest.md`
- `.codex-workflow/visuals/global/frozen-<slug>.png` for a frozen global direction
- `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` for a frozen page target
- `docs/release/release-checklist.md`

Use [references/artifacts.md](references/artifacts.md) for the artifact contract.

## Hard Gates

- No PRD confirmation, UX/UI direction, technical design, implementation plan, or delivery work before the initial `grilling` pass has recorded the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md`.
- Before approving or executing a decision-bearing stage with unresolved scope, priority, tradeoffs, risks, acceptance criteria, or dependencies, re-enter `grilling` and record the user's explicit confirmation; do not block factual discovery, deterministic work, or already confirmed low-risk execution.
- No implementation before MVP scope and screen states exist.
- No UX/UI direction approval before the product brief defines a testable first-value moment, safe-to-try conditions, trust evidence, product character, and a derived visual expression preset; visual treatment must not be used to conceal an unresolved value or trust problem, and task clarity must not be lowered to satisfy expression.
- No global visual exploration before the light visual interrogation for the derived preset has been asked once and recorded, with signature and implementation-cost commitments mirrored in the product brief.
- No implementation before the Flutter project has the fixed plugin stack and a generated `flutter-dev` skill path recorded in `docs/architecture/flutter-init.md`.
- No implementation planning before `docs/architecture/verification-platforms.md` records the global platform scope, required evidence, and unsupported platforms with `N/A: <reason>`.
- Do not claim a platform verified during an individual module or page task. After each business-flow level merges to the integration branch, run the planned integration smoke; run the full device, emulator, simulator, browser, and desktop matrix only after all modules/pages and high-fidelity restoration are complete.
- No UX/UI approval from text alone; high-value screens require selected high-fidelity effect images or an explicit "no mockup needed" decision.
- No global visual direction approval before the available image-generation capability provides three market-informed reviewable directions that satisfy the active preset’s required direction mix, the candidates are listed for the user, and the user's explicit selected direction is recorded. Do not select a direction automatically. Apply the Global Freeze Signature Rule from [../flutter-ux-ui-quality/references/visual-expression-presets.md](../flutter-ux-ui-quality/references/visual-expression-presets.md): when it applies, require an explicit restatable-signature confirmation and do not freeze if the answer is no; when it does not apply, record the N/A reason using the selected direction’s distinctive mix trait.
- No global effect-image generation before `docs/product/market-analysis.md` exists and a transient formal prompt prepared from the global prompt template maps every product requirement to PRD artifacts and every direction rationale to market-analysis findings, records the active visual expression preset with direction-mix, scoring-weight rules, and light-interrogation commitments, and records the product-design-principle check. Persist that prompt only after freeze confirmation.
- No representative-page effect-image generation during global visual exploration before the global prompt file records an autonomously selected representative page, its PRD-based rationale, and the shared device, required content, copy, data, user task, and state. Candidate directions may vary composition, grouping, visual rhythm, component silhouette, imagery, material, and motion intent without changing product meaning. Use the page high-fidelity prompt template for each candidate direction in the generation context; do not save a separate representative-page prompt file.
- No global visual direction approval before its completed effect-image batch has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements judged against the active expression preset’s signature strength and wow requirement rather than universal restraint, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. Keep the minimal review verdict, candidate IDs, prompt hashes, and selected image hash in the task visual-decision record.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, page interaction order, and business-flow levels for modules and pages are recorded in `docs/plans/module-map.md`.
- No task in a later business-flow level may start until every required task, acceptance path, and cross-module contract in the preceding level has passed or is explicitly accepted. Same-level work may run in parallel only when the module map marks it parallel-safe.
- No page implementation readiness from global high-fidelity direction alone; global mockups do not replace page-level design gates.
- The global design freeze is a reusable visual-system baseline only. Its representative-page effect images must not be reused as confirmation for a later page, including when that page has the same route or a similar state.
- No page-level high-fidelity mockup before the current page task has a low-fidelity Pencil structure, Wireframe Review, and `docs/design/pages/<page-name>/wireframe-spec.md`.
- No page-level effect-image generation before a transient formal prompt prepared from the page prompt template maps every page requirement to the PRD and approved design artifacts, records the active expression preset and page-type budget dial, and records the product-design-principle check. Persist it only after freeze confirmation.
- Do not generate or approve an effect image whose formal prompt invents a feature, user goal, content, state, commercial claim, or visual exception that conflicts with the PRD or approved product-design principles.
- No page design approval or design freeze before the completed page-level effect image has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements judged against the active expression preset and page-type budget dial rather than universal restraint, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. On full-budget or wow-required pages, missing restatable signature is a blocking Important finding unless explicitly accepted. Keep the minimal decision record in `docs/tasks/<task-id>/evidence/visual-decision.md`.
- No repository visual write before explicit freeze confirmation. At freeze, persist the exact selected image under `.codex-workflow/visuals/<scope>/` before any related prompt, brief, design-freeze, or ledger write; record the frozen path, candidate ID, decoded dimensions, SHA-256, and confirmation time in the design freeze and ledger.
- Do not modify any effect image from an independent review without the user's explicit approval.
- No page UI implementation before the current page task has a reviewed low-fidelity structure, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- For high-fidelity Pencil restoration, the selected page-level effect image and page design freeze control all visual details. A low-fidelity wireframe may define scope, structure, states, and interactions, but must not replace or override the approved visual target.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/pages/<page-name>/wireframe-spec.md`, page-level mockup approval, page design freeze, and a recorded effect-image analysis that assigns every restorable layer or atomic unit to bitmap, UI, or data.
- No high-fidelity Pencil restoration approval or Flutter handoff for an affected unit while a material visual uncertainty is unresolved; record it and obtain a decision instead of guessing.
- No UI bitmap fill or asset generation before the analysis records why native Flutter cannot reproduce the UI unit exactly. No bitmap restoration may be accepted before its source, crop, size, background treatment, target Pencil node, and 100% visual-content match verdict are recorded; only documented rasterization or scaling tolerance is allowed.
- No icon, image, illustration, logo, texture, or other visual resource may be restored with a near match. When its approved visual content cannot be verified as a 100% match, the task must generate a dedicated bitmap and complete the asset-atlas and fidelity-review flow before Pencil restoration or Flutter implementation.
- No page decomposition may enter Pencil restoration or Flutter implementation until every bitmap unit has a recorded separate-asset review verdict: reuse, adapt, generate, approved Pencil-node export, explicit mockup extraction, or `N/A: native Flutter/UI/data`.
- No high-fidelity Pencil restoration before required bitmap or bitmap-fill requirements have asset atlas evidence, or before a no-bitmap analysis has recorded the required `N/A` decision.
- No implementation from raw Pencil images; Pencil wireframes or high-fidelity restorations must be converted into text specs and `docs/design/pages/<page-name>/pencil-flutter-handoff.md`.
- No asset generation without global design-freeze constraints and page design-freeze constraints.
- No enhanced bitmap may be handed to Flutter implementation before the same output is synchronized to the corresponding design-draft asset or Pencil node and the updated design evidence is recorded. A bitmap enhancement includes upscaling, cleanup, relighting, recoloring, background removal, compositing, retouching, or other pixel-level changes.
- No high-fidelity Pencil restoration or Flutter UI implementation when required illustrations, bitmaps, logos, textures, generated images, or visual exports lack reuse check, production decision, bitmap source policy, background handling, background transparentization when applicable, transparent post-processing when applicable, asset atlas, generation evidence when used, slicing manifest, asset inventory, Flutter path, license status, and fidelity review.
- No UI completion claim before screenshots or Flutter golden evidence exist.
- No user-facing UI completion before `flutter-quality-review` records an aesthetic verdict against the approved mockup and design-freeze constraints; Critical or Important aesthetic findings must be resolved or explicitly accepted.
- No user-facing UI completion claim before independent visual-QA findings are resolved or explicitly accepted in `docs/tasks/<task-id>/visual-qa.md`.
- No task completion before its task-state claim, branch commit, `fvm flutter analyze`, relevant tests, and required design evidence are reported or explicitly marked unavailable with a blocker. Level integration smoke is an integration-branch gate; the full platform matrix is a final-integration gate.
- No final delivery or release-readiness claim before every in-scope platform has completed its final device, emulator, simulator, browser, or desktop runtime validation after all modules and pages are implemented.
- No next-task handoff before the confirmed task has completed its scoped cleanup or recorded `N/A` in `docs/tasks/<task-id>/evidence/manifest.md`.
- No delivery completion while Critical or Important review findings remain open.
- No release claim before privacy, account, payment, crash reporting, analytics, and store checklist are checked or explicitly marked out of scope.

## Subagent Use

Use subagents for independent product, UX, architecture, review, and release checks. Do not dispatch a writable agent before the Controller creates its task-state claim, task branch/worktree, base commit, and unique write scope. Do not dispatch multiple implementation agents against the same write scope. Read [references/subagent-map.md](references/subagent-map.md) and [../flutter-subagent-delivery/references/collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md) before orchestrating subagents.

## Common Mistakes

- Treating a prototype as a commercial app.
- Letting the implementer self-approve UI quality.
- Treating a generated mockup as implementation truth without design-freeze constraints.
- Generating an effect image without a formal transient prompt traced to the PRD and product-design principles, or writing that prompt and candidate visual files before the user confirms a freeze.
- Adding attractive but unscoped features, data, user goals, or visual exceptions to a prompt when they are absent from the PRD.
- Treating text-only UX/UI descriptions as sufficient for visual approval.
- Treating global high-fidelity direction as a substitute for page-level low-fidelity structure, Wireframe Review, and page mockup approval.
- Splitting modules only by code folders instead of product flow, data ownership, routing, and page interaction order.
- Generating page-level high-fidelity mockups before the page structure is reviewed and converted into text specs.
- Skipping asset atlas and slicing when the approved mockup contains required visual assets.
- Generating duplicate visual assets before checking existing brand, app, source, and inventory assets.
- Generating assets from the page mockup alone instead of global and page design-freeze constraints.
- Using Pencil whole-page screenshots or high-fidelity mockup crops as default bitmap sources instead of available image-generation output.
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
- Defaulting every product to restrained professional visuals instead of deriving a visual expression preset from category and audience.
- Skipping the one-time light visual interrogation before global exploration, or running a per-page visual interrogation stage.
- Freezing a global direction that lacks a restatable signature when the preset requires one.
- Retaining temporary files, invalid or expired artifacts, or superseded unselected design drafts after task confirmation without checking whether they are still required as approved or audit evidence.
