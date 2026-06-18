---
name: reference-image-to-hifi-prototype
description: Use when a reference UI image should be turned directly into a high-fidelity interactive prototype, skipping low-fidelity wireframing while still requiring structure playback, asset fidelity, and final design QA.
---

# Reference Image To Hifi Prototype

## Overview

Turn a reference UI image directly into a high-fidelity interactive prototype.

This skill compresses the old two-step flow of "low-fidelity wireframe first, high-fidelity prototype second" into one high-fidelity build path. It still requires an upfront playback step: first restate the page structure and interaction checklist, wait for explicit confirmation, then use `@product-design` to build the final interactive prototype and run visual QA against the reference.

When the workflow needs a concrete default implementation stack for that prototype, prefer `Vite + React + TypeScript`. This default gives the best balance between fast page assembly and later Flutter restoration, because component boundaries, interaction state, and region ownership stay easier to read back into a `display_restoration_blueprint`. Do not default to Vue unless the project already committed to it. Do not default to plain HTML/CSS/JS, because that makes the prototype faster to start but weaker as a frozen source once Flutter restoration needs stable structure and state semantics.

## When To Use

- The user already has a concrete screenshot, mockup, or UI reference image.
- The user wants the final output to be a high-fidelity interactive prototype rather than a low-fidelity wireframe.
- The user wants the structure and interaction plan repeated back before implementation starts.

Do not use this skill when:

- The visual target is still ambiguous.
- The user wants broad style exploration instead of faithful reconstruction.
- There is no usable reference image yet.

## Required Inputs

Before building the prototype, make sure these inputs are explicit:

- reference image or screenshot
- target page or flow purpose
- expected interaction level
- any provided assets
- any required platform or layout constraints

If any required input is missing, stop and request it instead of improvising.

## Workflow

1. Route through `@product-design get-context` to confirm the design brief for this exact request.
2. Inspect the reference image and extract:
   - information architecture
   - layout hierarchy
   - navigation model
   - primary content regions
   - control set
   - operation path
   - implied missing states
3. Before implementation, output two review sections only:
   - page structure playback
   - interaction checklist
4. Wait for explicit user confirmation.
5. After confirmation, route through `@product-design image-to-code` as the implementation owner.
6. Build the prototype directly as high-fidelity interactive UI. Do not spend a separate step on low-fidelity wireframing.
7. Prefer user-provided real assets. If a required independent asset is still missing and cannot be exported locally, allow the downstream workflow to call the designated image-generation path only for that missing asset.
8. Require final `@product-design design-qa` and iterate until the prototype visually matches the reference as closely as practical.

## High-Fidelity Requirements

- The prototype must preserve the reference layout, spacing, proportions, colors, typography, radius, borders, shadows, imagery, icon placement, and component states.
- Buttons, inputs, tabs, dropdowns, filters, popups, back actions, and submit actions must remain interactive.
- If the reference implies missing states, add reasonable:
  - loading state
  - empty state
  - error state
  - success state
  - popup or modal state when relevant
- Desktop and mobile layouts must both remain usable and structurally faithful.

## Asset Rules

- Prefer provided real assets first.
- Do not fake image assets with CSS crops when the workflow requires real independent asset files.
- If the build depends on missing local image tooling or missing independent assets, note that blocker explicitly and route the asset gap to the agreed asset-generation path instead of silently substituting placeholders.

## Output Contract

Before confirmation, output:

### 1. Page Structure Playback

Summarize:

- page regions
- hierarchy
- navigation
- primary task path
- major content blocks

### 2. Interaction Checklist

Summarize:

- interactive controls
- linked actions
- state coverage
- modal or popup behavior
- responsive expectations

After confirmation, produce:

- a runnable high-fidelity interactive prototype
- final design QA result against the reference image

## Hard Rules

- Do not create a separate low-fidelity wireframe stage.
- Do not implement before the structure playback and interaction checklist are explicitly confirmed.
- Do not drift away from the reference image's visual system.
- Do not replace missing real assets with CSS simulation when the requirement says assets must be real files.
- Do not skip `@product-design design-qa`.
- Do not hand off before at least one QA-and-fix loop has been completed against the reference.

## Common Blockers

Return `blocked` when:

- reference image is missing
- structure or interaction expectations are too incomplete to confirm
- required assets are missing and no approved fallback path exists
- the user has not confirmed the structure playback plus interaction checklist

## Recommended Response Shape

Use this exact interaction order:

1. `Page Structure Playback`
2. `Interaction Checklist`
3. `Please confirm before high-fidelity prototype build`

## Pressure Scenarios

- User says "skip the playback and just build it": block. Confirmation of structure and interactions is mandatory.
- User says "do low-fidelity first anyway": decline within this skill. This skill exists to go directly to high-fidelity.
- User says "good enough, no need for QA": block. Final visual QA is required.
- User says "assets can stay as CSS slices": block when the request requires real independent asset files.
