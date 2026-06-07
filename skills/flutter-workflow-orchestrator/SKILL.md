---
name: flutter-workflow-orchestrator
description: Use when coordinating raw Flutter requirements intake, requirements brainstorming, PRD document generation, PRD-based final product design direction confirmation, representative-first effect-image generation, Stitch-only structured design source, executable module implementation document generation, module design freezing, architecture planning, implementation readiness, human visual inspection handoff, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through raw requirements intake -> requirements brainstorming -> PRD document generation -> approved PRD -> PRD-based final product design direction confirmation -> representative light-mode effect-image generation -> user confirmation -> remaining all-page effect-image generation -> Stitch structured design source -> global technical baseline -> taste-first shared design direction -> shared freeze -> executable module `impl.md` generation -> module design freeze -> implementation RD readiness -> architecture -> implementation workflow.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow record document for the whole project.

In manual mode, pause at confirmation gates after one stage or one module reaches a reviewable milestone. In `--auto` mode, behave as a full-module advancement loop across the whole target module set, not as a single-module recommendation assistant.

The only default design source is Stitch. Effect images remain visual baseline evidence, but separate module design documents are no longer required and must not be used as the design source. A Stitch design-source packet must be generated or validated before freeze whenever Stitch MCP is available for the project. Before any Stitch call, confirm whether the user wants a new Stitch project or an existing Stitch project, then freeze the resulting `stitch_project_id`. Stitch page design runs in page-scoped subagents with at most 6 page-design subagents in parallel; only the orchestrator may merge receipts, update the workflow record, or freeze the packet. Pen/Pencil skills may remain available as optional external design adapters, but do not route to them unless the user explicitly asks for Pencil tooling.

## Required Reading

Load only the references needed for the current routing decision, but always preserve their authority over the workflow:

- `references/workflow-record-contract.md`: Read before initializing or updating `docs/rd/00-workflow-record.md`.
- `references/requirements-prd-flow.md`: Read when the input is raw requirements, a one-line feature idea, a partially specified request, or any request that lacks a PRD artifact.
- `references/stitch-design-source.md`: Read when effect images, approved visual comps, or module visual evidence must become the structured design source for freeze, architecture, implementation, or human visual inspection.
- `references/control-contracts.md`: Read before deriving route locks, running preflight, validating receipts, delegating to subagents, applying confirmation gates, or updating maturity.
- `references/execution-modes.md`: Read whenever the invocation includes `--auto`, `--perviewer`, module auto-advancement, effect-image generation, or stop-condition decisions.
- `references/workflow-states.md`: Read when classifying `current_stage`, module maturity, or allowed next moves.
- `references/routing-rules.md`: Read before selecting any downstream skill or crossing any stage boundary.
- `references/hard-rules.md`: Read before applying any state/status promotion, freeze decision, implementation handoff, visual-evidence decision, or downstream delegation.
- `references/pressure-scenarios.md`: Read when the user request resembles one of the pressure examples or tries to skip a gate.

## Core Freeze Requirements

Before any global design freeze or module design freeze, always run `flutter-taste-router` to normalize the textual design packet first. Before global design freeze, confirm the final product design direction with the user based on the PRD, then generate exactly one representative light-mode effect image first. After the user confirms or adjusts that representative image, generate the remaining page effect images. After normalization, inspect the matching artifact directories for static visual evidence before deciding whether any regeneration is necessary.

Before global design freeze, approved all-page effect images are required. If final product design direction is not explicitly confirmed from the PRD, stop and request confirmation before generating images. Generate one representative page effect image first, wait for explicit user confirmation or revision feedback, then generate the remaining required page effect images. If page images are missing, check `IMAGE_BASE_URL` and `IMAGE_API_KEY`. If both variables exist, call `gpt-image-2-generator` to generate the representative page first, save it into the global effect-image directory under `docs/rd/` using the corresponding page name, and keep all remaining effect images in that same global directory. After the representative image is confirmed, generate the remaining global effect-image paths for Stitch and human visual inspection.

Every generation request must explicitly include existing style constraints: `art_direction`, `taste_constraints`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, and image-treatment posture when those values already exist. If either image environment variable is missing while global freeze still lacks approved effect images, stop and record a blocker. All workflow effect images must use light mode unless the user explicitly changes that requirement upstream.

For module implementation, high-fidelity visual fidelity is the first design-freeze priority. Before queueing or applying `module_design_frozen`, verify that `flutter-design-freeze-gate` evaluated the module's Stitch design-source packet and high-fidelity visual contract first: hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and any approved Flutterization or bitmap fallback. If this contract is missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched design revision.

## Routing Procedure

For every invocation:

1. Ensure `docs/rd/00-workflow-record.md` exists. If missing, create it using `references/workflow-record-contract.md`.
2. Determine whether the run is manual, `--auto`, or `--perviewer`; load `references/execution-modes.md` when relevant.
3. Read the existing workflow record and any required artifact indexes before choosing a route.
4. Derive and persist one route lock before invoking anything downstream.
5. Run the preflight gate from `references/control-contracts.md`. If it fails, record the exact blocker and stop.
6. Select the next downstream skill using `references/workflow-states.md` and `references/routing-rules.md`.
7. If the step is subagent-eligible, delegate only the specialist work and require a structured receipt; keep workflow ownership in the orchestrator.
8. Validate the receipt against the active route lock before applying any transition or status update.
9. In manual mode, queue reviewable stage/status changes behind confirmation. In `--auto`, auto-apply deterministic pre-implementation confirmations until the implementation boundary or a blocker.
10. Update `docs/rd/00-workflow-record.md` as the single source of truth.
11. Return the output contract fields listed below.

## Delegation Boundary

Subagents may execute specialist work, but they must not own workflow control. The orchestrator alone may choose `current_stage`, choose `current_module`, persist route locks, run preflight, validate receipts, apply queued transitions, classify blockers, and update `docs/rd/00-workflow-record.md`.

Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race. The only exception is a route-locked Stitch page-design batch with at most 6 page-scoped subagents, where each subagent owns a different page and the orchestrator merges receipts. In `--auto` after executable module documents exist, advance one dependency-safe module at a time.

## Implementation Boundary

Do not move a module into `implementing` until `technical_baseline_ready`, `module_impl_docs_ready`, `module_design_frozen`, and `impl_rd_ready` exist for the module, confirmed maturity is at least `impl_status=landed` and `design_source_status=frozen`, the frozen Stitch design-source packet exists for the module, and the required global public code baseline is already landed.

The required global public code baseline includes app bootstrap and environment initialization, root router or route host plus redirect policy, global dependency injection or provider scope entry, local storage baseline and persistence wiring, global error mapping and logging baseline, required shared theme or design-token baseline, and the shared shell layer when feature modules depend on an `app-shell` or `root-shell`. Add network baseline and API client wiring only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities.

When implementation work should begin, the entry sequence is fixed: route through `@superpowers` to produce `Spec` first, then through `@superpowers` again to produce `Plan`, and only then execute implementation with project-local `flutter-dev` and `flutter-project-guardrails`. Implementation execution defaults to parallel execution of independent work packages defined by the `Plan`; only shared-file or shared-state conflicts justify a serial fallback. Before display-layer code begins, inspect the corresponding page image through `$image-to-code` when such evidence exists. If Stitch restoration downloaded approved image assets, implementation should use those local assets directly. Use `$imagegen` only for visuals whose approved source image is missing, unusable, or explicitly needs generation/rework.

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
