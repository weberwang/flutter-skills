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
- `ScreenUtil` only supplies root initialization and named shared size tokens; it is not the responsive layout engine. Do not use it to decide columns, navigation, scroll ownership, breakpoint structure, or global proportional scaling.

## Responsive Layout Rules

- Treat the page's layout/adaptation contract as the source of truth: record target logical-width ranges, structural breakpoints, content max width, columns/gutters, semantic anchors, docking, scroll ownership, system avoidance, keyboard behavior, and large-text/localization overflow policy before implementation.
- Prefer constraints over coordinates. Use the parent constraint (`LayoutBuilder`) for component-level structure decisions, `MediaQuery.sizeOf` for available viewport size, and `MediaQuery.paddingOf`/`viewPaddingOf`/`viewInsetsOf` for system and keyboard insets. Do not cache the startup size for a resizable, split-screen, or foldable view.
- Express relationships with the smallest behavior-fitting primitive: `Flexible`/`Expanded` for shared row or column space, `Wrap` for content that may form another line, `ConstrainedBox`/`Center` for min/max content width, `Align` for semantic alignment, and `Sliver`/scroll views for long content. A different widget is valid when its behavior is documented by the contract.
- Use `Stack`/`Positioned` only for true overlays or anchored layers. Give every fixed, pinned, or floating element an explicit SafeArea/keyboard inset, content-occlusion padding, hit target, and narrow-height fallback; keep the main page structure in flow.
- Give each scroll axis one owner. Add nested scrolling only when independent scroll semantics require it, and document controller, gesture competition, focus order, and `shrinkWrap` cost. Prefer slivers over a scroll view nested inside another scroll view solely to make layout fit.
- Keep text and primary actions free to wrap. Validate large text, long localized strings, RTL, loading/error states, keyboard focus, landscape, and the contracted breakpoint edges; never solve overflow by clipping, arbitrary truncation, or shrinking the whole page.
- Reuse one breakpoint resolver per feature/page instead of scattering width checks across child widgets. A breakpoint must describe a structural reason and a tested fallback, not just a device label.

Avoid `FittedBox` or a global scale transform for a full page, all-coordinate `.w`/`.h` placement, fixed heights around variable text, or absolute offsets that merely reproduce a mockup screenshot. The high-fidelity image freezes visual intent; constraints and the page contract determine production geometry.

## Verification

Run after relevant changes:

```bash
fvm dart run build_runner build --delete-conflicting-outputs
fvm flutter analyze
fvm flutter test
```

For UI work, also capture screenshot or golden evidence required by the task.
