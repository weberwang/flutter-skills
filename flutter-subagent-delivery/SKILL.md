---
name: flutter-subagent-delivery
description: Use when coordinating multi-agent execution of an approved Flutter implementation plan.
---

# Flutter Subagent Delivery

## Overview

Run implementation through controlled subagent loops. The controller owns sequencing, task claims, integration, and the shared workflow state.

## Roles

- Controller: owns plan, ledger, decisions, integration.
- Page design agent: prepares low-fidelity structure, high-fidelity mockup evidence, and design-freeze constraints for UI tasks.
- Asset atlas agent: prepares required visual asset reuse check, production decision, generation evidence, slicing manifest, inventory, and fidelity review after mockup approval.
- Pencil restoration agent: restores approved page visuals in Pencil and writes Flutter handoff constraints.
- Implementer: executes one task brief.
- Task reviewer: checks spec compliance and code quality.
- Visual QA reviewer: checks screenshots for UI tasks.
- Fixer: resolves review findings in the same task scope.
- Final reviewer: reviews the whole branch.

## Preflight

- Confirm subagent tools are available before dispatch.
- Confirm each task has an approved task brief.
- Confirm `docs/plans/module-map.md` exists, the next task is in the first incomplete business-flow level, and all prior-level acceptance paths and cross-module contracts have passed or are explicitly accepted.
- Confirm expected write scopes do not overlap for any parallel implementation work.
- Read [references/collaboration-protocol.md](references/collaboration-protocol.md). Confirm the integration branch is clean, then record its base commit, task branch, worktree, and unique write scope in `.codex-workflow/tasks/<task-id>.yaml` from [references/task-state-template.yaml](references/task-state-template.yaml). Validate every state transition with `scripts/validate-task-state.py`.
- Confirm `.codex-workflow/progress.md` exists or create it from [references/progress-ledger.md](references/progress-ledger.md). Only the Controller may update the ledger or task-state files.
- If subagent tools are unavailable, run the same implementer, reviewer, visual QA, and fixer roles sequentially in the controller session and record the downgrade in the ledger.
- If a subagent times out, returns `NEEDS_CONTEXT`, or returns `BLOCKED`, update the ledger before retrying with clearer context, smaller scope, or a stronger model.

## Execution Loop

1. Read task-state files; select an unleased `planned` task in the first incomplete business-flow level, record `claimed`, and create its task branch and worktree before dispatch.
2. Create `docs/tasks/<task-id>/brief.md` from the first incomplete business-flow level. Name the base commit, branch, worktree, expected write scope, page-scoped artifacts, and prior-level evidence. Do not create a later-level brief before the current level's advancement gate passes.
3. For a UI page task, complete the page design gate in `docs/design/pages/<page-name>/`: create low-fidelity Pencil structure, run Wireframe Review, write the page-scoped wireframe spec, then generate and review a page-level high-fidelity effect image transiently. Do not write candidate images before the user explicitly confirms the freeze. At freeze, persist the exact selected image first at `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`, then record its candidate ID, decoded dimensions, SHA-256, confirmation time, approval, and constraints in the page directory and `docs/tasks/<task-id>/evidence/visual-decision.md`. Before visual-asset work or Pencil restoration, classify each restorable layer or atomic unit as bitmap, UI, or data; split composite elements before classification. Restore data only as editable text or representative placeholders while preserving hierarchy, text length, and layout; data must never trigger bitmap generation or extraction. Record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess the answer. For UI, record whether native Flutter can reproduce it exactly and generate a bitmap fill only when it cannot. Run `flutter-asset-atlas` only for identified bitmaps or bitmap fills; otherwise record `N/A: no bitmap or exported visual assets` in the task brief and task evidence manifest. Decide whether high-fidelity Pencil restoration is required, restore the page in Pencil when required, and write page-scoped Flutter handoff constraints.
4. Transition the task to `implementing` and dispatch one implementer in its assigned worktree.
5. Store the implementer report at `docs/tasks/<task-id>/implementer-report.md` with changed files, tests run, output summary, and concerns.
6. Transition to `reviewing`, package the task commit/diff, and store the reviewer report at `docs/tasks/<task-id>/review.md`.
7. For UI tasks, store screenshots or golden evidence and the visual-QA report at `docs/tasks/<task-id>/visual-qa.md`.
8. Dispatch a fixer for Critical and Important findings on the same task branch, then re-review until approved.
9. Controller verifies the task commit, merges it into the integration branch, runs the level integration smoke when the level closes, and then records `accepted`, commit SHA, and evidence paths in the task state and ledger.
10. After all tasks and required high-fidelity restoration are complete, run final integration review and the in-scope platform matrix. Record platform evidence only in this final stage.

Use [references/subagent-prompts.md](references/subagent-prompts.md), [references/progress-ledger.md](references/progress-ledger.md), and [references/collaboration-protocol.md](references/collaboration-protocol.md).

## Parallelism Rule

Parallelize exploration and review. Serialize delivery across business-flow levels. Within one level, parallelize implementation only when task branches/worktrees are isolated, write scopes are disjoint, module contracts are already established, and `docs/plans/module-map.md` explicitly marks the work as parallel-safe.

## Required Verification

- `fvm flutter analyze`
- relevant `fvm flutter test` targets
- screenshots or golden tests for UI work

After each business-flow level is merged into the integration branch, run `fvm flutter test integration_test` when relevant integration tests exist. Treat it as level regression evidence, not as a platform-verification claim. Run the full device, emulator, simulator, browser, and desktop matrix only after all module/page tasks have passed; task-level screenshots or goldens remain design evidence.

## Gate

Do not mark a task accepted while its task-state transition, branch commit, reviewer verdict, page design gate evidence, required asset atlas evidence, required command output, or evidence manifest is missing, or while any Critical/Important issue is open.
