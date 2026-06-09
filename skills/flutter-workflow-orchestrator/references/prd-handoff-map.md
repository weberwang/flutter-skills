# PRD Handoff Map

Use this reference when the workflow must explain how the PRD feeds downstream stages.

## Purpose

The PRD is not only a document. It is the upstream contract for several later stages.

This map prevents one common failure mode:

"The PRD exists, but nobody knows which part is consumed by which downstream step."

## Downstream Consumers

### 1. `flutter-prd-rd-writer`

Consumes these PRD sections first:

- problem statement
- goals and success criteria
- target users and roles
- scope and non-goals
- data, permissions, and dependencies
- constraints
- question ledger

Uses them for:

- technical baseline
- package stack decisions
- backend collaboration model
- fullchain delivery planning

### 2. `@product-design`

Consumes these PRD sections first:

- target users and roles
- core scenarios and user journey
- UX posture
- platform and validation hints
- goals and task priorities
- explicit constraints

Uses them for:

- brief confirmation
- direction recommendation
- final product-direction confirmation

### 3. Pre-Direction `Creative Production`

Consumes these PRD sections first:

- target users
- business goal
- brand or campaign context when present
- scope posture
- UX tone hints when they affect the visual message

Uses them for:

- direction-input mood boards
- ad or hero direction exploration
- scene or offer-led exploration

This branch may inform direction but does not replace Product Design confirmation.

### 4. Post-Direction `Creative Production`

Consumes these PRD sections first:

- approved product direction context
- campaign or asset intent
- audience and channel constraints
- explicit non-goals
- compliance or claim-sensitive boundaries

Uses them for:

- asset exploration
- reviewable production outputs
- publish-safe polish

### 5. `flutter-rd-module-splitter`

Consumes these PRD sections first:

- in-scope functions
- explicit non-goals
- core user journey
- critical states
- data and dependency boundaries

Uses them for:

- module boundaries
- executable `impl.md`
- shell vs feature separation

### 6. Shared Freeze And Structured Design Source

Consumes these PRD sections indirectly through:

- Product Design output
- `DESIGN.md`
- approved visual evidence

The PRD should not attempt to replace those artifacts, but it must already define the product intent and constraints they inherit.

## Mapping Checklist

Before leaving PRD preparation, confirm:

- technical baseline can read product scope without guessing
- Product Design can read user journey and task priority without re-scoping the feature
- Creative Production can read audience and business goal without inventing campaign intent
- module splitting can read scope boundaries without inferring feature ownership from page count

## Hard Rule

If a downstream stage needs to invent scope, user role, or acceptance criteria that should have been present in the PRD, route back to PRD preparation first instead of patching the gap ad hoc later.
