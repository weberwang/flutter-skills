# Downstream Linking Rules

The purpose of this skill is to stop downstream workflow branching. Downstream skills may consume this contract, but they may not reinterpret it.

## Universal Rules

- If `global-design-guidelines.md` is missing, downstream design-freeze work is `blocked`.
- If either theme freeze file is missing, downstream theme-dependent work is `blocked`.
- If required sections are missing, downstream work is `blocked`.
- If a theme leaf value is qualitative or unresolved, downstream work is `blocked`.
- Downstream skills may cite, map, or implement values; they may not rewrite them without an explicit design rollback.

## Skill-Specific Consumption

### `flutter-design-freeze-gate`

Must verify:

- all three artifacts exist
- metadata block exists in `global-design-guidelines.md`
- required sections exist in the correct order
- light and dark theme files contain concrete values
- the frozen guidance is detailed enough to preserve typography hierarchy, contrast intent, and CTA priority

If any condition fails, return `blocked` and route to `design-preview-to-global-guidelines`.

### Optional external design adapters

Any optional external design adapter must treat these as the upstream source of truth:

- `layout_and_page_structure_principles`
- `component_system_principles`
- `visual_system_rules`
- `design_prohibitions`
- `engineering_guardrails`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`

It may rebuild structure and assets, but it may not redesign global theme roles. These adapters are not default gates for Flutter implementation.

### `flutter-uiux-to-architecture`

Must preserve frozen role names and values when mapping into Flutter theme layers. It may explain the mapping, but it may not recalculate the global design system.
Must also respect the frozen `platform_identifier` instead of treating `platform_baseline` as enough to choose the target validation surface.

### `flutter-design-source-control`

Must add the three artifacts to the frozen source priority and route any change request that touches them back to this skill plus `flutter-design-freeze-gate`.

### `flutter-design-parity-reviewer`

Must compare implementation evidence against both the frozen theme files and the relevant guideline sections, not against memory or informal visual preference.
Must also respect `module_preview_policy` so module-stage generated images are only treated as approved evidence when the matching generated paths are explicitly recorded.

### `flutter-design-freeze-gate`

When frozen shared artifacts already exist, it must use them to judge whether typography hierarchy, contrast, CTA emphasis, and global component rules are being preserved instead of re-inventing the design direction.

### `flutter-workflow-orchestrator`

Must treat `module_preview_policy` as the frozen default for module-stage image evidence:

- no new module images during refinement or module freeze unless that evidence path is explicitly approved
- when new module images are approved, generated module image paths must be written back into `global-design-guidelines.md`
Must also require the frozen `platform_identifier` to stay explicit once the workflow is entering architecture or implementation preparation.
