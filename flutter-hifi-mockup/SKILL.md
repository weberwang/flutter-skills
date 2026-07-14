---
name: flutter-hifi-mockup
description: Use when generating, selecting, reviewing, or freezing high-fidelity visual mockups, effect images, design references, image prompts, screen concepts, or visual target artifacts before Flutter UI implementation.
---

# Flutter HiFi Mockup

## Overview

Use this skill to confirm UX/UI direction with high-fidelity effect images. Global mockups confirm visual direction and design-system intent; page-level mockups confirm implementation targets after low-fidelity structure and Wireframe Review.

## When to Use

Use this before implementation when:

- The user asks for effect images, high-fidelity mockups, visual concepts, app screen design, or visual direction.
- The screen is commercially important: onboarding, home, paywall, checkout, dashboard, editor, settings, or error recovery.
- The UI brief contains vague terms such as "premium", "clean", "modern", or "high quality".
- UX/UI needs approval and text alone would be too abstract.
- The implementation team needs a visual target for Flutter widgets, tokens, layout, and states.
- A module or page implementation task is about to start and lacks approved page-level visual evidence.

## Inputs

- Product brief and MVP scope.
- User flow and screen spec.
- Reviewed low-fidelity Pencil structure and `docs/design/wireframe-spec.md` for page-level module work.
- Brand constraints or references, if available.
- Target device class: phone, tablet, or responsive set.
- Required states: success, loading, empty, error, disabled, permission, paywall.

## Workflow

1. Classify the mockup as global direction or page-level implementation target.
2. For page-level module work, confirm `docs/design/wireframe-spec.md` exists before writing the mockup brief.
3. Write a mockup brief for the current module or page with [references/mockup-brief-template.md](references/mockup-brief-template.md).
4. Confirm `@product-design user-context` preflight has completed, then use `@product-design get-context` to confirm the design target and intended user outcome. Use `@product-design ideate` to generate exactly three visual directions for the same screen or flow.
5. Run exactly one combined effect-image review with [references/mockup-review-rubric.md](references/mockup-review-rubric.md). Use Apple Human Interface Guidelines as the interaction baseline, then report product-design issues and premium-feel improvements in separate sections; do not run a second aesthetic-only review.
6. Select one direction or combine explicit traits from multiple directions.
7. If the selected page has interaction ambiguity that a static effect image cannot resolve, use `@product-design image-to-code` to create a review-only interactive prototype. Do not treat this prototype as Flutter implementation code or as a substitute for Pencil restoration.
8. Freeze implementation constraints with [references/design-freeze-template.md](references/design-freeze-template.md).
9. For a page-level implementation target, before visual-asset work or Pencil restoration, classify each restorable layer or atomic unit as bitmap, UI, or data; split composite elements before classification. Use placeholders only for data while preserving hierarchy, text length, and layout. For UI, record whether native Flutter can reproduce it exactly and require a bitmap fill only when it cannot.
10. If the analysis identifies required bitmaps or bitmap fills, use `flutter-asset-atlas` to create reuse checks, production decisions, product-design or image generation outputs when new bitmaps are needed, background transparentization when needed, slicing/export manifest, inventory, and fidelity review under global and page design-freeze constraints. Otherwise record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
11. If editable design handoff is required for the page task, use `flutter-pencil-design` to restore the approved page direction in Pencil after the analysis and either required asset atlas evidence or the no-bitmap `N/A` record exist.
12. Hand off the frozen constraints, effect-image analysis, asset evidence, optional Product Design prototype, and optional Pencil restoration to `flutter-ux-ui-quality` and the implementation task.

## Output Files

- `docs/design/mockup-brief.md`
- `docs/design/mockup-review.md`
- `docs/design/global-design-freeze.md` for global visual direction
- `docs/design/asset-atlas.md` when visual asset exports are required
- `docs/design/asset-slicing-manifest.md` when visual asset exports are required
- `docs/design/asset-fidelity-review.md` when visual asset exports are required
- `docs/design/asset-inventory.md` when visual assets are present
- `docs/design/design-freeze.md`
- `docs/design/pencil-hifi-restoration.md` for page-level implementation targets
- mockup image paths recorded in `.codex-workflow/progress.md`

For multiple pages, use page-scoped paths such as `docs/design/pages/<page-name>/design-freeze.md` and keep the same contracts.

## Generation Rules

- Generate every high-fidelity effect image at exactly `780 x 1688 px`, and verify the decoded file dimensions before review or selection.
- Use `@product-design ideate` as the visual-direction owner; do not generate more or fewer than its three reviewable directions before selection.
- Generate screen-specific mockups, not generic mood boards.
- Do not use global direction mockups as page implementation approval.
- Generate page-level mockups close to implementation time so they reflect the current task scope and Flutter constraints.
- For module page work, generate the high-fidelity effect image after low-fidelity Pencil structure has passed Wireframe Review.
- Include realistic app content, not filler names or fake vanity metrics.
- Use mockups to confirm UX/UI hierarchy, density, visual direction, and interaction intent before relying on text specs.
- Keep platform feasibility in mind: Flutter Material 3, custom tokens, normal widget composition.
- Cover the most important state first; generate secondary states when they affect layout or trust.
- Do not treat an image as implementation truth until it is reviewed and converted into design-freeze constraints.
- Convert global visual direction into `docs/design/global-design-freeze.md` before module/page asset generation depends on it.
- Do not send required visual assets to Pencil or Flutter until `flutter-asset-atlas` has recorded reuse check, production decision, background handling, background transparentization when applicable, source or generation evidence, slicing/export, Flutter path, license, fallback, and fidelity evidence.
- Treat product-design or image generation tools as the default source for new bitmap assets. Pencil export is valid only when the approved Pencil node is itself the production asset, not a whole-page screenshot or low-fidelity structure.
- Do not generate assets from the page mockup alone; asset prompts must use the global design freeze and page design freeze.
- If Pencil is used later, allow it to carry page-level high-fidelity visual restoration only after the selected page mockup is reviewed and converted into `design-freeze.md`.
- Treat every required bitmap or illustration as an asset with source, license, format, Flutter path, and fidelity requirements.

## Gate

Do not generate page-level high-fidelity mockups for module work until low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md` exist. Do not treat global visual direction as page implementation approval. Do not approve a generated effect image unless its decoded file dimensions are exactly `780 x 1688 px` and its selected direction is recorded from the three-direction `@product-design ideate` review. Do not approve UX/UI or start Flutter UI implementation for a high-value screen until a selected page-level high-fidelity effect image or an explicit "no mockup needed" decision is recorded. Before visual-asset work or Pencil restoration, a page-level implementation target must classify its restorable layers or atomic units as bitmap, UI, or data and record the native-Flutter feasibility of each UI unit. If the analysis identifies required bitmaps or bitmap fills, `docs/design/asset-atlas.md`, `docs/design/asset-slicing-manifest.md`, `docs/design/asset-inventory.md`, and `docs/design/asset-fidelity-review.md` are required; generated assets must reference global and page design-freeze constraints, and non-transparent sources that must be composited must pass the background transparentization work node. Otherwise, record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
