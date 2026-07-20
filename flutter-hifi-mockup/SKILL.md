---
name: flutter-hifi-mockup
description: Use when generating, selecting, reviewing, or freezing page-level high-fidelity visual mockups, effect images, design references, image prompts, screen concepts, or visual target artifacts during Flutter module implementation.
---

# Flutter HiFi Mockup

## Overview

Generate and freeze page-level effect images during module implementation. Treat `docs/design/global-design-freeze.md` as the visual-system baseline; never generate global or representative-page effect images during global direction positioning.

## Orchestrated Roles

When used inside the full workflow, dispatch a Page high-fidelity agent to generate transient candidates and a separate Effect Image Reviewer to review them. Neither agent may persist, select, modify, approve, or freeze a candidate. The controller presents the results, records the user's decision, persists the exact selected image, and writes the freeze evidence.

## Inputs

- Confirmed module scope: `docs/plans/modules/<module-name>-scope.md`.
- Module function and page-function refinement.
- Module Effect-Image Interrogation Gate record.
- Product brief, MVP scope, user flow, and screen spec.
- Global design freeze.
- Reviewed low-fidelity Pencil structure and `docs/design/wireframe-spec.md`.
- Target device and required page state.
- First-value, trust, permission, payment, privacy, and recovery constraints when applicable.

## Workflow

1. Confirm the module-level functional grilling, function/page refinement, and Module Effect-Image Interrogation Gate are complete. Do not repeat the visual interrogation for every page unless a new conflict or decision appears.
2. Confirm the current page's low-fidelity Pencil structure passed Wireframe Review and `docs/design/wireframe-spec.md` exists.
3. Draft the page mockup brief with [references/mockup-brief-template.md](references/mockup-brief-template.md), including the global direction, expression preset, page-type budget dial, required state, and module effect-image decisions. Keep the brief, prompt, candidates, and review transient. Treat the brief as planning evidence, not generation prose.
4. Prepare the page prompt from the orchestrator's page high-fidelity prompt template and [references/image-prompt-principles.md](references/image-prompt-principles.md). Keep full traceability in the planning artifact, then reduce the actual generation prompt to one clear outcome, essential structure/content, a concise visual direction, true non-negotiables, and output requirements. Do not paste PRD mappings, rationale, exhaustive component details, or repeated avoid lists into the image model.
5. Run `@product-design user-context`, `@product-design get-context`, and `@product-design ideate` to generate exactly three page-level effect-image candidates for the same page, state, content, and device.
6. Run exactly one combined Effect Image Review with [references/mockup-review-rubric.md](references/mockup-review-rubric.md). Report product-design issues and premium-feel improvements separately; use Apple Human Interface Guidelines as the interaction baseline and judge visual quality against the frozen global direction and active page budget.
7. Present candidates and review, then ask the user to select, accept or decline review changes, and explicitly freeze one image. Do not write any candidate or visual artifact before confirmation.
8. Persist the exact selected image first at `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`. Then write the page prompt, brief, page design freeze, and progress entry with candidate ID, decoded dimensions, SHA-256, confirmation time, and module effect-image interrogation evidence.
9. Freeze implementation constraints with [references/design-freeze-template.md](references/design-freeze-template.md), referencing only the persisted page image.
10. Before asset work or Pencil restoration, apply the ownership-first decomposition in [bitmap-decomposition-standard.md](../flutter-pencil-design/references/bitmap-decomposition-standard.md): split runtime data from its renderer and fixed treatment, then classify every atomic unit as bitmap, UI, or data. Never turn representative runtime data into a production bitmap. Run the mandatory back-to-front visual sweep for backgrounds, decorations, overlays, icons, logos, textures, and clipped fragments; require a coverage audit with zero unowned visible elements. Record unresolved visual facts and native-Flutter feasibility evidence for UI units.
11. Use `flutter-asset-atlas` for required bitmaps or bitmap fills. Require its complete pre-slicing table to be shown inline and explicitly confirmed before any asset generation, adaptation, extraction, export, transparentization, or slicing; otherwise record `N/A: no bitmap or exported visual assets`.
12. Restore the approved page in Pencil when editable high-fidelity handoff is required, then hand off the frozen constraints and evidence to implementation.

## Output Files

- `docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md` after freeze.
- Page-scoped mockup brief and `design-freeze.md` after freeze.
- `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`.
- Asset and Pencil artifacts when required.
- Freeze evidence in `.codex-workflow/progress.md`.

## Generation Rules

- Generate each effect image at exactly `780 x 1688 px` and verify decoded dimensions.
- Use the shortest prompt that preserves task, state, signature, critical content, trust/accessibility boundaries, and output requirements. Guide secondary composition and detail instead of prescribing them.
- Reject a prompt with duplicated constraints, contradictory directions, adjective stacks, unrelated style references, or planning rationale. Keep only material negative constraints.
- Generate page effects only during module delivery, after module visual interrogation and Wireframe Review.
- Keep the page, state, content, data, and device identical across all three candidates.
- Follow the global design freeze without treating it as a page layout or page approval.
- Use realistic content and do not invent features, states, claims, or visual exceptions.
- Full-budget pages must express the frozen global signature; dial-down pages reduce decoration while preserving system identity.
- Treat custom widgets, `CustomPainter`, shaders, motion, and dedicated bitmap assets as valid when their value and accepted cost are documented.
- Never transform the selected image during freezing.

## Gate

Do not generate any effect image during global visual direction positioning. Do not generate a module page effect image before the module-level functional grilling, function/page refinement, Module Effect-Image Interrogation Gate, low-fidelity Pencil structure, Wireframe Review, and wireframe text spec are complete. Do not send the planning worksheet, source mapping, rationale, exhaustive detail list, or repeated negative constraints to the image model; block prompts with contradictions or no meaningful creative space. Do not write a candidate, prompt, brief, review, freeze, or ledger visual entry before explicit page freeze confirmation. Do not approve a page image without one combined review, exact `780 x 1688 px` dimensions, global-direction alignment, required signature verdict, and the user's explicit decision on proposed changes. Do not begin asset work, Pencil restoration, or Flutter page implementation until the selected page image and design freeze exist. Do not approve decomposition while a runtime-data visual is marked for bitmap export, a visible element lacks ownership, or a background decoration or icon placement/state is absent from the coverage audit.
