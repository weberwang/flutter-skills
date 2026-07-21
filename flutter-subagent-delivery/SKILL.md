---
name: flutter-subagent-delivery
description: Use when coordinating multi-agent design and implementation of an approved Flutter delivery plan, including UX, visual direction, wireframes, high-fidelity pages, bitmap decomposition, asset production, Pencil restoration, implementation, and independent review.
---

# Flutter Subagent Delivery

## Overview

Run App delivery through role-based feature squads and controlled subagent loops. The controller assembles the smallest sufficient team and owns sequencing, context packaging, user confirmations, freeze gates, conflict resolution, and final integration; core engineering roles and specialized seats perform production and independent review work.

## Roles

Use the core App team, activation rules, task routing, specialist mapping, and decision authority in [../flutter-app-orchestrator/references/subagent-map.md](../flutter-app-orchestrator/references/subagent-map.md). Use the preset positioning, team value, and executable role prompts in [references/app-team-role-prompts.md](references/app-team-role-prompts.md).

The core roles are Controller, Product Manager, UX/UI Lead, Tech Lead, Flutter Engineer, Backend/Data Engineer, QA Engineer, and DevOps/Release Engineer. Market, visual direction, wireframe, high-fidelity, asset, Pencil, architecture, implementation, fixer, review, and release agents are task-scoped specialist seats under exactly one core role. A producer and reviewer must be different agent instances.

## Preflight

- Confirm subagent tools are available before dispatch.
- Read [../flutter-app-orchestrator/references/subagent-map.md](../flutter-app-orchestrator/references/subagent-map.md) and [references/app-team-role-prompts.md](references/app-team-role-prompts.md). Classify the task, activate the smallest sufficient team, and record `N/A: <reason>` for omitted roles.
- Assign exactly one DRI and one independent acceptance owner. Record their role and agent IDs, consulted roles, read/write scopes, accepted upstream evidence, and execution mode in `.codex-workflow/progress.md`.
- Read [references/design-subagent-orchestration.md](references/design-subagent-orchestration.md) and preserve its controller-only authority and required role separation.
- Confirm `docs/plans/module-map.md` exists, the next task is in the first incomplete business-flow level, and all prior-level acceptance paths and cross-module contracts have passed or are explicitly accepted.
- When the next module first becomes eligible, stop before task refinement and run `grilling` again. Confirm its included functions, non-goals, page/state boundaries, dependencies, and acceptance path; require the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md` and a confirmed `docs/plans/modules/<module-name>-scope.md` before creating or dispatching its tasks.
- For a UI module, after function/page refinement and before any page design task, run the Module Effect-Image Interrogation Gate once and record it in the grilling log and module scope. Do not dispatch page-effect generation without it.
- After module refinement, confirm each task has an approved task brief derived from the confirmed module scope.
- Confirm expected write scopes do not overlap for any parallel implementation work.
- Read [references/collaboration-protocol.md](references/collaboration-protocol.md). Before dispatching any writable task, the Controller must create `.codex-workflow/tasks/<task-id>.yaml` from [references/task-state-template.yaml](references/task-state-template.yaml), record the integration base commit, dedicated `codex/<task-id>` branch/worktree, lease, and unique write scope, then run `scripts/validate-task-state.py`.
- Confirm `docs/design/app-design.pen` is the only project `.pen` file and reserve it for one writer at a time. Assign stable module/fidelity sections and node scopes before dispatching Page structure, Pencil restoration, or design-asset synchronization work.
- Confirm `.codex-workflow/progress.md` exists or create it from [references/progress-ledger.md](references/progress-ledger.md). Only the Controller may update the ledger or task-state files.
- If subagent tools are unavailable, run the same roles sequentially in the controller session and record the downgrade in the ledger. Mark every same-session review as non-independent; it cannot alone pass a high-risk Product, Design, Technical, Quality, or Release Gate.
- If a subagent times out, returns `NEEDS_CONTEXT`, or returns `BLOCKED`, update the ledger before retrying with clearer context, smaller scope, or a stronger model.

## Execution Loop

1. Read `.codex-workflow/progress.md` and task-state files; select the first eligible unleased task, transition it to `claimed`, validate the state, and create its dedicated branch/worktree before dispatch.
2. Read `docs/plans/module-map.md` and select the next eligible module from the first incomplete business-flow level. If this module has not completed its implementation-stage grilling gate, run it now and do not refine functions, pages, or task briefs until the user explicitly confirms shared understanding.
3. After confirmation, append the module decision to `docs/product/grilling-log.md`, create `docs/plans/modules/<module-name>-scope.md`, and refine the confirmed module into its function inventory, page functions, states, contracts, acceptance path, and vertical-slice tasks.
3.1. Classify each task with the task-routing table, record the Team Assignment, and create one role card per dispatched agent from `references/app-team-role-prompts.md`. Backend/data work may not be inferred or absorbed by the Flutter Engineer when its contract or owner is missing.
4. For a UI module, run the Module Effect-Image Interrogation Gate once. Confirm the visual outcome, effect-image page/state list, budgets, signatures, accepted implementation/asset cost, and scope consistency; record explicit shared understanding before any page effect generation.
5. For a UI page task, dispatch the Page structure agent to select the wireframe level and produce its semantic contract, then a separate Wireframe reviewer. Require Pencil evidence only for Full and write it into the assigned section of `docs/design/app-design.pen`. The controller validates their outputs before advancing.
6. Dispatch the Page high-fidelity agent to generate exactly three transient candidates, then a separate Effect Image Reviewer. The controller presents results, records the user's choice and change disposition, and alone persists and freezes the selected image.
7. Dispatch the Bitmap decomposition agent. If assets are required, dispatch the Asset planning agent to prepare the complete pre-slicing table; the controller presents it and waits for explicit confirmation. Only then dispatch the Asset production agent for confirmed rows.
8. When required, dispatch the Pencil restoration agent as the sole active Pencil writer, restore into its assigned section of `docs/design/app-design.pen`, and validate its restoration and Flutter handoff evidence.
9. Dispatch the routed engineer for the task scope: Flutter Engineer for client work, Backend/Data Engineer for API/schema/migration work, Tech Lead for assigned cross-cutting technical work, or DevOps/Release Engineer for build/pipeline/environment work. Use the matching core prompt plus one specialist prompt.
10. Require the implementer report at `docs/tasks/<task-id>/implementer-report.md` with changed files, tests run, output summary, and concerns.
11. Package an immutable review snapshot with commit or diff identifier, changed-file list, input-artifact versions or hashes, and test-evidence version; dispatch the independent acceptance owner and store its report at `docs/tasks/<task-id>/review.md`. Any later fix makes the prior review stale.
12. For UI tasks, include screenshots or golden evidence and dispatch the QA Engineer in the Visual QA specialist seat.
13. Dispatch a fixer for Critical and Important findings.
14. Re-review until approved.
15. Controller validates the task commit, merges it into the integration branch, records the commit SHA and evidence paths, and only then transitions the task state to `accepted`.
16. After all tasks and required high-fidelity restoration are complete, dispatch an independent QA Final reviewer against an immutable branch snapshot, obtain the Tech Lead integration verdict, and run the in-scope device, emulator, simulator, browser, or desktop runtime validation. Record platform evidence only at this final integration stage.
17. When release is in scope, dispatch the DevOps/Release Engineer after QA acceptance. Require reproducible artifacts, signing and environment checks, monitoring, rollout, and rollback evidence before the Controller requests or records release authorization.

Use [references/design-subagent-orchestration.md](references/design-subagent-orchestration.md), [references/subagent-prompts.md](references/subagent-prompts.md), [references/progress-ledger.md](references/progress-ledger.md), and [references/collaboration-protocol.md](references/collaboration-protocol.md).

## Parallelism Rule

Parallelize read-only exploration, independent reviews, and disjoint page or asset production after their shared freeze exists. Serialize producer/reviewer pairs, user-confirmation gates, delivery across business-flow levels, overlapping write scopes, and every write to `docs/design/app-design.pen`. Disjoint Pencil node scopes do not make shared-file writes parallel-safe. Within one level, parallelize only when task branches/worktrees are isolated, contracts are established, and `docs/plans/module-map.md` marks the work parallel-safe.

## Required Verification

- `fvm flutter analyze`
- relevant `fvm flutter test` targets
- screenshots or golden tests for UI work

After each business-flow level is merged into the integration branch, run `fvm flutter test integration_test` when relevant integration tests exist. Treat it as level regression evidence, not as a platform-verification claim. Run the full device, emulator, simulator, browser, and desktop matrix only after all module/page tasks have passed; task-level screenshots or goldens remain design evidence.

## Gate

Do not create or dispatch a task before the module-level grilling confirmation and module scope refinement exist. Do not dispatch without a validated task-state claim, recorded task profile, enabled-role reasons, one DRI, one independent acceptance owner, agent IDs, accepted upstream evidence, base commit, dedicated branch/worktree, and non-overlapping write scopes. When subagent tools are available, do not silently perform delegable design production in the controller session; dispatch the required specialized role. Do not create a second project `.pen` file or run multiple Pencil writers concurrently. Do not let a producer review itself, let a subagent request or infer user approval, or let an agent write outside its assigned scope. Do not generate a UI module's page effect images before its Module Effect-Image Interrogation Gate passes. Do not advance on a stale review snapshot, a same-session high-risk review, `DONE_WITH_CONCERNS` containing Critical or Important findings, or missing mandatory evidence. Do not mark a task accepted while its task commit, evidence manifest, required design-agent report, reviewer verdict, page design gate evidence, asset confirmation/evidence, command output, or Critical/Important resolution is missing.
