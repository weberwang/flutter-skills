---
name: flutter-workflow
description: Use when coordinating a Flutter product workflow across requirements, launch-ready implementation, premium experience upgrade, Pencil design freezing, Flutter restoration, workflow state, or when the user asks what stage should happen next.
---

# Flutter Workflow

## Overview

This workflow now runs in two explicit phases:

1. `launchable_native_freeze`
2. `premium_experience_freeze`

Both phases use the same core design chain:

`prototype -> effect image -> Pencil design source -> design freeze -> Pencil-to-Flutter restoration -> implementation`

Prototype confirms structure and interaction.
Effect image confirms the visual target.
Pencil is the only frozen design source by default.
Flutter code restoration must default to the frozen Pencil design source instead of restoring directly from effect images.

`flutter-workflow` is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit confirmation in manual mode, and keeps one stable workflow truth model for the whole project.

On the first call for a target project root, run a lightweight git preflight before any downstream routing: check whether `.git/` already exists, whether `git status` is readable in that root, and whether a root `.gitignore` baseline already exists. If any repository-baseline item is missing, keep that finding in the route context and let `flutter-init` own the actual `git init` plus `.gitignore` creation or repair.

## Phase Model

### Phase 1: `launchable_native_freeze`

Goal: produce an App Store / Play Store-ready launch version with stable structure, complete key states, acceptable native Flutter experience, and a frozen launch Pencil design source.

This phase is not a low-quality MVP shortcut. It must reach release readiness.

Required sequence:

`product_scope_freeze`
-> `core_task_and_state_contract`
-> `page_flow_freeze`
-> `technical_baseline`
-> `compliance_and_release_constraints`
-> `project_init_and_bootstrap`
-> `module_scope_freeze`
-> `impl_contract_freeze`
-> `launch_prototype_build`
-> `launch_prototype_review_and_structure_freeze`
-> `launch_effect_image_generation`
-> `launch_pencil_design_generation`
-> `launch_design_freeze`
-> `launch_pencil_to_code_restoration`
-> `launch_asset_enhancement_resolution`
-> `native_ui_implementation`
-> `functional_complete`
-> `launch_quality_qa`
-> `release_readiness_gate`
-> `store_submission_ready`

### Phase 2: `premium_experience_freeze`

Goal: upgrade a launchable product into a more premium, visually stronger, and more refined experience while still using Pencil as the only frozen design source.

This phase is the mandatory visual and experience enhancement flow once the project explicitly enters Phase 2. The Phase 2 main chain itself is not optional. Both phases must pass through asset-enhancement resolution; only specific atlas-generation, background-processing, slicing, and bitmap-export techniques may be skipped when the frozen design does not require them.

Required sequence:

`upgrade_scope_selection`
-> `shared_design_direction`
-> `design_md_upgrade`
-> `premium_prototype_build`
-> `premium_prototype_review_and_structure_freeze`
-> `high_fidelity_effect_image_generation`
-> `premium_pencil_design_generation`
-> `premium_visual_freeze`
-> `premium_pencil_to_code_restoration`
-> `display_restoration_blueprint`
-> `visual_upgrade_implementation`
-> `asset_enhancement_resolution`
-> `design_parity_qa`
-> `human_visual_acceptance`

## Global Pencil Rule

Unless the user explicitly overrides the design-source branch, use `pencil_mcp_design_source_branch`.

- Default design source branch: `pencil_mcp_design_source_branch`
- Default frozen design artifact: confirmed Pencil design file
- Default code restoration path: `Pencil -> Flutter`
- Prototype is not the frozen design source
- Effect image is not the frozen design source
- No phase may skip the Pencil step before design freeze or code restoration

## Asset Enhancement Rule

Both phases must explicitly resolve asset-enhancement needs after Pencil-to-Flutter restoration and before code implementation is finalized.

- Phase 1 required node: `launch_asset_enhancement_resolution`
- Phase 2 required node: `asset_enhancement_resolution`

These nodes are always mandatory as decision points.

Inside each node:

- classify regions as `flutter_native`, `atlas_required`, or `placeholder_only`
- if no region is `atlas_required`, the node may finish without atlas outputs
- if any region is `atlas_required`, the workflow must continue through the deterministic atlas chain for those regions:
  - atlas analysis
  - atlas generation
  - background processing when needed
  - atlas slicing
  - asset integration back into the frozen design-source and implementation contract

Do not treat atlas generation and slicing as optional once the active phase has already proven that atlas-backed assets are required for fidelity.

## Design Source Branches

The workflow must lock exactly one explicit design-source branch for each active module before design-source generation starts.

Supported values:

- `pencil_mcp_design_source_branch`
- `stitch_design_source_branch`

Rules:

- `pencil_mcp_design_source_branch` is the default branch.
- When `design_source_branch=pencil_mcp_design_source_branch`, use `effect-image-to-pencil-design`.
- When `design_source_branch=stitch_design_source_branch`, use Stitch MCP with `model=GEMINI_3_1_PRO`, record `stitch_project_mode=new_project|existing_project`, and record `design_source_project_ref`.
- Freeze the resulting tool-specific design source, not the upstream effect image.
- Restore Flutter from the frozen design source instead of restoring directly from screenshots or effect images.

## Freeze Model

This workflow uses two distinct freeze types:

- `launch_design_freeze`
- `premium_visual_freeze`

### `launch_design_freeze`

Freezes the launch baseline:

- launch structure baseline
- launch task path
- launch primary CTA posture
- launch required states
- launch information-density posture
- launch Pencil design source
- launch native restoration expectations

### `premium_visual_freeze`

Freezes the premium enhancement baseline:

- upgraded structure baseline
- premium visual hierarchy
- premium component language
- premium motion posture
- premium Pencil design source
- premium restoration expectations
- approved visual deltas from the launch baseline

### Inheritance Rule

Phase 2 inherits the launch baseline by default.

Phase 2 may upgrade:

- visual hierarchy
- component language
- spacing rhythm
- motion and feedback posture
- imagery, texture, and asset strategy

Phase 2 may not silently rewrite:

- core task path
- primary CTA goal
- required state semantics
- module ownership

Phase 2 itself is not an optional side branch once premium enhancement work begins. The required Phase 2 chain must run through prototype, high-fidelity effect image, Pencil design source, premium visual freeze, restoration, implementation upgrade, and parity QA. Only the concrete asset-enhancement methods inside `asset_enhancement_resolution` remain conditional on actual design needs.

## Scope Reopen

Use `scope_reopen` when an enhancement request is no longer only a visual or experience upgrade.

Required triggers:

- `core_task_path_changed`
- `primary_cta_goal_changed`
- `page_flow_rewritten`
- `required_states_changed_semantically`
- `module_boundary_changed`
- `launch_freeze_invalidated`

If any trigger above is true, do not continue inside Phase 2 as a normal premium upgrade. Stop, record the trigger, and route back to the appropriate Phase 1 scope or contract step.

## Product Design Node Map

Use `@product-design` as a scoped design controller at specific workflow nodes instead of as a replacement for the whole Flutter workflow.

- requirements and clarification support -> `Product Design:get-context`
- shared direction exploration -> `Product Design:ideate`
- phase 1 effect-image generation -> `Product Design:ideate`
- phase 2 high-fidelity effect-image generation -> `Product Design:ideate`
- optional UX evidence gathering -> `Product Design:research` or `Product Design:audit`
- optional design QA helper -> `Product Design:design-qa`

`@product-design` owns direction and image generation quality. It does not own workflow control, freeze promotion, module routing, or Flutter implementation.

## Output Language Rule

Unless the user explicitly requests another language for a specific artifact, all workflow-generated human-readable project artifacts must use Simplified Chinese, including PRD text, notes, workflow records, review notes, and visible prototype copy.

## Required Reading

Read these references as needed:

- `references/workflow-states.md`
- `references/routing-rules.md`
- `references/control-contracts.md`
- `references/workflow-record-contract.md`
- `references/hard-rules.md`
- `references/execution-modes.md`
- `references/pressure-scenarios.md`

## Routing Procedure

For every invocation:

1. Ensure workflow state is initialized for the current run. If runtime persistence is enabled, use `references/workflow-record-contract.md` to shape the persisted artifact.
2. Run the git preflight on the first call for the target root.
3. Determine `execution_mode` and `current_phase`.
4. Read the existing workflow record and any required artifact indexes before choosing a route.
5. Derive and persist one route lock before invoking anything downstream.
6. Run the preflight gate from `references/control-contracts.md`. If it fails, record the exact blocker and stop.
7. Use `references/workflow-states.md` and `references/routing-rules.md` to select the next downstream skill or orchestrator-owned step.
8. If the step is subagent-eligible, delegate only the specialist work and require a structured receipt; keep workflow ownership in the orchestrator.
9. Validate the receipt against the active route lock before applying any transition or status update.
10. In manual mode, queue reviewable stage and status changes behind confirmation. In `--auto`, auto-apply deterministic orchestrator-owned transitions. In `--full-auto`, also auto-apply deterministic human-facing gates when exactly one supported default remains.
11. Update the orchestrator-owned workflow state as the single source of truth.
12. Return the output contract fields listed below.

## Delegation Boundary

Subagents may execute specialist work, but they must not own workflow control.

Only the orchestrator may:

- choose `current_phase`
- choose `current_stage`
- choose `current_module`
- persist route locks
- run preflight
- validate receipts
- classify blockers
- apply queued transitions
- decide whether `scope_reopen` is required
- update the workflow record

Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race. Module advancement remains serial by default.

## Implementation Boundary

Do not move a module into implementation execution until all of the following are true:

- the required phase freeze is complete
- the frozen Pencil design source exists for that phase
- the phase-matched Pencil-to-Flutter restoration contract exists
- the module `impl.md` is executable
- `display_restoration_blueprint_ready` is complete for the active implementation step
- `bootstrap_code_ready` exists
- the required global public code baseline is landed

For the launch phase, prefer Flutter SDK standard capabilities and keep high-cost visual enhancement branches closed unless explicitly justified.

For the premium phase, allow stronger fidelity and asset strategy, but still restore from the frozen Pencil design source instead of from screenshots directly.

For both phases, run the required asset-enhancement resolution node after Pencil restoration. If that node marks any region `atlas_required`, finish the corresponding atlas-generation and slicing chain before treating the implementation input packet as complete.

Whenever this workflow or any downstream skill needs to actually execute a Flutter or Dart command, prefer the `fvm` form first and fall back to bare `flutter` or `dart` only when the project contract already proves that `fvm` is unavailable or the user explicitly requires another contract.

## Output Contract

Return:

- `workflow_record_path`
- `workflow_record_update`
- `current_phase`
- `current_stage`
- `current_module`
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
