# Idea Sketch Flow

Use this reference when the first workflow node receives a rough product idea, scattered references, or any demand that is still too abstract to discuss through concrete pages.

## Goal

Turn an abstract idea into a confirmed product-planning sketch packet that is concrete enough for downstream PRD work.

This node exists before formal PRD generation. It must help the user see the product through `1-3` key-page sketches, but it must not replace later Product Design direction control, module final effect-image generation, or any freeze artifact.

## Entry Conditions

Enter `idea_sketch_brainstorming` when one or more of these are true:

- the input is mostly a rough idea or slogan
- the user can describe intent but not yet the main pages
- the page structure is still unclear
- the broad visual style is still unclear
- references exist, but they do not yet resolve the main task path into concrete screens

If the request is already concrete enough to define pages, users, scope, and product behavior without a planning sketch pass, skip this flow and enter `requirements_brainstorming`.

## Internal Flow

1. Capture the rough idea in the user's own terms so the original intent is not lost.
2. Brainstorm the core task path, target users, main scenario, non-goals, and broad product posture.
3. Collapse the discussion into `1-3` key pages that best represent the main user flow.
4. Generate reviewable planning sketches for those key pages.
5. Ask the user to confirm product direction, page structure, and broad visual style.
6. If the user rejects or revises the sketches, stay in `idea_sketch_brainstorming` and iterate only on the unconfirmed parts.
7. When the sketches are confirmed, write `docs/project/idea-sketch-brief.md`.
8. Queue `pending_next_stage=requirements_brainstorming` only after both sketch confirmation and the brief artifact exist.

## Sketch Scope

Default scope:

- `1-3` key pages only
- focus on the primary flow instead of exhaustive coverage
- broad visual style is allowed, but no freeze-ready polish is required

The sketches should answer:

- what the product is trying to help the user do
- which pages matter first
- what each key page is responsible for
- what the broad visual world feels like

## Confirmation Standard

The user confirmation gate for this stage is intentionally limited.

The stage confirms:

- product direction
- page structure
- broad visual style

The stage does not confirm:

- detailed business rules
- full exception coverage
- technical architecture
- module split
- final Product Design direction
- freeze-ready UI specs

## Brief Artifact

Write the lightweight handoff artifact to:

- `docs/project/idea-sketch-brief.md`

Minimum required sections:

- rough idea summary
- confirmed product direction
- key page list with page purpose, main information blocks, and primary actions
- sketch confirmation summary
- broad visual style summary
- deferred PRD questions

The artifact should be short, concrete, and directly reusable by `requirements-prd-flow.md`. It is a product-consensus snapshot, not a full PRD.

## Routing Outcome

Use one of these outcomes:

- `advanced`: the key-page sketches are confirmed, `docs/project/idea-sketch-brief.md` exists, queue `pending_next_stage=requirements_brainstorming`
- `blocked`: the product direction, page structure, or broad visual style is still unresolved, or the brief artifact does not exist yet
- `not_executed`: the sketch pass did not actually run or did not produce reviewable sketches

## Hard Rules

- Do not call `flutter-prd-rd-writer`, technical baseline generation, Product Design brief confirmation, `DESIGN.md`, shared freeze, architecture, or implementation planning from this stage.
- Do not treat a rough sketch as the later module final effect-image evidence that belongs to Product Design control.
- Do not allow this stage to drift into exhaustive state coverage or freeze-ready page design.
- Do not leave this stage without both explicit user confirmation and `docs/project/idea-sketch-brief.md`.
