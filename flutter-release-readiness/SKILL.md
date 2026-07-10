---
name: flutter-release-readiness
description: Use when preparing a Flutter app for App Store, Google Play, TestFlight, internal testing, production launch, privacy review, subscriptions, store metadata, release builds, or commercial release readiness.
---

# Flutter Release Readiness

## Overview

Check whether a Flutter app is ready for commercial release. Treat missing legal, account, payment, analytics, crash, and store evidence as release risks.

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
- Accessibility, localization, network failures, and offline behavior.
- Release build verification commands.
- The global verification platform scope and its required release evidence.

## Verification Commands

Select commands that match the app:

- `fvm flutter analyze`
- `fvm flutter test`
- `fvm flutter test integration_test`
- `fvm flutter build apk --release`
- `fvm flutter build appbundle --release`
- `fvm flutter build ios --release`

Do not claim a platform build passed unless the command was run and output was observed.
Use `docs/architecture/verification-platforms.md` as the sole source of truth for platform scope. Do not claim a platform is release-ready unless its required build, smoke, store, and privacy evidence exists. Mark unsupported platforms there as `N/A: <reason>`.

## Output

Produce:

- Ready / Not ready verdict.
- Blocking issues.
- Non-blocking risks.
- Evidence paths.
- Next release actions.

## Gate

Do not mark release ready while any store, privacy, account, payment, crash reporting, or release build blocker remains unresolved.
