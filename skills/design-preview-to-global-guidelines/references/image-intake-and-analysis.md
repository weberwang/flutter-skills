# Image Intake And Analysis

Use this reference when the input is a screenshot, preview comp, effect mockup, stitched multi-screen board, or another static visual source.

## Supported Input Surfaces

- Approved single-screen preview
- Approved multi-screen preview pack
- Design screenshot with visible states
- Composite board with repeated component patterns
- Mixed pack containing previews plus annotations

## Not A Good Entry Surface

- Text-only requests with no visual evidence
- Multiple materially different directions without an approved baseline
- A single decorative hero shot with no usable UI structure
- Low-fidelity sketch content when the user expects frozen theme values

Route those cases to `mobile-ui-design-coach` or `design-preview-to-pen` before using this skill.

## Minimum Evidence Checklist

Before freezing, confirm as much of this as the input allows:

- Primary screen or page family is visible
- Main call to action is visible
- Surface hierarchy can be distinguished
- Typography or information density is readable
- Repeated components exist, or the absence of reuse is itself obvious
- At least one state clue exists for loading, empty, disabled, alert, or success behavior
- Platform behavior baseline is known or can be reasonably inferred

## Analysis Order

1. Identify the product moment: what job is happening on screen.
2. Identify the primary action and the next best action.
3. Identify the hierarchy: what the eye should read first, second, and third.
4. Identify the surface model: page background, cards, elevated regions, overlays.
5. Identify the repeated components and their state hints.
6. Identify the visual temperature, density, and restraint level.
7. Identify what appears globally systematic versus locally decorative.

## Allowed Inference

Infer when the screen strongly implies a stable rule, such as:

- text contrast hierarchy
- primary versus secondary action treatment
- spacing rhythm
- radius family
- global surface depth
- light and dark semantic role expectations

## Required Output When Evidence Is Incomplete

Keep the output contract intact and use only these values for missing information:

- `not_provided`
- `not_applicable`
- `needs_confirmation`

Do not drop sections and do not let downstream skills guess what was omitted here.
