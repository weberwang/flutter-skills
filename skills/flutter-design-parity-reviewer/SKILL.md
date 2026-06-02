---
name: flutter-design-parity-reviewer
description: Use when reviewing implemented Flutter screens, local app screenshots, widget structure, or visual behavior against a frozen UI/UX RD and Pencil `.pen` design source before accepting a module.
---

# Flutter Design Parity Reviewer

## Overview

Review implemented Flutter UI against the frozen design source. This skill finds fidelity gaps and implementation risks; it does not redesign the UI or choose new visual directions.

## Required Inputs

- Module name and workflow state.
- Frozen UI/UX RD path.
- Frozen `.pen` file or Pencil MCP design data.
- Frozen `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` when the module uses static-source freezing.
- Flutter implementation files or local running app.
- Screenshots for the same states whenever available.
- Any allowed engineering adaptations from `flutter-design-source-control` or `flutter-pen-to-architecture`.

## Review Workflow

1. Confirm the design source priority: frozen `.pen` first, then `global-design-guidelines.md` plus theme freeze files when present, then UI/UX RD, and approved preview only if `.pen` is unavailable.
2. Collect implementation evidence: code paths, screenshots, rendered states, navigation, and interactions.
3. Compare structure before detail: navigation, layout regions, content hierarchy, state zones, and primary actions.
4. Compare visual system: typography roles, spacing rhythm, color semantics, surface depth, radius, icons, imagery, motion, and any frozen light/dark theme values.
5. Compare states: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
6. Classify each gap and decide whether it is a code fix, allowed adaptation, source conflict, or design change request.
7. Route design changes to `flutter-design-source-control`; do not solve them inside implementation review.

## Severity

- `P0`: Violates frozen design source, breaks core path, misses required state, or changes interaction intent.
- `P1`: Noticeable parity gap in hierarchy, spacing, typography, color, asset use, or component behavior.
- `P2`: Polish gap that does not change intent but should be fixed before final acceptance.
- `Note`: Allowed engineering adaptation or verified non-issue.

## Hard Rules

- Do not compare implementation against an outdated preview when `.pen` exists.
- Do not suggest a better design; report mismatch against the frozen source.
- Do not pass a module that lacks required state screenshots or equivalent evidence.
- Do not pass a module whose colors or theme-role usage contradict the frozen theme files even if the layout looks close.
- Do not treat snapshot similarity as enough when interaction or state behavior differs.
- Do not rewrite architecture here; route structural implementation issues to the relevant Flutter implementation skill.

## Output Contract

Return:

- `review_decision`
- `design_source`
- `contract_artifacts_used`
- `implementation_evidence`
- `gap_list`
- `severity`
- `fix_owner`
- `needs_design_workflow_rollback`

## Pressure Scenarios

- Code looks polished but uses a different hierarchy: mark `P0` or `P1` based on impact.
- Implementation matches ideal state but lacks empty/error/loading: do not pass.
- Implementation is visually close but swaps frozen primary and accent roles: fail the review and route the fix to code or design-source control based on intent.
- User asks "update the design file to match the current code": route to `flutter-design-source-control`.
