# Stitch Design Source

Use this reference when the confirmed `DESIGN.md`, optional approved effect images, approved visual comps, or module visual evidence must become the structured design source for freeze, architecture, implementation, or human visual inspection through Stitch.

## Role

Stitch is one first-class structured design-source adapter alongside Pencil. `DESIGN.md` is the primary upstream packet. Effect images remain optional supplemental visual evidence, but when Stitch is the selected adapter the frozen design source must be a Stitch-generated or Stitch-validated packet. Separate module design documents are not required and must not replace the Stitch packet as the design source.

Stitch is not an independent design-guidance authority. The only valid design-guidance sources are the frozen global design packet, the active module design package when module scope exists, and `DESIGN.md`. Stitch may structure, restore, validate, and serialize those inputs, but it must not inject Stitch-native internal guidance, hidden defaults, or tool-owned style opinions into the project design contract.

Before global design freeze, the workflow must first brainstorm the global visual design direction from the PRD and the technical baseline, then confirm the final product design direction with the user, then write that direction into the root-level `DESIGN.md`. Optional light-mode effect images may be attached as supplemental evidence when the current revision path asks for them. Only after the shared/global design freeze is complete may module `impl.md` generation begin. For module-scoped page component design drafts, Stitch must wait until the active module's `impl.md` has already fixed the module function, key states, and main task path. Stitch must not be asked to infer missing global decisions from partial visual evidence.

For a product that requires high visual consistency across the whole app, Stitch must operate as a page-expansion system on top of one frozen global design master, not as a per-page style invention system. The workflow must freeze one shared design master packet before page-level Stitch generation starts, and every page subagent must consume that same packet.

Regardless of page scope, Stitch output must preserve these four project-wide consistency contracts:

- one shared style direction
- one shared theme system
- one shared public shell
- one shared public component family set

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

## Shared Design Master Packet

Before any page-scoped Stitch generation or validation starts, the orchestrator must derive one frozen shared design master packet for the whole app.

That packet must include at minimum:

- final product design direction confirmed by the user
- confirmed `DESIGN.md`
- representative page effect-image approval decision, when it exists
- full approved page-effect set, when it exists
- global visual principles and anti-template constraints
- task-priority and first-screen hierarchy rules
- typography ladder
- spacing scale
- color and contrast system
- radius, border, elevation, and image-treatment posture
- CTA posture and interaction emphasis model
- interaction and feedback behavior rules
- root shell, navigation shell, and layout-grid rules
- shared component families
- shared state-surface rules
- explicit shared theme values and theme-behavior rules
- responsive and multi-device adaptation rules when relevant
- content tone and naming rules when relevant
- explicit `platform_identifier`
- fidelity-critical regions and approved reductions already known upstream

Do not append Stitch-internal guidance text, Stitch-inferred style heuristics, or adapter-only design rules to this packet as if they were project design guidance.

If the packet is incomplete, page-scoped Stitch work must not start. Do not ask page subagents to infer missing global style decisions from local page evidence.

## Flow

1. Start from a user-confirmed final product design direction that already passed the Product Design brief and direction confirmation step.
2. Write the confirmed direction into `DESIGN.md`.
3. Optionally generate and approve light-mode effect images for in-scope pages when the current path needs them.
4. Derive and freeze one shared design master packet for the whole app.
5. Ask the user to choose `stitch_project_mode=new` or `stitch_project_mode=existing`.
6. For `new`, create the Stitch project and freeze the returned id; for `existing`, collect and freeze the existing `stitch_project_id`.
7. Split the available design evidence set into page-scoped Stitch design tasks.
8. Run page-scoped Stitch design tasks in subagents with at most 6 concurrent page-design subagents.
9. Merge page-level receipts into one structured design-source packet.
10. Compare the Stitch packet against `DESIGN.md` and any optional effect images before freeze.
11. Extract or verify tokens, component families, layout hierarchy, spacing, typography, image treatment, task hierarchy, interaction feedback, responsive behavior, and state coverage.
12. Record every accepted deviation from the upstream design evidence as an explicit Flutterization or approved reduction.
13. Freeze only after the shared design master packet, Stitch project mode, Stitch project id, all required page receipts, merged Stitch packet, and high-fidelity visual contract all pass.

## Page Production Order

To maximize global consistency, prefer this page production order unless the app structure clearly requires another dependency-safe order:

1. root shell or `app-shell`
2. representative primary page
3. same-family list or overview pages
4. detail pages
5. form or create/edit pages
6. settings, support, and state-only pages

Do not let page generation order drift randomly when later pages depend on earlier shell, hierarchy, or component decisions.

## Page Design Parallelism

Stitch page design must run in subagents when more than one page needs design generation or validation.

- Run at most 6 page-design subagents in parallel.
- Give each subagent exactly one page id/name, one source effect-image path, the frozen `stitch_project_mode`, the frozen `stitch_project_id`, `modelId=GEMINI_3_1_PRO`, and the frozen shared design master packet.
- Each subagent may generate or validate only its assigned page's Stitch design output.
- Each subagent may download image assets needed to faithfully restore its assigned Stitch page and save them as project assets for direct implementation use.
- Each subagent must return a page-level receipt with produced artifact paths, source effect-image path, Stitch output id/path, shared components used, requested new shared components if any, visual mismatches, accepted reductions, blockers, and page coverage status.
- The orchestrator must merge page receipts into the final Stitch design-source packet and update the workflow record.
- Page-design subagents must not update workflow-state artifacts, freeze design status, change project mode/id, or decide global design acceptance.
- If any page subagent is blocked or missing a receipt, the whole Stitch design-source packet remains unfrozen.

## Page Subagent Contract

Each Stitch page subagent is a page-expansion worker, not a page-style owner.

It may:

- expand one page using the frozen shared design master packet
- reuse the frozen token system
- reuse frozen component families
- request a new shared component when the page cannot be expressed with the frozen component set
- download approved image assets for direct use

It must not:

- invent a new global palette
- invent a new typography mood
- redefine CTA posture
- redefine navigation shell or root shell behavior
- introduce a conflicting page density model
- silently create a new shared component family
- reinterpret the representative page into a different visual system

If a page truly needs a new cross-page component or a global style change, return a blocker or revision request to the orchestrator instead of making the change locally.

## Page Receipt Contract

Every page-level Stitch receipt must include:

- `page_id`
- source effect-image path, when one exists
- shared design master packet id or version
- Stitch output id/path
- produced artifact paths
- shared component families used
- requested new shared components, if any
- navigation-shell or root-shell dependencies touched by the page
- visual mismatches
- accepted reductions
- downloaded image assets
- blockers
- page coverage status
- whether the page preserves task hierarchy, feedback behavior, shared shell, and shared component contracts

If the receipt cannot show whether the page still conforms to the shared design master packet, treat that receipt as insufficient for merge.

## Downloaded Image Assets

When restoring a Stitch design, image assets may be downloaded and used directly instead of being regenerated or rebuilt in Flutter.

- Download only images that are part of the approved effect image, approved visual comp, Stitch page output, or user-approved source material.
- Save downloaded images into the project asset tree or the agreed RD asset directory, using stable page or component names.
- Record each downloaded image's source URL or source artifact path, local asset path, owning page, intended region/component, and whether implementation should use it directly.
- Treat downloaded image assets as first-class implementation inputs when they preserve fidelity better than native reconstruction.
- Do not force downloaded images through a separate generator unless the source image is missing, unusable, or explicitly needs generation/rework; when that happens, let the active MCP / design tool chain decide the concrete generation mechanism.
- If an image source cannot be downloaded or its usage is unclear, record a blocker instead of silently substituting a different image.

## Packet Contract

The Stitch design-source packet must include:

- shared design master packet id or version
- confirmed `DESIGN.md` path
- source effect-image paths, when they exist
- complete in-scope page list and page-to-effect-image mapping when images exist
- page-level Stitch receipt list
- downloaded image asset list with source and local paths
- frozen Stitch project mode: `new` or `existing`
- frozen Stitch project id
- Stitch model id
- generated or validated screen structure
- tokens and theme values
- component families and state matrix
- task hierarchy and primary CTA expectations
- interaction and feedback behavior expectations
- responsive adaptation rules
- content-tone or naming constraints when relevant
- region-level hierarchy and layout anchors
- spacing, typography, z-axis, image-treatment, and motion constraints
- fidelity-critical region list
- region classifications: `preserve_faithfully`, `flutterize`, or `simplify`
- approved reductions and their rationale
- unresolved visual mismatches, if any

## Global Consistency Merge Gate

Before freeze, the orchestrator must run a global consistency merge gate over the merged Stitch packet.

At minimum, verify:

- one shared token system is used across pages
- one shared style direction is preserved across pages
- one shared theme system is preserved across pages
- main task hierarchy stays consistent across pages
- first-screen CTA posture stays consistent across pages
- typography hierarchy stays consistent across pages
- component families are reused consistently across pages
- shell, nav, header, footer, and page-grid decisions stay consistent
- CTA posture and dominance are consistent
- interaction and feedback behavior are consistent
- image-treatment posture is consistent
- page density and spacing rhythm are consistent
- responsive adaptation stays within one design language
- state pages follow one coherent state language
- no page introduced an unapproved shared component family

If a page is visually strong in isolation but violates the shared system, reject the packet or route to a controlled revision. Global consistency is more important than a single page's local polish.

## Freeze Rules

- Treat `DESIGN.md`, the frozen global design packet, and the active module design package as the only design-guidance authorities. Treat optional effect images as supplemental visual evidence and the Stitch packet as the structured implementation source only.
- Treat the frozen shared design master packet as the upstream authority for all page-level Stitch expansion.
- Treat the complete all-page effect-image set as required Stitch input only when the active revision path explicitly chose that broader visual-evidence branch.
- If the Stitch packet contradicts `DESIGN.md` or any approved optional effect image, do not freeze until the mismatch is resolved or explicitly approved as a reduction.
- Do not let Stitch invent a new palette, typography mood, CTA posture, or component family after the shared direction has been approved.
- Do not let Stitch redefine the shared theme system, public shell contract, or shared public component families after the shared direction has been approved.
- Do not let Stitch quietly change first-screen task priority, CTA discoverability, interaction feedback rhythm, or responsive strategy without orchestrator-approved shared-packet revision.
- Do not let page-level Stitch output redefine shell rules, layout-grid rules, or page density without orchestrator-approved shared-packet revision.
- Do not treat any Stitch-native suggestion, adapter-internal guideline, generated helper prose, or model-side style rationale as valid project design guidance.
- Do not mark `design_source_status=frozen` unless the workflow record indexes both the Stitch packet and its source effect-image paths.
- Do not mark `design_source_status=frozen` when downloaded image assets are required but their local paths are missing from the Stitch packet or workflow record.
- Do not mark `design_source_status=frozen` unless every in-scope page has a successful page-level Stitch receipt.
- Do not mark `design_source_status=frozen` unless the merged packet passes the global consistency merge gate.
- Do not mark `design_source_status=frozen` unless the workflow record indexes the frozen `stitch_project_mode`.
- Do not mark `design_source_status=frozen` unless the workflow record indexes the frozen `stitch_project_id`.
- Do not allow implementation to consume Stitch output directly unless `flutter-design-freeze-gate` has accepted it.
