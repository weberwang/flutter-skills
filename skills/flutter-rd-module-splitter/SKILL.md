---
name: flutter-rd-module-splitter
description: Use when a Flutter PRD plus global technical baseline must be decomposed into bounded modules with detailed per-module UI/UX and implementation RD documents, module indexes, inherited package decisions, cross-links, and workflow states.
---

# Flutter RD Module Splitter

## Overview

Split broad Flutter product requirements into executable modules after the global technical baseline exists. This is the module-level detailed design skill: each module must receive two linked documents, one UI/UX RD and one implementation RD, while inheriting global architecture and package decisions from `flutter-prd-rd-writer`.

## Required Inputs

- PRD, product brief, or broad RD.
- Global technical baseline from `flutter-prd-rd-writer`.
- Package stack, architecture assumptions, backend collaboration shape, and delivery constraints.
- Known non-goals and release constraints.

If the global technical baseline is missing, stop and route to `flutter-prd-rd-writer` before splitting implementation modules.

## Module Boundary Rules

Create a module when the scope has at least one stable ownership boundary:

- A distinct user job or workflow.
- A distinct navigation entry, page family, or repeated screen pattern.
- A distinct domain model, backend contract, permission boundary, or state lifecycle.
- A release slice that can be designed, implemented, tested, and reviewed independently.

Do not create a module only because a screen exists. Small screens that share one user job and data lifecycle should stay in the same module.

## Workflow

1. Read the PRD, RD, feature brief, or user notes.
2. Read the global technical baseline, especially architecture, package stack, backend contracts, data security, analytics, monitoring, rollout, and release assumptions.
3. Extract business goals, users, flows, pages, states, data dependencies, permissions, analytics, non-goals, and technical constraints.
4. Identify missing information that changes module boundaries and list it under `open_questions`.
5. If global package or architecture decisions are missing, block splitting and route to `flutter-prd-rd-writer`.
6. Build a module map with module name, responsibility, pages, data owner, package or architecture constraints, upstream dependencies, downstream dependencies, and release value.
7. For each module, write a module detail card covering user job, page/state scope, domain responsibility, application state, infrastructure/API boundary, analytics, tests, and release value.
8. Assign document paths:
   - `docs/rd/modules/<module>/<module>.ui-ux.md`
   - `docs/rd/modules/<module>/<module>.impl.md`
   - Optional state note: `docs/rd/modules/<module>/<module>.workflow.md`
9. Generate or update `docs/rd/00-module-index.md` when the user asks for files to be written.
10. Mark each module with its initial workflow state, normally `modules_split`.

## UI/UX RD Contract

Each `<module>.ui-ux.md` must include:

- Module goal and target user.
- Page scope and navigation entry.
- Core user path.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Design source section with future Pencil path.
- Design freeze card placeholder.
- Acceptance gates for UI/UX and Pencil handoff.

## Implementation RD Contract

Each `<module>.impl.md` must include:

- Explicit reference to the paired UI/UX RD.
- Explicit reference to the global technical baseline.
- Business capability and bounded context.
- Inherited global package stack and module-specific usage notes.
- Domain model, application state, infrastructure dependencies, presentation boundary.
- API, repository, storage, permission, and backend collaboration notes.
- Data, security, analytics, monitoring, rollout, and test scope.
- Module-specific implementation constraints that do not override global decisions.
- Statement that implementation must not change UI/UX decisions after design freeze.

## Hard Rules

- Do not write visual direction; route that to `mobile-ui-design-coach`.
- Do not rebuild Pencil or plan assets; route that to `design-preview-to-pen`.
- Do not choose packages or create the global technical scheme; route that to `flutter-prd-rd-writer`.
- Do not override package or architecture decisions from the global technical baseline; record exceptions as open questions.
- Do not generate Flutter screen architecture from `.pen`; route that to `flutter-pen-to-architecture` after `.pen` is frozen.
- Do not split implementation modules from a raw PRD unless the user explicitly asks for a rough discovery split and accepts that technical decisions are pending.
- Do not output module names only. Each module needs enough detail for its paired UI/UX and implementation RD documents.
- Do not merge UI/UX RD and implementation RD into one document.
- Do not let implementation RD exist without a reference to the paired UI/UX RD.

## Output Contract

Return:

- `module_split_table`
- `document_paths`
- `module_detail_cards`
- `module_dependencies`
- `global_technical_baseline`
- `initial_workflow_states`
- `open_questions`
- `next_skill_recommendation`

## Pressure Scenarios

- A PRD lists ten screens but one user job: group by workflow, not by screen count.
- A raw PRD has no package or architecture decision: route to `flutter-prd-rd-writer` before creating implementation module docs.
- A split contains only module names: fail the output and add module detail cards.
- A module has backend-heavy logic but no UI: still create paired docs; UI/UX RD can declare no visible page and explain state surfaces.
- User asks for a new global package or architecture decision during splitting: stop and route to `flutter-prd-rd-writer`.
