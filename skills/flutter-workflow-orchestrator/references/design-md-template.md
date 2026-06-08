# DESIGN.md Template

Use this reference when `flutter-workflow-orchestrator` has reached `product_direction_confirmed` and must write a project-level `DESIGN.md` file that matches the Stitch `DESIGN.md` format.

## Purpose

`DESIGN.md` is the project-level design system document that downstream agents read to generate consistent UI.

In this workflow, `DESIGN.md` must:

- live at the project root as `DESIGN.md`
- be written after final product design direction confirmation
- exist before Stitch or Pencil structured design-source generation
- be self-contained
- avoid references to other repo files, variables, or paths

## Required Shape

A valid `DESIGN.md` has two layers:

1. YAML front matter at the top, delimited by `---`
2. Markdown prose below it

The YAML tokens are the normative machine-readable values. The prose captures design intent that raw tokens alone cannot express.

## Minimum YAML Schema

Use this baseline schema unless the project truly lacks a section:

```yaml
---
version: alpha
name: <design-system-name>
description: <short-summary>
colors:
  primary: <css-color>
  secondary: <css-color>
  tertiary: <css-color>
  surface: <css-color>
  on-surface: <css-color>
typography:
  headline-lg:
    fontFamily: <font-family>
    fontSize: <dimension>
    fontWeight: "<weight>"
    lineHeight: <dimension>
    letterSpacing: <dimension-optional>
  body-md:
    fontFamily: <font-family>
    fontSize: <dimension>
    fontWeight: "<weight>"
    lineHeight: <dimension>
rounded:
  sm: <dimension>
  md: <dimension>
  lg: <dimension>
spacing:
  sm: <dimension-or-number>
  md: <dimension-or-number>
  lg: <dimension-or-number>
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: <dimension-or-token-ref>
---
```

## Supported Token Areas

Prefer covering these token groups when they are relevant to the product:

- `colors`
- `typography`
- `rounded`
- `spacing`
- `components`

Additional token detail such as elevation, shadows, or motion may be expressed either through token-like component properties or through the markdown rationale section when the current schema does not need a separate top-level key.

## Required Markdown Order

If these sections are present, keep them in this order:

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

Sections may be omitted when truly unnecessary, but do not reorder them.

## Writing Rules

- Keep the file self-contained.
- Do not say "see `docs/rd/...`" or "follow the theme file".
- Do not leave placeholder text such as `TODO`, `TBD`, or angle-bracket markers in the final file.
- Use valid YAML values for token fields.
- Use token references like `{colors.primary}` when a component is intentionally mapped to another token.
- Capture product-level design intent, not page-by-page implementation instructions.
- Prefer concrete visual language over vague adjectives.

## Workflow Mapping

When writing `DESIGN.md`, translate confirmed upstream decisions into this file:

- final product design direction
- shared public shell posture
- visual system
- typography mood
- palette direction
- spacing rhythm
- component families
- CTA posture
- depth and material treatment
- shape language
- optional effect-image evidence, when it materially clarifies the design intent

Do not let optional effect images override the confirmed direction. `DESIGN.md` remains the primary upstream packet.

## Project Template

Use this starter template as the default output shape:

```md
---
version: alpha
name: <Project Design System>
description: <One-paragraph design system summary>
colors:
  primary: "#000000"
  on-primary: "#ffffff"
  secondary: "#666666"
  tertiary: "#cc5500"
  surface: "#ffffff"
  on-surface: "#111111"
  surface-container: "#f5f5f5"
  outline: "#dddddd"
typography:
  display-lg:
    fontFamily: <Primary Font>
    fontSize: 56px
    fontWeight: "700"
    lineHeight: 64px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: <Primary Font>
    fontSize: 32px
    fontWeight: "600"
    lineHeight: 40px
  body-md:
    fontFamily: <Primary Font>
    fontSize: 16px
    fontWeight: "400"
    lineHeight: 24px
  label-sm:
    fontFamily: <Primary Font>
    fontSize: 12px
    fontWeight: "600"
    lineHeight: 16px
rounded:
  sm: 4px
  md: 12px
  lg: 20px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.md}"
  card-default:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

## Overview

Describe the design system's personality, emotional tone, product posture, and intended user impression.

## Colors

Explain how the palette should be used, what each major color family means, and where contrast must stay strongest.

## Typography

Explain hierarchy, rhythm, and how display, body, and label styles should feel in practice.

## Layout

Describe spacing rhythm, container logic, density posture, and how the shell should organize content.

## Elevation & Depth

Describe whether the system feels flat, layered, glassy, tactile, editorial, or restrained, and how depth is signaled.

## Shapes

Describe radius language, corner posture, icon softness, and structural geometry.

## Components

Describe how buttons, cards, inputs, navigation, lists, and other repeated patterns should behave visually.

## Do's and Don'ts

- Do preserve the confirmed hierarchy and CTA posture.
- Do keep component families visually consistent across screens.
- Don't invent new local styles that contradict the shared system.
- Don't replace token-backed decisions with ad-hoc page-level styling.
```
