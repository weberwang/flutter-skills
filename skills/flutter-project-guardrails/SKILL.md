---
name: flutter-project-guardrails
description: Use when initializing or implementing a Flutter project that must follow mandatory package usage rules, DDD-by-feature architecture, and annotation-driven code generation, especially when choosing dependencies, adding a new feature, wiring state/network layers, or reviewing whether code structure violates project conventions.
---

# Flutter Project Guardrails

## Overview

Enforce a single Flutter engineering baseline for this workspace: mandatory package bundles, DDD modular boundaries, annotation-first generation, and taste-aligned presentation guardrails. Use this skill as the reusable base policy behind `flutter-init` and the generated project-local `flutter-dev` skill so initialization and ongoing implementation do not drift into mixed stacks, flat folders, hand-written boilerplate, or generic-looking display layers.

## Quick Start

- Use this skill together with `flutter-init` for every new Flutter project scaffold.
- After initialization, the day-to-day entry point should usually be the generated project-local `flutter-dev`; this skill remains the base policy layer behind it.
- When extending an existing project, read `references/mandatory-package-bundle.md` and `references/ddd-feature-blueprint.md` before editing features or dependencies.
- When a requirement seems to justify another package or another architecture style, prove why the current baseline fails first. Do not mix stacks by default.
- For presentation-layer work, keep taste guidance active as implementation guardrails: hierarchy, spacing, typography, contrast, CTA salience, motion restraint, and anti-template composition.
- If a requirement conflicts with these guardrails, state the conflict explicitly and keep one clear main plan plus one explicit fallback instead of silent compromise.

## Workflow

1. Identify which bounded context, layer, or engineering capability is being touched.
2. Apply the mandatory package baseline and any capability-triggered package bundle from the references.
3. Enforce the DDD feature blueprint so responsibilities stay inside `domain`, `application`, `infrastructure`, and `presentation`.
4. Enforce annotation coverage for providers, models, serialization, and API declarations.
5. For `presentation` work, compare the implementation against frozen UI/UX, theme artifacts, and taste guardrails before accepting layout or widget choices.
6. Reject overlap, hidden globals, manual boilerplate, unused dependencies, and display-layer choices that flatten frozen hierarchy or reintroduce AI-template patterns.
7. Output a short compliance checklist describing what follows the standard and what still violates it.

## Hard Rules

- Default architecture is DDD by bounded feature: `lib/features/<feature>/domain`, `application`, `infrastructure`, `presentation`.
- Default state and dependency organization is `flutter_riverpod` with `riverpod_annotation` and `riverpod_generator`.
- Default routing is `go_router`.
- Default HTTP stack is `dio` plus `retrofit`.
- Default model/state generation is `freezed_annotation` plus `json_annotation`, generated through `build_runner`.
- Sensitive data must use `flutter_secure_storage`; `shared_preferences` is only for non-sensitive lightweight preferences.
- Added packages must have a concrete owner and real usage in the scaffold or implementation. If they are not used, remove them.
- Providers, DTOs, unions, and API declarations must prefer annotations over hand-written boilerplate.
- Do not mix `provider`, `bloc`, `get_it`, `http`, `chopper`, manual JSON mapping, or duplicate storage stacks into the same responsibility path unless the skill itself is updated with a deliberate exception.
- If package version selection is time-sensitive, verify before pinning exact versions.
- Taste guidance may refine implementation craft, but it must not override frozen UI/UX intent, theme roles, state coverage, or approved component hierarchy.
- If a taste issue requires changing design meaning, route to `flutter-design-source-control` instead of silently changing code.

## Deliverables

- A clear package decision and usage plan.
- A compliant feature structure with explicit layer ownership.
- Annotation rules applied to providers, models, serialization, and API clients.
- Presentation-layer guardrails applied against frozen UI/UX and taste constraints.
- A reusable policy layer that can be referenced by the generated project-local `flutter-dev`.
- A short allowed / not allowed note for the current change so future edits stay aligned.

## References

- Read `references/mandatory-package-bundle.md` for baseline and capability-triggered package rules.
- Read `references/ddd-feature-blueprint.md` for the required project tree and layer responsibilities.
- Read `references/annotation-rules.md` for mandatory annotation usage, generator commands, and forbidden manual boilerplate.
