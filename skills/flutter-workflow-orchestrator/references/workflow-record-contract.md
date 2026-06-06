# Workflow Record Contract

Use this reference whenever `flutter-workflow-orchestrator` initializes or updates project workflow tracking.

## File Path

Always use this path:

`docs/rd/00-workflow-record.md`

Create parent directories if they do not exist.

## Purpose

This file is the single stable source for project workflow state. It should let any downstream agent answer:

- what stage the project is in now
- which module is active now
- whether the workflow is waiting for user confirmation
- which stage and skill are queued after confirmation
- which artifact maturity changes are queued after confirmation
- what skill should run next
- what artifacts already exist
- whether taste direction exists and which constraints it introduced
- whether freeze preparation already passed through `flutter-taste-router` textual normalization
- whether a shared or module design-source package has already been freeze-evaluated
- whether shared or module page-level static visual evidence already exists in the expected directories
- whether the accepted workflow preview set is confirmed as light-mode evidence
- whether shared/global effect-image generation stayed within the 3-image cap
- whether shared/global freeze already has the required approved effect images
- whether generated previews explicitly inherited the approved global style constraints
- whether implementation planning identified any non-native visual asset that should be generated through `$imagegen`
- whether display-layer readiness preflight is complete before implementation begins
- whether the display evidence pack is complete enough for fidelity-critical regions
- whether the architecture output classified important regions into `preserve_faithfully`, `flutterize`, or `simplify`
- whether a module document is still a split draft, already implementation-final, or already landed
- whether the active module's `.impl.md` records `superpowers_refinement_status`, and whether that status is truly evidenced by real execution
- whether the module design-source packet is frozen
- whether code has landed for the active module
- what blockers still prevent the next move
- whether `flutter-init` has already produced the scaffold and project-local `skills/flutter-dev/`
- whether the shared bootstrap-critical baseline is already clear enough to trigger `flutter-init`
- whether initialization has stopped at scaffold/bootstrap boundaries without starting feature implementation
- whether the orchestrator is currently running in manual mode or `--auto`
- whether `--auto` is still actively advancing remaining modules or has reached a valid stop condition
- what the active route lock is for the current turn
- whether the current turn is orchestrator-owned or delegated to a subagent
- whether the latest downstream receipt actually matched the locked route
- whether the latest auto iteration made provable progress or stopped on a blocker

## Initialization Rule

On the first orchestrator run:

1. Create `docs/rd/00-workflow-record.md` if it does not exist.
2. Fill every required section, even if some values are still unknown.
3. Use `not_started`, `not_selected`, `not_provided`, or `none` instead of leaving blanks.

## Required Metadata Block

Put this block at the top of the file:

```yaml
artifact_type: flutter_workflow_record
workflow_status: active | blocked | completed
execution_mode: manual | auto
current_stage: <workflow-state>
current_module: <module-name-or-not_selected>
confirmation_status: not_required | pending_confirmation | confirmed | rejected
next_skill: <skill-name-or-none>
pending_next_stage: <workflow-state-or-none>
pending_next_skill: <skill-name-or-none>
pending_status_updates: <module.field=target list-or-none>
route_lock: <stage|module|skill|stage_delta|status_delta summary-or-none>
execution_owner: orchestrator | subagent:<skill-name> | none
last_receipt_status: advanced | blocked | rejected | not_executed | route_drift | none
auto_progress_delta: <what actually advanced this turn-or-none>
```

Use `pending_status_updates` as a short semicolon-separated summary such as:

`home.uiux_status=implementation_final; home.impl_status=implementation_final; home.design_source_status=frozen`

## Required Sections

Keep this exact order:

1. `workflow_summary`
2. `current_stage_detail`
3. `current_module_detail`
4. `next_action`
5. `confirmation_gate`
6. `blockers`
7. `global_artifact_index`
8. `module_status_table`
9. `decision_log`

## Artifact Maturity Values

Use these values consistently:

### `uiux_status` and `impl_status`

- `not_started`
- `split_draft`
- `implementation_final`
- `landed`

### `design_source_status`

- `not_started`
- `in_review`
- `frozen`

### `code_status`

- `not_started`
- `in_progress`
- `landed`

## Section Expectations

### `workflow_summary`

Summarize the project's overall workflow posture in 2-4 short lines.

Include whether the workflow is still in shared freeze, already in module draft split, already in active module UI/UX refinement, or already in implementation.

If `execution_mode=auto`, also state whether the workflow is still auto-advancing or has stopped at the implementation boundary.

If `execution_mode=auto` and not all target modules are implementation-ready yet, explicitly name which modules are still pending and which module is being processed now.

### `current_stage_detail`

Record why the project is in the current stage and what must become true before the stage can advance.

If taste direction is missing before detailed UI/UX refinement, say so explicitly.

If the active module still has `split_draft` docs, say so explicitly.

If freeze preparation is in progress, state whether `flutter-taste-router` textual normalization is already complete and whether static-image directory inspection has already happened.

If previews are present, state whether the workflow is using the required light-mode preview baseline or an explicitly approved override.

Also state the current route lock for this turn and whether the next move is still inside that lock.

If the next move is delegated, also state which subagent-owned specialist step is running and what remains orchestrator-owned.

### `current_module_detail`

Record the active module, or `not_selected` if the workflow is still global.

Summarize the module's current `uiux_status`, `impl_status`, `design_source_status`, and `code_status`.

Also record the module's current `superpowers_refinement_status` when an `.impl.md` exists. If the active module has not truly gone through `@superpowers` refinement, say that explicitly.

Mention the latest freeze decision or blocker for that module when it exists.

If the module is entering implementation, mention whether its paired `ui-ux.md` and `impl.md` are both implementation-final and whether corresponding page-image evidence exists for display-layer landing.

If implementation planning already identified bitmap-only visual effects, mention whether they are pending generation, already saved into the project, or already wired into the implementation plan.

If display-layer work is about to begin, mention whether the readiness preflight passed, whether a concrete display-layer decision table already exists, whether the display evidence pack covers fidelity-critical regions, and whether those regions already have explicit fidelity classifications.

### `next_action`

Record the next skill, why it is next, and the minimum required inputs.

If the workflow is waiting for user confirmation, set the actionable `next_skill` to `none` and move the queued transition plus queued status changes into the confirmation section instead of pretending the next skill is already allowed to run.

If `execution_mode=auto`, do not hold the workflow at ordinary downstream confirmation gates. Auto-apply them until the implementation boundary or a blocker is reached.

If `execution_mode=auto`, `next_action` must describe the next real auto step for the same module or the next dependency-safe module. Do not write a pseudo-finished summary that leaves the remaining modules implicit.

If the workflow is `blocked`, do not point `next_skill` at the next process stage and do not preserve a stale queued transition or stale queued status change from a failed routing attempt.

If the latest downstream result drifted from the route lock, say so explicitly here and require the orchestrator to re-route instead of pretending the next move is already authorized.

If the current step is delegated, describe the expected receipt boundary instead of implying the subagent may decide the next workflow state.

### `confirmation_gate`

Record:

- `confirmation_status`
- why confirmation is or is not required
- `pending_next_stage`
- `pending_next_skill`
- `pending_status_updates`
- the user-facing confirmation target, such as which artifact pack, which document maturity upgrade, or which design-source freeze is under review

If the workflow is waiting only on artifact maturity changes and not a stage switch, keep `pending_next_stage: none` but still persist `pending_status_updates`.

### `blockers`

List blockers explicitly. Use `none` if there are no blockers.

If the workflow is waiting on approval, include `waiting_for_user_confirmation` unless a stronger blocker already exists.

If route drift, receipt mismatch, or no-progress auto advancement occurred, list that blocker explicitly instead of burying it inside the decision log only.

### `global_artifact_index`

Track project-level artifact paths when known, such as:

- PRD
- global technical baseline
- taste direction packet
- module index
- `global-design-guidelines.md`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`
- shared freeze evidence or freeze decision
- shared global preview image under `docs/rd/`
- whether the shared preview set is light mode or an explicitly approved override
- fidelity-critical display evidence pack paths when known
- architecture summary
- Flutter project root
- `flutter-init` summary
- project-local `skills/flutter-dev/`
- project-level `@superpowers` execution trace when one exists
- any approved generated bitmap assets that implementation must consume

When the chosen global preview originates from a module page, also index the copied module-local path so downstream implementation can trace the same image in both locations.

If the shared/public component freeze is tracked in a dedicated artifact, index it here too.

### `module_status_table`

Use one row per module with these columns:

| module | current_state | confirmation_status | next_skill | pending_next_stage | pending_next_skill | pending_status_updates | uiux_rd | uiux_status | impl_rd | impl_status | superpowers_refinement_status | global_guidelines | light_theme | dark_theme | taste_direction | visual_evidence | design_source_status | code_status | init_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

Keep the row values on the last confirmed state. Proposed upgrades go into `pending_status_updates` until the user confirms them.

If `execution_mode=auto`, the table must make it obvious which modules are already at the implementation boundary and which modules are still pending pre-implementation work.

### `decision_log`

Append short dated entries only when a stage changes, a blocker is cleared, a routing decision changes, or a confirmed artifact maturity change is applied.

When the workflow attempts module refinement in the default path, each dated entry should also capture the dependency-safe reason, the real `@superpowers` refinement input and output, and `未执行` when a claimed downstream step did not really happen.

When route drift, receipt mismatch, or no-progress auto stopping happens, add a dated entry that states the expected route lock, the actual downstream result, and why the orchestrator refused to advance.

## Update Rules

- Update the metadata block on every orchestrator run.
- Keep `current_stage` and the active module row in sync.
- Keep `confirmation_status`, `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` in sync between the metadata block and the active module row.
- Keep `route_lock`, `last_receipt_status`, and `auto_progress_delta` in sync with the latest routing turn.
- Keep `execution_owner` in sync with the latest routing turn.
- If taste direction is produced, index its artifact path in `global_artifact_index` and link it from active module rows when relevant.
- If `flutter-taste-router` completes textual normalization, record that status in the relevant summary or decision entry before any freeze promotion is queued.
- If freeze preparation inspects static-image directories, record whether existing evidence was reused, skipped due to missing environment variables, or newly generated.
- If previews are accepted for workflow use, record whether they satisfy the default light-mode requirement.
- If shared/global effect images were generated, record how many were generated and whether the run stayed within the 3-image cap.
- If shared/global freeze is under review, record whether the required approved effect images now exist or whether freeze is still blocked on image generation.
- If generated previews were created after a shared/global direction existed, record whether palette direction, typography mood, component family cues, CTA posture, visual system, and image treatment were explicitly inherited.
- If `design-preview-to-global-guidelines` artifacts are created, update the relevant module row and queue `global_guidelines_frozen` in `pending_next_stage` instead of switching immediately.
- If a freeze evaluation fails, keep the current stage unchanged, clear any queued freeze promotion, and route back to the correct upstream skill for exactly one scope-matched revision pass.
- If `execution_mode=auto`, the orchestrator should apply deterministic queued transitions and queued status updates without pausing for ordinary downstream confirmation, and it must stop only when the implementation boundary is reached or when a blocker appears.
- If `execution_mode=auto`, the orchestrator must not stop just because one module reached a local milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`.
- Before any downstream invocation, persist one route lock that names the expected stage, module, next skill, next stage delta, and status delta.
- Before any delegated specialist invocation, persist `execution_owner` as the exact subagent-owned step for this turn.
- After any downstream invocation, evaluate the receipt against that route lock and store the result in `last_receipt_status`.
- If the receipt is missing, ambiguous, or not provable from real artifacts, store `last_receipt_status` as `not_executed` or `route_drift`, clear queued promotions, and stop advancement.
- If the shared bootstrap-critical baseline is ready and the project scaffold is still missing, the orchestrator should prefer `flutter-init` before waiting for every feature module to reach later architecture milestones.
- If `execution_mode=auto`, after one module reaches a local milestone, immediately update `current_module`, `current_stage`, `next_skill`, the active module row, and `decision_log` to reflect the next real pre-implementation action.
- If `execution_mode=auto`, `current_module` means only the module being processed now. It must not imply that the current auto run is scoped to that single module.
- If `execution_mode=auto`, `workflow_summary` and `next_action` must explicitly state which modules remain to be advanced. Do not imply that auto is complete while target modules are still pending.
- If `execution_mode=auto`, do not use a generic "recommended next skill" as a stopping placeholder when unresolved target modules still exist. The record must reflect active continuation, not deferred manual pickup.
- If `execution_mode=auto`, each loop must either reduce the remaining pre-implementation work in a provable way or add a new blocker. Record that outcome in `auto_progress_delta`.
- If `execution_mode=auto` changed modules, rewrote `next_skill`, or rewrote stage posture without new proof or blocker, record `auto_progress_delta: none`, set a blocker, and stop.
- If the active module design-source packet is confirmed, queue or apply `design_source_status=frozen` according to the confirmation gate.
- If docs reference the frozen design-source packet and the user confirms, apply `uiux_status=landed` and `impl_status=landed`.
- If a step result is ready for review, keep `current_stage` on the last confirmed stage, set `confirmation_status: pending_confirmation`, set `next_skill: none`, and record candidate transitions and status changes in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- If the user confirms a pending transition, move `pending_next_stage` into `current_stage`, move `pending_next_skill` into `next_skill` only for that routing update, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed`.
- If the user confirms only queued status changes and there is no stage switch, keep `current_stage` unchanged, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed`.
- If the user rejects a pending transition or pending status change, keep the current confirmed stage and maturity values, set `confirmation_status: rejected`, and write the rejection reason into blockers plus the decision log.
- If a step returns `blocked`, keep `current_stage` unchanged, clear `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` to `none`, and do not rewrite the module into the next workflow state or next maturity level.
- If `flutter-init` completes, update the global artifact index with the project root, initialization summary, and `skills/flutter-dev/` path, then queue the relevant stage as `project_initialized` instead of switching immediately.
- If `flutter-init` completes, also record that feature implementation has not started yet and that initialization stopped at scaffold/bootstrap boundaries.
- If `flutter-init` has not run yet, record whether the shared bootstrap-critical baseline is already ready or still blocked, so the next routing decision can tell whether initialization should happen now.
- If the workflow is entering module refinement or module implementation, record that execution must be explicitly invoked through `@superpowers`; if corresponding page-image evidence exists, mention that display-layer landing should consult `$image-to-code`.
- If a selected module or its paired docs cannot be verified on disk, record the blocker and keep all refinement, freeze, and architecture trace fields as `未执行`, `not_executed`, or `unknown`.
- If architecture planning decides that a visual must become a bitmap asset, record the selected asset path or the pending `$imagegen` generation need explicitly.
- If display-layer readiness preflight is required, record whether the main preview, detail previews, structure semantics, display-layer decision table, fidelity classifications, and region-level evidence coverage are all ready.
- If a module is blocked, write the blocker both in the metadata summary section and in the module row.
- If the workflow completes, set `workflow_status: completed`.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not delete historical decisions from `decision_log`; append short entries instead.
- Do not hide blockers in prose outside the `blockers` section.
- Do not leave `route_lock`, `last_receipt_status`, or `auto_progress_delta` blank once routing has started.
- Do not leave `execution_owner` blank once a turn has selected local orchestration or delegated specialist ownership.
- Do not mark a stage as advanced until the required artifacts for that stage are actually available.
- Do not mark a maturity upgrade as confirmed until the artifact that proves it actually exists.
- Do not treat `split_draft` as implementation-ready.
- Do not mark `uiux_status=landed` or `impl_status=landed` before the docs reference a confirmed frozen design-source packet.
- Do not mark `code_status=landed` before code output actually exists.
- Do not claim static visual evidence was generated before recording whether the directory was checked first and whether the image environment variables were actually available.
- Do not accept preview evidence into the workflow record without stating whether it meets the default light-mode requirement.
- Do not accept shared/global preview evidence into the workflow record without stating whether the 3-image generation cap was respected.
- Do not accept generated preview evidence into the workflow record without stating whether the approved style constraints were explicitly inherited.
- Do not present shared/global freeze as ready in the workflow record while the required approved effect images are still missing.
- Do not hide a required `$imagegen` bitmap fallback inside prose without indexing the asset path or pending generation note.
- Do not mark a module ready for display-layer landing while the required preflight inputs or decision table are still missing.
- Do not mark a fidelity-critical module ready for display-layer landing while its evidence pack still lacks the detail, state, scroll, or overlay coverage needed for faithful implementation.
- Do not treat a complete design draft as freeze-ready when the design package is still incomplete.
- Do not switch to the next process while `confirmation_status` is `pending_confirmation`, unless `execution_mode=auto` and the next move is still before the implementation boundary.
- Do not let `execution_mode=auto` stop because one module reached a local completed state while other target modules still remain.
- Do not let `workflow_summary` or `next_action` present a single-module milestone as if the whole auto run were complete.
- Do not hide the remaining auto scope in prose. When `execution_mode=auto`, explicitly say which modules still need advancement.
- Do not write `next_skill: none` as if auto were finished when the real state is "this module is done but other modules remain".
- Do not store an "auto completed" interpretation when the actual state is only "one module reached a local stable node and the next module has not been selected yet".
- Do not store a queued transition or queued maturity change only in prose; always persist it in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- Do not let a downstream receipt redefine the locked route for the same turn.
- Do not let `execution_owner=subagent:*` imply that the subagent owns workflow bookkeeping or stage promotion.
- Do not treat a downstream recommendation, polished prose, or module switch by itself as progress.
- Do not keep auto running when `auto_progress_delta` is `none` and no new blocker was recorded.
- Do not keep `pending_next_stage`, `pending_next_skill`, or `pending_status_updates` populated after a `blocked` result.
- Do not rewrite `current_stage` to a later workflow state when the latest routing result is `blocked`.
- Do not mark `project_initialized` unless both the scaffold and project-local `skills/flutter-dev/` exist.
- Do not treat `project_initialized` as proof that any feature, page, or module implementation code already exists.
- Do not let `execution_mode=auto` enter `implementing` or set `code_status=in_progress`.
- Do not wait for every feature module to finish late-stage architecture planning before triggering `flutter-init` when the shared bootstrap-critical baseline is already sufficient.
- Do not hide the `@superpowers` implementation ownership or `$image-to-code` display-layer dependency when the module is already at the implementation boundary and those controls are relevant.
- Do not record a refinement or implementation step as valid if it was routed directly to a downstream execution skill without explicit `@superpowers` invocation.
- Do not infer `superpowers_refinement_status=verified_executed` from polished documents, manual backfill, or missing traces.
- Do not hide a missing module index row, missing paired docs, or other failed refinement precondition behind a later stage label.
- Do not require `pen_file`, `pen_status`, page-level Pen, `.pen`, or Pencil MCP data in the default workflow record.
