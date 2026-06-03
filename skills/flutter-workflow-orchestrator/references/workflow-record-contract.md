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
- whether the latest shared or module design draft has a visual review record
- whether that visual review record was produced in a fresh subagent
- whether a module document is still a split draft, already implementation-final, or already landed
- whether page-level Pen has landed for the active module
- whether code has landed for the active module
- what blockers still prevent the next move
- whether `flutter-init` has already produced the scaffold and project-local `skills/flutter-dev/`

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
current_stage: <workflow-state>
current_module: <module-name-or-not_selected>
confirmation_status: not_required | pending_confirmation | confirmed | rejected
next_skill: <skill-name-or-none>
pending_next_stage: <workflow-state-or-none>
pending_next_skill: <skill-name-or-none>
pending_status_updates: <module.field=target list-or-none>
```

Use `pending_status_updates` as a short semicolon-separated summary such as:

`home.uiux_status=implementation_final; home.impl_status=implementation_final`

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

### `pen_status`

- `not_started`
- `in_progress`
- `landed`

### `code_status`

- `not_started`
- `in_progress`
- `landed`

## Section Expectations

### `workflow_summary`

Summarize the project's overall workflow posture in 2-4 short lines.

Include whether the workflow is still in shared freeze, already in module draft split, or already in active module implementation preparation.

### `current_stage_detail`

Record why the project is in the current stage and what must become true before the stage can advance.

If the active module still has `split_draft` docs, say so explicitly here.

### `current_module_detail`

Record the active module, or `not_selected` if the workflow is still global.

Summarize the module's current `uiux_status`, `impl_status`, `pen_status`, and `code_status`.

Mention the latest module-level `visual_review` artifact when it exists, including whether it came from a fresh subagent run.

### `next_action`

Record the next skill, why it is next, and the minimum required inputs.

If the workflow is waiting for user confirmation, set the actionable `next_skill` to `none` and move the queued transition plus queued status changes into the confirmation section instead of pretending the next skill is already allowed to run.

If the workflow is `blocked`, do not point `next_skill` at the next process stage and do not preserve a stale queued transition or stale queued status change from a failed routing attempt.

### `confirmation_gate`

Record:

- `confirmation_status`
- why confirmation is or is not required
- `pending_next_stage`
- `pending_next_skill`
- `pending_status_updates`
- the user-facing confirmation target, such as which artifact pack, which document maturity upgrade, or which landed-state update is under review

If the workflow is waiting only on artifact maturity changes and not a stage switch, keep `pending_next_stage: none` but still persist `pending_status_updates`.

### `blockers`

List blockers explicitly. Use `none` if there are no blockers.

If the workflow is waiting on approval, include `waiting_for_user_confirmation` unless a stronger blocker already exists.

### `global_artifact_index`

Track project-level artifact paths when known, such as:

- PRD
- global technical baseline
- module index
- `global-design-guidelines.md`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`
- shared visual design review report
- whether the shared visual review was produced by a fresh subagent
- architecture summary
- Flutter project root
- `flutter-init` summary
- project-local `skills/flutter-dev/`

If the shared/public component freeze is tracked in a dedicated artifact, index it here too.

### `module_status_table`

Use one row per module with these columns:

| module | current_state | confirmation_status | next_skill | pending_next_stage | pending_next_skill | pending_status_updates | uiux_rd | uiux_status | impl_rd | impl_status | global_guidelines | light_theme | dark_theme | visual_review | pen_file | pen_status | code_status | init_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

Keep the row values on the last confirmed state. Proposed upgrades go into `pending_status_updates` until the user confirms them.

### `decision_log`

Append short dated entries only when a stage changes, a blocker is cleared, a routing decision changes, or a confirmed artifact maturity change is applied.

## Update Rules

- Update the metadata block on every orchestrator run.
- Keep `current_stage` and the active module row in sync.
- Keep `confirmation_status`, `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` in sync between the metadata block and the active module row.
- If `design-preview-to-global-guidelines` artifacts are created, update the relevant module row and queue `global_guidelines_frozen` in `pending_next_stage` instead of switching immediately.
- If `visual-design-reviewer` produces a shared review, index that artifact in `global_artifact_index` and note that it came from a fresh subagent. If it produces a module review, update the module row's `visual_review` and note the same.
- If a step result is ready for review, keep `current_stage` on the last confirmed stage, set `confirmation_status: pending_confirmation`, set `next_skill: none`, and record the candidate transition and candidate status changes in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- If the user confirms a pending transition, move `pending_next_stage` into `current_stage`, move `pending_next_skill` into `next_skill` only for that routing update, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed` for that update.
- If the user confirms only queued status changes and there is no stage switch, keep `current_stage` unchanged, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed` for that update.
- If the user rejects a pending transition or pending status change, keep the current confirmed stage and current confirmed maturity values, set `confirmation_status: rejected`, and write the rejection reason into blockers plus the decision log.
- If a step returns `blocked`, keep `current_stage` unchanged, clear `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` to `none`, and do not rewrite the module into the next workflow state or next maturity level.
- If `flutter-init` completes, update the global artifact index with the project root, initialization summary, and `skills/flutter-dev/` path, then queue the relevant stage as `project_initialized` instead of switching immediately.
- If a module is blocked, write the blocker both in the metadata summary section and in the module row.
- If the workflow completes, set `workflow_status: completed`.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not delete historical decisions from `decision_log`; append short entries instead.
- Do not hide blockers in prose outside the `blockers` section.
- Do not mark a stage as advanced until the required artifacts for that stage are actually available.
- Do not mark a maturity upgrade as confirmed until the artifact that proves it actually exists.
- Do not treat `split_draft` as implementation-ready.
- Do not mark `uiux_status=landed` or `impl_status=landed` before the corresponding page-level Pen is delivered and referenced.
- Do not mark `code_status=landed` before code output actually exists.
- Do not treat a complete design draft as freeze-ready when the required `visual_review` artifact is missing.
- Do not treat an inline parent-thread review as a valid `visual_review` artifact.
- Do not switch to the next process while `confirmation_status` is `pending_confirmation`.
- Do not store a queued transition or queued maturity change only in prose; always persist it in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- Do not keep `pending_next_stage`, `pending_next_skill`, or `pending_status_updates` populated after a `blocked` result.
- Do not rewrite `current_stage` to a later workflow state when the latest routing result is `blocked`.
- Do not mark `project_initialized` unless both the scaffold and project-local `skills/flutter-dev/` exist.
