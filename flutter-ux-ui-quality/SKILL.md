---
name: flutter-ux-ui-quality
description: Use when defining Flutter screen briefs, navigation flows, visual systems, responsive layout requirements, empty/loading/error states, screenshot evidence, golden evidence, or UX/UI quality gates.
---

# Flutter UX UI Quality

## Overview

Use this skill to freeze the global visual-system direction, then stop low-quality page UI from shipping through module-time effect images and evidence.

## Orchestrated Roles

When used inside `flutter-app-orchestrator`, dispatch Product/UX, Global direction, Global direction reviewer, and Visual QA subagents for their respective production or review work. The controller alone presents alternatives, requests user decisions, records confirmation, and freezes the selected direction or final verdict. Producer and reviewer must be different agents.

## Required Sequence

1. Write a global UI brief with [references/ui-brief-template.md](references/ui-brief-template.md) covering navigation, screen inventory, state coverage, cross-module page flows, first-value delivery, trust, safe-to-try conditions, and the active visual expression preset from [references/visual-expression-presets.md](references/visual-expression-presets.md).
2. Select or define the Flutter design system using [references/flutter-design-system.md](references/flutter-design-system.md).
3. Confirm the product brief recorded a derived expression preset and completed the one-time light visual interrogation. Use the orchestrator's global visual direction template to define exactly three market-informed direction positionings that satisfy the preset mix. Describe cross-page color, typography, shape, imagery, material, motion, signature, implementation cost, and system-extension rules; do not generate a page, representative-page, module, or screen effect image.
4. Present the three direction definitions, wait for the user's selection, and run the global direction freeze confirmation. Record the selected direction, signature confirmation or N/A reason, implementation-cost acceptance, any `pin` / `raise` / `loosen` override, and explicit freeze intent in `docs/design/global-design-freeze.md`. Do not create `.codex-workflow/visuals/global/`.
5. Feed global flows, screen inventory, and page interaction order into `docs/plans/module-map.md`.
6. During each UI module or page implementation task, use `flutter-pencil-design` first for low-fidelity structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
7. Before generating any effect image for the current UI module, complete the Module Effect-Image Interrogation Gate once for that module. Confirm its visual goals, pages and states requiring effect images, page budgets, signature expectations, and accepted implementation or asset cost; record the explicit shared-understanding confirmation.
8. After low-fidelity structure is reviewed, use `flutter-hifi-mockup` for the concrete page. On confirmation, persist the exact selected image first in `.codex-workflow/visuals/pages/<page-name>/` before writing the page prompt, brief, freeze, or ledger record.
9. After page-level high-fidelity approval and design freeze, use `flutter-asset-atlas` when required visual assets need reuse checks, generation, background transparentization, slicing, export, inventory, or fidelity review.
10. After required asset atlas evidence exists, use `flutter-pencil-design` for high-fidelity Pencil restoration when editable visual handoff is required.
11. Implement the screen against the UI brief, `docs/design/design-freeze.md`, `docs/design/wireframe-spec.md`, `docs/design/pencil-hifi-restoration.md`, and asset atlas evidence when present.
12. Capture evidence using screenshots, golden tests, or integration screenshots.
13. Review evidence with [references/visual-qa-rubric.md](references/visual-qa-rubric.md), then run `@product-design audit` for user-facing flows.
14. Fix Critical and Important issues, then repeat evidence capture and audit when the UI flow changed.

## Flutter UI Standards

- Use Apple Human Interface Guidelines and iOS conventions as the interaction, accessibility, and semantic baseline, not as a mandatory visual language. Define an authored component system whenever the approved product character benefits from shapes, composition, materials, imagery, or motion beyond stock Cupertino components.
- Centralize tokens: color, typography, spacing, radius, elevation, motion.
- Build reusable primitives for buttons, text fields, scaffold, empty state, error state, and loading skeletons.
- Use real user content examples. Avoid generic fake names and filler content.
- Test at small phone, normal phone, tablet, and large text scale where relevant.
- Treat visual quality as task clarity, system consistency, reliable feedback, and recognizable product character at the strength required by the visual expression preset. Decorations, gradient, shadow, texture, illustration, unconventional composition, or motion is allowed when it reinforces hierarchy, state, storytelling, or brand character within the page-type budget; require purpose and preset fit, not visual austerity.

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
- Global visual direction is frozen without three market-informed direction definitions or without satisfying the active preset’s required direction mix.
- A global, representative-page, module, or screen effect image is generated during global direction positioning.
- A module page effect image is generated before the module effect-image interrogation and Wireframe Review pass.
- Full-budget or wow-required pages ship without a restatable visual signature, or exploration defaults to universal restraint instead of the derived preset.

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
- frozen effect images stored only in `.codex-workflow/visuals/pages/<page-name>/`

## Gate

Do not generate effect images during global direction positioning. Do not approve a page UX/UI target from text alone. Do not generate a module page effect image before module effect-image interrogation and Wireframe Review. Do not write a page candidate, prompt, brief, review, freeze, or ledger entry before the user explicitly confirms the page freeze. At confirmation, persist the exact selected image under `.codex-workflow/visuals/pages/<page-name>/` before related artifacts and record candidate ID, decoded dimensions, SHA-256, and confirmation time. Do not call a screen complete until its page-level high-fidelity confirmation, global and page design-freeze constraints, wireframe text specs, required asset evidence, screenshots or goldens, audit findings, and visual QA have passed.
