# Control Contracts

Use this reference for route locking, preflight, receipt validation, subagent delegation, workflow-record update rules, confirmation gates, and phase-aware maturity tracking.

## Route Lock Contract

Treat this workflow as a locked phase-and-state machine, not as a loose recommendation graph.

For every routing turn, the orchestrator must derive and persist one route lock before invoking any downstream skill:

- `expected_phase`
- `expected_stage`
- `expected_module`
- `expected_next_skill`
- `expected_next_stage`
- `expected_freeze_type`
- `expected_status_delta`

If a downstream result implies a different phase, stage, module, skill, freeze type, or extra status promotion beyond the persisted route lock, treat that as route drift. Record the mismatch, mark the turn as `blocked`, clear queued promotions, and return control to the orchestrator instead of half-applying the result.

## Preflight Gate

Before every routing decision and before every downstream invocation, run a preflight gate.

The preflight gate must verify at minimum:

- workflow state is initialized for the current run
- `current_phase` authorizes the intended `next_skill`
- `current_stage` authorizes the intended `next_skill`
- `confirmation_status` does not forbid execution for this turn
- `current_module` is valid for module-scoped work
- the selected module exists in the module index when module-scoped work is requested
- all required artifact paths for the intended move exist on disk
- all required maturity prerequisites are already confirmed, not merely implied
- the required phase freeze and frozen Pencil design source exist before restoration or code execution
- `platform_identifier` is explicit enough before validation or implementation work that depends on a concrete runtime surface

If any preflight check fails, stop immediately. Record the exact failed check as a blocker.

## Specialist Receipt Contract

Every downstream specialist result must be consumed as a structured receipt.

At minimum, the orchestrator must verify these receipt fields before applying any transition:

- `receipt_status`: `advanced`, `blocked`, `rejected`, or `not_executed`
- `current_phase`
- `design_artifact_type`: `prototype`, `effect_image`, `pencil`, `freeze`, `restoration`, `blueprint`, `code`, or `qa`
- `freeze_type`: `launch`, `premium`, or `none`
- `artifacts_produced`
- `status_updates`
- `evidence_paths`
- `execution_trace` when the step required real execution
- `blockers`

If the receipt is missing, ambiguous, or not provable from real artifacts, treat the result as `not_executed` or `blocked`.

Only the orchestrator may:

- change `current_phase`
- change `current_stage`
- set or clear `pending_next_stage`
- set or clear `pending_next_skill`
- set or clear `pending_status_updates`
- confirm that a receipt satisfies the route lock

## No-Progress Stop Rule

In `--auto` or `--full-auto` mode, every loop iteration must produce one of only two valid outcomes:

- the remaining workflow workload shrinks in a provable way
- a new real blocker is recorded

If neither happened, stop as route drift or empty progress.

## Subagent Execution Boundary

Subagents may execute specialist work, but they must not own workflow control.

### Orchestrator-only steps

These steps must stay in the orchestrator:

- choose or confirm `current_phase`
- choose or confirm `current_stage`
- choose or confirm `current_module`
- derive and persist the route lock
- run the preflight gate
- decide whether `scope_reopen` is required
- validate downstream receipts against the active route lock
- apply or reject pending transitions
- update orchestrator-owned workflow state as the single source of truth

### Subagent-eligible specialist stages

These stages may run in a subagent once the route is locked:

- `flutter-prd-rd-writer`
- `flutter-rd-module-splitter`
- `effect-image-to-pencil-design`
- Stitch MCP design-source execution for `stitch_design_source_branch`
- `flutter-design-freeze-gate`
- `pencil-design-to-flutter-restoration`
- asset-enhancement resolution, atlas analysis, atlas generation, background processing, slicing, and asset integration when the active phase already proved that atlas-backed assets are required
- `flutter-uiux-to-architecture`
- `flutter-init`
- `flutter-design-parity-reviewer`
- `flutter-visual-enhancement-branch`
- phase-matched implementation execution through `@superpowers`, `flutter-dev`, and `flutter-project-guardrails`

### Subagent constraints

- only one active route-locked specialist step may run at a time for the same workflow record
- module advancement remains serial by default
- subagents may not promote phase or stage on their own
- subagents may report blockers, but only the orchestrator may classify them as workflow-blocking

## Workflow Record

- On the first run, always initialize workflow state for the current run.
- Keep all phase and stage bookkeeping under one orchestrator-owned workflow state model.
- Read `references/workflow-record-contract.md` before initializing or persisting workflow state.
- Persist the active route lock and latest receipt evaluation so the next turn can detect route drift.

## Real Execution Trace

When executable implementation work is being advanced, keep a real execution trace in workflow state.

For each touched module, record:

- `current_phase`
- `current_module`
- why the module is the correct next module right now
- the exact delegated input
- the real generated or executed output
- whether the expected freeze already existed
- whether the expected restoration contract already existed
- whether code really advanced

If any item above did not really happen, write `not_executed` or `unknown` explicitly.

## Confirmation Gate

Treat confirmation as a workflow gate, not as a workflow stage.

| Confirmation Status | Meaning |
| --- | --- |
| `not_required` | The current routing decision does not need fresh user confirmation before execution. |
| `pending_confirmation` | The current step produced reviewable artifacts or status updates, but the workflow must not switch to the next process until the user explicitly confirms. |
| `confirmed` | The user explicitly approved the pending transition or pending status updates. |
| `rejected` | The user rejected the pending transition or pending status updates. |

When a specialist skill finishes and produces the required artifacts for a later stage or a new maturity level, do not immediately switch to the next process in manual mode. Keep the current confirmed phase and stage, set `confirmation_status=pending_confirmation`, record `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`, and wait for confirmation.

In `--auto`, auto-apply deterministic orchestrator-owned transitions.
In `--full-auto`, also auto-apply deterministic human-facing gates when exactly one supported default remains.

Do not create a fresh human confirmation gate when the user already approved the only supported upstream direction and the new artifact only proves that deterministic route.
Collapse stacked confirmations into one human decision when the later confirmations would not unlock any alternate downstream route.
Keep human confirmation only for true branch selection, unresolved reuse ambiguity, external project binding, or final human visual acceptance.

## Module Artifact Maturity

Track module maturity in addition to `current_phase` and `current_stage`.

### `scope_status`

| Value | Meaning |
| --- | --- |
| `not_started` | Module responsibility is not frozen yet. |
| `confirmed` | Module responsibility is frozen strongly enough for phase-matched prototype work. |

### `prototype_status`

| Value | Meaning |
| --- | --- |
| `not_started` | No phase-matched prototype exists yet. |
| `reviewable` | Prototype exists and is ready for structure review. |
| `frozen` | Prototype-derived structure is frozen for the active phase. |

### `design_source_status`

| Value | Meaning |
| --- | --- |
| `not_started` | No module-level design source exists yet. |
| `in_review` | Pencil or Stitch design source is under review. |
| `frozen` | The phase-matched design source packet is frozen and confirmed for restoration and code consumption. |

### `code_status`

| Value | Meaning |
| --- | --- |
| `not_started` | Code implementation has not started. |
| `in_progress` | Code work is actively being implemented. |
| `landed` | Code implementation is present and the landed status change has been explicitly confirmed. |
