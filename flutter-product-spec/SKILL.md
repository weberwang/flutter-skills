---
name: flutter-product-spec
description: Use when defining or refining a Flutter app idea, MVP, product brief, commercial model, target users, user stories, acceptance criteria, or feature boundaries before design or implementation.
---

# Flutter Product Spec

## Overview

Turn an app idea into a constrained commercial product spec. The output must make scope, users, value, and acceptance criteria testable before UX or code work starts.

## Inputs

- App idea or business goal.
- `docs/product/grilling-log.md` with the user's explicit shared-understanding confirmation when the product is entering the commercial delivery workflow.
- Target market or audience, if known.
- Platform assumptions: Flutter mobile first unless the user states otherwise.
- Monetization intent, if known.

## Process

1. State assumptions and ask only for information that changes MVP scope.
2. Identify target users, painful jobs, high-value moments, and the first value the user must receive after starting.
3. Split MVP from later features.
4. Define user stories with acceptance criteria, including the value, trust, and perceived-risk conditions that affect first-time adoption.
5. Define commercial constraints: payment, account, data ownership, privacy, support, and retention.
6. Record the intended product quality: brand character, interaction tone, visual constraints, and decorations that are justified by the product rather than added for novelty.
7. Derive a visual expression preset from product category and audience using [../flutter-ux-ui-quality/references/visual-expression-presets.md](../flutter-ux-ui-quality/references/visual-expression-presets.md). Record preset ID, axis values, and derivation basis in the product brief. Do not lower task-clarity or trust gates; the preset only sets expression ceiling and exploration bias.
8. Before handing off to global UX/UI exploration, run the one-time light visual interrogation from the preset reference. Record answers in `docs/product/grilling-log.md` and mirror signature and implementation-cost commitments in the product brief. Both records are required.
9. Write product artifacts using [references/product-brief-template.md](references/product-brief-template.md) and [references/mvp-scope-template.md](references/mvp-scope-template.md).

## Output Files

- `docs/product/product-brief.md`
- `docs/product/mvp-scope.md`
- `docs/product/user-stories.md`
- `docs/product/grilling-log.md` updates for the light visual interrogation

## Gate

Do not proceed to UX/UI or technical design until the grilling log records the user's explicit shared-understanding confirmation, the MVP has clear non-goals, every core feature has acceptance criteria, the product brief records a derived visual expression preset, and the one-time light visual interrogation answers are recorded in the grilling log with signature and implementation-cost commitments mirrored in the product brief.

## Common Mistakes

- Writing a feature catalog without user value, a first-value moment, or a safe reason to try the product.
- Allowing "nice to have" items into MVP.
- Missing account, privacy, or monetization assumptions for a commercial app.
- Treating visual polish as a substitute for clear value, reliable feedback, and trust.
- Leaving the visual expression preset blank, or using "restrained" as a universal default instead of deriving axes from category and audience.
- Entering UX/UI after deriving a preset but before completing the light visual interrogation and brief mirror.
