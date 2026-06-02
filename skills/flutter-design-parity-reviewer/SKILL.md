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
- Flutter implementation files or local running app.
- Screenshots for the same states whenever available.
- Any allowed engineering adaptations from `flutter-design-source-control` or `flutter-pen-to-architecture`.

## Review Workflow

1. Confirm the design source priority: frozen `.pen` first, UI/UX RD second, approved preview only if `.pen` is unavailable.
2. Collect implementation evidence: code paths, screenshots, rendered states, navigation, and interactions.
3. Compare structure before detail: navigation, layout regions, content hierarchy, state zones, and primary actions.
4. Compare visual system: typography roles, spacing rhythm, color semantics, surface depth, radius, icons, imagery, and motion.
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
- Do not treat snapshot similarity as enough when interaction or state behavior differs.
- Do not rewrite architecture here; route structural implementation issues to the relevant Flutter implementation skill.

## Output Contract

Return:

- `review_decision`
- `design_source`
- `implementation_evidence`
- `gap_list`
- `severity`
- `fix_owner`
- `needs_design_workflow_rollback`

## Pressure Scenarios

- Code looks polished but uses a different hierarchy: mark `P0` or `P1` based on impact.
- Implementation matches ideal state but lacks empty/error/loading: do not pass.
- User asks "update the design file to match the current code": route to `flutter-design-source-control`.
