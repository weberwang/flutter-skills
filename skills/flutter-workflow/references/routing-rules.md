# Routing Rules

Use this reference before selecting any downstream skill, changing `current_phase`, changing `current_stage`, or applying module maturity changes.

1. Start by ensuring workflow state is initialized for the current run.
2. Unless the user explicitly overrides the language for a specific artifact, every workflow artifact produced during routing must use Simplified Chinese for human-readable content.
3. Before deciding or invoking anything downstream, derive one route lock and run the preflight gate. If either step fails, stop and record a blocker.
4. If `confirmation_status=pending_confirmation`, do not switch to the next process or apply queued status changes unless `--auto` or `--full-auto` is active.
5. If the user explicitly confirms a pending transition, promote the queued values, clear pending fields, and continue normal routing.
6. If the user rejects a pending transition, keep the current confirmed stage, write the rejection reason, and route back to the skill that must revise artifacts.
7. If a specialist skill returns `blocked`, `not_executed`, or a receipt that fails route-lock validation, do not advance. Keep the current confirmed phase and stage, clear queued transitions, and record the blocker or route-drift reason.

## Shared Entry Rules

8. If the input is still too abstract for page-level reasoning, set or keep `current_stage=idea_sketch_brainstorming`, read `idea-sketch-flow.md`, and block PRD work until the idea sketch artifact is confirmed.
9. If the request is concrete enough for PRD work but no PRD artifact exists yet, set or keep `current_stage=requirements_brainstorming`, read `requirements-prd-flow.md`, and require a confirmed `docs/project/page-navigation-flow.md` before promoting `prd_ready`.
10. Before promoting `prd_ready`, require the PRD completeness gate to pass and require the confirmed companion navigation artifact.
11. If the input is already a PRD or feature brief, use `flutter-prd-rd-writer` first to derive or refresh the technical baseline.
12. If the technical baseline exists and no explicit phase is active yet, initialize `current_phase=launch` and route into the Phase 1 chain.

## Commercial Product Gates

13. Do not accept a shared native HTML prototype, do not accept a final effect image, and do not accept a Pencil design source until `commercial_surface_gate.result=passed`.
13A. Do not accept a shared native HTML prototype.
13B. Do not accept a final effect image.
13C. Do not accept a Pencil design source.
14. Do not lock the shared native HTML prototype while `commercial_design_exploration` still needs first-screen structure, module order, CTA placement adjustments. After the exploration window closes, freeze the route.
15. Do not open commercial design exploration until `mandatory_mobbin_reference.status=complete`, `fixed_style_direction.status=selected`, and `strong_hierarchy_contract.status=recorded`.
16. Do not generate global page design drafts on the shared route. Keep `global_style_experience_image`, `non_page_design_evidence=true`, `global_style_scheme.status=selected`, `theme_and_style_only=true`, and `page_design_deferred_to_module_stage=true`. Global design may define theme tokens.
17. Route the shared/global scope to `Product Design:ideate`. Generate `global_style_experience_image` through `Product Design:ideate`, route the module final effect-image direction pass to `Product Design:ideate`, and select or revise a Product Design-generated candidate.
17A. route the shared/global scope to `Product Design:ideate`
17B. `global_style_experience_image` through `Product Design:ideate`
17C. route the module final effect-image direction pass to `Product Design:ideate`
17D. select or revise a Product Design-generated candidate
18. Require `minimal_default_copy_contract.status=passed`, `explanatory_copy_budget`, and `explanation_overload` review before product-surface images advance.
19. Generate the solid-background atlas bundle through `Product Design:ideate`. Keep atlas background removal plus slicing on the deterministic asset path.
20. Require the matching UI-only transparent atlas and atlas manifest before treating atlas-backed evidence as complete.
21. Record manual image review, human review result, and user confirmation or revision feedback whenever the route advances a reviewable image artifact.

## Phase 1 Rules

22. If `current_phase=launch`, do not route directly into premium enhancement work.
23. Before `phase_1_scope_frozen`, ensure launch scope, core task path, and required launch states are explicit enough for a releasable first version.
24. Before `phase_1_module_scope_frozen`, ensure module ownership is explicit enough that each primary page family has exactly one owning module.
25. Before `phase_1_impl_contract_frozen`, ensure the active module contract fixes module responsibility, required states, primary task path, data dependencies, and acceptance criteria.
26. The launch prototype is the structure and upstream visual source of truth for Phase 1.
27. Do not generate a launch Pencil design source before `phase_1_structure_frozen` is complete.
28. When `design_source_branch=pencil_mcp_design_source_branch`, route launch design-source generation from the confirmed launch prototype evidence plus required state contract instead of requiring a launch effect image.
29. Do not promote `phase_1_design_frozen` until the launch Pencil design source is confirmed and aligned to the approved launch prototype evidence.
30. Freeze the launch Pencil design source, not the launch prototype itself.
31. Do not restore Flutter code directly from launch prototype screenshots. Route through `pencil-design-to-flutter-restoration` once the launch Pencil design source is frozen.
32. After `phase_1_design_frozen`, prefer native Flutter SDK standard capabilities during launch implementation, but do not skip launch asset-enhancement resolution.
33. Route launch restoration outputs through `launch_asset_enhancement_resolution` before launch implementation is treated as fully authorized.
34. Inside `launch_asset_enhancement_resolution`, classify each important region as `flutter_native`, `atlas_required`, or `placeholder_only`.
35. If any launch region is `atlas_required`, complete atlas analysis, atlas generation, background processing when needed, atlas slicing, and asset integration for that region before promoting `phase_1_asset_enhancement_ready`.
36. If no launch region is `atlas_required`, promote `phase_1_asset_enhancement_ready` with an explicit `no_atlas_required` receipt instead of silently skipping the node.
37. Do not promote `phase_1_release_ready` until launch QA proves the product is release-ready rather than merely demo-ready.
38. Enter `phase_2_scope_selected` only after the launch build is ready for release or already launched.

## Phase 2 Rules

39. If `current_phase=premium`, the workflow must inherit the launch baseline by default.
40. Do not start Phase 2 until premium enhancement scope is explicit and bounded.
41. The premium prototype must exist before the premium effect image may be generated.
42. Do not confirm the premium effect image before `phase_2_structure_frozen` is complete.
43. The premium prototype is the structure source of truth for premium enhancement. The premium effect image may strengthen visual direction, but it must not silently rewrite the frozen premium structure.
44. Do not generate a premium Pencil design source before the premium effect image is confirmed.
45. When `design_source_branch=pencil_mcp_design_source_branch`, route premium design-source generation to `effect-image-to-pencil-design`.
46. Do not promote `phase_2_visual_frozen` until the premium Pencil design source is confirmed and aligned to the approved premium effect image.
47. Freeze the premium Pencil design source, not the premium effect image itself.
48. Do not restore Flutter code directly from premium effect images. Route through `pencil-design-to-flutter-restoration` once the premium Pencil design source is frozen.
49. Route premium restoration outputs through `asset_enhancement_resolution` before premium implementation input is treated as fully complete.
50. Inside premium asset-enhancement resolution, classify each important region as `flutter_native`, `atlas_required`, or `placeholder_only`.
51. If any premium region is `atlas_required`, complete atlas analysis, atlas generation, background processing when needed, atlas slicing, and asset integration for that region before promoting `phase_2_asset_enhancement_ready`.
52. If no premium region is `atlas_required`, promote `phase_2_asset_enhancement_ready` with an explicit `no_atlas_required` receipt instead of silently skipping the node.
53. After premium asset-enhancement resolution, route to `flutter-uiux-to-architecture` for the display restoration blueprint before premium implementation work begins.
54. Use `flutter-design-parity-reviewer` as the default implementation-review skill for `phase_2_parity_qa_ready`.

## Scope Reopen Rules

55. If a premium request changes `core_task_path`, `primary_cta_goal`, `page_flow`, `required_states` semantics, or `module_boundary`, set `current_phase=scope_reopen` and `current_stage=scope_reopen_required`.
56. If `current_stage=scope_reopen_required`, do not continue inside the normal premium route. Route back to the matching launch scope, module, or contract step.
57. Do not treat a scope-reopen event as a visual-only delta.

## Initialization And Bootstrap Rules

58. Once the shared technical baseline and launch scope are explicit enough, prefer `flutter-init` and bootstrap preparation before later implementation milestones.
59. `flutter-init` must stop at initialization boundaries. It may create the directory skeleton and sibling `skills/flutter-dev/` container, but it must not implement feature code.
60. If bootstrap code has landed and the required global public baseline is actually present on disk, record or queue the corresponding bootstrap-ready stage.

## Implementation Rules

61. Do not enter implementation execution in any phase until the corresponding phase freeze is complete, the frozen Pencil design source exists, the matching Pencil-to-Flutter restoration contract exists, and the required asset-enhancement resolution node is complete for that phase.
62. Before code execution, require `@superpowers` `Spec`, then `@superpowers` `Plan`, and only then execute code work.
63. Module implementation remains serial by default.
64. During launch implementation, prefer native Flutter standard capabilities, but consume any launch atlas-backed assets that were marked required by launch asset-enhancement resolution.
65. During premium implementation, allow stronger fidelity and asset strategy, but still restore from the frozen Pencil design source rather than from screenshots directly, and consume any atlas-backed assets that were marked required by premium asset-enhancement resolution.

## Review Rules

66. If code is complete or implementation screenshots exist, first route to the phase-appropriate review:
67. In the launch phase, prioritize release-quality QA and stability checks before premium-level parity concerns, and verify that required atlas-backed assets were integrated correctly when launch asset-enhancement resolution marked them `atlas_required`.
68. In the premium phase, route through `flutter-design-parity-reviewer` before final human visual inspection, and verify that required atlas-backed assets were integrated correctly when premium asset-enhancement resolution marked them `atlas_required`.
69. `@product-design design-qa` may assist when a source visual target and implementation screenshots both exist, but it does not replace final human acceptance.
70. Do not treat `@product-design` `design-qa` as final acceptance of an app page.
71. The final acceptance of app pages must happen only at the end of the workflow and only through explicit human visual inspection.
