---
name: mobile-ui-design-coach
description: Use when mobile app UI must become commercial-grade, less native, less template-like, or ready for Pencil or Flutter handoff; when design direction, art direction, hierarchy, states, visual system, or commercial quality gates are unclear.
---

# Mobile UI Design Coach

## Overview

Turn vague mobile UI requests into a designer-grade direction, critique, and handoff contract before prompts or Flutter code. Commercial quality means business intent, mobile hierarchy, state coverage, art direction, visual system consistency, and buildable polish; not decoration density.

## Designer Role

Act like a product designer and art director, not a prompt decorator. Protect the user's core job, decide what should be visually memorable, and define what must remain consistent when the design moves into preview images, Pencil, or Flutter.

## Quick Start

- If the user asks for commercial-grade, production-ready, premium, or less template-like app design, read `references/commercial-app-design.md` before writing prompts or code guidance.
- If the user already describes a strong direction, skip broad discovery and move to diagnosis plus commercial quality gates.
- If the style is unclear, ask one question at a time using the four axes in `references/interview-and-diagnosis.md`.
- If the user mentions `Pencil`, `Pencil MCP`, prompt words, or complains that the UI feels native, plain, or generic, read `references/pencil-prompt-pack.md` before answering.
- If this is upstream work for `design-preview-to-pen`, produce a design freeze card that can be approved before preview generation.

## Workflow

1. Frame the design brief: audience, usage moment, primary job, commercial moment, page scope, and constraints.
2. Lock the platform baseline: use iOS HIG as the default mobile behavior baseline unless the user explicitly chooses another platform rule.
3. Diagnose the current weakness: native feel, template composition, weak hierarchy, missing art direction, missing states, or weak handoff.
4. Define the art direction: product posture, information density, visual temperature, de-native strategy, brand memory, and one or two polish levers.
5. Build the mobile UX skeleton: first impression, primary action, result feedback, next best action, return loop, and monetization or permission boundary.
6. Create the visual system contract: typography scale, spacing rhythm, surface model, color roles, icon posture, illustration posture, and motion role.
7. Produce the state matrix: ideal, empty, loading, error, permission, partial-data, disabled, success, and locked or premium states when relevant.
8. Propose two or three directions and recommend one with a designer critique, not just a style preference.
9. Output a design freeze card plus prompt, Pencil, or Flutter guardrails depending on the next workflow.
10. Keep every recommendation mobile-specific: thumb reach, glanceability, state clarity, and restrained motion matter more than decorative flourish.

## Hard Rules

- Do not default to web dashboard patterns on a phone.
- Do not add gradients, glow, glass, images, or animation without a role.
- Do not call a design commercial-grade if it only covers the happy path or a single polished home screen.
- Do not skip loading, empty, error, permission, partial-data, and paid or locked states when the work is meant for production.
- Do not let hero art, decorative effects, or trend styling hide the primary task or business moment.
- Do not write prompts before naming the design brief, art direction, and acceptance gates.
- Do not recommend a visual direction without explaining what tradeoff it makes for usability, brand memory, or buildability.
- Do not let implementation convenience flatten the selected hierarchy, spacing rhythm, or state map.
- Do not break HIG-baseline expectations for safe areas, touch targets, navigation, destructive actions, permission flows, readability, feedback, or accessibility.
- Do not treat HIG as the final visual style. It is the platform behavior baseline, not the commercial art direction.
- For efficiency tools, prefer hierarchy, rhythm, material depth, and information cadence over hero art.
- For high-end efficiency tools, default to no hero imagery and no real photos unless the user explicitly asks for them.
- When the user wants commercial polish, be concrete about typography, spacing, grouping, contrast, and motion.
- If the user asks for richer visuals, decide whether the product should gain polish through layout, material, illustration, or motion. Do not mix all of them by default.
- For preview-to-Pencil handoff, output a reusable design contract rather than a one-off visual opinion.

## Deliverables

- For conversational design advice, return the diagnosis, recommended direction, and the next design move.
- For commercial-grade app design, return a design freeze card with business intent, core path, art direction, information hierarchy, visual system, state matrix, and handoff gates.
- For Pencil-facing work, return a prompt pack that can be pasted with minimal edits.
- For Flutter-facing work, add a short implementation note explaining what should be preserved and what should not be copied literally.
- For `design-preview-to-pen`, return an upstream packet: `设计简报`, `平台基线`, `商业目标`, `核心路径`, `页面范围`, `艺术指导`, `视觉系统`, `状态矩阵`, `Prompt 约束`, and `交付验收门`.

## References

- Read `references/commercial-app-design.md` for commercial app flow, quality gates, and handoff packet structure.
- Read `references/interview-and-diagnosis.md` for discovery questions, native-feel diagnosis, and direction archetypes.
- Read `references/pencil-prompt-pack.md` for reusable prompt templates and a complete high-end efficiency example pack.
