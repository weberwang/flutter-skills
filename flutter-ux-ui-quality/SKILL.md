---
name: flutter-ux-ui-quality
description: Use when defining Flutter screen briefs, navigation flows, visual systems, responsive layout requirements, empty/loading/error states, screenshot evidence, golden evidence, or UX/UI quality gates.
---

# Flutter UX UI Quality

## Overview

Use this skill to stop low-quality UI from shipping. Text specs are drafts until high-fidelity effect images confirm the UX/UI direction.

## Required Sequence

1. Write a global UI brief with [references/ui-brief-template.md](references/ui-brief-template.md) covering navigation, screen inventory, state coverage, cross-module page flows, first-value delivery, trust, and safe-to-try conditions.
2. Select or define the Flutter design system using [references/flutter-design-system.md](references/flutter-design-system.md).
3. Run `@product-design user-context` preflight, then use `@product-design get-context` to confirm the design target and intended user outcome. Use `@product-design ideate` to generate exactly three global visual directions and record the selected direction.
4. Use `flutter-hifi-mockup` to confirm global high-value UX/UI decisions with high-fidelity effect images.
5. Feed global flows, screen inventory, and page interaction order into `docs/plans/module-map.md`.
6. During each UI module or page implementation task, use `flutter-pencil-design` first for low-fidelity structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
7. After low-fidelity structure is reviewed, use `flutter-hifi-mockup` for the concrete page when page-level visual evidence is missing.
8. After page-level high-fidelity approval and design freeze, use `flutter-asset-atlas` when required visual assets need reuse checks, generation, background transparentization, slicing, export, inventory, or fidelity review.
9. After required asset atlas evidence exists, use `flutter-pencil-design` for high-fidelity Pencil restoration when editable visual handoff is required.
10. Implement the screen against the UI brief, `docs/design/design-freeze.md`, `docs/design/wireframe-spec.md`, `docs/design/pencil-hifi-restoration.md`, and asset atlas evidence when present.
11. Capture evidence using screenshots, golden tests, or integration screenshots.
12. Review evidence with [references/visual-qa-rubric.md](references/visual-qa-rubric.md), then run `@product-design audit` for user-facing flows.
13. Fix Critical and Important issues, then repeat evidence capture and audit when the UI flow changed.

## Flutter UI Standards

- Prefer Material 3 as the baseline unless the app has a stronger platform or brand requirement.
- Centralize tokens: color, typography, spacing, radius, elevation, motion.
- Build reusable primitives for buttons, text fields, scaffold, empty state, error state, and loading skeletons.
- Use real user content examples. Avoid generic fake names and filler content.
- Test at small phone, normal phone, tablet, and large text scale where relevant.
- Treat visual quality as task clarity, system consistency, and reliable feedback before material or decorative polish. Any decoration, gradient, shadow, texture, or motion must reinforce hierarchy, state, or brand character.

## Rejection Criteria

- No loading, empty, error, success, disabled, and permission-denied states where applicable.
- Text overflow, clipped controls, inaccessible contrast, or unclear primary action.
- Layout only verified on one viewport.
- Page-level high-fidelity effect image generated before low-fidelity structure passes Wireframe Review.
- UI page implementation starts from text-only descriptions without page-level high-fidelity effect image confirmation.
- Module page order contradicts the primary user flow or skips required transition states.
- A first-time user cannot understand the value, safely begin, or reach the specified first-value moment from the planned flow.
- Implementation claims "polished" without screenshots or golden evidence.
- Visual style diverges from the selected design system without written reason.
- Global visual direction is selected without the three-direction `@product-design ideate` review.

## Output Files

- `docs/design/user-flows.md`
- `docs/design/screen-spec.md`
- `docs/design/ui-quality-gates.md`
- `docs/design/design-freeze.md` when high-fidelity mockups are used
- `docs/design/wireframe-spec.md` when low-fidelity Pencil wireframes are used
- `docs/design/asset-atlas.md` when required visual assets exist
- `docs/design/asset-slicing-manifest.md` when required visual assets exist
- `docs/design/asset-fidelity-review.md` when required visual assets exist
- `docs/design/asset-inventory.md` when required illustrations or bitmaps exist
- `docs/design/pencil-flutter-handoff.md` when Pencil is used
- `docs/design/pencil-hifi-restoration.md` when Pencil carries high-fidelity visual restoration
- `docs/design/pencil-parity-review.md` when wireframe parity is reviewed
- screenshot or golden evidence path recorded in `.codex-workflow/progress.md`

## Gate

Do not approve UX/UI from text alone. Do not call a screen complete until the selected `@product-design ideate` direction, high-fidelity confirmation, global and page design-freeze constraints, wireframe text specs when present, required asset atlas evidence including background transparentization when applicable, screenshots or golden evidence, `@product-design audit` findings for user-facing flows, and visual QA have been reviewed with all Critical or Important findings closed.
