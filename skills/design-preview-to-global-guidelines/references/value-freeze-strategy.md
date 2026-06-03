# Value Freeze Strategy

Use this reference to turn visual evidence into concrete, stable theme values.

## Core Principle

Freeze semantic roles, not screenshot samples. The image is evidence for intent, hierarchy, and temperature; the final values should be normalized for readability, reuse, and downstream implementation.

## Light Theme Strategy

1. Lock the primary action color family.
2. Lock the CTA contrast relationship so the primary action is obvious without shouting.
3. Normalize background and surface separation so cards, panels, and overlays have predictable depth.
4. Establish text hierarchy with readability first and brand temperature second.
5. Normalize border strength so separators and field outlines are consistent.
6. Freeze status roles as semantic values, not decorative accents.

## Dark Theme Strategy

1. Start from semantic parity with light mode, not visual inversion.
2. Preserve hierarchy by controlling contrast bands across background, surface, elevated surface, and CTA surfaces.
3. Shift brightness, saturation, and overlay strength independently; do not mirror light mode ratios mechanically.
4. Keep primary action recognizability while protecting text readability and glare restraint.
5. Rebuild state colors so alerts remain legible without becoming neon noise.

## Missing-State Handling

If the source does not show all states:

- infer disabled treatment from the visual system's restraint level
- infer focus treatment from the product's interaction precision
- infer success, warning, and error treatments from existing accent and alert behavior
- infer CTA emphasis from the approved action hierarchy and visible button contrast
- record rationale in `light_theme_rationale`, `dark_theme_rationale`, or `engineering_guardrails`

Do not push unresolved state values to downstream skills.

## Normalization Rules

- Prefer 6-digit hex for opaque colors.
- Prefer `rgba(...)` for overlays and shadows.
- Keep naming semantic and stable across files.
- Freeze component-state colors only for globally repeated controls.
- Preserve the semantic difference between primary CTA surfaces and secondary controls.
- Put one-off decorative effects in the main guideline document, not in the global theme files.

## What Not To Do

- Do not use an eyedropper pipeline as the whole decision method.
- Do not set dark theme by subtracting or inverting light theme colors.
- Do not leave theme values qualitative.
- Do not let CTA emphasis collapse into the same contrast band as secondary actions.
- Do not encode implementation-specific APIs in the YAML; keep it tool-agnostic and semantic.
