---
name: flutter-quality-review
description: Use when reviewing a Flutter app, feature branch, screen, implementation task, UI evidence, tests, architecture, security, privacy, monetization, or commercial delivery quality before accepting work.
---

# Flutter Quality Review

## Overview

Review like a release-blocking commercial app gate. Findings lead; summaries are secondary.

## Review Inputs

- Product scope and task brief.
- Project-local `flutter-dev` implementation constraints.
- Module map and implementation plan.
- High-fidelity mockup, global design-freeze constraints, and page design-freeze constraints when present.
- Asset reuse check, production decision, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, atlas, slicing manifest, asset inventory, and fidelity review when illustrations, bitmaps, logos, photos, textures, generated visual assets, or visual exports are present.
- Wireframe text spec, Pencil intake, high-fidelity Pencil restoration decision and reason, restoration evidence when required, and handoff when Pencil is present.
- Technical design or relevant architecture decisions.
- Diff or changed files.
- Test commands and outputs.
- Global `docs/architecture/verification-platforms.md`, its applicable evidence, and screenshots or golden evidence for UI changes.

## Rubric

Use [references/review-rubric.md](references/review-rubric.md). Always check:

- Spec compliance.
- Module dependency, cross-module contract, and page interaction order compliance.
- Module acceptance and integration smoke results when module boundaries, routes, cross-module contracts, or user flows change.
- User path completeness.
- UI state coverage.
- Page design gate order: low-fidelity Pencil structure, Wireframe Review, wireframe text spec, high-fidelity effect image, design-freeze, restoration decision, then required restoration evidence.
- Asset gate order: approved high-fidelity effect image, global and page design-freeze constraints, reuse check, production decision, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, asset atlas, slicing manifest, asset inventory, fidelity review, then Pencil high-fidelity restoration or Flutter implementation.
- Pencil high-fidelity restoration decision quality: required screens are not skipped, and Not required decisions have a reason.
- Mockup parity and recorded design deviations when a high-fidelity mockup exists.
- Asset source, reuse decision, generation prompt constraints, background handling, background transparentization, transparent post-processing, transparency or retained-background decision, license, slicing/export, Flutter path, fallback, and fidelity compliance.
- Bitmap source compliance: new bitmaps default to product-design or image generation evidence; Pencil exports are accepted only for approved production asset nodes with a recorded reason.
- Wireframe spec, Pencil restoration, and recorded deviation compliance when Pencil is used.
- Mobile and accessibility risks.
- State management and data flow.
- Fixed stack compliance: Riverpod, hooks, Freezed, fpdart, json generation, and ScreenUtil.
- Annotation generation compliance: Freezed/json annotations and `build_runner` output for generated models, states, failures, unions, and DTOs.
- Error handling and recoverability.
- Payment, privacy, account, analytics, and crash reporting when in scope.
- Test sufficiency.
- Verification platform compliance: use the global platform scope as the only source of truth; accept a platform only when its required evidence exists.
- Overengineering and unnecessary abstractions.

## Output Shape

Report in this order:

1. Findings by severity with file and line references where available.
2. Missing evidence.
3. Open questions.
4. Short summary.

Severity:

- Critical: blocks release or breaks core path.
- Important: must fix before accepting the task.
- Minor: should fix if cheap or track in ledger.

## Gate

If no issues are found, say so clearly and list residual risks or missing evidence. Do not approve if the task brief, global verification platform scope, applicable platform evidence, module map, init report, generated `flutter-dev` path, required wireframe text spec, required asset atlas evidence, required asset generation evidence or `N/A` reason, Pencil high-fidelity restoration decision and reason, required restoration evidence, required screenshots, or required tests are absent. Require module acceptance result and integration smoke result only when the task changes module boundaries, routes, cross-module contracts, or user flows; otherwise require `N/A: <reason>`.
