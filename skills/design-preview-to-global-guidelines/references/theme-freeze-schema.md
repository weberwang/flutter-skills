# Theme Freeze Schema

This skill freezes two files:

- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`

Each file must be self-contained and must not rely on the other file for unresolved values.

## Required Top-Level Keys

```yaml
artifact_type: theme_freeze
theme_id: light | dark
platform_baseline: ios_hig | android_material | custom
color_roles: {}
surface_roles: {}
text_roles: {}
icon_roles: {}
border_roles: {}
status_roles: {}
shadow_or_overlay_roles: {}
component_state_roles: {}
contrast_rules: {}
forbidden_overrides: []
```

## Required Role Families

### `color_roles`

Include at least:

- `primary`
- `on_primary`
- `secondary`
- `on_secondary`
- `accent`

### `surface_roles`

Include at least:

- `background`
- `surface`
- `surface_subtle`
- `surface_elevated`
- `surface_inverse`

### `text_roles`

Include at least:

- `text_primary`
- `text_secondary`
- `text_tertiary`
- `text_inverse`

### `icon_roles`

Include at least:

- `icon_primary`
- `icon_secondary`
- `icon_inverse`

### `border_roles`

Include at least:

- `border_subtle`
- `border_strong`
- `divider`

### `status_roles`

Include at least:

- `success`
- `on_success`
- `warning`
- `on_warning`
- `error`
- `on_error`
- `info`
- `on_info`

### `shadow_or_overlay_roles`

Include at least:

- `shadow_color`
- `overlay_scrim`
- `focus_ring`

### `component_state_roles`

Include concrete values for at least these global component families:

- `primary_button`
- `secondary_button`
- `input_field`
- `card`

Add more only when the design system clearly requires them.

## Value Rules

- Use concrete values only: `#RRGGBB`, `rgba(...)`, numbers, or explicit comparison strings.
- Do not write token aliases like `primary/12`, `same_as_light`, or `auto`.
- Do not leave placeholders.
- Do not omit a role family because the input does not show every state.
- Use the main guideline document for rationale, not for unresolved values.

## Contrast Rules

Add explicit minimum rules such as:

- `body_text_on_background: ">= 4.5:1"`
- `body_text_on_surface: ">= 4.5:1"`
- `text_on_primary: ">= 4.5:1"`
- `essential_iconography: ">= 3:1"`

## Forbidden Overrides

Use this list to protect the frozen meaning of the theme. Examples:

- `Do not replace semantic primary with ad-hoc gradients.`
- `Do not darken surfaces until text contrast falls below the stated rules.`
- `Do not swap warning and accent roles inside local widgets.`
