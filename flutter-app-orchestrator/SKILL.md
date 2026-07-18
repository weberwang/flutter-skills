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
2. Draft global UX/UI goals, flows, states, navigation model, and design-system direction with `flutter-ux-ui-quality`. The brief must show how the first-value moment is reached, how the user can safely try the product, and how the visual system conveys the approved product character and expression preset without using decoration as a substitute for clarity. Use [references/global-visual-direction-prompt-template.md](references/global-visual-direction-prompt-template.md) to prepare a transient formal prompt that defines the three-direction comparison, its PRD and market-analysis alignment, and the active visual expression preset with required direction mix and scoring weights. Do not write this prompt, a mockup brief, candidate images, or review output to the repository before the user confirms a freeze. Use the PRD, preset, and `docs/product/market-analysis.md` to recommend exactly three candidate directions for effect-image generation; enforce the preset’s three-direction distribution so the set does not collapse into three restrained professional looks; derive categories from the product, market opportunity, category conventions, and differentiation opportunities, so the template examples are optional references rather than a fixed set. When the exploration needs a representative page to generate effect images, choose it autonomously from the highest-priority PRD user task, high-value moment, first-value proof, and information needed to distinguish the directions; retain the selected page and rationale in the transient prompt. Do not use the global template as the image-generation prompt. Instead, fill [references/page-hifi-mockup-prompt-template.md](references/page-hifi-mockup-prompt-template.md) for each recommended candidate direction in the generation context, without saving a page-prompt file, then use it to generate comparable images. Keep the representative page, device, required content, copy, data, user task, and state identical across all directions so comparison remains fair; allow composition, grouping, visual rhythm, component silhouette, imagery, material, and motion intent to vary when those choices express the candidate direction and preset signature without changing product meaning. During this exploration, do not use ordinary Flutter widget composition or downstream asset workload as a visual ceiling. Trace every product claim, task, state, content constraint, and acceptance criterion to the PRD artifacts and market-analysis findings; document the product-design-principle check in the transient prompt. Run `@product-design user-context` preflight followed by `@product-design get-context` and `@product-design ideate` to produce the three recommended directions and their effect images. List the candidates and wait for the user to explicitly choose and confirm one; do not select a direction automatically.
3. Confirm global UX/UI direction with high-fidelity effect images using `flutter-hifi-mockup`. After the effect-image batch is complete, automatically dispatch exactly one Effect Image Reviewer with the images, product brief, active expression preset, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Use Apple Human Interface Guidelines as the interaction baseline. Present two separate sections inline: product-design issues with concrete fixes, then premium-feel improvements judged against the preset’s signature strength and wow requirement rather than universal visual austerity; list the candidate directions with their combined review results, then wait for the user to choose and confirm one direction. When the Global Freeze Signature Rule applies, require an explicit restatable-signature confirmation before freeze; if the answer is no, iterate instead of freezing. When the rule does not apply, record the N/A reason. Then record any `pin` / `raise` / `loosen` override and decide whether to apply the proposed changes. Do not save the review as a repository artifact. Do not revise, select, or freeze a direction until the user explicitly confirms it. After confirmation, copy the exact selected image to `.codex-workflow/visuals/global/frozen-<slug>.png` first, then write the prompt, brief, global design freeze, and ledger entry together with its candidate ID, decoded dimensions, SHA-256, and confirmation time. Use `@product-design image-to-code` only when the selected visual target has interaction ambiguity that needs a review-only prototype. This confirms visual direction and design-system intent only; the resulting global design freeze and representative-page effect images must not confirm any later page mockup, page design freeze, or implementation readiness.
4. Create architecture with `flutter-tech-design`, including module boundaries, cross-module contracts, data ownership, routing ownership, and shared foundations.
5. Initialize or standardize the Flutter project from that technical design with `flutter-project-init`.
6. Split coarse module boundaries and build order with `flutter-implementation-plan`; derive business-flow levels from the end-to-end user flow, module dependencies, and known page interaction order. Each known module and page must have a level, and delivery must complete and verify one level before advancing to the next; the plan must also account for the global verification platform scope. Do not prematurely freeze the detailed function and page task list for every module at this stage.

### Module Delivery

7. Execute modules with `flutter-subagent-delivery`. When a module first becomes eligible for implementation, re-enter `grilling` before refining or dispatching any task for it. Review the PRD, module map, technical design, existing code, and prior decisions; confirm the module's included user-facing functions, explicit non-goals, page and state boundaries, cross-module dependencies, and acceptance path one question at a time. After the user explicitly confirms shared understanding, append the module-stage result to `docs/product/grilling-log.md`, create `docs/plans/modules/<module-name>-scope.md`, then refine that module into functions, page functions, states, contracts, acceptance criteria, and task briefs. Each UI module or page task must then create a low-fidelity Pencil structure, pass Wireframe Review, and convert it into text specs. Before generating any page-level effect image, prepare [references/page-hifi-mockup-prompt-template.md](references/page-hifi-mockup-prompt-template.md) transiently, including the active expression preset and the page-type budget dial from the preset reference. Do not save `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`, the brief, candidates, or review output before a confirmed freeze. Full-budget pages (home, first-value, paywall, brand landing, high-value detail) must pursue the preset signature; settings, forms, permissions, account, error, and legal pages dial decoration down while keeping system consistency. Trace every page task, module, state, copy, data, interaction, and visual constraint to the PRD and approved design artifacts; document the product-design-principle check in the transient prompt; then use it to generate the page-level high-fidelity effect image. After the image is complete, automatically dispatch exactly one Effect Image Reviewer with the image, wireframe spec, active preset, page-type dial, and [references/mockup-self-review-prompt-template.md](references/mockup-self-review-prompt-template.md). Use Apple Human Interface Guidelines as the interaction baseline and present product-design issues with concrete fixes separately from premium-feel improvements measured against preset signature strength rather than restraint-for-its-own-sake. Do not save the review as a repository artifact. Do not revise, approve, or freeze the page design until the user explicitly approves changes or explicitly accepts the current result. After freeze confirmation, persist the exact selected image to `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png` first, then write the prompt, brief, page design freeze, and progress entry with its candidate ID, decoded dimensions, SHA-256, and confirmation time.
8. Use the selected page-level high-fidelity effect image and page design freeze as the sole visual source of truth for Pencil high-fidelity restoration; the wireframe remains a scope, structure, state, and interaction prerequisite only. Before deciding visual-asset work or restoring the approved image into Pencil, analyze each restorable layer or atomic unit and record one mutually exclusive category in `docs/design/pencil-hifi-restoration.md`: bitmap, UI, or data. Split composite elements into their bitmap, UI, and data units before classification, then review each bitmap unit for a separate production asset decision. For every icon, image, illustration, logo, texture, or other visual resource, verify a 100% match to the approved visual content, including silhouette, crop, color, texture, lighting, and intended transparency. Reuse, adapt, approved Pencil-node export, or explicit mockup extraction is allowed only when that exact-match evidence exists; otherwise the mandatory verdict is `generate`, followed by the independent bitmap generation, asset-atlas, and fidelity-review flow. Never substitute a near-match system icon, Flutter component, or existing asset for an unmatched resource. Restore data with editable text and representative placeholders that preserve the approved information hierarchy, text length, and layout; production data is not required for visual restoration, and a data unit must never trigger bitmap generation or extraction. Before proceeding, record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess asset provenance, font or icon sources, component states, crop rules, or hidden interactions. For every bitmap, record its source, crop, size, background treatment, and target node, then require a 100% match of the approved visual content; only documented rasterization or scaling tolerance is allowed. For every UI unit, record the native-Flutter feasibility reason and expected implementation approach. Use native Flutter when it can reproduce the unit exactly; otherwise record the bitmap-fill requirement and generate the required bitmap before restoration. Confirm the native-Flutter decision with implementation screenshot or golden evidence. Do not generate a bitmap for UI that native Flutter can reproduce exactly.
9. After the analysis identifies a bitmap or bitmap-fill requirement, use `flutter-asset-atlas` for its reuse check, production decision, generation or enhancement, slicing, export, inventory, and fidelity review. New bitmap generation must use product-design or image generation tools by default and follow the global design freeze and page design freeze. Treat bitmap enhancement as a design change: replace the corresponding asset in the design draft, preserve the approved layout and constraints, and record the updated design evidence before implementation. When the analysis identifies no bitmap or bitmap fill, record `N/A: no bitmap or exported visual assets` in the task brief and `.codex-workflow/progress.md`.
10. Decide whether Pencil high-fidelity restoration is required. Restore the page in Pencil when required, including every bitmap and bitmap fill identified by the analysis, then implement the Flutter page from text specs and handoff artifacts.
11. Review delivery with `flutter-quality-review`; for user-facing UI flows, run `@product-design audit` against screenshots before the final UX/UI verdict.
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
- Do not perform or claim device, emulator, simulator, browser, or desktop runtime verification during an individual module or page task. Defer it until all business-flow levels, module/page functionality, and required high-fidelity restoration are complete.
- No UX/UI approval from text alone; high-value screens require selected high-fidelity effect images or an explicit "no mockup needed" decision.
- No global visual direction approval before `@product-design ideate` provides three market-informed reviewable directions that satisfy the active preset’s required direction mix, the candidates are listed for the user, and the user's explicit selected direction is recorded. Do not select a direction automatically. Apply the Global Freeze Signature Rule from [../flutter-ux-ui-quality/references/visual-expression-presets.md](../flutter-ux-ui-quality/references/visual-expression-presets.md): when it applies, require an explicit restatable-signature confirmation and do not freeze if the answer is no; when it does not apply, record the N/A reason using the selected direction’s distinctive mix trait.
- No global effect-image generation before `docs/product/market-analysis.md` exists and a transient formal prompt prepared from the global prompt template maps every product requirement to PRD artifacts and every direction rationale to market-analysis findings, records the active visual expression preset with direction-mix, scoring-weight rules, and light-interrogation commitments, and records the product-design-principle check. Persist that prompt only after freeze confirmation.
- No representative-page effect-image generation during global visual exploration before the global prompt file records an autonomously selected representative page, its PRD-based rationale, and the shared device, required content, copy, data, user task, and state. Candidate directions may vary composition, grouping, visual rhythm, component silhouette, imagery, material, and motion intent without changing product meaning. Use the page high-fidelity prompt template for each candidate direction in the generation context; do not save a separate representative-page prompt file.
- No global visual direction approval before its completed effect-image batch has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements judged against the active expression preset’s signature strength and wow requirement rather than universal restraint, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. Review output is transient and must not be saved as a repository artifact.
- No implementation plan before module boundaries, module dependencies, cross-module interactions, page interaction order, and business-flow levels for modules and pages are recorded in `docs/plans/module-map.md`.
- No module function refinement, page-function refinement, task brief, page design gate, or implementation before that module has completed its implementation-stage `grilling` pass, the user's explicit shared-understanding confirmation is appended to `docs/product/grilling-log.md`, and `docs/plans/modules/<module-name>-scope.md` records the confirmed included functions and non-goals.
- Module-level grilling must happen just in time when the module first becomes eligible for implementation. A global PRD confirmation or earlier implementation plan does not substitute for this gate.
- No task in a later business-flow level may start until every required task, acceptance path, and cross-module contract in the preceding level has passed or is explicitly accepted. Same-level work may run in parallel only when the module map marks it parallel-safe.
- No page implementation readiness from global high-fidelity direction alone; global mockups do not replace page-level design gates.
- The global design freeze is a reusable visual-system baseline only. Its representative-page effect images must not be reused as confirmation for a later page, including when that page has the same route or a similar state.
- No page-level high-fidelity mockup before the current page task has a low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- No page-level effect-image generation before a transient formal prompt prepared from the page prompt template maps every page requirement to the PRD and approved design artifacts, records the active expression preset and page-type budget dial, and records the product-design-principle check. Persist it only after freeze confirmation.
- Do not generate or approve an effect image whose formal prompt invents a feature, user goal, content, state, commercial claim, or visual exception that conflicts with the PRD or approved product-design principles.
- No page design approval or design freeze before the completed page-level effect image has one independent Effect Image Reviewer result using Apple Human Interface Guidelines as the interaction baseline, separate product-design issues and premium-feel improvements judged against the active expression preset and page-type budget dial rather than universal restraint, or an explicit “no material issue” verdict for each section, and the user's explicit decision to apply or decline the proposed changes. On full-budget or wow-required pages, missing restatable signature is a blocking Important finding unless explicitly accepted. Review output is transient and must not be saved as a repository artifact.
- No repository visual write before explicit freeze confirmation. At freeze, persist the exact selected image under `.codex-workflow/visuals/<scope>/` before any related prompt, brief, design-freeze, or ledger write; record the frozen path, candidate ID, decoded dimensions, SHA-256, and confirmation time in the design freeze and ledger.
- Do not modify any effect image from an independent review without the user's explicit approval.
- No page UI implementation before the current page task has a reviewed low-fidelity structure, selected high-fidelity effect image, recorded approval, design-freeze constraints, and a recorded Pencil high-fidelity restoration decision.
- For high-fidelity Pencil restoration, the selected page-level effect image and page design freeze control all visual details. A low-fidelity wireframe may define scope, structure, states, and interactions, but must not replace or override the approved visual target.
- No high-fidelity Pencil restoration before Flutter initialization, Wireframe Review, `docs/design/wireframe-spec.md`, page-level mockup approval, design freeze, and a recorded effect-image analysis that assigns every restorable layer or atomic unit to bitmap, UI, or data.
- No high-fidelity Pencil restoration approval or Flutter handoff for an affected unit while a material visual uncertainty is unresolved; record it and obtain a decision instead of guessing.
- No UI bitmap fill or asset generation before the analysis records why native Flutter cannot reproduce the UI unit exactly. No bitmap restoration may be accepted before its source, crop, size, background treatment, target Pencil node, and 100% visual-content match verdict are recorded; only documented rasterization or scaling tolerance is allowed.
- No icon, image, illustration, logo, texture, or other visual resource may be restored with a near match. When its approved visual content cannot be verified as a 100% match, the task must generate a dedicated bitmap and complete the asset-atlas and fidelity-review flow before Pencil restoration or Flutter implementation.
- No page decomposition may enter Pencil restoration or Flutter implementation until every bitmap unit has a recorded separate-asset review verdict: reuse, adapt, generate, approved Pencil-node export, explicit mockup extraction, or `N/A: native Flutter/UI/data`.
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

Use subagents for independent product, UX, architecture, review, and release checks. Do not dispatch multiple implementation agents against the same write scope. Read [references/subagent-map.md](references/subagent-map.md) before orchestrating subagents.

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
- Defaulting every product to restrained professional visuals instead of deriving a visual expression preset from category and audience.
- Skipping the one-time light visual interrogation before global exploration, or running a per-page visual interrogation stage.
- Freezing a global direction that lacks a restatable signature when the preset requires one.
- Retaining temporary files, invalid or expired artifacts, or superseded unselected design drafts after task confirmation without checking whether they are still required as approved or audit evidence.
