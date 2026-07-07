# Workflow Record Contract

Use this reference whenever `flutter-workflow` initializes workflow state or persists project workflow tracking into a runtime artifact.

All human-readable workflow-record content must default to Simplified Chinese unless the user explicitly requires another language for that artifact.

## Runtime Persistence

If persistence is needed, prefer an untracked runtime location such as:

`tmp/flutter-workflow/workflow-record.md`

Project-level durable workflow artifacts still default to `docs/project/` unless a downstream contract explicitly requires another path.

## Purpose

When persisted, this runtime artifact is the single stable source for workflow state for that run.

It must let any downstream agent answer:

- what phase the project is in now
- what stage the project is in now
- which module is active now
- whether the workflow is waiting for confirmation
- which phase freeze is active
- whether Phase 2 inherits the Phase 1 freeze
- which Pencil design source is frozen for the active phase
- whether the active phase has already completed asset-enhancement resolution
- whether any active region was classified as `atlas_required`
- whether a scope reopen is required
- what specialist skill should run next
- which artifacts already exist
- what blockers still prevent the next move

It should also be able to persist these review and design-control records:

- `commercial_surface_gate`
- `gate_owner`
- `failed_dimensions`
- `revision_target`
- recorded before any downstream promotion
- `commercial_design_exploration`
- `selected_direction`
- `structure_recomposition_decisions`
- `freeze_boundary`
- `mandatory_mobbin_reference`
- `reference_screen_evidence`
- `fixed_style_direction`
- `strong_hierarchy_contract`
- `hierarchy_contrast_ladder`
- `global_style_scheme`
- `global_style_experience_image`
- `theme_style_scope`
- `theme_and_style_only`
- `non_page_design_evidence`
- `no_global_page_design_draft`
- `page_design_deferred_to_module_stage`
- `minimal_default_copy_contract`
- `explanatory_copy_budget`
- `visible_explanation_count`
- `disclosure_destination`
- `explanation_overload`
- first module final effect image has been generated
- selected final effect-image direction path was actually available
- selected Product Design candidate
- manual image review
- human review result
- user confirmation or revision feedback

## Initialization Rule

On the first orchestrator run, if runtime persistence is enabled:

1. Create the runtime workflow-record artifact if it does not exist.
2. Fill every required section, even if some values are still unknown.
3. Use `not_started`, `not_selected`, `not_provided`, or `none` instead of leaving blanks.

## Required Metadata Block

Put this block at the top of the file:

```yaml
artifact_type: flutter_workflow_record
workflow_status: active | blocked | completed
execution_mode: manual | auto | full_auto
current_phase: launch | premium | scope_reopen
current_stage: <workflow-state>
current_module: <module-name-or-not_selected>
confirmation_status: not_required | pending_confirmation | confirmed | rejected
freeze_type: launch | premium | none
launch_freeze_version: <value-or-none>
premium_freeze_version: <value-or-none>
inherits_from_launch_freeze: yes | no
scope_reopen_required: yes | no
scope_reopen_reason: <summary-or-none>
next_skill: <skill-name-or-none>
pending_next_stage: <workflow-state-or-none>
pending_next_skill: <skill-name-or-none>
pending_status_updates: <module.field=target list-or-none>
route_lock: <phase|stage|module|skill|freeze|status summary-or-none>
execution_owner: orchestrator | subagent:<skill-name> | none
last_receipt_status: advanced | blocked | rejected | not_executed | route_drift | none
auto_progress_delta: <what actually advanced this turn-or-none>
launch_pencil_path: <path-or-none>
premium_pencil_path: <path-or-none>
launch_asset_resolution: pending | no_atlas_required | atlas_required_done | none
premium_asset_resolution: pending | no_atlas_required | atlas_required_done | none
```

## Required Sections

Keep this exact order:

1. `workflow_summary`
2. `phase_summary`
3. `current_stage_detail`
4. `current_module_detail`
5. `freeze_summary`
6. `next_action`
7. `confirmation_gate`
8. `blockers`
9. `global_artifact_index`
10. `module_status_table`
11. `decision_log`

## Module Status Table

Use one row per module with these columns:

| module | current_phase | current_stage | confirmation_status | next_skill | pending_next_stage | pending_next_skill | pending_status_updates | design_source_branch | design_source_type | launch_prototype_status | launch_pencil_status | launch_freeze_status | premium_prototype_status | premium_pencil_status | premium_freeze_status | launch_pencil_path | premium_pencil_path | restoration_status | launch_asset_resolution | premium_asset_resolution | code_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

## Section Expectations

### `workflow_summary`

Summarize the project posture in 2-4 short lines.

Include:

- current phase
- current stage
- whether the run is blocked
- whether the workflow is still auto-advancing when `execution_mode` is not manual

### `phase_summary`

Record:

- whether the workflow is in `launch`, `premium`, or `scope_reopen`
- whether the active phase freeze already exists
- whether the active phase inherits another freeze
- whether the active phase has already completed asset-enhancement resolution
- whether scope reopen is currently required

### `current_stage_detail`

Explain why the project is in the current stage and what must become true before the stage can advance.

If the active phase still lacks:

- a confirmed prototype
- a confirmed Pencil design source
- a confirmed phase freeze
- a confirmed restoration contract
- a confirmed asset-enhancement resolution result

say so explicitly and keep downstream work blocked.

If the active phase is `premium` and still lacks a confirmed effect image, say so explicitly and keep premium downstream work blocked.

### `freeze_summary`

Record:

- active `freeze_type`
- active freeze version
- inherited freeze version when the premium phase reuses the launch baseline
- allowed visual deltas
- forbidden deltas
- whether a scope reopen is required

### `global_artifact_index`

At minimum, index:

- PRD path
- page-navigation-flow path
- `DESIGN.md` path
- premium effect-image paths
- launch Pencil design source path
- premium Pencil design source path
- restoration contract paths
- launch asset-resolution result
- premium asset-resolution result
- display restoration blueprint path when it exists

## Update Rules

- Keep `current_phase` and `current_stage` in sync.
- If raw requirements are provided without a PRD artifact, keep the run in the shared pre-phase route until the PRD and navigation artifact exist.
- If the active phase is `launch`, do not record premium-only artifacts as if they already existed.
- If the active phase is `premium`, explicitly state whether the run inherits the launch freeze or has triggered `scope_reopen`.
- If a phase prototype is generated in manual mode, keep the current confirmed stage, queue the next stage, and wait for confirmation.
- If a premium phase effect image is generated in manual mode, keep the current confirmed stage, queue the next stage, and wait for confirmation.
- If a Pencil design source is generated in manual mode, keep the current confirmed stage, queue the next stage, and wait for confirmation.
- If asset-enhancement resolution completes in manual mode, keep the current confirmed stage, queue the next stage, and wait for confirmation.
- If a freeze evaluation fails, keep the current phase and stage unchanged, clear any queued freeze promotion, and route back to the correct upstream revision path.
- If `execution_mode=auto` or `execution_mode=full_auto`, apply deterministic queued transitions without pausing for ordinary downstream confirmation.
- Before any downstream invocation, persist one route lock that names the expected phase, stage, module, next skill, next stage delta, freeze type, and status delta.
- After any downstream invocation, evaluate the receipt against that route lock and store the result in `last_receipt_status`.
- If the receipt is missing, ambiguous, or not provable from real artifacts, store `last_receipt_status` as `not_executed` or `route_drift`, clear queued promotions, and stop advancement.
- If a scope-reopen trigger is discovered, update `current_phase=scope_reopen`, `scope_reopen_required=yes`, and record the exact reason before routing again.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not hide blockers outside the `blockers` section.
- Do not leave `current_phase`, `freeze_type`, `launch_pencil_path`, or `premium_pencil_path` blank once the corresponding phase has started.
- Do not mark a phase freeze as complete until the corresponding Pencil design source is actually confirmed.
- Do not record effect images as the frozen design source.
- Do not record Flutter restoration as direct-from-image when the active phase requires a Pencil design source.
- Do not mark a phase ready for implementation while its asset-enhancement resolution is still missing.
- Do not record `no_atlas_required` implicitly. Write it explicitly when the phase completed asset-enhancement resolution and no region required atlas outputs.
- Do not treat Phase 2 as a normal premium upgrade when `scope_reopen_required=yes`.
- Do not mark `code_status=landed` before code output actually exists.
