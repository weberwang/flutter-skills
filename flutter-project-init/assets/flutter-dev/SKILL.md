---
name: flutter-dev
description: Use when implementing, refactoring, reviewing, or debugging Flutter app code in this project, especially Riverpod providers, hooks widgets, Freezed models, fpdart results, JSON DTOs, ScreenUtil layouts, or state changes.
---

# Flutter Dev

## Overview

Use this project-local skill for Flutter implementation. Prefer the existing plugin stack, existing project primitives, and the smallest state surface that satisfies the task.

## FVM Environment Rule

Use `fvm flutter` and `fvm dart` for every Flutter or Dart command. Do not run bare `flutter` or `dart` commands.

## Fixed Stack

Use these packages before adding alternatives:

- `flutter_riverpod`
- `hooks_riverpod`
- `flutter_hooks`
- `freezed_annotation`
- `json_annotation`
- `fpdart`
- `flutter_screenutil`
- dev: `build_runner`, `freezed`, `json_serializable`, `riverpod_lint`, `custom_lint`

## Dependency Approval Rule

Do not add a new dependency until the task records:

1. Which existing package or project primitive was checked first.
2. Why the fixed stack cannot solve the requirement.
3. The approved artifact path in `docs/architecture/technical-design.md` or the task brief.
4. The package's runtime, size, maintenance, and platform risk.

## Implementation Rules

- Use `HookConsumerWidget` when a widget needs providers and hook-managed local lifecycle.
- Use `ConsumerWidget` when no hooks are needed.
- Use hooks for local ephemeral UI objects: controllers, focus nodes, tab controllers, animation controllers, and simple local UI toggles.
- Use Riverpod providers for app state, async state, dependencies, repositories, and use cases.
- Use Freezed for immutable state, data models, failures, and union states.
- Use `fpdart` for typed repository or domain failures where callers must handle both success and failure.
- Use `json_serializable` for API DTOs and persisted JSON models.
- Use ScreenUtil only through app initialization and shared sizing tokens.

## Mandatory Annotation Generation

Use annotations plus `build_runner` for all generated Dart code.

- Freezed annotations are required for immutable models, state objects, union states, failures, and value objects that need equality or copy semantics.
- JSON annotations are required for API DTOs and persisted JSON models.
- `part` files must be declared correctly.
- Run `fvm dart run build_runner build --delete-conflicting-outputs` after changing annotated files.
- Do not handwrite `copyWith`, equality, sealed union plumbing, `fromJson`, or `toJson` when Freezed or json_serializable can generate it.

## Minimum State Change Rule

Before creating or changing state, answer:

1. Is this local visual state? Use hooks.
2. Is this shared app or async state? Use Riverpod.
3. Is this derived from existing state? Use selectors, computed providers, or local variables.
4. Can this rebuild less? Use `select`, smaller providers, or smaller widgets.

Do not create a provider for a constant, one-off callback, static config, or purely local controller. Do not introduce state just to pass data down one or two widget levels.

## Riverpod Rules

- Keep providers small and named by responsibility.
- Prefer `AsyncValue` for loading, data, and error UI.
- Keep repository providers separate from UI state providers.
- Do not mutate collections in place inside provider state.
- Do not call network or storage APIs directly from widgets.

## Freezed and JSON Rules

- Add `part` files and run build generation after model changes.
- Keep DTOs separate from domain models when API shape leaks transport concerns.
- Hand-written `fromJson`, `toJson`, equality, `copyWith`, and union plumbing are forbidden unless generator support is impossible and the task brief records the exception.

## fpdart Rules

- Use `Either<Failure, T>` or `TaskEither<Failure, T>` at repository and use-case boundaries when failure is expected.
- Convert failures to `AsyncValue` or UI state at the presentation boundary.
- Do not throw for ordinary recoverable domain failures.

## ScreenUtil Rules

- Initialize once near the app root.
- Prefer design tokens over scattered `.w`, `.h`, `.sp` calls.
- Do not use ScreenUtil to hide poor responsive structure.

## Verification

Run after relevant changes:

```bash
fvm dart run build_runner build --delete-conflicting-outputs
fvm flutter analyze
fvm flutter test
```

For UI work, also capture screenshot or golden evidence required by the task.
