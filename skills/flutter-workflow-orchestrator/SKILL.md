---
name: flutter-workflow-orchestrator
description: Use when coordinating rough Flutter idea intake, idea-sketch brainstorming, requirements brainstorming, PRD document generation, technical baseline generation, Product Design brief confirmation, reference-image-backed effect-image generation, atlas-extraction analysis, solid-background UI atlas preparation, imagegen-based atlas background removal, minimum-cell atlas slicing, design-direction confirmation, DESIGN.md output, mandatory Pencil design-source generation, post-review shared image-asset generation, shared design freezing, module implementation document generation, mandatory native HTML module prototype confirmation, implementation-stage module effect-image generation, display-evidence-pack checks, mandatory module Pencil design-source generation, implementation-stage post-review module image-asset generation, module design freezing, Pencil-to-Flutter restoration planning, architecture planning, display restoration blueprint generation, implementation readiness, Product Design design QA, human visual inspection handoff, workflow state, or when a user asks what stage should happen next.
---

# Flutter Workflow Orchestrator

## Overview

Route a Flutter module through rough idea intake -> idea-sketch brainstorming -> requirements brainstorming -> PRD document generation -> global technical baseline -> target design-device preset and base resolution confirmation -> `@product-design` brief confirmation -> reference-image-backed representative sketch generation through local `$imagegen` under `@product-design` direction -> final product design direction confirmation from the approved sketch -> effect image plus atlas-extraction analysis -> confirmed solid-background UI atlas preparation -> confirmed `$imagegen` atlas background removal -> minimum-cell atlas slicing -> `DESIGN.md` output -> mandatory shared Pencil design-source generation -> shared image-asset generation after review when still needed -> optional post-direction Creative Production asset production / polish when the request is asset-oriented -> shared freeze -> early project initialization plus bootstrap preparation -> module `impl.md` generation under frozen design and interaction principles -> mandatory native HTML module prototype confirmation -> implementation-stage effect image plus atlas-extraction analysis -> confirmed solid-background UI atlas preparation -> confirmed `$imagegen` atlas background removal -> minimum-cell atlas slicing -> display-evidence-pack confirmation -> mandatory module Pencil design-source generation -> module image-asset generation after review when still needed -> module design freeze -> implementation RD readiness -> Pencil-to-Flutter restoration planning -> architecture -> display restoration blueprint readiness -> implementation workflow -> Flutter render versus frozen-design QA -> `@product-design` design QA -> human visual inspection.

This skill is the traffic controller. It chooses the next specialist skill, records state, blocks skipped gates, waits for explicit user confirmation before promoting any stage or status change, and maintains one stable workflow truth model for the whole project. When persistence is needed for a live run, it may serialize that state into runtime artifacts, but those artifacts are not part of the stable skill bundle.

On the first call for a target project root, run a lightweight git preflight before any downstream routing: check whether `.git/` already exists, whether `git status` is readable in that root, and whether a root `.gitignore` baseline already exists. If any of those repository-baseline pieces are missing, keep that finding in the route context and let `flutter-init` own the actual `git init` plus `.gitignore` creation or repair.

In manual mode, pause at confirmation gates after one stage or one module reaches a reviewable milestone. In `--auto` mode, behave as a full-module advancement loop across the whole target module set, auto-confirm ordinary orchestrator-owned stage and status promotions after receipt validation, and keep executing one serial module step after another until every target module is implemented or a real blocker appears, rather than opening parallel module lanes. In `--full-auto` mode, keep the same serial advancement loop but also auto-confirm deterministic human-facing workflow gates when one default is uniquely justified by existing artifacts. That expanded auto-confirm scope includes Product Design brief confirmation, public-shell confirmation, final product direction confirmation, and primary-platform device selection when the control contracts say the default target is unique. If the choice is still ambiguous, the workflow must stop and record a blocker instead of inventing certainty.

The required design-source output is a frozen structured restoration packet whose primary design-file form is now Pencil. After the final design direction is confirmed and `DESIGN.md` is written, the workflow must convert the approved screenshot references, the confirmed representative final effect-image baseline, and `DESIGN.md` into one shared structured design packet, then build a high-fidelity Pencil design source through MCP. `@product-design` still owns the design-side kickoff: brief confirmation, direction framing, visual-target selection, and the commercial product UI/UX bar for both sketch and final-image stages. The shared/global flow must first generate one local representative sketch through `$imagegen` under `@product-design` constraints, wait for explicit sketch confirmation in manual mode, and only then generate the representative final effect image before entering the dedicated atlas-preparation node. That node must first produce one written atlas extraction analysis from the confirmed effect image, the original prompt, and the frozen constraints; the analysis must list only the visuals that Flutter SDK standard capabilities cannot reproduce faithfully enough, and it must explicitly exclude dynamic-data-driven regions. Only after that atlas extraction analysis is confirmed may the node choose one least-conflicting preset background color and generate one solid-background UI-only atlas together with the atlas manifest and slicing config. After the solid atlas bundle is confirmed, the workflow must route through `$imagegen` to remove the background while preserving the atlas layout and then stop for confirmation again before the dedicated minimum-cell slicing stage may run. For module scope, overlay UI surfaces such as modal, dialog, bottom sheet, action sheet, and other overlays are controlled by a prerequisite constraint rather than a mere preferred order: they may enter atlas scope and later Pencil usage only after the same page's `page_base` atlas contract already exists. Every workflow-generated image that enters evidence or downstream consumption must also pass one automatic `@product-design` QA review before the workflow asks for confirmation, promotes the next stage, or consumes that image as a frozen baseline. Final effect images remain mandatory, but the workflow now requires only the representative final effect image at the shared/global stage. The orchestrator must first route through `effect-image-to-pencil-design` to build the mandatory Pencil design source, compare the result against the approved effect image, output a visible-difference list plus concrete repair actions, stop for confirmation, apply one focused repair pass, and only then request human acceptance of the Pencil design file. That Pencil design source must consume the confirmed atlas slice outputs for asset-backed visuals rather than re-deriving those visuals from the whole-page effect image. Only after that review result is confirmed may the workflow decide whether any non-standard bitmap assets still require post-review supplemental generation beyond the accepted atlas outputs and route through post-review shared image-asset generation. Separate module design documents must not replace the frozen structured design-source packet. All module-related work must stay behind the global design freeze. Only after the shared design direction, shared interaction principles, shared public shell rules, and shared component families are frozen may the workflow start the per-module loop. In that loop, the active module's `impl.md` becomes a detailed module task implementation document constrained by the frozen design and interaction principles. After `impl.md` fixes the module function, key states, task path, and non-display behavior boundaries, the workflow must first produce a module-scoped native HTML prototype that shows the module pages' static layout. That prototype is a mandatory confirmation gate before any module-scoped atlas-preparation work may begin. The module HTML prototype must use only native `HTML`, `CSS`, and `JavaScript`; do not use React, Vue, Svelte, Angular, Next.js, Nuxt, Vite app scaffolds, UI frameworks, or any other component/runtime framework. The HTML prototype should remain static and must not be used to validate interaction flows; interaction, state, and behavior expectations stay owned by `impl.md` plus the downstream visual restoration and architecture steps. After the user confirms that native HTML prototype in manual mode, the workflow should run the atlas-preparation node to generate the module effect image analysis, stop for confirmation, then generate the matching solid-background UI atlas plus manifest and slicing config, confirm that solid atlas bundle, run `$imagegen` background removal, confirm the transparent atlas result, enter minimum-cell slicing, confirm the display evidence pack, enter mandatory module Pencil design-source generation, and only then continue into post-review module image-asset generation plus later freeze and implementation work. Before every shared/global or implementation-stage module sketch or effect-image generation request, the workflow must first read the frozen global design packet and explicitly extract the visual constraints that already exist for that page or module, including palette direction, typography mood, component family, CTA posture, image-treatment posture, spacing or hierarchy bias, and any other approved visual-system rules; both sketch generation and final effect-image generation may only extend those constraints rather than inventing replacements. At both stages, generated output must read as mature commercial product UI/UX rather than a requirements mock, poster, or explanatory collage. If an image-generation step fails and the workflow retries it, the retry prompt must preserve the full original prompt plus all frozen visual constraints; do not shorten, simplify, or drop prompt detail as the retry mechanism. Design guidance for the module stage must come only from the frozen global design images, the confirmed native HTML prototype, the frozen Pencil design source, the active module design-source packet, uploaded approved screenshot references, any post-review confirmed generated asset files, and `DESIGN.md`; tool-native defaults, hidden heuristics, or internal style opinions are not valid guidance sources. After any shared/global or module freeze is confirmed, delete previously generated but no-longer-selected sketches or effect images from the corresponding workflow artifact directories and indexes so later routing cannot accidentally reuse stale alternatives. Restored design output must preserve one shared style direction, one shared theme system, one shared public shell contract, one shared public component family contract, and one shared interaction-principle contract across all pages.

## Idea Sketch Brainstorming Boundary

The `idea_sketch_brainstorming` stage exists to turn rough product intent into something concrete enough for PRD work.

- Use this stage when the user has only a rough idea, a few references, or abstract goals that are still hard to reason about as pages.
- The stage must brainstorm the product direction, collapse the core task path, and generate `1-3` key-page sketches that make the main flow visible.
- Those sketches confirm product direction, page structure, and broad visual style only. They are not a design freeze, not the later Product Design representative sketch, and not a substitute for `DESIGN.md`.
- Before leaving this stage, write a lightweight `docs/project/idea-sketch-brief.md` artifact that captures the confirmed idea summary, key pages, broad style direction, and the questions that still belong to PRD.
- Do not let this stage jump straight to technical baseline, Product Design brief confirmation, shared freeze, architecture, or implementation planning. It exists to make the idea concrete enough for the downstream PRD flow, not to bypass that flow.

## Asset Resource Boundary

The asset-resource stage exists to turn approved page imagery into reusable single bitmap assets after Pencil design review has confirmed what still truly needs image generation.

- Use this stage only after the current shared or module Pencil design source has already completed compare, confirmed repair scope, and human acceptance.
- Use this stage only when the confirmed Pencil review result still shows visual regions that cannot be restored faithfully enough in code and therefore require bitmap assets that stay very close to the approved effect image.
- “Restored faithfully enough in code” means the region can be recreated with Flutter SDK standard capabilities alone, without adding new bitmap assets, while still remaining close enough to the approved effect image in structure, shape, color, spacing, shadow, and overall visual character.
- Flutter SDK standard capabilities here include normal layout primitives, `Container`, `BoxDecoration`, borders, border radius, box shadows, gradients, text styles, standard icons, clipping, and other built-in drawing primitives such as `CustomPaint` when they can still preserve the intended look without bitmap assistance.
- Always maintain one project-wide asset catalog at `docs/project/assets/global-asset-catalog.json` before deciding whether a new bitmap asset should be generated again.
- The asset catalog is also the mandatory generated-image record table. Every workflow-generated representative sketch, final effect image, implementation-stage module effect image, matching atlas files plus manifests, shared bitmap asset, and module bitmap asset that enters workflow evidence or downstream consumption must be written into that catalog in the same workflow step.
- Every workflow-generated image that enters workflow evidence or downstream consumption must also leave one automatic `@product-design` QA receipt in the same workflow step or immediately after it, before later confirmation or freeze work continues.
- Asset reuse decisions must be based on `name`, `semantic`, and `usage_scenarios`, not only on filename similarity. If the workflow cannot safely decide whether an existing asset can be reused, mark it as `candidate_reuse` and stop for confirmation.
- Before any bitmap asset calls `$imagegen`, the workflow must first check `docs/project/assets/global-asset-catalog.json` plus the already-approved output files referenced by that catalog. If an approved reusable image already exists for the same semantic and usage scenario, reuse it directly and skip generation.
- If an image region is only a schematic placeholder and its real content must be created later from runtime data, keep it as a placeholder contract instead of generating a bitmap asset. Placeholder-only regions must not enter image generation.
- The resource generation unit may be one approved atlas-slice asset or one approved standalone bitmap resource. A shared resource lives under `docs/project/assets/shared/<page-name>/`, and a module resource lives under `docs/project/modules/<module>/assets/<page-name>/`. When the accepted atlas-slice outputs already satisfy the runtime contract, they count as final approved resource files and do not need to be regenerated as separate bitmaps.
- One page may contain multiple independently generated resources covering the primary surface plus that same page's `error`, `empty`, `loading`, and other page-local states, but it must not regenerate already approved reusable assets from other pages.
- After the workflow excludes code-restorable regions, `placeholder_only` regions, confirmed reusable assets, and any regions whose post-review Pencil adjustments made bitmap generation unnecessary, it must first present the remaining new bitmap list for that page to the user. Do not generate that page's individual assets before the bitmap list is explicitly confirmed.
- For module pages, do not limit the resource scope to only what already appears in the current effect image. First compare the page against the active module `impl.md` and supplement any missing but required page-local states before finalizing that page's bitmap checklist.
- Every new supplemental bitmap resource that is still required beyond the accepted atlas-slice outputs must be generated through `$imagegen` as its own prompt and saved as its own file. When an accepted `UI-only sheet atlas` already serves as the standard runtime resource atlas for that page, its confirmed slice outputs may be used directly as final runtime assets.
- Generated image assets must decide their background mode from the frozen design intent. For workflow atlas generation, always generate the atlas first on one preset least-conflicting flat background color and remove that background later through `$imagegen` before slicing. Use a baked background only when the frozen design explicitly treats that background as part of the asset itself.
- If an atlas input is already transparent, do not run background removal again. When a workflow atlas still needs transparent output, route through `$imagegen` background removal, validate the alpha result, and confirm it before slicing.
- If a generated image is later superseded or deleted, update the same catalog row in the same workflow step so downstream routing cannot accidentally reuse the stale file.
- Shared and module structured design sources must directly reference the final generated asset files for every approved bitmap asset. Regions that are explicitly tracked as `placeholder_only` may remain placeholders, but screenshot crops or undeclared temporary placeholder assets are not allowed.
- If the same visual result can already be restored faithfully enough with code, tokens, vectors, gradients, or standard components, do not convert it into a bitmap asset.
- Every page-level bitmap decision must be written into a text checklist before confirmation. That checklist must classify the current page into `bitmap_required`, `flutter_native`, and `placeholder_only` groups so the later resource contract is grounded in an explicit written decision rather than only in image markup. When a matching atlas exists, the atlas manifest should carry the same classification per slice and keep runtime-data regions out of cut-safe UI slices.
- Generate approved bitmap resources serially. After one page's post-review bitmap list is confirmed, generate only that page's required resources, review them, and only then advance to the next page.

## Representative Sketch Boundary

The representative sketch stage exists to lock direction, not to finish rendering.

- Use the local `$imagegen` sketch to confirm the page's product temperament, information hierarchy, module order, CTA posture, shell fit, and whether the page still belongs to the already-frozen visual system.
- Both the sketch and the later final effect image must be driven by `@product-design` brief confirmation, approved visual direction, and commercial product UI/UX standards. Neither stage may behave like a detached art-generation step.
- Treat the sketch as reviewable direction evidence. It should be good enough to answer "is this the right page and the right visual world?" but it does not need to prove pixel-perfect spacing, final material fidelity, exact text rendering, or freeze-ready polish.
- Do not let the sketch stage silently redefine palette direction, typography mood, component family, image-treatment posture, or public-shell language that were already frozen upstream. It may only extend those constraints to the active page.
- Keep the final effect-image stage for post-confirmation fidelity work: tighter spacing, higher material precision, stronger hierarchy finish, cleaner text treatment, and the final light-mode baseline that downstream freeze and implementation will inherit.
- Before any generated sketch or final effect image may be treated as accepted workflow evidence, run one automatic `@product-design` QA pass against the active brief and frozen visual constraints.
- Keep both stages anchored to mature commercial product UI/UX: fast scan clarity, strong action hierarchy, compact but readable density, and product-surface realism over poster-like styling.
- If review feedback is still about page purpose, module order, emphasis, or overall visual direction, stay in the sketch stage. Move to `gpt-image-2-generator` only when the remaining work is high-fidelity finishing inside an already accepted direction.

## Display Evidence Pack Boundary

The `display_evidence_pack_ready` stage exists to prove that fidelity-critical regions have enough evidence before freeze, architecture, or display restoration work proceeds.

- For fidelity-sensitive pages, the evidence pack must include at least one readable main preview plus any required detail, state, scroll-position, and overlay evidence.
- If `error`, `empty`, `loading`, permission, disabled, success, locked, premium, or other key states materially change composition or hierarchy, the workflow must collect state-specific evidence or an equally explicit frozen visual contract before moving on.
- Do not let a single pretty main effect image stand in for missing state or structure evidence when the later Flutter restoration would have to guess.
- The display evidence pack must be confirmed before the workflow finalizes module freeze, architecture mapping, or display-layer readiness.

## Module Native HTML Prototype Boundary

The `module_html_prototype_ready` stage exists to make the active module reviewable in native web form before the workflow commits to module effect images, atlas slicing, and Pencil restoration.

- Enter this stage only after the shared/global design freeze is complete and the active module `impl.md` already fixes the module function, key states, task path, and non-display behavior boundaries.
- The prototype must show the module pages' static layout, hierarchy, spacing, and visual grouping clearly enough for page confirmation before downstream effect-image work.
- The prototype must use only native `HTML`, `CSS`, and `JavaScript`. Do not use any framework, runtime, UI component library, build-only frontend stack, or generated SPA shell.
- The prototype's visible interface copy must default to Simplified Chinese unless the active module contract or the user explicitly requires another display language.
- The prototype must read as a mature commercial product surface rather than a marketing page, ad concept, poster, or explanatory requirements mock.
- Keep visible copy tight and product-facing. Use explanatory text only when it is necessary for labels, helper text, state cues, or risk prompts, and avoid long instructional or descriptive paragraphs.
- The prototype is static-page evidence only. Do not use it to validate interaction flow, state switching, scroll ownership, sticky behavior, or overlay behavior.
- In manual mode, the workflow must stop for explicit user confirmation after the native HTML prototype is reviewable. Do not generate module effect images, atlases, or Pencil design files before that confirmation.
- The confirmed native HTML prototype is static layout evidence. It does not replace `impl.md` for behavior definition, and it does not replace the module Pencil design source as the frozen implementation design file.
- When the module stage advances beyond this gate, record the accepted prototype paths and the receipt that proves the prototype was generated from the active module contract instead of from ad hoc downstream guesswork.

## Pencil Design Source Boundary

The `pencil_design_source_ready` stage exists to turn the approved effect image into the mandatory frozen design file.

- The workflow must route through `effect-image-to-pencil-design` for both shared scope and module scope.
- Pencil design execution must happen through MCP, not through ad hoc file generation.
- Pencil page width must keep the frozen design width unchanged. Pencil page height must not be lower than the frozen base design viewport height. If the page or a major region is intentionally scrollable, the Pencil page height may exceed that minimum to preserve the designed scroll range.
- Before a Pencil design file can be accepted, it must be compared against the approved effect image.
- The compare result must produce a visible-difference list and a concrete fix plan, then stop for confirmation.
- After confirmation, apply one focused repair pass and request human acceptance.
- Do not skip Pencil and move directly from effect image to freeze, architecture, or code.

## Display Restoration Blueprint Boundary

The `display_restoration_blueprint_ready` stage exists to make Flutter display restoration executable instead of interpretive.

- Every implementation-facing page must have a concrete display-layer decision table plus a page-level `display_restoration_blueprint` before code execution begins.
- The blueprint remains mandatory because the frozen structured packet is a design source, not self-executing implementation code.
- The blueprint must lock region ownership, scroll and sticky behavior, state slots, asset bindings, spacing locks, and fidelity-critical constraints strongly enough that display-layer code does not need to reinterpret design intent.
- Do not move a module into implementation execution while the blueprint is missing, vague, or contradicted by the frozen design packet.

## Pencil Restoration Boundary

The `pencil_restoration_ready` stage exists to turn the frozen Pencil design source into a Flutter restoration contract before architecture and code execution.

- The workflow must route through `pencil-design-to-flutter-restoration`.
- This restoration contract must explicitly evaluate Flutter standard library fit, third-party plugin fit, and bitmap-asset fit.
- The restoration contract must identify which regions are safe for standard Flutter, which require plugins, and which must preserve approved bitmap assets.
- Do not start architecture or code execution without this restoration contract once Pencil has become the frozen primary design source.

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
- if a support card explains something already visible from status, icon, color, or control state, remove or collapse it
- if multiple text blocks explain the same system state, keep only the shortest necessary one
- if the screen still works after deleting a paragraph, that paragraph should not be on the default surface

Long explanatory copy is allowed only when one of these is true:

- the user must understand a risk before acting
- the system is blocked and the cause is otherwise invisible
- the user is entering a recovery or exception flow
- the explanation is intentionally behind disclosure

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

Before any global design freeze or module design freeze, use `@product-design` as the primary design controller. After the technical baseline is ready, first freeze the target design-device preset and base resolution for the current design cycle, then route to `@product-design` `get-context` to confirm the design brief. That brief-confirmation pass must also lock a structured clarification packet for later module splitting: core user journeys, page families, critical states, interaction goals, explicit `platform_identifier`, platform-aware navigation and feedback expectations, and per-surface information-density posture including what must be visible immediately versus what must be deferred, collapsed, paged, or moved to a secondary surface. During the shared/global taste-direction stage, use `https://mobbin.com/` as the mandatory first-stop product-design inspiration library, and do not enter direction recommendation, sketch generation, final effect-image generation, or downstream design freezing until the workflow has completed a Mobbin-backed inspiration pass. Treat Mobbin only as direction evidence rather than the formal design source. Then derive three comparable direction candidates from that inspiration pass, mark one as the primary recommendation, and use the approved reference images plus `@product-design` constraints to generate one representative reviewable local sketch through `$imagegen`. That sketch must still behave as commercial product UI/UX under the confirmed Product Design brief rather than as a loose concept board. Optionally enrich that exploration with the pre-direction Creative Production branch when the workflow needs richer commercial visual evidence, confirm that representative sketch with the user as the final product design direction baseline, and only then use `gpt-image-2-generator` to generate the representative final effect image that becomes the frozen visual baseline for downstream work. The final effect image must remain inside the same `@product-design` brief, accepted direction, and commercial product UI/UX standard instead of reinterpreting the page as a marketing visual. Only after that write the confirmed direction into `DESIGN.md`. For iPhone-first mobile work, offer at least these common presets in manual mode unless the user already chose a viewport: `375 x 667 px` (SE / compact), `390 x 844 px` (standard iPhone baseline), `393 x 852 px` (Pro baseline), and `430 x 932 px` (Pro Max baseline). In `--auto` or `--full-auto`, when the run does not already have a frozen viewport, default the global design viewport to `390 x 844 px`. In `--full-auto`, when the design brief, public shell, or final direction already have one uniquely supported default backed by the current artifacts, apply that confirmation directly and continue; if multiple plausible defaults remain, stop and record the ambiguity as a blocker. If downstream freeze still needs normalization for the frozen packet, convert the approved image evidence and confirmed direction into one image-backed design packet, build the mandatory shared Pencil design source, confirm human acceptance of that Pencil file, and route through shared single-resource generation only when the confirmed review result still requires bitmap assets. The shared/global design freeze packet is limited to theme, public-shell, shared-component, and shared interaction-principle design; do not generate any page design during that shared/global freeze step. After the shared design freeze has passed, prefer starting project initialization and bootstrap preparation as soon as the shared public baseline is explicit, rather than waiting for every later module milestone. Only after the shared design freeze has passed may the workflow start module `impl.md` generation, the mandatory native HTML module prototype stage, implementation-stage module effect-image generation, module Pencil design generation, module freeze, `pencil_restoration_ready`, architecture, and later `display_restoration_blueprint` preparation. The native HTML stage is now the module-stage interaction and layout gate, while module-scoped effect-image generation and module-scoped bitmap generation belong immediately after that HTML confirmation and before Pencil restoration. After normalization, inspect the matching artifact directories for static visual evidence before deciding whether any regeneration is necessary.

Effect images are mandatory across the workflow. If the target design-device preset or base resolution has not yet been frozen for the current global design cycle, stop before Product Design direction confirmation, sketch generation, or final effect-image generation and request it first. If the Product Design brief has not yet been confirmed through `@product-design` `get-context`, stop and route there before asking for confirmation. If the common public shell has not yet been explicitly agreed, stop and request shell confirmation before confirming design direction or generating images. If final product design direction is not explicitly confirmed from the approved representative sketch, stop and request confirmation before emitting `DESIGN.md`, entering shared Pencil design execution, or entering any later structured design-source normalization work. Before every representative-sketch or final effect-image generation step, explicitly collect the already-frozen shared visual constraints from the global design packet and pass them forward as required inputs instead of letting the image tools infer them from scratch. Every final effect image must keep the frozen design width unchanged and must not use a canvas height smaller than the frozen base viewport height. Each completed effect-image step must first output a matching atlas extraction analysis, and only after that analysis is confirmed may it output the matching solid-background atlas plus manifest and slicing config: the atlas must preserve the frozen width, use one preset least-conflicting flat background color, keep only stable UI layers, use rectangular non-overlapping cells, and leave runtime-data regions as placeholders rather than baked slices. After the solid atlas bundle is confirmed, route through `$imagegen` to produce the transparent atlas result and confirm that result before minimum-cell slicing begins. When the target page or region is scrollable, the design image may extend vertically beyond that minimum height to show the intended scrolling content, but it must still preserve the frozen width and must not compress the layout just to avoid extra height. In manual mode, first generate the representative page sketch from the approved reference images through local `$imagegen` and wait for explicit user confirmation or revision feedback; that confirmation step should expose the three Mobbin-backed direction candidates with one primary recommendation instead of a single hidden answer. Once that representative sketch is explicitly confirmed, generate the representative final effect image through `gpt-image-2-generator`, freeze that final effect image as the sole visual baseline for the current design cycle, close alternative-direction browsing, delete obsolete alternative sketches or effect images that are no longer part of the frozen packet, and allow only same-direction completion work unless the user explicitly rejects the confirmation or restarts the design cycle. In `--auto`, if the recommendation pass already produced one clear primary direction from the three Mobbin-backed candidates, adopt it directly, generate the required representative sketch automatically after the route reaches the sketch stage, and then generate the representative final effect image after that sketch is accepted by the active execution mode. In `--full-auto`, if the route lock, recommendation artifacts, and existing shell or brief artifacts collapse the human-facing choice to exactly one supported default, auto-confirm that default and continue without a manual stop. Pre-confirmation representative sketches must be produced through local `$imagegen`; final effect images must be produced through `gpt-image-2-generator`, and any final-generation access or credential blocker must be recorded as a blocker for the workflow. Save representative sketches with a `-draft` suffix and final effect images with the corresponding page names under `docs/project/`, then index both for any post-review selected generated asset set, the display evidence pack, and human visual inspection when needed.

When the user explicitly needs campaign-ready visuals, marketing routes, or polished asset packs, prefer the `Creative Production` branch over direct preview-image generation. Before final product direction confirmation, the branch may act only as reviewable direction input. After `DESIGN.md`, use `Creative Production:explore` as the controlled asset-production entry point, then route into a focused explorer and finally to `generative-polish` only after one direction or deterministic base is selected. Keep both windows behind the same design-direction gates: they may inherit the confirmed product direction and `DESIGN.md`, but they must not silently redefine them.

Every representative-sketch or final effect-image generation request must explicitly include existing image-backed design constraints: `art_direction`, `visual_system`, `cta_posture`, palette direction, typography mood, component family cues, image-treatment posture, and the approved reference-image baseline when those values already exist. Those constraints must be read from the current frozen global-design packet first, then narrowed only by the active page or module needs; if the global packet cannot supply the required visual constraints, stop and repair the packet instead of generating a speculative image. Every request must also carry the frozen design width plus the frozen base viewport height as the minimum output height. When the design target includes a scrollable page or scrollable region, allow a taller output height to show the designed scroll range, but do not shrink width or reduce height below the frozen minimum in order to fit more content into one screen. Representative sketch requests must go through local `$imagegen`, and the post-confirmation final effect-image request must inherit the same constraints plus any accepted revision notes before calling `gpt-image-2-generator`. Both stages must stay inside the confirmed `@product-design` brief and must target mature commercial product UI/UX rather than speculative concept art. If `gpt-image-2-generator` or its required environment cannot generate the required final effect images, stop and record a blocker for the workflow. All workflow final effect images must use light mode unless the user explicitly changes that requirement upstream.

For module implementation, high-fidelity visual fidelity is still the first design-freeze priority, and the pre-implementation module path now requires visual confirmation work before freeze. Before queueing or applying `module_design_frozen`, verify that the global design freeze is already complete, that the module `impl.md` already fixed the module function, states, interaction path, non-display behavior boundaries, and platform-aware information-density decisions under the frozen shared design and interaction principles, that a native static HTML module prototype has been generated and accepted for the active module, and that the implementation-stage module effect image, atlas extraction analysis, atlas evidence, display evidence pack, and module Pencil design source already exist strongly enough to support later restoration planning. If any of those inputs are missing, vague, or weaker than the implementation target requires, keep the module unfrozen and route back to the correct scope-matched revision. After the module has entered implementation, require the selected structured design-source packet, the display evidence pack, and the approved implementation-stage module effect image before later display restoration decisions are finalized.

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

The required global public code baseline includes app bootstrap and environment initialization, root router or route host plus redirect policy, global dependency injection or provider scope entry, local storage baseline and persistence wiring, global error mapping and logging baseline, required shared theme or design-token baseline, and the shared shell layer when feature modules depend on an `app-shell` or `root-shell`. Unless the user explicitly overrides the toolchain choice, treat `fvm` as the default Flutter environment contract for project initialization, bootstrap, validation, and implementation commands, and prefer `fvm flutter ...` / `fvm dart ...` over bare `flutter` or `dart`. Add network baseline and API client wiring only when the project or target modules actually require remote data, API access, upload, sync, or other network capabilities.

`project_initialized` is directory-only: `flutter-init` may create the project shell, directory skeleton, and the sibling `skills/flutter-dev/` beside `flutter-init`, but it must stop before bootstrap code, shared wiring, feature code, or page code. Unless the user explicitly requires another toolchain contract, initialization should assume an `fvm`-managed Flutter environment and keep generated command guidance aligned with that default. Those global code responsibilities belong to the separate bootstrap code stage.

As soon as the shared design freeze is complete and the shared bootstrap-critical baseline is explicit enough, prefer `flutter-init` and bootstrap preparation before later module architecture milestones. Treat project initialization and bootstrap as early public-code preparation, not as a late afterthought.

When implementation work should begin, the entry sequence is fixed: route through `@superpowers` to produce `Spec` first, then through `@superpowers` again to produce `Plan`, and only then execute implementation with sibling `flutter-dev` and `flutter-project-guardrails`. Treat the modules as one serial implementation loop rather than a parallel batch. For each active module in order: first confirm the module `impl.md` as the detailed functional contract, then build and confirm the native static HTML module prototype in plain `HTML/CSS/JS`, then run the implementation-stage visual restoration loop to generate or refresh the module effect image, produce and confirm the matching atlas extraction analysis, generate and confirm the matching solid-background `UI-only sheet atlas`, run and confirm `$imagegen` background removal, run minimum-cell atlas slicing, confirm the display evidence pack, execute module Pencil review and repair, and generate only the still-required module bitmap assets, then require `pencil-design-to-flutter-restoration` to produce a restoration contract that explicitly evaluates Flutter standard library fit, third-party plugin fit, and approved bitmap usage, then require `flutter-uiux-to-architecture` to materialize and confirm a page-level `display_restoration_blueprint`, then land non-display-layer code against that blueprint, and only after that restore the display layer from the same approved blueprint rather than re-interpreting upstream design artifacts in code. Implementation execution inside that active module should stay serial by default unless the same module's ownership split is explicitly proven safe. Before display-layer code begins, inspect the corresponding native HTML prototype, implementation-stage module effect image, frozen Pencil design, matching atlas manifest, `display_restoration_blueprint`, and frozen design evidence when such evidence exists. If the selected design-source restoration already exported approved image assets, implementation should use those local assets directly. If an internal illustration, icon asset, texture, or bitmap fallback still needs generation or rework, let the active MCP / design tool chain choose the concrete generation mechanism as long as the result still satisfies the frozen design principles and implementation target. If non-display implementation drifts away from the frozen interaction or layout contract captured by that blueprint, fix the non-display code or route back to design-source control instead of allowing display-layer code to absorb the drift. After the display layer lands and screenshots exist, run `flutter_render_vs_frozen_design_qa` before final handoff, then run `@product-design` `design-qa` as a blocking helper when both a source visual target and implementation screenshots exist, and only then return to explicit human visual inspection rather than introducing a new automatic workflow stage.

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
