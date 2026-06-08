# Pencil Design Source

Use this reference when the confirmed `DESIGN.md` plus any optional effect images or approved visual comps must become the structured design source through Pencil for freeze, architecture, implementation, or human visual inspection.

## Role

Pencil is a first-class structured design-source adapter alongside Stitch. It consumes the confirmed root-level `DESIGN.md` as the primary source of truth and may also consume optional approved effect images or approved visual comps as supplemental evidence.

Pencil must not invent a new global style after the shared taste direction and final product design direction have been confirmed. It must expand pages from one frozen shared design master packet, not from page-local improvisation.

Regardless of page scope, Pencil output must preserve these four project-wide consistency contracts:

- one shared style direction
- one shared theme system
- one shared public shell
- one shared public component family set

## Source Gate

Before entering any Pencil design-source generation or validation step:

- confirm the final product design direction with the user
- ensure `DESIGN.md` exists and reflects that confirmation
- freeze one shared design master packet for the whole app
- freeze the project-level Pencil source reference such as the `.pen` file, Pencil project id, or equivalent adapter-owned project pointer

If the Pencil source reference is missing or ambiguous:

- keep the current workflow stage unchanged
- record `required_inputs=pencil_source_ref`
- do not generate or freeze any Pencil design-source packet

## Flow

1. Start from a user-confirmed final product design direction.
2. Write the confirmed direction into `DESIGN.md`.
3. Optionally attach approved effect images or approved visual comps as supplemental evidence.
4. Freeze one shared design master packet for the whole app.
5. Freeze the project-level Pencil source reference.
6. Split the design-source work into page-scoped tasks when multiple pages need generation or validation.
7. Run page-scoped Pencil design tasks in subagents with at most 6 concurrent page-design subagents.
8. Merge page-level receipts into one structured design-source packet.
9. Compare the Pencil packet against `DESIGN.md` and any optional visual evidence before freeze.
10. Freeze only after the shared design master packet, Pencil source reference, all required page receipts, merged Pencil packet, and high-fidelity visual contract all pass.

## Page Design Parallelism

Pencil page design must run in subagents when more than one page needs generation or validation.

- Run at most 6 page-design subagents in parallel.
- Give each subagent exactly one page id/name, the frozen Pencil source reference, the frozen shared design master packet, and any optional source effect-image path for that page when such evidence exists.
- Each subagent may generate or validate only its assigned page's Pencil design output.
- Each subagent must return a page-level receipt with produced artifact paths, any source effect-image path, Pencil output id/path, shared components used, requested new shared components if any, visual mismatches, accepted reductions, blockers, and page coverage status.
- The orchestrator must merge page receipts into the final Pencil design-source packet and update the workflow record.
- Page-design subagents must not update workflow-state artifacts, freeze design status, change project references, or decide global design acceptance.

## Packet Contract

The Pencil design-source packet must include:

- shared design master packet id or version
- confirmed `DESIGN.md` path
- optional source effect-image paths when they exist
- complete in-scope page list
- page-level Pencil receipt list
- frozen Pencil source reference
- generated or validated screen structure
- tokens and theme values
- component families and state matrix
- task hierarchy and primary CTA expectations
- interaction and feedback behavior expectations
- explicit shared public shell rules
- responsive adaptation rules
- content-tone or naming constraints when relevant
- region-level hierarchy and layout anchors
- spacing, typography, z-axis, image-treatment, and motion constraints
- fidelity-critical region list
- region classifications: `preserve_faithfully`, `flutterize`, or `simplify`
- approved reductions and their rationale
- unresolved visual mismatches, if any

## Freeze Rules

- Treat `DESIGN.md` as the primary upstream authority and optional effect images as supplemental evidence.
- Do not let Pencil invent a new palette, typography mood, CTA posture, or component family after the shared direction has been approved.
- Do not let Pencil redefine the shared theme system, public shell contract, or shared public component families after the shared direction has been approved.
- Do not let Pencil quietly change first-screen task priority, CTA discoverability, interaction feedback rhythm, or responsive strategy without orchestrator-approved shared-packet revision.
- Do not let page-level Pencil output redefine shell rules, layout-grid rules, or page density without orchestrator-approved shared-packet revision.
- Do not mark `design_source_status=frozen` unless the workflow record indexes both the Pencil packet and the frozen Pencil source reference.
- Do not mark `design_source_status=frozen` unless every in-scope page has a successful page-level Pencil receipt when page-scoped generation was required.
- Do not allow implementation to consume Pencil output directly unless `flutter-design-freeze-gate` has accepted it.
