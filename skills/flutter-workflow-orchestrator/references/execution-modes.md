# Execution Modes

Use this reference when `flutter-workflow-orchestrator` is invoked with `--auto`, `--perviewer`, or when it must decide whether to continue routing after a local module milestone.

## Contents

- [`--auto`](#--auto)
- [`--perviewer`](#--perviewer)
- [Auto Loop Contract](#auto-loop-contract)
- [Stop Condition](#stop-condition)

## `--auto`

This skill supports an `--auto` execution parameter.

When `--auto` is present, the orchestrator must keep routing and applying workflow transitions without stopping for any downstream confirmation gate, as long as the next move is deterministic and no blocker is hit. If optional representative effect-image generation is active in the current run, that confirmation gate is an explicit exception and must stop `--auto`.

`--auto` is a full-module advancement mode, not a current-module recommendation mode. It must keep working through the remaining target modules until every dependency-safe module has been advanced to the implementation boundary and no further pre-implementation move is available.

The `--auto` goal is:

- finish the global technical baseline first
- generate module boundaries and executable module `impl.md` documents in one pass immediately after the technical baseline
- finish shared taste direction and shared freeze preparation from the PRD, technical baseline, and executable module `impl.md` contracts
- brainstorm the global visual design direction, then stop if final product design direction confirmation from the user is still missing
- support two confirmation branches after global visual design: direct human confirmation, or subagent-generated recommendation plus human confirmation
- write the confirmed direction into `DESIGN.md`
- run `flutter-taste-router` textual normalization before every shared freeze or module freeze decision
- confirm the final product design direction with the user after the visual brainstorming step and before structured design-source work
- generate optional effect images only when they are explicitly requested or when downstream freeze asks for additional visual evidence
- if optional effect images are in scope, generate one representative light-mode effect image first and stop for user confirmation or revision feedback on that representative image before generating any additional optional page images
- route into either Stitch or Pencil structured design-source generation, then merge page receipts before freeze
- treat every generated module `impl.md` as implementation-final enough to drive downstream design-source work and later enter module design freeze; separate refinement documents are not required
- freeze each module's Stitch design-source packet
- treat each module's high-fidelity visual contract as the first acceptance criterion for module design freeze
- advance each module to implementation-ready document maturity
- continue until every target module is ready to enter implementation, but before any module actually starts code implementation

`--auto` is not allowed to:

- start code implementation
- mark `code_status=in_progress`
- switch into `implementing`
- produce implementation execution before `@superpowers` `Spec` and `@superpowers` `Plan` exist
- bypass real blockers or missing inputs
- invent approvals for ambiguous design choices
- stop just because one active module reached a local stable milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`
- leave a module-complete handoff behind as a mere `next_skill` suggestion when other target modules are still not implementation-ready

When `--auto` reaches shared freeze, it must first verify that executable module `impl.md` documents already exist, that the global visual design direction has been brainstormed from those module contracts, that the final product design direction was explicitly confirmed from that brainstorm, and that `DESIGN.md` exists. If confirmation is missing, stop and request confirmation instead of advancing. If effect-image evidence is not required for the active path, `--auto` may continue directly into the chosen structured design-source branch without generating images. If optional effect-image generation is explicitly in scope and both `IMAGE_BASE_URL` and `IMAGE_API_KEY` exist, automatically call `gpt-image-2-generator` to produce exactly one representative light-mode page effect image first. After that image is generated, stop and wait for explicit user confirmation or revision feedback before generating any remaining optional page effect images. If optional effect-image generation is in scope but either environment variable is missing, stop and record a blocker for that branch. For module freeze, the frozen selected structured design-source packet remains required.

The representative effect image, when generated, should be treated as:

- the first approval gate for the shared visual system
- the page that best represents overall hierarchy, component family, palette, and density
- a hard prerequisite before remaining page effect images may be generated

After confirmation, any remaining generated page effect images should be treated as:

- shared freeze input after the representative direction is locked
- optional module freeze input when a module-specific screen pack is still needed
- page-named evidence files that can be referenced directly by downstream implementation

Auto-generated effect images do not remove the need for freeze-quality evaluation; they only provide optional supplemental static visual evidence.

## `--perviewer`

This skill also supports a `--perviewer` execution parameter.

`--perviewer` is a module-stage effect-image opt-in flag for executable module document generation and module freeze preparation.

Without `--perviewer`:

- executable module document generation must not generate new real-device or module-stage effect images by default
- module freeze should prefer the textual design packet plus already approved evidence
- downstream work may consume existing module visuals, but it must not auto-generate new module-stage effect images merely for convenience

With `--perviewer`:

- module-stage effect-image generation is allowed when the current module still benefits from page-addressable visual evidence
- generated module-stage effect images must inherit the approved shared/global style system instead of opening a new visual direction
- the workflow must record that opt-in decision and any generated global effect-image paths into `global-design-guidelines.md`

`--perviewer` does not weaken the shared/global freeze policy. Shared/global freeze still follows the confirmed `DESIGN.md` plus the selected structured design-source packet; any generated effect-image set remains optional supplemental evidence.

## Auto Loop Contract

After executable module documents are generated and the workflow enters downstream freeze preparation, `--auto` must behave as a loop:

1. Select the next dependency-safe target module that is not yet at the implementation boundary.
2. Set that module as `current_module` and update the workflow record immediately.
3. Verify that the selected module really exists in the module index, that its executable `impl.md` exists on disk, and that its frozen selected structured design-source packet is available before implementation readiness. If any required artifact is missing, record a real blocker and stop auto-advancement instead of inventing the module state.
4. Record why that module is dependency-safe right now before module freeze begins.
5. If the module `impl.md` is not executable enough for implementation readiness, route back to the combined module document generation step for a scope-matched regeneration and stop instead of opening a separate refinement stage.
6. If combined module document generation did not truly execute, mark that step as `not_executed` or `未执行` in the workflow record and any project-level execution trace, then stop instead of promoting later stages.
7. Run module freeze and freeze the design-source packet only when the packet is explicit enough and the high-fidelity visual contract has passed as the first freeze priority.
8. Advance the module to implementation-ready maturity.
9. Produce any required architecture output for that module.
10. Update `current_stage`, `next_skill`, `module_status_table`, and `decision_log`.
11. Re-evaluate the remaining modules and immediately continue with the next dependency-safe module.

`current_module` is only the module being processed right now. It must never be interpreted as the only module covered by the current `--auto` run.

If one module reaches `implementation_final`, `module_design_frozen`, `impl_rd_ready`, or `architecture_ready`, that is only a local milestone. In `--auto` mode, the orchestrator must immediately decide whether the same module still needs another pre-implementation step or whether another module should become `current_module`.

## Stop Condition

The default stop condition for `--auto` is:

- every module row has at least `impl_status=landed`
- every module row has `design_source_status=frozen`
- any required architecture outputs for those modules are ready
- the workflow is waiting at the boundary before module implementation

When this stop condition is reached, the orchestrator should surface that the project is `implementation_ready_waiting` and return control to the user or downstream implementation skill.

`--auto` may stop only when one of these conditions is true:

- all target modules satisfy the implementation-boundary condition above
- a real blocker appears and the current round cannot safely continue

It must not stop because one module finished its local pre-implementation flow, because a downstream skill recommendation was produced, or because `current_module` changed from one module to another.
