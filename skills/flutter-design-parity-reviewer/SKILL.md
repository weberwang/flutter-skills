---
name: flutter-design-parity-reviewer
description: Use when reviewing implemented Flutter screens, local app screenshots, widget structure, or visual behavior against frozen UI/UX RD, theme artifacts, visual evidence, and module design-source packet before accepting a module.
---

# Flutter Design Parity Reviewer

## Overview

Review implemented Flutter UI against the frozen design source. This skill finds fidelity gaps and implementation risks; it does not redesign the UI or choose new visual directions. The default workflow compares against frozen UI/UX and visual evidence, not Pen.

## Required Inputs

- Module name and workflow state.
- Frozen UI/UX RD path.
- Frozen module design-source packet and visual evidence.
- Frozen `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` when the module uses static-source freezing.
- Flutter implementation files or local running app.
- Screenshots for the same states whenever available.
- The architecture output for display-layer decisions whenever the module relied on `flutter-uiux-to-architecture` for high-fidelity display planning.
- Motion evidence, overlay evidence, scroll-state screenshots, or equivalent captures when those dimensions materially affect fidelity.
- Any allowed engineering adaptations from `flutter-design-source-control` or architecture planning.

## Review Dimensions

Review parity in four explicit dimensions instead of collapsing everything into one screenshot judgment:

- `structure`: route framing, region boundaries, hierarchy, primary-task path, sticky behavior, overlay placement, and content zoning
- `visual`: typography roles, spacing rhythm, size ratios, color semantics, radius, depth, texture, imagery, and asset usage
- `state`: ideal, loading, empty, error, disabled, permission, partial data, success, locked, premium, and other required states
- `motion`: transitions, reveal order, feedback timing, restraint, and whether motion changes structure or CTA salience

When a module has fidelity-critical regions, compare them region by region against the architecture display contract instead of only against a full-page screenshot.

## Review Workflow

1. Confirm the design source priority: frozen module design-source packet first, then `global-design-guidelines.md` plus theme freeze files when present, then UI/UX RD, and approved preview only as visual evidence.
2. Collect implementation evidence: code paths, screenshots, rendered states, navigation, and interactions.
3. Compare structure before detail: navigation, layout regions, content hierarchy, state zones, primary actions, sticky behavior, and overlay zoning.
4. Compare visual system: typography roles, spacing rhythm, color semantics, surface depth, radius, icons, imagery, texture, layer ordering, and any frozen light/dark theme values.
5. Compare states: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
6. Compare motion and transitions when they were part of the frozen display intent or materially affect hierarchy and CTA clarity.
7. For fidelity-critical regions, verify whether the implementation respected `preserve_faithfully`, `flutterize`, or `simplify` decisions and any locked spacing, asset, or layer-depth rules from architecture output.
8. Classify each gap and decide whether it is a code fix, allowed adaptation, source conflict, or design change request.
9. Route design changes to `flutter-design-source-control`; do not solve them inside implementation review.

## Severity

- `P0`: Violates frozen design source, breaks core path, misses required state, or changes interaction intent.
- `P1`: Noticeable parity gap in hierarchy, spacing, typography, color, asset use, or component behavior.
- `P2`: Polish gap that does not change intent but should be fixed before final acceptance.
- `Note`: Allowed engineering adaptation or verified non-issue.

## Hard Rules

- Do not compare implementation against an outdated preview when a newer frozen design-source packet exists.
- Do not suggest a better design; report mismatch against the frozen source.
- Do not pass a module that lacks required state screenshots or equivalent evidence.
- Do not pass a fidelity-critical module when the implementation evidence does not cover the same region or state coverage promised by the display evidence pack.
- Do not pass a module whose colors or theme-role usage contradict the frozen theme files even if the layout looks close.
- Do not treat snapshot similarity as enough when interaction or state behavior differs.
- Do not collapse structure, visual, state, and motion review into one aggregate opinion; review each dimension explicitly.
- Do not rewrite architecture here; route structural implementation issues to the relevant Flutter implementation skill.
- Do not require `.pen` or Pencil MCP data in the default parity workflow.

## Output Contract

Return:

- `review_decision`
- `design_source`
- `contract_artifacts_used`
- `implementation_evidence`
- `review_dimensions`
- `gap_list`
- `severity`
- `fix_owner`
- `needs_design_workflow_rollback`

## Pressure Scenarios

- Code looks polished but uses a different hierarchy: mark `P0` or `P1` based on impact.
- Implementation matches ideal state but lacks empty/error/loading: do not pass.
- Implementation is visually close but swaps frozen primary and accent roles: fail the review and route the fix to code or design-source control based on intent.
- User asks "update the design file to match the current code": route to `flutter-design-source-control`.
