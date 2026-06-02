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
next_skill: <skill-name-or-none>
```

## Required Sections

Keep this exact order:

1. `workflow_summary`
2. `current_stage_detail`
3. `current_module_detail`
4. `next_action`
5. `blockers`
6. `global_artifact_index`
7. `module_status_table`
8. `decision_log`

## Section Expectations

### `workflow_summary`

Summarize the project's overall workflow posture in 2-4 short lines.

### `current_stage_detail`

Record why the project is in the current stage and what must become true before the stage can advance.

### `current_module_detail`

Record the active module, or `not_selected` if the workflow is still global.

### `next_action`

Record the next skill, why it is next, and the minimum required inputs.

### `blockers`

List blockers explicitly. Use `none` if there are no blockers.

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

| module | current_state | next_skill | uiux_rd | impl_rd | global_guidelines | light_theme | dark_theme | pen_file | init_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

### `decision_log`

Append short dated entries only when a stage changes, a blocker is cleared, or a routing decision changes.

## Update Rules

- Update the metadata block on every orchestrator run.
- Keep `current_stage` and the active module row in sync.
- If `design-preview-to-global-guidelines` artifacts are created, update the relevant module row and move the stage to `global_guidelines_frozen`.
- If `flutter-init` completes, update the global artifact index with the project root, initialization summary, and `skills/flutter-dev/` path, then move the relevant stage to `project_initialized`.
- If a module is blocked, write the blocker both in the metadata summary section and in the module row.
- If the workflow completes, set `workflow_status: completed`.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not delete historical decisions from `decision_log`; append short entries instead.
- Do not hide blockers in prose outside the `blockers` section.
- Do not mark a stage as advanced until the required artifacts for that stage are actually available.
- Do not mark `project_initialized` unless both the scaffold and project-local `skills/flutter-dev/` exist.
