---
name: flutter-subagent-delivery
description: Use when coordinating concurrent, multi-agent, high-risk, or release-sensitive implementation of an approved Flutter delivery plan with isolated worktrees, deterministic pre-review validation, independent acceptance, targeted re-review, and automatic integration cleanup.
---

# Flutter Subagent Delivery

## Overview

Use this skill only when the task needs multi-agent coordination, concurrent writes, high-risk isolation, or release-grade acceptance. Light and ordinary sequential tasks should use a simpler branch workflow from `flutter-app-orchestrator`.

## Preflight

1. Classify the task with [references/task-risk-tiers.md](references/task-risk-tiers.md). Stop using this skill if a light or standard sequential workflow is sufficient.
2. Resolve the actual integration branch and base commit before creating the task. Confirm FVM, dependencies, upstream contracts, write scope, and executable verification commands.
3. Assign one DRI and an independent acceptance owner. Add specialist roles only for material work; do not document omitted roles.
4. Create one task branch and one dedicated worktree from the verified base. Reuse them through implementation, fixes, and targeted re-review.
5. Create `.codex-workflow/tasks/<task-id>.yaml` from [references/task-state-template.yaml](references/task-state-template.yaml), set `risk_tier` to `high` or `release`, record the lease and write scope, then run `scripts/validate-task-state.py`.
6. Keep the active task-state file in the Controller integration worktree. Only the Controller updates task state and `.codex-workflow/progress.md`.
7. Serialize all writes to `docs/design/app-design.pen` and every other shared generated file.

## Execution Loop

### Build And Validate

1. Dispatch the routed implementer with a concise task brief, canonical inputs, exact write scope, non-goals, and verification commands.
2. Let the implementer iterate in the same worktree until static checks, relevant tests, audit commands, and known regression fixtures execute successfully.
3. Treat failures discovered during execution as construction feedback, not formal review findings. Do not create review snapshots or dispatch Product, QA, technical, or visual reviewers while deterministic checks are failing.
4. When checks pass, create one candidate commit and package its immutable diff, changed files, canonical inputs, and evidence links.

### Review

5. Dispatch only reviewers whose acceptance dimension is material. Product, QA, technical, and visual reviews may run in parallel against the same candidate snapshot.
6. Store durable conclusions in named sections of `docs/tasks/<task-id>/review.md`; do not create implementer reports, separate evidence manifests, or duplicate visual-QA files.
7. A reviewer must be independent only for the dimension it accepts. Do not require unrelated reviewers to repeat after a narrow change.
8. Apply the selective invalidation rules from [references/task-risk-tiers.md](references/task-risk-tiers.md):
   - Scope or acceptance changes invalidate Product and QA.
   - Command, test matrix, audit script, dependency rule, or implementation changes invalidate QA and any directly affected technical review.
   - Visual-only changes invalidate visual QA; include QA when behavior changed.
   - Formatting, links, or non-semantic wording normally require only deterministic checks.
9. Fix findings in the original task worktree, produce a new candidate commit, and re-dispatch only affected reviewers.

### UI Conditions

10. Use Page structure, effect-image, bitmap, asset, Pencil, and visual-QA specialists only when the page and risk tier require them.
11. Generate one global direction or page candidate when the visual target is clear. Generate two or three only for requested exploration or unresolved material design tradeoffs.
12. Require independent design review for high-value, high-risk, or exploratory designs; do not make external product-design tooling a dependency.

### Finalize

13. When all required review sections approve the same final candidate, set `acceptance.verdict: approved` and run `scripts/finalize-task.py` once from the clean integration worktree.
14. The finalizer merges the task branch and removes the task worktree and local branch. Use `--remote origin` only when deletion of the pushed temporary branch is authorized.
15. Link the final merge, accepted state, and `review.md` from the ledger. Do not create a new review cycle for cleanup-only metadata.

## Parallelism

Parallelize read-only exploration, deterministic environment discovery, and independent reviews of the same frozen candidate. Parallelize writable work only when scopes are disjoint and each writer has an isolated worktree. Serialize overlapping contracts, business-flow levels, user decisions, shared generated files, and final integration.

## Required Verification

- Run `fvm flutter analyze` when Flutter source is affected.
- Run the relevant `fvm flutter test` targets.
- Run task-specific audit scripts and known regression fixtures completely before review.
- Capture screenshots or goldens when UI acceptance needs visual evidence.
- Run level integration smoke after merge; reserve the full platform matrix for final integration or a task that explicitly owns it.

## Gate

Do not dispatch implementation from an unresolved base branch. Do not recreate the worktree between review rounds. Do not ask a reviewer to discover errors that deterministic execution can expose. Do not treat every changed commit as invalidating every review dimension. Do not finalize without a passing final candidate, required independent acceptance, resolved Critical/Important findings, and successful cleanup.
