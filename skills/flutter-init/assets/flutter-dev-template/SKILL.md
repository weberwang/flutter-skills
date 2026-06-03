---
name: flutter-dev
description: Use when implementing or extending the {{PROJECT_NAME}} Flutter app after initialization, especially when working inside existing DDD features, adding a new bounded feature, wiring routes or APIs, or following the project's chosen package, layering, and code-generation conventions.
---

# Flutter Dev

## Overview

Operate on the initialized {{PROJECT_NAME}} Flutter app using the project decisions captured during setup. This skill is project-specific and must inherit the base rules from `flutter-project-guardrails`.

## Scope

- This skill only constrains code implementation work inside the initialized project.
- Do not use this skill to handle project initialization, plugin setup, plugin reconfiguration, or `--force` flows.
- Initialization and plugin handling stay in `flutter-init`.

## Required Base Policy

- Apply `flutter-project-guardrails` first for mandatory package rules, DDD layering, annotation usage, and forbidden mixed stacks.
- Use this skill for project-specific details that do not belong in the global guardrails.

## Project Snapshot

- Project name: `{{PROJECT_NAME}}`
- Package id: `{{APP_ID}}`
- Platforms: `{{PLATFORMS}}`
- Environments: `{{ENVIRONMENTS}}`
- Primary features: `{{PRIMARY_FEATURES}}`
- Core integrations: `{{CORE_INTEGRATIONS}}`

## Workflow

1. Map the task to an existing bounded feature or decide whether a new feature is required.
2. Re-check the feature boundary, route ownership, data source ownership, and generation impact before editing files.
3. If the touched provider, model, serializer, union state, or API contract can be expressed through the approved annotation toolchain, implement it with annotations first and remove equivalent hand-written boilerplate instead of keeping parallel styles.
4. If the project stack includes `flutter_hooks` or `hooks_riverpod`, inspect the touched widget and provider path first and implement every applicable lifecycle, ephemeral state, and composition concern with hooks instead of parallel non-hooks boilerplate.
5. Follow the project command set and environment conventions defined in the references.
6. When adding new project-specific decisions, update the decision log instead of hiding them in implementation details.

## Hard Rules

- Do not bypass DDD layers defined for this project.
- Do not add packages outside the approved project bundle without recording the reason and impact.
- Do not hand-edit generated `.g.dart` or `.freezed.dart` files.
- If `@riverpod`, `@freezed`, `@JsonSerializable`, or `@RestApi` can express the current contract, do not ship a hand-written equivalent implementation.
- Do not create cross-feature dependencies without updating the feature map and rationale.
- Do not take over initialization, plugin setup, or force-based reconfiguration responsibilities.
- If this project uses `flutter_hooks` or `hooks_riverpod`, do not write new applicable UI logic as `StatefulWidget` or manual lifecycle glue where hooks can express it directly.
- Replace every `{{PLACEHOLDER}}` before shipping this generated skill with the project.

## Project Conventions

- Route strategy: `{{ROUTE_STRATEGY}}`
- Networking strategy: `{{NETWORK_STRATEGY}}`
- Storage strategy: `{{STORAGE_STRATEGY}}`
- Test commands: `{{TEST_COMMANDS}}`
- Build commands: `{{BUILD_COMMANDS}}`

## References

- Read `references/project-context.md` for the concrete project summary and environment details.
- Read `references/feature-map.md` for the bounded contexts, ownership map, and extension rules.
- Read `references/decision-log.md` for project-specific architectural decisions and exceptions.
