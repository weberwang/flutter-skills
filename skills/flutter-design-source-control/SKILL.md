---
name: flutter-design-source-control
description: Use when a Flutter module has frozen UI/UX or Pencil sources, when `.pen` must be the single design source, when implementation requests visual or interaction changes, or when post-freeze design changes need routing.
---

# Flutter Design Source Control

## Overview

Protect the frozen design source during implementation. After a module is frozen, `.pen` and the paired UI/UX RD define the design; code may restore or adapt implementation details, but it may not redesign the product.

## Source Priority

Use this priority after freeze:

1. Frozen `.pen` file.
2. Paired UI/UX RD design freeze card.
3. Approved preview only when `.pen` is not available yet.
4. PRD only for business intent, never for visual overrides.

If sources conflict, stop and require a design-source decision before implementation continues.

## Change Classification

Classify every requested change:

| Type | Meaning | Action |
| --- | --- | --- |
| `restore_fidelity` | Code deviates from frozen design | Fix in code |
| `allowed_engineering_adaptation` | Change is listed as allowed by freeze or architecture | Implement with note |
| `implementation_constraint` | Flutter cannot reasonably reproduce the design | Return to design-source decision |
| `design_change` | User wants different layout, hierarchy, visual style, interaction, or state scope | Return to `mobile-ui-design-coach` and `flutter-design-freeze-gate` |
| `source_conflict` | UI/UX RD, `.pen`, and preview disagree | Block until one source is selected |

## Workflow

1. Identify module, workflow state, UI/UX RD path, `.pen` path, and freeze record.
2. Confirm whether the request is implementation fidelity work or a design change.
3. For fidelity work, keep implementation inside the frozen design source.
4. For allowed engineering adaptation, record why the adaptation is allowed and where it appears in the architecture or freeze card.
5. For design changes, route back to design and require a new freeze before code continues.
6. Return a concise decision record that the next agent can follow.

## Hard Rules

- Do not let code-stage convenience change design hierarchy.
- Do not accept "small visual tweak" as harmless after freeze; classify it first.
- Do not use screenshots of implemented code as the new design source.
- Do not override `.pen` with memory of an older preview.
- Do not export or parse `.pen` directly; use Pencil MCP through downstream skills when design data is needed.

## Output Contract

Return:

- `design_source_decision`
- `change_classification`
- `allowed_actions`
- `forbidden_actions`
- `rollback_stage`
- `document_update_location`

## Pressure Scenarios

- User says "slightly adjust button spacing in code so it looks better": classify as `design_change` unless the freeze card allows it.
- Developer says "Flutter cannot reproduce this effect": classify as `implementation_constraint`, not silent redesign.
- User provides a new screenshot after freeze: treat it as a change request, not source replacement.
