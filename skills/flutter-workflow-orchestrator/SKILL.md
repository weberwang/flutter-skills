---
name: flutter-workflow-orchestrator
description: Use when coordinating modular Flutter PRD/RD, taste-first shared design direction, module draft splitting, implementation-stage UI/UX refinement, module design freezing, architecture planning, implementation readiness, parity review, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through the approved PRD -> global technical baseline -> taste-first shared design direction -> taste-router text normalization plus static-evidence intake -> shared freeze -> split drafts -> implementation-stage paired `ui-ux.md` and `impl.md` refinement -> module design freeze -> implementation RD readiness -> architecture -> implementation workflow.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow record document for the whole project.

In manual mode, it may pause at a confirmation gate after one stage or one module reaches a reviewable milestone. In `--auto` mode, it must behave as a full-module advancement loop across the whole target module set, not as a single-module recommendation assistant.

The default workflow no longer requires Pen, Pencil, page-level `.pen`, or Pencil MCP data before Flutter implementation. Pen/Pencil skills may remain available as optional external design adapters, but this orchestrator must not route to them unless the user explicitly asks for Pencil tooling.

Before any global design freeze or module design freeze, always run `flutter-taste-router` to normalize the textual design packet first. After that normalization, inspect the matching artifact directories for static visual evidence. Before global design freeze, approved effect images are required. If global static evidence is missing, check `IMAGE_BASE_URL` and `IMAGE_API_KEY`. If both variables exist, call `gpt-image-2-generator` to generate global app preview images, save them under the matching page or module directory using the corresponding page name, and when one module page is selected as the global reference, store that chosen global preview under `docs/rd/` and copy the same file into the related module directory. The global preview should be the module page that shows the richest overall app surface. Global design-freeze generation must produce no more than 3 preview images in total. Every generation request must explicitly include the current style constraints, not just a loose theme reference. At minimum, write `art_direction`, `taste_constraints`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, and image-treatment posture into the generation input whenever those values already exist. If either environment variable is missing while global freeze still lacks approved effect images, stop and record a blocker instead of continuing. All workflow preview images, whether generated or accepted as new references, must use light mode instead of dark mode unless the user explicitly changes that requirement upstream.

For module implementation, high-fidelity visual fidelity is the first design-freeze priority. Before queueing or applying `module_design_frozen`, the orchestrator must verify that `flutter-design-freeze-gate` evaluated the module's high-fidelity visual contract first: hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and any approved Flutterization or bitmap fallback. If this contract is missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched design revision instead of treating later architecture or engineering planning as the place to polish visuals.

## `--auto`

This skill supports an `--auto` execution parameter.

When `--auto` is present, the orchestrator must keep routing and applying workflow transitions without stopping for any downstream confirmation gate, as long as the next move is deterministic and no blocker is hit.

`--auto` is a full-module advancement mode, not a current-module recommendation mode. It must keep working through the remaining target modules until every dependency-safe module has been advanced to the implementation boundary and no further pre-implementation move is available.

The `--auto` goal is:

- finish shared taste direction and shared freeze preparation
- run `flutter-taste-router` textual normalization before every shared freeze or module freeze decision
- inspect static-evidence directories before deciding whether image generation is necessary
- split modules
- iterate every module through paired `ui-ux.md` and `impl.md` refinement in `module_uiux_refinement`
- freeze each module design-source packet
- treat each module's high-fidelity visual contract as the first acceptance criterion for module design freeze
- advance each module to implementation-ready document maturity
- continue until every target module is ready to enter implementation, but before any module actually starts code implementation

`--auto` is not allowed to:

- start code implementation
- mark `code_status=in_progress`
- switch into `implementing`
- bypass real blockers or missing inputs
- invent approvals for ambiguous design choices
- stop just because one active module reached a local stable milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`
- leave a module-complete handoff behind as a mere `next_skill` suggestion when other target modules are still not implementation-ready

When `--auto` reaches shared freeze and static visual evidence is still missing after the `flutter-taste-router` text packet has been normalized, it should first inspect the relevant directories for existing page images. If none are available and both `IMAGE_BASE_URL` and `IMAGE_API_KEY` exist, it should automatically call `gpt-image-2-generator` to produce up to 3 global light-mode app preview images before continuing. If either environment variable is missing, it must stop and record a blocker because shared freeze requires approved effect images. For module freeze, static visual evidence remains optional when the normalized packet is already explicit enough.

Those generated page previews should be treated as:

- light-mode exploratory visual evidence for taste consolidation
- shared freeze input when one direction is selected
- optional module freeze input when a module-specific screen pack is still needed
- page-named evidence files that can be referenced directly by downstream implementation

The auto-generated previews do not remove the need for freeze-quality evaluation; they only satisfy the missing static-visual prerequisite.

## `--perviewer`

This skill also supports a `--perviewer` execution parameter.

`--perviewer` is a module-preview opt-in flag for module refinement and module freeze preparation.

Without `--perviewer`:

- module refinement must not generate new real-device or module-stage preview images by default
- module freeze should prefer the textual design packet plus already approved evidence
- downstream work may consume existing module visuals, but it must not auto-generate new module previews merely for convenience

With `--perviewer`:

- module-stage preview generation is allowed when the current module still benefits from page-addressable visual evidence
- generated module previews must inherit the approved shared/global style system instead of opening a new visual direction
- the workflow must record that opt-in decision and any generated module preview paths into `global-design-guidelines.md`

`--perviewer` does not weaken the shared/global freeze policy. Shared/global freeze may still auto-generate up to 3 shared previews when required by the existing workflow.

## Auto Loop Contract

After `modules_split`, `--auto` must behave as a loop:

1. Select the next dependency-safe target module that is not yet at the implementation boundary.
2. Set that module as `current_module` and update the workflow record immediately.
3. Verify that the selected module really exists in the module index and that its paired `ui-ux.md` and `impl.md` files already exist on disk from `modules_split`. If any of those artifacts is missing, record a real blocker and stop auto-advancement instead of inventing the module state.
4. Record why that module is dependency-safe right now before refinement begins.
5. Refine that module until its docs reach implementation-final maturity, strictly through explicit `@superpowers` execution.
6. If the refinement did not truly execute, mark that step as `not_executed` or `未执行` in the workflow record and any project-level execution trace, then stop instead of promoting later stages.
7. Run module freeze and freeze the design-source packet only when the packet is explicit enough and the high-fidelity visual contract has passed as the first freeze priority.
8. Advance the module to implementation-ready maturity.
9. Produce any required architecture output for that module.
10. Update `current_stage`, `next_skill`, `module_status_table`, and `decision_log`.
11. Re-evaluate the remaining modules and immediately continue with the next dependency-safe module.

`current_module` is only the module being processed right now. It must never be interpreted as the only module covered by the current `--auto` run.

If one module reaches `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`, that is only a local milestone. In `--auto` mode, the orchestrator must immediately decide whether the same module still needs another pre-implementation step or whether another module should become `current_module`.

## Stop Condition

The default stop condition for `--auto` is:

- every module row has at least `uiux_status=landed`
- every module row has at least `impl_status=landed`
- every module row has `design_source_status=frozen`
- any required architecture outputs for those modules are ready
- the workflow is waiting at the boundary before module implementation

When this stop condition is reached, the orchestrator should surface that the project is `implementation_ready_waiting` and return control to the user or downstream implementation skill.

`--auto` may stop only when one of these conditions is true:

- all target modules satisfy the implementation-boundary condition above
- a real blocker appears and the current round cannot safely continue

It must not stop because one module finished its local pre-implementation flow, because a downstream skill recommendation was produced, or because `current_module` changed from one module to another.

## Route Lock Contract

Treat this workflow as a locked state machine, not as a loose recommendation graph.

For every routing turn, the orchestrator must derive and persist one route lock before invoking any downstream skill:

- `expected_stage`: the current confirmed workflow state that authorizes the next move
- `expected_module`: the active module for this turn, or `not_selected` for global work
- `expected_next_skill`: the only downstream skill allowed to run next for this turn
- `expected_next_stage`: the only stage that may be queued or promoted after a successful result
- `expected_status_delta`: the only status fields that may change on success

The route lock belongs to the orchestrator, not to downstream specialist skills. A specialist skill may produce artifacts, blockers, or revision feedback, but it must not reinterpret the workflow and invent a different route.

If a downstream result implies a different module, a different stage, a different skill, or extra status promotion beyond the persisted route lock, treat that as route drift. Record the mismatch, mark the turn as `blocked`, clear queued promotions, and return control to the orchestrator instead of half-applying the result.

## Preflight Gate

Before every routing decision and before every downstream invocation, run a preflight gate.

The preflight gate must verify at minimum:

- `docs/rd/00-workflow-record.md` exists and matches the latest confirmed state
- `current_stage` really authorizes the intended `next_skill`
- `confirmation_status` does not forbid execution for this turn
- `current_module` is valid for module-scoped work
- the selected module exists in the module index when module-scoped work is requested
- all required artifact paths for the intended move exist on disk
- all required maturity prerequisites are already confirmed, not merely implied in prose
- `platform_identifier` is explicit before architecture, implementation-readiness, parity-review, or implementation work that depends on a concrete validation surface
- the next move does not cross the implementation boundary when `--auto` is active

If any preflight check fails, stop immediately. Record the exact failed check as a blocker. Do not let a downstream skill try to compensate for missing prerequisites by reconstructing state, inferring approvals, or backfilling artifacts opportunistically.

## Specialist Receipt Contract

Every downstream specialist result must be consumed as a structured receipt, not as free-form optimism.

At minimum, the orchestrator must verify these receipt fields before applying any transition:

- `receipt_status`: `advanced`, `blocked`, `rejected`, or `not_executed`
- `artifacts_produced`: exact artifact paths that now exist
- `status_updates`: only the maturity or stage-adjacent fields actually proven by artifacts
- `evidence_paths`: files, screenshots, traces, or packet paths that justify the claimed progress
- `execution_trace`: the real execution input and output when `@superpowers` or another execution-bound step was required
- `blockers`: explicit reasons when the step did not advance

If the receipt is missing, ambiguous, or not provable from real artifacts, treat the result as `not_executed` or `blocked`. Do not promote `current_stage`, do not apply queued maturity changes, and do not infer success from polished documents alone.

Only the orchestrator may:

- change `current_stage`
- set or clear `pending_next_stage`
- set or clear `pending_next_skill`
- set or clear `pending_status_updates`
- confirm that a receipt satisfies the route lock

## No-Progress Stop Rule

In `--auto` mode, every loop iteration must produce one of only two valid outcomes:

- the remaining pre-implementation workload shrinks in a provable way
- a new real blocker is recorded

If neither happened, the iteration is invalid and must stop as route drift or empty progress.

Treat the following as no-progress failures:

- `current_module` changed but no artifact, status, or blocker changed
- a downstream skill recommended a future move but did not produce a valid receipt
- a local milestone was described in prose but the remaining module set was not re-evaluated
- the workflow record was rewritten into a later posture without any new proof on disk

When a no-progress failure occurs, keep the last confirmed stage, clear queued promotions, record the cause in `decision_log`, and stop instead of continuing with speculative auto-advancement.

## Subagent Execution Boundary

Subagents may execute specialist work, but they must not own workflow control.

Treat subagent usage in this workflow with three categories:

### Orchestrator-only steps

These steps must stay in the orchestrator and must not be delegated:

- choose or confirm `current_stage`
- choose or confirm `current_module`
- derive and persist the route lock
- run the preflight gate
- decide whether a blocker is real enough to stop advancement
- validate downstream receipts against the active route lock
- apply or reject `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`
- update `docs/rd/00-workflow-record.md` as the single source of truth
- decide whether `--auto` should continue, stop at the implementation boundary, or stop for no progress

These actions define workflow truth. If a subagent performs them, route drift becomes unverifiable.

### Subagent-eligible specialist stages

The following specialist stages may run inside a subagent, as long as the orchestrator locks the route first and validates the receipt after the run:

- `flutter-prd-rd-writer` for PRD or broad RD expansion into a technical baseline
- `flutter-taste-router` for shared or module textual design normalization
- `design-preview-to-global-guidelines` for turning approved shared visuals into reusable global guidelines
- `flutter-design-freeze-gate` for freeze evaluation and revision feedback, both at shared scope and module scope
- `flutter-rd-module-splitter` for creating module index rows and paired split-draft docs
- module-scoped `@superpowers` execution for `module_uiux_refinement`
- `flutter-design-source-control` when post-freeze design changes must be incorporated in a controlled way
- `flutter-uiux-to-architecture` for architecture mapping, display-layer decision tables, and native-vs-bitmap decisions
- `flutter-init` for scaffold and bootstrap generation, as long as it stops at initialization boundaries
- module implementation through explicit `@superpowers` with project-local `flutter-dev` and `flutter-project-guardrails`
- `flutter-design-parity-reviewer` for implementation-vs-design verification
- `$imagegen` when the workflow already proved a raster asset is the correct implementation fallback

The subagent may create or revise artifacts, run specialist reasoning, and report blockers. It must return those results as a receipt. It must not promote workflow state on its own.

### Subagent constraints

Even when a step is subagent-eligible, these constraints still apply:

- only one active route-locked specialist step may run at a time for the same workflow record
- `--auto` after `modules_split` still advances one dependency-safe module at a time; do not refine multiple active modules in parallel against the same record
- any subagent touching module docs must be given the exact active module, expected artifact paths, and expected status delta
- any subagent doing refinement or implementation must preserve a real execution trace suitable for receipt validation
- any subagent that discovers a blocker may report it, but only the orchestrator may classify it as stage-blocking and rewrite the workflow record

### Not subagent-eligible by default

The following work must not be delegated by default unless the user explicitly requests a different control model and the workflow contract is updated accordingly:

- cross-module scheduling decisions in `--auto`
- confirmation-gate application or rejection
- route-drift judgment
- no-progress stop judgment
- final interpretation of whether a step truly reached `implementation_final`, `frozen`, `landed`, or `project_initialized`

## Workflow Record

- On the first run, always create `docs/rd/00-workflow-record.md` if it does not exist.
- Keep all stage bookkeeping in that one file. Do not split stage tracking across ad-hoc notes or per-module workflow files.
- Read `references/workflow-record-contract.md` before initializing or updating the workflow record.
- After every routing decision, update the record with the current stage, current module, confirmation status, next skill, blockers, pending next-stage data, pending status updates, confirmed artifact paths, and whether `--auto` is still advancing remaining modules.
- If `--auto` is active, persist that execution mode in the workflow record so downstream agents know why confirmation gates were auto-applied.
- Persist the active route lock and the latest receipt evaluation in the workflow record so the next turn can detect route drift instead of silently continuing from an invalid assumption.
- Persist whether the current step is orchestrator-only or subagent-eligible, so downstream execution ownership stays explicit.

## Real Execution Trace

When `module_uiux_refinement`, module freeze, implementation-readiness, or architecture work is being advanced in the default workflow, keep a real execution trace in the workflow record and optionally in a project-level document such as `docs/rd/00-superpowers-execution-trace.md`.

For each touched module, record:

- `current_module`
- why the module is dependency-safe right now
- the exact `@superpowers` refinement input
- the real refinement output
- whether `implementation_final` was truly reached
- the module freeze result
- the architecture output
- whether the workflow switched to the next module or stopped

If any item above did not really happen, write `未执行`, `not_executed`, or `unknown` explicitly. Document completeness alone is never proof that the execution really happened.

## Confirmation Gate

Treat confirmation as a workflow gate, not as a workflow stage.

Use these confirmation states:

| Confirmation Status | Meaning |
| --- | --- |
| `not_required` | The current routing decision does not need a fresh user confirmation before execution. |
| `pending_confirmation` | The current step has produced reviewable artifacts or status updates, but the workflow must not switch to the next process or apply queued status changes until the user explicitly confirms. |
| `confirmed` | The user has explicitly approved the pending transition or pending status updates, so the workflow can apply the recorded changes. |
| `rejected` | The user rejected the pending transition or pending status updates and the workflow must stay on the current confirmed state until the issues are resolved. |

When a specialist skill finishes and produces the required artifacts for a later stage or a new artifact maturity level, do not immediately switch to the next process. Keep `current_stage` at the last confirmed stage, set `confirmation_status` to `pending_confirmation`, record `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`, and write `waiting_for_user_confirmation` into blockers if no stronger blocker exists.

When `--auto` is active, the orchestrator should auto-apply all of its own queued stage transitions and queued status updates instead of waiting for the user, until the auto stop condition is reached or a blocker appears.

In `--auto` mode, a queued transition for one module must immediately be followed by a fresh routing decision for the same module or the next dependency-safe module. Do not leave the workflow record in a pseudo-idle "recommended next skill" state while unresolved target modules still exist.

## Module Artifact Maturity

Track module-stage maturity in addition to `current_stage`.

### `uiux_status` and `impl_status`

| Value | Meaning |
| --- | --- |
| `not_started` | The document does not exist yet. |
| `split_draft` | The document was created during `modules_split` and only captures initial module intent, scope, and constraints. It is not implementation-ready. |
| `implementation_final` | The document has been refined during implementation preparation to directly implementable granularity and is waiting for design-source freeze confirmation. |
| `landed` | The document references the frozen design source packet and the landed status has been explicitly confirmed. |

### `design_source_status`

| Value | Meaning |
| --- | --- |
| `not_started` | No module-level design-source packet exists. |
| `in_review` | The module has visual evidence or a freeze packet under review, but it is not confirmed as frozen. |
| `frozen` | The module design source packet is frozen and confirmed for architecture and code consumption. |

### `code_status`

| Value | Meaning |
| --- | --- |
| `not_started` | Code implementation has not started. |
| `in_progress` | Code work is actively being implemented. |
| `landed` | Code implementation is present and the landed status change has been explicitly confirmed. |

## Workflow States

Use one state per module:

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `prd_ready` | PRD or feature brief exists | `flutter-prd-rd-writer` |
| `technical_baseline_ready` | Global architecture, package stack, backend collaboration, and delivery assumptions exist without a taste-aligned shared UI direction | taste direction through `flutter-taste-router` |
| `shared_taste_direction` | Project-level visual posture, anti-template rules, information density, typography hierarchy, contrast posture, CTA model, motion role, and platform baseline are defined | `flutter-taste-router` or `design-preview-to-global-guidelines` |
| `uiux_draft` | Shared UI/UX direction exists but is not frozen | `flutter-taste-router`, `design-preview-to-global-guidelines`, or `flutter-design-freeze-gate` |
| `global_guidelines_frozen` | Approved screenshots or preview comps have been converted into frozen shared guidance, explicit global public component decisions, and dual-theme artifacts | `flutter-design-freeze-gate` |
| `design_freeze_ready` | The shared design packet plus required global freeze artifacts are ready for approval before module splitting | `flutter-rd-module-splitter` |
| `modules_split` | Detailed modules, paired doc paths, module detail cards, global baseline references, and module-level component skeletons exist. Each module's `uiux_status` and `impl_status` start as `split_draft` unless confirmed otherwise. | `flutter-rd-module-splitter` |
| `module_uiux_refinement` | The active module is being refined from split draft into paired implementation-final `ui-ux.md` and `impl.md`, incorporating taste, global freeze constraints, and page-level visual references when available | strictly call `@superpowers`, using `flutter-rd-module-splitter` contracts, then `flutter-design-freeze-gate` |
| `module_design_frozen` | The active module's implementation-final docs, high-fidelity visual contract, visual evidence, component freeze, state matrix, and design-source packet are frozen and confirmed | `flutter-design-source-control` or `flutter-uiux-to-architecture` |
| `impl_rd_ready` | The active module's UI/UX RD and implementation RD are implementation-final or landed, reference the frozen design source packet and global technical baseline, and are confirmed as implementable | `flutter-uiux-to-architecture` |
| `architecture_ready` | Tokens, assets, components, screen plan, non-native visual asset strategy, and scaffold contract exist | `flutter-init`, especially once the shared public baseline is clear enough to initialize the project before feature-module code |
| `project_initialized` | `flutter-init` has created the project scaffold and generated project-local `skills/flutter-dev/`, but has not started any feature implementation code | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `implementing` | Code work is in progress after the active module's design source is frozen and the paired module docs are no longer split drafts; execution must be strictly invoked through `@superpowers`, and display-layer work must inspect the corresponding page image through `$image-to-code` first when such evidence exists | strictly call `@superpowers` with project-local `flutter-dev`, `flutter-project-guardrails`, and `$image-to-code` for display-layer landing |
| `parity_reviewed` | Implementation has been checked against the frozen UI/UX source, theme artifacts, visual evidence, and required states | fix issues or mark `module_done` |
| `module_done` | Shared freeze is confirmed, module docs are landed, design source is frozen, code is landed, and parity review has passed | maintain index only |

## Routing Rules

1. Start by ensuring `docs/rd/00-workflow-record.md` exists. If it is missing, create it before any stage routing.
2. Before deciding or invoking anything downstream, derive one route lock and run the preflight gate. If either step fails, stop and record a blocker instead of letting the downstream skill reinterpret the workflow.
3. If `confirmation_status` is `pending_confirmation`, do not switch to the next process and do not apply queued status changes, unless `--auto` is active. In `--auto` mode, downstream confirmation gates are auto-confirmed until the implementation boundary or a blocker is reached, and the orchestrator must continue routing after the queued values are applied instead of stopping on the newly reached local milestone.
4. If the user explicitly confirms a pending transition or status update, promote the queued values, clear pending fields, and continue normal routing from the newly confirmed state.
5. If the user rejects a pending transition or status update, keep the current confirmed state, write the rejection reason, and route back to the skill that must revise artifacts.
6. If a specialist skill returns `blocked`, `not_executed`, or a receipt that fails route-lock validation, do not advance. Keep `current_stage` on the last confirmed stage, clear queued transitions, and record the blocker or route-drift reason.
7. If the input is only a PRD, broad RD, or feature brief, use `flutter-prd-rd-writer` first.
8. If a global technical baseline exists but the workflow lacks shared visual posture, commercial design decisions, or anti-template constraints, route to `flutter-taste-router`.
9. Do not fully refine module UI/UX before taste direction exists. The safe order is rough module split -> taste direction -> module UI/UX refinement.
10. Before any global design freeze or module design freeze, always let `flutter-taste-router` normalize the textual design packet first.
11. After textual normalization and before freeze, inspect the expected artifact directory for matching static visuals. Prefer existing images over regeneration.
12. If approved screenshots, preview comps, or static mockups must become a reusable shared design-source contract with fixed light and dark theme values, use `design-preview-to-global-guidelines`, then record `global_guidelines_frozen` as `pending_next_stage` until the user confirms.
13. If the workflow requests shared design freezing but no reference screenshots or usable preview images exist, do not route to `design-preview-to-global-guidelines` immediately. First check `IMAGE_BASE_URL` and `IMAGE_API_KEY`; if both exist, call `gpt-image-2-generator` to create the missing shared app previews. Shared freeze may generate at most 3 images total before selecting the approved direction. If either variable is missing, stop and record that global freeze is blocked by missing effect-image generation credentials.
14. All newly generated shared or module app previews must be light-mode visuals. Do not generate dark-mode freeze evidence unless the user explicitly requests a dark-only or dual-mode design cycle.
15. Before `modules_split`, treat design freezing as shared/public freeze only. Do not treat it as module page freeze or module-private component freeze.
16. If shared design has a candidate direction or a complete visual draft but no explicit freeze decision, use `flutter-design-freeze-gate` directly.
17. If `--auto` is active and shared freeze still needs static visual evidence after directory inspection, call `gpt-image-2-generator` only when both image environment variables exist; generate no more than 3 shared previews, save the selected global preview under `docs/rd/` and copy it into the owning module directory, then continue through `flutter-taste-router` and `flutter-design-freeze-gate`. Every generated preview must explicitly include the current style constraints in its generation input. If credentials are missing, stop and record a blocker instead of continuing toward shared freeze.
18. If `flutter-design-freeze-gate` finds hierarchy, task guidance, typography, contrast, CTA clarity, or state coverage still weak, do not route to freeze. Allow one shared revision pass through `flutter-taste-router` plus optional preview regeneration, then stop unless the user explicitly restarts the design cycle.
19. If the shared visual direction has been approved but detailed modules and paired doc paths do not exist yet, use `flutter-rd-module-splitter`. Its first pass creates split drafts, not implementation-final docs.
20. If multiple feature modules depend on one shared route host, root redirect layer, tab shell, or shell-level state, allow `flutter-rd-module-splitter` to split an `app-shell` or `root-shell` module first instead of burying that responsibility inside feature modules.
21. If a module has been selected for implementation preparation and its `uiux_status` or `impl_status` is still `split_draft`, keep or promote the module to `module_uiux_refinement` and strictly call `@superpowers` to refine only that active module's existing paired docs while following the document contracts defined by `flutter-rd-module-splitter`.
22. In module implementation preparation, refine `docs/rd/modules/<module>/<module>.ui-ux.md` and `docs/rd/modules/<module>/<module>.impl.md` before attempting module design freeze. Do not freeze a module whose paired docs are not both implementation-final.
23. When module refinement produces implementation-final docs, keep `current_stage` at the last confirmed stage, queue `<module>.uiux_status=implementation_final` and `<module>.impl_status=implementation_final`, and wait for confirmation before design freeze. In `--auto` mode, auto-apply those queued updates and continue directly into module freeze for the same module.
24. In module freeze, static visual evidence is optional. If the active module has no static preview but the `flutter-taste-router` design packet is explicit enough, route that packet directly to `flutter-design-freeze-gate`.
25. If a complete active-module visual draft, preview pack, or implementation-facing design-source packet exists, route to `flutter-design-freeze-gate` before queueing `module_design_frozen`. Treat the module's high-fidelity visual contract as the first freeze question; it must be accepted, explicitly reduced by design-source control, or returned for revision before any architecture or code handoff.
26. In `--auto` mode, module freeze should rely on `flutter-taste-router` to determine and consolidate module UI/UX. Do not require auto-generated static images for module freeze unless the packet is still too ambiguous to freeze safely.
27. During `module_uiux_refinement` and module freeze preparation, do not generate new module real-device previews by default. Generate them only when `--perviewer` is explicitly active for the current run.
28. When `--perviewer` is active and module previews are generated, write that opt-in plus the generated module preview paths into `global-design-guidelines.md` so downstream implementation and parity review know those previews were intentional module-stage evidence.
29. If `flutter-design-freeze-gate` finds the active-module design package not yet strong enough to freeze, keep the workflow on the active module, update the active module UI/UX doc plus design packet and optional visual evidence exactly once, and stop without another automatic freeze pass unless the user explicitly restarts a design cycle.
30. When `flutter-design-freeze-gate` approves the active module design source, first verify its receipt includes `high_fidelity_freeze_status=passed` or an explicit approved reduction. Do not immediately mark it frozen. Queue `pending_next_stage=module_design_frozen`, queue `design_source_status=frozen`, and if docs reference the frozen design source packet, also queue `uiux_status=landed` and `impl_status=landed`. In `--auto` mode, auto-apply that promotion and immediately decide whether the same module still needs implementation-readiness or architecture output before switching modules.
31. If a frozen UI/UX source is about to be consumed by implementation RD or code, use `flutter-design-source-control`.
32. If frozen UI/UX, theme values, component rules, and visual evidence must become Flutter-facing tokens, assets, components, screen architecture, and non-native visual fallback decisions, route to `flutter-uiux-to-architecture`. Do not require `.pen`.
33. Before architecture planning, implementation-readiness confirmation, parity review, or code implementation, verify that `platform_identifier` is explicit enough for the real validation surface. Do not treat `platform_baseline` such as `ios_hig` as if it already meant `android_emulator`, `windows_desktop`, or `web_browser`.
34. Do not move a module into `implementing` until `technical_baseline_ready`, `modules_split`, `module_design_frozen`, and `impl_rd_ready` exist for the module, confirmed maturity is at least `uiux_status=landed`, `impl_status=landed`, and `design_source_status=frozen`, and the required global public code baseline is already landed.
35. The required global public code baseline before module implementation must include at least:
   - app bootstrap and environment initialization
   - root router or route host plus root redirect policy
   - global dependency injection or provider scope entry
   - local storage baseline and persistence wiring
   - global error mapping and logging baseline
   - shared theme or design-token baseline required by the frozen design source
   - the shared shell layer when feature modules depend on an `app-shell` or `root-shell`
35. Add network baseline and API client wiring to the global public code baseline only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities. Do not force network infrastructure into purely local, offline, or static-flow projects.
36. As soon as the shared public baseline is explicit enough, prefer triggering `flutter-init` before feature-module code begins. The best trigger point is after shared design freeze, module split, shared shell or global public baseline clarification, and the first architecture output that defines bootstrap-critical inputs.
37. Bootstrap-critical inputs for that early `flutter-init` trigger include at least the global public code baseline, any required `app-shell` or `root-shell`, shared theme or token baseline, route host or redirect policy, storage baseline, error/logging baseline, and network baseline only when the project actually needs it.
38. Do not wait for every feature module to reach `architecture_ready` before triggering `flutter-init` when the shared baseline above is already clear enough.
39. When `--auto` is active after `modules_split`, iterate all target modules in dependency-safe order and continue refinement until every module reaches implementation-ready maturity, but allow `flutter-init` to run as soon as the shared bootstrap-critical baseline is ready.
40. In `--auto` mode, after one module reaches any local stable node such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`, immediately choose the next valid pre-implementation action. That may mean continuing the same module, switching `current_module` to the next dependency-safe module, or triggering `flutter-init` if the shared baseline is ready and the scaffold is still missing.
41. In `--auto` mode, after a module becomes locally complete for the current step, immediately update `current_module`, `current_stage`, `next_skill`, `module_status_table`, and `decision_log` to reflect the next remaining work. Do not leave `next_skill` as a passive future suggestion if unresolved target modules still exist.
42. If a module dependency prevents the next module from being refined safely, keep the workflow active but stop auto-advancement and record the blocker explicitly.
43. If the shared bootstrap-critical baseline is ready and the target project has not been scaffolded yet or does not contain project-local `skills/flutter-dev/`, use `flutter-init` before feature-module implementation begins. Do not delay this just because unrelated feature modules still lack later-stage architecture output.
44. `flutter-init` must stop at initialization boundaries. It may scaffold folders, shared bootstrap, shared wiring, and annotation-ready contracts, but it must not implement feature code, page code, or module-specific business logic.
45. If `flutter-init` has completed and project-local `skills/flutter-dev/` exists, record `project_initialized` as `pending_next_stage`.
46. If `--auto` is active, do not stop for `project_initialized`, `implementation_final`, `module_design_frozen`, `impl_rd_ready`, `architecture_ready`, or other downstream confirmation gates. Keep advancing until the implementation boundary is reached for all target modules or a blocker appears.
47. If `--auto` is active and all target modules are implementation-ready, stop here instead of entering `implementing`.
48. If implementation work should begin or continue, strictly call `@superpowers` together with project-local `flutter-dev` and `flutter-project-guardrails`.
49. During module implementation, split execution into `uiux` and `impl` tracks when the work naturally separates presentation from behavior or data contracts. Both tracks must still be executed through explicit `@superpowers` invocation, not by directly running downstream implementation skills on their own.
50. The default module landing order is: define the minimum data contract first, then land the display layer skeleton and main user path, then connect the real data layer. The minimum data contract should cover interface fields, state enums, loading or empty or error states, and interaction input-output boundaries without forcing full data-layer completion first.
51. For ordinary business-page modules, prefer `minimum data contract -> display layer -> data integration`. For infrastructure-heavy modules such as auth guards, route shells, sync engines, caches, payment orchestration, or backend-first flows, it is allowed to land the minimum process or data layer first and then attach display surfaces later.
52. Before display-layer code begins, run a display-layer readiness preflight. At minimum, verify:
   - the page has a readable main preview image
   - complex areas have readable detail previews when needed
   - fidelity-critical regions have enough evidence coverage, including state, scroll-position, and overlay evidence when those dimensions materially affect the layout
   - `ui-ux.md` explicitly records scroll, list, overlay, layout, sticky, and component-repeatability semantics
   - `flutter-uiux-to-architecture` has already produced a concrete display-layer decision table
   - every important page region is classified as `preserve_faithfully`, `flutterize`, or `simplify`
   - every fidelity-critical region has an explicit `layout_anchor`, `spacing_lock_rule`, `z_axis_rule`, and `pixel_tolerance`
   - non-native visual effects are already classified as native code or asset fallback
53. Treat hero regions, CTA clusters, branded illustration zones, layered backgrounds, sticky headers, and overlay-heavy regions as fidelity-critical by default unless the frozen design source explicitly says otherwise.
54. During display-layer implementation, keep taste guidance active as a guardrail for hierarchy, spacing, typography, contrast, CTA salience, motion restraint, and anti-template composition. Taste must not override frozen UI/UX intent. If corresponding page images exist, inspect them through `$image-to-code` before landing display-layer code.
55. Treat preview images as visual-structure evidence, not as the only source of truth for Flutter implementation choices. Final scroll, list, sticky, overlay, and layout decisions must follow the combination of `ui-ux.md`, `impl.md`, and `flutter-uiux-to-architecture`.
56. If the architecture output marks a region `preserve_faithfully`, do not normalize away its locked spacing, hierarchy, layering, or asset usage for engineering convenience. Any such change must return to `flutter-design-source-control`.
57. If the page effect image contains a bitmap visual, texture, illustration, composite, or other effect that Flutter cannot reproduce natively with reasonable cost and fidelity, do not force a code-only rebuild. Record it as a generated asset requirement, use `$imagegen` to generate the needed bitmap asset, move the selected result into the project, and let implementation consume that asset explicitly.
58. Only use `$imagegen` for visuals that are genuinely better as raster assets. Do not use it for shapes, simple gradients, icons that belong to an existing vector system, or effects that Flutter can reproduce cleanly with native code.
59. If code is complete or screenshots exist, use `flutter-design-parity-reviewer`.
60. If the user requests UI, layout, interaction, hierarchy, visual token, or state changes after shared freeze or module design freeze, use `flutter-design-source-control`.
61. Only route to Pen/Pencil skills when the user explicitly requests Pencil tooling or provides a `.pen` workflow. That optional path must not become a default gate for Flutter implementation.

## Hard Rules

- Do not split implementation modules from a raw PRD before a global technical baseline and package stack exist.
- Do not treat routing as a best-effort recommendation flow; it is a locked state machine owned by the orchestrator.
- Do not invoke a downstream skill until the route lock is persisted and the preflight gate passes.
- Do not delegate workflow truth ownership to a subagent.
- Do not use `flutter-prd-rd-writer` for detailed module design.
- Do not skip taste direction before detailed module UI/UX refinement.
- Do not confuse `platform_baseline` with a verified `platform_identifier`.
- Do not skip `flutter-taste-router` textual normalization before any shared freeze or module freeze check.
- Do not generate new static visuals before checking whether the target directories already contain usable page images.
- Do not accept or generate dark-mode effect images as the default workflow reference set; the default preview baseline is light mode.
- Do not let shared design freeze proceed without approved effect images.
- Do not generate more than 3 new shared/global preview images before global design freeze.
- Do not send shared/global or module preview generation requests without explicit style constraints once the design packet already defines them.
- Do not let module preview generation redefine palette, typography mood, component family, image treatment, or CTA posture after a shared/global direction has been approved.
- Do not let shared freeze before `modules_split` claim that module pages or module-private components are frozen.
- Do not treat `modules_split` output as implementation-ready.
- Do not attempt module freeze before both paired module docs, `ui-ux.md` and `impl.md`, have been refined to implementation-final maturity.
- Do not freeze a module for implementation while its high-fidelity visual contract is missing, vague, or deferred to later code polish.
- Do not let code implementation begin before `technical_baseline_ready`, `modules_split`, `module_design_frozen`, and `impl_rd_ready` exist for the module.
- Do not let code implementation begin while `uiux_status` or `impl_status` is still `split_draft`.
- Do not let a feature module start landing before the required global public code baseline is present.
- Do not force a network baseline into projects or modules that do not require remote data or network capabilities.
- Do not postpone `flutter-init` until every feature module is fully architecture-ready when the shared bootstrap-critical baseline is already sufficient to initialize the project.
- Do not let `flutter-init` implement feature pages, feature business flows, or module-specific behavior while initializing the project.
- Do not mark `uiux_status=landed` or `impl_status=landed` until the docs reference a confirmed frozen design-source packet.
- Do not start ordinary page-module implementation by fully building the data layer first when a minimum contract is enough to unblock the display layer.
- Do not mark `code_status=landed` until code output exists and the landed status change has been explicitly confirmed.
- Do not route around `flutter-design-freeze-gate` on implied approval.
- Do not let a complete shared or module design draft skip `flutter-design-freeze-gate` before freeze.
- Do not allow design packages with unresolved hierarchy, task guidance, typography, contrast, CTA, or state-coverage defects to advance into shared freeze or module design freeze.
- Do not treat architecture planning, Flutterization, or implementation convenience as a substitute for resolving high-fidelity visual decisions during module design freeze.
- Do not let `--auto` cross the boundary into `implementing`.
- Do not let `--auto` skip blockers, unresolved dependencies, or missing design inputs.
- Do not let `--auto` pretend a module is implementation-ready when its docs are still `split_draft` or its design source is not frozen.
- Do not stop `--auto` for ordinary downstream confirmation gates before the implementation boundary.
- Do not stop `--auto` just because the current module reached `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready` while other target modules still remain.
- Do not treat `current_module` as the only module covered by an `--auto` run; it is only the module currently being processed.
- Do not leave `next_skill` as a passive handoff recommendation after a local module milestone when `execution_mode=auto` and more target modules are still pending.
- Do not continue `--auto` past `modules_split` when the selected active module, its module-index row, or its paired docs cannot be verified on disk.
- Do not skip directory inspection and environment-variable checks before auto-generating static visual evidence in `--auto` mode.
- Do not continue into shared/global freeze when `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing and approved effect images still do not exist.
- Do not require static images for module freeze when `flutter-taste-router` has already produced a sufficiently explicit module design packet.
- Do not generate new module real-device previews during module refinement or module freeze by default; require explicit `--perviewer` opt-in.
- Do not treat `--perviewer` as permission to redefine the approved shared/global style direction; it only enables module-stage preview evidence generation.
- Do not require page-level Pen, `.pen`, Pencil MCP data, or `pen_status` in the default Flutter implementation workflow.
- Do not let implementation rewrite design intent. Design changes after freeze must return to design control.
- Do not route directly from `architecture_ready` to project-local `flutter-dev`; new project scaffolding must pass through `flutter-init`.
- Do not let module refinement or code landing bypass `@superpowers`.
- Do not directly route module refinement to `flutter-rd-module-splitter`, `flutter-dev`, project-local implementation skills, or any other execution path without explicit `@superpowers` invocation.
- Do not directly route module implementation to `flutter-dev` or project-local execution skills without explicit `@superpowers` invocation.
- Do not treat a complete-looking `ui-ux.md` or `impl.md` as proof that `@superpowers` refinement really happened.
- Do not let `.impl.md` claim `superpowers_refinement_status=verified_executed` unless the workflow record or execution trace contains the real `@superpowers` inputs and outputs for that module.
- Do not start display-layer landing before the preflight inputs are complete enough to avoid image-only guessing.
- Do not start high-fidelity display-layer landing with only a broad page preview when fidelity-critical regions still lack detail, state, scroll, or overlay evidence.
- Do not let display-layer code land without consulting the corresponding page image through `$image-to-code` when such image evidence exists.
- Do not let preview images alone decide final Flutter widget strategy when documented interaction or architecture semantics say otherwise.
- Do not leave a fidelity-critical region without an explicit `preserve_faithfully`, `flutterize`, or `simplify` classification in architecture output.
- Do not let engineering convenience flatten locked spacing, layer depth, or CTA dominance for regions marked `preserve_faithfully`.
- Do not force Flutter-native reconstruction for visuals that are clearly better shipped as generated bitmap assets; route those through `$imagegen` and store them inside the project.
- Do not use `$imagegen` as an excuse to skip native implementation for visuals that Flutter can reproduce cleanly.
- Do not switch to the next process automatically after a specialist skill finishes; wait for explicit user confirmation whenever queued transitions or status updates exist.
- Do not ask an execution skill to do workflow bookkeeping that belongs here.
- Do not let a downstream skill change `current_stage`, `pending_next_stage`, `pending_next_skill`, or `pending_status_updates` by implication.
- Do not accept a downstream result without a verifiable receipt containing artifacts, evidence, and blockers.
- Do not treat an iteration with no status delta and no new blocker as valid progress in `--auto`.
- Do not continue auto-advancement after route drift, receipt mismatch, or empty progress.
- Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race.
- Do not let a subagent decide whether `--auto` should switch modules, stop, or promote a stage.
- Do not treat one module's state as proof that another module is ready.
- Do not create per-module workflow state files; keep stage tracking in `docs/rd/00-workflow-record.md`.

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

## Pressure Scenarios

- User says "implement this home page directly" with only a PRD: route to `flutter-prd-rd-writer`, not module split or code.
- User says "split modules first, choose packages later": block and require baseline architecture and package decisions.
- User says "refine UI/UX first, taste later": block detailed refinement; require rough split plus taste direction first.
- User says "the design draft is complete, just freeze it": route to `flutter-design-freeze-gate`.
- User says "the shared effect image looks close enough, just freeze it": block and route back through exactly one shared revision pass, then stop.
- User says "skip global effect images and freeze directly": block. Shared/global design freeze requires approved effect images, and generated previews are capped at 3 before choosing the direction.
- User says "modules are split, now refine only the home module": keep the active module in `module_uiux_refinement` and strictly route to `@superpowers` for focused paired-doc refinement using the `flutter-rd-module-splitter` contract.
- User says "continue auto from modules_split" but the module index or paired docs are missing: treat that as a real blocker, record `未执行` for refinement-related steps, and stop instead of reconstructing fake progress.
- User asks why a root navigation host was split separately: explain that an `app-shell` module is valid when shared route hosting, root redirects, or shell-level state has independent implementation value.
- User says "the docs are final, start coding": require explicit confirmation for queued `implementation_final` and design-source freeze updates before code.
- User says "we can make it high fidelity during implementation": block module freeze and route to the correct design revision path; high-fidelity visual fidelity is the first module design-freeze priority, not a later code-polish task.
- User says "run `flutter-workflow-orchestrator --auto`": keep advancing through shared freeze, module split, per-module paired-doc refinement, module freeze, implementation-readiness preparation, and any required architecture output for every dependency-safe target module until all target modules are waiting at the implementation boundary, then stop before code. Before each freeze, normalize text through `flutter-taste-router`, inspect static-image directories, and only generate missing page images when the image environment variables are present.
- User says "模块细化时也生成真机效果图": do not do that by default; require explicit `--perviewer`, and if it is active, record the opt-in plus generated paths into `global-design-guidelines.md`.
- User says "验证平台是 android 模拟器、Windows 或 Web": record that as explicit `platform_identifier` instead of hiding it under a generic mobile baseline.
- User says "use a dark-mode preview as the workflow reference": treat that as a special override request. The default workflow reference previews remain light mode unless the user explicitly changes the design requirement.
- User says "this module is done, what next": if `--auto` is active and other target modules still remain, do not stop to ask. Select the next dependency-safe module, update the workflow record, and continue automatically.
- User says "why did auto stop after one module reached architecture_ready": treat that as incorrect behavior. `--auto` must continue unless all target modules are implementation-ready or a real blocker was recorded.
- User says "when should project initialization happen": explain that the preferred trigger is once the shared global public baseline and bootstrap-critical architecture inputs are clear, before feature-module code starts, not after every feature reaches late-stage architecture output.
- User says "where is the Pen file": explain that Pen is optional and not required by the default workflow.
- User says "adjust button hierarchy during implementation": route to `flutter-design-source-control`.
- User says "implement the screen layer now": strictly route to `@superpowers` and require `$image-to-code` to inspect the corresponding page image first when that image exists.
- User says "start implementing this feature module now": first verify that the required global public code baseline is already landed; if not, block module implementation and land the missing global code first.
- User says "this effect cannot be written natively in Flutter": classify whether it should become a project bitmap asset; if yes, route to `$imagegen`, save the chosen asset into the workspace, and reference it from the implementation plan instead of forcing a brittle code imitation.
- User says "the code is done, check whether it matches the design": route to `flutter-design-parity-reviewer`.

## References

- Read `references/workflow-record-contract.md` for the exact initialization and update contract of `docs/rd/00-workflow-record.md`.
