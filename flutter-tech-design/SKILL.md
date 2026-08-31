---
name: flutter-tech-design
description: Use when the user explicitly asks for Flutter architecture, dependency, API, migration, security, or platform technical decisions, or when flutter-app-orchestrator routes the accepted technical-design stage.
---

# Flutter Tech Design

## Overview

Create the smallest practical technical design that supports the approved product. This skill selects architecture and integration strategy; release evidence belongs to `flutter-release-readiness`.

## Process

1. Read product and UX artifacts before choosing architecture.
2. Identify the app and service shape: local-first, API-backed, subscription, content, community, commerce, AI, or enterprise.
3. Choose only required state, routing, persistence, networking, auth, payment, observability, environment, and dependency capabilities.
4. Define module/data ownership and cross-module contracts.
5. For APIs/services, define contract and versioning, authentication/authorization, idempotency/retry/timeout, migration/rollback, service tests, deployment/monitoring, backup/recovery, and client compatibility. If server implementation is out of scope, record only external dependencies, owners, assumptions, and client boundaries.
6. Define layered platform verification: foundation startup/routing/plugin smoke; primary-target runtime smoke after critical business flows; complete platform matrix at final integration/release. Never auto-start physical-device acceptance.
7. Define the shared breakpoint resolver, constrained page container, scroll-owner policy, docking/overlay primitives, and system-inset/keyboard infrastructure that page layout specs will consume. Do not reimplement these decisions independently in each page.
8. Write `docs/architecture/technical-design.md` with [references/technical-design-template.md](references/technical-design-template.md) and `docs/architecture/verification-platforms.md` with [references/verification-platforms-template.md](references/verification-platforms-template.md).

## Dependency Capability Bias

- Prefer SDK features, existing packages, and boring well-supported dependencies.
- Use [dependency-profiles.md](../flutter-project-init/references/dependency-profiles.md) to enable only needed core, data/API, complex-domain, and UI-token profiles.
- Record why each package/profile is enabled and which lighter option was rejected.
- Require annotations and generation only for actually adopted generated-model/serialization profiles.
- Do not add offline sync, plugin abstraction, multi-backend support, or a custom design engine unless the MVP requires it.
- Centralize configuration and secrets; never hardcode keys.

## Commercial Requirements

Explicitly address applicable account lifecycle, privacy-sensitive data, payment restoration, analytics/crash reporting, feature flags, CI, build flavors, release signing, service rollout, monitoring and recovery.

## Gate

Do not move to implementation planning until decisions, rejected alternatives, dependency profile reasons, module/data ownership, contracts, service boundaries, verification commands, layered platform scope, migrations/rollback, and production-risk ownership are explicit.
