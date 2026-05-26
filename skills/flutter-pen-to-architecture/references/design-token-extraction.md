# Design Token Extraction

## Goal

Collapse raw Pencil styling into a maintainable Flutter token system instead of mirroring every distinct visual value.

## Token Families

Always try to classify extracted styles into these groups:

- color tokens
- text tokens
- spacing tokens
- radius tokens
- elevation or surface-depth tokens
- border and divider tokens
- state tokens such as success, warning, error, disabled, selected

## Extraction Rules

### Color

- Group by semantic role first, not by exact hex value.
- Separate surface, content, accent, status, divider, and overlay colors.
- If near-identical colors are used in many places, merge them unless the contrast role is meaningfully different.

### Typography

- Extract text roles before font sizes: display, title, body, label, caption, numeric emphasis.
- Treat repeated weight-size-line-height clusters as candidate text styles.
- Avoid one-off text styles unless they clearly represent a special semantic role.

### Spacing

- Look for rhythm steps instead of raw margins.
- Convert irregular values into a compact spacing ladder when the design intent is obviously rhythmic.
- Keep a note when a screen intentionally breaks the rhythm for emphasis.

### Radius And Border

- Merge visually equivalent corner radii into a small set unless shape meaning changes by component category.
- Distinguish input, card, chip, sheet, and dialog edge treatment when they carry different interaction posture.

### Elevation And Surface Depth

- Treat shadow, blur, tint, and border combinations as a single depth system.
- Extract layers such as base surface, raised card, overlay panel, modal sheet, floating affordance.

## Flutter Mapping Guidance

Map tokens into Flutter responsibilities explicitly:

- `ColorScheme` for app-wide semantic colors
- `TextTheme` for stable text roles
- `ThemeData` for baseline component defaults
- `ThemeExtension` for product-specific tokens that do not fit Material semantics

## Normalization Rules

- Prefer fewer durable tokens over many brittle raw values.
- Keep a note when two values are visually different but operationally safe to merge.
- Call out places where merging would erase deliberate hierarchy or product branding.

## Output Expectations

For every token family, try to output:

- raw observed pattern
- normalized token proposal
- intended semantic role
- recommended Flutter home
- risk or uncertainty
