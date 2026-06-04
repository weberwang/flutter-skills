---
name: flutter-taste-router
description: Use when a Flutter project needs a taste-first shared design direction, mobile design packet, or design-freeze input derived from the taste-skill family. This skill selects the right taste-skill, consolidates its output, and returns a freeze-ready design packet for downstream Flutter workflow skills.
---

# Flutter Taste Router

## Overview

This skill is the taste-first routing and consolidation layer for the Flutter workflow.

It does not replace the taste-skill family. It decides which taste-skill should lead the current design task, then normalizes the result into one Flutter-facing design packet that downstream skills can freeze, split, refine, and implement against.

In the default Flutter workflow, this textual normalization pass must happen before every global design freeze and every module design freeze, even when static images already exist.

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
- Platform choice when explicit, otherwise default to iOS HIG behavior baseline for mobile behavior.
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
5. Before a freeze decision, inspect the matching shared or module directory for existing static page images that already satisfy the needed evidence.
6. If static evidence is missing, check `IMAGE_BASE_URL` and `IMAGE_API_KEY`.
7. If both environment variables exist, call `gpt-image-2-generator` to generate page-specific app preview images, save each file with its page or screen name, and when one module page is chosen as the global reference, save that selected preview under `docs/rd/` and copy the same file into the related module directory.
8. If either environment variable is missing, continue with the textual design packet instead of blocking on image generation.
9. If static visual evidence is approved and should become reusable frozen global guidance, route the result into `design-preview-to-global-guidelines`.
10. If the packet is still too weak for freeze, return one scope-matched revision plan instead of pretending it is ready.

When `--auto` is active:

- if shared freeze requires static visual evidence and it is missing, this skill should first inspect the target directories, then call `gpt-image-2-generator` only when both image environment variables exist, generate the missing page-specific app preview images automatically, and fold those images into `visual_evidence`
- if module freeze is being prepared, this skill may determine UI/UX directly from the design packet without static images, as long as hierarchy, CTA posture, state scope, and component freeze are explicit enough
- if the environment variables are missing, this skill should continue with the normalized textual packet and explicitly note that image generation was skipped because credentials were unavailable

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
- `primary_taste_source`
- `art_direction`
- `taste_constraints`
- `information_hierarchy`
- `cta_posture`
- `visual_system`
- `state_matrix`
- `component_freeze_scope`
- `allowed_engineering_adjustments`
- `visual_evidence`
- `acceptance_gates`

### Minimum meanings

- `platform_baseline`
  Default to iOS HIG behavior rules for safe areas, touch targets, navigation, readability, feedback, and accessibility unless the user explicitly chooses another platform baseline.

- `taste_constraints`
  The anti-template rules, composition rules, density/motion posture, typography discipline, color discipline, and visual prohibitions inherited from the selected taste skill.

- `state_matrix`
  Must include at least ideal, empty, loading, error, permission, partial data, disabled, success, and locked or premium states when relevant.

- `component_freeze_scope`
  Must identify which repeated controls or building blocks are globally shared, module-private, or intentionally local.

## Hard Rules

- Do not let multiple taste skills define competing visual directions in the same pass.
- Do not let a raw image-generation skill become the only source of freeze truth; always normalize its output into the design packet.
- Do not use `design-taste-frontend` alone as if it already contains mobile freeze artifacts; it is a direction source, not the final packet.
- Do not use `imagegen-frontend-mobile` alone as if generated images already define state scope or handoff rules; convert them into the packet.
- Do not skip platform baseline, state matrix, or allowed engineering adjustments.
- Do not claim freeze readiness when hierarchy, contrast, CTA clarity, or state coverage are still ambiguous.
- Do not reopen shared brand direction inside a module-specific refinement pass unless the problem is genuinely global.
- Do not route to code or architecture directly from taste exploration without producing the packet first.
- Do not skip the textual normalization pass before looking at static visuals.
- Do not generate new app previews before checking whether the target directories already contain usable page images.
- Do not block the workflow on static visuals when `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing; continue with the textual packet and mark the gap explicitly.
- Do not generate generic mood boards or unnamed collages when the workflow needs app-page evidence; generate page-specific app previews named after the corresponding page.
- In `--auto` mode, do not stop for missing shared static visuals when `gpt-image-2-generator` can generate them; generate the missing page previews and continue.
- In `--auto` mode, allow module freeze to proceed without static images when the packet is already explicit enough.

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
- `--auto` mode reaches shared freeze with no static mobile previews: inspect the target directories, then call `gpt-image-2-generator` only when both image environment variables exist, generate the missing page app preview images, and normalize them into the packet.
- `--auto` mode reaches module freeze with no static mobile previews: determine UI/UX from the consolidated packet first; generate images only if the packet is still too ambiguous to freeze.
- User asks for a Flutter shared direction with strong verbal style cues but no image request: prefer `design-taste-frontend`, then normalize into the packet.
- User asks for redesign of an existing app: prefer `redesign-existing-projects`, then normalize into the packet.
- User asks for branding first: use `brandkit`, then convert the brand direction into UI-facing taste constraints.
