---
name: flutter-design-source-control
description: Use when a Flutter module has frozen UI/UX, Pencil, global design-guideline, or theme-freeze sources; when `.pen` and frozen guidance must stay the design source; when implementation requests visual or interaction changes; or when post-freeze design changes need routing.
---

# Flutter Design Source Control

## Overview

Protect the frozen design source during implementation. After a module is frozen, `.pen`, the paired UI/UX RD, and any `design-preview-to-global-guidelines` artifacts define the design; code may restore or adapt implementation details, but it may not redesign the product.

## Source Priority

Use this priority after freeze:

1. Frozen `.pen` file.
2. `global-design-guidelines.md`.
3. `light-theme-freeze.yaml` and `dark-theme-freeze.yaml`.
4. Paired UI/UX RD design freeze card.
5. Approved preview only when `.pen` is not available yet.
6. PRD only for business intent, never for visual overrides.

If sources conflict, stop and require a design-source decision before implementation continues.

## Change Classification

Classify every requested change:

| Type | Meaning | Action |
| --- | --- | --- |
| `restore_fidelity` | Code deviates from frozen design | Fix in code |
| `allowed_engineering_adaptation` | Change is listed as allowed by freeze or architecture | Implement with note |
| `implementation_constraint` | Flutter cannot reasonably reproduce the design | Return to design-source decision |
| `design_change` | User wants different layout, hierarchy, visual style, interaction, state scope, or frozen theme meaning | Return to `mobile-ui-design-coach` or `design-preview-to-global-guidelines`, then `flutter-design-freeze-gate` |
| `source_conflict` | UI/UX RD, `.pen`, theme freezes, and preview disagree | Block until one source is selected |

## Workflow

1. Identify module, workflow state, UI/UX RD path, `.pen` path, freeze record, and any frozen global-guideline artifacts.
2. Confirm whether the request is implementation fidelity work or a design change.
3. For fidelity work, keep implementation inside the frozen design source.
4. For allowed engineering adaptation, record why the adaptation is allowed and where it appears in the architecture or freeze card.
5. If the requested change touches `global-design-guidelines.md` or either theme freeze file, classify it as a design change unless the current contract explicitly allows it.
6. For design changes, route back to design and require a new freeze before code continues.
7. Return a concise decision record that the next agent can follow.

## Hard Rules

- Do not let code-stage convenience change design hierarchy.
- Do not accept "small visual tweak" as harmless after freeze; classify it first.
- Do not use screenshots of implemented code as the new design source.
- Do not override `.pen` with memory of an older preview.
- Do not let implementation locally rewrite frozen theme values or global guidance sections.
- Do not export or parse `.pen` directly; use Pencil MCP through downstream skills when design data is needed.

## Output Contract

Return:

- `design_source_decision`
- `source_artifacts`
- `change_classification`
- `allowed_actions`
- `forbidden_actions`
- `rollback_stage`
- `document_update_location`

## Pressure Scenarios

- User says "slightly adjust button spacing in code so it looks better": classify as `design_change` unless the freeze card allows it.
- Developer says "Flutter cannot reproduce this effect": classify as `implementation_constraint`, not silent redesign.
- User says "make dark mode a bit bluer in code": classify as `design_change` unless `dark-theme-freeze.yaml` already allows that variation.
- User provides a new screenshot after freeze: treat it as a change request, not source replacement.
