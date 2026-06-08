---
name: flutter-workflow-orchestrator
description: Use when coordinating raw Flutter requirements intake, requirements brainstorming, PRD document generation, technical baseline generation, Product Design brief confirmation, Product Design visual-direction recommendation, DESIGN.md output, optional effect-image evidence, Stitch or Pencil structured design source, shared design freezing, module implementation document generation, module page component design drafting, module design freezing, architecture planning, project initialization, bootstrap code generation, implementation readiness, Product Design design QA, human visual inspection handoff, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through raw requirements intake -> requirements brainstorming -> PRD document generation -> global technical baseline -> target design-device preset and base resolution confirmation -> `@product-design` brief confirmation -> `@product-design` visual-direction recommendation -> final product design direction confirmation -> `DESIGN.md` output -> optional light-mode effect-image evidence -> Stitch or Pencil structured design source -> shared freeze -> module `impl.md` generation under frozen design and interaction principles -> module page component design draft -> module design freeze -> implementation RD readiness -> architecture -> project initialization -> bootstrap code generation -> implementation workflow -> `@product-design` design QA -> human visual inspection.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow truth model for the whole project. When persistence is needed for a live run, it may serialize that state into runtime artifacts, but those artifacts are not part of the stable skill bundle.

In manual mode, pause at confirmation gates after one stage or one module reaches a reviewable milestone. In `--auto` mode, behave as a full-module advancement loop across the whole target module set, but still advance modules one by one in a serial order rather than opening parallel module lanes.

Structured design source is no longer Stitch-only. After the final design direction is confirmed and `DESIGN.md` is written, the workflow must choose one project-level structured design-source adapter: Stitch or Pencil. `@product-design` owns the design-side kickoff: brief confirmation, direction recommendation, and visual-target selection. Effect images remain optional visual evidence rather than a mandatory gate. Separate module design documents are no longer required and must not replace the chosen structured design-source packet. All module-related work must stay behind the global design freeze. Only after the shared design direction, shared interaction principles, shared public shell rules, and shared component families are frozen may the workflow start the per-module loop. In that loop, the active module's `impl.md` becomes a detailed module task implementation document constrained by the frozen design and interaction principles, and the module page component design draft must wait until that `impl.md` already fixes the module function, key states, task path, and non-display behavior boundaries. If Stitch is selected, confirm whether the user wants a new Stitch project or an existing Stitch project, then freeze the resulting `stitch_project_id`. If Pencil is selected, freeze the project-level Pencil source reference before downstream freeze. For whole-app visual consistency, either adapter must expand pages from one frozen shared design master packet rather than letting page subagents invent local styles. When approved effect images exist, Stitch or Pencil must treat that frozen image set as the primary visual baseline and `DESIGN.md` as the constraint packet rather than replacing the visual baseline with prose. Design guidance must come only from the frozen global design, the active module design package, and `DESIGN.md`; Stitch or Pencil internal guidance, adapter heuristics, and tool-native stylistic defaults are not valid guidance sources. Regardless of adapter, restored design output must preserve one shared style direction, one shared theme system, one shared public shell contract, one shared public component family contract, and one shared interaction-principle contract across all pages. Page-scoped design runs stay capped at at most 6 parallel page-design subagents, and only the orchestrator may merge receipts, update the workflow record, or freeze the packet.

## Required Reading

Load only the references needed for the current routing decision, but always preserve their authority over the workflow:

- `references/workflow-record-contract.md`: Read before initializing or optionally persisting workflow state for the current run.
- `references/requirements-prd-flow.md`: Read when the input is raw requirements, a one-line feature idea, a partially specified request, or any request that lacks a PRD artifact.
- `references/design-quality-guidance.md`: Read when defining global visual direction, writing `DESIGN.md`, or judging whether a design is strong enough to freeze.
- `references/design-md-template.md`: Read when the final product design direction is confirmed and the workflow must write a root-level `DESIGN.md`.
- `references/stitch-design-source.md`: Read when effect images, approved visual comps, or module visual evidence must become the structured design source for freeze, architecture, implementation, or human visual inspection.
- `references/pencil-design-source.md`: Read when the selected structured design-source adapter is Pencil and the confirmed `DESIGN.md` plus any optional visual evidence must become the frozen implementation source.
- `references/control-contracts.md`: Read before deriving route locks, running preflight, validating receipts, delegating to subagents, applying confirmation gates, or updating maturity.
- `references/execution-modes.md`: Read whenever the invocation includes `--auto`, `--preview`, module auto-advancement, effect-image generation, or stop-condition decisions.
- `references/workflow-states.md`: Read when classifying `current_stage`, module maturity, or allowed next moves.
- `references/routing-rules.md`: Read before selecting any downstream skill or crossing any stage boundary.
- `references/hard-rules.md`: Read before applying any state/status promotion, freeze decision, implementation handoff, visual-evidence decision, or downstream delegation.
- `references/pressure-scenarios.md`: Read when the user request resembles one of the pressure examples or tries to skip a gate.

## Core Freeze Requirements

Before any global design freeze or module design freeze, use `@product-design` as the primary design controller. After the technical baseline is ready, first freeze the target design-device preset and base resolution for the current design cycle, then route to `@product-design` `get-context` to confirm the design brief, then to `@product-design` visual exploration to obtain a reviewable global direction, confirm that final product design direction with the user, and then write the confirmed direction into `DESIGN.md`. For iPhone-first mobile work, offer at least these common presets in manual mode unless the user already chose a viewport: `375 x 667 px` (SE / compact), `390 x 844 px` (standard iPhone baseline), `393 x 852 px` (Pro baseline), and `430 x 932 px` (Pro Max baseline). In `--auto`, when the run does not already have a frozen viewport, default the global design viewport to `390 x 844 px`. If downstream freeze needs textual normalization for the frozen packet, `flutter-taste-router` may still refine the wording, but it no longer owns direction generation. Optional effect-image evidence may be generated after that when the user asks for it or when downstream freeze needs extra visual proof. Only after the shared design freeze has passed may the workflow start module `impl.md` generation, module page component design drafts, and module freeze. After normalization, inspect the matching artifact directories for static visual evidence before deciding whether any regeneration is necessary.

Effect images are optional across the workflow. If the target design-device preset or base resolution has not yet been frozen for the current global design cycle, stop before Product Design direction confirmation or optional image generation and request it first. If the Product Design brief has not yet been confirmed through `@product-design` `get-context`, stop and route there before asking for confirmation. If the common public shell has not yet been explicitly agreed, stop and request shell confirmation before confirming design direction or generating optional images. If final product design direction is not explicitly confirmed from the approved Product Design visual target, stop and request confirmation before emitting `DESIGN.md`, generating optional images, or entering structured design-source work. In manual mode, when effect images are in scope, treat the selected Product Design visual target as the representative page baseline, wait for explicit user confirmation or revision feedback, then generate any remaining optional page effect images. In `--auto --preview`, generate the representative page and the remaining in-scope effect images automatically without pausing for confirmation. Preview images must be generated through `gpt-image-2-generator`, and any access or credential blocker must be recorded on that branch. Save generated images into the global effect-image directory under `docs/rd/` using the corresponding page names, and index them for the selected structured design source and human visual inspection when needed. If `--preview` is not present, `--auto` must skip effect-image generation entirely.

Every preview-image generation request must explicitly include existing style constraints: `art_direction`, `taste_constraints`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, and image-treatment posture when those values already exist. If `gpt-image-2-generator` or its required environment cannot generate the required optional effect images, stop and record a blocker for that optional branch instead of treating the whole workflow as blocked by default. All workflow effect images must use light mode unless the user explicitly changes that requirement upstream.

For module implementation, high-fidelity visual fidelity is the first design-freeze priority. Before queueing or applying `module_design_frozen`, verify that the global design freeze is already complete, that the module `impl.md` already fixed the module function, states, interaction path, and non-display behavior boundaries under the frozen shared design and interaction principles, and that `flutter-design-freeze-gate` then evaluated the module page component design draft plus the selected structured design-source packet and high-fidelity visual contract: hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and any approved Flutterization or bitmap fallback. If the shared constraints, function contract, or visual contract are missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched revision.

## Routing Procedure

For every invocation:

1. Ensure workflow state is initialized for the current run. If runtime persistence is enabled, use `references/workflow-record-contract.md` to shape the persisted artifact.
2. Determine whether the run is manual, `--auto`, or `--preview`; load `references/execution-modes.md` when relevant.
3. Read the existing workflow record and any required artifact indexes before choosing a route.
4. Derive and persist one route lock before invoking anything downstream.
5. Run the preflight gate from `references/control-contracts.md`. If it fails, record the exact blocker and stop.
6. Select the next downstream skill using `references/workflow-states.md` and `references/routing-rules.md`.
7. If the step is subagent-eligible, delegate only the specialist work and require a structured receipt; keep workflow ownership in the orchestrator.
8. Validate the receipt against the active route lock before applying any transition or status update.
9. In manual mode, queue reviewable stage/status changes behind confirmation. In `--auto`, auto-apply deterministic stage and status transitions end-to-end until the workflow completes or a blocker appears.
10. Update the orchestrator-owned workflow state as the single source of truth. Persist it only when the current run actually needs a runtime artifact.
11. Return the output contract fields listed below.

## Delegation Boundary

Subagents may execute specialist work, but they must not own workflow control. The orchestrator alone may choose `current_stage`, choose `current_module`, persist route locks when needed, run preflight, validate receipts, apply queued transitions, classify blockers, and update orchestrator-owned workflow state.

Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race. The only exception is a route-locked Stitch page-design batch with at most 6 page-scoped subagents, where each subagent owns a different page and the orchestrator merges receipts. In `--auto` after the shared/global design freeze, advance one module at a time in the confirmed serial module order until all target modules are fully implemented or a blocker appears.

## Implementation Boundary

Do not move a module into `implementing` until `technical_baseline_ready`, `module_impl_docs_ready`, `module_design_frozen`, `impl_rd_ready`, and `bootstrap_code_ready` exist for the module, confirmed maturity is at least `impl_status=landed` and `design_source_status=frozen`, the frozen selected structured design-source packet exists for the module, and the required global public code baseline is already landed.

The required global public code baseline includes app bootstrap and environment initialization, root router or route host plus redirect policy, global dependency injection or provider scope entry, local storage baseline and persistence wiring, global error mapping and logging baseline, required shared theme or design-token baseline, and the shared shell layer when feature modules depend on an `app-shell` or `root-shell`. Add network baseline and API client wiring only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities.

`project_initialized` is directory-only: `flutter-init` may create the project shell, directory skeleton, and project-local `skills/flutter-dev/`, but it must stop before bootstrap code, shared wiring, feature code, or page code. Those global code responsibilities belong to the separate bootstrap code stage.

When implementation work should begin, the entry sequence is fixed: route through `@superpowers` to produce `Spec` first, then through `@superpowers` again to produce `Plan`, and only then execute implementation with project-local `flutter-dev` and `flutter-project-guardrails`. Treat the modules as one serial implementation loop rather than a parallel batch. For each active module in order: first confirm the module `impl.md` as the detailed functional contract, then consume the frozen module page component design draft, then land non-display-layer code, and only after that restore the display layer from the design draft. Implementation execution inside that active module should stay serial by default unless the same module's ownership split is explicitly proven safe. Before display-layer code begins, inspect the corresponding page image through `$image-to-code` when such evidence exists. If the selected structured design-source restoration downloaded approved image assets, implementation should use those local assets directly. If an internal illustration, icon asset, texture, or bitmap fallback still needs generation or rework, let the active MCP / design tool chain choose the concrete generation mechanism as long as the result still satisfies the frozen design principles and implementation target. When a source visual target and implementation screenshots both exist, run `@product-design` `design-qa` as a blocking helper before final handoff, then return to explicit human visual inspection rather than introducing a new automatic workflow stage.

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
