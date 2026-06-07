# Stitch Design Source

Use this reference when approved effect images, approved visual comps, or module visual evidence must become the structured design source for freeze, architecture, implementation, or human visual inspection.

## Role

Stitch is the only default structured design-source adapter. Effect images remain the visual baseline, but the frozen design source must be a Stitch-generated or Stitch-validated packet whenever Stitch MCP is available. Separate module design documents are not required and must not replace the Stitch packet as the design source.

Before global design freeze, the workflow must first brainstorm the global visual design direction from the PRD plus the technical baseline, then confirm the final product design direction with the user, then generate and approve light-mode effect images for every in-scope page in one complete set. Stitch consumes that complete effect-image set; it must not be asked to infer missing pages from partial visual evidence.

## Model Requirement

Every Stitch design-source request must use:

```text
modelId = "GEMINI_3_1_PRO"
```

If Stitch MCP is not exposed in the current tool list, record `stitch_status=unavailable` and keep the workflow blocked when Stitch is required by the current design-source policy.

## Project Choice And ID Gate

Before entering any Stitch design-source generation or validation step, first ask the user to choose the Stitch project mode:

- `new`: create a new Stitch project for this workflow, then freeze the returned project id
- `existing`: use an existing Stitch project, then require the user-provided project id to be confirmed and frozen

If `stitch_project_mode` is missing or ambiguous, stop immediately:

- set `stitch_status=blocked_missing_project_mode`
- keep the current workflow stage unchanged
- record `required_inputs=stitch_project_mode:new_or_existing`
- do not call Stitch
- do not generate or freeze any Stitch design-source packet

After `stitch_project_mode` is confirmed, obtain the project id according to the mode:

- For `new`, create the Stitch project and freeze the returned `stitch_project_id`.
- For `existing`, collect the user-provided `stitch_project_id` and freeze it only after explicit confirmation.

If `stitch_project_mode=new` but project creation cannot return a frozen id, stop immediately:

- set `stitch_status=blocked_project_creation`
- keep the current workflow stage unchanged
- record `required_inputs=stitch_project_creation`
- do not generate or freeze any Stitch design-source packet

If `stitch_project_mode=existing` and `stitch_project_id` is missing, ambiguous, or not frozen after the mode choice, stop immediately:

- set `stitch_status=blocked_missing_project_id`
- keep the current workflow stage unchanged
- record `required_inputs=stitch_project_id`
- do not call Stitch
- do not generate or freeze any Stitch design-source packet

Once confirmed, both `stitch_project_mode` and `stitch_project_id` are immutable for the current project workflow. Any later change to either value is a design-source reset and must return through `flutter-design-source-control` before new Stitch output can be trusted.

## Flow

1. Start from a user-confirmed final product design direction that already passed the global visual design brainstorming step.
2. Generate and approve one light-mode effect image for every in-scope page.
3. Ask the user to choose `stitch_project_mode=new` or `stitch_project_mode=existing`.
4. For `new`, create the Stitch project and freeze the returned id; for `existing`, collect and freeze the existing `stitch_project_id`.
5. Split the complete visual evidence set into page-scoped Stitch design tasks.
6. Run page-scoped Stitch design tasks in subagents with at most 6 concurrent page-design subagents.
7. Merge page-level receipts into one structured design-source packet.
8. Compare the Stitch packet against the original effect images before freeze.
9. Extract or verify tokens, component families, layout hierarchy, spacing, typography, image treatment, and state coverage.
10. Record every accepted deviation from the effect images as an explicit Flutterization or approved reduction.
11. Freeze only after the Stitch project mode, Stitch project id, all page receipts, merged Stitch packet, complete page coverage, and high-fidelity visual contract all pass.

## Page Design Parallelism

Stitch page design must run in subagents when more than one page needs design generation or validation.

- Run at most 6 page-design subagents in parallel.
- Give each subagent exactly one page id/name, one source effect-image path, the frozen `stitch_project_mode`, the frozen `stitch_project_id`, `modelId=GEMINI_3_1_PRO`, and the shared visual constraints.
- Each subagent may generate or validate only its assigned page's Stitch design output.
- Each subagent may download image assets needed to faithfully restore its assigned Stitch page and save them as project assets for direct implementation use.
- Each subagent must return a page-level receipt with produced artifact paths, source effect-image path, Stitch output id/path, visual mismatches, accepted reductions, blockers, and page coverage status.
- The orchestrator must merge page receipts into the final Stitch design-source packet and update the workflow record.
- Page-design subagents must not update workflow-state artifacts, freeze design status, change project mode/id, or decide global design acceptance.
- If any page subagent is blocked or missing a receipt, the whole Stitch design-source packet remains unfrozen.

## Downloaded Image Assets

When restoring a Stitch design, image assets may be downloaded and used directly instead of being regenerated or rebuilt in Flutter.

- Download only images that are part of the approved effect image, approved visual comp, Stitch page output, or user-approved source material.
- Save downloaded images into the project asset tree or the agreed RD asset directory, using stable page or component names.
- Record each downloaded image's source URL or source artifact path, local asset path, owning page, intended region/component, and whether implementation should use it directly.
- Treat downloaded image assets as first-class implementation inputs when they preserve fidelity better than native reconstruction.
- Do not route downloaded images through `$imagegen` unless the source image is missing, unusable, or explicitly needs generation/rework.
- If an image source cannot be downloaded or its usage is unclear, record a blocker instead of silently substituting a different image.

## Packet Contract

The Stitch design-source packet must include:

- source effect-image paths
- complete in-scope page list and page-to-effect-image mapping
- page-level Stitch receipt list
- downloaded image asset list with source and local paths
- frozen Stitch project mode: `new` or `existing`
- frozen Stitch project id
- Stitch model id
- generated or validated screen structure
- tokens and theme values
- component families and state matrix
- region-level hierarchy and layout anchors
- spacing, typography, z-axis, image-treatment, and motion constraints
- fidelity-critical region list
- region classifications: `preserve_faithfully`, `flutterize`, or `simplify`
- approved reductions and their rationale
- unresolved visual mismatches, if any

## Freeze Rules

- Treat the effect image as the visual baseline and the Stitch packet as the structured implementation source.
- Treat the complete all-page effect-image set as the minimum Stitch input for global design freeze.
- If the Stitch packet contradicts the effect image, do not freeze until the mismatch is resolved or explicitly approved as a reduction.
- Do not let Stitch invent a new palette, typography mood, CTA posture, or component family after the shared direction has been approved.
- Do not mark `design_source_status=frozen` unless the workflow record indexes both the Stitch packet and its source effect-image paths.
- Do not mark `design_source_status=frozen` when downloaded image assets are required but their local paths are missing from the Stitch packet or workflow record.
- Do not mark `design_source_status=frozen` unless every in-scope page has a successful page-level Stitch receipt.
- Do not mark `design_source_status=frozen` unless the workflow record indexes the frozen `stitch_project_mode`.
- Do not mark `design_source_status=frozen` unless the workflow record indexes the frozen `stitch_project_id`.
- Do not allow implementation to consume Stitch output directly unless `flutter-design-freeze-gate` has accepted it.
