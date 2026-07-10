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
- Confirm each task has an approved task brief.
- Confirm `docs/plans/module-map.md` exists and the next task follows module dependency order and page interaction order.
- Confirm expected write scopes do not overlap for any parallel implementation work.
- Confirm `.codex-workflow/progress.md` exists or create it from [references/progress-ledger.md](references/progress-ledger.md).
- If subagent tools are unavailable, run the same implementer, reviewer, visual QA, and fixer roles sequentially in the controller session and record the downgrade in the ledger.
- If a subagent times out, returns `NEEDS_CONTEXT`, or returns `BLOCKED`, update the ledger before retrying with clearer context, smaller scope, or a stronger model.

## Execution Loop

1. Read `.codex-workflow/progress.md`; resume at the first incomplete task.
2. Read `docs/plans/module-map.md` and create a task brief from the next module/page in dependency order.
3. For a UI page task, complete the page design gate first: create low-fidelity Pencil structure, run Wireframe Review, write `docs/design/wireframe-spec.md`, generate a page-level high-fidelity effect image, record approval, freeze global and page constraints, run `flutter-asset-atlas` when required visual assets exist, decide whether high-fidelity Pencil restoration is required, restore the page in Pencil when required, and write Flutter handoff constraints.
4. Dispatch one implementer for the task scope.
5. Require report with changed files, tests run, output summary, and concerns.
6. Package diff and dispatch reviewer.
7. For UI tasks, include screenshots or golden evidence and dispatch visual QA.
8. Dispatch a fixer for Critical and Important findings.
9. Re-review until approved.
10. Mark task complete in the ledger.
11. After all tasks, run final branch review.

Use [references/subagent-prompts.md](references/subagent-prompts.md) and [references/progress-ledger.md](references/progress-ledger.md).

## Parallelism Rule

Parallelize exploration and review. Serialize implementation unless write scopes are disjoint, module contracts are already established, and `docs/plans/module-map.md` explicitly marks the work as parallel-safe.

## Required Verification

- `fvm flutter analyze`
- relevant `fvm flutter test` targets
- `fvm flutter test integration_test` when integration tests exist and the task affects flows
- screenshots or golden tests for UI work

## Gate

Do not mark a task complete while any reviewer verdict is missing, any page design gate evidence is missing, any required asset atlas evidence is missing, any required command lacks output, or any Critical/Important issue is open.
