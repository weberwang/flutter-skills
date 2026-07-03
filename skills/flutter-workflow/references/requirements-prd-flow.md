# Requirements PRD Flow

Use this reference when the workflow is already inside `requirements_brainstorming` and must turn a confirmed idea sketch brief or an already-concrete feature request into a PRD artifact.

## Goal

Transform a now-concrete product request into a confirmed companion page-navigation-flow artifact first, then into a PRD that is refined from that confirmed navigation and is specific enough for `flutter-prd-rd-writer` to expand into the global technical baseline. This node resolves remaining product ambiguity for PRD quality; it must not perform technical architecture, executable module document generation, detailed design-source work, or implementation planning.

Upstream expectation:

- either `docs/project/idea-sketch-brief.md` already exists and has been confirmed
- or the request was already concrete enough that the workflow skipped `idea_sketch_brainstorming`

Read `prd-template.md`, `prd-completeness-gate.md`, and `prd-handoff-map.md` when the workflow needs a stronger PRD contract instead of a minimal one-off summary.

## Internal Flow

1. Start from the confirmed `docs/project/idea-sketch-brief.md` when it exists, or capture the already-concrete request in equivalent structure when the sketch stage was skipped.
2. Brainstorm the requirement space across users, jobs-to-be-done, core scenarios, non-goals, data needs, platform expectations, UX posture, success criteria, and risks.
3. Build a question ledger that separates decision-blocking questions from questions that can be answered by low-risk defaults.
4. Resolve every decision-blocking question from user-provided context, existing project docs, or explicit user confirmation.
5. Define the first PRD scope boundary: what belongs in this PRD, what is explicitly out of scope, and what should become a later module or follow-up.
6. Generate or update `docs/project/page-navigation-flow.md` as the companion navigation artifact for the current PRD scope. Use a Mermaid flowchart and make the primary entry points, main page transitions, branch routes, and return paths explicit without freezing detailed UI.
7. Stop for explicit navigation confirmation. Do not draft or refine the PRD until the navigation artifact is accepted as the current scope baseline.
8. For low-risk defaults, write the assumption, rationale, and risk into the PRD instead of leaving the point implicit.
9. Generate or update the PRD artifact using the standard template shape, using the confirmed navigation artifact as an authoritative input for pages, transitions, scope boundaries, and primary scenarios.
10. Run the PRD completeness gate and record the score plus weak dimensions.
11. Queue `pending_next_stage=prd_ready` only after the PRD artifact exists, the confirmed companion page-navigation-flow artifact exists, the question ledger has no unresolved decision-blocking items, and the completeness gate passes.

## Upstream Dependency

Before this flow runs, the workflow should already know enough to describe the product through concrete pages.

Minimum expectation:

- the core product direction is already concrete
- the main user flow is already concrete
- the key pages are already identifiable
- if the workflow started from a rough idea, `docs/project/idea-sketch-brief.md` already exists

## Brainstorming Checklist

Cover these dimensions before writing the PRD:

- target users and roles
- user goals and primary jobs-to-be-done
- happy-path scenarios
- edge cases and failure states
- business objective or success metric
- primary platform and validation-device hints
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
- primary-platform and validation-device assumptions when known
- UX direction hints without freezing detailed UI
- alignment with the confirmed companion `docs/project/page-navigation-flow.md` artifact
- scenario and scope descriptions refined from that confirmed navigation rather than reconstructed independently
- success metrics or acceptance criteria
- resolved question ledger
- remaining deferred questions
- explicit assumptions and risks

The preferred document structure lives in `prd-template.md`. If the project already has a stronger house style, preserve that style but do not weaken the required sections.

## Completeness Gate

Before advancing to `prd_ready`, run the gate in `prd-completeness-gate.md`.

Minimum expectation:

- PRD artifact exists on disk
- confirmed companion `docs/project/page-navigation-flow.md` artifact exists on disk
- completeness outcome is `ready_for_prd_ready`
- no unresolved `decision_blocking` items remain
- downstream handoff risk is low enough for `flutter-prd-rd-writer` to consume the PRD without reopening basic scope

## Handoff Discipline

Before leaving PRD preparation, check `prd-handoff-map.md` and verify the PRD can support:

- technical baseline generation
- Product Design brief confirmation
- optional Creative Production direction input
- later module splitting
- downstream page-entry and transition understanding without reconstructing navigation from prose alone

## Do Not Use This Flow To

- replace the upstream sketch-confirmation stage when the idea is still too abstract
- reopen open-ended page ideation that belongs to `idea_sketch_brainstorming`
- decide the main page structure from scratch when the workflow still lacks concrete page understanding
- pre-build atlas sheets, cut slices, or finalize TexturePacker contracts that belong to later shared or module asset-atlas work

## Routing Outcome

Use one of these outcomes:

- `advanced`: confirmed navigation artifact exists, PRD artifact exists, decision-blocking questions are resolved, the completeness gate passes, queue `pending_next_stage=prd_ready`.
- `blocked`: decision-blocking questions remain unresolved, record `required_inputs`, keep `current_stage=requirements_brainstorming`.
- `not_executed`: the PRD generation did not really run or did not produce an artifact; keep the current stage unchanged.

## Hard Rules

- Do not call technical baseline, image-backed design direction, executable module document generation, architecture, or implementation skills before this flow produces a PRD artifact.
- Do not promote to `prd_ready` only because a PRD file exists; the completeness gate must also pass.
- Do not draft, review, or refine the PRD before the companion `docs/project/page-navigation-flow.md` artifact is explicitly confirmed.
- Do not promote to `prd_ready` while the companion `docs/project/page-navigation-flow.md` artifact is missing or its page names and transitions still disagree with the PRD.
- Do not bury unresolved product questions inside later RD, architecture, or code planning.
- Do not invent business-critical answers. Ask or stop when the answer changes scope, roles, behavior, data, platform, compliance, or delivery order.
- Do not use this flow to decide the key pages when the request is still too abstract for concrete screens; route back to `idea_sketch_brainstorming` instead.
- Do not try to finalize shared or module asset-atlas packaging here. At most, record likely non-standard asset families or state-image needs for later atlas preparation.
- Do not freeze detailed screen design in the PRD. Capture product direction and constraints only; final product design direction confirmation and downstream design-source work belong to later workflow nodes.
