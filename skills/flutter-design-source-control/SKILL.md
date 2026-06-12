---
name: flutter-design-source-control
description: Use when a Flutter module has frozen UI/UX, global design-guideline, theme-freeze, visual-evidence, or design-source packet artifacts; when implementation requests visual or interaction changes; or when post-freeze design changes need routing.
---

# Flutter Design Source Control

## Overview

Protect the frozen design source during implementation. After a module is frozen, the paired UI/UX RD, module design-source packet, visual evidence, and any `design-preview-to-global-guidelines` artifacts define the design; code may restore or adapt implementation details, but it may not redesign the product.

## Source Priority

Use this priority after freeze:

1. Module design-source packet.
2. `global-design-guidelines.md`.
3. `light-theme-freeze.yaml` and `dark-theme-freeze.yaml`.
4. Paired UI/UX RD design freeze card.
5. Approved preview or screenshot pack as visual evidence.
6. PRD only for business intent, never for visual overrides.

If sources conflict, stop and require a design-source decision before implementation continues.

## Change Classification

Classify every requested change:

| Type | Meaning | Action |
| --- | --- | --- |
| `restore_fidelity` | Code deviates from frozen design | Fix in code |
| `allowed_engineering_adaptation` | Change is listed as allowed by freeze or architecture | Implement with note |
| `implementation_constraint` | Flutter cannot reasonably reproduce the design | Return to design-source decision |
| `design_change` | User wants different layout, hierarchy, visual style, interaction, state scope, or frozen theme meaning | Return to the image-backed design-source flow or `design-preview-to-global-guidelines`, then `flutter-design-freeze-gate` |
| `source_conflict` | UI/UX RD, design-source packet, theme freezes, and visual evidence disagree | Block until one source is selected |

## Workflow

1. Identify module, workflow state, UI/UX RD path, design-source packet, visual evidence, freeze record, and any frozen global-guideline artifacts.
2. Confirm whether the request is implementation fidelity work or a design change.
3. For fidelity work, keep implementation inside the frozen design source.
4. For allowed engineering adaptation, record why the adaptation is allowed and where it appears in the architecture or freeze card.
5. If the requested change touches `global-design-guidelines.md` or either theme freeze file, classify it as a design change unless the current contract explicitly allows it.
6. Treat `module_preview_policy` and `generated_module_preview_paths` inside `global-design-guidelines.md` as frozen source fields once shared artifacts are approved.
7. For design changes, route back to design and require a new freeze before code continues.
8. Return a concise decision record that the next agent can follow.

## Hard Rules

- Do not let code-stage convenience change design hierarchy.
- Do not accept "small visual tweak" as harmless after freeze; classify it first.
- Do not use screenshots of implemented code as the new design source.
- Do not override the frozen design-source packet with memory of an older preview.
- Do not let implementation locally rewrite frozen theme values or global guidance sections.
- Do not let implementation silently enable new module-stage image evidence generation after freeze; changes to `module_preview_policy` require design rollback.
- Do not require external design-draft files or tool-specific node data in the default design-source control workflow.

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
- User says "模块细化时默认也生图吧": classify as `design_change` unless the frozen `module_preview_policy` already allowed additional module-stage image evidence.
