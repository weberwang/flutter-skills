# Global Guideline Contract

This skill freezes one main document named `global-design-guidelines.md`.

## Metadata Block

Place this block at the top of the document:

```yaml
artifact_type: global_design_guidelines
freeze_status: frozen | blocked
source_type: screenshot | preview_comp | multi_screen_pack | mixed
theme_freeze_files:
  light: light-theme-freeze.yaml
  dark: dark-theme-freeze.yaml
```

## Required Sections

Use these exact section ids and keep this exact order:

1. `design_position`
2. `product_personality`
3. `target_users_and_core_scenarios`
4. `global_experience_principles`
5. `information_hierarchy_principles`
6. `layout_and_page_structure_principles`
7. `component_system_principles`
8. `global_public_component_freeze`
9. `interaction_behavior_principles`
10. `state_and_feedback_principles`
11. `content_and_copy_principles`
12. `visual_system_rules`
13. `light_theme_rationale`
14. `dark_theme_rationale`
15. `design_prohibitions`
16. `engineering_guardrails`
17. `downstream_reference_index`

## Section Expectations

### `design_position`

State the product posture, category, and the experience promise the UI should communicate.

### `product_personality`

Describe tone, restraint, confidence level, density, and the memorable visual traits that should stay stable.

### `target_users_and_core_scenarios`

Describe who uses the product, under what pressure or context, and what the UI must optimize for.

### `global_experience_principles`

List global interaction principles that should remain true across screens.

### `information_hierarchy_principles`

Describe how information prominence, scanning order, focus management, typography hierarchy, and CTA dominance work globally.

### `layout_and_page_structure_principles`

Describe recurring page skeletons, regions, spacing logic, and when to use elevation or separation.

### `component_system_principles`

Describe component families, reuse expectations, and which variants are globally allowed.

### `global_public_component_freeze`

Record the frozen global public component set, including:

- which component families belong to the shared global system
- which states or variants are globally allowed
- which parts are immutable for downstream Pencil and Flutter work
- which engineering adjustments remain allowed without design rollback
- which components are explicitly not part of the global shared layer

### `interaction_behavior_principles`

Describe action emphasis, primary CTA posture, secondary-action restraint, gestures, toggles, navigation cues, and destructive-action behavior.

### `state_and_feedback_principles`

Describe how ideal, loading, empty, disabled, success, warning, and error states should feel and be expressed.

### `content_and_copy_principles`

Describe writing tone, label economy, helper text strategy, and alert/empty-state wording posture.

### `visual_system_rules`

Describe the global rules for typography ladder, reading contrast, CTA contrast posture, spacing, surface depth, icon posture, illustration posture, motion role, and decorative limits.

### `light_theme_rationale`

Explain why the frozen light theme values take their current semantic direction.

### `dark_theme_rationale`

Explain why the frozen dark theme values differ from light mode and how readability and depth are preserved.

### `design_prohibitions`

List what downstream skills may not reinterpret or override, especially typography hierarchy, CTA priority, and contrast intent.

### `engineering_guardrails`

List what implementation may simplify, what must stay faithful, and what requires design rollback, including any non-negotiable typography, contrast, and CTA decisions.

### `downstream_reference_index`

Map exact downstream skills to the sections and theme files they must cite.

## Missing Values

If any section cannot be fully resolved, keep the section and use one of:

- `not_provided`
- `not_applicable`
- `needs_confirmation`

No section may be removed, renamed, or merged.
