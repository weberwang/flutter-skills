---
name: flutter-workflow-orchestrator
description: Use when coordinating modular Flutter PRD/RD, shared design freezing, complete design review, module draft splitting, implementation-stage page/Pencil freezing, architecture planning, implementation readiness, parity review, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through the approved PRD -> global technical baseline -> shared design direction -> complete design review -> shared freeze -> split drafts -> implementation-stage module refinement -> module design review -> module Pencil freeze -> architecture -> implementation workflow.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow record document for the whole project.

When it routes to `visual-design-reviewer`, it must dispatch that review in a fresh subagent with a bounded context packet instead of running the review inline in the parent thread.

## Workflow Record

- On the first run, always create `docs/rd/00-workflow-record.md` if it does not exist.
- Keep all stage bookkeeping in that one file. Do not split stage tracking across ad-hoc notes or per-module workflow files.
- Read `references/workflow-record-contract.md` before initializing or updating the workflow record.
- After every routing decision, update the record with the current stage, current module, confirmation status, next skill, blockers, pending next-stage data, pending status updates, and any newly confirmed artifact paths.

## Confirmation Gate

Treat confirmation as a workflow gate, not as a workflow stage.

Use these confirmation states:

| Confirmation Status | Meaning |
| --- | --- |
| `not_required` | The current routing decision does not need a fresh user confirmation before execution. |
| `pending_confirmation` | The current step has produced reviewable artifacts or status updates, but the workflow must not switch to the next process or apply the queued status changes until the user explicitly confirms. |
| `confirmed` | The user has explicitly approved the pending transition or pending status updates, so the workflow can apply the recorded changes. |
| `rejected` | The user rejected the pending transition or pending status updates and the workflow must stay on the current confirmed state until the issues are resolved. |

When a specialist skill finishes and produces the required artifacts for a later stage or a new artifact maturity level, do not immediately switch to the next process. Instead, keep `current_stage` at the last confirmed stage, set `confirmation_status` to `pending_confirmation`, record `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`, and write `waiting_for_user_confirmation` into blockers if no stronger blocker exists.

## Module Artifact Maturity

Track module-stage maturity in addition to `current_stage`.

Use these values:

### `uiux_status` and `impl_status`

| Value | Meaning |
| --- | --- |
| `not_started` | The document does not exist yet. |
| `split_draft` | The document was created during `modules_split` and only captures initial module intent, scope, and constraints. It is not implementation-ready. |
| `implementation_final` | The document has been refined during implementation preparation to directly implementable granularity and is waiting for the corresponding page-level Pen delivery to become landed. |
| `landed` | The corresponding page-level Pen exists, the document references the delivered design source, and the landed status has been explicitly confirmed. |

### `pen_status`

| Value | Meaning |
| --- | --- |
| `not_started` | No module-level page Pen work has started. |
| `in_progress` | The module is preparing or producing page-level Pen artifacts. |
| `landed` | The active module's page-level and module-private component Pen artifacts are delivered, frozen, and confirmed. |

### `code_status`

| Value | Meaning |
| --- | --- |
| `not_started` | Code implementation has not started. |
| `in_progress` | Code work is actively being implemented. |
| `landed` | Code implementation is present and the landed status has been explicitly confirmed. |

## Workflow States

Use one state per module:

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `prd_ready` | PRD or feature brief exists | `flutter-prd-rd-writer` |
| `technical_baseline_ready` | Global architecture, package stack, backend collaboration, and delivery assumptions exist without frozen shared UI direction or detailed module breakdown | `mobile-ui-design-coach` or `design-preview-to-global-guidelines` |
| `uiux_draft` | Shared UI/UX direction exists but is not frozen | `mobile-ui-design-coach`, `visual-design-reviewer`, or `design-preview-to-global-guidelines` |
| `global_guidelines_frozen` | Approved screenshots or preview comps have been converted into frozen global/shared guidance, explicit global public component decisions, and dual-theme artifacts | `flutter-design-freeze-gate` |
| `design_freeze_ready` | The shared design packet plus any required global freeze artifacts are ready for approval before module splitting | `flutter-rd-module-splitter` |
| `modules_split` | Detailed modules, paired doc paths, module detail cards, global baseline references, and module-level component design skeletons exist. Each module's `uiux_status` and `impl_status` start as `split_draft` unless already confirmed otherwise. | `flutter-rd-module-splitter` |
| `pen_ready` | The active module has entered implementation preparation. Split drafts may now be refined into implementation-final docs before page-level Pen production. | `flutter-rd-module-splitter`, `design-preview-to-pen`, or `visual-design-reviewer` |
| `pen_frozen` | The active module's page-level Pen and module-private component design are frozen during implementation preparation, including reusable component decisions required for implementation handoff | `flutter-design-source-control` or `flutter-pen-to-architecture` |
| `impl_rd_ready` | The active module's UI/UX RD and implementation RD are implementation-final or landed, reference the current Pen source and global technical baseline, and are confirmed as implementable | `flutter-pen-to-architecture` |
| `architecture_ready` | Tokens, assets, components, screen plan, and scaffold contract exist | `flutter-init` |
| `project_initialized` | `flutter-init` has created the project scaffold and generated project-local `skills/flutter-dev/` | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `implementing` | Code work is in progress inside the initialized project after the active module's page-level Pen has landed and the module docs are no longer split drafts | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `parity_reviewed` | Implementation has been checked against the landed design source | fix issues or mark `module_done` |
| `module_done` | Shared freeze is confirmed, module docs are landed, Pen is landed, code is landed, and parity review has passed | maintain index only |

## Routing Rules

1. Start by ensuring `docs/rd/00-workflow-record.md` exists. If it is missing, create it before any stage routing.
2. If `confirmation_status` is `pending_confirmation`, do not switch to the next process and do not apply queued status changes. Keep `next_skill` as `none`, preserve the current confirmed stage, surface `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`, and wait for explicit user confirmation.
3. If the user explicitly confirms a pending transition or pending status update, promote `pending_next_stage` into `current_stage` when present, promote `pending_next_skill` into `next_skill` only for that routing update, apply `pending_status_updates`, set `confirmation_status` to `confirmed`, clear all pending fields, and then continue normal routing from the newly confirmed state.
4. If the user rejects a pending transition or pending status update, keep `current_stage` unchanged, keep all current status fields unchanged, set `confirmation_status` to `rejected`, keep or replace blockers with the rejection reason, and route back to the skill that must revise the artifacts.
5. If a specialist skill returns `blocked`, do not advance to the next process. Keep `current_stage` on the last confirmed stage, clear `pending_next_stage`, `pending_next_skill`, and `pending_status_updates` to `none`, set `next_skill` to `none` unless the blocker response explicitly names a remediation step, and record the blocker before any further routing.
6. If the input is only a PRD, broad RD, or feature brief, use `flutter-prd-rd-writer` first to create the global technical baseline and package decisions without detailed module splitting.
7. If a global technical baseline exists but the workflow still lacks shared UI/UX direction, state framing, or commercial design decisions, use `mobile-ui-design-coach`.
8. If approved screenshots, preview comps, or static mockups must become a reusable shared design-source contract with fixed light and dark theme values, use `design-preview-to-global-guidelines`, then record the module as `global_guidelines_frozen` as `pending_next_stage` until the user confirms the switch.
9. If the workflow requests shared design freezing but no reference screenshots or usable preview images exist, do not route to `design-preview-to-global-guidelines`; return the module as blocked and ask the user whether to fall back.
10. Before `modules_split`, treat design freezing as shared/public freeze only. Do not treat `global_guidelines_frozen` or `design_freeze_ready` as module page freeze or module-private component freeze.
11. If shared design has a visually complete draft and no current `visual-design-reviewer` record, or the last review findings are no longer trustworthy after substantial design changes, dispatch `visual-design-reviewer` in a fresh subagent before shared freeze approval, unless the latest failed shared review has already consumed its one allowed follow-up revision.
12. If the latest shared visual review score is below `90` or the review still requires changes, do not route to freeze. Allow exactly one shared revision pass through `mobile-ui-design-coach` plus shared preview regeneration, record that follow-up as `revision_pending`, and after that single revision is produced do not dispatch `visual-design-reviewer` again unless the user explicitly restarts a new shared design cycle.
13. If shared design has a candidate direction but no explicit approval, use `flutter-design-freeze-gate`.
14. If the shared visual direction has been approved but detailed modules and paired doc paths do not exist yet, use `flutter-rd-module-splitter`. Its first pass creates split drafts, not implementation-final docs.
15. If a module has been selected for implementation preparation and its `uiux_status` or `impl_status` is still `split_draft`, keep or promote the module to `pen_ready` and use `flutter-rd-module-splitter` again to refine only that active module's existing docs to implementation-final granularity.
16. When module refinement produces implementation-final docs, keep `current_stage` at the last confirmed stage, queue the relevant `pending_status_updates` such as `<module>.uiux_status=implementation_final` and `<module>.impl_status=implementation_final`, and wait for confirmation before routing to page-level Pen work.
17. After the active module docs are implementation-final and confirmed, use `design-preview-to-pen` to create the active module's page-level Pen and module-private component Pen artifacts.
18. If a complete active-module visual draft or Pencil result exists and no current `visual-design-reviewer` record exists for that latest draft, dispatch `visual-design-reviewer` in a fresh subagent before queueing `pen_frozen` or landed Pen status updates, unless the latest failed module review has already consumed its one allowed follow-up revision.
19. If the latest active-module visual review score is below `90` or the review still requires changes, do not route to freeze or landed Pen status. Keep the workflow on the active module, update the active module `ui/ux` doc, modify the current module design draft in Pen through `design-preview-to-pen` exactly once, record that follow-up as `revision_pending`, and after that single revision is produced do not dispatch `visual-design-reviewer` again unless the user explicitly restarts a new module design cycle.
20. When page-level Pen artifacts are produced and the latest complete draft has passed `visual-design-reviewer` in a fresh subagent with score `>= 90`, do not immediately mark the module landed. Queue `pending_next_stage=pen_frozen`, queue `pending_status_updates` for `pen_status=landed`, and if the docs have been updated to reference the delivered Pen source also queue `uiux_status=landed` and `impl_status=landed`, then wait for explicit confirmation.
21. If a frozen `.pen` or UI/UX source is about to be consumed by implementation RD or code, use `flutter-design-source-control`.
22. If Pencil design must become Flutter-facing tokens, assets, components, and screen architecture, use `flutter-pen-to-architecture`.
23. Do not move a module into `implementing` until `technical_baseline_ready`, `modules_split`, `pen_frozen`, and `impl_rd_ready` exist for the module, and the confirmed module maturity is at least `uiux_status=landed`, `impl_status=landed`, and `pen_status=landed`.
24. If the module is `architecture_ready` and the target project has not been scaffolded yet or does not contain project-local `skills/flutter-dev/`, use `flutter-init`.
25. If `flutter-init` has completed and the project-local `skills/flutter-dev/` exists, record `project_initialized` as `pending_next_stage` and wait for confirmation before switching to the project-local `flutter-dev`.
26. If the project is already initialized and implementation work should begin or continue, use the project-local `flutter-dev`.
27. When code implementation starts, keep `code_status` at the last confirmed value and only queue `code_status=in_progress` if the status change itself needs to be recorded for review. Do not mark `code_status=landed` until code output actually exists and the user confirms that state change.
28. If code is complete or screenshots exist, use `flutter-design-parity-reviewer`.
29. If the user requests UI, layout, interaction, hierarchy, visual token, or state changes after shared freeze or module page freeze, use `flutter-design-source-control`.

## Workflow Record Update Rules

- Always update `workflow_summary` with the latest project-level stage summary.
- Always update `current_stage`, `current_module`, `confirmation_status`, `next_skill`, and `pending_status_updates`.
- Record blockers explicitly instead of hiding them in prose.
- Add or refresh artifact paths when new module docs, subagent-produced visual review reports, frozen theme files, `.pen` files, architecture summaries, project roots, or `skills/flutter-dev/` become available.
- Keep one row per module in the module status table and update that row instead of appending duplicate rows.
- When no module is selected yet, store project-level routing in the summary and leave module-specific fields as `not_selected`.
- When a step is waiting for review, keep `current_stage` at the last confirmed stage, set `next_skill` to `none`, and store the candidate transition in `pending_next_stage`, `pending_next_skill`, and `pending_status_updates`.
- When a step returns `blocked`, keep `current_stage` at the last confirmed stage and clear any queued transition or queued status change instead of changing the workflow to the next process.
- Move the project or module to `project_initialized` only after `flutter-init` has produced a usable scaffold and generated the project-local `skills/flutter-dev/`, and only switch into that stage after explicit user confirmation.
- Keep the last confirmed maturity values in the module row. Never overwrite confirmed values with proposed values before confirmation.

## Hard Rules

- Do not split implementation modules from a raw PRD before a global technical baseline and package stack exist.
- Do not use `flutter-prd-rd-writer` for detailed module design; it owns global technical baseline only.
- Do not let shared freeze before `modules_split` claim that module pages or module-private components are frozen. Only shared/public components, global principles, and theme artifacts may freeze there.
- Do not treat `modules_split` output as implementation-ready. The first split only creates draft module docs and workflow structure.
- Do not let page-level or module-private component freeze happen before the active module enters implementation preparation.
- Do not let code implementation begin before `technical_baseline_ready`, `modules_split`, `pen_frozen`, and `impl_rd_ready` exist for the module.
- Do not let code implementation begin while `uiux_status` or `impl_status` is still `split_draft`.
- Do not mark `uiux_status=landed` or `impl_status=landed` until the corresponding module page-level Pen exists and has been confirmed.
- Do not mark `code_status=landed` until the code output exists and the landed status change has been explicitly confirmed.
- Do not route around `flutter-design-freeze-gate` on implied approval.
- Do not let a complete shared or module design draft skip `visual-design-reviewer` before freeze or Pen landed-state promotion, especially when information hierarchy or task guidance is still being tuned.
- Do not allow a visual review score below `90` to advance into shared freeze, module page freeze, or landed Pen promotion.
- Do not shortcut a sub-90 review into local polish only; return to exactly one scope-matched revision pass first, then stop the review cycle.
- Do not use the shared/global revision path as the default fix path for a module-stage review failure.
- Do not route a module-stage design review failure back to module splitting by default.
- Do not dispatch another `visual-design-reviewer` run after the one allowed post-failure revision unless the user explicitly starts a new design cycle.
- Do not run `visual-design-reviewer` inline in the parent orchestration thread.
- Do not accept a visual review result that inherited unnecessary parent-thread context when a bounded subagent packet should have been used.
- Do not let screenshot-based design freezing skip `design-preview-to-global-guidelines` when downstream skills need stable global principles or concrete theme values.
- Do not attempt `global_guidelines_frozen` when no reference screenshots or usable preview images exist; block and ask the user whether to fall back instead.
- Do not let implementation rewrite design intent. Design changes after freeze must return to design control.
- Do not route directly from `architecture_ready` to project-local `flutter-dev`; new project scaffolding must pass through `flutter-init`.
- Do not switch to the next process automatically after a specialist skill finishes; wait for explicit user confirmation whenever `pending_next_stage`, `pending_next_skill`, or `pending_status_updates` are set.
- Do not treat a `blocked` result as a pending transition; blocked work must stay on the current confirmed stage.
- Do not invoke `pending_next_skill` while `confirmation_status` is `pending_confirmation`.
- Do not ask an execution skill to do workflow bookkeeping that belongs here.
- Do not treat one module's state as proof that another module is ready.
- Do not create per-module workflow state files; keep stage tracking in `docs/rd/00-workflow-record.md`.
- Do not advance a stage or artifact maturity without updating the workflow record in the same response.

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
- `required_inputs`
- `blockers`
- `allowed_next_actions`
- `forbidden_actions`

## Pressure Scenarios

- User says "implement this home page directly" with only a PRD: route to `flutter-prd-rd-writer` for the global technical baseline, not module split or code.
- User says "split modules first, choose packages later": block and require at least a baseline architecture and package decision.
- User says "the design draft is complete, just freeze it": dispatch `visual-design-reviewer` in a fresh subagent first, then `flutter-design-freeze-gate`.
- User says "the shared effect image scored 88, just freeze it": block and route back through exactly one shared requirements-analysis and preview-regeneration pass, then stop without another automatic review.
- User says "the shared design is basically fine, freeze it and split": require `flutter-design-freeze-gate`, but freeze only the shared/public layer before `modules_split`.
- User says "modules are split, now refine only the home module to implementation level": keep the active module in `pen_ready` and route to `flutter-rd-module-splitter` for refinement, not a full project re-split.
- User says "the docs are final, start drawing the page Pen": require explicit confirmation for the queued `implementation_final` status change before routing to `design-preview-to-pen`.
- User says "the Pen draft is done, continue": if the latest complete draft has not been reviewed, dispatch `visual-design-reviewer` in a fresh subagent before queuing landed state updates.
- User says "the module review listed change requests but the score is close enough": block and return to updating the current module `ui/ux` doc plus modifying the current module design draft in Pen exactly once, then stop without another automatic review.
- User says "the Pen file is done, start coding": if the module docs are not yet landed against that Pen source, queue the landed status updates first and wait for confirmation before code.
- User says "the architecture summary is done, start coding": if the scaffold or `skills/flutter-dev/` does not exist yet, route to `flutter-init` first.
- User says "the last step looks good, continue": if `confirmation_status` is `pending_confirmation`, promote the recorded pending transition and pending status updates, then switch to the next process.
- User says "adjust button hierarchy during implementation": route to `flutter-design-source-control`.
- User says "the code is done, check whether it matches the design": route to `flutter-design-parity-reviewer`.
- Workflow record is missing on a live project: create `docs/rd/00-workflow-record.md` first, then continue routing.

## References

- Read `references/workflow-record-contract.md` for the exact initialization and update contract of `docs/rd/00-workflow-record.md`.
