---
name: flutter-tech-design
description: Use when designing Flutter app architecture, state management, routing, storage, API boundaries, authentication, payments, analytics, crash reporting, environment configuration, testing strategy, or commercial app technical decisions.
---

# Flutter Tech Design

## Overview

Create a practical technical design for a commercial Flutter app. The design must support the MVP without speculative architecture.

This skill selects and documents integration strategy. It does not certify launch readiness; use `flutter-release-readiness` to verify production evidence before release.

## Process

1. Read product and UX artifacts before choosing architecture.
2. Identify app type: local-first, API-backed, subscription, content, community, commerce, AI, or enterprise.
3. Choose state, routing, persistence, networking, auth, payments, analytics, crash reporting, and environment strategy.
4. Define module boundaries, data flow, routing ownership, and cross-module contracts.
5. Define verification commands and test layers.
6. Write `docs/architecture/technical-design.md` with [references/technical-design-template.md](references/technical-design-template.md).

## Default Flutter Bias

- Prefer boring, well-supported packages.
- Use the `flutter-project-init` fixed stack as the default implementation foundation.
- Prefer Riverpod, hooks, Freezed, fpdart, json generation, and ScreenUtil before adding alternatives.
- Require annotations plus `build_runner` for Freezed and JSON generated code.
- Prefer feature modules with clear presentation, application, domain, and data boundaries only when the app complexity justifies them.
- Module boundaries must align with product flow, route ownership, data ownership, and implementation sequencing.
- Do not add offline sync, plugin abstraction, multi-backend support, or custom design engines unless the MVP requires them.
- Centralize app configuration and secrets handling. Never hardcode keys.

## Commercial Requirements

Explicitly address:

- Account lifecycle and deletion.
- Privacy-sensitive data.
- Subscription or purchase restoration if monetized.
- Crash reporting and analytics.
- Feature flags or remote config only when needed.
- CI, build flavors, and release signing assumptions.

## Gate

Do not move to implementation planning until the design states architecture decisions, rejected alternatives, module boundaries, data ownership, cross-module contracts, and verification commands.
