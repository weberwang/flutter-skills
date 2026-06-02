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
- what skill should run next
- what artifacts already exist
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
```

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

## Section Expectations

### `workflow_summary`

Summarize the project's overall workflow posture in 2-4 short lines.

### `current_stage_detail`

Record why the project is in the current stage and what must become true before the stage can advance.

### `current_module_detail`

Record the active module, or `not_selected` if the workflow is still global.

### `next_action`

Record the next skill, why it is next, and the minimum required inputs.

If the workflow is waiting for user confirmation, set the actionable `next_skill` to `none` and move the queued transition into the confirmation section instead of pretending the next skill is already allowed to run.

If the workflow is `blocked`, do not point `next_skill` at the next process stage and do not preserve a stale queued transition from a failed routing attempt.

### `confirmation_gate`

Record:

- `confirmation_status`
- why confirmation is or is not required
- `pending_next_stage`
- `pending_next_skill`
- the user-facing confirmation target, such as which artifact pack or stage output is under review

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
- architecture summary
- Flutter project root
- `flutter-init` summary
- project-local `skills/flutter-dev/`

### `module_status_table`

Use one row per module with these columns:

| module | current_state | confirmation_status | next_skill | pending_next_stage | pending_next_skill | uiux_rd | impl_rd | global_guidelines | light_theme | dark_theme | pen_file | init_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

### `decision_log`

Append short dated entries only when a stage changes, a blocker is cleared, or a routing decision changes.

## Update Rules

- Update the metadata block on every orchestrator run.
- Keep `current_stage` and the active module row in sync.
- Keep `confirmation_status`, `pending_next_stage`, and `pending_next_skill` in sync between the metadata block and the active module row.
- If `design-preview-to-global-guidelines` artifacts are created, update the relevant module row and queue `global_guidelines_frozen` in `pending_next_stage` instead of switching immediately.
- If a step result is ready for review, keep `current_stage` on the last confirmed stage, set `confirmation_status: pending_confirmation`, set `next_skill: none`, and record the candidate transition in `pending_next_stage` and `pending_next_skill`.
- If the user confirms a pending transition, move `pending_next_stage` into `current_stage`, move `pending_next_skill` into `next_skill`, clear both pending fields to `none`, and set `confirmation_status: confirmed` for that update.
- If the user rejects a pending transition, keep the current confirmed stage, set `confirmation_status: rejected`, and write the rejection reason into blockers plus the decision log.
- If a step returns `blocked`, keep `current_stage` unchanged, clear `pending_next_stage` and `pending_next_skill` to `none`, and do not rewrite the module into the next workflow state.
- If `flutter-init` completes, update the global artifact index with the project root, initialization summary, and `skills/flutter-dev/` path, then queue the relevant stage as `project_initialized` instead of switching immediately.
- If a module is blocked, write the blocker both in the metadata summary section and in the module row.
- If the workflow completes, set `workflow_status: completed`.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not delete historical decisions from `decision_log`; append short entries instead.
- Do not hide blockers in prose outside the `blockers` section.
- Do not mark a stage as advanced until the required artifacts for that stage are actually available.
- Do not switch to the next process while `confirmation_status` is `pending_confirmation`.
- Do not store a queued transition only in prose; always persist it in `pending_next_stage` and `pending_next_skill`.
- Do not keep `pending_next_stage` or `pending_next_skill` populated after a `blocked` result.
- Do not rewrite `current_stage` to a later workflow state when the latest routing result is `blocked`.
- Do not mark `project_initialized` unless both the scaffold and project-local `skills/flutter-dev/` exist.
