---
name: flutter-app-orchestrator
description: Use when a user wants to build, redesign, commercialize, or ship a Flutter app with Codex, especially when the request spans product definition, UX/UI quality, architecture, implementation planning, risk-based task execution, review, or release readiness.
---

# Flutter App Orchestrator

## Overview

Coordinate Flutter delivery with the smallest process that protects the current risk. Keep one canonical source for each decision and route review through the multi-level funnel so failed or low-risk candidates do not consume unnecessary specialist review.

## Operating Model

1. Classify the request with [task-risk-tiers.md](../flutter-subagent-delivery/references/task-risk-tiers.md) before assembling roles or creating task infrastructure.
2. Use `light` for deterministic small work, `standard` for bounded feature work, `high` for risky work, and `release` for production delivery. Risk changes review depth, not the default execution topology.
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

1. Resolve the correct integration branch and base commit before drafting or reviewing a task. Discover reusable healthy processes, FVM, dependencies, existing contracts, and required commands during this preflight.
2. For a new project, complete technical design, Flutter initialization, module scope and task brief before page design or implementation. For an existing project, inspect and reuse these facts read-only unless the accepted task explicitly changes them.
3. `light`: work directly or on a short branch, run deterministic checks, and do not create worktrees, team assembly, or independent-review artifacts.
4. `standard`: use a normal task branch and concise task brief. After F0/F1, route behavior or acceptance changes through the independent QA lane and add other lanes only when triggered.
5. `high`: use a normal task branch, one DRI, durable `review.md`, and independent acceptance.
6. `release`: use a candidate branch, PR, CI, release evidence, and independent QA/technical gates.
7. Default to one writer and sequential handoff. Run independent read-only review in parallel when useful. Use `flutter-subagent-delivery` for parallel writers or worktrees only when the user explicitly requests that topology.
8. Escalate the tier when scope, irreversibility, shared ownership, security, data, payment, migration, visual fidelity, or release risk increases.

### Build, Validate, Review

1. Use the four-level funnel from [review-funnel.md](../flutter-quality-review/references/review-funnel.md): F0 deterministic filtering, F1 change triage, F2 triggered specialist lanes, and F3 convergence acceptance.
2. At F0, let the implementer run the project's native build, analysis, test, audit, and known-regression commands in the task branch until they pass. A planned command or synthetic status record is not execution evidence.
3. Freeze one candidate commit and evidence snapshot only after F0 passes. At F1, verify snapshot identity, scope, risk, acceptance traceability, and evidence; return failures immediately and record the minimum required F2 lanes.
4. At F2, dispatch only the triggered Product, QA, technical, visual, or Release lanes against that snapshot. Reviewers are read-only and return structured conclusions to the Controller; independent lanes may run in parallel.
5. At F3, converge the valid lane verdicts without repeating their detailed review. Approve only when every required lane covers the effective snapshot and all Critical, Important, and mandatory-evidence blockers are resolved.
6. When durable review is required, the Controller is the only writer of `docs/tasks/<task-id>/review.md`. It records the candidate SHA, F0 evidence references, F1 routing, copied F2 conclusions, invalidation history, and F3 outcome; it is not automation input.
7. After a fix, rerun F0 and F1. Bind review to the new candidate SHA and invalidate only lanes whose covered facts changed.

### Conditional UI Delivery

1. Let UX/UI Lead produce the semantic page contract and select Full, Lightweight, or Reuse. Create `phase: sketch` layout-spec, implement the Code Sketch on the production Flutter skeleton, and obtain independent Code Sketch Review before high-fidelity work.
2. Generate one page candidate when direction is clear. Generate two or three only when the user requests exploration, the direction is unresolved, or materially different design tradeoffs need comparison.
3. Require an independent effect-image review only for high-value, high-risk, or exploratory pages. The Controller records the user's selection and freezes the selected image.
4. After user freeze, compare the target with the reviewed semantic contract/sketch spec. Return to the semantic/sketch stage if scope, states, navigation, scrolling, breakpoints, accessibility, or ownership changed. Then run bitmap decomposition and asset planning/production only when required; the asset manifest is the sole authority for ownership, coverage, number mapping, and production facts.
5. Upgrade the same layout-spec to `phase: fidelity`, implement high fidelity by refactoring the same skeleton, and block absolute overlay patching over the old sketch.
6. Run fidelity validator, actual Widget relationship measurements, target/Flutter same-viewport screenshots, and independent Visual QA before F0/F1/F2/F3.

### Integration And Release

1. Integrate through standard Git, PR, and CI. Before merging, verify the current branch, approved candidate SHA, clean worktree, `git diff --check`, required tests/CI, required review verdicts, and merge authorization.
2. Never use Markdown to trigger a merge and never automatically merge or clean up parallel branches/worktrees.
3. After shared foundations, run representative startup, routing, and plugin smoke checks. After a critical business flow, run its primary-target runtime smoke. Run the complete platform matrix at final integration or release. Never turn task evidence into a full-platform claim or automatically start physical-device acceptance.
4. Use `flutter-release-readiness` only when release is in scope. Publishing, production mutation, signing, rollout, and remote branch deletion still require the applicable authorization.
5. After integration, list exactly one next eligible task.

## Artifacts

Use [references/artifacts.md](references/artifacts.md). Create only artifacts required by the current project stage and risk tier. Link canonical evidence rather than copying command output, review prose, page facts, or asset facts.

## Hard Gates

- Do not start from an uncertain integration branch or unverified base commit.
- Do not request formal review before required deterministic validation succeeds.
- Do not bypass F1 or dispatch every specialist by default; route only the lanes triggered by the candidate and risk tier.
- Do not let F3 replace a missing Product, QA, technical, visual, or Release verdict.
- Do not create a worktree unless the user explicitly requests parallel writing or worktree use. If authorized, keep write scopes disjoint and leave merging to the normal authorized Git/PR path.
- Do not invalidate unrelated reviews after a narrow fix.
- Do not force three design candidates when one direction is already clear.
- Do not require independent role separation for `light` work; require it for `high`, `release`, and materially risky `standard` work.
- Do not let a producer independently approve its own high-risk output.
- Do not run parallel writers without explicit user authorization, or against overlapping scopes and shared generated files.
- Do not infer user approval for product scope, visual freeze, destructive action, external release, or accepted risk.
- Do not generate, adapt, extract, export, transparentize, or slice a bitmap before the numbered overlay derived from the frozen page image has been shown by itself and explicitly confirmed.
- Do not claim full platform verification from task-level screenshots, goldens, builds, static analysis, or an early smoke check.
- Do not create standalone derivative reports when a canonical record already holds the decision or evidence.

## Routing

Use [references/subagent-map.md](references/subagent-map.md) only after the risk tier shows that multiple roles are useful. Use [app-team-role-prompts.md](../flutter-subagent-delivery/references/app-team-role-prompts.md) for core responsibility, [subagent-prompts.md](../flutter-subagent-delivery/references/subagent-prompts.md) for a necessary specialist seat, and [collaboration-protocol.md](../flutter-subagent-delivery/references/collaboration-protocol.md) only after the user explicitly requests parallel writers or worktrees.
