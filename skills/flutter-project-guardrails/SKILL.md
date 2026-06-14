---
name: flutter-project-guardrails
description: Use when initializing or implementing a Flutter project that must follow mandatory package usage rules, DDD-by-feature architecture, and annotation-driven code generation, especially when choosing dependencies, adding a new feature, wiring state/network layers, or reviewing whether code structure violates project conventions.
---

# Flutter Project Guardrails

## Overview

Enforce a single Flutter engineering baseline for this workspace: mandatory package bundles, DDD modular boundaries, annotation-first generation, and frozen-design-aligned presentation guardrails. Use this skill as the reusable base policy behind `flutter-init` and the generated sibling `flutter-dev` skill so initialization and ongoing implementation do not drift into mixed stacks, flat folders, hand-written boilerplate, or generic-looking display layers.

## Quick Start

- Use this skill together with `flutter-init` for every new Flutter project scaffold.
- After initialization, the day-to-day entry point should usually be the generated sibling `flutter-dev`; this skill remains the base policy layer behind it.
- When extending an existing project, read `references/mandatory-package-bundle.md` and `references/ddd-feature-blueprint.md` before editing features or dependencies.
- When a requirement seems to justify another package or another architecture style, prove why the current baseline fails first. Do not mix stacks by default.
- If a provider, model, serializer, API declaration, or comparable scaffold can be expressed through the approved annotation toolchain, treat annotations as mandatory instead of optional and reject equivalent hand-written boilerplate.
- If the project has already introduced `flutter_hooks` or `hooks_riverpod`, treat hooks as a mandatory implementation style in every applicable widget or provider composition path instead of falling back to duplicated lifecycle or local-state boilerplate.
- For presentation-layer work, keep frozen design-quality guidance active as implementation guardrails: hierarchy, spacing, typography, contrast, CTA salience, motion restraint, and anti-template composition.
- If a requirement conflicts with these guardrails, state the conflict explicitly and keep one clear main plan plus one explicit fallback instead of silent compromise.

## Workflow

1. Identify which bounded context, layer, or engineering capability is being touched.
2. Apply the mandatory package baseline and any capability-triggered package bundle from the references.
3. Enforce the DDD feature blueprint so responsibilities stay inside `domain`, `application`, `infrastructure`, and `presentation`.
4. Enforce annotation coverage for providers, models, serialization, and API declarations, and replace any newly introduced hand-written boilerplate when the approved annotations can express the same contract.
5. If `flutter_hooks` or `hooks_riverpod` is present, audit whether the touched UI path should use hooks for controller lifecycle, effect orchestration, memoized derived values, or provider composition, and convert those spots instead of adding parallel `StatefulWidget` or manual listener code.
6. For `flutter_riverpod` reads in the presentation layer, keep the smallest watch scope possible so provider changes refresh only the widget subtree that actually depends on that state instead of rebuilding the whole page.
7. For `presentation` work, compare the implementation against frozen UI/UX, theme artifacts, and design-quality guardrails before accepting layout or widget choices.
8. Reject overlap, hidden globals, manual boilerplate, unused dependencies, and display-layer choices that flatten frozen hierarchy or reintroduce AI-template patterns.
9. Output a short compliance checklist describing what follows the standard and what still violates it.

## Hard Rules

- Default architecture is DDD by bounded feature: `lib/features/<feature>/domain`, `application`, `infrastructure`, `presentation`.
- Default state and dependency organization is `flutter_riverpod` with `riverpod_annotation` and `riverpod_generator`.
- Default screen adaptation baseline is `flutter_screenutil: ^5.9.3`.
- Default pagination baseline, when the product actually has paginated loading, is `infinite_scroll_pagination: ^5.1.1`.
- If the approved annotation toolchain can cover the current provider, DTO, union, serializer, or API contract, it must be implemented with annotations and generators instead of hand-written equivalents.
- If `flutter_hooks` or `hooks_riverpod` is part of the project stack, every applicable widget or provider composition path must use hooks first; do not keep `StatefulWidget`, manual `initState` / `dispose`, or duplicated listener glue where hooks can express the same behavior directly.
- In `flutter_riverpod`-driven UI, always keep the smallest watch scope possible; prefer local `Consumer`, `HookConsumerWidget`, `ConsumerWidget`, or provider-derived leaf widgets that refresh only the widget subtree that depends on the changed state instead of rebuilding the whole page.
- Default routing is `go_router`.
- Default HTTP stack is `dio` plus `retrofit`.
- Default model/state generation is `freezed_annotation` plus `json_annotation`, generated through `build_runner`.
- Sensitive data must use `flutter_secure_storage`; `shared_preferences` is only for non-sensitive lightweight preferences.
- Added packages must have a concrete owner and real usage in the scaffold or implementation. If they are not used, remove them.
- Providers, DTOs, unions, serializers, and API declarations must use annotations whenever the current standard toolchain supports that shape.
- Do not mix `provider`, `bloc`, `get_it`, `http`, `chopper`, manual JSON mapping, or duplicate storage stacks into the same responsibility path unless the skill itself is updated with a deliberate exception.
- Do not replace, omit, or version-drift `flutter_screenutil: ^5.9.3` in the default project baseline unless the guardrails themselves are explicitly revised first.
- Do not replace, omit, or version-drift `infinite_scroll_pagination: ^5.1.1` when the project has paginated loading requirements, unless the guardrails themselves are explicitly revised first.
- Do not keep or add self-built infinite-scroll pagination glue or another pagination package in a responsibility path that already uses the default pagination baseline.
- Do not keep or add hand-written provider wiring, DTO copy logic, JSON mapping, or API client glue in places where `@riverpod`, `@freezed`, `@JsonSerializable`, or `@RestApi` can express the same contract.
- Do not add `flutter_hooks` or `hooks_riverpod` and then continue writing new applicable code in a non-hooks style.
- If package version selection is time-sensitive, verify before pinning exact versions.
- Design-quality guidance may refine implementation craft, but it must not override frozen UI/UX intent, theme roles, state coverage, or approved component hierarchy.
- If a design-quality issue requires changing design meaning, route to `flutter-design-source-control` instead of silently changing code.

## Deliverables

- A clear package decision and usage plan.
- A compliant feature structure with explicit layer ownership.
- Annotation rules applied to providers, models, serialization, and API clients.
- Presentation-layer guardrails applied against frozen UI/UX and image-backed design constraints.
- A reusable policy layer that can be referenced by the generated sibling `flutter-dev`.
- A short allowed / not allowed note for the current change so future edits stay aligned.

## References

- Read `references/mandatory-package-bundle.md` for baseline and capability-triggered package rules.
- Read `references/ddd-feature-blueprint.md` for the required project tree and layer responsibilities.
- Read `references/annotation-rules.md` for mandatory annotation usage, generator commands, and forbidden manual boilerplate.
