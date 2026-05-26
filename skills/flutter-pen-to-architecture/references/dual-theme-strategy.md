# Dual Theme Strategy

## Goal

Produce both light and dark themes as first-class systems while preserving readability, hierarchy, and product character.

## Base Principle

Dark theme is not the light theme with colors inverted. It is a separate semantic rendering of the same product language.

## Theme Layers To Plan

Always reason across these layers:

- app background
- primary surfaces
- secondary and tertiary surfaces
- content hierarchy
- accent and interactive color
- status colors
- overlays, sheets, dialogs, and scrims

## Shared Versus Split Tokens

### Shared When Possible

- spacing scale
- typography roles
- radius system
- most component anatomy
- semantic state naming

### Split When Necessary

- surface colors
- content contrast values
- border intensity
- overlay depth treatment
- shadow strategy
- muted and disabled appearance

## Readability Rules

- Preserve content hierarchy before preserving exact hue relationships.
- Prefer cleaner surface separation over heavy shadow when working in dark mode.
- Watch for accent overuse; colors that feel balanced in light mode can become visually dominant in dark mode.

## Inference Rules For Missing Dark Theme

When no dark-mode source exists:

- infer from semantic roles, not direct inversion
- prioritize legibility and hierarchy
- flag the result as inferred, not confirmed
- keep branded accents stable unless they destroy contrast

## Flutter Mapping

Recommend how the dual-theme system should land in Flutter:

- shared text roles in `TextTheme`
- shared semantic colors through paired light/dark `ColorScheme`
- product-specific surface or accent families in `ThemeExtension`

## Output Expectations

For each important token family, state:

- what is shared
- what splits by theme
- why the split exists
- where the split belongs in Flutter
