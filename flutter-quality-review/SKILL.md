---
name: flutter-quality-review
description: Use when reviewing a Flutter app, feature branch, screen, implementation task, UI evidence, tests, architecture, security, privacy, monetization, or commercial delivery quality before accepting work.
---

# Flutter Quality Review

## Overview

Review against the task's declared risk and acceptance scope. Use release-blocking rigor for `high` and `release`; keep standard reviews focused on changed behavior and evidence.

## Review Inputs

- Product scope and task brief.
- Project-local `flutter-dev` implementation constraints.
- Module map and implementation plan.
- Page high-fidelity mockup frozen under `.codex-workflow/visuals/pages/<page-name>/`, plus its `design-decision.md` and global freeze.
- Page `asset-manifest.md` when illustrations, bitmaps, logos, photos, textures, generated assets or visual exports are present.
- `design-decision.md` Pencil decision, frame/node IDs, restoration evidence and handoff constraints when Pencil is present.
- Technical design or relevant architecture decisions.
- Diff or changed files.
- Test commands and outputs.
- Global `docs/architecture/verification-platforms.md`, final-integration platform evidence when reviewing final delivery, and screenshots or golden evidence for UI changes.
- Named Visual QA section when visual risk or acceptance requires independent visual review.

## Rubric

Use [references/review-rubric.md](references/review-rubric.md). Select checks that cover the changed behavior, declared risk, and acceptance criteria; do not expand a narrow review into a release audit. Applicable checks include:

- Spec compliance.
- Business-flow level, module dependency, cross-module contract, and page interaction order compliance.
- Module acceptance and integration smoke results when module boundaries, routes, cross-module contracts, or user flows change.
- User path completeness.
- First-value, safe-to-try, trust, and recovery conditions for user-facing adoption flows.
- UI state coverage.
- Page design gate order: low-fidelity structure, independent semantic review, high-fidelity image, frozen page decision, restoration decision, then required restoration evidence.
- Freeze-record integrity: the selected page image is stored under `.codex-workflow/visuals/pages/<page-name>/` before the page decision records its candidate ID, decoded dimensions, SHA-256 and confirmation time.
- Asset gate order: approved high-fidelity effect image, global/page freeze constraints, reuse and production decision, background handling, generation evidence when used, output path and fidelity verdict in one asset manifest, then Pencil restoration or Flutter implementation.
- Pencil high-fidelity restoration decision quality: required screens are not skipped, and Not required decisions have a reason.
- Data units are restored as editable text or representative placeholders and do not create bitmap-generation or extraction work.
- Material visual uncertainties record their affected units, available evidence, required decision, and blocking status; no affected unit is approved or handed off while unresolved.
- Mockup parity and recorded design deviations when a high-fidelity mockup exists.
- Visual aesthetics and intended premium feel: hierarchy, spacing, typography, color and contrast, component consistency, asset quality, and decoration that meets the active visual expression preset’s signature strength and page-type budget without harming task clarity. Compare the implementation screenshot with the approved mockup and page-design-decision constraints; record an explicit aesthetic verdict and actionable findings. Do not treat restraint as the default premium standard.
- Product-fit quality: visual character supports the intended audience and product promise; polish does not hide unclear value, unnecessary friction, or unresolved trust concerns.
- Independent visual-QA findings are resolved or explicitly accepted when visual risk requires that review.
- Asset source, reuse decision, generation prompt constraints, background handling, license, output/Flutter path, fallback and fidelity compliance from the page manifest.
- Bitmap source compliance: new bitmaps default to available image-generation evidence; Pencil exports are accepted only for approved production asset nodes with a recorded reason.
- Page design decision, Pencil restoration, and recorded deviation compliance when Pencil is used.
- Mobile and accessibility risks.
- State management and data flow.
- Fixed stack compliance: Riverpod, hooks, Freezed, fpdart, json generation, and ScreenUtil.
- Annotation generation compliance: Freezed/json annotations and `build_runner` output for generated models, states, failures, unions, and DTOs.
- Error handling and recoverability.
- Payment, privacy, account, analytics, and crash reporting when in scope.
- Test sufficiency.
- Verification platform compliance: use the global platform scope as the only source of truth; review runtime platform evidence only at final integration after all module/page functionality and high-fidelity restoration are complete.
- Overengineering and unnecessary abstractions.

## Output Shape

Report in this order:

1. Findings by severity with file and line references where available.
2. Aesthetic verdict for user-facing UI work: approved / approved with Minor findings / not approved, with the visual evidence and remaining actions.
3. Missing evidence.
4. Open questions.
5. Short summary.

Severity:

- Critical: blocks release or breaks core path.
- Important: must fix before accepting the task.
- Minor: should fix if cheap or track in ledger.

## Gate

Do not start formal review until required deterministic commands and regression fixtures pass against a candidate commit. Approve against the declared risk tier: light work needs no durable independent review; standard work needs only evidence relevant to changed behavior; high and release work require the declared independent sections and task-state evidence. After a fix, invalidate only review dimensions whose covered facts changed. Require level integration smoke only when a business-flow level closes and full runtime platform evidence only for final integration or release; do not write inapplicability records for unrelated checks.
