---
name: flutter-design-freeze-gate
description: Use when a Flutter module's UI/UX direction, state matrix, preview, design freeze card, global design-guidelines artifacts, approval status, or Pencil/code handoff must be checked before design work proceeds to Pencil or implementation.
---

# Flutter Design Freeze Gate

## Overview

Decide whether a module's UI/UX work is approved enough to move forward. This skill validates explicit design approval, state coverage, immutable constraints, and the presence of any required global freeze artifacts; it does not create the design or rebuild it in Pencil.

## Required Inputs

- Module name and current workflow state.
- Paired UI/UX RD path.
- Design packet from `mobile-ui-design-coach` and, when static previews are the frozen source, artifacts from `design-preview-to-global-guidelines`.
- Preview decision when previews were generated.
- State matrix and acceptance gates.
- Reference screenshots or preview images when the module claims `global_guidelines_frozen` from static visual sources.
- `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` when the module relies on approved screenshots or preview comps as a reusable source contract.
- Explicit user approval or a documented approval marker.

## Freeze Checklist

Approve only when all items are present:

- Business intent and target user.
- Platform baseline, normally iOS HIG for mobile behavior.
- Page scope and navigation entry.
- Core path and return loop.
- Art direction and hierarchy decisions.
- Visual system contract: typography, spacing, color roles, radius, surfaces, icon posture, motion role.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Global design freeze artifacts exist when the workflow depends on static visual sources:
  - `global-design-guidelines.md`
  - `light-theme-freeze.yaml`
  - `dark-theme-freeze.yaml`
- The guideline document keeps its required sections and the theme files contain concrete values instead of downstream TODOs.
- Immutable items that code and Pencil may not change.
- Engineering adjustments that are explicitly allowed.
- Acceptance criteria for Pencil and Flutter parity.
- Explicit approval from the user.

## Gate Decisions

Use these outcomes:

- `blocked`: required design evidence is missing.
- `needs_user_approval`: design evidence exists but approval is not explicit.
- `frozen_for_pen`: approved design can move to `design-preview-to-pen`.
- `frozen_for_code`: `.pen`, UI/UX RD, and implementation RD references are ready for code consumption.

## Hard Rules

- Do not infer approval from silence or enthusiasm.
- Do not allow Pencil work before the design direction is frozen.
- Do not allow Flutter implementation to reinterpret hierarchy, spacing, states, or visual tokens.
- Do not allow global design freeze to pass when reference screenshots or preview images are missing; block and send the workflow back to `mobile-ui-design-coach`.
- Do not let downstream skills infer missing theme values from static previews; require `design-preview-to-global-guidelines` to freeze them first.
- Do not decide visual alternatives here; route unresolved choices to `mobile-ui-design-coach` or `design-preview-to-global-guidelines` depending on whether the missing work is exploratory or contract-freezing.
- Do not treat a pretty preview as frozen unless it has an approval record.

## Output Contract

Return:

- `freeze_decision`
- `missing_items`
- `required_artifacts`
- `immutable_items`
- `allowed_engineering_adjustments`
- `next_skill`
- `approval_record`

## Pressure Scenarios

- User says "this direction is fine, continue": ask whether that is explicit approval if the target artifact is Pencil or code.
- User says "there is no reference image, freeze the global design first": block and route to `mobile-ui-design-coach`.
- User says "we can add states later": block production freeze.
- User says "Flutter can decide the dark theme later": block until `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` are frozen.
- User says "optimize visuals during implementation": block and route to `flutter-design-source-control`.
