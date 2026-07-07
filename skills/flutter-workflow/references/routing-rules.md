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

## Phase 1 Rules

13. If `current_phase=launch`, do not route directly into premium enhancement work.
14. Before `phase_1_scope_frozen`, ensure launch scope, core task path, and required launch states are explicit enough for a releasable first version.
15. Before `phase_1_module_scope_frozen`, ensure module ownership is explicit enough that each primary page family has exactly one owning module.
16. Before `phase_1_impl_contract_frozen`, ensure the active module contract fixes module responsibility, required states, primary task path, data dependencies, and acceptance criteria.
17. Do not build the launch effect image before the launch prototype exists.
18. Do not confirm the launch effect image before `phase_1_structure_frozen` is complete.
19. The launch prototype is the structure source of truth. The launch effect image may strengthen visual direction, but it must not rewrite the already-frozen launch structure.
20. Do not generate a launch Pencil design source before the launch effect image is confirmed.
21. When `design_source_branch=pencil_mcp_design_source_branch`, route launch design-source generation to `effect-image-to-pencil-design`.
22. Do not promote `phase_1_design_frozen` until the launch Pencil design source is confirmed and aligned to the approved launch effect image.
23. Freeze the launch Pencil design source, not the launch effect image itself.
24. Do not restore Flutter code directly from launch effect images. Route through `pencil-design-to-flutter-restoration` once the launch Pencil design source is frozen.
25. After `phase_1_design_frozen`, prefer native Flutter SDK standard capabilities during launch implementation and keep atlas or bitmap enhancement branches closed unless the route explicitly proves they are needed.
26. Do not promote `phase_1_release_ready` until launch QA proves the product is release-ready rather than merely demo-ready.
27. Enter `phase_2_scope_selected` only after the launch build is ready for release or already launched.

## Phase 2 Rules

28. If `current_phase=premium`, the workflow must inherit the launch baseline by default.
29. Do not start Phase 2 until premium enhancement scope is explicit and bounded.
30. The premium prototype must exist before the premium effect image may be generated.
31. Do not confirm the premium effect image before `phase_2_structure_frozen` is complete.
32. The premium prototype is the structure source of truth for premium enhancement. The premium effect image may strengthen visual direction, but it must not silently rewrite the frozen premium structure.
33. Do not generate a premium Pencil design source before the premium effect image is confirmed.
34. When `design_source_branch=pencil_mcp_design_source_branch`, route premium design-source generation to `effect-image-to-pencil-design`.
35. Do not promote `phase_2_visual_frozen` until the premium Pencil design source is confirmed and aligned to the approved premium effect image.
36. Freeze the premium Pencil design source, not the premium effect image itself.
37. Do not restore Flutter code directly from premium effect images. Route through `pencil-design-to-flutter-restoration` once the premium Pencil design source is frozen.
38. After `phase_2_visual_frozen`, route to `flutter-uiux-to-architecture` for the display restoration blueprint before premium implementation work begins.
39. Use `flutter-design-parity-reviewer` as the default implementation-review skill for `phase_2_parity_qa_ready`.

## Scope Reopen Rules

40. If a premium request changes `core_task_path`, `primary_cta_goal`, `page_flow`, `required_states` semantics, or `module_boundary`, set `current_phase=scope_reopen` and `current_stage=scope_reopen_required`.
41. If `current_stage=scope_reopen_required`, do not continue inside the normal premium route. Route back to the matching launch scope, module, or contract step.
42. Do not treat a scope-reopen event as a visual-only delta.

## Initialization And Bootstrap Rules

43. Once the shared technical baseline and launch scope are explicit enough, prefer `flutter-init` and bootstrap preparation before later implementation milestones.
44. `flutter-init` must stop at initialization boundaries. It may create the directory skeleton and sibling `skills/flutter-dev/` container, but it must not implement feature code.
45. If bootstrap code has landed and the required global public baseline is actually present on disk, record or queue the corresponding bootstrap-ready stage.

## Implementation Rules

46. Do not enter implementation execution in any phase until the corresponding phase freeze is complete, the frozen Pencil design source exists, and the matching Pencil-to-Flutter restoration contract exists.
47. Before code execution, require `@superpowers` `Spec`, then `@superpowers` `Plan`, and only then execute code work.
48. Module implementation remains serial by default.
49. During launch implementation, prefer native Flutter standard capabilities and do not introduce high-cost visual fallback branches without explicit justification.
50. During premium implementation, allow stronger fidelity and asset strategy, but still restore from the frozen Pencil design source rather than from screenshots directly.

## Review Rules

51. If code is complete or implementation screenshots exist, first route to the phase-appropriate review:
52. In the launch phase, prioritize release-quality QA and stability checks before premium-level parity concerns.
53. In the premium phase, route through `flutter-design-parity-reviewer` before final human visual inspection.
54. `@product-design design-qa` may assist when a source visual target and implementation screenshots both exist, but it does not replace final human acceptance.
