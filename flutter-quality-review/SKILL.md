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
- Page `asset-manifest.md` when illustrations, bitmaps, logos, photos, textures, generated assets or visual exports are present.
- `design-decision.md` Pencil decision, frame/node IDs, restoration evidence and handoff constraints when Pencil is present.
- Technical design or relevant architecture decisions.
- Diff or changed files.
- Test commands and outputs.
- Global `docs/architecture/verification-platforms.md`, final-integration platform evidence when reviewing final delivery, and screenshots or golden evidence for UI changes.
- Named Visual QA section when visual risk or acceptance requires independent visual review.
- Responsive contract source: `flutter-ux-ui-quality/references/responsive-layout-strategy.md@1.1`, the page decision's region tree and layout implementation mapping, and the task brief's concrete viewport matrix.

## Rubric

First use [references/review-funnel.md](references/review-funnel.md) to select the funnel depth and specialist lanes. Then use [references/review-rubric.md](references/review-rubric.md) only inside the triggered lanes. Do not expand a narrow review into a release audit. Applicable checks include:

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
- New pages, page restoration, structural breakpoint changes, and any user-visible layout change are at least `standard`; F1 must trigger the visual lane for those changes.
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
- Responsive audit and contract-specific multi-viewport Widget/Golden evidence pass at F0. A single screenshot, absent contract, or version mismatch is not review-ready.

## Output Shape

At F1, report the immutable snapshot, risk check, changed dimensions, required specialist lanes with reasons, missing entry evidence, and `return to implementation` / `route to specialist review` / `light self-check passed`.

At F2, report only the assigned lane in this order:

1. Assigned lane and covered facts.
2. Findings by severity with file and line references where available.
3. Missing evidence.
4. Open questions.
5. Lane verdict: approved / changes_requested / blocked.

For the visual lane, also include the aesthetic verdict: approved / approved with Minor findings / not approved, with the visual evidence and remaining actions.

At F3, report the immutable snapshot, valid lane verdicts, closed blockers, integration or CI evidence required at this level, and the final verdict. Do not repeat detailed findings from F2.

Visual QA must read the page decision before judging evidence. Check both sides of each structural breakpoint, relative anchors and region mappings, accidental coordinate translation, maximum width/columns/gutters, scroll and docking ownership, SafeArea/system insets, keyboard behavior, and the contract's large-text/long-content matrix.

Severity:

- Critical: blocks release or breaks core path.
- Important: must fix before accepting the task.
- Minor: should fix if cheap or track in ledger.

## Gate

Do not enter F1 until required deterministic commands and regression fixtures pass against a candidate commit. F1 must reject stale evidence, scope drift, understated risk, and unidentified snapshots before specialist dispatch. F2 may open only the lanes triggered by the change and risk tier; independent acceptance is mandatory where the funnel requires it. F3 may approve only when every required lane covers the same effective snapshot and has no Critical, unresolved Important, or mandatory evidence gap. Task state is required only for simultaneous writable branches. After a fix, rerun F0 and F1, then invalidate only review lanes whose covered facts changed. Require level integration smoke only when a business-flow level closes and full runtime platform evidence only for final integration or release; do not write inapplicability records for unrelated checks.

## F0 响应式审计

UI 任务在 F0 运行标准库脚本，并把结果与任务简报中声明的 Widget/Golden 视口矩阵一起保存：

```bash
python <flutter-quality-review skill 目录>/scripts/audit-responsive_layout.py <Flutter 仓库> \
  --task-brief <task-brief.md> \
  --page-decision <design-decision.md> \
  --require-contract
```

UI 预检必须先解析实际安装的 `flutter-quality-review` skill 目录并把路径填入任务简报；不得假设 `.agents/skills`、个人目录或其他固定安装位置。脚本会扫描 `.dart` 源码中的整页缩放、主结构绝对坐标、比例坐标、固定高度包可变文本、缓存启动尺寸和散落断点，并可选校验契约必填章节。真实叠层只能使用带中文原因的窄范围 `响应式审计豁免` 注释；错误会阻塞 F0，警告必须记录。
