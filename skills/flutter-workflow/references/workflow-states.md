# Workflow States

Use this reference when classifying `current_phase`, `current_stage`, module maturity, or allowed next moves.

## Shared States

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `idea_sketch_brainstorming` | The input is still too abstract for page-level planning. | `requirements_brainstorming` after sketch confirmation |
| `requirements_brainstorming` | The workflow is turning concrete intent into a PRD and confirmed page-navigation flow. | `prd_ready` |
| `prd_ready` | PRD, confirmed page-navigation-flow, and question ledger are ready for technical baseline generation. | `technical_baseline_ready` |
| `technical_baseline_ready` | The global technical baseline exists and phase routing may begin. | `phase_1_scope_frozen` |

## Phase 1 States

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `phase_1_scope_frozen` | Launch scope, core task path, and required launch states are confirmed. | `phase_1_module_scope_frozen` |
| `phase_1_module_scope_frozen` | Launch module boundaries and active module ownership are frozen. | `phase_1_impl_contract_frozen` |
| `phase_1_impl_contract_frozen` | Launch implementation contract is frozen strongly enough to build the launch prototype. | `phase_1_prototype_ready` |
| `phase_1_prototype_ready` | The launch prototype exists and is reviewable. | `phase_1_structure_frozen` |
| `phase_1_structure_frozen` | Launch structure, primary CTA posture, and key state boundaries are frozen from the launch prototype. | `phase_1_pencil_ready` |
| `phase_1_pencil_ready` | Launch Pencil design source is confirmed and aligned to the approved launch prototype evidence. | `phase_1_design_frozen` |
| `phase_1_design_frozen` | Launch freeze is complete and the launch Pencil design source is the frozen design baseline. | `phase_1_restoration_ready` |
| `phase_1_restoration_ready` | Launch Pencil-to-Flutter restoration contract exists and is confirmed. | `phase_1_asset_enhancement_ready` |
| `phase_1_asset_enhancement_ready` | Launch asset-enhancement resolution is complete. Any `atlas_required` launch regions already have the required atlas-analysis, generation, background-processing, slicing, and asset-integration outputs. | `phase_1_implementing` |
| `phase_1_implementing` | Launch implementation is in progress. | `phase_1_launch_qa_ready` |
| `phase_1_launch_qa_ready` | Launch build is ready for release-quality QA. | `phase_1_release_ready` |
| `phase_1_release_ready` | Launch build meets release-readiness requirements. | `phase_2_scope_selected` or workflow completion |

## Phase 2 States

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `phase_2_scope_selected` | Premium enhancement scope is explicitly selected from a launchable baseline. | `phase_2_direction_ready` |
| `phase_2_direction_ready` | Shared premium direction and upgraded design rules are confirmed strongly enough to build the premium prototype. | `phase_2_prototype_ready` |
| `phase_2_prototype_ready` | The premium prototype exists and is reviewable. | `phase_2_structure_frozen` |
| `phase_2_structure_frozen` | Premium structure and allowed structural deltas are frozen from the premium prototype. | `phase_2_effect_image_ready` |
| `phase_2_effect_image_ready` | High-fidelity premium effect image is confirmed under the frozen premium structure. | `phase_2_pencil_ready` |
| `phase_2_pencil_ready` | Premium Pencil design source is confirmed and aligned to the approved premium effect image. | `phase_2_visual_frozen` |
| `phase_2_visual_frozen` | Premium visual freeze is complete and the premium Pencil design source is the frozen premium baseline. | `phase_2_restoration_ready` |
| `phase_2_restoration_ready` | Premium Pencil-to-Flutter restoration contract exists and is confirmed. | `phase_2_asset_enhancement_ready` |
| `phase_2_asset_enhancement_ready` | Premium asset-enhancement resolution is complete. Any `atlas_required` premium regions already have the required atlas-analysis, generation, background-processing, slicing, and asset-integration outputs. | `phase_2_blueprint_ready` or `phase_2_implementing` depending on route posture |
| `phase_2_blueprint_ready` | Display restoration blueprint is ready for premium implementation. | `phase_2_implementing` |
| `phase_2_implementing` | Premium implementation upgrade is in progress. | `phase_2_parity_qa_ready` |
| `phase_2_parity_qa_ready` | Premium implementation is ready for design parity QA. | `phase_2_done` |
| `phase_2_done` | Premium enhancement has passed parity review and human acceptance. | maintain index only |

Shared style-only state evidence should keep:

- `global_style_scheme.status=selected`
- `global_style_experience_image`
- `theme_and_style_only=true`
- `no_global_page_design_draft=true`
- `non_page_design_evidence=true`
- `page_design_deferred_to_module_stage=true`
- not page design evidence

Atlas-backed evidence should include:

- one UI-only atlas image
- transparent atlas result ready for slicing

The final app-page acceptance must happen only at the end of the workflow.
human visual inspection remains the final acceptance owner.

## Control States

| State | Meaning | Allowed Next Move |
| --- | --- | --- |
| `scope_reopen_required` | A premium change request now exceeds enhancement-only scope and must reopen launch-level scope or contract work. | return to the matching Phase 1 scope or contract step |
