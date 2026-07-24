---
name: flutter-app-orchestrator
description: Use when a user wants to build, redesign, commercialize, or ship a Flutter app with Codex, especially when the request spans product definition, UX/UI quality, architecture, implementation planning, risk-based task execution, review, or release readiness.
---

# Flutter App Orchestrator

## Overview

Coordinate Flutter delivery with the smallest process that protects the current risk. Keep one canonical source for each decision, complete deterministic validation before formal review, and escalate only when scope or risk requires it.

## Operating Model

1. Classify the request with [task-risk-tiers.md](../flutter-subagent-delivery/references/task-risk-tiers.md) before assembling roles or creating task infrastructure.
2. Use `light` for deterministic small work, `standard` for bounded feature work, `high` for risky or concurrent work, and `release` for production delivery.
3. Ask the user only for decisions that cannot be established from code, configuration, existing artifacts, or deterministic execution.
4. Use `grilling` only when material scope, priority, tradeoff, risk, acceptance, dependency, visual direction, or release authority remains unresolved. Do not repeat it merely because a new phase or module started.
5. Activate only roles that produce or independently accept material work. Do not record omitted ceremonial roles.

## Project Workflow

### Product And Global Design

1. For a new or materially changed product, confirm the product brief with `flutter-product-spec`; record only actual user decisions in `docs/product/grilling-log.md`.
2. Run market analysis only when current category evidence can change positioning, scope, trust, or commercial decisions. Condense decision-relevant sources into the product brief.
3. Define `docs/design/ui-spec.md` and the global design system with `flutter-ux-ui-quality` when UI scope exists.
4. If the user already supplied a brand, reference, or clear direction, prepare one global visual direction. Prepare two or three meaningfully different directions only when exploration is requested or material uncertainty remains. Review and freeze only the selected direction in `docs/design/global-design-freeze.md`.
5. Create technical design, Flutter initialization, platform scope, module map, and implementation plan only when the project stage requires them. Existing accepted artifacts remain valid until a material dependency or decision changes.

### Task Preparation

1. Resolve the correct integration branch and base commit before drafting or reviewing a task. Discover FVM, dependencies, existing contracts, and required commands during this preflight.
2. `light`: work directly or on a short branch, run deterministic checks, and do not create task state, worktree, team assembly, or independent-review artifacts.
3. `standard`: use a normal task branch and concise task brief. Add one independent review after validation when the change affects behavior or acceptance.
4. `high`: use a normal task branch, one DRI, durable `review.md`, and independent acceptance; do not create task-state automation solely for risk.
5. `release`: use a candidate branch, PR, CI, release evidence, and independent QA/technical gates.
6. When multiple writable branches must run simultaneously, use `flutter-subagent-delivery` with one worktree and short-lived task state per writer.
7. Escalate the tier when scope, irreversibility, shared ownership, security, data, payment, migration, visual fidelity, or release risk increases.

### Build, Validate, Review

1. Let the implementer iterate in the same branch or worktree until every deterministic command and known regression fixture passes. A task brief, audit script, test matrix, or implementation that has not executed successfully is not review-ready.
2. Freeze one candidate commit and evidence snapshot only after validation passes.
3. Dispatch the required Product, QA, technical, or visual reviewers against that same snapshot. Run independent reviews in parallel when their scopes do not depend on one another.
4. Store all task conclusions in `docs/tasks/<task-id>/review.md` when a durable review is required.
5. After a fix, invalidate only reviews whose covered facts changed. Scope changes invalidate Product and QA; command, test, audit, or implementation changes invalidate QA; visual-only changes invalidate visual QA; formatting-only changes normally require no new human review.
6. Keep the same task branch or worktree during repair and targeted re-review.

### Conditional UI Delivery

1. Use a semantic page contract before high-fidelity work. Require Pencil wireframes only for structurally complex or high-risk pages.
2. Generate one page candidate when direction is clear. Generate two or three only when the user requests exploration, the direction is unresolved, or materially different design tradeoffs need comparison.
3. Require an independent effect-image review only for high-value, high-risk, or exploratory pages. The Controller records the user's selection and freezes the selected image.
4. Run bitmap decomposition, asset planning/production, and Pencil restoration only when the selected design actually requires those outputs. Record their durable facts in the page design decision and asset manifest.
5. Use `flutter-quality-review` for screenshot or golden-based visual acceptance. External product-design tooling is optional and must never be a workflow dependency unless the user explicitly requests it.

### Integration And Release

1. Integrate sequential tasks through the normal branch or PR path without manufacturing task state.
2. Run `flutter-subagent-delivery/scripts/finalize-task.py` only for approved parallel worktree tasks; it merges the candidate and removes local task resources.
3. Run business-flow integration smoke after the relevant level merges. Run the complete platform matrix only for final integration or when the current task explicitly owns it.
4. Use `flutter-release-readiness` only when release is in scope. Publishing, production mutation, signing, rollout, and remote branch deletion still require the applicable authorization.
5. After integration, list exactly one next eligible task.

## Artifacts

Use [references/artifacts.md](references/artifacts.md). Create only artifacts required by the current project stage and risk tier. Link canonical evidence rather than copying command output, review prose, page facts, or asset facts.

## Hard Gates

- Do not start from an uncertain integration branch or unverified base commit.
- Do not request formal review before required deterministic validation succeeds.
- Do not create a worktree solely because a task is high risk or release-related. When concurrency requires one, reuse it until final acceptance or explicit abandonment.
- Do not invalidate unrelated reviews after a narrow fix.
- Do not force three design candidates when one direction is already clear.
- Do not require independent role separation for `light` work; require it for `high`, `release`, and materially risky `standard` work.
- Do not let a producer independently approve its own high-risk output.
- Do not run parallel writers against overlapping scopes or the shared `docs/design/app-design.pen` file.
- Do not infer user approval for product scope, visual freeze, destructive action, external release, or accepted risk.
- Do not claim platform verification from task-level screenshots, goldens, builds, or static analysis.
- Do not create standalone derivative reports when a canonical record already holds the decision or evidence.

## Routing

Use [references/subagent-map.md](references/subagent-map.md) only after the risk tier shows that multiple roles are useful. Use [app-team-role-prompts.md](../flutter-subagent-delivery/references/app-team-role-prompts.md) for core responsibility, [subagent-prompts.md](../flutter-subagent-delivery/references/subagent-prompts.md) for a necessary specialist seat, and [collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md) only when multiple writable branches run simultaneously.
