---
name: flutter-project-init
description: Use when creating, bootstrapping, re-initializing, or standardizing a Flutter app project with a fixed Riverpod, hooks, Freezed, fpdart, json serialization, and ScreenUtil implementation stack.
---

# Flutter Project Init

## Overview

Use this skill to initialize a Flutter app for the commercial delivery workflow. It installs the fixed plugin stack, writes project-level constraints, and generates a project-local `flutter-dev` skill for all later implementation work.

## Fixed Stack

The default stack is mandatory unless `docs/architecture/technical-design.md` explicitly rejects one item and records the approved alternative:

- `flutter_riverpod`
- `hooks_riverpod`
- `flutter_hooks`
- `freezed_annotation`
- `json_annotation`
- `fpdart`
- `flutter_screenutil`
- dev: `build_runner`
- dev: `freezed`
- dev: `json_serializable`
- dev: `riverpod_lint`
- dev: `custom_lint`

Use [references/fixed-plugin-stack.md](references/fixed-plugin-stack.md) for commands and package responsibilities.

## Annotation Generation Rule

Annotation-based code generation is mandatory. Use Freezed and JSON annotations plus `build_runner` for immutable models, unions, state objects, failures, DTOs, and JSON serialization. Do not handwrite code that Freezed or json_serializable can generate.

## Workflow

1. Confirm the target directory and whether this is a new or existing Flutter project.
2. Read `docs/architecture/technical-design.md`; if it is missing, create or request it before initialization.
3. Create the Flutter project if needed.
4. Add the fixed plugin stack.
5. Ensure `ScreenUtilInit`, `ProviderScope`, theme, routing shell, and code generation commands are planned.
6. Generate the project-local `flutter-dev` skill from [assets/flutter-dev/SKILL.md](assets/flutter-dev/SKILL.md).
7. Write `docs/architecture/flutter-init.md` using [references/init-report-template.md](references/init-report-template.md).
8. Run verification commands.

## Required Commands

For a new app:

```bash
flutter create <app_name>
```

Then in the app root:

```bash
flutter pub add flutter_riverpod hooks_riverpod flutter_hooks freezed_annotation json_annotation fpdart flutter_screenutil
flutter pub add --dev build_runner freezed json_serializable riverpod_lint custom_lint
dart run build_runner build --delete-conflicting-outputs
flutter analyze
flutter test
```

## Generated Skill

Generate `flutter-dev/SKILL.md` in the target app repo, or another project-local skills folder if the repo already has a skill layout. That generated skill constrains future Flutter implementation:

- Prefer existing plugins and project primitives.
- Use Riverpod and hooks consistently.
- Use Freezed for immutable models, unions, and state objects.
- Use `fpdart` for typed failures and functional result flows where domain errors matter.
- Use json annotations and generated serialization for API or persisted data.
- Use ScreenUtil through app-level initialization and design tokens.
- Minimize state changes and rebuild scope.

## Gate

Do not mark initialization complete until dependencies are installed, annotation-based generated code succeeds through `build_runner`, `docs/architecture/flutter-init.md` records the generated `flutter-dev` path, and `flutter analyze` plus relevant tests are reported.
