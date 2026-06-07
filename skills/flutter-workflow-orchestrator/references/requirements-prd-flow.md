# Requirements PRD Flow

Use this reference when the first workflow node receives raw requirements, a one-line feature idea, a partial brief, or any request that lacks a PRD artifact.

## Goal

Transform unclear demand into a PRD that is specific enough for `flutter-prd-rd-writer` to expand into the global technical baseline. This node resolves product ambiguity; it must not perform technical architecture, executable module document generation, detailed design-source work, or implementation planning.

## Internal Flow

1. Capture the raw requirement exactly enough to preserve the user's intent.
2. Brainstorm the requirement space across users, jobs-to-be-done, core scenarios, non-goals, data needs, platform expectations, UX posture, success criteria, and risks.
3. Build a question ledger that separates decision-blocking questions from questions that can be answered by low-risk defaults.
4. Resolve every decision-blocking question from user-provided context, existing project docs, or explicit user confirmation.
5. For low-risk defaults, write the assumption, rationale, and risk into the PRD instead of leaving the point implicit.
6. Define the first PRD scope boundary: what belongs in this PRD, what is explicitly out of scope, and what should become a later module or follow-up.
7. Generate or update the PRD artifact.
8. Queue `pending_next_stage=prd_ready` only after the PRD artifact exists and the question ledger has no unresolved decision-blocking items.

## Brainstorming Checklist

Cover these dimensions before writing the PRD:

- target users and roles
- user goals and primary jobs-to-be-done
- happy-path scenarios
- edge cases and failure states
- business objective or success metric
- platform and validation surface hints
- required data, permissions, and integrations
- content, localization, accessibility, privacy, and compliance constraints when relevant
- UX posture, information density, and interaction expectations
- explicit non-goals
- dependencies, assumptions, and risks

## Question Ledger

Classify every open question:

| Type | Meaning | Action |
| --- | --- | --- |
| `decision_blocking` | The answer changes product scope, core behavior, user role, platform target, data model, compliance posture, or implementation order. | Stop and request the missing input unless the user has already approved a default. |
| `defaultable` | A conservative assumption can be made without changing the core product promise. | Write the default, rationale, and risk into the PRD. |
| `deferred` | The question matters later but does not block PRD creation. | Record it as an explicit follow-up or later-stage decision. |

## PRD Artifact Contract

The generated PRD must include:

- problem statement
- target users and roles
- goals and non-goals
- core user stories or scenarios
- functional requirements
- edge cases and error states
- data and integration assumptions
- platform and validation-surface assumptions when known
- UX direction hints without freezing detailed UI
- success metrics or acceptance criteria
- resolved question ledger
- remaining deferred questions
- explicit assumptions and risks

## Routing Outcome

Use one of these outcomes:

- `advanced`: PRD artifact exists, decision-blocking questions are resolved, queue `pending_next_stage=prd_ready`.
- `blocked`: decision-blocking questions remain unresolved, record `required_inputs`, keep `current_stage=requirements_brainstorming`.
- `not_executed`: the PRD generation did not really run or did not produce an artifact; keep the current stage unchanged.

## Hard Rules

- Do not call technical baseline, taste direction, executable module document generation, architecture, or implementation skills from raw demand before this flow produces a PRD artifact.
- Do not bury unresolved product questions inside later RD, architecture, or code planning.
- Do not invent business-critical answers. Ask or stop when the answer changes scope, roles, behavior, data, platform, compliance, or delivery order.
- Do not freeze detailed screen design in the PRD. Capture product direction and constraints only; final product design direction confirmation and Stitch design-source work belong to later workflow nodes.
