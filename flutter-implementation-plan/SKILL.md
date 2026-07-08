---
name: flutter-implementation-plan
description: Use when converting Flutter product, UX, UI, or architecture specs into milestones, implementation tasks, task briefs, acceptance criteria, test plans, or a build sequence for Codex.
---

# Flutter Implementation Plan

## Overview

Convert approved specs into small, verifiable Flutter implementation tasks. A good plan separates global design from module delivery, then orders modules by dependency and page interaction flow so Codex or subagents can execute without guessing scope.

## Inputs

- Product brief and MVP scope.
- Screen specs and UI quality gates.
- Technical design.
- Module boundaries, page flow, and cross-module contracts.
- Existing app structure, if this is not a greenfield app.

## Module Planning Rules

- Define modules by product responsibility, route ownership, data ownership, and page interactions, not just folder names.
- Keep modules independently deliverable where possible, but record every required cross-module contract.
- Order modules by shared foundations first, then primary user path, then dependent secondary paths.
- Within a module, order pages by user interaction sequence and state dependency.
- If two modules interact, identify the contract task before either module implements UI against that contract.
- Do not split a module so finely that one user action requires multiple agents to change the same files in parallel.

## Task Rules

- One task should produce one vertical slice or one isolated foundation.
- Each task must list scope, non-scope, files likely touched, acceptance criteria, and verification commands.
- UI tasks must include screenshot or golden evidence requirements.
- Risky shared foundations must happen before dependent feature tasks.
- Module entry tasks must establish routing, state boundary, contracts, and test scaffolding before page tasks.
- Do not plan parallel implementation tasks that write the same files.

## Output Files

- `docs/plans/module-map.md`
- `docs/plans/implementation-plan.md`
- `.codex-workflow/progress.md`

Use [references/module-map-template.md](references/module-map-template.md), [references/implementation-plan-template.md](references/implementation-plan-template.md), and [references/task-brief-template.md](references/task-brief-template.md).

## Default Milestones

1. Project foundation.
2. Design system and navigation shell.
3. Core data model and services.
4. Primary user path.
5. Account, settings, and privacy.
6. Monetization if in MVP.
7. Analytics, crash reporting, and release hardening.

## Gate

Do not execute a Flutter implementation task until it has an isolated task brief, named verification commands, `docs/plans/module-map.md`, `docs/architecture/flutter-init.md`, and a generated project-local `flutter-dev` path.
