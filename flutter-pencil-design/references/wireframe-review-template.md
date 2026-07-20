# Wireframe Review Template

Use this after the page semantic contract is written. Review meaning and behavior, not layout polish or geometry similarity.

## Inputs

- Wireframe level: Full / Lightweight / Reuse
- Level reason:
- Pencil evidence path or `N/A`:
- Canonical Pencil file: `docs/design/app-design.pen` / N/A
- Frame/node IDs in canonical file:
- Layout snapshot path:
- Frame dimensions verified as `390 x 844 px`: Yes / No / N/A
- Reused approved pattern and page-specific deltas:
- UI brief:
- High-fidelity mockup review:
- Flutter init report:

## Verdict

- Pass / Needs revision / Reject:
- Reason:

## Review Checks

- The wireframe maps to approved product scope.
- Full has complete `390 x 844 px` Pencil evidence; Lightweight and Reuse record a valid `N/A` reason when absent.
- All Pencil evidence belongs to `docs/design/app-design.pen`; no page- or module-specific `.pen` file was created.
- Main navigation is clear.
- Screen hierarchy is clear.
- Primary and secondary actions, outcomes, and recovery paths are defined without freezing exact placement.
- Required states are represented or explicitly listed.
- Empty, loading, error, disabled, permission, and success states are accounted for.
- Required content priority, accessibility meaning, and data/UI/fixed-asset ownership are explicit.
- The contract does not freeze exact coordinates, spacing, card/container count, component silhouette, image ratio/crop, secondary composition, or decoration placement.
- The contract leaves the high-fidelity agent free to recompose the page while preserving semantics.
- The wireframe can be implemented with the initialized Flutter stack and existing primitives.
- Ambiguities are listed instead of inferred.

## Findings

| Severity | Finding | Required text-spec change |
|---|---|---|

## Text Spec Requirements

- Screens to write:
- State specs to write:
- Navigation rules to write:
- Component roles to write:
- Non-goals to write:
