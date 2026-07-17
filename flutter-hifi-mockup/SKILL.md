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
- First-value moment, safe-to-try conditions, and trust evidence when the screen is part of first-time adoption.

## Workflow

1. Classify the mockup as global direction or page-level implementation target.
2. For page-level module work, confirm `docs/design/wireframe-spec.md` exists before writing the mockup brief.
3. Draft a mockup brief for the current module or page with [references/mockup-brief-template.md](references/mockup-brief-template.md), including the active visual expression preset, page-type budget dial, and whether a restatable signature moment is required. Keep this brief, the formal prompt, and all candidate images transient in the current conversation; do not write visual workflow files yet.
4. Confirm `@product-design user-context` preflight has completed, then use `@product-design get-context` to confirm the design target and intended user outcome. Use `@product-design ideate` to generate exactly three visual directions for the same screen or flow.
5. Run exactly one combined effect-image review with [references/mockup-review-rubric.md](references/mockup-review-rubric.md). Use Apple Human Interface Guidelines as the interaction baseline, then report product-design issues and premium-feel improvements in separate sections; judge premium feel against the active visual expression preset’s signature strength and wow requirement, not universal restraint; do not run a second aesthetic-only review.
6. Present the candidate set and review in the conversation, then wait for the user's explicit selection and freeze confirmation. Do not write, copy, move, or register any candidate image or visual-workflow artifact before this confirmation.
7. After confirmation, persist the exact selected image first under `.codex-workflow/visuals/<scope>/frozen-<slug>.png` (`<scope>` is `global` or `pages/<page-name>`). Then write the mockup brief, formal prompt, applicable design-freeze, and progress-ledger entries in the same freeze operation; record the frozen path, source candidate ID, decoded dimensions, SHA-256, and confirmation time. Never transform the selected image while freezing it.
8. If the selected page has interaction ambiguity that a static effect image cannot resolve, use `@product-design image-to-code` to create a review-only interactive prototype. Do not treat this prototype as Flutter implementation code or as a substitute for Pencil restoration.
9. Freeze implementation constraints with [references/design-freeze-template.md](references/design-freeze-template.md), referencing only the persisted frozen image.
9. For a page-level implementation target, before visual-asset work or Pencil restoration, classify each restorable layer or atomic unit as bitmap, UI, or data; split composite elements before classification. Restore data only as editable text or representative placeholders while preserving hierarchy, text length, and layout; data must never trigger bitmap generation or extraction. Record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess asset provenance, font or icon sources, component states, crop rules, or hidden interactions. For UI, record whether native Flutter can reproduce it exactly and require a bitmap fill only when it cannot.
10. If the analysis identifies required bitmaps or bitmap fills, use `flutter-asset-atlas` to create reuse checks, production decisions, product-design or image generation outputs when new bitmaps are needed, background transparentization when needed, slicing/export manifest, inventory, and fidelity review under global and page design-freeze constraints. Otherwise record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
11. If editable design handoff is required for the page task, use `flutter-pencil-design` to restore the approved page direction in Pencil after the analysis and either required asset atlas evidence or the no-bitmap `N/A` record exist.
12. Hand off the frozen constraints, effect-image analysis, asset evidence, optional Product Design prototype, and optional Pencil restoration to `flutter-ux-ui-quality` and the implementation task.

## Output Files

- `docs/design/mockup-brief.md` after freeze
- `docs/design/global-design-freeze.md` for global visual direction, after freeze
- `docs/design/asset-atlas.md` when visual asset exports are required
- `docs/design/asset-slicing-manifest.md` when visual asset exports are required
- `docs/design/asset-fidelity-review.md` when visual asset exports are required
- `docs/design/asset-inventory.md` when visual assets are present
- `docs/design/design-freeze.md` after freeze
- `docs/design/pencil-hifi-restoration.md` for page-level implementation targets
- frozen mockup images under `.codex-workflow/visuals/global/` or `.codex-workflow/visuals/pages/<page-name>/`, with their paths recorded in `.codex-workflow/progress.md`

For multiple pages, use page-scoped paths such as `docs/design/pages/<page-name>/design-freeze.md` and keep the same contracts.

## Generation Rules

- Generate every high-fidelity effect image at exactly `780 x 1688 px`, and verify the decoded file dimensions before review or selection.
- Treat generated candidates, draft briefs, prompts, and review output as transient until the user explicitly confirms the freeze. The first repository write for a confirmed visual must be the exact frozen image in `.codex-workflow/visuals/`; write its associated documents only after that copy succeeds.
- Use `@product-design ideate` as the visual-direction owner; do not generate more or fewer than its three reviewable directions before selection.
- Generate screen-specific mockups, not generic mood boards.
- Do not use global direction mockups as page implementation approval.
- Generate page-level mockups close to implementation time so they reflect the current task scope and Flutter constraints.
- For module page work, generate the high-fidelity effect image after low-fidelity Pencil structure has passed Wireframe Review.
- Include realistic app content, not filler names or fake vanity metrics.
- Use mockups to confirm UX/UI hierarchy, density, visual direction, and interaction intent before relying on text specs.
- Separate visual exploration from implementation assessment. During global-direction exploration, optimize first for product character, compositional distinction, emotional energy, and task clarity according to the derived visual expression preset; enforce the preset’s three-direction mix; do not reject a direction merely because it needs custom widgets, `CustomPainter`, shaders, animation, or dedicated bitmap assets.
- After a direction is selected, record a credible Flutter implementation path for each distinctive treatment: native widget, authored component, custom painting, shader or animation, or bitmap asset. Treat implementation complexity as an explicit tradeoff for user review, not an automatic rejection criterion.
- Use Apple Human Interface Guidelines and iOS conventions as interaction, accessibility, and semantic foundations rather than a visual ceiling. A brand-led component language may depart from stock Cupertino component appearance when the departure is intentional and implementable.
- Cover the most important state first; generate secondary states when they affect layout or trust.
- For first-run, onboarding, paywall, permission, or data-import screens, make the expected value, risk, and recovery path visible before relying on visual polish.
- Do not treat an image as implementation truth until it is reviewed and converted into design-freeze constraints.
- Convert global visual direction into `docs/design/global-design-freeze.md` before module/page asset generation depends on it.
- Do not send required visual assets to Pencil or Flutter until `flutter-asset-atlas` has recorded reuse check, production decision, background handling, background transparentization when applicable, source or generation evidence, slicing/export, Flutter path, license, fallback, and fidelity evidence.
- Treat product-design or image generation tools as the default source for new bitmap assets. Pencil export is valid only when the approved Pencil node is itself the production asset, not a whole-page screenshot or low-fidelity structure.
- Do not generate assets from the page mockup alone; asset prompts must use the global design freeze and page design freeze.
- If Pencil is used later, allow it to carry page-level high-fidelity visual restoration only after the selected page mockup is reviewed and converted into `design-freeze.md`.
- Treat every required bitmap or illustration as an asset with source, license, format, Flutter path, and fidelity requirements.
- Do not simplify global exploration to avoid downstream asset work. Record asset cost and risk after exploration, then let the user choose whether the visual value justifies them.

## Gate

Do not generate page-level high-fidelity mockups for module work until low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md` exist. Do not treat global visual direction as page implementation approval. Do not start global visual exploration until the product brief records a derived visual expression preset and the one-time light visual interrogation answers are recorded in the grilling log with commitments mirrored in the product brief. Do not approve a global direction set unless the three directions satisfy the active preset’s required direction mix. When the Global Freeze Signature Rule applies, do not freeze a selected direction without an explicit restatable-signature confirmation; if the answer is no, iterate. Do not write a candidate effect image, mockup brief, formal prompt, review, design freeze, or progress-ledger visual entry to the repository before explicit freeze confirmation. After confirmation, the exact selected image must be persisted under `.codex-workflow/visuals/<scope>/` before any related document is written, and the freeze record must include its candidate ID, dimensions, SHA-256, and confirmation time. Do not approve a generated effect image unless its decoded file dimensions are exactly `780 x 1688 px`, its selected direction is recorded from the three-direction `@product-design ideate` review, the mockup brief records the active expression preset and page-type budget dial, and the combined Effect Image Review judged premium feel against that preset rather than universal restraint. On full-budget or wow-required pages, do not approve a page mockup that lacks a restatable signature unless the user explicitly accepts the gap. Do not approve UX/UI or start Flutter UI implementation for a high-value screen until a selected page-level high-fidelity effect image or an explicit "no mockup needed" decision is recorded. Before visual-asset work or Pencil restoration, a page-level implementation target must classify its restorable layers or atomic units as bitmap, UI, or data and record the native-Flutter feasibility of each UI unit. If the analysis identifies required bitmaps or bitmap fills, `docs/design/asset-atlas.md`, `docs/design/asset-slicing-manifest.md`, `docs/design/asset-inventory.md`, and `docs/design/asset-fidelity-review.md` are required; generated assets must reference global and page design-freeze constraints, and non-transparent sources that must be composited must pass the background transparentization work node. Otherwise, record `N/A: no bitmap or exported visual assets` in the task brief and progress ledger.
