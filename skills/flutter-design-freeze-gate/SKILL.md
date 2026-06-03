---
name: flutter-design-freeze-gate
description: Use when shared Flutter design direction, shared/public component freeze, module-level page freeze, approval status, or Pencil/code handoff must be checked before work proceeds to module splitting, Pencil, or implementation.
---

# Flutter Design Freeze Gate

## Overview

Decide whether a Flutter design freeze request is approved enough to move forward.

This gate has two different responsibilities:

1. Before `modules_split`, it validates only the shared/public freeze needed to split modules safely.
2. During active module implementation preparation, it validates the active module's page-level and module-private component freeze before Pencil or code handoff.

It validates explicit design approval, state coverage, immutable constraints, and the presence of required freeze artifacts. It does not create the design or rebuild it in Pencil.

## Required Inputs

- Freeze target type:
  - `shared_pre_split`
  - `module_impl_prep`
- Module name when the target is module-specific.
- Current workflow state.
- Paired UI/UX RD path when the target is module-specific.
- Design packet from `mobile-ui-design-coach` and, when static previews are the frozen source, artifacts from `design-preview-to-global-guidelines`.
- `visual-design-reviewer` output whenever the target draft is visually complete enough to review, and that output must come from a fresh subagent run against the effect image, preview pack, static comp, or complete visual draft being frozen.
- Preview decision when previews were generated.
- State matrix and acceptance gates.
- Reference screenshots or preview images when the workflow claims `global_guidelines_frozen` from static visual sources.
- `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` when the workflow relies on approved screenshots or preview comps as a reusable source contract.
- Explicit user approval or a documented approval marker.

## Freeze Checklist

### Shared freeze before `modules_split`

Approve `shared_pre_split` only when all items are present:

- Business intent and target user.
- Platform baseline, normally iOS HIG for mobile behavior.
- Shared art direction, information hierarchy, and key-task guidance decisions.
- Visual system contract: typography hierarchy, contrast strategy, CTA posture, spacing, color roles, radius, surfaces, icon posture, motion role.
- A completed `visual-design-reviewer` record from a fresh subagent exists, it reviews the freeze-facing visual draft itself, its score is `>= 90`, and it does not report unresolved critical issues in information hierarchy, key-task guidance, typography hierarchy, contrast, or CTA clarity.
- Shared/public component freeze exists for reusable controls that should be stable before module splitting.
- Global design freeze artifacts exist when the workflow depends on static visual sources:
  - `global-design-guidelines.md`
  - `light-theme-freeze.yaml`
  - `dark-theme-freeze.yaml`
- The guideline document keeps its required sections and the theme files contain concrete values instead of downstream TODOs.
- Immutable items that later modules, Pencil, and code may not change without returning to design control.
- Explicit approval from the user.

Do not require page-level freeze or module-private component freeze at this stage.

### Module freeze during implementation preparation

Approve `module_impl_prep` only when all items are present:

- Active module name and paired UI/UX RD.
- Shared freeze inputs that the module depends on.
- Page scope and navigation entry for the active module.
- Core path and return loop.
- Page hierarchy, key-task guidance, and state details at implementation-final granularity.
- A completed `visual-design-reviewer` record from a fresh subagent exists, it reviews the freeze-facing visual draft itself, its score is `>= 90`, and it does not report unresolved critical issues in information hierarchy, key-task guidance, typography hierarchy, contrast, or CTA clarity.
- Module-private component freeze exists for repeated building blocks inside that module, including frozen states, variant boundaries, immutable parts, and allowed adjustments.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Immutable items that code and Pencil may not change.
- Engineering adjustments that are explicitly allowed.
- Acceptance criteria for Pencil and Flutter parity.
- Explicit approval from the user.

## Gate Decisions

Use these outcomes:

- `blocked`: required design evidence is missing.
- `needs_user_approval`: design evidence exists but approval is not explicit.
- `frozen_shared_for_split`: approved shared/public design can move to `flutter-rd-module-splitter`.
- `frozen_for_pen`: approved active-module page design can move to `design-preview-to-pen`.
- `frozen_for_code`: `.pen`, UI/UX RD, and implementation RD references are ready for code consumption.

## Hard Rules

- Do not infer approval from silence or enthusiasm.
- Do not let a visually complete draft skip `visual-design-reviewer` before freeze.
- Do not accept an inline parent-thread review as a valid `visual-design-reviewer` result.
- Do not let strong decorative polish mask unclear information hierarchy or weak task guidance.
- Do not allow a draft with `visual-design-reviewer` score below `90` to enter freeze.
- Do not treat “close enough” as a valid exception to the 90-point freeze threshold.
- Do not allow module splitting to treat shared freeze as page-level freeze.
- Do not allow Pencil work for an active module before that module's page-level design is frozen.
- Do not allow Flutter implementation to reinterpret hierarchy, spacing, states, or visual tokens.
- Do not treat premium decoration as compensation for weak typography hierarchy, low contrast, or a buried CTA.
- Do not allow module-private reusable components to enter Pencil or Flutter handoff without an explicit component-freeze decision for that active module.
- Do not allow global design freeze to pass when reference screenshots or preview images are missing; block and ask the user whether to fall back.
- Do not let downstream skills infer missing theme values from static previews; require `design-preview-to-global-guidelines` to freeze them first.
- Do not decide visual alternatives here; route unresolved choices to `mobile-ui-design-coach` or `design-preview-to-global-guidelines` depending on whether the missing work is exploratory or contract-freezing.
- Do not treat a pretty preview as frozen unless it has an approval record.

## Output Contract

Return:

- `freeze_decision`
- `missing_items`
- `required_artifacts`
- `review_requirement_status`
- `immutable_items`
- `allowed_engineering_adjustments`
- `next_skill`
- `approval_record`

## Pressure Scenarios

- User says "this direction is fine, continue": ask whether that is explicit approval if the target artifact is module splitting, Pencil, or code.
- User says "there is no reference image, freeze the global design first": block and ask whether to fall back.
- User says "shared styles are frozen, pages can be decided later": allow shared freeze only for module splitting, not for Pencil or code handoff.
- User says "the page is frozen, components can be decided later": block until module-private component freeze is explicit for that active module.
- User says "we can add states later": block production freeze.
- User says "Flutter can decide the dark theme later": block until `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` are frozen.
- User says "the draft looks premium enough, skip review": block and require `visual-design-reviewer`.
- User says "I already reviewed it in the main thread": block and require a fresh-subagent `visual-design-reviewer` run.
- User says "the score is 88, just freeze it and we will polish later": block and send the work back through the correct scope-matched regeneration loop before another review.
- User says "the module draft failed review, rerun module splitting": block unless the problem is actually global; default to updating the current module `ui/ux` doc and modifying the current module design draft in Pen.
- User says "users can figure out the flow after reading carefully": block if the key task still needs interpretation instead of guidance.
- User says "the CTA is subtle on purpose": block if the primary action is no longer clearly dominant.
- User says "optimize visuals during implementation": block and route to `flutter-design-source-control`.
