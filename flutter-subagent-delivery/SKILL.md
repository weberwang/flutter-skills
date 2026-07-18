---
name: flutter-subagent-delivery
description: Use when coordinating multi-agent execution of an approved Flutter implementation plan.
---

# Flutter Subagent Delivery

## Overview

Run implementation through controlled subagent loops. The controller owns sequencing, context packaging, review gates, and final integration.

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
- Confirm `docs/plans/module-map.md` exists, the next task is in the first incomplete business-flow level, and all prior-level acceptance paths and cross-module contracts have passed or are explicitly accepted.
- When the next module first becomes eligible, stop before task refinement and run `grilling` again. Confirm its included functions, non-goals, page/state boundaries, dependencies, and acceptance path; require the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md` and a confirmed `docs/plans/modules/<module-name>-scope.md` before creating or dispatching its tasks.
- After module refinement, confirm each task has an approved task brief derived from the confirmed module scope.
- Confirm expected write scopes do not overlap for any parallel implementation work.
- Confirm `.codex-workflow/progress.md` exists or create it from [references/progress-ledger.md](references/progress-ledger.md).
- If subagent tools are unavailable, run the same implementer, reviewer, visual QA, and fixer roles sequentially in the controller session and record the downgrade in the ledger.
- If a subagent times out, returns `NEEDS_CONTEXT`, or returns `BLOCKED`, update the ledger before retrying with clearer context, smaller scope, or a stronger model.

## Execution Loop

1. Read `.codex-workflow/progress.md`; resume at the first incomplete task.
2. Read `docs/plans/module-map.md` and select the next eligible module from the first incomplete business-flow level. If this module has not completed its implementation-stage grilling gate, run it now and do not refine functions, pages, or task briefs until the user explicitly confirms shared understanding.
3. After confirmation, append the module decision to `docs/product/grilling-log.md`, create `docs/plans/modules/<module-name>-scope.md`, and refine the confirmed module into its function inventory, page functions, states, contracts, acceptance path, and vertical-slice tasks. Update the module map and implementation plan with the refinement result, then create the next task brief in dependency and page-interaction order.
4. For a UI page task, complete the page design gate first: create low-fidelity Pencil structure, run Wireframe Review, write `docs/design/wireframe-spec.md`, then generate and review a page-level high-fidelity effect image transiently. Do not write the candidate image, prompt, brief, review, freeze, or ledger visual entry until the user explicitly confirms the freeze. At freeze, persist the exact selected image first at `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`, then record its candidate ID, decoded dimensions, SHA-256, confirmation time, approval, and global/page constraints. Before visual-asset work or Pencil restoration, classify each restorable layer or atomic unit as bitmap, UI, or data; split composite elements before classification. Restore data only as editable text or representative placeholders while preserving hierarchy, text length, and layout; data must never trigger bitmap generation or extraction. Record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess the answer. For UI, record whether native Flutter can reproduce it exactly and generate a bitmap fill only when it cannot. Run `flutter-asset-atlas` only for identified bitmaps or bitmap fills; otherwise record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger. Decide whether high-fidelity Pencil restoration is required, restore the page in Pencil when required, and write Flutter handoff constraints.
5. Dispatch one implementer for the task scope.
6. Require report with changed files, tests run, output summary, and concerns.
7. Package diff and dispatch reviewer.
8. For UI tasks, include screenshots or golden evidence and dispatch visual QA.
9. Dispatch a fixer for Critical and Important findings.
10. Re-review until approved.
11. Mark task complete in the ledger.
12. After all tasks and required high-fidelity restoration are complete, run final branch review and the in-scope device, emulator, simulator, browser, or desktop runtime validation. Record platform evidence only at this final integration stage.

Use [references/subagent-prompts.md](references/subagent-prompts.md) and [references/progress-ledger.md](references/progress-ledger.md).

## Parallelism Rule

Parallelize exploration and review. Serialize delivery across business-flow levels. Within one level, parallelize implementation only when write scopes are disjoint, module contracts are already established, and `docs/plans/module-map.md` explicitly marks the work as parallel-safe.

## Required Verification

- `fvm flutter analyze`
- relevant `fvm flutter test` targets
- `fvm flutter test integration_test` when integration tests exist and the task affects flows
- screenshots or golden tests for UI work

Run device, emulator, simulator, browser, and desktop runtime validation only after all module/page tasks have passed; task-level screenshots or goldens remain design evidence and do not verify a platform.

## Gate

Do not create or dispatch a task before the module-level grilling confirmation and module scope refinement exist. Do not mark a task complete while any reviewer verdict is missing, any page design gate evidence is missing, any required asset atlas evidence is missing, any required command lacks output, or any Critical/Important issue is open.
