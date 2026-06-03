---
name: flutter-rd-module-splitter
description: Use when a Flutter PRD plus global technical baseline must be decomposed into bounded modules with paired draft UI/UX and implementation RDs, or when an active module entering implementation preparation must refine those drafts into implementation-final documents.
---

# Flutter RD Module Splitter

## Overview

Split broad Flutter product requirements into executable modules after the global technical baseline exists.

This skill has two modes:

1. Initial split mode: create paired `ui-ux` and `impl` draft documents for each module during `modules_split`, while defining module dependencies and parallel implementation stages in the module index.
2. Implementation refinement mode: revisit one active module during implementation preparation and refine its existing draft docs to implementation-final granularity after shared taste direction is available.

The initial split is not page-level freeze and not implementation-ready by default. It creates structured drafts, module boundaries, and an explicit implementation-order view. The later refinement pass turns one active module into an implementation-ready document set without pretending the whole product is already landed. The default workflow no longer prepares page-level Pen artifacts; it prepares a frozen UI/UX design-source packet for Flutter architecture and code.

This skill refines one active module per call. When `flutter-workflow-orchestrator --auto` is driving the workflow, the orchestrator must call this skill repeatedly across dependency-safe modules until all target modules reach the pre-implementation boundary, not stop after one refined module.

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
  - latest taste direction packet or equivalent taste constraints
  - current workflow record state for that module

If the global technical baseline is missing, stop and route to `flutter-prd-rd-writer` before splitting implementation modules.

## Module Boundary Rules

Create a module when the scope has at least one stable ownership boundary:

- A distinct user job or workflow.
- A distinct navigation entry, page family, or repeated screen pattern.
- A distinct domain model, backend contract, permission boundary, or state lifecycle.
- A release slice that can be designed, implemented, tested, and reviewed independently.

Do not create a module only because a screen exists. Small screens that share one user job and data lifecycle should stay in the same module.

Create a dedicated shell module, preferably named `app-shell` or `root-shell`, when the root container itself has independent implementation value, such as:

- root navigation state
- bottom-tab or top-tab persistence
- auth-aware root redirects
- deep-link dispatch at the shell layer
- shared app bar, FAB, badge, or overlay orchestration
- a shared route host that feature modules depend on before they can be implemented safely

Do not default to a vague technical module name like `main`. Prefer a responsibility name such as `app-shell`.

## Workflow

1. Read the PRD, RD, feature brief, or user notes.
2. Read the global technical baseline, especially architecture, package stack, backend contracts, data security, analytics, monitoring, rollout, and release assumptions.
3. Read the active module row from `docs/rd/00-workflow-record.md` when refining an existing module.
4. Extract business goals, users, flows, pages, states, data dependencies, permissions, analytics, non-goals, and technical constraints.
5. Identify missing information that changes module boundaries or implementation detail depth and list it under `open_questions`.
6. If global package or architecture decisions are missing, block splitting and route to `flutter-prd-rd-writer`.
7. Decide the mode:
   - Initial split mode if paired module docs do not exist yet.
   - Implementation refinement mode if the active module already has paired docs and the workflow is preparing that module for module design freeze and code.
8. In initial split mode:
   - Build a module map with module name, responsibility, pages, data owner, package or architecture constraints, upstream dependencies, downstream dependencies, implementation preconditions, and release value.
   - Evaluate whether the product needs a dedicated `app-shell` module before feature-module decomposition. If multiple features share one root scaffold, root navigation state, or shell-level routing logic, split that shell out explicitly instead of hiding it inside prose.
   - For each module, write a module detail card covering user job, page/state scope, non-page-level component scope, domain responsibility, application state, infrastructure/API boundary, analytics, tests, release value, and implementation dependency notes.
   - Classify the modules into implementation stages or waves that show which modules can run in parallel and which modules must wait for upstream completion.
   - Assign document paths:
      - `docs/rd/modules/<module>/<module>.ui-ux.md`
      - `docs/rd/modules/<module>/<module>.impl.md`
   - Write both docs as `split_draft`, not implementation-final.
   - Mark each module with its initial workflow state, normally `modules_split`, so `flutter-workflow-orchestrator` can write that state into the global workflow record.
9. In implementation refinement mode:
   - Refine only the active module's existing docs.
   - Expand the paired docs to implementation-final granularity.
   - Keep inherited global package and architecture decisions unchanged unless the user explicitly requests a baseline revision upstream.
   - Add the detail needed for module design-source freeze and later code implementation, but do not mark the docs as landed here.
   - Incorporate taste direction into page hierarchy, typography intent, contrast posture, CTA priority, spacing rhythm, motion role, and anti-template rules.
10. Ensure the global workflow record path is reserved as `docs/rd/00-workflow-record.md`; stage tracking belongs there, not inside per-module workflow notes.
11. Generate or update `docs/rd/00-module-index.md` when the user asks for files to be written.
12. Treat `docs/rd/00-module-index.md` as the canonical split-stage coordination index:
   - Include a module table with module name, responsibility summary, paired doc paths, `depends_on`, `unblocks`, `parallel_group`, recommended implementation stage, and blocking assumptions.
   - Include a parallel execution section that groups modules by stage or wave and explicitly states which modules can be implemented in the same stage.
   - Include dependency notes that explain why a module must precede another module when the dependency is not obvious from the table alone.
13. In implementation refinement mode, update only the affected module row and any directly impacted stage or dependency notes unless the refinement reveals a real module-boundary change.
14. Return workflow recommendations instead of editing the workflow record directly:
   - Initial split mode normally recommends `current_state=modules_split`, `uiux_status=split_draft`, and `impl_status=split_draft`.
   - Implementation refinement mode normally recommends `current_state=module_uiux_refinement`, `uiux_status=implementation_final`, and `impl_status=implementation_final`.
   - Those recommendations are local module results, not an instruction for `--auto` to stop after the current module.

## Module Index Contract

When `docs/rd/00-module-index.md` is written or updated, it must be useful for both planning and execution handoff.

At minimum, the index must contain:

- A module summary table.
- A dependency summary for upstream and downstream relationships.
- A parallel execution plan that groups modules into implementation stages or waves.
- Notes for assumptions or unresolved constraints that make a parallel decision conditional.
- Explicit shell-module notes when a root shell exists or is intentionally not split.

For each module row, include at least:

- `module_name`
- `goal_or_scope`
- `uiux_doc`
- `impl_doc`
- `depends_on`
- `unblocks`
- `parallel_group`
- `recommended_stage`
- `parallelization_notes`

## UI/UX RD Contract

Each `<module>.ui-ux.md` must include these minimum sections:

- Module goal and target user.
- Page scope and navigation entry.
- Core user path.
- State matrix.
- Design source section.
- Design freeze card section.
- Module-level non-page component design skeleton covering repeated controls, cards, bars, list items, dialogs, chips, or other shared building blocks that belong to the module.
- For each important module-level component, document at least intended usage scope, expected states or variants, reuse boundaries, and whether the component is expected to be frozen in the module design-source packet.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Design source section with taste direction, future visual evidence, and future `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` references when approved static previews exist.
- Design freeze card section reserved for later approval, including reserved fields for module-level component freeze decisions.
- Acceptance gates for UI/UX, module design freeze, and code handoff.

### Split-draft minimum

In initial split mode, the document must cover:

- Module goal and user value.
- Page family and navigation ownership.
- Core path and key alternate states.
- Coarse state matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Shared design references, taste constraints, and future visual-evidence placeholders when approved static previews exist.
- Open questions that block implementation-level detail later.
- If a shell module exists, the document must state whether navigation ownership belongs to that shell or to the current module.

### Implementation-final expansion

In implementation refinement mode, expand the same document to directly implementable granularity:

- Page-by-page structure and section hierarchy.
- Component inventory and reuse boundaries for that module.
- Interaction rules, transitions, disabled logic, and recovery paths.
- Edge-state handling that code must preserve.
- Immutable visual or behavioral constraints versus explicitly adjustable items.
- Exact inputs needed for module design-source freeze and architecture planning.
- Acceptance gates for module design freeze and code handoff.

## Implementation RD Contract

Each `<module>.impl.md` must include:

- Explicit reference to the paired UI/UX RD.
- Explicit reference to the global technical baseline.
- Business capability and bounded context.
- Inherited global package stack and module-specific usage notes.
- Domain model, application state, infrastructure dependencies, presentation boundary.
- Module-level component implementation notes that reference the paired UI/UX RD component skeleton instead of inventing reusable components from scratch later.
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
- Dependencies on shared shells, contracts, or prerequisite modules that affect implementation order.
- Early risks and open questions.
- If `app-shell` exists, the implementation RD must state which root navigation, redirect, or shell-state responsibilities stay in the shell and which belong to the module.

### Implementation-final expansion

In implementation refinement mode, expand the same document to directly implementable granularity:

- Screen-level state ownership and coordination.
- Detailed loading, empty, retry, permission, and failure behavior.
- Navigation contract, entry conditions, and return behavior.
- Repository/service responsibilities and mutation boundaries.
- Analytics events, monitoring hooks, and test scope at implementation level.
- Explicit notes about how the later frozen design-source packet must be consumed by code.

## Hard Rules

- Do not write shared visual direction; route that to `flutter-taste-router`.
- Do not freeze screenshot-based global guidance or concrete theme values here; route that to `design-preview-to-global-guidelines`.
- Do not rebuild page-level Pen or assets here. Pen is optional and outside the default workflow.
- Do not choose packages or create the global technical scheme; route that to `flutter-prd-rd-writer`.
- Do not override package or architecture decisions from the global technical baseline; record exceptions as open questions.
- Do not generate Flutter screen architecture here; route architecture planning after the module design-source packet is frozen.
- Do not create per-module workflow state files; use `docs/rd/00-workflow-record.md` through `flutter-workflow-orchestrator`.
- Do not split implementation modules from a raw PRD unless the user explicitly asks for a rough discovery split and accepts that technical decisions are pending.
- Do not output module names only. Each module needs enough detail for its paired UI/UX and implementation RD documents.
- Do not merge UI/UX RD and implementation RD into one document.
- Do not let implementation RD exist without a reference to the paired UI/UX RD.
- Do not hide implementation sequencing only inside prose. Dependency and parallel-execution decisions must be visible in `docs/rd/00-module-index.md` and in the structured output.
- Do not mark two modules as safe to implement in parallel when they still share an unresolved backend contract, shared route shell, shared permission owner, or unfrozen shared component dependency.
- Do not guess at safe parallelism when critical dependencies are unknown; record the uncertainty in `open_questions` and mark the parallel decision as conditional.
- Do not treat the first split output as implementation-ready.
- Do not freeze module page-level or module-private component design on the initial split pass.
- Do not mark `uiux_status` or `impl_status` as `landed` here. Landed status only happens after the module design-source packet is frozen and confirmed through the orchestrator.
- Do not refine unrelated modules when only one active module is entering implementation preparation.
- Do not reinterpret one module's refinement result as completion of the whole auto run. Cross-module continuation belongs to `flutter-workflow-orchestrator`.
- Do not leave module-level reusable components completely undefined in UI/UX RD when the module clearly contains repeated non-page building blocks.
- Do not perform detailed module UI/UX refinement before taste direction exists. If taste direction is missing, block and route upstream.
- Do not hide a real root-shell dependency inside multiple feature modules. If the shell has independent state or routing responsibility, split it explicitly as `app-shell` or `root-shell`.
- Do not create a generic `main` module name. Use a responsibility-driven shell name instead.

## Output Contract

Return:

- `module_split_table`
- `document_paths`
- `module_detail_cards`
- `module_dependencies`
- `parallel_execution_plan`
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
- A module UI/UX RD only lists pages and states but omits obvious shared module components: fail the output and add a component design skeleton.
- A module has backend-heavy logic but no UI: still create paired docs; UI/UX RD can declare no visible page and explain state surfaces.
- User asks for a new global package or architecture decision during splitting: stop and route to `flutter-prd-rd-writer`.
- User asks to start building one module that still has draft docs: stay focused on that module and refine it to implementation-final instead of re-splitting the whole project.
- Two modules share no unresolved navigation, backend, permission, or state-owner dependency: place them in the same recommended implementation stage and record that they are safe to run in parallel.
- A shared shell or foundation module must land before feature modules can proceed: place the shell module in an earlier stage and record the feature modules as dependent, not parallel peers.
- Multiple feature modules share one root scaffold, redirect policy, or tab host with independent state: split an `app-shell` module first instead of burying the shell inside feature modules.
