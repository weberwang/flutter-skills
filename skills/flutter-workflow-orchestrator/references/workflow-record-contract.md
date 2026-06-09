# Workflow Record Contract

Use this reference whenever `flutter-workflow-orchestrator` initializes workflow state or optionally persists project workflow tracking into a runtime artifact.

## Contents

- [Runtime Persistence](#runtime-persistence)
- [Purpose](#purpose)
- [Initialization Rule](#initialization-rule)
- [Required Metadata Block](#required-metadata-block)
- [Required Sections](#required-sections)
- [Artifact Maturity Values](#artifact-maturity-values)
- [Section Expectations](#section-expectations)
- [Update Rules](#update-rules)
- [Hard Rules](#hard-rules)

## Runtime Persistence

This contract describes the shape of a workflow-record artifact when the orchestrator chooses to persist runtime state.

Do not treat the artifact as a stable bundled skill resource. If persistence is needed, prefer an untracked runtime location such as:

`tmp/flutter-workflow-orchestrator/workflow-record.md`

Create parent directories only for the current run when persistence is actually enabled.

Project-level durable workflow artifacts default to `docs/project/` unless a downstream contract or the user explicitly requires another path. Runtime workflow state remains outside that tree.

## Purpose

When persisted, this runtime artifact is the single stable source for project workflow state for that run. It should let any downstream agent answer:

- what stage the project is in now
- which module is active now
- whether the workflow is waiting for user confirmation
- which stage and skill are queued after confirmation
- which artifact maturity changes are queued after confirmation
- what skill should run next
- what artifacts already exist
- whether raw requirements have been captured before PRD generation
- whether requirements brainstorming has produced a question ledger
- whether PRD decision-blocking questions are resolved, defaulted, or still blocked
- where the generated PRD artifact lives
- whether the global visual design direction has already been brainstormed before asking the user to confirm it
- whether the workflow used a confirmed Product Design brief, approved visual source, or Product Design recommendation artifact before final design-direction confirmation
- whether the target design-device preset and base resolution are already frozen for the current design cycle
- which iPhone preset or custom viewport was selected
- whether the common public shell has already been explicitly agreed before any effect-image generation starts
- whether the final product design direction has been confirmed with the user after the Product Design brief and direction step
- whether a root-level `DESIGN.md` already exists for the confirmed final design direction
- whether `DESIGN.md` already captures task-priority and first-screen CTA rules
- whether `DESIGN.md` already captures interaction and feedback rules
- whether `DESIGN.md` already captures responsive and multi-device rules
- whether `DESIGN.md` already captures critical-state coverage and edge-case behavior
- whether `DESIGN.md` already captures content tone and naming rules when relevant
- whether one representative light-mode effect image has been generated before remaining optional page-image generation starts
- whether the representative effect image is pending confirmation, confirmed, or rejected
- whether every page in scope has an approved light-mode effect image when the optional full effect-image branch is active
- whether taste direction exists and which constraints it introduced
- whether `platform_baseline` exists and whether `platform_identifier` has been explicitly verified
- whether freeze preparation already passed through `flutter-taste-router` textual normalization
- whether a shared or module design-source package has already been freeze-evaluated
- whether freeze evaluation already verified task hierarchy, CTA discoverability, interaction feedback, responsive strategy, and critical-state coverage
- whether the chosen `design_source_adapter` is Stitch or Pencil
- whether Stitch MCP was available and which `modelId` was used for structured design-source generation or validation
- whether `stitch_project_mode` is confirmed as `new` or `existing` before Stitch design-source work starts
- whether `stitch_project_id` is confirmed and frozen after the Stitch project mode choice
- whether Stitch page design ran in page-scoped subagents and whether the batch respected the 6-subagent concurrency cap
- whether every in-scope page has a successful page-level Stitch receipt before packet merge and freeze
- whether Stitch restoration downloaded image assets for direct use, and where those assets were saved
- whether the Stitch design-source packet has been checked against its source effect image or approved visual comp
- whether the active module's high-fidelity visual contract was evaluated as the first module design-freeze priority
- whether shared or module page-level static visual evidence already exists in the expected directories
- whether the accepted workflow effect-image set is confirmed as optional light-mode evidence
- whether shared/global effect-image generation covers all pages in the approved product scope
- whether shared/global freeze already has the approved effect images required by the active revision path, if any
- whether generated effect images explicitly inherited the approved global style constraints
- whether module-stage effect-image generation stayed disabled by default unless `--preview` was explicitly enabled
- whether `global-design-guidelines.md` records the current effect-image policy and generated global effect-image paths
- whether implementation planning identified any non-native visual asset that still needs MCP-driven generation or rework
- whether display-layer readiness preflight is complete before implementation begins
- whether the display evidence pack is complete enough for fidelity-critical regions
- whether the architecture output classified important regions into `preserve_faithfully`, `flutterize`, or `simplify`
- whether a module implementation document is missing, already implementation-final, or already landed
- whether executable module document generation has real artifact and receipt evidence when delegated execution was used
- whether the module design-source packet is frozen
- whether code has landed for the active module
- what blockers still prevent the next move
- whether `flutter-init` has already produced the directory skeleton and project-local `skills/flutter-dev/`
- whether the shared bootstrap-critical baseline is already clear enough to trigger `flutter-init`
- whether initialization has stopped at directory-creation boundaries without starting bootstrap or feature implementation
- whether the separate bootstrap code stage has landed the required global public code baseline
- whether the orchestrator is currently running in manual mode or `--auto`
- whether `--auto` is still actively advancing remaining modules or has reached a valid stop condition
- what the active route lock is for the current turn
- whether the current turn is orchestrator-owned or delegated to a subagent
- whether the latest downstream receipt actually matched the locked route
- whether the latest auto iteration made provable progress or stopped on a blocker

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

`home.impl_status=implementation_final; home.design_source_status=frozen`

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

### `impl_status`

- `not_started`
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

Include whether the workflow is still in requirements brainstorming, PRD generation, Product Design brief confirmation, Product Design recommendation review, final product design direction confirmation, `DESIGN.md` output, optional representative effect-image confirmation, optional remaining page-effect generation, shared freeze, module `impl.md` generation, module page component drafting, module freeze, bootstrap code generation, code implementation, or human visual inspection handoff.

If `execution_mode=auto`, also state whether the workflow is still auto-advancing or has stopped at workflow completion.

If `execution_mode=auto` and not all target modules are fully implemented yet, explicitly name which modules are still pending and which module is being processed now.

### `current_stage_detail`

Record why the project is in the current stage and what must become true before the stage can advance.

If the global visual design direction has not yet been brainstormed, say so explicitly and keep final product design direction confirmation blocked.

If the target design-device preset or base resolution is still missing, say so explicitly and keep Product Design brief confirmation, visual recommendation, and optional effect-image generation blocked.

If the common public shell has not yet been explicitly agreed, say so explicitly and keep design-direction confirmation plus optional effect-image generation blocked.

If the final product design direction has not been confirmed, say so explicitly and keep `DESIGN.md`, structured design-source work, and optional image generation blocked.

If the root-level `DESIGN.md` is missing after final product direction confirmation, say so explicitly and keep structured design-source work blocked.

If `DESIGN.md` exists but still lacks task-priority, interaction-feedback, responsive-strategy, critical-state, or content-tone coverage that the product clearly needs, say so explicitly and keep freeze and design-source work blocked.

If the representative effect image exists but is still waiting for user confirmation, say so explicitly and keep remaining optional page-image generation blocked.

If taste direction is missing before detailed design-source work, say so explicitly.

If the workflow is still in requirements brainstorming, state whether raw requirements are captured, whether the PRD question ledger exists, which decision-blocking questions remain, and whether a PRD artifact has been generated.

If the shared/global design freeze is not complete yet, say so explicitly and keep all module-related workflow blocked.

If the active module lacks an executable `impl.md`, say so explicitly.

If freeze preparation is in progress, state whether `flutter-taste-router` textual normalization is already complete and whether static-image directory inspection has already happened.

If module design freeze is in progress, state whether the module function is already fixed in `impl.md`, whether the module-scoped display-layer design draft already exists, and whether the high-fidelity visual contract has passed, is explicitly reduced by design-source control, or is blocking freeze.

If effect images are present, state whether the workflow is using the optional light-mode effect-image baseline or an explicitly approved override.

If the workflow is moving toward freeze, architecture, or implementation, state whether `platform_identifier` is already explicit, and do not treat `platform_baseline` as a substitute.

If the workflow is in or beyond `project_initialized`, state whether bootstrap code is still pending or already landed.

Also state the current route lock for this turn and whether the next move is still inside that lock.

If the next move is delegated, also state which subagent-owned specialist step is running and what remains orchestrator-owned.

### `current_module_detail`

Record the active module, or `not_selected` if the workflow is still global.

Summarize the module's current `impl_status`, `design_source_status`, and `code_status`.

Also record the module's current generation or execution trace status when an `.impl.md` exists and delegated execution was required. If the executable `impl.md` cannot be proven from real artifacts, say that explicitly.

Mention the latest freeze decision or blocker for that module when it exists.

Mention the module's current `high_fidelity_freeze_status` when module freeze, architecture, or implementation-readiness is being considered.

If the module is entering implementation, mention whether its `impl.md` is implementation-final, whether it references the frozen selected structured design-source packet, whether the frozen module display-layer design draft already exists, and whether corresponding page-image evidence exists for display-layer landing.

If implementation planning already identified bitmap-only visual effects, mention whether they are pending generation, already saved into the project, or already wired into the implementation plan.

If display-layer work is about to begin, mention whether the readiness preflight passed, whether a concrete display-layer decision table already exists, whether the display evidence pack covers fidelity-critical regions, whether those regions already have explicit fidelity classifications, and whether the required non-display behavior contracts have already stabilized for faithful display restoration.

### `next_action`

Record the next skill, why it is next, and the minimum required inputs.

If the workflow is waiting for user confirmation, set the actionable `next_skill` to `none` and move the queued transition plus queued status changes into the confirmation section instead of pretending the next skill is already allowed to run.

If `execution_mode=auto`, do not hold the workflow at ordinary downstream confirmation gates. Auto-apply them until workflow completion or a blocker is reached.

If `execution_mode=auto`, `next_action` must describe the next real auto step for the same module or the next serial module. Do not write a pseudo-finished summary that leaves the remaining modules implicit.

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

- raw requirement source or intake summary
- requirements brainstorming notes
- PRD question ledger
- PRD
- Product Design brief or recommendation packet
- frozen design-device preset and base resolution record
- design confirmation mode
- design recommendation packet
- public shell confirmation record
- final product design direction confirmation record
- root-level `DESIGN.md`
- DESIGN.md quality audit
- representative effect image path
- representative effect image page
- representative effect image status
- all-page light-mode effect-image set and approval status, when the optional full image branch is active
- global technical baseline
- taste direction packet
- verified platform identifier or target validation surface
- module index
- `global-design-guidelines.md`
- chosen `design_source_adapter`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`
- shared freeze evidence or freeze decision
- shared global effect-image directory under `docs/project/`
- Stitch design-source packet path and `modelId`
- frozen `stitch_project_mode`
- frozen `stitch_project_id`
- Stitch page-design batch id or trace path
- page-level Stitch receipt paths
- downloaded Stitch image asset source paths or URLs
- downloaded Stitch image asset local paths
- Stitch source effect-image paths
- Stitch-vs-effect-image validation result
- whether the shared effect-image set is light mode or an explicitly approved override
- effect-image policy recorded in `global-design-guidelines.md`
- fidelity-critical display evidence pack paths when known
- architecture summary
- Flutter project root
- `flutter-init` directory-creation summary
- project-local `skills/flutter-dev/`
- bootstrap code artifact summary or execution trace
- project-level `@superpowers` execution trace when one exists
- any approved generated bitmap assets that implementation must consume

When the chosen global effect image originates from a module page, keep only the global effect-image path under `docs/project/`; do not require or index a copied module-local path.

If the shared/public component freeze is tracked in a dedicated artifact, index it here too.

### `module_status_table`

Use one row per module with these columns:

| module | current_state | confirmation_status | next_skill | pending_next_stage | pending_next_skill | pending_status_updates | design_source_adapter | design_source_project_mode | design_source_project_ref | design_source_packet | effect_images | impl_rd | impl_status | generation_trace_status | global_guidelines | light_theme | dark_theme | taste_direction | visual_evidence | high_fidelity_freeze_status | design_source_status | code_status | init_status | blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Update the existing row for a module instead of creating duplicates.

Keep the row values on the last confirmed state. Proposed upgrades go into `pending_status_updates` until the user confirms them.

If `execution_mode=auto`, the table must make it obvious which modules are already fully implemented and which modules are still pending later workflow work.

### `decision_log`

Append short dated entries only when a stage changes, a blocker is cleared, a routing decision changes, or a confirmed artifact maturity change is applied.

When the workflow attempts executable module document generation in the default path, each dated entry should also capture the confirmed serial-module-order reason, the real generation input and output, and `未执行` when a claimed downstream step did not really happen.

When route drift, receipt mismatch, or no-progress auto stopping happens, add a dated entry that states the expected route lock, the actual downstream result, and why the orchestrator refused to advance.

## Update Rules

- Update the metadata block on every orchestrator run.
- Keep `current_stage` and the active module row in sync.
- Keep `confirmation_status`, `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` in sync between the metadata block and the active module row.
- Keep `route_lock`, `last_receipt_status`, and `auto_progress_delta` in sync with the latest routing turn.
- Keep `execution_owner` in sync with the latest routing turn.
- If raw requirements are provided without a PRD artifact, set or keep `current_stage=requirements_brainstorming`, index the raw requirement source or intake summary, and record whether the PRD question ledger exists.
- If requirements brainstorming resolves decision-blocking questions, index the generated PRD artifact and queue `pending_next_stage=prd_ready` instead of silently jumping to technical baseline.
- If decision-blocking questions remain unresolved, record them in `required_inputs` or `blockers`, keep `current_stage=requirements_brainstorming`, and do not route to technical baseline, taste direction, executable module document generation, architecture, or implementation.
- If a default is used to answer a PRD question, record the assumption, rationale, and risk in the workflow record or PRD artifact index.
- If the PRD exists but the global visual design direction has not yet been brainstormed, keep `DESIGN.md`, structured design-source work, and optional effect-image generation blocked and route first to `@product-design` brief confirmation or visual-direction recommendation as needed. If richer commercial evidence is needed before confirmation, record the pending pre-direction Creative Production branch explicitly instead of treating `flutter-taste-router` as the primary direction owner.
- If the technical baseline exists but the target design-device preset or base resolution is still missing, keep `current_stage=technical_baseline_ready`, record `required_inputs=design_device_preset_and_resolution`, and do not route to Product Design brief confirmation yet. In `--auto`, if the viewport is still missing, record that `390 x 844 px` was auto-selected.
- If the global visual direction exists but the common public shell has not yet been agreed, keep design-direction confirmation and optional effect-image generation blocked, record `required_inputs=public_shell_confirmation`, and do not route to representative or full page-effect generation.
- If the brainstormed direction exists but the final product design direction has not been confirmed with the user, keep `DESIGN.md`, structured design-source work, and optional effect-image generation blocked, record `required_inputs=final_product_design_direction_confirmation`, and do not route to downstream design-source generation.
- If final product design direction is confirmed but the shared or module freeze packet is still not standardized, route to `flutter-taste-router` for textual normalization and freeze-contract consolidation before any freeze promotion is queued.
- If final product design direction is confirmed, index the confirmation artifact or decision-log entry before writing the root-level `DESIGN.md` or generating any optional effect image.
- If the root-level `DESIGN.md` is written, index its path before generating any structured design source.
- If `DESIGN.md` captures task priority, first-screen CTA posture, interaction feedback, responsive strategy, critical states, and content tone, record that quality audit explicitly. If not, record the missing areas as blockers before structured design-source generation.
- If no representative effect image exists yet and the optional effect-image branch is active in manual mode, generate exactly one representative effect image first, index its path and selected page, set `confirmation_status=pending_confirmation`, and stop before generating remaining page images.
- If the representative effect image is still pending confirmation or has been rejected in manual mode, keep remaining optional page-image generation blocked and do not advance to the broader optional page-image generation step.
- If the representative effect image is confirmed in manual mode, record that confirmation explicitly before generating the remaining optional page-effect set.
- If `execution_mode=auto` and `--preview` is active, generate the in-scope effect images automatically, record their paths, and do not create a confirmation stop.
- If taste direction is produced, index its artifact path in `global_artifact_index` and link it from active module rows when relevant.
- If `platform_identifier` becomes explicit, record it in the relevant summary or artifact index instead of leaving it implicit in prose.
- If `flutter-taste-router` completes textual normalization, record that status in the relevant summary or decision entry before any freeze promotion is queued.
- If freeze preparation inspects static-image directories, record whether existing evidence was reused, skipped due to missing environment variables, or newly generated.
- If effect images are accepted for workflow use, record whether they satisfy the default light-mode requirement.
- If Stitch is used as the structured design source, record the Stitch packet path, `modelId`, source effect-image paths, page-level Stitch receipt paths, downloaded image asset source/local paths, page-design batch concurrency, and Stitch-vs-effect-image validation result.
- Before any Stitch design-source generation or validation, verify that `stitch_project_mode` is confirmed as `new` or `existing`. If it is missing or ambiguous, record `stitch_status=blocked_missing_project_mode`, keep the current stage unchanged, and stop with `required_inputs=stitch_project_mode:new_or_existing`.
- After `stitch_project_mode` is confirmed, record how the id is obtained. For `new`, create the Stitch project and freeze the returned `stitch_project_id`; if creation cannot return a frozen id, record `stitch_status=blocked_project_creation` and stop with `required_inputs=stitch_project_creation`. For `existing`, verify that the user-provided `stitch_project_id` is confirmed and frozen; if it is missing, ambiguous, or mutable, record `stitch_status=blocked_missing_project_id`, keep the current stage unchanged, and stop with `required_inputs=stitch_project_id`.
- If `stitch_project_mode` or `stitch_project_id` changes after being frozen, route through `flutter-design-source-control` and treat existing Stitch packets as needing revalidation.
- If Stitch MCP is required but unavailable in the current tool context, record `stitch_status=unavailable`, keep the relevant freeze blocked, and do not silently fall back to raw effect images as the only design source.
- If Stitch page design is delegated, record the page-to-subagent assignment, enforce `stitch_parallel_limit=6`, and keep workflow record updates orchestrator-owned.
- If any page-level Stitch receipt is missing or blocked, keep `design_source_status` out of `frozen`, record the failed page, and stop packet freeze.
- If a Stitch page subagent downloads image assets for direct use, index each source URL or artifact path, local asset path, owning page, intended component/region, and direct-use decision.
- If a required downloaded image asset is missing, keep the relevant Stitch packet unfrozen and record the missing asset as a blocker.
- If shared/global effect images were generated, record the complete page list, one approved image path per page, and whether every in-scope page is covered for that optional branch.
- If the representative effect image was generated, record its path, selected page, and approval status.
- If shared/global freeze is under review, record whether the approved effect images required by the active revision path now exist or whether that path is still blocked on image generation.
- If shared/global freeze is under review, record whether task hierarchy, CTA discoverability, interaction feedback, responsive strategy, and critical-state coverage were explicitly verified.
- If generated effect images were created after a shared/global direction existed, record whether palette direction, typography mood, component family cues, CTA posture, visual system, and image treatment were explicitly inherited.
- If shared/global effect images were created, record the frozen base design viewport they were generated against.
- If `design-preview-to-global-guidelines` artifacts are created, update the relevant module row and queue `global_guidelines_frozen` in `pending_next_stage` instead of switching immediately.
- If a freeze evaluation fails, keep the current stage unchanged, clear any queued freeze promotion, and route back to the correct upstream skill for exactly one scope-matched revision pass.
- If `execution_mode=auto`, the orchestrator should apply deterministic queued transitions and queued status updates without pausing for ordinary downstream confirmation, and it must otherwise stop only when workflow completion is reached or when a blocker appears.
- If `execution_mode=auto`, the orchestrator must not stop just because one module reached a local milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`.
- Before any downstream invocation, persist one route lock that names the expected stage, module, next skill, next stage delta, and status delta.
- Before any delegated specialist invocation, persist `execution_owner` as the exact subagent-owned step for this turn.
- After any downstream invocation, evaluate the receipt against that route lock and store the result in `last_receipt_status`.
- If the receipt is missing, ambiguous, or not provable from real artifacts, store `last_receipt_status` as `not_executed` or `route_drift`, clear queued promotions, and stop advancement.
- If the shared bootstrap-critical baseline is ready and the project directory skeleton is still missing, the orchestrator should prefer `flutter-init` before waiting for every feature module to reach later architecture milestones.
- If `execution_mode=auto`, after one module reaches a local milestone, immediately update `current_module`, `current_stage`, `next_skill`, the active module row, and `decision_log` to reflect the next real workflow action in the confirmed serial module order.
- If `execution_mode=auto`, `current_module` means only the module being processed now. It must not imply that the current auto run is scoped to that single module.
- If `execution_mode=auto`, `workflow_summary` and `next_action` must explicitly state which modules remain to be advanced. Do not imply that auto is complete while target modules are still pending.
- If `execution_mode=auto`, do not use a generic "recommended next skill" as a stopping placeholder when unresolved target modules still exist. The record must reflect active continuation, not deferred manual pickup.
- If `execution_mode=auto`, each loop must either reduce the remaining workflow work in a provable way or add a new blocker. Record that outcome in `auto_progress_delta`.
- If `execution_mode=auto` changed modules, rewrote `next_skill`, or rewrote stage posture without new proof or blocker, record `auto_progress_delta: none`, set a blocker, and stop.
- If module design freeze is evaluated, record `high_fidelity_freeze_status` as `passed`, `approved_reduction`, `blocked`, or `not_evaluated`. Do not queue `design_source_status=frozen` when the value is `blocked` or `not_evaluated`.
- If the active module design-source packet is confirmed, queue or apply `design_source_status=frozen` according to the confirmation gate.
- If the module `impl.md` references the frozen selected structured design-source packet and the user confirms, apply `impl_status=landed`.
- If a step result is ready for review, keep `current_stage` on the last confirmed stage, set `confirmation_status: pending_confirmation`, set `next_skill: none`, and record candidate transitions and status changes in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- If the user confirms a pending transition, move `pending_next_stage` into `current_stage`, move `pending_next_skill` into `next_skill` only for that routing update, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed`.
- If the user confirms only queued status changes and there is no stage switch, keep `current_stage` unchanged, apply `pending_status_updates`, clear all pending fields to `none`, and set `confirmation_status: confirmed`.
- If the user rejects a pending transition or pending status change, keep the current confirmed stage and maturity values, set `confirmation_status: rejected`, and write the rejection reason into blockers plus the decision log.
- If a step returns `blocked`, keep `current_stage` unchanged, clear `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` to `none`, and do not rewrite the module into the next workflow state or next maturity level.
- If `flutter-init` completes, update the global artifact index with the project root, directory-creation summary, and `skills/flutter-dev/` path, then queue the relevant stage as `project_initialized` instead of switching immediately.
- If `flutter-init` completes, also record that bootstrap code and feature implementation have not started yet and that initialization stopped at directory-creation boundaries.
- If `flutter-init` has not run yet, record whether the shared bootstrap-critical baseline is already ready or still blocked, so the next routing decision can tell whether initialization should happen now.
- If bootstrap code lands after initialization, record the execution summary or trace, the covered global public code baseline, and queue or apply `bootstrap_code_ready`.
- If the workflow is entering delegated module document generation or module implementation, record that execution must be explicitly invoked through `@superpowers`; if corresponding page-image evidence exists, mention that display-layer landing should consult the page image and frozen design evidence.
- If the workflow is entering implementation, record whether `@superpowers` `Spec` exists, whether `@superpowers` `Plan` exists, and do not treat execution as authorized before both exist.
- If implementation execution begins, record the active serial module order, the current active module, and any explicitly approved ownership split. Default expectation is serial module execution.
- If a selected module, module index row, executable module `impl.md`, or required Stitch design-source packet cannot be verified on disk, record the blocker and keep all generation, freeze, and architecture trace fields as `未执行`, `not_executed`, or `unknown`.
- If architecture planning decides that a visual must become a bitmap asset, record the selected asset path or the pending MCP-driven generation need explicitly.
- If display-layer readiness preflight is required, record whether the main effect image, detail effect images, structure semantics, display-layer decision table, fidelity classifications, region-level evidence coverage, and non-display behavior readiness are all ready.
- If a module is blocked, write the blocker both in the metadata summary section and in the module row.
- If the workflow completes, set `workflow_status: completed`.

## Hard Rules

- Do not create separate workflow state files per module.
- Do not delete historical decisions from `decision_log`; append short entries instead.
- Do not hide blockers in prose outside the `blockers` section.
- Do not treat raw requirements as `prd_ready` until a PRD artifact exists and decision-blocking questions are resolved or explicitly defaulted.
- Do not route from raw demand directly into technical baseline, taste direction, executable module document generation, architecture, or implementation.
- Do not record PRD assumptions as facts unless their rationale and risk are explicit.
- Do not treat `platform_baseline` as if it already verified the real target surface.
- Do not leave `route_lock`, `last_receipt_status`, or `auto_progress_delta` blank once routing has started.
- Do not leave `execution_owner` blank once a turn has selected local orchestration or delegated specialist ownership.
- Do not mark a stage as advanced until the required artifacts for that stage are actually available.
- Do not mark a maturity upgrade as confirmed until the artifact that proves it actually exists.
- Do not treat a missing or non-executable module `impl.md` as implementation-ready.
- Do not mark `impl_status=landed` before the module `impl.md` references a confirmed frozen selected structured design-source packet.
- Do not mark `design_source_status=frozen` for module implementation when `high_fidelity_freeze_status` is `blocked`, `not_evaluated`, or missing.
- Do not mark `code_status=landed` before code output actually exists.
- Do not claim static visual evidence was generated before recording whether the directory was checked first and whether `gpt-image-2-generator` for that branch was actually available.
- Do not accept effect-image evidence into the workflow record without stating whether it meets the default light-mode requirement.
- Do not mark a Stitch design-source packet as frozen before recording the source effect-image paths, `modelId`, and validation result.
- Do not mark a Stitch design-source packet as frozen before recording the frozen `stitch_project_mode`.
- Do not mark a Stitch design-source packet as frozen before recording the frozen `stitch_project_id`.
- Do not mark a Stitch design-source packet as frozen before recording successful page-level Stitch receipts for every in-scope page.
- Do not mark a Stitch design-source packet as frozen before recording local paths for every downloaded image asset required for direct implementation use.
- Do not store literal Stitch API keys in the workflow record.
- Do not accept shared/global effect-image evidence into the workflow record without stating whether every in-scope page has an approved light-mode effect image for that optional branch.
- Do not treat a representative effect image as if the complete all-page effect-image set already exists.
- In manual mode, do not generate remaining page effect images before the representative effect image is explicitly confirmed.
- Do not accept generated effect-image evidence into the workflow record without stating whether the approved style constraints were explicitly inherited.
- Do not present shared/global freeze as ready in the workflow record while a revision path that explicitly requires approved effect images is still missing them.
- Do not hide a required bitmap fallback or MCP-driven asset-generation need inside prose without indexing the asset path or pending generation note.
- Do not mark a module ready for display-layer landing while the required preflight inputs or decision table are still missing.
- Do not mark a fidelity-critical module ready for display-layer landing while its evidence pack still lacks the detail, state, scroll, or overlay coverage needed for faithful implementation.
- Do not treat a complete design draft as freeze-ready when the design package is still incomplete.
- Do not switch to the next process while `confirmation_status` is `pending_confirmation`, unless `execution_mode=auto`.
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
- Do not mark `project_initialized` unless both the directory skeleton and project-local `skills/flutter-dev/` exist.
- Do not treat `project_initialized` as proof that any feature, page, or module implementation code already exists.
- Do not mark `bootstrap_code_ready` unless the required global public code baseline actually exists on disk.
- Do not let `execution_mode=auto` claim implementation progress without recording the corresponding `@superpowers` gates, execution evidence, and code artifacts.
- Do not wait for every feature module to finish late-stage architecture planning before triggering `flutter-init` when the shared bootstrap-critical baseline is already sufficient.
- Do not hide the `@superpowers` implementation ownership or the display-layer evidence dependency when the module is already in or beyond implementation and those controls are relevant.
- Do not treat implementation execution as valid before both `@superpowers` `Spec` and `@superpowers` `Plan` are recorded for the active module.
- Do not treat implementation execution as valid unless the workflow record shows the active serial module order, the current active module, and any explicitly approved ownership split when one exists.
- Do not record delegated module document generation or implementation as valid if it was routed directly to a downstream execution skill without explicit `@superpowers` invocation when execution ownership was required.
- Do not infer verified execution from polished documents, manual backfill, or missing traces.
- Do not hide a missing module index row, missing executable module `impl.md`, missing Stitch design-source packet, or other failed generation precondition behind a later stage label.
- Do not require `pen_file`, `pen_status`, page-level Pen, `.pen`, or Pencil MCP data unless the workflow selected the Pencil design-source branch.
