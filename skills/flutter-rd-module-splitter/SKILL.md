---
name: flutter-rd-module-splitter
description: Use when a Flutter PRD plus global technical baseline must be decomposed into bounded modules with paired draft UI/UX and implementation RDs, or when an active module entering implementation preparation needs the paired-doc refinement contract that `@superpowers` should execute against.
---

# Flutter RD Module Splitter

## Overview

Split broad Flutter product requirements into executable modules after the global technical baseline exists.

This skill has two modes:

1. Initial split mode: create paired `ui-ux` and `impl` draft documents for each module during `modules_split`, while defining module dependencies and parallel implementation stages in the module index.
2. Implementation refinement contract mode: define how one active module's existing paired docs must be refined to implementation-final granularity after shared image-backed design direction is available.

The initial split is not page-level freeze and not implementation-ready by default. It creates structured drafts, module boundaries, and an explicit implementation-order view. The later refinement contract defines what one active module must contain before design freeze and code without pretending the whole product is already landed. In the default workflow, that refinement execution must be explicitly carried out through `@superpowers`, while this skill remains the source of truth for paired-doc structure and refinement completeness. The default workflow no longer prepares page-level Pen artifacts; it prepares a frozen UI/UX design-source packet for Flutter architecture and code.

This skill defines one active module's refinement target per call. When `flutter-workflow --auto` is driving the workflow, the orchestrator should reuse this contract across dependency-safe modules until all target modules reach the pre-implementation boundary, not stop after one refined module.

## Required Inputs

- PRD, product brief, or broad RD.
- Global technical baseline from `flutter-prd-rd-writer`.
- Package stack, architecture assumptions, backend collaboration shape, and delivery constraints.
- Known non-goals and release constraints.
- Confirmed Product Design clarification packet or equivalent structured record covering core user journeys, page families, critical states, interaction goals, explicit `platform_identifier`, platform-aware navigation or feedback expectations, and per-surface information-density posture.
- When refining an active module:
  - active module name
  - existing `docs/project/modules/<module>/<module>.ui-ux.md`
  - existing `docs/project/modules/<module>/<module>.impl.md`
  - latest shared freeze artifacts when they exist
  - latest approved image-backed design packet or equivalent image-derived design constraints
  - current workflow record state for that module

If the global technical baseline is missing, stop and route to `flutter-prd-rd-writer` before splitting implementation modules.

## Module Boundary Rules

Create a module when the scope has at least one stable ownership boundary:

- A distinct user job or workflow.
- A distinct navigation entry, page family, or repeated screen pattern.
- A distinct domain model, backend contract, permission boundary, or state lifecycle.
- A release slice that can be designed, implemented, tested, and reviewed independently.

Do not create a module only because a screen exists. Small screens that share one user job and data lifecycle should stay in the same module.

Each page family must have exactly one owning module. Other modules may depend on that flow, launch it, or reuse shared components from it, but they must not claim parallel ownership of the same page family.

Do not split a list page, detail page, filter page, and state variants into different modules when they still serve the same primary user job, the same core data owner, and the same state lifecycle. Unless a real permission boundary, release slice boundary, or independent backend ownership proves otherwise, keep that task chain inside one module.

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
3. Read the active module row from the current workflow-record runtime artifact when refining an existing module, if that runtime artifact exists for the current run.
4. Read the confirmed Product Design clarification packet and treat it as the authority for user journeys, page families, critical states, interaction goals, target platform fit, and page-density posture before splitting or refining modules.
5. Extract business goals, users, flows, pages, states, data dependencies, permissions, analytics, non-goals, technical constraints, and platform-aware information-density constraints.
6. Identify missing information that changes module boundaries, platform-specific density decisions, or implementation detail depth and list it under `open_questions`.
7. If global package or architecture decisions are missing, block splitting and route to `flutter-prd-rd-writer`.
8. Decide the mode:
   - Initial split mode if paired module docs do not exist yet.
   - Implementation refinement contract mode if the active module already has paired docs and the workflow is preparing that module for module design freeze and code.
9. In initial split mode:
   - Build a module map with module name, responsibility, pages, data owner, package or architecture constraints, upstream dependencies, downstream dependencies, implementation preconditions, and release value.
   - For every page family, assign exactly one owning module and record that ownership explicitly before approving the split.
   - Evaluate whether the product needs a dedicated `app-shell` module before feature-module decomposition. If multiple features share one root scaffold, root navigation state, or shell-level routing logic, split that shell out explicitly instead of hiding it inside prose.
   - For each module, write a module detail card covering user job, page/state scope, non-page-level component scope, domain responsibility, application state, infrastructure/API boundary, analytics, tests, release value, and implementation dependency notes.
   - Classify the modules into implementation stages or waves that show which modules can run in parallel and which modules must wait for upstream completion.
   - Assign document paths:
      - `docs/project/modules/<module>/<module>.ui-ux.md`
      - `docs/project/modules/<module>/<module>.impl.md`
   - Write both docs as `split_draft`, not implementation-final.
   - Mark each module with its initial workflow state, normally `modules_split`, so `flutter-workflow` can write that state into the global workflow record.
10. In implementation refinement contract mode:
   - Refine only the active module's existing docs.
   - Expand the paired docs to implementation-final granularity.
   - Keep inherited global package and architecture decisions unchanged unless the user explicitly requests a baseline revision upstream.
   - Add the detail needed for module design-source freeze and later code implementation, but do not mark the docs as landed here.
   - Incorporate the approved image-backed design direction into page hierarchy, typography intent, contrast posture, CTA priority, spacing rhythm, motion role, and anti-template rules.
   - In the default workflow, treat this as the document contract that `@superpowers` must explicitly execute rather than a reason to bypass `@superpowers`.
11. Keep global workflow state under orchestrator ownership; stage tracking belongs there, not inside per-module workflow notes.
12. Generate or update `docs/project/00-module-index.md` when the user asks for files to be written.
13. Treat `docs/project/00-module-index.md` as the canonical split-stage coordination index:
   - Include a module table with module name, responsibility summary, paired doc paths, `depends_on`, `unblocks`, `parallel_group`, recommended implementation stage, `owned_page_families`, `shared_surface_dependencies`, and blocking assumptions.
   - Include a parallel execution section that groups modules by stage or wave and explicitly states which modules can be implemented in the same stage.
   - Include dependency notes that explain why a module must precede another module when the dependency is not obvious from the table alone.
14. In implementation refinement contract mode, update only the affected module row and any directly impacted stage or dependency notes unless the refinement reveals a real module-boundary change.
15. Return workflow recommendations instead of editing the workflow record directly:
   - Initial split mode normally recommends `current_state=modules_split`, `uiux_status=split_draft`, and `impl_status=split_draft`.
   - Implementation refinement contract mode normally recommends `current_state=module_uiux_refinement`, `uiux_status=implementation_final`, and `impl_status=implementation_final`.
   - Those recommendations are local module results, not an instruction for `--auto` to stop after the current module.

## Module Index Contract

When `docs/project/00-module-index.md` is written or updated, it must be useful for both planning and execution handoff.

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
- `owned_page_families`
- `shared_surface_dependencies`
- `parallelization_notes`

## UI/UX RD Contract

Each `<module>.ui-ux.md` must include these minimum sections:

- Module goal and target user.
- Page scope and navigation entry.
- Core user path.
- State matrix.
- Platform fit and information-density posture.
- Structure semantics section.
- Design source section.
- Design freeze card section.
- Module-level non-page component design skeleton covering repeated controls, cards, bars, list items, dialogs, chips, or other shared building blocks that belong to the module.
- For each important module-level component, document at least intended usage scope, expected states or variants, reuse boundaries, and whether the component is expected to be frozen in the module design-source packet.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Structure semantics section must include at least:
  - `scroll_model`: whole-page scroll, local scroll, fixed zone, or mixed
  - `list_model`: static block, repeated list, grouped list, grid, or mixed
  - `overlay_model`: none, floating action, badge overlay, bottom action area, modal layer, or mixed
  - `layout_model`: linear, layered, relative-positioned, or mixed
  - `sticky_model`: none, sticky header, sticky tab/filter, sticky footer, or mixed
  - `component_repeatability`: which parts must become reusable repeated components
- Platform fit and information-density posture must include at least:
  - `platform_surface`: the concrete primary surface this module page family is targeting
  - `primary_task_visibility`: what must be visible immediately on first screen for the main task
  - `deferred_or_secondary_content`: what must move below the fold, behind disclosure, into another step, or onto a secondary surface
  - `density_posture`: lean, standard, or dense, with platform-specific rationale rather than personal taste
  - `platform_adaptation_notes`: navigation, gesture, focus, hover, safe-area, and feedback expectations that materially affect density or page structure
- Design source section with approved image-backed design direction, future visual evidence, and future `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` references when approved static previews exist.
- Design source section must not assume new module real-device preview generation by default. If module-stage additional image evidence is intended, reserve that as explicit later evidence instead of implied future work.
- Design freeze card section reserved for later approval, including reserved fields for module-level component freeze decisions.
- Acceptance gates for UI/UX, module design freeze, and code handoff.

### Split-draft minimum

In initial split mode, the document must cover:

- Module goal and user value.
- Page family and navigation ownership.
- Core path and key alternate states.
- Coarse state matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Initial platform fit and information-density posture, including what is required on first screen versus what may be deferred or collapsed on the primary platform.
- Initial structure semantics for scroll, list, overlay, layout, sticky behavior, and component repeatability.
- Shared design references, image-derived design constraints, and future visual-evidence placeholders when approved static previews exist.
- If the module still lacks approved module-stage visuals, keep that as an explicit optional placeholder. Do not imply that refinement will auto-generate new previews by default.
- Open questions that block implementation-level detail later.
- If a shell module exists, the document must state whether navigation ownership belongs to that shell or to the current module.

### Implementation-final expansion

In implementation refinement contract mode, expand the same document to directly implementable granularity:

- Page-by-page structure and section hierarchy.
- Platform-specific density decisions for each important page or page family, including what must stay visible immediately, what must move into disclosure, and what must become a separate surface.
- Explicit structure semantics refined enough for implementation decisions. Do not leave scroll, list, overlay, or sticky behavior implied only by screenshots.
- Component inventory and reuse boundaries for that module.
- Interaction rules, transitions, disabled logic, and recovery paths.
- Edge-state handling that code must preserve.
- Immutable visual or behavioral constraints versus explicitly adjustable items.
- Exact inputs needed for module design-source freeze and architecture planning.
- If module-stage additional image evidence is requested, state that it is explicit opt-in evidence, not a default refinement side effect.
- Acceptance gates for module design freeze and code handoff.

## Implementation RD Contract

Each `<module>.impl.md` must include:

- Explicit reference to the paired UI/UX RD.
- Explicit reference to the global technical baseline.
- Business capability and bounded context.
- Inherited global package stack and module-specific usage notes.
- Domain model, application state, infrastructure dependencies, presentation boundary.
- Explicit reference to the Product Design clarification packet or its equivalent structured record for journeys, page families, critical states, platform fit, and information density.
- Module-level component implementation notes that reference the paired UI/UX RD component skeleton instead of inventing reusable components from scratch later.
- API, repository, storage, permission, and backend collaboration notes.
- Data, security, analytics, monitoring, rollout, and test scope.
- Module-specific implementation constraints that do not override global decisions.
- Statement that implementation must not change approved UI/UX decisions after freeze.
- A scan-friendly refinement provenance block with `superpowers_refinement_status`.
- Optional `superpowers_refinement_date` and `superpowers_refinement_notes` when the provenance needs extra audit detail.

Use these provenance values consistently:

- `verified_executed`: only when the active module refinement was truly executed through explicit `@superpowers` invocation and the execution can be traced in the workflow record or a project-level execution trace.
- `not_executed`: the document exists, but this module has not yet gone through a real `@superpowers` refinement pass.
- `unknown`: the document existed before the current audit and the team cannot yet prove whether the refinement was truly executed through `@superpowers`.

### Split-draft minimum

In initial split mode, the implementation RD must identify:

- Bounded context and business responsibility.
- Data owners and backend dependencies.
- High-level application state and persistence boundaries.
- Package usage notes inherited from the baseline.
- Dependencies on shared shells, contracts, or prerequisite modules that affect implementation order.
- Early risks and open questions.
- If `app-shell` exists, the implementation RD must state which root navigation, redirect, or shell-state responsibilities stay in the shell and which belong to the module.
- Set `superpowers_refinement_status: not_executed` because initial split output is not a real refinement pass.

### Implementation-final expansion

In implementation refinement contract mode, expand the same document to directly implementable granularity:

- Screen-level state ownership and coordination.
- Detailed loading, empty, retry, permission, and failure behavior.
- Navigation contract, entry conditions, and return behavior.
- Platform-specific page-density implementation notes, including which content stays first-screen visible, which content is progressively disclosed, and which content must move to another surface to preserve task clarity.
- Repository/service responsibilities and mutation boundaries.
- Analytics events, monitoring hooks, and test scope at implementation level.
- Explicit notes about how the later frozen design-source packet must be consumed by code.
- Display-layer decision notes that explain which parts are visually inferred from preview images and which parts are fixed by documented interaction or state semantics.
- Update the refinement provenance block so it reflects reality instead of document completeness alone.
- Set `superpowers_refinement_status: verified_executed` only after a real `@superpowers` refinement run on this active module.
- If the document was manually edited, batch-generated, or retroactively reconstructed without a real `@superpowers` execution trace, keep `superpowers_refinement_status` as `not_executed` or `unknown`.

## Hard Rules

- Do not write shared visual direction from abstract prose alone; route that to the approved image-backed design-source flow.
- Do not freeze screenshot-based global guidance or concrete theme values here; route that to `design-preview-to-global-guidelines`.
- Do not rebuild page-level Pen or assets here. Pen is optional and outside the default workflow.
- Do not choose packages or create the global technical scheme; route that to `flutter-prd-rd-writer`.
- Do not override package or architecture decisions from the global technical baseline; record exceptions as open questions.
- Do not generate Flutter screen architecture here; route architecture planning after the module design-source packet is frozen.
- Do not create per-module workflow state files; keep workflow state under `flutter-workflow` control.
- Do not split implementation modules from a raw PRD unless the user explicitly asks for a rough discovery split and accepts that technical decisions are pending.
- Do not output module names only. Each module needs enough detail for its paired UI/UX and implementation RD documents.
- Do not approve a split where the same page family appears as owned by more than one module.
- Do not leave page-family ownership implicit. If the owning module is unclear, block the split and record the ambiguity in `open_questions`.
- Do not split one task chain across multiple modules when the list, detail, filter, and state surfaces still share one user job, one core data owner, and one state lifecycle.
- Do not merge UI/UX RD and implementation RD into one document.
- Do not let implementation RD exist without a reference to the paired UI/UX RD.
- Do not hide implementation sequencing only inside prose. Dependency and parallel-execution decisions must be visible in `docs/project/00-module-index.md` and in the structured output.
- Do not mark two modules as safe to implement in parallel when they still share an unresolved backend contract, shared route shell, shared permission owner, or unfrozen shared component dependency.
- Do not guess at safe parallelism when critical dependencies are unknown; record the uncertainty in `open_questions` and mark the parallel decision as conditional.
- Do not treat the first split output as implementation-ready.
- Do not freeze module page-level or module-private component design on the initial split pass.
- Do not mark `uiux_status` or `impl_status` as `landed` here. Landed status only happens after the module design-source packet is frozen and confirmed through the orchestrator.
- Do not refine unrelated modules when only one active module is entering implementation preparation.
- Do not reinterpret one module's refinement result as completion of the whole auto run. Cross-module continuation belongs to `flutter-workflow`.
- Do not let this skill bypass `@superpowers` for default-workflow module refinement execution.
- Do not directly use this skill as the execution engine for active-module refinement in the default workflow; the actual refinement step must be invoked through `@superpowers`.
- Do not set `superpowers_refinement_status=verified_executed` from manual doc edits, inferred completeness, or post-hoc bookkeeping.
- Do not leave the refinement provenance block out of `<module>.impl.md`; the status must stay explicit even when it is `not_executed` or `unknown`.
- Do not leave module-level reusable components completely undefined in UI/UX RD when the module clearly contains repeated non-page building blocks.
- Do not leave scroll, list, overlay, relative-layout, or sticky behavior to image-only interpretation when the module is entering implementation preparation.
- Do not split or refine modules without the confirmed Product Design clarification packet or an equivalent structured record for journeys, page families, critical states, platform fit, and information density.
- Do not describe page density only as "show more" or "show less". State exactly what stays first-screen visible, what is progressively disclosed, and what must move to another surface for the target platform.
- Do not imply that module refinement will auto-generate new real-device previews by default.
- Do not perform detailed module UI/UX refinement before image-backed design direction exists. If image-backed design direction is missing, block and route upstream.
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
