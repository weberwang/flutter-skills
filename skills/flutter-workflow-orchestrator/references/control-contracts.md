# Control Contracts

Use this reference for route locking, preflight, receipt validation, subagent delegation, workflow-record update rules, confirmation gates, and module maturity tracking.

## Contents

- [Route Lock Contract](#route-lock-contract)
- [Preflight Gate](#preflight-gate)
- [Specialist Receipt Contract](#specialist-receipt-contract)
- [No-Progress Stop Rule](#no-progress-stop-rule)
- [Subagent Execution Boundary](#subagent-execution-boundary)
- [Workflow Record](#workflow-record)
- [Real Execution Trace](#real-execution-trace)
- [Confirmation Gate](#confirmation-gate)
- [Module Artifact Maturity](#module-artifact-maturity)

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

- orchestrator-owned workflow state is initialized for the current run; if runtime persistence is enabled, the persisted artifact matches the latest confirmed state
- `current_stage` really authorizes the intended `next_skill`
- `confirmation_status` does not forbid execution for this turn
- `current_module` is valid for module-scoped work
- the selected module exists in the module index when module-scoped work is requested
- all required artifact paths for the intended move exist on disk
- all required maturity prerequisites are already confirmed, not merely implied in prose
- `platform_identifier` is explicit as the primary runtime and validation platform before architecture, implementation-readiness, human visual inspection, or implementation work that depends on a concrete validation surface
- validation follows the primary platform only: if exactly one eligible device exists, use it; if multiple eligible devices exist, stop and wait for explicit device selection; if `--full-auto` is active and exactly one eligible device is already booted, use that one as the deterministic default; if no eligible device exists and the platform supports emulator or simulator startup, start one and validate there
- when `--auto` or `--full-auto` is active, the next move is still authorized by the current confirmed artifacts and does not skip required execution gates

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

In `--auto` or `--full-auto` mode, every loop iteration must produce one of only two valid outcomes:

- the remaining workflow workload shrinks in a provable way
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

Treat subagent usage in this workflow with three categories.

### Orchestrator-only steps

These steps must stay in the orchestrator and must not be delegated:

- choose or confirm `current_stage`
- choose or confirm `current_module`
- derive and persist the route lock
- run the preflight gate
- decide whether a blocker is real enough to stop advancement
- validate downstream receipts against the active route lock
- apply or reject `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`
- update orchestrator-owned workflow state as the single source of truth
- decide whether `--auto` or `--full-auto` should continue, stop at workflow completion, or stop for no progress

These actions define workflow truth. If a subagent performs them, route drift becomes unverifiable.

### Subagent-eligible specialist stages

The following specialist stages may run inside a subagent, as long as the orchestrator locks the route first and validates the receipt after the run:

- `flutter-prd-rd-writer` for PRD or broad RD expansion into a technical baseline
- image-backed design-packet normalization for shared or module design consolidation
- `effect-image-to-pencil-design` for mandatory shared or module Pencil design-source generation, compare-and-fix review, and handoff to human design acceptance
- `Creative Production:explore` for controlled asset-branch intake and path selection after the orchestrator has confirmed that the request is asset-oriented
- focused Creative Production explorers such as `moodboard-explorer`, `ads-explorer`, `offer-explorer`, `scene-explorer`, `shot-explorer`, and `logo-explorer` when the asset branch already has a locked brief and desired output family
- `Creative Production:generative-polish` when a selected direction or deterministic base already exists and the asset output is publish-bound
- `design-preview-to-global-guidelines` for turning approved shared visuals into reusable global guidelines
- `flutter-design-freeze-gate` for freeze evaluation and revision feedback, both at shared scope and module scope
- `flutter-rd-module-splitter` for creating module index rows and executable module `impl.md` documents in one pass after the shared/global design freeze
- module-scoped `@superpowers` execution when delegated module document generation or implementation requires real execution ownership
- `flutter-design-source-control` when post-freeze design changes must be incorporated in a controlled way
- `pencil-design-to-flutter-restoration` for turning frozen Pencil design files into high-fidelity Flutter restoration contracts with standard-library, plugin, and bitmap-fit decisions
- `flutter-uiux-to-architecture` for architecture mapping, display-layer decision tables, and native-vs-bitmap decisions
- `flutter-init` for directory-skeleton creation, as long as it stops at initialization boundaries
- module implementation through explicit `@superpowers` `Spec`, then explicit `@superpowers` `Plan`, then serial execution of the active module loop with sibling `flutter-dev` and `flutter-project-guardrails`
- human visual inspection handoff when implementation output or screenshots are ready
- an MCP-driven image or design tool when the workflow already proved a raster asset is the correct implementation fallback

The subagent may create or revise artifacts, run specialist reasoning, and report blockers. It must return those results as a receipt. It must not promote workflow state on its own.

### Subagent constraints

Even when a step is subagent-eligible, these constraints still apply:

- only one active route-locked specialist step may run at a time for the same workflow record
- implementation execution for module work is serial by default after `Spec` and `Plan`; do not split the active module loop into parallel ownership units unless the workflow contract is explicitly changed
- `--auto` or `--full-auto` after the shared/global design freeze still advances one active module at a time; do not generate module docs, freeze modules, or implement multiple active modules in parallel against the same record
- parallel page-design subagents must not update workflow state artifacts, freeze `design_source_status`, decide adapter mode or project refs, or merge the final design-source packet
- if the workflow contract explicitly allows an ownership split inside one active module, those implementation subagents must not overlap ownership of the same file, same generated asset path, or the same mutable state contract in one batch
- any subagent touching module docs must be given the exact active module, expected artifact paths, and expected status delta
- any subagent doing module document generation or implementation must preserve a real execution trace suitable for receipt validation
- any subagent that discovers a blocker may report it, but only the orchestrator may classify it as stage-blocking and rewrite the workflow record

### Not subagent-eligible by default

The following work must not be delegated by default unless the user explicitly requests a different control model and the workflow contract is updated accordingly:

- cross-module scheduling decisions in `--auto` or `--full-auto`
- confirmation-gate application or rejection
- route-drift judgment
- no-progress stop judgment
- final interpretation of whether a step truly reached `implementation_final`, `frozen`, `landed`, or `project_initialized`

## Workflow Record

- On the first run, always initialize workflow state for the current run. Persist it only when the run actually needs a runtime artifact.
- Keep all stage bookkeeping under one orchestrator-owned workflow state model. Do not split stage tracking across ad-hoc notes or per-module workflow files.
- Read `references/workflow-record-contract.md` before initializing or optionally persisting workflow state.
- After every routing decision, update the record with the current stage, current module, confirmation status, next skill, blockers, pending next-stage data, pending status updates, confirmed artifact paths, and whether `--auto` or `--full-auto` is still advancing remaining modules.
- If `--auto` or `--full-auto` is active, persist that execution mode in the workflow record so downstream agents know why confirmation gates were auto-applied.
- Persist the active route lock and the latest receipt evaluation in the workflow record so the next turn can detect route drift instead of silently continuing from an invalid assumption.
- Persist whether the current step is orchestrator-only or subagent-eligible, so downstream execution ownership stays explicit.

## Real Execution Trace

When executable module document generation, module freeze, implementation-readiness, architecture work, or real code implementation is being advanced in the default workflow, keep a real execution trace in workflow state and optionally in a runtime execution-trace artifact outside the stable skill bundle.

For each touched module, record:

- `current_module`
- why the module is the correct next module in the confirmed serial module order right now
- the exact delegated generation or execution input
- the real generated module-document or execution output
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

Treat confirmation gates in two categories:

- soft confirmation: ordinary orchestrator-owned stage or status promotions, plus human-facing workflow gates that already have one uniquely supported default backed by the current artifacts
- hard confirmation: any gate where more than one plausible default remains, where route-lock or receipt proof is incomplete, or where the workflow would need subjective taste judgment instead of deterministic selection

When `--auto` is active, the orchestrator should auto-apply all of its own queued stage transitions and queued status updates instead of waiting for the user, until the auto stop condition is reached or a blocker appears.

When `--full-auto` is active, the orchestrator should auto-apply both ordinary orchestrator-owned queued transitions and any soft confirmation gate that has collapsed to exactly one supported default. It must not auto-apply a hard confirmation gate.

When `--auto` or `--full-auto` is active and a queued transition has been validated successfully, do not keep `confirmation_status=pending_confirmation` as an idle review pause. Promote the queued values, clear the pending fields, and continue directly into the next authorized step unless the workflow has reached a real blocker or the global auto stop condition.

In `--auto` or `--full-auto` mode, a queued transition for one module must immediately be followed by a fresh routing decision for the same module or the next serial module. Do not leave the workflow record in a pseudo-idle "recommended next skill" state while unresolved target modules still exist, and do not ask for an ordinary "continue" choice while downstream execution is still authorized.

## Module Artifact Maturity

Track module-stage maturity in addition to `current_stage`.

### `impl_status`

| Value | Meaning |
| --- | --- |
| `not_started` | The document does not exist yet. |
| `implementation_final` | The module `impl.md` was generated after the shared/global design freeze as a detailed module task implementation document. It already fixes the module function and key states under the frozen shared design and interaction principles, and is now the upstream contract for downstream Pencil design execution and freeze. |
| `landed` | The document references the frozen structured design-source packet and the landed status has been explicitly confirmed. |

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
