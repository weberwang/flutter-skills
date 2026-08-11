---
name: flutter-quality-review
description: Use a risk-based multi-level review funnel when reviewing a Flutter app, feature branch, screen, implementation task, UI evidence, tests, architecture, security, privacy, monetization, or commercial delivery quality before accepting work.
---

# Flutter Quality Review

## Overview

Review through a multi-level funnel: deterministic filtering, change triage, triggered specialist lanes, then convergence acceptance. Spend independent review effort only on candidates and dimensions that survive the earlier gates.

## Review Inputs

Select only the inputs required by F1 or the assigned F2 lane:

- Product scope and task brief.
- Project-local `flutter-dev` implementation constraints.
- Module map and implementation plan.
- Page high-fidelity mockup frozen under `.codex-workflow/visuals/pages/<page-name>/`, plus its `design-decision.md` and global freeze.
- Page implementation input `docs/design/pages/<page-name>/layout-spec.yaml`, the deterministic validator result, and parameterized relation-test evidence when layout-sensitive UI changed.
- Page `asset-manifest.md` when illustrations, bitmaps, logos, photos, textures, generated assets or visual exports are present.
- Code Sketch Level, independent Code Sketch Review, candidate/spec/screenshot hashes, and fidelity evidence when UI changed.
- Technical design or relevant architecture decisions.
- Diff or changed files.
- Test commands and outputs.
- Global `docs/architecture/verification-platforms.md`, final-integration platform evidence when reviewing final delivery, and screenshots or golden evidence for UI changes.
- Named Visual QA section when visual risk or acceptance requires independent visual review.

## Rubric

First use [references/review-funnel.md](references/review-funnel.md) to select the funnel depth and specialist lanes. Then use [references/review-rubric.md](references/review-rubric.md) only inside the triggered lanes. Do not expand a narrow review into a release audit. Applicable checks include:

- Spec compliance.
- Business-flow level, module dependency, cross-module contract, and page interaction order compliance.
- Module acceptance and integration smoke results when module boundaries, routes, cross-module contracts, or user flows change.
- User path completeness.
- First-value, safe-to-try, trust, and recovery conditions for user-facing adoption flows.
- UI state coverage.
- Page design gate order: semantic contract/level, sketch layout-spec, production Code Sketch/tests, independent review, high-fidelity generation/review/user freeze, contract back-check, assets or N/A, fidelity upgrade, measurements/parity, Visual QA.
- Freeze-record integrity: the selected page image is stored under `.codex-workflow/visuals/pages/<page-name>/` before the page decision records its candidate ID, decoded dimensions, SHA-256 and confirmation time.
- Asset gate order: approved frozen target, contract back-check, ownership/coverage audit and numbered user confirmation, production/background evidence and fidelity verdict in one authoritative asset manifest, then fidelity implementation.
- Data units are restored as editable text or representative placeholders and do not create bitmap-generation or extraction work.
- Material visual uncertainties record their affected units, available evidence, required decision, and blocking status; no affected unit is approved or handed off while unresolved.
- Mockup parity and recorded design deviations when a high-fidelity mockup exists.
- Independent critical-alignment gate: for every critical element verify reproducible target↔Flutter geometry relations, actual Widget measurement and same-viewport screenshot evidence against `adaptive-layout-implementation/references/critical-alignment-gate.md`. “No layout problems” is never proof of parity.
- Visual aesthetics and intended premium feel: hierarchy, spacing, typography, color and contrast, component consistency, asset quality, and decoration that meets the active visual expression preset’s signature strength and page-type budget without harming task clarity. Compare the implementation screenshot with the approved mockup and page-design-decision constraints; record an explicit aesthetic verdict and actionable findings. Do not treat restraint as the default premium standard.
- Product-fit quality: visual character supports the intended audience and product promise; polish does not hide unclear value, unnecessary friction, or unresolved trust concerns.
- Independent visual-QA findings are resolved or explicitly accepted when visual risk requires that review.
- Asset source, reuse decision, generation prompt constraints, background handling, license, output/Flutter path, fallback and fidelity compliance from the page manifest.
- Bitmap source compliance: new bitmaps default to approved generation/reuse evidence and never derive pixels from representative runtime data.
- Page design decision, semantic contract, Code Sketch Review, contract back-check and recorded deviation compliance.
- Mobile and accessibility risks.
- State management and data flow.
- Adopted dependency-profile compliance: review only packages and generation rules actually enabled by the technical design, including their recorded reasons.
- API/service conditions when applicable: contract/version, permissions/security, idempotency/retry, migrations/rollback, service tests, deployment/monitoring, backup/recovery, and client compatibility. If server implementation is out of scope, check only dependencies and boundaries.
- Error handling and recoverability.
- Payment, privacy, account, analytics, and crash reporting when in scope.
- Test sufficiency.
- Verification platform compliance: review representative foundation smoke early, primary-target runtime smoke after critical flows, and full platform coverage only at final integration/release.
- Overengineering and unnecessary abstractions.

## Output Shape

At F1, report the immutable snapshot, risk check, changed dimensions, required specialist lanes with reasons, missing entry evidence, and `return to implementation` / `route to specialist review` / `light self-check passed`.

At F2, remain read-only and report only the assigned lane in this order:

1. Assigned lane, candidate SHA, covered facts and evidence.
2. Findings by severity with file and line references where available.
3. Missing evidence.
4. Open questions.
5. Lane verdict: approved / changes_requested / blocked.

For the visual lane, also include the aesthetic verdict and a separate critical-alignment verdict: approved / changes_requested / blocked, with geometry measurements, screenshot evidence and remaining actions.

Only the Controller writes `docs/tasks/<task-id>/review.md`, including candidate history, evidence references, F2 returned conclusions and invalidations. At F3, report the effective snapshot, valid lane verdicts, closed blockers, integration or CI evidence required at this level, and the final verdict. Do not repeat detailed findings from F2.

Severity:

- Critical: blocks release or breaks core path.
- Important: must fix before accepting the task.
- Minor: should fix if cheap or track in ledger.

## Gate

Do not enter F1 until required project-native commands and regression fixtures actually pass against a candidate commit. F1 must reject stale evidence, scope drift, understated risk, and unidentified snapshots. F2 is read-only and may open only triggered lanes. F3 may approve only when every required lane covers the effective SHA and has no Critical, unresolved Important, or mandatory evidence gap. After a fix, rerun F0/F1 and invalidate only affected lanes. Markdown is never runtime state or an automatic merge signal. Apply layered platform evidence without turning early smoke into a full-platform claim or automatically starting physical-device acceptance.
