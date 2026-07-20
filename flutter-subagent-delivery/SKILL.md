---
name: flutter-subagent-delivery
description: Use when coordinating multi-agent design and implementation of an approved Flutter delivery plan, including UX, visual direction, wireframes, high-fidelity pages, bitmap decomposition, asset production, Pencil restoration, implementation, and independent review.
---

# Flutter Subagent Delivery

## Overview

Run design and implementation through controlled subagent loops. The controller owns sequencing, context packaging, user confirmations, freeze gates, conflict resolution, and final integration; specialized subagents perform production and review work.

## Roles

- Controller: owns plan, ledger, decisions, integration.
- Product/UX agent: drafts confirmed product, flow, state, and screen artifacts.
- Market agent: produces market and category analysis.
- Global direction agent and reviewer: produce and independently review three visual-system definitions.
- Page structure agent and Wireframe reviewer: prepare and independently review low-fidelity structure and text specs.
- Page high-fidelity agent and Effect Image Reviewer: generate and independently review page candidates without selecting or freezing them.
- Bitmap decomposition agent: performs ownership classification, visual sweep, and coverage audit.
- Asset planning agent: prepares reuse decisions and the pre-slicing confirmation table without producing assets.
- Asset production agent: produces only explicitly confirmed asset rows and writes slicing, inventory, and fidelity evidence.
- Pencil restoration agent: restores approved page visuals in Pencil and writes Flutter handoff constraints.
- Implementer: executes one task brief.
- Task reviewer: checks spec compliance and code quality.
- Visual QA reviewer: checks screenshots for UI tasks.
- Fixer: resolves review findings in the same task scope.
- Final reviewer: reviews the whole branch.

## Preflight

- Confirm subagent tools are available before dispatch.
- Read [references/design-subagent-orchestration.md](references/design-subagent-orchestration.md) and preserve its controller-only authority and required role separation.
- Confirm `docs/plans/module-map.md` exists, the next task is in the first incomplete business-flow level, and all prior-level acceptance paths and cross-module contracts have passed or are explicitly accepted.
- When the next module first becomes eligible, stop before task refinement and run `grilling` again. Confirm its included functions, non-goals, page/state boundaries, dependencies, and acceptance path; require the user's explicit shared-understanding confirmation in `docs/product/grilling-log.md` and a confirmed `docs/plans/modules/<module-name>-scope.md` before creating or dispatching its tasks.
- For a UI module, after function/page refinement and before any page design task, run the Module Effect-Image Interrogation Gate once and record it in the grilling log and module scope. Do not dispatch page-effect generation without it.
- After module refinement, confirm each task has an approved task brief derived from the confirmed module scope.
- Confirm expected write scopes do not overlap for any parallel implementation work.
- Confirm `.codex-workflow/progress.md` exists or create it from [references/progress-ledger.md](references/progress-ledger.md).
- If subagent tools are unavailable, run the same design, implementer, reviewer, visual QA, and fixer roles sequentially in the controller session and record the downgrade in the ledger.
- If a subagent times out, returns `NEEDS_CONTEXT`, or returns `BLOCKED`, update the ledger before retrying with clearer context, smaller scope, or a stronger model.

## Execution Loop

1. Read `.codex-workflow/progress.md`; resume at the first incomplete task.
2. Read `docs/plans/module-map.md` and select the next eligible module from the first incomplete business-flow level. If this module has not completed its implementation-stage grilling gate, run it now and do not refine functions, pages, or task briefs until the user explicitly confirms shared understanding.
3. After confirmation, append the module decision to `docs/product/grilling-log.md`, create `docs/plans/modules/<module-name>-scope.md`, and refine the confirmed module into its function inventory, page functions, states, contracts, acceptance path, and vertical-slice tasks.
4. For a UI module, run the Module Effect-Image Interrogation Gate once. Confirm the visual outcome, effect-image page/state list, budgets, signatures, accepted implementation/asset cost, and scope consistency; record explicit shared understanding before any page effect generation.
5. For a UI page task, dispatch the Page structure agent, then a separate Wireframe reviewer. The controller validates their outputs before advancing.
6. Dispatch the Page high-fidelity agent to generate exactly three transient candidates, then a separate Effect Image Reviewer. The controller presents results, records the user's choice and change disposition, and alone persists and freezes the selected image.
7. Dispatch the Bitmap decomposition agent. If assets are required, dispatch the Asset planning agent to prepare the complete pre-slicing table; the controller presents it and waits for explicit confirmation. Only then dispatch the Asset production agent for confirmed rows.
8. When required, dispatch the Pencil restoration agent and validate its restoration and Flutter handoff evidence.
9. Dispatch one implementer for the task scope.
10. Require report with changed files, tests run, output summary, and concerns.
11. Package diff and dispatch reviewer.
12. For UI tasks, include screenshots or golden evidence and dispatch Visual QA.
13. Dispatch a fixer for Critical and Important findings.
14. Re-review until approved.
15. Mark task complete in the ledger.
16. After all tasks and required high-fidelity restoration are complete, run final branch review and the in-scope device, emulator, simulator, browser, or desktop runtime validation. Record platform evidence only at this final integration stage.

Use [references/design-subagent-orchestration.md](references/design-subagent-orchestration.md), [references/subagent-prompts.md](references/subagent-prompts.md), and [references/progress-ledger.md](references/progress-ledger.md).

## Parallelism Rule

Parallelize read-only exploration, independent reviews, and disjoint page or asset production after their shared freeze exists. Serialize producer/reviewer pairs, user-confirmation gates, delivery across business-flow levels, and any overlapping write scopes. Within one level, parallelize only when contracts are established and `docs/plans/module-map.md` marks the work parallel-safe.

## Required Verification

- `fvm flutter analyze`
- relevant `fvm flutter test` targets
- `fvm flutter test integration_test` when integration tests exist and the task affects flows
- screenshots or golden tests for UI work

Run device, emulator, simulator, browser, and desktop runtime validation only after all module/page tasks have passed; task-level screenshots or goldens remain design evidence and do not verify a platform.

## Gate

Do not create or dispatch a task before the module-level grilling confirmation and module scope refinement exist. When subagent tools are available, do not silently perform delegable design production in the controller session; dispatch the required specialized role. Do not let a producer review itself, let a subagent request or infer user approval, or let an agent write outside its assigned scope. Do not generate a UI module's page effect images before its Module Effect-Image Interrogation Gate passes. Do not mark a task complete while any required design-agent report, reviewer verdict, page design gate evidence, asset confirmation/evidence, command output, or Critical/Important resolution is missing.
