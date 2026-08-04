---
name: flutter-subagent-delivery
description: Use when an approved Flutter delivery plan requires two or more disjoint writable tasks to run concurrently, with one worktree per writer, concise task state, deterministic validation, risk-based independent acceptance, targeted re-review, and automatic local integration cleanup.
---

# Flutter Subagent Delivery

## Overview

Use this skill only for simultaneous writable branches. Single-writer tasks, including `high` and `release`, use the normal branch or PR path from `flutter-app-orchestrator` without task-state automation.

## Prepare

1. Classify each task with [references/task-risk-tiers.md](references/task-risk-tiers.md).
2. Confirm the integration branch, common base, executable verification commands, and disjoint write scopes before starting parallel work.
3. Assign one DRI and lease per writable scope. Serialize shared dependencies, routes, themes, generated files, shared state, and `docs/design/app-design.pen`.
4. Create one `codex/<task-id>` branch and one worktree per writer from the verified base.
5. Create `.codex-workflow/tasks/<task-id>.yaml` from [references/task-state-template.yaml](references/task-state-template.yaml), then run `scripts/validate-task-state.py`.
6. Keep task state uncommitted in the Controller workspace. Only the Controller updates state and `.codex-workflow/progress.md`.

## Execute And Review

1. Give each implementer a concise brief with canonical inputs, exact write scope, non-goals, and verification commands.
2. Run F0 in the same worktree until static checks, relevant tests, audit commands, and known regression fixtures pass; deterministic failures return directly to implementation.
3. Freeze one candidate commit, record it in task state, then run F1 change triage from [review-funnel.md](../flutter-quality-review/references/review-funnel.md).
4. F1 verifies the snapshot, scope, risk, acceptance trace, and evidence, then records only the F2 Product, QA, technical, visual, or Release lanes actually required.
5. Dispatch the triggered F2 lanes against the same candidate snapshot. Review independent read-only lanes in parallel when scopes are independent.
6. Run F3 only after every required lane has a valid verdict. Store F0 references, F1 routing, F2 lane conclusions, and F3 acceptance in named sections of `docs/tasks/<task-id>/review.md`; do not create duplicate reports.
7. Fix findings in the same worktree, rerun F0/F1, and re-review only lanes affected by the new candidate:
   - Scope or acceptance changes: Product and QA.
   - Commands, tests, audit rules, dependencies, or implementation: QA and affected technical review.
   - Visual-only changes: visual QA; include QA when behavior changed.
   - Formatting or links: deterministic checks only.

## Finalize

1. After F3 confirms that all required lanes approve the effective candidate, set `state: reviewing` and `acceptance.verdict: approved`.
2. Keep the Controller on the integration branch and run:

   ```text
   scripts/finalize-task.py <state> --repository <Controller 工作目录> --integration-branch <分支>
   ```

3. The finalizer confirms the worktree branch and candidate, checks the common base and `git diff --check`, merges once, removes the worktree and local branch, then deletes the runtime state file.
4. Record the merge and integration smoke in the ledger or `review.md`, then remove the completed ledger row. Handle pushes and remote branch deletion through the normal authorized Git workflow.

## Required Verification

- Run `fvm flutter analyze` when Flutter source is affected.
- Run relevant `fvm flutter test` targets and task-specific regression fixtures.
- Capture screenshots or goldens when UI acceptance needs visual evidence.
- Run business-flow integration smoke after merge; reserve the full platform matrix for final integration or release.

## Gate

Do not use this skill for sequential work, read-only parallel review, or risk tier alone. Do not start writers with overlapping scopes or an uncertain base. Do not recreate worktrees between review rounds. Do not bypass F1, dispatch untriggered F2 lanes by default, or finalize before F3 confirms deterministic validation, required independent acceptance, and resolution of Critical or Important findings.
