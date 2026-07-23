---
name: flutter-implementation-plan
description: Use when converting Flutter product, UX, UI, or architecture specs into milestones, implementation tasks, task briefs, acceptance criteria, test plans, or a build sequence for Codex.
---

# Flutter Implementation Plan

## Overview

Convert approved specs into a coarse cross-module build sequence, then refine each eligible module into small, risk-classified and verifiable tasks. Re-enter product questioning only when the module exposes a new or conflicting decision.

## Inputs

- Product brief with MVP scope and user stories.
- UI spec with screen states and quality gates.
- Technical design.
- Module boundaries, page flow, and cross-module contracts.
- Existing app structure, if this is not a greenfield app.
- Product grilling log and any actual module-stage decisions.

## Module Planning Rules

- Define modules by product responsibility, route ownership, data ownership, and page interactions, not just folder names.
- Keep modules independently deliverable where possible, but record every required cross-module contract.
- Assign every module and page a business-flow level based on the prerequisite user outcome, shared foundation, contract, and page interaction it requires; do not infer levels from folders or technical layers alone.
- Order levels from shared foundations through the primary user path to dependent secondary paths. Complete the acceptance paths and required contracts of one level before beginning the next.
- Within a module, assign page levels from user interaction sequence and state dependency; pages in a later level cannot start before their prerequisite page level passes.
- If two modules interact, identify the contract task before either module implements UI against that contract.
- Do not split a module so finely that one user action requires multiple agents to change the same files in parallel.
- Treat the initial implementation plan as coarse. Record module boundaries, known pages, dependencies, contracts, levels, and acceptance paths, but defer final function/page/task refinement until the module becomes eligible for implementation.
- When a module first becomes eligible, audit included functions, non-goals, page/state boundaries, dependencies, and its acceptance path against existing evidence. Run `grilling` only for unresolved or conflicting decisions; otherwise refine directly.

## Task Rules

- One task should produce one vertical slice or one isolated foundation.
- Create task briefs from the confirmed module scope, not directly from the coarse global plan.
- Classify every task with [task-risk-tiers.md](../flutter-subagent-delivery/references/task-risk-tiers.md). Add a DRI, independent acceptance, specialist roles, and shared-resource locks only when the selected tier requires them.
- Route Flutter work to Flutter Engineer, API/schema/migration work to Backend/Data Engineer, cross-cutting technical work to Tech Lead, quality evidence to QA Engineer, and build/pipeline/release work to DevOps/Release Engineer. Do not use a generic implementer when the owning discipline is known.
- Each task must list risk tier, scope, non-scope, acceptance criteria, verified integration base, and executable verification commands. Add task-state, worktree and finalizer fields only for `high`, `release`, or concurrent multi-agent work.
- For a controlled worktree task, keep one active task-state file in the Controller integration worktree and one task worktree through final acceptance. Do not recreate either for review rounds.
- Each task must follow `docs/architecture/verification-platforms.md`; do not duplicate platform scope or claim an unrecorded platform as verified. Run integration smoke after each business-flow level merges to the integration branch; reserve the full device, emulator, simulator, browser, and desktop matrix for final integration.
- UI tasks must include screenshot or golden evidence requirements.
- Deterministic verification and known regression fixtures must execute successfully before formal review starts.
- Risky shared foundations must happen before dependent feature tasks.
- Module entry tasks must establish routing, state boundary, contracts, and test scaffolding before page tasks.
- A task brief must name its business-flow level and the prior-level evidence it depends on.
- Task briefs must distinguish level integration smoke from the final platform matrix; task-level screenshots or goldens are design evidence only.
- Do not plan parallel implementation tasks that write the same files, generated files, dependencies, routes, themes, shared state containers, or the canonical Pencil file. Record a single owner for every shared resource.

## Output Files

- `docs/plans/module-map.md`
- `docs/plans/modules/<module-name>-scope.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`, task-state YAML, and `review.md` only for tiers that require durable coordination or review

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

Do not execute from an uncertain integration base, unresolved material scope, missing acceptance criteria, or unexecutable verification plan. Do not require grilling, worktrees, task-state files, role assembly, independent review, or release evidence merely because the task exists; select them from the risk tier. For controlled multi-agent work, follow [collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md).
