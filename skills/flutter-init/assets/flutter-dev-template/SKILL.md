---
name: flutter-dev
description: Use when implementing or extending the {{PROJECT_NAME}} Flutter app after initialization, especially when working inside existing DDD modules, adding a new bounded module, wiring routes or APIs, updating environments, or following the project's chosen package, command, and code-generation conventions.
---

# Flutter Dev

## Overview

Operate on the initialized {{PROJECT_NAME}} Flutter app using the project decisions captured during setup. This skill is project-specific and must inherit the base rules from `flutter-project-guardrails`.

## Invocation Parameters

- Support an optional `--force` flag.
- When `--force` is present, reconfigure plugin integrations that belong to the current task scope, then continue the remaining development tasks.
- When `--force` is absent and no required plugin setup exists yet, perform the first-time plugin configuration, then continue the remaining development tasks.
- When `--force` is absent and plugin setup already exists, preserve the existing plugin setup and continue the remaining development tasks without reconfiguration.

## Required Base Policy

- Apply `flutter-project-guardrails` first for mandatory package rules, DDD layering, annotation usage, and forbidden mixed stacks.
- Use this skill for project-specific details that do not belong in the global guardrails.

## Project Snapshot

- Project name: `{{PROJECT_NAME}}`
- Package id: `{{APP_ID}}`
- Platforms: `{{PLATFORMS}}`
- Environments: `{{ENVIRONMENTS}}`
- Primary modules: `{{PRIMARY_MODULES}}`
- Core integrations: `{{CORE_INTEGRATIONS}}`

## Workflow

1. Map the task to an existing bounded module or decide whether a new module is required.
2. Check whether the request includes `--force`. If yes, refresh plugin configuration for the task scope. If no but the required plugin setup is missing, run the first-time plugin configuration. Otherwise, keep the existing plugin setup and continue.
3. Re-check the module boundary, route ownership, data source ownership, and generation impact before editing files.
4. Follow the project command set and environment conventions defined in the references.
5. When adding new project-specific decisions, update the decision log instead of hiding them in implementation details.

## Hard Rules

- Do not bypass DDD layers defined for this project.
- Do not add packages outside the approved project bundle without recording the reason and impact.
- Do not hand-edit generated `.g.dart` or `.freezed.dart` files.
- Do not create cross-module dependencies without updating the module map and rationale.
- Do not overwrite an existing plugin setup unless `--force` is explicitly present.
- Do not skip first-time plugin configuration when the current task requires plugins that are still missing.
- Replace every `{{PLACEHOLDER}}` before shipping this generated skill with the project.

## Project Conventions

- Route strategy: `{{ROUTE_STRATEGY}}`
- Networking strategy: `{{NETWORK_STRATEGY}}`
- Storage strategy: `{{STORAGE_STRATEGY}}`
- Test commands: `{{TEST_COMMANDS}}`
- Build commands: `{{BUILD_COMMANDS}}`

## References

- Read `references/project-context.md` for the concrete project summary and environment details.
- Read `references/module-map.md` for the bounded contexts, ownership map, and extension rules.
- Read `references/decision-log.md` for project-specific architectural decisions and exceptions.
- Read `references/plugin-rules.md` when the request includes `--force` or touches plugin integrations.
