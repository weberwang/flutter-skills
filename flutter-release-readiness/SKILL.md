---
name: flutter-release-readiness
description: Use when preparing a Flutter app for App Store, Google Play, TestFlight, internal testing, production launch, privacy review, subscriptions, store metadata, release builds, or commercial release readiness.
---

# Flutter Release Readiness

## Overview

Act as the Release lane in the multi-level review funnel after F0 and F1 pass. Check whether the immutable Flutter release candidate is ready for commercial release. Treat missing legal, account, payment, analytics, crash, and store evidence as release risks.

This skill verifies launch evidence. Architecture choices for payments, analytics, crash reporting, signing, and environments belong in `flutter-tech-design`; release readiness checks whether those choices are implemented and documented.

## Required Checks

Use [references/release-checklist.md](references/release-checklist.md) and create `docs/release/release-checklist.md`.

Always cover:

- App identity, icons, splash, bundle IDs, versioning.
- Release signing and environment configuration.
- Privacy policy, terms, consent, account deletion.
- Payment, subscription, restore purchase, receipt validation when monetized.
- Crash reporting, analytics, logging, and support channels.
- Store screenshots, descriptions, keywords, categories, and test account.
- App Store Privacy Nutrition Labels.
- Google Play Data Safety form.
- Export compliance and encryption declaration.
- iOS entitlements, Android permissions, and manifest disclosures.
- Data collection disclosures consistent with runtime analytics, crash, ads, and payment SDK behavior.
- API/service contract version compatibility, auth/permission controls, idempotent retry behavior, migration rollback, service tests, deployment monitoring, backup restore and recovery evidence when applicable. If server implementation is externally owned, verify only the recorded dependency, owner, compatibility and release boundary.
- Accessibility, localization, network failures, and offline behavior.
- Release build verification commands.
- The global verification platform scope and its required release evidence.
- Earlier foundation startup/routing/plugin smoke and critical-flow primary-target smoke are present without being overstated; final device/emulator/simulator/browser/desktop matrix is complete for release scope.

## Verification Commands

Select commands that match the app:

- `fvm flutter analyze`
- `fvm flutter test`
- `fvm flutter test integration_test`
- `fvm flutter build apk --release`
- `fvm flutter build appbundle --release`
- `fvm flutter build ios --release`

Do not claim a platform build passed unless the command was run and output was observed.
Use `docs/architecture/verification-platforms.md` as the sole source of truth. Earlier smoke should already cover shared foundations and critical flows; release executes and records the complete in-scope matrix. Do not claim a platform release-ready unless required build, final runtime smoke, store, privacy and applicable service evidence exists. Never automatically start physical-device acceptance.

## Output

Produce:

- Release-lane verdict: approved / changes_requested / blocked.
- Blocking issues.
- Non-blocking risks.
- Evidence paths.
- Next release actions.

## Gate

Do not approve the Release lane while any store, privacy, account, payment, crash reporting, API/service rollout/recovery, or release build blocker remains unresolved. Release-lane approval does not itself complete F3: QA and technical verdicts, any triggered Product or visual verdict, PR/CI evidence, and explicit external-release authorization remain required.
