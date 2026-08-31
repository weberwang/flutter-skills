---
name: flutter-project-init
description: Use when the user explicitly asks to initialize or standardize a Flutter project and its approved dependency profiles, or when flutter-app-orchestrator routes the accepted project-initialization stage.
---

# Flutter Project Init

## Overview

Initialize the smallest Flutter foundation required by the approved technical design. Dependencies are capability profiles, not a mandatory bundle.

## FVM Environment Rule

Use FVM as the only Flutter and Dart execution environment. Run commands through `fvm flutter` or `fvm dart`.

## Dependency Profiles

Read [references/dependency-profiles.md](references/dependency-profiles.md). Select only the profiles justified in `docs/architecture/technical-design.md`:

- Core: shared/async state, dependency injection, and optional hook-managed lifecycle.
- Data/API: API DTOs or persisted JSON and their generation tooling.
- Complex domain: generated immutable/union models or typed failure composition.
- UI token: optional named size-token mapping; never structural responsive layout.

Do not install Riverpod, hooks, Freezed, fpdart, JSON generators, or ScreenUtil merely because initialization runs. Record each enabled item, reason, rejected lighter option, and package risk.

## Process

1. Read product, UI, technical design, verification-platform scope, and existing project configuration.
2. Confirm the FVM SDK and run `fvm flutter create` only when project creation is required.
3. Preserve accepted existing structure and dependencies; do not rewrite unrelated configuration.
4. Install only dependencies from approved capability profiles and any separately approved package additions.
5. Set up the app shell, theme, routing, linting, test scaffolding, and code generation only when the selected profiles require them.
6. Generate the project-local `flutter-dev` skill with `node scripts/create_flutter_dev_skill.js`, then adapt its dependency sections to the actual selected profiles.
7. Write `docs/architecture/flutter-init.md` from [references/init-report-template.md](references/init-report-template.md).

## Verification

Run only applicable generation plus the project-native baseline:

```bash
fvm dart run build_runner build --delete-conflicting-outputs
fvm flutter analyze
fvm flutter test
```

After shared foundations are usable, run the representative startup, routing, and enabled-plugin smoke defined in `docs/architecture/verification-platforms.md`. This is early evidence, not full platform verification, and must not automatically start physical-device acceptance.

## Gate

Do not finish initialization until FVM commands work, selected dependencies match documented capability needs, the project-local skill reflects actual packages, baseline checks pass, and the representative foundation smoke is executed or explicitly blocked with evidence.
