---
name: product-screenshot-to-page-design
description: Use when uploaded screenshots from an existing product must be extended into a new same-product page, and the run must output style analysis plus a page-structure proposal before generating a local sketch and then the final UI image.
---

# Product Screenshot To Page Design

## Overview

Turn uploaded screenshots from an existing product into a new page concept that still looks like the same product system.

This skill is for page-level visual extension, not for redefining the global product direction. It first extracts the product design language from the screenshots, then proposes the new page structure, generates a local review sketch through `$imagegen`, waits for explicit confirmation, and only then generates the final UI image through `gpt-image-2-generator`.

## When To Use

- The user uploads screenshots from an existing product and wants a new page that belongs to that same product family.
- The new page must inherit the current product's color language, typography hierarchy, component style, spacing rhythm, icon treatment, and visual posture.
- The user explicitly wants analysis first and final image generation second.

Do not use this skill when:

- The user wants to redefine the brand or explore a different visual direction.
- The user has no usable screenshot evidence.
- The task is global design freezing rather than a new page extension.

## Required Inputs

Before final page generation, make sure these inputs are explicit:

- uploaded screenshot references
- page name
- page purpose or core function
- frozen page size or viewport
- PRD-backed functional scope
- required modules
- avoid-list

If any required input is missing, stop and request it instead of improvising.

## Workflow

1. Verify the screenshot set is strong enough:
   - same product family
   - readable hierarchy
   - enough repeated components to infer a stable language
2. Extract the product design language from the screenshots:
   - color usage
   - typography hierarchy
   - card, form, list, button, and navigation patterns
   - corner radius, border, shadow, spacing, icon style
   - illustration or image treatment
   - overall product temperament
3. Map the new page back to the product:
   - page goal
   - main task path
   - required modules
   - critical states if relevant
4. Output a reviewable response in two parts only:
   - style analysis
   - page structure proposal
5. Generate one local review sketch through `$imagegen` using the approved structure and screenshot-derived style constraints.
6. Wait for explicit user confirmation on that sketch.
7. Only after confirmation, invoke `gpt-image-2-generator` to generate the final UI image for the new page.
8. If `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing, stop and report the blocker instead of switching to another generator.

## Output Contract

Before confirmation, output:

### 1. Style Analysis

Summarize the extracted design language in concise sections:

- color system
- typography ladder
- layout and spacing rhythm
- component language
- iconography
- illustration or media style
- product temperament

### 2. Page Structure Proposal

Summarize the new page plan:

- page role
- primary user task
- information hierarchy
- required modules and their order
- interaction emphasis
- states or edge cases that materially affect the layout

### 3. Local Sketch

- one local `$imagegen` sketch for review that follows the extracted product language

After confirmation, generate:

- one final UI image for the new page via `gpt-image-2-generator`

## Hard Rules

- Do not change the brand color direction unless the user explicitly asks for it.
- Do not turn the page into a marketing-style visual when the screenshots are clearly product UI.
- Do not introduce a new visual language that breaks the same-product feeling.
- Do not skip the style-analysis step.
- Do not skip the page-structure proposal step.
- Do not generate the final UI image before the local sketch has been explicitly confirmed.
- Do not skip the local `$imagegen` sketch step.
- Do not use any image generator other than `gpt-image-2-generator` for the final page image in this skill.
- Do not send a live generation request when `IMAGE_BASE_URL` or `IMAGE_API_KEY` is missing.
- Do not infer page function from screenshots alone when PRD-backed function or user-specified function is missing.
- Do not over-decorate the page beyond the screenshot-derived product language.

## Common Blockers

Return `blocked` when:

- screenshots are missing
- screenshots come from materially different directions
- page name or function is missing
- frozen viewport is missing
- required modules are missing
- avoid-list is missing when the user clearly expects constraints
- `IMAGE_BASE_URL` is missing
- `IMAGE_API_KEY` is missing

## Recommended Response Shape

Use this exact interaction order:

1. `Style Analysis`
2. `Page Structure Proposal`
3. `Local Sketch`
4. `Please confirm before final UI image generation`

## Pressure Scenarios

- User says "generate the final image directly": block and output analysis plus structure first.
- User says "use this product as reference, but also make it trendier": block unless they explicitly want a new direction.
- User says "you can infer the feature yourself": block when the page function is not recoverable from the provided product context.
- User says "skip the size for now and generate first": block until the frozen page size is explicit.
- User says "use another image model": block. This skill's final image generation path is `gpt-image-2-generator`.
