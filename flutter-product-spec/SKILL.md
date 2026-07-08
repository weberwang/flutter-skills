---
name: flutter-product-spec
description: Use when defining or refining a Flutter app idea, MVP, product brief, commercial model, target users, user stories, acceptance criteria, or feature boundaries before design or implementation.
---

# Flutter Product Spec

## Overview

Turn an app idea into a constrained commercial product spec. The output must make scope, users, value, and acceptance criteria testable before UX or code work starts.

## Inputs

- App idea or business goal.
- Target market or audience, if known.
- Platform assumptions: Flutter mobile first unless the user states otherwise.
- Monetization intent, if known.

## Process

1. State assumptions and ask only for information that changes MVP scope.
2. Identify target users, painful jobs, and high-value moments.
3. Split MVP from later features.
4. Define user stories with acceptance criteria.
5. Define commercial constraints: payment, account, data ownership, privacy, support, and retention.
6. Write product artifacts using [references/product-brief-template.md](references/product-brief-template.md) and [references/mvp-scope-template.md](references/mvp-scope-template.md).

## Output Files

- `docs/product/product-brief.md`
- `docs/product/mvp-scope.md`
- `docs/product/user-stories.md`

## Gate

Do not proceed to UX/UI or technical design until the MVP has clear non-goals and every core feature has acceptance criteria.

## Common Mistakes

- Writing a feature catalog without user value.
- Allowing "nice to have" items into MVP.
- Missing account, privacy, or monetization assumptions for a commercial app.
