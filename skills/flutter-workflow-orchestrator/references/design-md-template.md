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

The goal is not only visual consistency. A high-quality `DESIGN.md` in this workflow must also preserve:

- task completion efficiency
- interaction and feedback consistency
- multi-state coverage
- responsive and multi-device behavior
- one frozen base design viewport for the current design cycle
- content and brand tone consistency
- shared shell and shared component consistency

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

If the product has mature design-system data, also capture:

- semantic state colors
- elevation or shadow scales
- motion timing or motion posture
- component naming conventions
- state naming conventions

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

Recommended extension sections for this workflow:

- `## Task Priorities`
- `## Interaction & Feedback`
- `## Responsive Strategy`
- `## States & Edge Cases`
- `## Content & Tone`

If you add these extension sections, place them after `## Components` and before `## Do's and Don'ts`.

## Writing Rules

- Keep the file self-contained.
- Do not say "see `docs/rd/...`" or "follow the theme file".
- Do not leave placeholder text such as `TODO`, `TBD`, or angle-bracket markers in the final file.
- Use valid YAML values for token fields.
- Use token references like `{colors.primary}` when a component is intentionally mapped to another token.
- Capture product-level design intent, not page-by-page implementation instructions.
- Prefer concrete visual language over vague adjectives.
- Explicitly state what must stay consistent across screens: style direction, theme system, public shell, and shared component families.
- Explicitly state that page layouts must not be reduced below the frozen base design viewport and that layout density should be solved without collapsing core whitespace.
- Explicitly state what matters most in the first 3 seconds of the main user journey.
- Explicitly state how the design behaves under empty, loading, error, disabled, long-content, short-content, and slow-network scenarios.
- Explicitly state which regions may adapt responsively and which regions are visually locked.
- Explicitly state naming conventions for shared components and shared states when the system is large enough to need them.

## Workflow Mapping

When writing `DESIGN.md`, translate confirmed upstream decisions into this file:

- frozen base design viewport and chosen device preset
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
- core user task priorities
- first-screen information hierarchy and CTA exposure
- interaction feedback rhythm
- responsive behavior across phone, tablet, and desktop surfaces when relevant
- state design for loading, empty, error, disabled, and transition-heavy flows
- content tone, brand voice, and writing posture
- shared naming conventions for components and states

Do not let optional effect images override the confirmed direction. `DESIGN.md` remains the primary upstream packet.

## Quality Goals

Treat this checklist as the minimum bar for a high-quality design target:

- The main user task is obvious within the first 3 seconds.
- The primary CTA is visible or predictably discoverable on the main path.
- Information hierarchy is stable across screens.
- Interaction feedback is consistent across taps, hovers, focus, submission, and error recovery.
- Empty, loading, error, disabled, long-content, and short-content states are intentionally designed rather than implied.
- The design scales across target devices without inventing a second visual language.
- Pages do not collapse below the frozen design viewport just to fit more content.
- Spacing, margins, and structural whitespace remain intentional rather than being compressed away.
- Shared shell and shared components remain recognizable everywhere.
- Copy tone matches the product personality and user context.

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

## Task Priorities

Describe the product's highest-priority user tasks, what must be visible first, and which actions should dominate the primary path.

## Interaction & Feedback

Describe hover, press, focus, loading, success, warning, error, disabled, and transition feedback. Explain the intended motion restraint or motion emphasis.

## Responsive Strategy

Describe how the design adapts across phone, tablet, desktop, or other target surfaces. State which layouts can reflow and which visual relationships must stay locked.

## States & Edge Cases

Describe empty states, loading states, errors, permission denial, long text, short text, slow network, and multi-step transition behavior.

## Content & Tone

Describe brand voice, UX writing tone, naming patterns, and how CTA language should feel in high-confidence, low-confidence, and recovery moments.

## Do's and Don'ts

- Do preserve the confirmed hierarchy and CTA posture.
- Do keep component families visually consistent across screens.
- Do preserve the same style direction, theme system, shared shell, and shared public component families across all restored pages.
- Do design all critical states, not only the ideal happy path.
- Do keep the first-screen task path obvious and low-friction.
- Do make interaction feedback predictable across primary flows, recovery flows, and disabled states.
- Do state how the design scales on every target surface that is actually in scope.
- Don't invent new local styles that contradict the shared system.
- Don't let responsive adaptation become a second design language.
- Don't hide core actions behind decorative hierarchy.
- Don't leave loading, empty, error, or disabled behavior undefined.
- Don't let copy tone drift between primary flow, support flow, and recovery flow.
- Don't replace token-backed decisions with ad-hoc page-level styling.
```
