---
name: mobile-ui-design-coach
description: Use when working on mobile app UI design, especially when a screen feels too native, too plain, or not commercial enough, when refining Pencil MCP prompts, or when choosing visual direction, information density, and anti-native constraints for Flutter or native mobile apps.
---

# Mobile UI Design Coach

## Overview

Turn vague mobile UI requests into a sharper visual direction and a prompt pack that can produce richer, more commercial screens without losing product clarity. Bias toward mobile-native UX and clear hierarchy, not desktop SaaS patterns squeezed onto a phone.

## Quick Start

- If the user already describes a strong direction, skip discovery and move to diagnosis plus prompt generation.
- If the style is unclear, ask one question at a time using the four axes in `references/interview-and-diagnosis.md`.
- If the user mentions `Pencil`, `Pencil MCP`, prompt words, or complains that the UI feels native, plain, or generic, read `references/pencil-prompt-pack.md` before answering.

## Workflow

1. Diagnose why the current result feels native or under-designed.
2. Lock four axes: product posture, information density, visual temperature, and de-native strategy.
3. Propose two or three directions and recommend one.
4. Produce an output pack:
   - direction summary
   - native-feel diagnosis
   - master prompt
   - negative constraints
   - page-level prompts
   - implementation guardrails
5. Keep every recommendation mobile-specific: thumb reach, glanceability, state clarity, and restrained motion matter more than decorative flourish.

## Hard Rules

- Do not default to web dashboard patterns on a phone.
- Do not add gradients, glow, glass, images, or animation without a role.
- For efficiency tools, prefer hierarchy, rhythm, material depth, and information cadence over hero art.
- For high-end efficiency tools, default to no hero imagery and no real photos unless the user explicitly asks for them.
- When the user wants commercial polish, be concrete about typography, spacing, grouping, contrast, and motion.
- If the user asks for richer visuals, decide whether the product should gain polish through layout, material, illustration, or motion. Do not mix all of them by default.

## Deliverables

- For conversational design advice, return the diagnosis, recommended direction, and the next design move.
- For Pencil-facing work, return a prompt pack that can be pasted with minimal edits.
- For Flutter-facing work, add a short implementation note explaining what should be preserved and what should not be copied literally.

## References

- Read `references/interview-and-diagnosis.md` for discovery questions, native-feel diagnosis, and direction archetypes.
- Read `references/pencil-prompt-pack.md` for reusable prompt templates and a complete high-end efficiency example pack.
