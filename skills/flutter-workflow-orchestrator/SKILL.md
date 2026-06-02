---
name: flutter-workflow-orchestrator
description: Use when coordinating modular Flutter PRD/RD, UI/UX design, static-preview freezing, Pencil handoff, implementation RD, architecture planning, implementation readiness, parity review, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through the approved PRD -> global technical baseline -> UI direction -> static-source freeze -> detailed module design -> Pencil -> architecture -> implementation workflow. This skill is the traffic controller: it selects the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before switching to the next process, and maintains one stable workflow record document for the whole project.

## Workflow Record

- On the first run, always create `docs/rd/00-workflow-record.md` if it does not exist.
- Keep all stage bookkeeping in that one file. Do not split stage tracking across ad-hoc notes or per-module workflow files.
- Read `references/workflow-record-contract.md` before initializing or updating the workflow record.
- After every routing decision, update the record with the current stage, current module, confirmation status, next skill, blockers, pending next-stage data, and any newly confirmed artifact paths.

## Confirmation Gate

Treat confirmation as a workflow gate, not as a workflow stage.

Use these confirmation states:

| Confirmation Status | Meaning |
| --- | --- |
| `not_required` | The current routing decision does not need a fresh user confirmation before execution. |
| `pending_confirmation` | The current step has produced reviewable artifacts, but the workflow must not switch to the next process until the user explicitly confirms. |
| `confirmed` | The user has explicitly approved the pending transition, so the workflow can switch to the recorded next process. |
| `rejected` | The user rejected the pending transition and the workflow must stay on the current confirmed stage until the issues are resolved. |

When a specialist skill finishes and produces the required artifacts for a later stage, do not immediately switch to the next process. Instead, keep `current_stage` at the last confirmed stage, set `confirmation_status` to `pending_confirmation`, record `pending_next_stage` and `pending_next_skill`, and write `waiting_for_user_confirmation` into blockers if no stronger blocker exists.

## Workflow States

Use one state per module:

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `prd_ready` | PRD or feature brief exists | `flutter-prd-rd-writer` |
| `technical_baseline_ready` | Global architecture, package stack, backend collaboration, and delivery assumptions exist without frozen UI direction or detailed module breakdown | `mobile-ui-design-coach` or `design-preview-to-global-guidelines` |
| `uiux_draft` | UI/UX direction exists but is not frozen | `mobile-ui-design-coach` or `design-preview-to-global-guidelines` |
| `global_guidelines_frozen` | Approved screenshots or preview comps have been converted into frozen global guidance and dual-theme artifacts | `flutter-design-freeze-gate` |
| `design_freeze_ready` | Design packet plus any required global freeze artifacts are ready for approval | `flutter-rd-module-splitter` |
| `modules_split` | Detailed modules, paired doc paths, module detail cards, and global baseline references exist after the visual direction has been approved | `design-preview-to-pen` |
| `pen_ready` | Approved design can move to Pencil | `design-preview-to-pen` |
| `pen_frozen` | `.pen` and UI/UX source are frozen | `flutter-design-source-control` or `flutter-pen-to-architecture` |
| `impl_rd_ready` | Module implementation RD references UI/UX RD, `.pen`, and the global technical baseline | `flutter-pen-to-architecture` |
| `architecture_ready` | Tokens, assets, components, screen plan, and scaffold contract exist | `flutter-init` |
| `project_initialized` | `flutter-init` has created the project scaffold and generated project-local `skills/flutter-dev/` | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `implementing` | Code work is in progress inside the initialized project | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `parity_reviewed` | Implementation has been checked against design source | fix issues or mark `module_done` |
| `module_done` | Module passes design and implementation gates | maintain index only |

## Routing Rules

1. Start by ensuring `docs/rd/00-workflow-record.md` exists. If it is missing, create it before any stage routing.
2. If `confirmation_status` is `pending_confirmation`, do not switch to the next process. Keep `next_skill` as `none`, preserve the current confirmed stage, surface `pending_next_stage` and `pending_next_skill`, and wait for explicit user confirmation.
3. If the user explicitly confirms a pending transition, promote `pending_next_stage` into `current_stage`, promote `pending_next_skill` into `next_skill`, set `confirmation_status` to `confirmed` for that routing update, clear pending transition fields, and then continue normal routing from the newly confirmed stage.
4. If the user rejects a pending transition, keep `current_stage` unchanged, set `confirmation_status` to `rejected`, keep or replace blockers with the rejection reason, and route back to the skill that must revise the artifacts.
5. If the input is only a PRD, broad RD, or feature brief, use `flutter-prd-rd-writer` first to create the global technical baseline and package decisions without detailed module splitting.
6. If a global technical baseline exists but the workflow still lacks UI/UX direction, page states, or commercial design decisions, use `mobile-ui-design-coach`.
7. If approved screenshots, preview comps, or static mockups must become a reusable global design-source contract with fixed light and dark theme values, use `design-preview-to-global-guidelines`, then record the module as `global_guidelines_frozen` as `pending_next_stage` until the user confirms the switch.
8. If the workflow requests global design freezing but no reference screenshots or usable preview images exist, do not route to `design-preview-to-global-guidelines`; return the module as blocked and ask the user whether to fall back.
9. If UI/UX has a candidate design but no explicit approval, use `flutter-design-freeze-gate`.
10. If the visual direction has been approved but detailed modules and paired doc paths do not exist yet, use `flutter-rd-module-splitter`.
11. If an approved visual direction must become Pencil, use `design-preview-to-pen`.
12. If a frozen `.pen` or UI/UX source is about to be consumed by implementation RD or code, use `flutter-design-source-control`.
13. If module implementation details are missing after splitting, return to `flutter-rd-module-splitter`; do not use `flutter-prd-rd-writer` for module-level detailed design.
14. If Pencil design must become Flutter-facing tokens, assets, components, and screen architecture, use `flutter-pen-to-architecture`.
15. If the module is `architecture_ready` and the target project has not been scaffolded yet or does not contain project-local `skills/flutter-dev/`, use `flutter-init`.
16. If `flutter-init` has completed and the project-local `skills/flutter-dev/` exists, record `project_initialized` as `pending_next_stage` and wait for confirmation before switching to the project-local `flutter-dev`.
17. If the project is already initialized and implementation work should begin or continue, use the project-local `flutter-dev`.
18. If code is complete or screenshots exist, use `flutter-design-parity-reviewer`.
19. If the user requests UI, layout, interaction, hierarchy, visual token, or state changes after freeze, use `flutter-design-source-control`.

## Workflow Record Update Rules

- Always update `workflow_summary` with the latest project-level stage summary.
- Always update `current_stage`, `current_module`, `confirmation_status`, and `next_skill`.
- Record blockers explicitly instead of hiding them in prose.
- Add or refresh artifact paths when new module docs, frozen theme files, `.pen` files, architecture summaries, project roots, or `skills/flutter-dev/` become available.
- Keep one row per module in the module status table and update that row instead of appending duplicate rows.
- When no module is selected yet, store project-level routing in the summary and leave module-specific fields as `not_selected`.
- When a step is waiting for review, keep `current_stage` at the last confirmed stage, set `next_skill` to `none`, and store the candidate transition in `pending_next_stage` plus `pending_next_skill`.
- Move the project or module to `project_initialized` only after `flutter-init` has produced a usable scaffold and generated the project-local `skills/flutter-dev/`, and only switch into that stage after explicit user confirmation.

## Hard Rules

- Do not split implementation modules from a raw PRD before a global technical baseline and package stack exist.
- Do not use `flutter-prd-rd-writer` for detailed module design; it owns global technical baseline only.
- Do not let code implementation begin before `technical_baseline_ready`, `modules_split`, `pen_frozen`, and `impl_rd_ready` exist for the module.
- Do not route around `flutter-design-freeze-gate` on implied approval.
- Do not let screenshot-based design freezing skip `design-preview-to-global-guidelines` when downstream skills need stable global principles or concrete theme values.
- Do not attempt `global_guidelines_frozen` when no reference screenshots or usable preview images exist; block and ask the user whether to fall back instead.
- Do not let implementation rewrite design intent. Design changes after freeze must return to design control.
- Do not route directly from `architecture_ready` to project-local `flutter-dev`; new project scaffolding must pass through `flutter-init`.
- Do not switch to the next process automatically after a specialist skill finishes; wait for explicit user confirmation whenever `pending_next_stage` and `pending_next_skill` are set.
- Do not invoke `pending_next_skill` while `confirmation_status` is `pending_confirmation`.
- Do not ask an execution skill to do workflow bookkeeping that belongs here.
- Do not treat one module's state as proof that another module is ready.
- Do not create per-module workflow state files; keep stage tracking in `docs/rd/00-workflow-record.md`.
- Do not advance a stage without updating the workflow record in the same response.

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
- `required_inputs`
- `blockers`
- `allowed_next_actions`
- `forbidden_actions`

## Pressure Scenarios

- User says "implement this home page directly" with only a PRD: route to `flutter-prd-rd-writer` for the global technical baseline, not module split or code.
- User says "split modules first, choose packages later": block and require at least a baseline architecture and package decision.
- User says "the design is basically fine, make the Pen file first": require `flutter-design-freeze-gate`.
- User says "these previews are final, let Flutter use the colors directly": route to `design-preview-to-global-guidelines`, queue `global_guidelines_frozen` for confirmation, and only then switch to `flutter-design-freeze-gate`.
- User says "there is no reference image, freeze the global design anyway": block and ask whether to fall back.
- User says "the architecture summary is done, start coding": if the scaffold or `skills/flutter-dev/` does not exist yet, route to `flutter-init` first.
- User says "the last step looks good, continue": if `confirmation_status` is `pending_confirmation`, promote the recorded pending transition and switch to the next process.
- User says "adjust button hierarchy during implementation": route to `flutter-design-source-control`.
- User says "the code is done, check whether it matches the design": route to `flutter-design-parity-reviewer`.
- Workflow record is missing on a live project: create `docs/rd/00-workflow-record.md` first, then continue routing.

## References

- Read `references/workflow-record-contract.md` for the exact initialization and update contract of `docs/rd/00-workflow-record.md`.
