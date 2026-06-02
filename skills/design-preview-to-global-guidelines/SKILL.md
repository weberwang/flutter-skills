---
name: design-preview-to-global-guidelines
description: Use when screenshots, visual previews, effect mockups, or approved static comps must be analyzed into a stable global UI/UX guidance contract, especially when downstream Pencil, Flutter architecture, implementation, or parity-review skills need fixed design principles plus concrete light and dark theme values without branching or reinterpretation.
---

# Design Preview To Global Guidelines

## Overview

Turn approved visual evidence into a design-source contract that downstream skills can consume directly. The goal is not taste commentary alone; it is to freeze one global guidance document plus two concrete theme files so later skills stop guessing.

## Designer Role

Act like a product designer and design-systems lead. Infer stable product rules from the visual evidence, decide what belongs in the global system, and close the gaps that downstream implementation would otherwise reinterpret.

## Quick Start

- If the user only has a text brief and no usable visual evidence, use `mobile-ui-design-coach` first.
- If the user still needs preview exploration or direction comparison, use `mobile-ui-design-coach` or `design-preview-to-pen` first, then return here after a direction is chosen.
- If multiple previews represent materially different directions and no single direction is approved, stop and require a chosen baseline before freezing.
- If downstream Pencil, Flutter architecture, implementation, or parity work must not reinterpret theme values or global UI rules, use this skill before `flutter-design-freeze-gate`, `design-preview-to-pen`, or `flutter-pen-to-architecture`.
- When the user wants written artifacts, default to exactly these files: `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml`.

## Workflow

1. Read `references/image-intake-and-analysis.md` to confirm the visual input is strong enough for freezing.
2. Separate confirmed evidence from missing evidence. If multiple competing directions still exist, stop and require a single chosen baseline.
3. Infer the product posture, target users, core scenarios, and the global experience promise from the visuals.
4. Extract stable global rules for hierarchy, page structure, repeated components, interaction posture, state handling, and visual restraint.
5. Read `references/global-guideline-contract.md` and produce `global-design-guidelines.md` with the exact metadata block, exact section ids, and exact section order.
6. Read `references/theme-freeze-schema.md` and `references/value-freeze-strategy.md`, then freeze concrete light and dark theme values in `light-theme-freeze.yaml` and `dark-theme-freeze.yaml`.
7. Read `references/downstream-linking-rules.md` and fill `downstream_reference_index` so later skills know which sections and files they must cite.
8. If some evidence is incomplete, keep the contract structure intact and use only `not_provided`, `not_applicable`, or `needs_confirmation`; do not omit sections or push missing values downstream.

## Hard Rules

- Do not return only aesthetic commentary; always land on a reusable global contract.
- Do not leave theme outputs as adjectives such as “warmer,” “calmer,” or “more premium.”
- Do not let downstream skills infer missing global token values when this skill can freeze them now.
- Do not omit required files, required sections, or required role families.
- Do not treat dark mode as light mode with inverted colors.
- Do not let one-off local decoration become a global token unless the pattern is clearly systemic.
- Do not continue when multiple materially different directions are still unresolved.
- Do not rewrite the approved visual intent for implementation convenience.

## Deliverables

Every completed run should leave:

- `analysis_status`: `frozen` or `blocked`
- `global-design-guidelines.md`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`

The main guideline document must:

- use the exact metadata block from `references/global-guideline-contract.md`
- use the exact section ids and exact section order from `references/global-guideline-contract.md`
- include `downstream_reference_index` so later skills know what they must cite

Each theme file must:

- follow the exact schema from `references/theme-freeze-schema.md`
- use concrete values for every required leaf
- freeze global component-state roles for repeated controls
- include explicit contrast rules and forbidden overrides

## References

- Read `references/image-intake-and-analysis.md` for visual-input sufficiency, blocker rules, and allowed inference boundaries.
- Read `references/global-guideline-contract.md` for the exact `global-design-guidelines.md` contract.
- Read `references/theme-freeze-schema.md` for the exact light and dark theme file schema.
- Read `references/value-freeze-strategy.md` for converting visual evidence into stable concrete values.
- Read `references/downstream-linking-rules.md` for non-branching downstream consumption rules.
