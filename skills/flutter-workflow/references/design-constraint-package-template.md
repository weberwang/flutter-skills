# Design Constraint Package Template

Use this reference when `flutter-workflow` needs a single product-design constraint packet that can drive high-fidelity effect images, structured Pencil design source generation, restoration, and implementation review without forcing the human reviewer to restate the same rules repeatedly.

This is an outward-facing design artifact.
It is not the runtime workflow state file.
It is not a replacement for `DESIGN.md`.

## Purpose

The design constraint package defines:

- what kind of product surface is being designed
- which user tasks and business goals matter most
- which visual directions are acceptable
- which visual directions are forbidden
- which implementation and asset boundaries must be respected
- what the high-fidelity effect image must prove before downstream promotion

Use it to keep the workflow product-led instead of image-led.

## Artifact Position

Within the current workflow, keep artifact responsibilities separate:

1. `design_constraint_package.md`
   Defines product, interaction, visual, and implementation constraints.
2. `human_decision_recommendation_package.md`
   Defines the 2-3 recommended options for the human decision points that cannot be fully automated.
3. runtime workflow record
   Stores machine-readable execution state and must remain an internal orchestrator artifact.

Do not merge all three responsibilities into `DESIGN.md`.
Do not use the runtime workflow record as the main design communication document.

## Output Language

When instantiated for a real project, all human-readable content in this artifact must default to Simplified Chinese unless the user explicitly requests another language.

## Required Sections

Keep this order unless a project truly does not need one of the sections:

1. `## Product Basics`
2. `## Scope And Core Flows`
3. `## Information Hierarchy`
4. `## Interaction Priorities`
5. `## Global Visual Goals`
6. `## Style Boundaries`
7. `## Visual System Constraints`
8. `## Component And Screen Language`
9. `## Content And Tone`
10. `## State Design Requirements`
11. `## Asset And Implementation Boundaries`
12. `## High-Fidelity Effect Image Contract`
13. `## Acceptance Criteria`

## PRD Extraction Rule

Prefer auto-filling these fields from the PRD, navigation, and technical baseline when the evidence is explicit enough:

- product type
- target users
- core tasks
- business goals
- required pages
- critical flows
- first-screen information hierarchy
- high-risk actions
- trust and compliance pressure
- state coverage requirements
- platform scope
- performance limits
- responsive constraints

If a field is not explicit in the source artifacts, do not invent it.
Write `not_provided` and route that gap into the human decision recommendation package when needed.

## Human Decision Rule

These fields usually still require a human or design-owner decision even when the PRD is complete:

- final style direction
- brand maturity and emotional tension
- acceptable experimentation level
- reference band
- texture, illustration, and 3D tolerance
- which regions may use atlas-backed assets
- which regions must remain `flutter_native`

Do not ask the human to answer those from a blank slate.
Produce recommended options first through `human_decision_recommendation_package.md`.

## Template

```md
# Design Constraint Package

## Product Basics
- Product name:
- Product type:
- Platform:
- Target users:
- Core task:
- Business goal:
- Design scope for this cycle:

## Scope And Core Flows
- Required pages:
- Primary flow:
- Secondary flows:
- Explicitly out of scope:

## Information Hierarchy
- Tier-1 information:
- Tier-2 information:
- De-emphasized information:
- The first screen must answer:

## Interaction Priorities
- First user action:
- Primary CTA posture:
- High-risk actions:
- States that need strong feedback:
- Regions allowed to trade some efficiency for stronger atmosphere:
- Regions that must stay efficiency-first:

## Global Visual Goals
- Desired product temperament:
- Brand keywords:
- Explicitly forbidden temperament:
- Maturity target:
- Emotional tension:
- Brand visibility priority:

## Style Boundaries
- Acceptable style range:
- Forbidden style range:
- Decoration tolerance:
- Experimental layout tolerance:
- Illustration / 3D / skeuomorphic tolerance:
- Marketing-like expression tolerance:

## Visual System Constraints
- Color strategy:
- Contrast strategy:
- Typography mood:
- Weight strategy:
- Shape language:
- Shadow and elevation posture:
- Icon style:
- Image or illustration treatment:
- Density target:
- Whitespace strategy:

## Component And Screen Language
- Navigation posture:
- List posture:
- Form posture:
- Button posture:
- Layer / modal posture:
- Data-display posture:
- Empty-state posture:
- Error-state posture:
- Loading-state posture:

## Content And Tone
- Copy tone:
- Title length preference:
- Explanation budget:
- Minimal default copy rule:
- Emotional copy tolerance:
- Professional / trust wording requirement:

## State Design Requirements
- Normal state:
- Empty state:
- Error state:
- Success state:
- Risk state:
- Onboarding or first-use state:

## Asset And Implementation Boundaries
- Prefer `flutter_native` by default:
- Atlas-backed regions allowed:
- Regions that must stay code-restored:
- Transparent atlas allowed:
- Slicing allowed:
- Performance limits:
- Device adaptation limits:

## High-Fidelity Effect Image Contract
- Effect-image purpose:
- Effect image is the only visual input for later structured design generation:
- Product-surface requirements it must prove:
- Things that must never appear:
- Regions that must remain commercially shippable:
- Restoration fidelity expectations:

## Acceptance Criteria
- UX acceptance criteria:
- Visual acceptance criteria:
- Consistency acceptance criteria:
- Implementation feasibility criteria:
- Final human confirmation items:
```

## Writing Rules

- Keep the package product-facing rather than art-poster-facing.
- Reject ad-like, landing-hero-like, or concept-only language for product surfaces.
- Prefer explicit boundaries over vague adjectives.
- Every line should be actionable by design generation, Pencil structuring, or implementation review.
- If a section is unknown, mark it explicitly instead of skipping it.
