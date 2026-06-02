---
name: flutter-workflow-orchestrator
description: Use when coordinating modular Flutter PRD/RD, UI/UX design, Pencil handoff, implementation RD, architecture planning, implementation readiness, parity review, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through the approved PRD -> global technical baseline -> detailed module design -> design -> Pencil -> implementation workflow. This skill is the traffic controller: it selects the next specialist skill, records state, and blocks skipped gates; it does not write UI designs, rebuild Pencil files, produce architecture, or implement code.

## Workflow States

Use one state per module:

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `prd_ready` | PRD or feature brief exists | `flutter-prd-rd-writer` |
| `technical_baseline_ready` | Global architecture, package stack, backend collaboration, and delivery assumptions exist without detailed module breakdown | `flutter-rd-module-splitter` |
| `modules_split` | Detailed modules, paired doc paths, module detail cards, and global baseline references exist | `mobile-ui-design-coach` |
| `uiux_draft` | UI/UX RD exists but is not frozen | `mobile-ui-design-coach` or `flutter-design-freeze-gate` |
| `design_freeze_ready` | Design packet is ready for approval | `flutter-design-freeze-gate` |
| `pen_ready` | Approved design can move to Pencil | `design-preview-to-pen` |
| `pen_frozen` | `.pen` and UI/UX source are frozen | `flutter-design-source-control` or `flutter-pen-to-architecture` |
| `impl_rd_ready` | Module implementation RD references UI/UX RD, `.pen`, and the global technical baseline | `flutter-pen-to-architecture` |
| `architecture_ready` | Tokens, assets, components, and screen plan exist | `flutter-init` or project-local `flutter-dev` |
| `implementing` | Code work is in progress | project-local `flutter-dev` plus `flutter-project-guardrails` |
| `parity_reviewed` | Implementation has been checked against design source | fix issues or mark `module_done` |
| `module_done` | Module passes design and implementation gates | maintain index only |

## Routing Rules

1. If the input is only a PRD, broad RD, or feature brief, use `flutter-prd-rd-writer` first to create the global technical baseline and package decisions without detailed module splitting.
2. If a global technical baseline exists but detailed modules and paired doc paths do not, use `flutter-rd-module-splitter`.
3. If a module lacks UI/UX direction, page states, or commercial design decisions, use `mobile-ui-design-coach`.
4. If UI/UX has a candidate design but no explicit approval, use `flutter-design-freeze-gate`.
5. If an approved visual direction must become Pencil, use `design-preview-to-pen`.
6. If a frozen `.pen` or UI/UX source is about to be consumed by implementation RD or code, use `flutter-design-source-control`.
7. If module implementation details are missing after splitting, return to `flutter-rd-module-splitter`; do not use `flutter-prd-rd-writer` for module-level detailed design.
8. If Pencil design must become Flutter-facing tokens, assets, components, and screen architecture, use `flutter-pen-to-architecture`.
9. If project scaffolding starts from RD, use `flutter-init`; if extending an existing project, use the project-local `flutter-dev` when present.
10. If code is complete or screenshots exist, use `flutter-design-parity-reviewer`.
11. If the user requests UI, layout, interaction, hierarchy, visual token, or state changes after freeze, use `flutter-design-source-control`.

## Hard Rules

- Do not split implementation modules from a raw PRD before a global technical baseline and package stack exist.
- Do not use `flutter-prd-rd-writer` for detailed module design; it owns global technical baseline only.
- Do not let code implementation begin before `technical_baseline_ready`, `modules_split`, `pen_frozen`, and `impl_rd_ready` exist for the module.
- Do not route around `flutter-design-freeze-gate` on implied approval.
- Do not let implementation rewrite design intent. Design changes after freeze must return to design control.
- Do not ask an execution skill to do workflow bookkeeping that belongs here.
- Do not treat one module's state as proof that another module is ready.

## Output Contract

Return:

- `current_module`
- `current_state`
- `next_skill`
- `required_inputs`
- `blockers`
- `allowed_next_actions`
- `forbidden_actions`

## Pressure Scenarios

- User says "implement this home page directly" with only a PRD: route to `flutter-prd-rd-writer` for the global technical baseline, not module split or code.
- User says "split modules first, choose packages later": block and require at least a baseline architecture and package decision.
- User says "the design is basically fine, make the Pen file first": require `flutter-design-freeze-gate`.
- User says "adjust button hierarchy during implementation": route to `flutter-design-source-control`.
- User says "the code is done, check whether it matches the design": route to `flutter-design-parity-reviewer`.
