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
- Reviewed low-fidelity Pencil structure and `docs/design/pages/<page-name>/wireframe-spec.md` for page-level module work.
- Brand constraints or references, if available.
- Target device class: phone, tablet, or responsive set.
- Required states: success, loading, empty, error, disabled, permission, paywall.
- First-value moment, safe-to-try conditions, and trust evidence when the screen is part of first-time adoption.

## Workflow

1. Classify the mockup as global direction or page-level implementation target.
2. For page-level module work, confirm `docs/design/pages/<page-name>/wireframe-spec.md` exists before writing the mockup brief.
3. Draft a mockup brief for the current module or page with [references/mockup-brief-template.md](references/mockup-brief-template.md), including the active visual expression preset, page-type budget dial, and whether a restatable signature moment is required. Keep this brief, the formal prompt, and all candidate images transient in the current conversation; do not write visual workflow files yet.
4. Confirm the product brief, market analysis, and screen constraints identify the design target and intended user outcome. Use the available image-generation capability to generate exactly three visual directions for the same screen or flow. Do not require an external visual-design skill; if image generation is unavailable, record `BLOCKED: image generation unavailable` and do not fabricate image evidence.
5. Run exactly one combined effect-image review with [references/mockup-review-rubric.md](references/mockup-review-rubric.md). Use Apple Human Interface Guidelines as the interaction baseline, then report product-design issues and premium-feel improvements in separate sections; judge premium feel against the active visual expression preset’s signature strength and wow requirement, not universal restraint; do not run a second aesthetic-only review.
6. Present the candidate set and review in the conversation, then wait for the user's explicit selection and freeze confirmation. Do not write, copy, move, or register any candidate image or visual-workflow artifact before this confirmation.
7. After confirmation, persist the exact selected image first under `.codex-workflow/visuals/<scope>/frozen-<slug>.png` (`<scope>` is `global` or `pages/<page-name>`). Then write the mockup brief, formal prompt, applicable design-freeze, and progress-ledger entries in the same freeze operation; record the frozen path, source candidate ID, decoded dimensions, SHA-256, and confirmation time. Never transform the selected image while freezing it.
8. If the selected page has interaction ambiguity that a static effect image cannot resolve, create a review-only local prototype when the environment provides a suitable implementation tool. Do not treat this prototype as Flutter implementation code or as a substitute for Pencil restoration.
9. Freeze implementation constraints with [references/design-freeze-template.md](references/design-freeze-template.md), referencing only the persisted frozen image.
9. For a page-level implementation target, before visual-asset work or Pencil restoration, classify each restorable layer or atomic unit as bitmap, UI, or data; split composite elements before classification. Restore data only as editable text or representative placeholders while preserving hierarchy, text length, and layout; data must never trigger bitmap generation or extraction. Record every unresolved visual fact with its affected unit, evidence, decision needed, and whether it blocks approval or Flutter handoff; do not guess asset provenance, font or icon sources, component states, crop rules, or hidden interactions. For UI, record whether native Flutter can reproduce it exactly and require a bitmap fill only when it cannot.
10. If the analysis identifies required bitmaps or bitmap fills, use `flutter-asset-atlas` to create reuse checks, production decisions, image-generation outputs when new bitmaps are needed, background transparentization when needed, slicing/export manifest, inventory, and fidelity review under global and page design-freeze constraints. Otherwise record `N/A: no bitmap or exported visual assets` in the task brief and task evidence manifest.
11. If editable design handoff is required for the page task, use `flutter-pencil-design` to restore the approved page direction in Pencil after the analysis and either required asset atlas evidence or the no-bitmap `N/A` record exist.
12. Hand off the frozen constraints, effect-image analysis, asset evidence, optional review-only prototype, and optional Pencil restoration to `flutter-ux-ui-quality` and the implementation task.

## Output Files

- `docs/design/global/mockup-brief.md` and `docs/design/global/design-freeze.md` for global visual direction, after freeze
- `docs/design/pages/<page-name>/mockup-brief.md` and `docs/design/pages/<page-name>/design-freeze.md` after a page freeze
- `docs/design/pages/<page-name>/asset-atlas.md`, `asset-slicing-manifest.md`, `asset-fidelity-review.md`, and `asset-inventory.md` when page visual assets are required
- `docs/design/pages/<page-name>/pencil-hifi-restoration.md` for page-level implementation targets
- frozen mockup images under `.codex-workflow/visuals/global/` or `.codex-workflow/visuals/pages/<page-name>/`, with their paths recorded in `.codex-workflow/progress.md`

For multiple pages, use page-scoped paths such as `docs/design/pages/<page-name>/design-freeze.md` and keep the same contracts.

## Generation Rules

- Generate every high-fidelity effect image at exactly `780 x 1688 px`, and verify the decoded file dimensions before review or selection.
- Treat generated candidates, draft briefs, prompts, and review output as transient until the user explicitly confirms the freeze. The first repository write for a confirmed visual must be the exact frozen image in `.codex-workflow/visuals/`; write its associated documents only after that copy succeeds.
- Use the available image-generation capability as the visual-direction owner; do not generate more or fewer than three reviewable directions before selection, and never require an external product-design skill.
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
- Convert global visual direction into `docs/design/global/design-freeze.md` before module/page asset generation depends on it.
- Do not send required visual assets to Pencil or Flutter until `flutter-asset-atlas` has recorded reuse check, production decision, background handling, background transparentization when applicable, source or generation evidence, slicing/export, Flutter path, license, fallback, and fidelity evidence.
- Treat the available image-generation capability as the default source for new bitmap assets. Pencil export is valid only when the approved Pencil node is itself the production asset, not a whole-page screenshot or low-fidelity structure.
- Do not generate assets from the page mockup alone; asset prompts must use the global design freeze and page design freeze.
- If Pencil is used later, allow it to carry page-level high-fidelity visual restoration only after the selected page mockup is reviewed and converted into the page-scoped `design-freeze.md`.
- Treat every required bitmap or illustration as an asset with source, license, format, Flutter path, and fidelity requirements.
- Do not simplify global exploration to avoid downstream asset work. Record asset cost and risk after exploration, then let the user choose whether the visual value justifies them.

## Gate

- Do not generate a page-level high-fidelity mockup until low-fidelity Pencil structure, Wireframe Review, and `docs/design/pages/<page-name>/wireframe-spec.md` exist.
- Do not treat global visual direction as page implementation approval. Start global exploration only after the product brief records the derived visual expression preset and the one-time light visual interrogation commitments.
- Generate exactly three directions with the available image-generation capability. Do not require an external visual-design skill; if the capability is unavailable, record a blocker instead of inventing image evidence.
- Do not write a candidate image before explicit freeze confirmation. After confirmation, persist the exact selected image under `.codex-workflow/visuals/<scope>/` before writing related documents; record candidate ID, dimensions, SHA-256, confirmation time, prompt hash, and review verdict in the task visual-decision record.
- Do not approve a generated effect image unless it is exactly `780 x 1688 px`, satisfies the preset direction mix, has the active preset and page-type budget dial in its brief, and passes the combined Effect Image Review.
- On full-budget or wow-required pages, do not approve a mockup that lacks a restatable signature unless the user explicitly accepts the gap. Do not start Flutter UI implementation for a high-value screen until a selected page-level effect image or an explicit `no mockup needed` decision exists.
- Before visual-asset work or Pencil restoration, classify each restorable unit as bitmap, UI, or data and record native-Flutter feasibility for each UI unit. When bitmaps or bitmap fills are required, write their page-scoped asset atlas, slicing manifest, inventory, and fidelity review; otherwise record `N/A: no bitmap or exported visual assets` in the task brief and evidence manifest.
