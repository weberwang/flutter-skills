# Creative Production Branch

Use this reference when the workflow needs commercial creative exploration, campaign visuals, reviewable asset packs, or publish-safe polish without weakening the Product Design and Flutter implementation gates.

## Purpose

This branch integrates `Creative Production` as the standard `creative -> production -> polish` lane inside the broader Flutter workflow.

It exists to handle asset-oriented work such as:

- campaign direction
- mood boards
- ad concepts
- offer-led visual routes
- scene exploration
- logo exploration
- shot variants
- launch visuals
- social cards
- landing hero directions
- publish-safe generative polish

It does not replace Product Design, image-backed design-packet normalization, HTML interactive prototype generation, shared freeze, module freeze, architecture, or Flutter implementation.

## Ownership Split

Keep ownership explicit:

- `@product-design` owns product-surface brief confirmation, screen-level direction, interactive UX, and the final product design direction that feeds `DESIGN.md`.
- `Creative Production` owns commercial visual exploration, asset-family exploration, reviewable image boards, and publish-bound creative asset finishing.
- Image-backed design-packet normalization owns the downstream Flutter-facing freeze-packet normalization when approved direction and evidence still need to be standardized before shared or module freeze.
- The HTML interactive prototype flow owns prototype-derived design-source restoration after `DESIGN.md` is confirmed.
- `generative-polish` owns bounded visual finish only after a concrete direction or deterministic base already exists.

Do not blur these roles. If the user is choosing how the app itself should behave, route through Product Design. If the user is choosing how a campaign, ad family, hero image, or brand-facing visual system should look, route through Creative Production.

## Entry Gate

This branch now has two valid entry windows.

### Window A: Direction Input Branch

Use this branch before the final product direction is locked when the workflow needs richer creative evidence to help choose the direction.

Preferred prerequisites:

- PRD exists
- technical baseline exists
- Product Design brief is confirmed
- the branch is being used to inform direction rather than to override product-surface UX

Typical outputs:

- mood boards
- ad routes
- offer-led hero directions
- scene territories
- logo territories

This window should feed back into Product Design direction confirmation. It must not silently become the final product direction by itself.

### Window B: Asset Production Branch

The preferred entry point is after:

- PRD exists
- technical baseline exists
- Product Design brief is confirmed when product-surface alignment matters
- final product design direction is confirmed when the asset branch must inherit the app or product visual system
- `DESIGN.md` exists when the assets must inherit the frozen visual system

If the user only wants broad campaign or brand exploration and the branch does not need to redefine product-surface UX, the workflow may enter Creative Production before HTML interactive prototype work. Even in that case, the branch must not redefine the app-shell, interaction logic, or screen hierarchy owned by Product Design.

## Direction Input Branch

Use this sequence when Creative Production is feeding into product-direction choice:

1. Normalize the creative brief.
2. Route into `Creative Production:explore`.
3. Select one focused explorer.
4. Generate reviewable direction evidence.
5. Return to Product Design direction confirmation with the new evidence.

Do not move directly from this branch into publish-bound polish unless the workflow explicitly shifts into the asset-production branch.

## Asset Production Branch

Use this sequence as the default implementation of the post-`DESIGN.md` production branch:

1. Normalize the creative brief.
   - Confirm product or offer, audience, goal, market, channels, brand constraints, and avoid-list.
2. Route into `Creative Production:explore`.
   - Use it as the path chooser, not as the final deliverable.
3. Select one focused explorer.
   - `moodboard-explorer` for visual territories.
   - `ads-explorer` for ad directions.
   - `offer-explorer` for hero or offer-led variations.
   - `scene-explorer` for real-world usage context.
   - `shot-explorer` for angle or crop variants.
   - `logo-explorer` for identity concepts.
4. Confirm one creative direction.
   - Do not enter publish polish while the direction is still ambiguous.
5. Produce reviewable assets.
   - Save durable outputs, manifests, and review surfaces.
6. Apply `generative-polish` only when exact output constraints are known.
   - Preserve text, logos, dimensions, charts, data, safe zones, and filenames deterministically.
7. Hand off or archive.
   - Return exported assets plus manifest plus review surface, or feed approved visual evidence back into the broader workflow where appropriate.

## Artifact Contract

The branch should create durable review artifacts rather than chat-only descriptions.

Preferred outputs include:

- reviewable board or gallery
- saved run directory
- exported image set
- manifest
- concise handoff notes
- review risks and validation notes

If publish-bound outputs exist, keep exact text, logos, charts, pricing, and dimensions outside the generative layer whenever possible.

## Relationship To The Main Flutter Flow

This branch is optional and scope-driven.

- For app UI direction, Product Design remains mandatory.
- For direction-input exploration before final product confirmation, Creative Production can supply evidence but cannot close the product-direction gate on its own.
- If the broader workflow still needs one freeze-ready Flutter design packet, route the approved Product Design direction plus any Creative Production evidence back through image-backed design-packet normalization instead of treating Creative Production output as the final packet.
- For Flutter preview images used as supplemental app-page evidence, `gpt-image-2-generator` remains the default preview-image owner unless the user explicitly wants the richer Creative Production asset branch.
- Creative Production outputs may be attached as supplemental visual evidence, but they are never the implementation design source by themselves.
- Mood boards, ads, scenes, or hero explorations do not automatically authorize HTML prototype freeze.
- If a Creative Production run reveals a new visual direction that materially changes the confirmed product direction, return to Product Design direction confirmation and update `DESIGN.md` before downstream freeze.

## Publish Gate

Before any publish-bound asset is considered complete, verify:

- exact copy is deterministic
- logos and marks are approved
- dimensions and placements are correct
- review status is explicit
- generative layers did not rewrite critical claims
- provenance is clear when required

If any of those conditions fail, keep the branch in revision rather than marking the asset output complete.
