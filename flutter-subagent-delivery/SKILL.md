---
name: flutter-subagent-delivery
description: Use only when the user explicitly requests parallel writable Flutter tasks or worktrees; coordinate disjoint writers with normal branches, Markdown briefs, read-only review, and standard Git/PR/CI integration.
---

# Flutter Subagent Delivery

## Overview

Default Flutter delivery is single-writer and sequential. Use this skill only after the user explicitly authorizes parallel writers or worktrees. Read-only exploration and review may run in parallel without this skill.

Markdown records decisions, evidence, and conclusions only. It is never runtime state, automation input, a merge signal, or a state machine. Do not create YAML or JSON workflow state.

## Prepare

1. Classify each task with [references/task-risk-tiers.md](references/task-risk-tiers.md).
2. Confirm the integration branch, common base SHA, executable project-native verification commands, and non-overlapping write scopes.
3. Assign one DRI per writable scope. Serialize dependencies, routes, themes, generated files, shared state, migrations, API contracts, and each page layout-spec under one writer.
4. Use ordinary task branches. Create worktrees only when the user explicitly requested worktrees; record branch and scope in `docs/tasks/<task-id>/brief.md`.
5. The Controller coordinates through task briefs plus observed Git, PR, and CI facts. Do not create leases or structured status files.

## Execute And Review

1. Give each writer a Markdown brief with canonical inputs, exact write scope, non-goals, acceptance criteria, and executable verification commands.
2. At F0, run the project's native analysis, build, test, audit, migration, and regression commands in the task branch until they pass.
3. Freeze one candidate commit. At F1, the Controller checks its SHA, scope, risk, acceptance trace, and evidence, then selects only required F2 lanes.
4. F2 reviewers are read-only. Independent lanes may run in parallel and must return the structured conclusion defined by [review-funnel.md](../flutter-quality-review/references/review-funnel.md); they never edit shared `review.md`.
5. When durable review is required, only the Controller writes `docs/tasks/<task-id>/review.md`, binds each conclusion to its candidate SHA and evidence, and records invalidation after fixes.
6. After changes, rerun F0 and F1. Reopen only F2 lanes whose covered facts changed, then let the Controller perform F3 convergence.

## Integration

1. Use standard Git, PR, and CI; do not automatically merge branches or remove worktrees.
2. Before merge, the Controller verifies the current integration branch, approved candidate SHA, clean worktree, `git diff --check`, required tests and CI, required review conclusions, and explicit merge authority.
3. Resolve conflicts in the owning task branch and repeat affected verification/review. Markdown must not drive merge behavior.
4. After shared foundations, run representative startup, routing, and plugin smoke checks. After critical business flows, run the primary-target runtime smoke. Final integration or release owns the complete platform matrix.
5. Task-level evidence and early smoke checks must not claim full platform coverage. Never automatically start physical-device acceptance.

## Gate

Do not use this skill for sequential work, read-only parallel review, or risk tier alone. Do not start parallel writers without explicit user authorization, with overlapping scopes, or from an uncertain base. Do not create workflow YAML/JSON, let reviewers write shared `review.md`, automate merges from Markdown, or approve F3 before all required conclusions cover the effective candidate SHA.
