---
name: gpt-image-2-generator
description: Use when Codex needs to generate concept art, design previews, UI mockups, hero images, marketing visuals, icons, or illustration drafts with gpt-image-2, especially when the request should run through a custom OpenAI-compatible base URL and API key loaded from environment variables and the output needs to be written to local image files.
---

# GPT Image 2 Generator

## Overview

Generate local image files with `gpt-image-2` through the bundled `scripts/image_gen.py` helper. This skill is a focused generation workflow through `/images/generations`, narrowed to explicit prompt shaping and local file output.

When the upstream OpenAI-compatible endpoint supports transparent backgrounds, this skill may pass through `background=transparent` for PNG or WebP outputs. Transparency success depends on endpoint support rather than on this local wrapper alone.

## Quick Start

- Confirm both environment variables exist before running anything:
  - `IMAGE_BASE_URL`
  - `IMAGE_API_KEY`
- Start with a dry run when the prompt is new, text-heavy, or uses a custom size.
- Save single-image jobs with `--out` and multi-image jobs with `--out-dir`.

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "A polished mobile banking dashboard in a bright editorial 3D style" \
  --dry-run
```

## Workflow

1. Clarify the target artifact: subject, use case, style, aspect ratio, visible text, and anything the image must avoid.
2. When the request is broad or under-specified, read `references/prompt-patterns.md` and translate the request into structured fields instead of relying on one long freeform prompt.
3. Prefer the structured prompt flags when control matters: `--use-case`, `--scene`, `--subject`, `--style`, `--composition`, `--lighting`, `--palette`, `--materials`, `--text`, `--constraints`, and `--negative`.
4. Run `--dry-run` first for unusual sizes, `--n > 1`, or text-in-image requests so the payload can be reviewed before spending tokens.
5. Run the live generation request and write outputs to an explicit local path.
6. Report the output path, the final prompt summary, and any quality risks that still need a second pass.

## Flutter Workflow Usage

When this skill is called from the Flutter workflow:

1. Treat the target as app-page visual evidence, not a generic collage.
2. If the upstream workflow is still at the pre-confirmation representative-sketch stage, stop and return control so local `$imagegen` can generate that sketch first. This skill owns only the post-confirmation final effect-image step in that flow.
3. In the Flutter workflow, do not treat this as a standalone art generator. The final image must stay inside the confirmed `@product-design` brief, accepted visual direction, and commercial product UI/UX constraints.
4. Generate one file per page or screen and name the output file after that page or screen.
5. Use light mode as the default visual baseline for all workflow previews unless the upstream request explicitly overrides that requirement.
6. Save shared or global reference images under `docs/project/`.
7. Save module-specific page images under `docs/project/modules/<module>/`.
8. If one generated module page is selected as the global reference, copy that same image into both locations:
   - `docs/project/<page-name>.<ext>`
   - `docs/project/modules/<module>/<page-name>.<ext>`
9. If `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing, do not send a request. Return control so the upstream workflow can continue without generated images.
10. Prefer prompts that describe a concrete app page, state, and information hierarchy. Avoid mood-board phrasing when the output will drive implementation.
11. When the request is for shared/global design freeze, generate no more than 3 preview images in total before the workflow chooses the approved direction.
12. When the request comes from the Flutter workflow, explicitly write the inherited style constraints into the prompt or structured fields. At minimum, include:
   - `art_direction`
   - `taste_constraints`
   - `visual_system`
   - `cta_posture`
   - palette direction
   - typography mood
   - component family cues
   - image-treatment posture when available
13. If the request is for a module preview after a shared direction already exists, preserve the same visual world instead of inventing a new palette, typography mood, component family, or image-treatment language.
14. If the request is for module refinement or module freeze image evidence, require explicit upstream approval for that evidence path. Without that approval, return control so the upstream workflow can continue without generating new module images.

## Command Patterns

### Single image

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "A clean fintech hero illustration with two devices on a desk" \
  --out output/imagegen/fintech-hero.png
```

### Structured prompt

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "Design preview for a premium sleep tracking app" \
  --use-case "Mobile App Store preview" \
  --subject "Three iPhone screens showing onboarding, dashboard, and bedtime routine" \
  --style "Premium product render with soft realism" \
  --composition "Front-facing triptych with centered hero focus" \
  --lighting "Soft diffused studio light" \
  --palette "Deep navy, cyan, coral accent" \
  --constraints "Readable UI hierarchy, no extra floating cards" \
  --negative "warped phones, unreadable text, busy background" \
  --out output/imagegen/sleep-preview.png
```

### Multiple images

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "Sticker-style mascot for a developer tooling brand" \
  --n 3 \
  --out-dir output/imagegen/mascot-set
```

### Transparent background

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "A floating reward badge icon, isolated, no shadow spill" \
  --background transparent \
  --output-format png \
  --out output/imagegen/reward-badge.png
```

### Flutter page evidence

```bash
rtk python skills/gpt-image-2-generator/scripts/image_gen.py \
  --prompt "Rewards home page for a mobile lifestyle app" \
  --use-case "Flutter module freeze visual evidence" \
  --subject "Single mobile app page named rewards-home with header, progress card, offers list, and bottom action area" \
  --style "High-fidelity mobile product preview" \
  --composition "One app page per file, front-facing, readable hierarchy" \
  --constraints "No collage, no second screen, preserve realistic mobile spacing" \
  --out docs/project/modules/rewards/rewards-home.png
```

## Environment Rules

- `IMAGE_BASE_URL` and `IMAGE_API_KEY` are required. Do not hardcode them and do not pass secrets through prompt files.
- `IMAGE_BASE_URL` should point to the API root, for example `https://your-endpoint.example/v1`. The script appends `/images/generations` automatically unless the value already ends with that path.
- The bundled script targets `gpt-image-2` only and calls the image generation endpoint. Transparent backgrounds may be requested through this skill when the configured OpenAI-compatible endpoint supports `background=transparent`.
- Upstream workflow skills should check whether both environment variables exist before invoking a live generation request. If either value is missing, skip generation instead of treating that as a blocker.

## Hard Rules

- Do not silently substitute another model when the request explicitly requires `gpt-image-2`.
- Do not send a live request when either environment variable is missing.
- Do not generate dark-mode workflow previews by default. Use light mode unless the upstream workflow explicitly requests another mode.
- Do not generate more than 3 shared/global workflow previews for one global freeze cycle.
- Do not send Flutter workflow generation prompts without explicit style constraints when the design packet already defines them.
- Do not let module preview generation drift away from the approved shared/global style system.
- Do not generate new module-stage Flutter images unless the upstream workflow explicitly approved that evidence path.
- Do not claim text rendered inside an image is correct unless it was visually checked afterward.
- Do not claim transparent output is guaranteed. This skill only passes through generation requests and depends on endpoint support for transparent backgrounds.
- Do not bypass script validation for custom sizes; let the helper reject invalid dimensions first.
- Do not generate unnamed image sets when the Flutter workflow needs page-addressable evidence for module freeze or display-layer implementation.
- Do not generate a multi-screen board when the downstream task expects one app page per file.

## References

- Read `references/prompt-patterns.md` when prompt quality is the main bottleneck.
- Read `references/environment-and-outputs.md` when the endpoint format, output naming, or response handling is unclear.
