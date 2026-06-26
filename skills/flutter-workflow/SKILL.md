---
name: flutter-workflow
description: Use when coordinating a Flutter product workflow across idea intake, requirements, PRD, technical baseline, Product Design brief, reference-image effect images, UI atlas preparation, Pencil design source, shared/module design freeze, module impl docs, native HTML prototype confirmation, Pencil-to-Flutter restoration, architecture, display restoration blueprint, implementation readiness, QA, human visual inspection, workflow state, or when the user asks what stage should happen next.
---

# Flutter Workflow

## Overview

Route a Flutter module through rough idea intake -> idea-sketch brainstorming -> requirements brainstorming -> PRD document generation -> global technical baseline -> target design-device preset, design viewport, and image output scale confirmation -> `@product-design` brief confirmation -> Mobbin-backed global theme and style scheme selection -> `DESIGN.md` output for theme, hierarchy, public shell, component family, and interaction principles only -> shared freeze -> early project initialization plus bootstrap preparation -> module `impl.md` generation under frozen design and interaction principles -> mandatory native HTML module prototype confirmation -> mandatory module Pencil design source confirmation -> implementation RD readiness -> architecture -> display restoration blueprint readiness -> implementation workflow -> Flutter render versus frozen-design QA -> `@product-design` design QA -> human visual inspection -> post-implementation visual enhancement pass when needed, including effect images, atlas preparation, atlas slicing, Pencil reinforcement, and bitmap assets only after all target modules have already completed their primary functional implementation.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow truth model for the whole project. When persistence is needed for a live run, it may serialize that state into runtime artifacts, but those artifacts are not part of the stable skill bundle.

On the first call for a target project root, run a lightweight git preflight before any downstream routing: check whether `.git/` already exists, whether `git status` is readable in that root, and whether a root `.gitignore` baseline already exists. If any of those repository-baseline pieces are missing, keep that finding in the route context and let `flutter-init` own the actual `git init` plus `.gitignore` creation or repair.

In manual mode, pause at confirmation gates after one stage or one module reaches a reviewable milestone. In `--auto` mode, behave as a full-module advancement loop across the whole target module set, auto-confirm ordinary orchestrator-owned stage and status promotions after receipt validation, and keep executing one serial module step after another until every target module is implemented or a real blocker appears, rather than opening parallel module lanes. In `--full-auto` mode, keep the same serial advancement loop but also auto-confirm deterministic human-facing workflow gates when one default is uniquely justified by existing artifacts. That expanded auto-confirm scope includes Product Design brief confirmation, public-shell confirmation, final product direction confirmation, and primary-platform device selection when the control contracts say the default target is unique. If the choice is still ambiguous, the workflow must stop and record a blocker instead of inventing certainty.

The global design output is a frozen `global_style_scheme`, one optional reviewable `global_style_experience_image`, and `DESIGN.md`, not a page design draft. `@product-design` still owns the design-side kickoff: brief confirmation, direction framing, visual-target selection, Mobbin-backed reference judgment, and the commercial product UI/UX bar. The shared/global flow must select one fixed style direction, one theme system, one hierarchy contract, one public shell posture, one component-family contract, one minimal-copy contract, and one shared interaction-principle contract. It must set `theme_and_style_only=true`, `no_global_page_design_draft=true`, `non_page_design_evidence=true` for the global style experience image when present, and `page_design_deferred_to_module_stage=true`. Before any module page-generation step is allowed to begin, the workflow must already lock a commercial product creation packet through the confirmed brief and the active module contract: `surface_goal=commercial_product_app`, one `primary_task`, one dominant `primary_cta`, `first_screen_required_information`, `defer_or_collapse_content`, `information_density_posture`, `copy_posture=minimal`, and `disallowed_surface_modes=[marketing_page, explanatory_mock, poster_layout, slogan_first_layout, concept_art]`. All page-level HTML prototypes, module final effect images, atlas bundles, and Pencil page designs belong to module scope after the active module `impl.md` fixes function, the primary task path, and non-display behavior boundaries. The workflow default is to plan only the primary page or primary surface for each module; any additional `error`, `empty`, `loading`, permission, or other page-local states must be appended later only after explicit human confirmation. In the default module loop, the native HTML prototype is the static layout gate before architecture and first-pass implementation work, and the initial module version should restore the design with Flutter SDK standard capabilities plus platform HIG-aligned interaction constraints before any effect-image, atlas, slicing, Pencil, or bitmap-asset workflow is opened. Every workflow-generated image that enters evidence or downstream consumption must pass manual image review and leave a human review result before the workflow asks for confirmation, promotes the next stage, or consumes that image as a frozen baseline. If an image-generation step fails and the workflow retries it, the retry prompt must preserve the full original prompt plus all frozen visual constraints; do not shorten, simplify, or drop prompt detail as the retry mechanism. Tool-native defaults, hidden heuristics, or internal style opinions are not valid guidance sources. After any module freeze is confirmed, delete previously generated but no-longer-selected effect images from the corresponding workflow artifact directories and indexes so later routing cannot accidentally reuse stale alternatives.

Use `Product Design:ideate` as the default design-controller-owned path for direction images. In this workflow, that means the shared/global `global_style_experience_image` and the later module final effect-image direction pass should stay under Product Design ideation and QA control before they become frozen evidence. The module final effect image must select or revise a Product Design-generated candidate before it is frozen as the chosen baseline. After atlas extraction analysis is confirmed, atlas generation may also use `Product Design:ideate` to render the solid-background atlas image from the approved cell plan. Keep atlas slicing on the existing deterministic asset path. Atlas background removal is optional and should run only when transparent atlas output is actually needed by the later visual-enhancement evidence chain.

## Global Style-Only Design Boundary

Global design freezes a `global_style_scheme`, not page design drafts. Set `theme_and_style_only=true`, `no_global_page_design_draft=true`, and `page_design_deferred_to_module_stage=true` for shared/global visual work.

- The global stage may define palette posture, typography posture, density posture, surface depth, component family, CTA posture, icon or image treatment, hierarchy rules, motion restraint, copy posture, public-shell principles, and reusable theme tokens.
- The global stage must use Mobbin references as mandatory style evidence, but those references only justify the selected theme and fixed visual language. They must not become page-level layout sources, generated screen drafts, or hidden page comps.
- The global stage may include one `global_style_experience_image` to make the selected style direction visually reviewable. It must be a non-page visual mood preview for theme, hierarchy, density, surface depth, and component feel, with `non_page_design_evidence=true`; it must not show a complete app screen, page flow, final layout, exportable asset atlas, or Pencil-ready page design.
- The global stage must not generate page-level HTML prototypes, representative page sketches, final effect images, page-level Pencil files, atlas bundles, or shared page design drafts. Any older shared/global wording that requests those artifacts is superseded by this boundary.
- Page design belongs to the module stage after the active module `impl.md` fixes function, the primary task path, and behavior boundaries. The default planning target is the primary page only, and additional page states may be appended later only after explicit human confirmation. Only then may the workflow generate module HTML, module effect images, module atlas evidence, and module Pencil design source.
- `DESIGN.md` at the global stage records the theme and style scheme, strong hierarchy contract, minimal-copy contract, public-shell rules, component-family rules, and interaction principles. It must avoid page-specific screen comps or explanatory page mockups, while still forcing downstream module creation to inherit a commercial-product-first posture, task-first hierarchy, dominant CTA rule, and copy-minimization rule from the start instead of after prototype review.

## Artifact Necessity Boundary

Do not treat every workflow artifact as a hard gate. The workflow distinguishes between required artifacts, optional review aids, conditional implementation evidence, and legacy-only non-authoritative evidence.

- Required shared/global artifacts:
  `global_style_scheme` and `DESIGN.md` are the shared/global freeze requirements. They are the authoritative output of the current global style-only route.
- Optional shared/global artifacts:
  `global_style_experience_image` is optional. It may help human review of the selected style direction, but the shared/global freeze must not depend on it.
- Forbidden-as-required shared/global artifacts:
  shared/global page-level HTML prototypes, page-sketch drafts, final effect images, atlas bundles, Pencil page files, and shared page comps must not become required inputs for the current shared/global freeze.
- Removed legacy evidence states:
  the old shared/global legacy states for shared HTML prototype, global effect-image pilot, and shared asset resources are no longer part of the current workflow state model. Do not reintroduce them as compatibility aliases.
- Module-scoped image evidence naming:
  module image-evidence progress must use module-scoped state names instead of carrying the old `global_effect_images_ready` label forward.
- Required module-stage artifacts:
  for the initial implementation pass, the required path is the module `impl.md`, confirmed native `HTML/CSS/JS` prototype, mandatory Pencil design source, architecture output, and display restoration blueprint. Implementation-stage effect-image evidence and atlas chain belong to the later visual-enhancement path only when the project still needs them after all target modules have already reached complete primary functionality.
- Conditional module artifacts:
  `display_evidence_pack_ready` is required only when the page is fidelity-sensitive enough that later restoration would otherwise have to guess. Additional standalone bitmap assets are required only when atlas slices and code restoration are still insufficient after Pencil review.
- Optional post-direction branches:
  the pre-direction or post-direction `Creative Production` branch is optional enrichment. It must not replace the authoritative product-direction and design-source chain.

## Idea Sketch Brainstorming Boundary

The `idea_sketch_brainstorming` stage exists to turn rough product intent into something concrete enough for PRD work.

- Use this stage when the user has only a rough idea, a few references, or abstract goals that are still hard to reason about as pages.
- The stage must brainstorm the product direction, collapse the core task path, and generate `1-3` key-page sketches that make the main flow visible.
- Those sketches confirm product direction, page structure, and broad visual style only. They are not a design freeze, not the later module final effect-image generation stage, and not a substitute for `DESIGN.md`.
- Before leaving this stage, write a lightweight `docs/project/idea-sketch-brief.md` artifact that captures the confirmed idea summary, key pages, broad style direction, and the questions that still belong to PRD.
- Do not let this stage jump straight to technical baseline, Product Design brief confirmation, shared freeze, architecture, or implementation planning. It exists to make the idea concrete enough for the downstream PRD flow, not to bypass that flow.

## Asset Resource Boundary

The asset-resource stage exists to turn approved page imagery into reusable single bitmap assets after Pencil design review has confirmed what still truly needs image generation.

- Use this stage only after the current shared or module Pencil design source has already completed compare, confirmed repair scope, and human acceptance.
- Use this stage only when the confirmed Pencil review result still shows visual regions that cannot be restored faithfully enough in code and therefore require bitmap assets that stay very close to the approved effect image.
- “Restored faithfully enough in code” means the region can be recreated with Flutter SDK standard capabilities alone, without adding new bitmap assets, while still remaining close enough to the approved effect image in structure, shape, color, spacing, shadow, and overall visual character.
- Flutter SDK standard capabilities here include normal layout primitives, `Container`, `BoxDecoration`, borders, border radius, box shadows, gradients, text styles, standard icons, clipping, and other built-in drawing primitives such as `CustomPaint` when they can still preserve the intended look without bitmap assistance.
- Always maintain one project-wide asset catalog at `docs/project/assets/global-asset-catalog.json` before deciding whether a new bitmap asset should be generated again.
- The asset catalog is also the mandatory generated-image record table. Every workflow-generated final effect image, implementation-stage module effect image, matching atlas files plus manifests, shared bitmap asset, and module bitmap asset that enters workflow evidence or downstream consumption must be written into that catalog in the same workflow step.
- Every workflow-generated image that enters workflow evidence or downstream consumption must also leave one manual image review record in the same workflow step or immediately after it, before later confirmation or freeze work continues.
- Asset reuse decisions must be based on `name`, `semantic`, and `usage_scenarios`, not only on filename similarity. If the workflow cannot safely decide whether an existing asset can be reused, mark it as `candidate_reuse` and stop for confirmation.
- Before any bitmap asset calls `$imagegen`, the workflow must first check `docs/project/assets/global-asset-catalog.json` plus the already-approved output files referenced by that catalog. If an approved reusable image already exists for the same semantic and usage scenario, reuse it directly and skip generation.
- If an image region is only a schematic placeholder and its real content must be created later from runtime data, keep it as a placeholder contract instead of generating a bitmap asset. Placeholder-only regions must not enter image generation.
- The resource generation unit may be one approved atlas-slice asset or one approved standalone bitmap resource. A shared resource lives under `docs/project/assets/shared/<page-name>/`, and a module resource lives under `docs/project/modules/<module>/assets/<page-name>/`. When the accepted atlas-slice outputs already satisfy the runtime contract, they count as final approved resource files and do not need to be regenerated as separate bitmaps.
- By default, one page's resource planning should cover only the primary surface for the confirmed main task path. Additional resources for `error`, `empty`, `loading`, and other page-local states may be appended later only after explicit human confirmation, and the workflow must not regenerate already approved reusable assets from other pages.
- After the workflow excludes code-restorable regions, `placeholder_only` regions, confirmed reusable assets, and any regions whose post-review Pencil adjustments made bitmap generation unnecessary, it must first present the remaining new bitmap list for that page to the user. Do not generate that page's individual assets before the bitmap list is explicitly confirmed.
- For module pages, do not limit the resource scope to only what already appears in the current effect image. First compare the page against the active module `impl.md` and finalize the bitmap checklist around the confirmed primary page. Additional page-local states may be appended later only after explicit human confirmation.
- Every new supplemental bitmap resource that is still required beyond the accepted atlas-slice outputs must be generated through `$imagegen` as its own prompt and saved as its own file. When an accepted `UI-only sheet atlas` already serves as the standard runtime resource atlas for that page, its confirmed slice outputs may be used directly as final runtime assets.
- Generated image assets must decide their background mode from the frozen design intent. For workflow atlas generation, always generate the atlas first on one preset least-conflicting flat background color and remove that background later through `$imagegen` before slicing. Use a baked background only when the frozen design explicitly treats that background as part of the asset itself.
- Treat a workflow atlas as a rearranged representation of the approved effect-image canvas rather than as an independent lower-resolution redraw. The recomposed atlas-backed result must stay consistent with the original effect-image dimensions, and every image-backed atlas cell must keep at least the same pixel size as its source region on that approved effect image.
- Atlas cell content must stay faithful to the original effect image. Do not add background colors, panel fills, separator blocks, helper mats, or any other new backing surfaces merely to make cells easier to distinguish, export, or inspect.
- Atlas cells must not add line frames, strokes, crop guides, divider rules, helper boundaries, or any other edge-marking decoration that was not already part of the approved design. Keep background or border treatment only when that treatment is genuinely part of the original design content for that exported visual.
- Atlas analysis and atlas export must use the original effect image as the visual source of truth. Do not perform decorative repainting, cleanup redraws, embellishment passes, or stylistic补画 that make the atlas look clearer than the approved screen itself.
- If an atlas input is already transparent, do not run background removal again. When a workflow atlas still needs transparent background output, route through `$imagegen` background removal, validate the alpha result, and confirm it before slicing.
- Atlas background removal may run only from solid-color backgrounds; non-solid inputs must be regenerated as a solid-background atlas first.
- Atlas helper rows may use `data_excluded_placeholder` to mark runtime-data regions that must stay out of generated bitmap slices.
- If a generated image is later superseded or deleted, update the same catalog row in the same workflow step so downstream routing cannot accidentally reuse the stale file.
- Shared and module structured design sources must directly reference the final generated asset files for every approved bitmap asset. Regions that are explicitly tracked as `placeholder_only` may remain placeholders, but screenshot crops or undeclared temporary placeholder assets are not allowed.
- If the same visual result can already be restored faithfully enough with code, tokens, vectors, gradients, or standard components, do not convert it into a bitmap asset.
- Every page-level bitmap decision must be written into a text checklist before confirmation. That checklist must classify the current page into `bitmap_required`, `flutter_native`, and `placeholder_only` groups so the later resource contract is grounded in an explicit written decision rather than only in image markup. When a matching atlas exists, the atlas manifest should carry the same classification per slice and keep runtime-data regions out of cut-safe UI slices.
- Generate approved bitmap resources serially. After one page's post-review bitmap list is confirmed, generate only that page's required resources, review them, and only then advance to the next page.

## Final Effect Image Boundary

The module final effect-image stage exists as an optional post-implementation visual-enhancement step after all target modules have already completed their primary functional implementation and the team is ready to refine visual fidelity beyond the standard-library baseline. Treat this as an explicit generate-and-review step before any atlas work begins.

- Use `Product Design:ideate` to generate the module final effect image only when the standard-library-first implementation pass has already landed across the target modules and the project still needs a higher-fidelity visual baseline for later refinement.
- When an approved native HTML prototype already exists, treat that prototype as the first-priority source for layout structure, page hierarchy, module grouping, visible action order, and basic interaction ownership. The final effect image may improve visual fidelity, but it must not overturn the confirmed structural contract.
- The final effect image must be driven by `@product-design` brief confirmation, approved visual direction, and commercial product UI/UX standards. It must not behave like a detached art-generation step.
- Treat the final effect image as a later visual-refinement baseline, not as a prerequisite for the first-pass module implementation.
- In practical weighting, restore layout and interaction-related structure first and visual polish second. If a visual flourish conflicts with the confirmed prototype's task path, grouping, spacing logic, or action priority, keep the prototype structure and revise the image direction instead.
- Treat "commercial product UI/UX" here as a hard generation constraint: the image should look like a shippable app screen, not a wireframe-like draft, not a mood board, not a poster, not an ad, and not a marketing hero composition.
- Do not let the final effect-image stage silently redefine palette direction, typography mood, component family, image-treatment posture, or public-shell language that were already frozen upstream. It may only extend those constraints to the active page.
- Before any generated final effect image may be treated as accepted workflow evidence, complete manual image review against the active brief and frozen visual constraints and record the human review result.
- Do not block first-pass module architecture, blueprint generation, or functional implementation on the absence of a final effect image.
- Keep the stage anchored to mature commercial product UI/UX: fast scan clarity, strong action hierarchy, compact but readable density, and product-surface realism over poster-like styling.
- If review feedback is still about page purpose, module order, emphasis, or overall visual direction, revise the same module final effect-image direction pass instead of opening a separate sketch gate.

## HTML Prototype Stack Boundary

When the workflow explicitly needs a Product Design-owned high-fidelity review prototype from reference images, the default stack is `Vite + React + TypeScript` for later Flutter restoration comparison. Do not default that high-fidelity review prototype path to `Vue` or plain `HTML/CSS/JS`. This does not replace the module confirmation prototype: module layout gates still use native `HTML/CSS/JS` only.

## Display Evidence Pack Boundary

The `display_evidence_pack_ready` stage exists to prove that fidelity-critical regions have enough evidence before the optional post-implementation visual-enhancement path proceeds.

- For fidelity-sensitive pages, the evidence pack must include at least one readable main preview plus any required detail, scroll-position, and overlay evidence for the confirmed primary page.
- Do not expand the evidence pack into `error`, `empty`, `loading`, permission, disabled, success, locked, premium, or other additional page states unless explicit human confirmation has already requested those states to be appended.
- Do not let a single pretty main effect image stand in for missing state or structure evidence when the later Flutter restoration would have to guess.
- The display evidence pack must be confirmed before the workflow finalizes any later effect-image, atlas, slicing, Pencil, or bitmap-asset refinement pass, but it is not a blocker for the first-pass standard-library implementation path.

## Module Native HTML Prototype Boundary

The `module_html_prototype_ready` stage exists to make the active module reviewable in native web form before the workflow commits to architecture and first-pass implementation.

- Enter this stage only after the shared/global design freeze is complete and the active module `impl.md` already fixes the module function, the primary task path, and non-display behavior boundaries for the confirmed primary page.
- Before the first prototype draft is created, verify that the active module already carries a commercial-product creation packet: `surface_goal=commercial_product_app`, exactly one `primary_task`, exactly one dominant `primary_cta`, explicit `first_screen_required_information`, explicit `defer_or_collapse_content`, explicit `information_density_posture`, `copy_posture=minimal`, and explicit `disallowed_surface_modes`. If any field is missing, stop and repair the brief or `impl.md` before creating the prototype.
- Treat `@product-design` as the default prototype-quality controller for this stage: reuse the confirmed design brief, and when prototype quality is still weak in hierarchy, commercial polish, copy compression, or interaction framing, route to `Product Design:ideate` first and optionally to `Product Design:prototype` or `Product Design:image-to-code` for a reviewable high-fidelity direction before revising the native module prototype.
- The prototype must show the module pages' static layout, hierarchy, spacing, and visual grouping clearly enough for page confirmation before downstream architecture and implementation work.
- The prototype must use only native `HTML`, `CSS`, and `JavaScript`. Do not use any framework, runtime, UI component library, build-only frontend stack, or generated SPA shell.
- The prototype's visible interface copy must default to Simplified Chinese unless the active module contract or the user explicitly requires another display language.
- The prototype must read as a mature commercial product surface rather than a marketing page, ad concept, poster, or explanatory requirements mock.
- Keep visible copy tight and product-facing. Use explanatory text only when it is necessary for labels, helper text, state cues, or risk prompts, and avoid long instructional or descriptive paragraphs.
- The first generated draft must already honor the creation packet. Do not rely on review-time repair as the normal path for removing explanation-heavy copy, collapsing secondary content, or re-establishing CTA dominance.
- The prototype is static-page evidence only. Do not use it to validate interaction flow, state switching, scroll ownership, sticky behavior, or overlay behavior.
- In manual mode, the workflow must stop for explicit user confirmation after the native HTML prototype is reviewable. Do not enter architecture or implementation before that confirmation.
- The confirmed native HTML prototype is static layout evidence. It does not replace `impl.md` for behavior definition, and it does not replace the module Pencil design source as the frozen implementation design file.
- When the module stage advances beyond this gate, record the accepted prototype paths and the receipt that proves the prototype was generated from the active module contract instead of from ad hoc downstream guesswork.
- If the module native HTML prototype is revised after review, treat that revision as a requirements change. Update the active module `impl.md`, any affected shared design rules, and the workflow record before architecture, implementation, or any later visual-enhancement step continues.

## Pencil Design Source Boundary

The `pencil_design_source_ready` stage remains a mandatory pre-implementation design-normalization step for module scope. After the later visual-enhancement pass adds effect images, atlas outputs, or bitmap evidence, the workflow may run one additional Pencil reinforcement pass on top of that original mandatory Pencil baseline.

- The workflow must route through `effect-image-to-pencil-design` for both shared scope and module scope.
- Pencil design execution must happen through MCP, not through ad hoc file generation.
- Pencil page width must keep the frozen design width unchanged. Pencil page height must not be lower than the frozen base design viewport height. If the page or a major region is intentionally scrollable, the Pencil page height may exceed that minimum to preserve the designed scroll range.
- Before a Pencil design file can be accepted, it must be compared against the approved effect image.
- The compare result must produce a visible-difference list and a concrete fix plan, then stop for confirmation.
- After confirmation, apply one focused repair pass and request human acceptance.
- Pencil remains a prerequisite for the first-pass architecture and code path. If later visual-enhancement evidence is generated after all modules become functionally complete, run one additional focused Pencil reinforcement pass instead of replacing the original Pencil position.

## Display Restoration Blueprint Boundary

The `display_restoration_blueprint_ready` stage exists to make Flutter display restoration executable instead of interpretive.

- Every implementation-facing page must have a concrete display-layer decision table plus a page-level `display_restoration_blueprint` before code execution begins.
- The blueprint remains mandatory because the frozen structured packet is a design source, not self-executing implementation code.
- The blueprint must lock region ownership, scroll and sticky behavior, state slots, spacing locks, and fidelity-critical constraints strongly enough that display-layer code does not need to reinterpret design intent. For the initial module version, prefer Flutter SDK standard capabilities and platform HIG-aligned interaction decisions before introducing asset bindings or bitmap fallbacks.
- Do not move a module into implementation execution while the blueprint is missing, vague, or contradicted by the frozen design packet.

## Pencil Restoration Boundary

The `pencil_restoration_ready` stage exists to turn the frozen Pencil design source into a Flutter restoration contract before architecture and code execution. If the later visual-enhancement path later produces stronger effect-image or atlas evidence, that path may trigger one additional Pencil-backed restoration refresh.

- The workflow must route through `pencil-design-to-flutter-restoration`.
- This restoration contract must explicitly evaluate Flutter standard library fit, third-party plugin fit, and bitmap-asset fit.
- The restoration contract must identify which regions are safe for standard Flutter, which require plugins, and which must preserve approved bitmap assets.
- Do not start architecture or code execution without this restoration contract once Pencil has become the frozen primary design source. If a later visual-enhancement pass refreshes Pencil, update the restoration contract before consuming that refreshed Pencil packet.

## Render QA Boundary

The `flutter_render_vs_frozen_design_qa` stage exists to compare landed Flutter rendering against the frozen design source before final human acceptance.

- Use this stage only after the relevant display layer has landed and implementation screenshots or renders exist.
- Compare Flutter output against the frozen design packet, including approved effect images, confirmed generated asset files, and the frozen `display_restoration_blueprint`.
- Record visible fidelity deltas explicitly instead of treating render QA as a casual visual glance.
- This stage is a blocking helper before final human visual inspection; it does not replace final human acceptance.

When the request is asset-oriented rather than screen-implementation-oriented, the orchestrator may open the `Creative Production` branch in two windows. Before final product direction confirmation, it may use Creative Production as a direction-input branch when richer campaign or hero exploration is needed to inform the final decision. After `DESIGN.md` exists, it may use Creative Production as the post-direction asset-production branch for mood boards, ad directions, offer-led hero directions, scenes, shots, logos, asset packs, and publish-safe polish. Keep ownership explicit: `@product-design` still owns product-surface UX and the confirmed design direction, while `Creative Production` owns commercial creative exploration and asset finishing. Creative Production outputs may enrich reviewable visual evidence, but they never replace the frozen structured design source or screenshot-based and image-based design-source normalization.

## Commercial Product UI Constraint

This workflow must optimize for a mature commercial product feel, not a requirements demo, explanatory mock, or settings-manual style UI.

Default assumption:
users scan, recognize, and act; they do not read long explanatory text unless they are blocked.

The workflow must treat excessive explanatory copy as a product-quality defect, not as a harmless fallback.

Always prefer this communication order on product surfaces:

1. visual hierarchy
2. spatial grouping
3. control state
4. icon / badge / chip / toggle / color cues
5. short label
6. short status text
7. optional secondary explanation behind disclosure

Do not let primary screens explain what the interface can already show through visual structure.

### Default Copy Posture

For product-facing mobile screens:

- prefer recognition over explanation
- prefer visual state over descriptive paragraphs
- prefer one-line labels over multi-line descriptive copy
- prefer short status chips, helper rows, and compact captions over long support text
- prefer progressive disclosure over always-visible explanation
- prefer secondary surfaces for education: bottom sheet, detail page, info modal, learn-more link, expandable cell

Users should understand the screen mostly by looking, not by reading.

### Commercial UI Compression Rule

Every product-facing screen must pass a copy-compression check before freeze:

- if a subtitle repeats the title's meaning, remove it
- if a row description only restates the row title, remove it
- if a helper paragraph can be reduced to a chip, short status line, or one-line helper row, reduce it
- if two adjacent text blocks explain the same action or the same state, keep only the shorter one
- if a support card explains something already visible from status, icon, color, or control state, remove or collapse it
- if multiple text blocks explain the same system state, keep only the shortest necessary one
- if the screen still works after deleting a paragraph, that paragraph should not be on the default surface

Long explanatory copy is allowed only when one of these is true:

- the user must understand a risk before acting
- the system is blocked and the cause is otherwise invisible
- the user is entering a recovery or exception flow
- the explanation is intentionally behind disclosure

### Minimal Default Copy Contract

Every default product surface must satisfy `minimal_default_copy_contract` before it can be accepted as commercial UI.

Use an `explanatory_copy_budget` for the default visible surface:

- keep at most one short helper line for a primary region
- prefer labels, status chips, badges, icons, toggles, grouping, and state visuals before explanatory text
- move explanation behind disclosure when the explanation is educational, policy-like, repetitive, or not required for immediate action
- use a bottom sheet, detail page, info modal, expandable row, or secondary page as the `disclosure_destination`
- mark the design as `explanation_overload` when multiple visible helper paragraphs, notice cards, subtitles, and support-copy blocks compete on the same default surface
- establish these limits before first generation, not only before freeze: no subtitle-plus-paragraph pattern by default, no repeated helper stack for the same state, no educational support card on the primary surface unless the action would otherwise be unsafe

If `explanation_overload` appears, revise the design before HTML prototype acceptance, final effect-image acceptance, Pencil acceptance, or freeze.

### Primary Surface Rule

On the first screenful of any page, show only:

- the main task
- the current state
- the next action
- the minimum supporting context required to act safely

Do not spend first-screen space on broad education, repeated context, or policy-style explanation.

### Freeze Review Questions

Before approving any product-facing design, ask:

- If all long explanatory copy disappeared, would the screen still mostly make sense?
- Does the user understand the primary task in under 3 seconds without reading paragraphs?
- Is this screen acting like a product interface, or like a document explaining the interface?
- Would a mature commercial iOS app ship this much always-visible text on the primary surface?

If the answer is weak, the design must be revised before freeze.

### Commercial Design Exploration Window

Use a wide-before-freeze, narrow-after-freeze model for commercial product design quality.

Before this window opens, the workflow must complete `mandatory_mobbin_reference`. This is not optional inspiration browsing: it is a required product-design evidence step that collects relevant Mobbin or Mobbin-equivalent product screens, extracts concrete reference decisions, and records why those decisions fit the active product, platform, and viewport.

Before the `global_style_scheme` is locked, the workflow must keep `direction_space_open` and allow `structure_recomposition_allowed` under the confirmed PRD, technical baseline, Product Design brief, target platform, and frozen viewport. This window exists so AI design work can select a commercially plausible theme, hierarchy, density, and component posture instead of merely decorating an early requirements-shaped layout.

During this window, Product Design may propose and compare commercial directions that change:

- first-screen structure
- module order
- CTA placement and dominance
- navigation or shell emphasis
- visible versus deferred information density
- card/list/table rhythm
- state presentation strategy
- copy compression and disclosure placement
- component family posture

The selected direction must become one `fixed_style_direction`. Treat it as the `style_single_source` for all later module prototypes, module effect images, module Pencil sources, and Flutter display restoration. The workflow must not mix visual families from multiple Mobbin references after the style direction is selected.

The selected direction must also include a `strong_hierarchy_contract`. At minimum, record a `hierarchy_contrast_ladder` for primary action, primary content, secondary content, metadata, disabled or supporting copy, and background surfaces. That ladder must define contrast, scale, weight, spacing, and emphasis differences strongly enough that the page reads with clear commercial product hierarchy before decoration is considered.

The exploration window must still preserve the product goal, user roles, primary task path, platform target, and technical constraints. It may not silently expand into additional page states or invent new product scope, new roles, or new business behavior that the PRD did not authorize.

The window closes at the `freeze_boundary`: once the commercial direction is selected and `global_style_scheme.status=selected`, later module sketches, module effect images, Pencil design, and Flutter restoration must narrow around the confirmed style system instead of reopening broad layout exploration.

### Commercial Product Surface Gate

Every global style scheme, module HTML prototype, final effect image, and Pencil design source must produce a `commercial_surface_gate` receipt before it can be accepted, frozen, or used by a downstream stage.

The gate is a product-surface acceptance check, not a taste note. It must decide whether the artifact can plausibly ship as an in-product commercial app screen for the confirmed platform and product task.

Required receipt fields:

- `gate_owner`: the specialist or orchestrator step that ran the check
- `artifact_type`: `shared_html_prototype`, `module_html_prototype`, `final_effect_image`, `pencil_design_source`, or `freeze_packet`
- `artifact_paths`: local paths for the reviewed files or images
- `result`: `passed` or `revision_required`
- `first_screen_task_recognition`: whether the main task is clear within 3 seconds without paragraph reading
- `primary_cta_dominance`: whether the primary action is visible, singular enough, and not competing with decoration or support copy
- `real_control_density`: whether controls, lists, filters, tabs, and status surfaces on the confirmed primary page feel like a real product rather than a presentation mock
- `platform_information_density`: whether visible, deferred, collapsed, paged, and secondary-surface content matches the frozen platform and viewport
- `primary_surface_scope_control`: whether the artifact stays focused on the confirmed primary page and avoids silently expanding into unconfirmed additional states
- `copy_compression_result`: whether redundant subtitles, helper paragraphs, notice cards, and repeated support copy were removed or deferred
- `reference_decision_inheritance`: whether Mobbin/reference-image decisions are named as concrete inherited choices, not vague inspiration
- `commercial_failure_modes`: any detected poster, ad, landing-page hero, concept board, requirements mock, settings manual, or wireframe-like traits
- `failed_dimensions`: the gate dimensions that failed, or `[]`
- `revision_target`: the exact upstream artifact to revise when `result=revision_required`

If `commercial_surface_gate.result=revision_required`, the workflow must route back to the matching artifact owner for one scope-matched revision pass. Do not promote the stage, freeze the design, enter atlas work, enter Pencil work, or hand off to Flutter restoration until a later receipt records `commercial_surface_gate.result=passed`.

## Product Design Node Map

Use `@product-design` as a scoped design controller at specific workflow nodes instead of as a general replacement for the whole Flutter workflow.

- `technical_baseline_ready` -> `Product Design:get-context`
  Use to confirm the design brief, product surface intent, key journeys, page families, the default primary-page scope, interaction goals, platform assumptions, and information-density posture before visual direction work starts.
- `shared_design_direction` / `design_recommendation_ready` -> `Product Design:ideate`
  Use to explore and compare shared product-surface visual directions, module final effect-image directions, and reference-image-grounded alternatives before locking the selected final effect-image baseline.
- upstream UX evidence gathering -> `Product Design:research` or `Product Design:audit`
  Use only when the workflow needs evidence about user pain, screenshot-based flow review, or UX friction before the design brief or direction can be trusted. Do not use these as substitutes for PRD writing, technical baseline generation, or freeze approval.
- optional design-prototype branch -> `Product Design:prototype` or `Product Design:image-to-code`
  Use only when the workflow explicitly needs a Product Design-owned coded prototype or visual-target implementation for design review, prototype sharing, or source-visual validation. Do not use these to replace the mandatory module native `HTML/CSS/JS` prototype gate, the Pencil design source, or Flutter implementation work.
- module prototype quality recovery -> `Product Design:ideate` -> optional `Product Design:prototype` or `Product Design:image-to-code`
  Use when the module native prototype is structurally acceptable but still weak in commercial polish, hierarchy, density, CTA posture, copy compression, or interaction framing. Use the Product Design output as upstream revision guidance, then fold the accepted decisions back into the mandatory native `HTML/CSS/JS` module prototype instead of treating the Product Design artifact itself as the accepted gate output.
- prototype delivery -> `Product Design:share`
  Use only when a non-production review prototype must be published or shared by URL. Do not use it as an app release, module acceptance, or Flutter deployment stage.
- implementation review -> `Product Design:design-qa`
  Use only after a coded prototype or rendered implementation already has both a source visual target and rendered output that can be compared. Do not use it for broad product audits, flow critique, or final human acceptance.

`@product-design` may control design brief quality, direction quality, prototype quality, design QA quality, and the confirmed solid-atlas image generation pass, but it does not own PRD writing, Flutter technical baseline generation, module splitting, design-freeze approval, atlas background-removal, atlas slicing, Pencil restoration, Flutter architecture, or final Flutter implementation.

## Output Language Rule

All workflow output artifacts must default to Simplified Chinese unless the user explicitly requires another language for a specific artifact or workflow branch.

This default applies to:

- PRD artifacts
- RD and technical baseline artifacts
- `DESIGN.md`
- workflow records
- route summaries and receipts
- design checklists
- freeze decisions
- review conclusions
- generated prototype visible copy

Do not mix English headings, English field summaries, or English prose into a Chinese-default artifact unless the artifact contract explicitly requires fixed English identifiers, code symbols, or file-format keys.

## Required Reading

Load only the references needed for the current routing decision, but always preserve their authority over the workflow:

- `references/workflow-record-contract.md`: Read before initializing or optionally persisting workflow state for the current run.
- `references/idea-sketch-flow.md`: Read when the input is still a rough idea, scattered references, or any demand that is too abstract to discuss through concrete pages yet.
- `references/requirements-prd-flow.md`: Read when the workflow is already inside `requirements_brainstorming` and must turn a confirmed idea sketch brief or an already-concrete feature request into a durable PRD artifact.
- `references/asset-atlas-flow.md`: Read after Pencil design review whenever atlas-slice outputs or supplemental bitmap assets still require runtime-asset normalization.
- `@effect-image-to-ui-sheet-atlas`: Use when the workflow must first produce atlas extraction analysis from a confirmed effect image and then generate the confirmed solid-background UI-only atlas, atlas manifest, and atlas slicing config as one reviewable node.
- `@ui-sheet-atlas-slicer`: Use after the atlas bundle is confirmed and the workflow must cut the atlas through one generic config-driven slicing step before entering Pencil restoration.
- `references/global-asset-catalog-contract.md`: Read when the workflow must create, update, validate, or reuse entries in the project-wide asset catalog.
- `references/prd-template.md`: Read when raw demand must become a durable PRD artifact rather than a chat-only summary.
- `references/prd-completeness-gate.md`: Read before promoting `requirements_brainstorming` to `prd_ready`.
- `references/prd-handoff-map.md`: Read when checking whether the PRD is strong enough for technical baseline, Product Design, Creative Production, or later module splitting.
- `references/design-quality-guidance.md`: Read when defining global visual direction, writing `DESIGN.md`, or judging whether a design is strong enough to freeze.
- `references/design-md-template.md`: Read when the final product design direction is confirmed and the workflow must write a root-level `DESIGN.md`.
- `references/creative-production-branch.md`: Read when the user asks for campaign visuals, mood boards, hero directions, ad routes, asset packs, or publish-safe creative polish within the broader Flutter workflow.
- `references/control-contracts.md`: Read before deriving route locks, running preflight, validating receipts, delegating to subagents, applying confirmation gates, or updating maturity.
- `references/execution-modes.md`: Read whenever the invocation includes `--auto`, `--full-auto`, module auto-advancement, effect-image generation, or stop-condition decisions.
- `references/workflow-states.md`: Read when classifying `current_stage`, module maturity, or allowed next moves.
- `references/routing-rules.md`: Read before selecting any downstream skill or crossing any stage boundary.
- `references/hard-rules.md`: Read before applying any state/status promotion, freeze decision, implementation handoff, visual-evidence decision, or downstream delegation.
- `references/pressure-scenarios.md`: Read when the user request resembles one of the pressure examples or tries to skip a gate.

## Core Freeze Requirements

Before any global design freeze or module design freeze, use `@product-design` as the primary design controller. After the technical baseline is ready, first freeze the target design-device preset, design viewport, and `image_output_scale` for the current design cycle, then route to `@product-design` `get-context` to confirm the design brief. That brief-confirmation pass must also lock a structured clarification packet for later module splitting: core user journeys, page families, the default primary-page scope, interaction goals, explicit `platform_identifier`, platform-aware navigation and feedback expectations, and per-surface information-density posture including what must be visible immediately versus what must be deferred, collapsed, paged, or moved to a secondary surface. It must also lock the commercial-product creation packet used by downstream module page generation: `surface_goal=commercial_product_app`, a single `primary_task`, a single dominant `primary_cta`, `first_screen_required_information`, `defer_or_collapse_content`, `information_density_posture`, `copy_posture=minimal`, and explicit `disallowed_surface_modes`. The workflow must not proactively plan additional `error`, `empty`, `loading`, permission, disabled, or other page-local states in that packet; those states may be appended later only after explicit human confirmation. During the shared/global taste-direction stage, use `https://mobbin.com/` as the mandatory first-stop product-design inspiration library, and do not enter direction recommendation, `DESIGN.md`, or downstream design freezing until the workflow has completed a Mobbin-backed inspiration pass. Treat Mobbin only as style evidence rather than the formal design source. Then derive three comparable theme and style candidates from that inspiration pass, mark one as the primary recommendation, and confirm one `global_style_scheme` with the user or deterministic auto gate. When visual review would help the user judge the direction, generate or assemble one `global_style_experience_image` through `Product Design:ideate` as a non-page style board that makes the selected hierarchy, palette, density, surface depth, component feel, and imagery posture visible without defining a screen layout. The global scheme must set `theme_and_style_only=true`, `no_global_page_design_draft=true`, `non_page_design_evidence=true` for that image when present, and `page_design_deferred_to_module_stage=true`. Only after that write the confirmed theme, hierarchy, public shell, component family, minimal-copy contract, and interaction principles into `DESIGN.md`. After the shared design freeze has passed, treat `@product-design` as the default upstream quality controller for the mandatory module prototype stage as well, but keep it as a creation-time guardrail first: do not open the first native prototype draft until the commercial-product creation packet is present in the active module contract. When the active module prototype is still weak in commercial UI bar, hierarchy clarity, default-copy compression, or task-first interaction framing, route through `Product Design:ideate` before revising the native prototype, and open `Product Design:prototype` or `Product Design:image-to-code` only when a coded high-fidelity review target is needed. The accepted Product Design output must still be translated back into the mandatory native `HTML/CSS/JS` module prototype before the module can pass `module_html_prototype_ready`. For iPhone-first mobile work, offer at least these common presets in manual mode unless the user already chose a viewport: `375 x 667 px` (SE / compact), `390 x 844 px` (standard iPhone baseline), `393 x 852 px` (Pro baseline), and `430 x 932 px` (Pro Max baseline). In manual mode, default `image_output_scale` to `2x` for those iPhone presets unless the user or an upstream artifact explicitly requires another workflow output size. In `--auto` or `--full-auto`, when the run does not already have a frozen viewport, default the global design viewport to `390 x 844 px`; when `image_output_scale` is still unset for iPhone-first work, default it to `2x`. In `--full-auto`, when the design brief, public shell, or final direction already have one uniquely supported default backed by the current artifacts, apply that confirmation directly and continue; if multiple plausible defaults remain, stop and record the ambiguity as a blocker. The shared/global design freeze packet is limited to theme, public-shell, shared-component, and shared interaction-principle design; do not generate any page design during that shared/global freeze step. After the shared design freeze has passed, prefer starting project initialization and bootstrap preparation as soon as the shared public baseline is explicit, rather than waiting for every later module milestone. Only after the shared design freeze has passed may the workflow start module `impl.md` generation, the mandatory native HTML module prototype stage, architecture, display-restoration blueprint preparation, and the first-pass implementation path. Module-scoped effect-image generation, atlas preparation, atlas slicing, Pencil design generation, and bitmap generation belong to a separate later visual-enhancement pass that may start only after all target modules have already completed their primary functional implementation. After normalization, inspect the matching artifact directories for static visual evidence before deciding whether any later regeneration is necessary.

Effect images are optional and belong only to the later visual-enhancement pass after the project has already finished the first-pass functional implementation across all target modules. If the target design-device preset, design viewport, or `image_output_scale` has not yet been frozen for the current global design cycle, stop before Product Design direction confirmation and request it first. If the Product Design brief has not yet been confirmed through `@product-design` `get-context`, stop and route there before asking for confirmation. If the common public shell has not yet been explicitly agreed, stop and request shell confirmation before confirming the global style scheme. If final product design direction is not explicitly confirmed through `global_style_scheme.status=selected`, stop before emitting `DESIGN.md` or entering later shared freeze work. Before every optional module final effect-image generation step, explicitly collect the already-frozen shared visual constraints from the global design packet and pass them forward as required inputs instead of letting the image tools infer them from scratch. Every module final effect image must keep the frozen design width unchanged and must not use a canvas height smaller than the frozen base viewport height. The request must also carry the frozen `image_output_scale` so the final workflow output size is derived from the logical viewport instead of reusing viewport pixels as the generated image size. Each completed module effect-image step must first output a matching atlas extraction analysis, and only after that analysis is confirmed may it output the matching solid-background atlas plus manifest and slicing config. That atlas analysis and downstream atlas bundle must treat the approved effect image as the pixel-space source of truth: the atlas may rearrange regions, but the combined atlas-backed result must stay consistent with the original effect-image dimensions, and no image-backed atlas cell may be exported below its source-region pixel size on that effect image. The module final effect-image direction pass should stay under `Product Design:ideate` plus `@product-design` QA control before the selected baseline is frozen. After atlas extraction analysis is confirmed, generate the solid-background atlas bundle through `Product Design:ideate` while preserving the approved cell plan and chosen background color. Keep atlas background removal plus slicing on the later visual-enhancement asset chain, and any final-generation access or credential blocker must be recorded as a blocker for the workflow. Save module draft or final effect images with the corresponding page names under `docs/project/`, then index them for any post-review selected generated asset set, the display evidence pack, and human visual inspection when needed.

When the user explicitly needs campaign-ready visuals, marketing routes, or polished asset packs, prefer the `Creative Production` branch over direct preview-image generation. Before final product direction confirmation, the branch may act only as reviewable direction input. After `DESIGN.md`, use `Creative Production:explore` as the controlled asset-production entry point, then route into a focused explorer and finally to `generative-polish` only after one direction or deterministic base is selected. Keep both windows behind the same design-direction gates: they may inherit the confirmed product direction and `DESIGN.md`, but they must not silently redefine them.

Every module final effect-image generation request must explicitly include existing image-backed design constraints: `art_direction`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, image-treatment posture, and the approved reference-image baseline when those values already exist. Those constraints must be read from the current frozen global-design packet first, then narrowed only by the active page or module needs; if the global packet cannot supply the required visual constraints, stop and repair the packet instead of generating a speculative image. Every request must also carry the frozen design width plus the frozen base viewport height as the minimum logical output size, and must separately carry `image_output_scale` to derive the workflow output size. For example, a frozen viewport of `390 x 844` with `image_output_scale=2x` means the generated image should start from about `780 x 1688` pixels before any intentional extra scroll height. When the design target includes a scrollable page or scrollable region, allow a taller output height to show the designed scroll range, but do not shrink width or reduce height below the frozen minimum in order to fit more content into one screen. Final effect-image requests must go through `Product Design:ideate`, and any revision request must inherit the same constraints plus the accepted review notes before the Product Design-owned final effect-image direction pass is frozen as the selected baseline. The workflow must select or revise a Product Design-generated candidate instead of generating the module final effect image through `gpt-image-2-generator`. The workflow must also generate the solid-background atlas image through `Product Design:ideate` instead of `gpt-image-2-generator`, but only after the atlas extraction analysis, cell plan, background-key color, source effect-image canvas size, and per-cell source-region bounds are already confirmed. Each image-backed atlas cell must preserve at least that source-region pixel size when exported so recomposing the accepted atlas-backed cells can return to the approved effect-image dimensions without density loss. The module stage must stay inside the confirmed `@product-design` brief and must target mature commercial product UI/UX rather than speculative concept art, wireframe-like draft output, marketing illustration, ad visual, or slogan-led hero art. The generation prompt must explicitly say that the output is an in-product commercial app screen, with functional controls, believable information density, and product-task hierarchy as the first priority. When a confirmed native HTML prototype, `impl.md`, or frozen structural blueprint already exists, preserve that structure first and use the effect image only to raise visual fidelity inside the confirmed layout and interaction contract. If the selected final effect-image direction path is blocked by missing access, credentials, or upstream capability, stop and record a blocker for the workflow. All workflow final effect images must use light mode unless the user explicitly changes that requirement upstream.

For module implementation, the first priority before freeze is faithful restoration of the confirmed layout structure, task path, action order, and interaction ownership, with functional completeness and interaction experience taking priority over later-stage visual asset generation. Before queueing or applying `module_design_frozen`, verify that the global design freeze is already complete, that the module `impl.md` already fixed the module function, the primary interaction path, non-display behavior boundaries, and platform-aware information-density decisions under the frozen shared design and interaction principles, that a native static HTML module prototype has been generated and accepted for the active module, and that the display restoration blueprint is already strong enough to support a first-pass implementation using Flutter SDK standard capabilities plus platform HIG-aligned interaction constraints. The default freeze scope is the confirmed primary page only; any additional page states must be appended later only after explicit human confirmation. Effect images, atlas extraction analysis, atlas evidence, display evidence packs, module Pencil design source, and bitmap assets belong to the later visual-enhancement path only when they are still necessary after all target modules have completed their primary functional implementation. If the initial implementation inputs are missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched revision. After the module has entered implementation, prefer standard-library-first restoration and postpone bitmap-dependent refinement decisions until the post-implementation visual pass.

## Routing Procedure

For every invocation:

1. Ensure workflow state is initialized for the current run. If runtime persistence is enabled, use `references/workflow-record-contract.md` to shape the persisted artifact.
2. On the first call for that target root, run the git preflight: verify `.git/`, run `git status`, and check whether `.gitignore` already exists. Record missing repository-baseline items explicitly instead of silently assuming a clean repo.
3. Determine whether the run is manual, `--auto`, or `--full-auto`; load `references/execution-modes.md` when relevant.
4. Read the existing workflow record and any required artifact indexes before choosing a route.
5. Derive and persist one route lock before invoking anything downstream.
6. Run the preflight gate from `references/control-contracts.md`. If it fails, record the exact blocker and stop.
7. If the input is still a rough idea or reference bundle that lacks a concrete page model, route first to `idea_sketch_brainstorming`, read `references/idea-sketch-flow.md`, and block PRD generation until the key-page sketch confirmation plus `docs/project/idea-sketch-brief.md` both exist.
8. Select the next downstream skill using `references/workflow-states.md` and `references/routing-rules.md`.
9. If the step is subagent-eligible, delegate only the specialist work and require a structured receipt; keep workflow ownership in the orchestrator.
10. Validate the receipt against the active route lock before applying any transition or status update.
11. In manual mode, queue reviewable stage/status changes behind confirmation. In `--auto`, auto-apply deterministic stage and status transitions, auto-confirm ordinary orchestrator-owned review gates after receipt validation, and keep invoking the next authorized serial step end-to-end until all target modules are implemented or a blocker appears. In `--full-auto`, also auto-confirm deterministic human-facing workflow gates when the control contracts prove there is exactly one supported default; otherwise stop with a blocker instead of guessing.
12. Update the orchestrator-owned workflow state as the single source of truth. Persist it only when the current run actually needs a runtime artifact.
13. Return the output contract fields listed below.

## Delegation Boundary

Subagents may execute specialist work, but they must not own workflow control. The orchestrator alone may choose `current_stage`, choose `current_module`, persist route locks when needed, run preflight, validate receipts, apply queued transitions, classify blockers, and update orchestrator-owned workflow state.

Do not run multiple subagents in parallel against the same active module or the same workflow record when their outputs could race. In `--auto` or `--full-auto` after the shared/global design freeze, advance one module at a time in the confirmed serial module order until all target modules are fully implemented or a blocker appears.

## Implementation Boundary

Do not move a module into `implementing` until `technical_baseline_ready`, `module_impl_docs_ready`, `module_design_frozen`, `impl_rd_ready`, `pencil_restoration_ready`, `display_restoration_blueprint_ready`, and `bootstrap_code_ready` exist for the module, confirmed maturity is at least `impl_status=landed` and `design_source_status=frozen`, the frozen Pencil-backed structured design-source packet exists for the module, the display evidence pack plus display-layer decision table are already complete, and the required global public code baseline is already landed.

The required global public code baseline includes app bootstrap and environment initialization, root router or route host plus redirect policy, global dependency injection or provider scope entry, local storage baseline and persistence wiring, global error mapping and logging baseline, required shared theme or design-token baseline, and the shared shell layer when feature modules depend on an `app-shell` or `root-shell`. Unless the user explicitly overrides the toolchain choice, treat `fvm` as the default Flutter environment contract for project initialization, bootstrap, validation, and implementation commands, and prefer `fvm flutter ...` / `fvm dart ...` over bare `flutter` or `dart`. Whenever this workflow or any downstream skill needs to actually execute a Flutter or Dart command, prefer the `fvm` form first and fall back to bare `flutter` or `dart` only when the user explicitly requires it or the project contract already proves that `fvm` is unavailable. Add network baseline and API client wiring only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities.

`project_initialized` is directory-only: `flutter-init` may create the project shell, directory skeleton, and the sibling `skills/flutter-dev/` beside `flutter-init`, but it must stop before bootstrap code, shared wiring, feature code, or page code. That generated `skills/flutter-dev/` directory must stay at that sibling path and must not be deleted by later workflow steps; later refreshes should update its contents in place. Unless the user explicitly requires another toolchain contract, initialization should assume an `fvm`-managed Flutter environment and keep generated command guidance aligned with that default. Those global code responsibilities belong to the separate bootstrap code stage.

As soon as the shared design freeze is complete and the shared bootstrap-critical baseline is explicit enough, prefer `flutter-init` and bootstrap preparation before later module architecture milestones. Treat project initialization and bootstrap as early public-code preparation, not as a late afterthought.

When implementation work should begin, the entry sequence is fixed: route through `@superpowers` to produce `Spec` first, then through `@superpowers` again to produce `Plan`, and only then execute implementation with sibling `flutter-dev` and `flutter-project-guardrails`. During code implementation, the generated sibling `flutter-dev` skill is the strict project-local execution contract and must be followed directly rather than treated as optional guidance. Treat the modules as one serial implementation loop rather than a parallel batch. For each active module in order: first confirm the module `impl.md` as the detailed functional contract, then build and confirm the native static HTML module prototype in plain `HTML/CSS/JS`, then confirm the mandatory module Pencil design source, then require `flutter-uiux-to-architecture` to materialize and confirm a page-level `display_restoration_blueprint`, then land non-display-layer code against that blueprint, and only after that restore the display layer from the same approved blueprint with Flutter SDK standard capabilities plus platform HIG-aligned interaction constraints rather than re-interpreting upstream design artifacts in code. The first-pass goal is complete functional experience and usable design restoration without depending on effect images, atlas bundles, slicing outputs, or bitmap assets, but it still depends on the original mandatory Pencil source. Implementation execution inside that active module should stay serial by default unless the same module's ownership split is explicitly proven safe. Before display-layer code begins, inspect the corresponding native HTML prototype, Pencil design, `display_restoration_blueprint`, and frozen design evidence when such evidence exists. If later visual refinement proves that an internal illustration, icon asset, texture, or bitmap fallback still needs generation or rework, let the later MCP / design tool chain choose the concrete generation mechanism as long as the result still satisfies the frozen design principles and implementation target. Generated code artifacts produced during this implementation path do not require extra validation, static analysis, or test gates unless the user explicitly asks for them. If non-display implementation drifts away from the frozen interaction or layout contract captured by that blueprint, fix the non-display code or route back to design-source control instead of allowing display-layer code to absorb the drift. After the display layer lands and screenshots exist, run `flutter_render_vs_frozen_design_qa` before final handoff, then run `@product-design` `design-qa` as a blocking helper when both a source visual target plus implementation screenshots are available, and only then return to explicit human visual inspection rather than introducing a new automatic workflow stage. Only after all target modules have already completed that primary functional loop may the workflow open a later optional visual-enhancement pass for effect images, atlas preparation, slicing, Pencil reinforcement, and bitmap assets when they are still truly necessary.

## Output Contract

Return:

- `workflow_record_path`
- `workflow_record_update`
- `current_module`
- `current_state`
- `confirmation_status`
- `next_skill`
- `pending_next_stage`
- `pending_next_skill`
- `pending_status_updates`
- `route_lock`
- `execution_owner`
- `receipt_status`
- `receipt_summary`
- `progress_delta`
- `required_inputs`
- `blockers`
- `allowed_next_actions`
- `forbidden_actions`
