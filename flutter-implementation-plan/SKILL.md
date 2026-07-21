---
name: flutter-implementation-plan
description: Use when converting Flutter product, UX, UI, or architecture specs into milestones, implementation tasks, task briefs, acceptance criteria, test plans, or a build sequence for Codex.
---

# Flutter Implementation Plan

## Overview

Convert approved specs into small, verifiable Flutter implementation tasks. A good plan separates global design from module delivery, then derives business-flow levels from dependency and page interaction flow so Codex or subagents can execute without guessing scope.

## Inputs

- Product brief and MVP scope.
- Screen specs and UI quality gates.
- Technical design.
- Module boundaries, page flow, and cross-module contracts.
- Existing app structure, if this is not a greenfield app.

## Module Planning Rules

- Define modules by product responsibility, route ownership, data ownership, and page interactions, not just folder names.
- Keep modules independently deliverable where possible, but record every required cross-module contract.
- Assign every module and page a business-flow level based on the prerequisite user outcome, shared foundation, contract, and page interaction it requires; do not infer levels from folders or technical layers alone.
- Order levels from shared foundations through the primary user path to dependent secondary paths. Complete the acceptance paths and required contracts of one level before beginning the next.
- Within a module, assign page levels from user interaction sequence and state dependency; pages in a later level cannot start before their prerequisite page level passes.
- If two modules interact, identify the contract task before either module implements UI against that contract.
- Do not split a module so finely that one user action requires multiple agents to change the same files in parallel.

## Task Rules

- One task should produce one vertical slice or one isolated foundation.
- Each task must list scope, non-scope, files likely touched, acceptance criteria, verification commands, base commit, task branch/worktree, and its task-state path.
- Each task must follow `docs/architecture/verification-platforms.md`; do not duplicate platform scope or claim an unrecorded platform as verified. Run integration smoke after each business-flow level merges to the integration branch; reserve the full device, emulator, simulator, browser, and desktop matrix for final integration.
- UI tasks must include screenshot or golden evidence requirements.
- Risky shared foundations must happen before dependent feature tasks.
- Module entry tasks must establish routing, state boundary, contracts, and test scaffolding before page tasks.
- A task brief must name its business-flow level and the prior-level evidence it depends on.
- Task briefs must distinguish level integration smoke from the final platform matrix; task-level screenshots or goldens are design evidence only.
- Do not plan parallel implementation tasks that write the same files, global design artifacts, generated files, dependencies, routes, themes, or shared state containers. Record a single owner for every such shared path.
- Store each UI page's design artifacts under `docs/design/pages/<page-name>/` and each task's reports under `docs/tasks/<task-id>/`; never use a global page-design filename for multiple tasks.

## Output Files

- `docs/plans/module-map.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`

Use [references/module-map-template.md](references/module-map-template.md), [references/implementation-plan-template.md](references/implementation-plan-template.md), and [references/task-brief-template.md](references/task-brief-template.md).

## Default Milestones

1. Project foundation.
2. Design system and navigation shell.
3. Core data model and services.
4. Primary user path.
5. Account, settings, and privacy.
6. Monetization if in MVP.
7. Analytics, crash reporting, and release hardening.

## Gate

Do not execute a Flutter implementation task until it has an isolated task brief, task-state claim, clean integration base commit, isolated branch/worktree, `docs/architecture/verification-platforms.md`, named verification commands, `docs/plans/module-map.md`, `docs/architecture/flutter-init.md`, a generated project-local `flutter-dev` path, and evidence that all prerequisite business-flow levels have passed or are explicitly accepted. Follow [../flutter-subagent-delivery/references/collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md).
