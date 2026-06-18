---
name: flutter-workflow-orchestrator
description: Use when coordinating raw Flutter requirements intake, requirements brainstorming, PRD document generation, technical baseline generation, Product Design brief confirmation, reference-image-backed effect-image generation, design-direction confirmation, DESIGN.md output, shared HTML interactive prototype design source, shared design freezing, module implementation document generation, module effect-image generation, module HTML interactive prototype generation, module design freezing, architecture planning, project initialization, bootstrap code generation, implementation readiness, Product Design design QA, human visual inspection handoff, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through raw requirements intake -> requirements brainstorming -> PRD document generation -> global technical baseline -> target design-device preset and base resolution confirmation -> `@product-design` brief confirmation -> reference-image-backed representative sketch generation through local `$imagegen` -> final product design direction confirmation from the approved sketch -> representative final effect-image generation through `gpt-image-2-generator` -> `DESIGN.md` output -> optional post-direction Creative Production asset production / polish when the request is asset-oriented -> shared HTML interactive prototype design source -> shared freeze -> early project initialization plus bootstrap preparation -> module `impl.md` generation under frozen design and interaction principles -> module effect-image generation -> module HTML interactive prototype generation -> module design freeze -> implementation RD readiness -> architecture -> implementation workflow -> `@product-design` design QA -> human visual inspection.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow truth model for the whole project. When persistence is needed for a live run, it may serialize that state into runtime artifacts, but those artifacts are not part of the stable skill bundle.

On the first call for a target project root, run a lightweight git preflight before any downstream routing: check whether `.git/` already exists, whether `git status` is readable in that root, and whether a root `.gitignore` baseline already exists. If any of those repository-baseline pieces are missing, keep that finding in the route context and let `flutter-init` own the actual `git init` plus `.gitignore` creation or repair.

In manual mode, pause at confirmation gates after one stage or one module reaches a reviewable milestone. In `--auto` mode, behave as a full-module advancement loop across the whole target module set, auto-confirm ordinary orchestrator-owned stage and status promotions after receipt validation, and keep executing one serial module step after another until every target module is implemented or a real blocker appears, rather than opening parallel module lanes. In `--full-auto` mode, keep the same serial advancement loop but also auto-confirm deterministic human-facing workflow gates when one default is uniquely justified by existing artifacts. That expanded auto-confirm scope includes Product Design brief confirmation, public-shell confirmation, final product direction confirmation, and primary-platform device selection when the control contracts say the default target is unique. If the choice is still ambiguous, the workflow must stop and record a blocker instead of inventing certainty.

The default design source is now a shared HTML interactive prototype rather than any external design-draft adapter. After the final design direction is confirmed and `DESIGN.md` is written, the workflow must convert the approved screenshot references, the confirmed representative final effect-image baseline, and `DESIGN.md` into one prototype-derived design-source packet through the HTML interactive prototype flow. `@product-design` still owns the design-side kickoff: brief confirmation, direction framing, and visual-target selection. The shared/global flow must first generate one local representative sketch through `$imagegen`, wait for explicit sketch confirmation in manual mode, and only then generate the representative final effect image through `gpt-image-2-generator`. Final effect images remain mandatory, but the workflow now requires only the representative final effect image at the shared/global stage. Separate module design documents must not replace the frozen HTML interactive prototype packet. All module-related work must stay behind the global design freeze. Only after the shared design direction, shared interaction principles, shared public shell rules, and shared component families are frozen may the workflow start the per-module loop. In that loop, the active module's `impl.md` becomes a detailed module task implementation document constrained by the frozen design and interaction principles. The module no longer needs an independent design-draft stage. Instead, after `impl.md` fixes the module function, key states, task path, and non-display behavior boundaries, the workflow should generate the module's effect image first and then the module's HTML interactive prototype. Before every shared/global or module-stage sketch or effect-image generation request, the workflow must first read the frozen global design packet and explicitly extract the visual constraints that already exist for that page or module, including palette direction, typography mood, component family, CTA posture, image-treatment posture, spacing or hierarchy bias, and any other approved visual-system rules; both sketch generation and final effect-image generation may only extend those constraints rather than inventing replacements. At the shared/global freeze scope, the HTML interactive prototype packet may express or validate only the shared theme system, shared public shell, shared public component families, and shared interaction principles; it must not generate final module page implementation code at that stage. Module-scoped page prototype work belongs only to the active module after the shared/global freeze has passed and the active module's `impl.md` is already implementation-final. The HTML interactive prototype flow must treat the frozen final effect-image baseline and approved module effect images as the primary visual baselines and `DESIGN.md` as the constraint packet rather than replacing the visual baseline with prose. Design guidance must come only from the frozen global design images, the active module design-source packet, uploaded approved screenshot references, the frozen HTML prototype artifacts, and `DESIGN.md`; tool-native defaults, hidden heuristics, or internal style opinions are not valid guidance sources. After any shared/global or module freeze is confirmed, delete previously generated but no-longer-selected sketches or effect images from the corresponding workflow artifact directories and indexes so later routing cannot accidentally reuse stale alternatives. Restored design output must preserve one shared style direction, one shared theme system, one shared public shell contract, one shared public component family contract, and one shared interaction-principle contract across all pages. Page-scoped prototype runs stay capped at at most 6 parallel page-design subagents, and only the orchestrator may merge receipts, update the workflow record, or freeze the packet.

Default HTML prototype stack policy: use `Vite + React + TypeScript` unless the user explicitly overrides it. This default exists because it balances fast prototype implementation with stable Flutter restoration: React component structure is easier to translate into region ownership, state slots, overlay semantics, and the later `display_restoration_blueprint`. Do not default to Vue for the shared workflow unless a project-specific constraint requires it, because it adds a second component mental model without improving Flutter restoration enough to justify the drift. Do not default to plain `HTML/CSS/JS`, because it is easy to start but weak as a frozen design source: structure, interaction semantics, and state ownership are too easy to scatter across selectors and ad hoc scripts, which makes Flutter restoration noisier and less reliable.

When the request is asset-oriented rather than screen-implementation-oriented, the orchestrator may open the `Creative Production` branch in two windows. Before final product direction confirmation, it may use Creative Production as a direction-input branch when richer campaign or hero exploration is needed to inform the final decision. After `DESIGN.md` exists, it may use Creative Production as the post-direction asset-production branch for mood boards, ad directions, offer-led hero directions, scenes, shots, logos, asset packs, and publish-safe polish. Keep ownership explicit: `@product-design` still owns product-surface UX and the confirmed design direction, while `Creative Production` owns commercial creative exploration and asset finishing. Creative Production outputs may enrich reviewable visual evidence, but they never replace the shared HTML interactive prototype as the implementation design source, and they do not replace screenshot-based or image-based design-source normalization.

## Commercial Product UI Constraint

This workflow must optimize for a mature commercial product feel, not a requirements demo, explanatory mock, or settings-manual style UI.

Default assumption:
users scan, recognize, and act; they do not read long explanatory text unless they are blocked.

The workflow must treat excessive explanatory copy as a product-quality defect, not as a harmless fallback.

Always prefer this communication order on product surfaces:

1. visual hierarchy
2. spatial grouping
3. control state
4. icon / badge / chip / toggle / color cues
5. short label
6. short status text
7. optional secondary explanation behind disclosure

Do not let primary screens explain what the interface can already show through visual structure.

### Default Copy Posture

For product-facing mobile screens:

- prefer recognition over explanation
- prefer visual state over descriptive paragraphs
- prefer one-line labels over multi-line descriptive copy
- prefer short status chips, helper rows, and compact captions over long support text
- prefer progressive disclosure over always-visible explanation
- prefer secondary surfaces for education: bottom sheet, detail page, info modal, learn-more link, expandable cell

Users should understand the screen mostly by looking, not by reading.

### Commercial UI Compression Rule

Every product-facing screen must pass a copy-compression check before freeze:

- if a subtitle repeats the title's meaning, remove it
- if a row description only restates the row title, remove it
- if a support card explains something already visible from status, icon, color, or control state, remove or collapse it
- if multiple text blocks explain the same system state, keep only the shortest necessary one
- if the screen still works after deleting a paragraph, that paragraph should not be on the default surface

Long explanatory copy is allowed only when one of these is true:

- the user must understand a risk before acting
- the system is blocked and the cause is otherwise invisible
- the user is entering a recovery or exception flow
- the explanation is intentionally behind disclosure

### Primary Surface Rule

On the first screenful of any page, show only:

- the main task
- the current state
- the next action
- the minimum supporting context required to act safely

Do not spend first-screen space on broad education, repeated context, or policy-style explanation.

### Freeze Review Questions

Before approving any product-facing design, ask:

- If all long explanatory copy disappeared, would the screen still mostly make sense?
- Does the user understand the primary task in under 3 seconds without reading paragraphs?
- Is this screen acting like a product interface, or like a document explaining the interface?
- Would a mature commercial iOS app ship this much always-visible text on the primary surface?

If the answer is weak, the design must be revised before freeze.

## Required Reading

Load only the references needed for the current routing decision, but always preserve their authority over the workflow:

- `references/workflow-record-contract.md`: Read before initializing or optionally persisting workflow state for the current run.
- `references/requirements-prd-flow.md`: Read when the input is raw requirements, a one-line feature idea, a partially specified request, or any request that lacks a PRD artifact.
- `references/prd-template.md`: Read when raw demand must become a durable PRD artifact rather than a chat-only summary.
- `references/prd-completeness-gate.md`: Read before promoting `requirements_brainstorming` to `prd_ready`.
- `references/prd-handoff-map.md`: Read when checking whether the PRD is strong enough for technical baseline, Product Design, Creative Production, or later module splitting.
- `references/design-quality-guidance.md`: Read when defining global visual direction, writing `DESIGN.md`, or judging whether a design is strong enough to freeze.
- `references/design-md-template.md`: Read when the final product design direction is confirmed and the workflow must write a root-level `DESIGN.md`.
- `references/creative-production-branch.md`: Read when the user asks for campaign visuals, mood boards, hero directions, ad routes, asset packs, or publish-safe creative polish within the broader Flutter workflow.
- `references/control-contracts.md`: Read before deriving route locks, running preflight, validating receipts, delegating to subagents, applying confirmation gates, or updating maturity.
- `references/execution-modes.md`: Read whenever the invocation includes `--auto`, `--full-auto`, module auto-advancement, effect-image generation, or stop-condition decisions.
- `references/workflow-states.md`: Read when classifying `current_stage`, module maturity, or allowed next moves.
- `references/routing-rules.md`: Read before selecting any downstream skill or crossing any stage boundary.
- `references/hard-rules.md`: Read before applying any state/status promotion, freeze decision, implementation handoff, visual-evidence decision, or downstream delegation.
- `references/pressure-scenarios.md`: Read when the user request resembles one of the pressure examples or tries to skip a gate.

## Core Freeze Requirements

Before any global design freeze or module design freeze, use `@product-design` as the primary design controller. After the technical baseline is ready, first freeze the target design-device preset and base resolution for the current design cycle, then route to `@product-design` `get-context` to confirm the design brief. That brief-confirmation pass must also lock a structured clarification packet for later module splitting: core user journeys, page families, critical states, interaction goals, explicit `platform_identifier`, platform-aware navigation and feedback expectations, and per-surface information-density posture including what must be visible immediately versus what must be deferred, collapsed, paged, or moved to a secondary surface. During the shared/global taste-direction stage, use `https://mobbin.com/` as the mandatory first-stop product-design inspiration library, and do not enter direction recommendation, sketch generation, final effect-image generation, or downstream design freezing until the workflow has completed a Mobbin-backed inspiration pass. Treat Mobbin only as direction evidence rather than the formal design source. Then derive three comparable direction candidates from that inspiration pass, mark one as the primary recommendation, and use the approved reference images plus `@product-design` constraints to generate one representative reviewable local sketch through `$imagegen`. Optionally enrich that exploration with the pre-direction Creative Production branch when the workflow needs richer commercial visual evidence, confirm that representative sketch with the user as the final product design direction baseline, and only then use `gpt-image-2-generator` to generate the representative final effect image that becomes the frozen visual baseline for downstream work. Only after that write the confirmed direction into `DESIGN.md`. For iPhone-first mobile work, offer at least these common presets in manual mode unless the user already chose a viewport: `375 x 667 px` (SE / compact), `390 x 844 px` (standard iPhone baseline), `393 x 852 px` (Pro baseline), and `430 x 932 px` (Pro Max baseline). In `--auto` or `--full-auto`, when the run does not already have a frozen viewport, default the global design viewport to `390 x 844 px`. In `--full-auto`, when the design brief, public shell, or final direction already have one uniquely supported default backed by the current artifacts, apply that confirmation directly and continue; if multiple plausible defaults remain, stop and record the ambiguity as a blocker. If downstream freeze still needs normalization for the frozen packet, convert the approved image evidence and confirmed direction into one image-backed design packet, then route that packet into the shared HTML interactive prototype flow. The shared/global design freeze packet is limited to theme, public-shell, shared-component, and shared interaction-principle design; do not generate any page design during that shared/global freeze step. After the shared design freeze has passed, prefer starting project initialization and bootstrap preparation as soon as the shared public baseline is explicit, rather than waiting for every later module milestone. Only after the shared design freeze has passed may the workflow start module `impl.md` generation, module effect-image generation, module HTML interactive prototype generation, and module freeze. After normalization, inspect the matching artifact directories for static visual evidence before deciding whether any regeneration is necessary.

Effect images are mandatory across the workflow. If the target design-device preset or base resolution has not yet been frozen for the current global design cycle, stop before Product Design direction confirmation, sketch generation, or final effect-image generation and request it first. If the Product Design brief has not yet been confirmed through `@product-design` `get-context`, stop and route there before asking for confirmation. If the common public shell has not yet been explicitly agreed, stop and request shell confirmation before confirming design direction or generating images. If final product design direction is not explicitly confirmed from the approved representative sketch, stop and request confirmation before emitting `DESIGN.md` or entering HTML interactive prototype design-source work. Before every representative-sketch or final effect-image generation step, explicitly collect the already-frozen shared visual constraints from the global design packet and pass them forward as required inputs instead of letting the image tools infer them from scratch. Every final effect image must keep the frozen design width unchanged and must not use a canvas height smaller than the frozen base viewport height. When the target page or region is scrollable, the design image may extend vertically beyond that minimum height to show the intended scrolling content, but it must still preserve the frozen width and must not compress the layout just to avoid extra height. In manual mode, first generate the representative page sketch from the approved reference images through local `$imagegen` and wait for explicit user confirmation or revision feedback; that confirmation step should expose the three Mobbin-backed direction candidates with one primary recommendation instead of a single hidden answer. Once that representative sketch is explicitly confirmed, generate the representative final effect image through `gpt-image-2-generator`, freeze that final effect image as the sole visual baseline for the current design cycle, close alternative-direction browsing, delete obsolete alternative sketches or effect images that are no longer part of the frozen packet, and allow only same-direction completion work unless the user explicitly rejects the confirmation or restarts the design cycle. In `--auto`, if the recommendation pass already produced one clear primary direction from the three Mobbin-backed candidates, adopt it directly, generate the required representative sketch automatically after the route reaches the sketch stage, and then generate the representative final effect image after that sketch is accepted by the active execution mode. In `--full-auto`, if the route lock, recommendation artifacts, and existing shell or brief artifacts collapse the human-facing choice to exactly one supported default, auto-confirm that default and continue without a manual stop. Pre-confirmation representative sketches must be produced through local `$imagegen`; final effect images must be produced through `gpt-image-2-generator`, and any final-generation access or credential blocker must be recorded as a blocker for the workflow. Save representative sketches with a `-draft` suffix and final effect images with the corresponding page names under `docs/project/`, then index both for the selected HTML interactive prototype packet and human visual inspection when needed.

When the user explicitly needs campaign-ready visuals, marketing routes, or polished asset packs, prefer the `Creative Production` branch over direct preview-image generation. Before final product direction confirmation, the branch may act only as reviewable direction input. After `DESIGN.md`, use `Creative Production:explore` as the controlled asset-production entry point, then route into a focused explorer and finally to `generative-polish` only after one direction or deterministic base is selected. Keep both windows behind the same design-direction gates: they may inherit the confirmed product direction and `DESIGN.md`, but they must not silently redefine them.

Every representative-sketch or final effect-image generation request must explicitly include existing image-backed design constraints: `art_direction`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, image-treatment posture, and the approved reference-image baseline when those values already exist. Those constraints must be read from the current frozen global-design packet first, then narrowed only by the active page or module needs; if the global packet cannot supply the required visual constraints, stop and repair the packet instead of generating a speculative image. Every request must also carry the frozen design width plus the frozen base viewport height as the minimum output height. When the design target includes a scrollable page or scrollable region, allow a taller output height to show the designed scroll range, but do not shrink width or reduce height below the frozen minimum in order to fit more content into one screen. Representative sketch requests must go through local `$imagegen`, and the post-confirmation final effect-image request must inherit the same constraints plus any accepted revision notes before calling `gpt-image-2-generator`. If `gpt-image-2-generator` or its required environment cannot generate the required final effect images, stop and record a blocker for the workflow. All workflow final effect images must use light mode unless the user explicitly changes that requirement upstream.

For module implementation, high-fidelity visual fidelity is the first design-freeze priority. Before queueing or applying `module_design_frozen`, verify that the global design freeze is already complete, that the module `impl.md` already fixed the module function, states, interaction path, non-display behavior boundaries, and platform-aware information-density decisions under the frozen shared design and interaction principles, and that `flutter-design-freeze-gate` then evaluated the module effect image plus the frozen module HTML interactive prototype packet and high-fidelity visual contract: hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, platform-fit density, and any approved Flutterization or bitmap fallback. If the shared constraints, function contract, or visual contract are missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched revision.

## Routing Procedure

For every invocation:

1. Ensure workflow state is initialized for the current run. If runtime persistence is enabled, use `references/workflow-record-contract.md` to shape the persisted artifact.
2. On the first call for that target root, run the git preflight: verify `.git/`, run `git status`, and check whether `.gitignore` already exists. Record missing repository-baseline items explicitly instead of silently assuming a clean repo.
3. Determine whether the run is manual, `--auto`, or `--full-auto`; load `references/execution-modes.md` when relevant.
4. Read the existing workflow record and any required artifact indexes before choosing a route.
5. Derive and persist one route lock before invoking anything downstream.
6. Run the preflight gate from `references/control-contracts.md`. If it fails, record the exact blocker and stop.
7. Select the next downstream skill using `references/workflow-states.md` and `references/routing-rules.md`.
8. If the step is subagent-eligible, delegate only the specialist work and require a structured receipt; keep workflow ownership in the orchestrator.
9. Validate the receipt against the active route lock before applying any transition or status update.
10. In manual mode, queue reviewable stage/status changes behind confirmation. In `--auto`, auto-apply deterministic stage and status transitions, auto-confirm ordinary orchestrator-owned review gates after receipt validation, and keep invoking the next authorized serial step end-to-end until all target modules are implemented or a blocker appears. In `--full-auto`, also auto-confirm deterministic human-facing workflow gates when the control contracts prove there is exactly one supported default; otherwise stop with a blocker instead of guessing.
11. Update the orchestrator-owned workflow state as the single source of truth. Persist it only when the current run actually needs a runtime artifact.
12. Return the output contract fields listed below.

## Delegation Boundary

Subagents may execute specialist work, but they must not own workflow control. The orchestrator alone may choose `current_stage`, choose `current_module`, persist route locks when needed, run preflight, validate receipts, apply queued transitions, classify blockers, and update orchestrator-owned workflow state.

Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race. The only exception is a route-locked HTML interactive prototype page batch with at most 6 page-scoped subagents, where each subagent owns a different page and the orchestrator merges receipts. In `--auto` or `--full-auto` after the shared/global design freeze, advance one module at a time in the confirmed serial module order until all target modules are fully implemented or a blocker appears.

## Implementation Boundary

Do not move a module into `implementing` until `technical_baseline_ready`, `module_impl_docs_ready`, `module_design_frozen`, `impl_rd_ready`, and `bootstrap_code_ready` exist for the module, confirmed maturity is at least `impl_status=landed` and `design_source_status=frozen`, the frozen prototype-derived design-source packet exists for the module, and the required global public code baseline is already landed.

The required global public code baseline includes app bootstrap and environment initialization, root router or route host plus redirect policy, global dependency injection or provider scope entry, local storage baseline and persistence wiring, global error mapping and logging baseline, required shared theme or design-token baseline, and the shared shell layer when feature modules depend on an `app-shell` or `root-shell`. Unless the user explicitly overrides the toolchain choice, treat `fvm` as the default Flutter environment contract for project initialization, bootstrap, validation, and implementation commands, and prefer `fvm flutter ...` / `fvm dart ...` over bare `flutter` or `dart`. Add network baseline and API client wiring only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities.

`project_initialized` is directory-only: `flutter-init` may create the project shell, directory skeleton, and the sibling `skills/flutter-dev/` beside `flutter-init`, but it must stop before bootstrap code, shared wiring, feature code, or page code. Unless the user explicitly requires another toolchain contract, initialization should assume an `fvm`-managed Flutter environment and keep generated command guidance aligned with that default. Those global code responsibilities belong to the separate bootstrap code stage.

As soon as the shared design freeze is complete and the shared bootstrap-critical baseline is explicit enough, prefer `flutter-init` and bootstrap preparation before later module architecture milestones. Treat project initialization and bootstrap as early public-code preparation, not as a late afterthought.

When implementation work should begin, the entry sequence is fixed: route through `@superpowers` to produce `Spec` first, then through `@superpowers` again to produce `Plan`, and only then execute implementation with sibling `flutter-dev` and `flutter-project-guardrails`. Treat the modules as one serial implementation loop rather than a parallel batch. For each active module in order: first confirm the module `impl.md` as the detailed functional contract, then consume the frozen module effect image and module HTML interactive prototype, then require `flutter-uiux-to-architecture` to materialize a page-level `display_restoration_blueprint`, then land non-display-layer code against that blueprint, and only after that restore the display layer from the same approved blueprint rather than re-interpreting the prototype in code. Implementation execution inside that active module should stay serial by default unless the same module's ownership split is explicitly proven safe. Before display-layer code begins, inspect the corresponding page image, module effect image, HTML prototype, `display_restoration_blueprint`, and frozen design evidence when such evidence exists. If the selected prototype-derived design-source restoration already exported approved image assets, implementation should use those local assets directly. If an internal illustration, icon asset, texture, or bitmap fallback still needs generation or rework, let the active MCP / design tool chain choose the concrete generation mechanism as long as the result still satisfies the frozen design principles and implementation target. If non-display implementation drifts away from the frozen interaction or layout contract captured by that blueprint, fix the non-display code or route back to design-source control instead of allowing display-layer code to absorb the drift. When a source visual target and implementation screenshots both exist, run `@product-design` `design-qa` as a blocking helper before final handoff, then return to explicit human visual inspection rather than introducing a new automatic workflow stage.

## Output Contract

Return:

- `workflow_record_path`
- `workflow_record_update`
- `current_module`
- `current_state`
- `confirmation_status`
- `next_skill`
- `pending_next_stage`
- `pending_next_skill`
- `pending_status_updates`
- `route_lock`
- `execution_owner`
- `receipt_status`
- `receipt_summary`
- `progress_delta`
- `required_inputs`
- `blockers`
- `allowed_next_actions`
- `forbidden_actions`
