---
name: flutter-taste-router
description: Use when a Flutter project needs a taste-first shared design direction, mobile design packet, or design-freeze input derived from the taste-skill family. This skill selects the right taste-skill, consolidates its output, and returns a freeze-ready design packet for downstream Flutter workflow skills.
---

# Flutter Taste Router

## Overview

This skill is the taste-first routing and consolidation layer for the Flutter workflow.

It does not replace the taste-skill family. It decides which taste-skill should lead the current design task, then normalizes the result into one Flutter-facing design packet that downstream skills can freeze, split, refine, and implement against.

In the default Flutter workflow, this textual normalization pass must happen before every global design freeze and every module design freeze, even when static images already exist.

For module freeze preparation, the normalized packet must expose the high-fidelity visual contract as the first freeze concern. Do not leave visual fidelity as an implementation polish note.

Use this skill instead of calling `mobile-ui-design-coach` directly in the default workflow.

## Routing Targets

Select the primary taste source by task type:

- `design-taste-frontend`
  Use for shared visual posture, anti-template rules, typography direction, layout language, color discipline, and interaction taste.

- `imagegen-frontend-mobile`
  Use when the task needs mobile screen concepts, multi-screen flows, or image-based mobile design exploration.

- `brandkit`
  Use when brand identity, visual-world direction, logo posture, or palette system must shape the UI direction first.

- `redesign-existing-projects`
  Use when the task is redesigning an existing app or product surface instead of defining a greenfield direction.

Optional:

- `design-preview-to-global-guidelines`
  Use only after a direction is chosen and static visual evidence should be frozen into global artifacts.

## Required Inputs

- PRD or feature brief.
- Global technical baseline when it already exists.
- Product type, audience, and usage context.
- Any screenshots, references, preview comps, or existing app surfaces.
- Platform choice when explicit; otherwise mobile work must default to strict iOS HIG behavior baseline until the user explicitly approves another platform baseline.
- Platform identifier when the target validation surface is known. Use explicit values such as:
  - `android_emulator`
  - `android_device`
  - `ios_simulator`
  - `ios_device`
  - `windows_desktop`
  - `macos_desktop`
  - `linux_desktop`
  - `web_browser`
  - `custom`
- Whether the deliverable is:
  - direction only
  - image exploration
  - freeze-ready design packet
  - redesign of an existing app
- Optional target output directories for shared and module-level visual evidence. If not provided, default to:
  - shared/global: `docs/rd/`
  - module-local: `docs/rd/modules/<module>/`

## Workflow

1. Identify the dominant design job:
   - shared taste direction
   - mobile image exploration
   - brand-first direction
   - redesign of an existing surface
2. Choose the primary taste skill.
3. Apply that skill's direction rules without letting multiple taste skills compete for authority in the same pass.
4. Normalize the result into one Flutter-facing design packet.
5. Validate that `platform_baseline` and `platform_identifier` are not being conflated:
   - `platform_baseline` is the design-behavior baseline
   - `platform_identifier` is the actual validation or delivery surface
   - if the workflow is targeting desktop, browser, or a specific emulator/device surface, do not leave `platform_identifier` implicit
6. Before a freeze decision, inspect the matching shared or module directory for existing static page images that already satisfy the needed evidence.
7. If shared/global freeze still lacks static evidence, check `IMAGE_BASE_URL` and `IMAGE_API_KEY`.
8. If both environment variables exist, call `gpt-image-2-generator` to generate light-mode page-specific app preview images. For shared/global freeze, generate no more than 3 images total before selecting the approved direction. Save each file with its page or screen name, and when one module page is chosen as the global reference, save that selected preview under `docs/rd/` and copy the same file into the related module directory.
9. If shared/global freeze still lacks static evidence and either environment variable is missing, stop and return a blocker instead of pretending the packet is ready for global freeze.
10. For module freeze, if image generation credentials are missing, continue with the textual design packet only when the packet is already explicit enough.
11. For module refinement or module freeze preparation, do not generate new module previews by default. Only generate them when the current workflow explicitly enables `--perviewer`.
12. During module freeze preparation, include a `high_fidelity_visual_contract` that locks hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and any approved Flutterization or bitmap fallback.
13. If `--perviewer` is active for module-stage preview generation, record that opt-in plus the generated module preview paths into `global-design-guidelines.md` instead of leaving the policy implicit.
14. Whenever the workflow calls image generation, write the design packet's style constraints into the generation input explicitly instead of relying on loose reference behavior. At minimum, the generation input must carry forward:
   - `art_direction`
   - `taste_constraints`
   - `visual_system`
   - `cta_posture`
   - the approved palette direction
   - typography mood
   - component family cues
   - image treatment rules when they already exist
15. If module-level previews are generated after a global direction already exists, those module previews must inherit the global style system instead of redefining a new visual world.
16. If static visual evidence is approved and should become reusable frozen global guidance, route the result into `design-preview-to-global-guidelines`.
17. If the packet is still too weak for freeze, return one scope-matched revision plan instead of pretending it is ready.

When `--auto` is active:

- if shared freeze requires static visual evidence and it is missing, this skill should first inspect the target directories, then call `gpt-image-2-generator` only when both image environment variables exist, generate no more than 3 shared app preview images automatically, and fold those images into `visual_evidence`
- if module freeze is being prepared, this skill may determine UI/UX directly from the design packet without static images, as long as hierarchy, CTA posture, state scope, and component freeze are explicit enough
- if module freeze is being prepared, the packet must include `high_fidelity_visual_contract`; if that contract cannot be made explicit, return a blocker or revision plan instead of freeze readiness
- if module refinement or module freeze is running without `--perviewer`, this skill must not auto-generate new module previews
- if module refinement or module freeze is running with `--perviewer`, this skill may generate module previews only after confirming the shared/global style system remains authoritative
- if the environment variables are missing during shared/global freeze and no approved effect images exist yet, this skill should stop and mark shared freeze blocked
- if the environment variables are missing during module freeze, this skill should continue with the normalized textual packet only when the packet is already explicit enough

## Downstream Consumers

The consolidated design packet is the default upstream source for:

- `flutter-design-freeze-gate`
- `flutter-rd-module-splitter`
- `flutter-design-source-control`
- `flutter-uiux-to-architecture`
- optional `design-preview-to-pen`

## Design Packet Contract

Every successful run must return one packet with at least:

- `design_brief`
- `platform_baseline`
- `platform_identifier`
- `primary_taste_source`
- `art_direction`
- `taste_constraints`
- `information_hierarchy`
- `cta_posture`
- `visual_system`
- `state_matrix`
- `component_freeze_scope`
- `high_fidelity_visual_contract`
- `allowed_engineering_adjustments`
- `visual_evidence`
- `acceptance_gates`
- `style_generation_constraints`

### Minimum meanings

- `platform_baseline`
  Default to strict iOS HIG behavior rules for safe areas, touch targets, navigation, readability, feedback, and accessibility unless the user explicitly chooses another platform baseline. Do not soften this into a vague “Apple-like” preference.

- `platform_identifier`
  The exact target validation surface for downstream implementation and review. Do not use `platform_baseline` as a substitute. For mobile work, it may stay `needs_confirmation` early in the design cycle, but before architecture or implementation it should be explicit.

- `taste_constraints`
  The anti-template rules, composition rules, density/motion posture, typography discipline, color discipline, and visual prohibitions inherited from the selected taste skill.

- `state_matrix`
  Must include at least ideal, empty, loading, error, permission, partial data, disabled, success, and locked or premium states when relevant.

- `component_freeze_scope`
  Must identify which repeated controls or building blocks are globally shared, module-private, or intentionally local.

- `high_fidelity_visual_contract`
  For module freeze, must lock implementation-facing hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and approved Flutterization or bitmap fallback.

- `style_generation_constraints`
  Must make image-generation style constraints explicit enough to be written into prompts. At minimum, include palette direction, typography mood, component family cues, and image-treatment posture whenever those decisions already exist.

## Hard Rules

- Do not let multiple taste skills define competing visual directions in the same pass.
- Do not confuse `platform_baseline` with `platform_identifier`.
- Do not relax the default iOS HIG mobile baseline unless the user explicitly approves another platform baseline.
- Do not leave desktop, browser, or emulator-specific validation targets implicit once the workflow is entering freeze or implementation preparation.
- Do not let a raw image-generation skill become the only source of freeze truth; always normalize its output into the design packet.
- Do not use `design-taste-frontend` alone as if it already contains mobile freeze artifacts; it is a direction source, not the final packet.
- Do not use `imagegen-frontend-mobile` alone as if generated images already define state scope or handoff rules; convert them into the packet.
- Do not send image generation requests from the Flutter workflow without explicitly embedding the current style constraints into the prompt or structured fields.
- Do not let module-generated previews drift away from the approved global style system once the shared direction exists.
- Do not skip platform baseline, state matrix, or allowed engineering adjustments.
- Do not claim freeze readiness when hierarchy, contrast, CTA clarity, or state coverage are still ambiguous.
- Do not claim module freeze readiness when `high_fidelity_visual_contract` is missing, vague, or deferred to implementation polish.
- Do not reopen shared brand direction inside a module-specific refinement pass unless the problem is genuinely global.
- Do not route to code or architecture directly from taste exploration without producing the packet first.
- Do not skip the textual normalization pass before looking at static visuals.
- Do not generate new app previews before checking whether the target directories already contain usable page images.
- Do not treat dark-mode previews as the default workflow evidence set; default generated and selected workflow previews must remain in light mode unless the user explicitly overrides that choice.
- Do not let shared/global freeze proceed without approved effect images.
- Do not generate more than 3 new shared/global preview images before choosing the global direction.
- Do not continue shared/global freeze when `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing and approved effect images still do not exist.
- Do not generate generic mood boards or unnamed collages when the workflow needs app-page evidence; generate page-specific app previews named after the corresponding page.
- In `--auto` mode, do not stop for missing shared static visuals when `gpt-image-2-generator` can generate them; generate the missing page previews and continue.
- In `--auto` mode, allow module freeze to proceed without static images when the packet is already explicit enough.
- Do not generate new module-stage previews unless `--perviewer` is explicitly active for the current workflow run.

## Output Contract

Return:

- `primary_taste_source`
- `selected_supporting_skills`
- `design_packet`
- `freeze_readiness`
- `missing_items`
- `next_skill`

## Pressure Scenarios

- User asks for mobile app direction with no visuals yet: prefer `imagegen-frontend-mobile`, then normalize into the packet.
- `--auto` mode reaches shared freeze with no static mobile previews: inspect the target directories, then call `gpt-image-2-generator` only when both image environment variables exist, generate no more than 3 shared page app preview images, and normalize them into the packet. If credentials are missing, block shared freeze instead of continuing.
- `--auto` mode reaches module freeze with no static mobile previews: determine UI/UX from the consolidated packet first; generate images only if the packet is still too ambiguous to freeze.
- Module freeze packet says "make it high fidelity during implementation": return a blocker or revision plan; high-fidelity visual fidelity must be explicit before design freeze.
- A module preview starts drifting in palette or typography from the chosen global preview: treat that as a style-system violation, regenerate with the explicit global style constraints, and do not accept the drift as a new direction.
- User asks for a Flutter shared direction with strong verbal style cues but no image request: prefer `design-taste-frontend`, then normalize into the packet.
- User asks for redesign of an existing app: prefer `redesign-existing-projects`, then normalize into the packet.
- User asks for branding first: use `brandkit`, then convert the brand direction into UI-facing taste constraints.
