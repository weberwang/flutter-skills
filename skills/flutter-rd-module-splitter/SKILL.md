---
name: flutter-rd-module-splitter
description: Use when a Flutter PRD plus global technical baseline must be decomposed into bounded modules with paired draft UI/UX and implementation RDs, or when an active module entering implementation preparation must refine those drafts into implementation-final documents.
---

# Flutter RD Module Splitter

## Overview

Split broad Flutter product requirements into executable modules after the global technical baseline exists.

This skill has two modes:

1. Initial split mode: create paired `ui-ux` and `impl` draft documents for each module during `modules_split`.
2. Implementation refinement mode: revisit one active module during implementation preparation and refine its existing draft docs to implementation-final granularity.

The initial split is not page-level freeze and not implementation-ready by default. It creates structured drafts and module boundaries. The later refinement pass turns one active module into an implementation-ready document set without pretending the whole product is already landed.

## Required Inputs

- PRD, product brief, or broad RD.
- Global technical baseline from `flutter-prd-rd-writer`.
- Package stack, architecture assumptions, backend collaboration shape, and delivery constraints.
- Known non-goals and release constraints.
- When refining an active module:
  - active module name
  - existing `docs/rd/modules/<module>/<module>.ui-ux.md`
  - existing `docs/rd/modules/<module>/<module>.impl.md`
  - latest shared freeze artifacts when they exist
  - current workflow record state for that module

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
3. Read the active module row from `docs/rd/00-workflow-record.md` when refining an existing module.
4. Extract business goals, users, flows, pages, states, data dependencies, permissions, analytics, non-goals, and technical constraints.
5. Identify missing information that changes module boundaries or implementation detail depth and list it under `open_questions`.
6. If global package or architecture decisions are missing, block splitting and route to `flutter-prd-rd-writer`.
7. Decide the mode:
   - Initial split mode if paired module docs do not exist yet.
   - Implementation refinement mode if the active module already has paired docs and the workflow is preparing that module for page-level Pen and code.
8. In initial split mode:
   - Build a module map with module name, responsibility, pages, data owner, package or architecture constraints, upstream dependencies, downstream dependencies, and release value.
   - For each module, write a module detail card covering user job, page/state scope, domain responsibility, application state, infrastructure/API boundary, analytics, tests, and release value.
   - Assign document paths:
     - `docs/rd/modules/<module>/<module>.ui-ux.md`
     - `docs/rd/modules/<module>/<module>.impl.md`
   - Write both docs as `split_draft`, not implementation-final.
9. In implementation refinement mode:
   - Refine only the active module's existing docs.
   - Expand the paired docs to implementation-final granularity.
   - Keep inherited global package and architecture decisions unchanged unless the user explicitly requests a baseline revision upstream.
   - Add the detail needed for page-level Pen production and later code implementation, but do not mark the docs as landed here.
10. Ensure the global workflow record path is reserved as `docs/rd/00-workflow-record.md`; stage tracking belongs there, not inside per-module workflow notes.
11. Generate or update `docs/rd/00-module-index.md` when the user asks for files to be written.
12. Return workflow recommendations instead of editing the workflow record directly:
   - Initial split mode normally recommends `current_state=modules_split`, `uiux_status=split_draft`, and `impl_status=split_draft`.
   - Implementation refinement mode normally recommends `current_state=pen_ready`, `uiux_status=implementation_final`, and `impl_status=implementation_final`.

## UI/UX RD Contract

Each `<module>.ui-ux.md` must include these minimum sections:

- Module goal and target user.
- Page scope and navigation entry.
- Core user path.
- State matrix.
- Design source section.
- Design freeze card section.
- Acceptance gates for UI/UX and Pencil handoff.

### Split-draft minimum

In initial split mode, the document must cover:

- Module goal and user value.
- Page family and navigation ownership.
- Core path and key alternate states.
- Coarse state matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Shared design references and future Pencil placeholders when approved static previews exist.
- Open questions that block implementation-level detail later.

### Implementation-final expansion

In implementation refinement mode, expand the same document to directly implementable granularity:

- Page-by-page structure and section hierarchy.
- Component inventory and reuse boundaries for that module.
- Interaction rules, transitions, disabled logic, and recovery paths.
- Edge-state handling that code must preserve.
- Immutable visual or behavioral constraints versus explicitly adjustable items.
- Exact inputs needed by `design-preview-to-pen`.
- Acceptance gates for page-level Pen and code handoff.

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
- Statement that implementation must not change approved UI/UX decisions after freeze.

### Split-draft minimum

In initial split mode, the implementation RD must identify:

- Bounded context and business responsibility.
- Data owners and backend dependencies.
- High-level application state and persistence boundaries.
- Package usage notes inherited from the baseline.
- Early risks and open questions.

### Implementation-final expansion

In implementation refinement mode, expand the same document to directly implementable granularity:

- Screen-level state ownership and coordination.
- Detailed loading, empty, retry, permission, and failure behavior.
- Navigation contract, entry conditions, and return behavior.
- Repository/service responsibilities and mutation boundaries.
- Analytics events, monitoring hooks, and test scope at implementation level.
- Explicit notes about how the later landed Pen source must be consumed by code.

## Hard Rules

- Do not write shared visual direction; route that to `mobile-ui-design-coach`.
- Do not freeze screenshot-based global guidance or concrete theme values here; route that to `design-preview-to-global-guidelines`.
- Do not rebuild page-level Pen or assets here; route that to `design-preview-to-pen`.
- Do not choose packages or create the global technical scheme; route that to `flutter-prd-rd-writer`.
- Do not override package or architecture decisions from the global technical baseline; record exceptions as open questions.
- Do not generate Flutter screen architecture from `.pen`; route that to `flutter-pen-to-architecture` after `.pen` is frozen.
- Do not create per-module workflow state files; use `docs/rd/00-workflow-record.md` through `flutter-workflow-orchestrator`.
- Do not split implementation modules from a raw PRD unless the user explicitly asks for a rough discovery split and accepts that technical decisions are pending.
- Do not output module names only. Each module needs enough detail for its paired UI/UX and implementation RD documents.
- Do not merge UI/UX RD and implementation RD into one document.
- Do not let implementation RD exist without a reference to the paired UI/UX RD.
- Do not treat the first split output as implementation-ready.
- Do not freeze module page-level or module-private component design on the initial split pass.
- Do not mark `uiux_status` or `impl_status` as `landed` here. Landed status only happens after the corresponding page-level Pen is delivered and confirmed through the orchestrator.
- Do not refine unrelated modules when only one active module is entering implementation preparation.

## Output Contract

Return:

- `module_split_table`
- `document_paths`
- `module_detail_cards`
- `module_dependencies`
- `global_technical_baseline`
- `initial_workflow_states`
- `document_maturity_recommendation`
- `refinement_scope`
- `open_questions`
- `next_skill_recommendation`

## Pressure Scenarios

- A PRD lists ten screens but one user job: group by workflow, not by screen count.
- A raw PRD has no package or architecture decision: route to `flutter-prd-rd-writer` before creating implementation module docs.
- A split contains only module names: fail the output and add module detail cards.
- A module has backend-heavy logic but no UI: still create paired docs; UI/UX RD can declare no visible page and explain state surfaces.
- User asks for a new global package or architecture decision during splitting: stop and route to `flutter-prd-rd-writer`.
- User asks to start building one module that still has draft docs: stay focused on that module and refine it to implementation-final instead of re-splitting the whole project.
