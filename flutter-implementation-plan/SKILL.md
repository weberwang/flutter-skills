---
name: flutter-implementation-plan
description: Use when converting Flutter product, UX, UI, or architecture specs into milestones, implementation tasks, task briefs, acceptance criteria, test plans, or a build sequence for Codex.
---

# Flutter Implementation Plan

## Overview

Convert approved specs into a coarse cross-module build sequence, then refine each module just in time into small, verifiable Flutter implementation tasks after its module-level grilling gate. This keeps global dependencies visible without pretending every module and page function is settled before implementation reaches it.

## Inputs

- Product brief and MVP scope.
- Screen specs and UI quality gates.
- Technical design.
- Module boundaries, page flow, and cross-module contracts.
- Existing app structure, if this is not a greenfield app.
- Product grilling log and the current module's implementation-stage confirmation when refining that module.

## Module Planning Rules

- Define modules by product responsibility, route ownership, data ownership, and page interactions, not just folder names.
- Keep modules independently deliverable where possible, but record every required cross-module contract.
- Assign every module and page a business-flow level based on the prerequisite user outcome, shared foundation, contract, and page interaction it requires; do not infer levels from folders or technical layers alone.
- Order levels from shared foundations through the primary user path to dependent secondary paths. Complete the acceptance paths and required contracts of one level before beginning the next.
- Within a module, assign page levels from user interaction sequence and state dependency; pages in a later level cannot start before their prerequisite page level passes.
- If two modules interact, identify the contract task before either module implements UI against that contract.
- Do not split a module so finely that one user action requires multiple agents to change the same files in parallel.
- Treat the initial implementation plan as coarse. Record module boundaries, known pages, dependencies, contracts, levels, and acceptance paths, but defer final function/page/task refinement until the module becomes eligible for implementation.
- When a module first becomes eligible, run `grilling` again and confirm included functions, non-goals, page/state boundaries, dependencies, and its acceptance path. Only after explicit shared-understanding confirmation may `docs/plans/modules/<module-name>-scope.md` refine the module and page functions.

## Task Rules

- One task should produce one vertical slice or one isolated foundation.
- Create task briefs from the confirmed module scope, not directly from the coarse global plan.
- Route every task through `flutter-app-orchestrator/references/subagent-map.md`. Record one DRI core role, one independent acceptance role, optional specialist seat, consulted roles, omitted-role reasons, exact read/write/non-scope, and shared-resource locks.
- Route Flutter work to Flutter Engineer, API/schema/migration work to Backend/Data Engineer, cross-cutting technical work to Tech Lead, quality evidence to QA Engineer, and build/pipeline/release work to DevOps/Release Engineer. Do not use a generic implementer when the owning discipline is known.
- Each task must list scope, non-scope, files likely touched, acceptance criteria, verification commands, task-state path, integration base commit, task branch/worktree, Controller integration worktree, and the `finalize-task.py` command used after independent approval.
- Keep an active task-state file only in the Controller integration worktree and uncommitted after the task branch is created; the task branch must not contain that active state file. The finalizer alone records `integrating` and `accepted` after its merge succeeds.
- Each task must follow `docs/architecture/verification-platforms.md`; do not duplicate platform scope or claim an unrecorded platform as verified. Run integration smoke after each business-flow level merges to the integration branch; reserve the full device, emulator, simulator, browser, and desktop matrix for final integration.
- UI tasks must include screenshot or golden evidence requirements.
- Risky shared foundations must happen before dependent feature tasks.
- Module entry tasks must establish routing, state boundary, contracts, and test scaffolding before page tasks.
- A task brief must name its business-flow level and the prior-level evidence it depends on.
- Task briefs must distinguish level integration smoke from the final platform matrix; task-level screenshots or goldens are design evidence only.
- Do not plan parallel implementation tasks that write the same files, generated files, dependencies, routes, themes, shared state containers, or the canonical Pencil file. Record a single owner for every shared resource.

## Output Files

- `docs/plans/module-map.md`
- `docs/plans/modules/<module-name>-scope.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`
- `.codex-workflow/tasks/<task-id>.yaml`
- `docs/tasks/<task-id>/`

Use [references/module-map-template.md](references/module-map-template.md), [references/module-scope-template.md](references/module-scope-template.md), [references/implementation-plan-template.md](references/implementation-plan-template.md), and [references/task-brief-template.md](references/task-brief-template.md).

## Default Milestones

1. Project foundation.
2. Design system and navigation shell.
3. Core data model and services.
4. Primary user path.
5. Account, settings, and privacy.
6. Monetization if in MVP.
7. Analytics, crash reporting, and release hardening.

## Gate

Do not refine or execute an implementation task until the current module has completed implementation-stage `grilling`, the explicit shared-understanding confirmation is recorded in `docs/product/grilling-log.md`, and `docs/plans/modules/<module-name>-scope.md` contains the confirmed function inventory and page-function refinement. Execution also requires an isolated task brief, a validated task-state claim, clean integration base commit, dedicated branch/worktree, a clean Controller-owned integration worktree, a recorded task profile, one DRI, one independent acceptance owner, role activation reasons, non-overlapping write scopes, shared-resource locks, `docs/architecture/verification-platforms.md`, named verification commands, `docs/plans/module-map.md`, `docs/architecture/flutter-init.md`, a generated project-local `flutter-dev` path for Flutter work, and evidence that all prerequisite business-flow levels have passed or are explicitly accepted. Follow [../flutter-subagent-delivery/references/collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md).
