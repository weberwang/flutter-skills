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

1. Write `docs/design/ui-spec.md` with [references/ui-brief-template.md](references/ui-brief-template.md), covering navigation, screen inventory, state coverage, cross-module page flows, first-value delivery, trust, safe-to-try conditions, quality gates and the active visual expression preset.
2. Select or define the Flutter design system using [references/flutter-design-system.md](references/flutter-design-system.md).
3. Confirm the product brief recorded a derived expression preset and completed any needed visual interrogation. Define one market-informed direction when the user already supplied a clear brand or reference; define two or three when exploration or a material visual tradeoff remains. Describe cross-page color, typography, shape, imagery, material, motion, signature, implementation cost, and system-extension rules; do not generate a page, representative-page, module, or screen effect image.
4. Present the requested direction definitions, wait for the user's selection when alternatives exist, and run the global direction freeze confirmation. Record the selected direction, signature confirmation when required, implementation-cost acceptance, any `pin` / `raise` / `loosen` override, and explicit freeze intent in `docs/design/global-design-freeze.md`. Do not create `.codex-workflow/visuals/global/`.
5. Feed global flows, screen inventory, and page interaction order into `docs/plans/module-map.md`.
6. During each UI module or page implementation task, use `flutter-pencil-design` first for low-fidelity structure and Wireframe Review; store the semantic contract in that page's `design-decision.md`.
7. Before generating an effect image, check whether visual goals, required pages/states, page budget, signature strength, or implementation/asset cost still needs a user decision. Record only new decisions; otherwise reuse the existing global and page constraints.
8. After low-fidelity structure is reviewed, use `flutter-hifi-mockup` for the concrete page. On confirmation, persist the exact selected image first in `.codex-workflow/visuals/pages/<page-name>/`, then write one page `design-decision.md`.
9. After page-level high-fidelity approval and a page design decision, use `flutter-asset-atlas` when required visual assets need reuse checks, generation, background transparentization, slicing, export, inventory, or fidelity review.
10. After required asset-manifest evidence exists, use `flutter-pencil-design` for high-fidelity Pencil restoration when editable visual handoff is required.
11. Implement the screen against `docs/design/ui-spec.md`, the page `design-decision.md`, and its `asset-manifest.md` when present.
12. Capture evidence using screenshots, golden tests, or integration screenshots.
13. Review evidence with [references/visual-qa-rubric.md](references/visual-qa-rubric.md), then run an independent visual-QA review for user-facing flows.
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
- A high-risk or exploratory page generates high-fidelity effects before its required semantic review.
- A high-value page starts implementation without the page-level visual evidence selected by its risk tier.
- Module page order contradicts the primary user flow or skips required transition states.
- A first-time user cannot understand the value, safely begin, or reach the specified first-value moment from the planned flow.
- Implementation claims "polished" without screenshots or golden evidence.
- Visual style diverges from the selected design system without written reason.
- Global visual direction is frozen while a material visual uncertainty remains unresolved or, when exploration is required, without meaningfully distinct alternatives.
- A global, representative-page, module, or screen effect image is generated during global direction positioning.
- A module page effect image is generated before the module effect-image interrogation and Wireframe Review pass.
- Full-budget or wow-required pages ship without a restatable visual signature, or exploration defaults to universal restraint instead of the derived preset.

## Output Files

- `docs/design/ui-spec.md`
- `docs/design/global-design-freeze.md`
- Page `design-decision.md`, frozen effect image and `asset-manifest.md` only when their conditions apply
- Screenshot or golden paths linked from task `review.md`

## Gate

Do not generate effect images during global direction positioning. For pages whose risk tier requires a visual target, complete the semantic contract and any needed review before generation, then persist only the explicitly frozen selection and its identifiers. Do not force high-fidelity images, asset manifests, Pencil evidence, or independent visual QA onto ordinary reuse work. Call a screen complete only when the design evidence, screenshots or goldens, and review selected by its risk tier have passed.
