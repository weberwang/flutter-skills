# Execution Modes

Use this reference when `flutter-workflow-orchestrator` is invoked with `--auto` or when it must decide whether to continue routing after a local module milestone.

## Contents

- [`--auto`](#--auto)
- [Auto Loop Contract](#auto-loop-contract)
- [Stop Condition](#stop-condition)

## `--auto`

This skill supports an `--auto` execution parameter.

When `--auto` is present, the orchestrator must keep routing and applying workflow transitions without stopping for ordinary downstream confirmation gates, as long as the next move is deterministic and no blocker is hit.

`--auto` is a full-workflow advancement mode, not a current-module recommendation mode. It must keep working through the remaining target modules in the confirmed serial module order until every target module has been fully implemented and no further workflow move is available.

The `--auto` goal is:

- finish the global technical baseline first
- freeze the target design-device preset and base resolution before global visual design work begins
- finish Product Design brief confirmation, shared public-shell convergence, and shared freeze preparation from the PRD and technical baseline first
- stop only if Product Design brief confirmation, public-shell confirmation, or final product design direction confirmation from the user is still missing
- route through `@product-design` for design brief playback and design-direction recommendation before `DESIGN.md`
- in manual mode, surface a small recommended style set before shared/global freeze and wait for confirmation
- when explicitly requested, allow a pre-direction Creative Production exploration pass as direction evidence before final product-direction confirmation
- in `--auto`, if the recommendation pass already produced one clear primary style recommendation, adopt it directly and continue
- write the confirmed direction into `DESIGN.md`
- after shared/global design freeze, start project initialization and bootstrap preparation as soon as the shared baseline is explicit enough
- when the active route explicitly requires additional effect-image evidence, generate the in-scope light-mode effect images automatically after the relevant prerequisites are ready, using the approved Product Design visual target as the first baseline when available
- when no additional effect-image evidence is required, skip automatic effect-image generation
- route into shared HTML interactive prototype generation before shared freeze; do not generate final module page implementation code at global scope
- complete the shared/global design freeze before any module-related work begins
- generate module boundaries and executable module `impl.md` documents in one pass only after the shared/global design freeze
- treat every generated module `impl.md` as a detailed module task implementation document constrained by the frozen shared design and interaction principles, and strong enough to drive the active module's effect-image generation, module HTML interactive prototype generation, and later module freeze; separate refinement documents are not required
- freeze each active module's prototype-derived design-source packet only after its module effect image and module HTML interactive prototype are complete
- treat each module's high-fidelity visual contract as the first acceptance criterion for module design freeze
- advance each module through implementation-ready maturity, architecture, bootstrap prerequisites, and real code implementation
- continue until every target module is fully implemented and ready for human visual inspection or workflow completion

`--auto` is not allowed to:

- produce implementation execution before `@superpowers` `Spec` and `@superpowers` `Plan` exist for the active module
- bypass real blockers or missing inputs
- invent approvals for ambiguous design choices
- stop just because one active module reached a local stable milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, `architecture_ready`, or `code_status=landed`
- leave a module-complete handoff behind as a mere `next_skill` suggestion when other target modules are still unfinished

When `--auto` reaches shared freeze, it must first verify that the design viewport is already frozen; if not, auto-freeze `390 x 844 px` as the global design viewport. Then verify that the Product Design brief has been confirmed from the PRD and technical baseline, that the public shell is explicitly agreed, that the final product design direction was explicitly confirmed from the approved Product Design visual target or recommendation, and that `DESIGN.md` exists. If confirmation is missing, stop and request confirmation instead of advancing. If the active route requires additional light-mode effect images and `gpt-image-2-generator` is available, automatically generate the in-scope images and continue without waiting for user confirmation. If the active route requires additional images but `gpt-image-2-generator` is blocked by missing access, credentials, or upstream capability, stop and record a blocker for that branch. If no additional image evidence is required, skip effect-image generation entirely. The shared/global freeze packet must stop at shared theme/public-shell design and must not include page design. Only after the shared/global design freeze is complete may `--auto` enter module `impl.md` generation, per-module serial advancement, and later code implementation.

Auto-generated effect images do not remove the need for freeze-quality evaluation; they only provide optional supplemental static visual evidence.

`--auto` does not automatically open the Creative Production branch by default. That branch is scope-driven and should be entered only when the current request explicitly includes asset-oriented work such as campaign visuals, mood boards, ad routes, hero variations, or publish-bound marketing assets. When that branch is active before final direction confirmation, it is direction evidence only. When it is active after `DESIGN.md`, it is an asset-production branch. In both cases, the orchestrator should still preserve the same upstream design-direction gates and should not let asset exploration rewrite the already confirmed product direction silently.

## Auto Loop Contract

After the shared/global design freeze is complete and module `impl.md` generation begins, `--auto` must behave as a serial loop:

1. Select the next target module in the confirmed serial module order that is not yet fully implemented.
2. Set that module as `current_module` and update the workflow record immediately.
3. Verify that the selected module really exists in the module index, that the shared/global design freeze is already complete, that its executable `impl.md` exists on disk, and that its frozen prototype-derived design-source packet is available before implementation readiness. If any required artifact is missing, record a real blocker and stop auto-advancement instead of inventing the module state.
4. Record why that module is the correct next serial module right now before module `impl.md` refinement, module freeze, or code execution begins.
5. If the module `impl.md` is not executable enough as a detailed task implementation document constrained by the frozen shared design and interaction principles, route back to the combined module document generation step for a scope-matched regeneration and stop instead of opening a separate refinement stage.
6. If combined module document generation did not truly execute, mark that step as `not_executed` or `未执行` in the workflow record and any project-level execution trace, then stop instead of promoting later stages.
7. Run the active module's page component draft generation and module freeze, and freeze the design-source packet only when the packet is explicit enough and the high-fidelity visual contract has passed as the first freeze priority.
8. Advance the module through implementation-ready maturity.
9. Produce any required architecture output for that module.
10. Run `@superpowers` `Spec`, then `@superpowers` `Plan`, then execute the active module's serial implementation loop to real code completion.
11. Update `current_stage`, `next_skill`, `module_status_table`, `code_status`, and `decision_log`.
12. Re-evaluate the remaining modules and immediately continue with the next serial module.

`current_module` is only the module being processed right now. It must never be interpreted as the only module covered by the current `--auto` run.

If one module reaches `implementation_final`, `module_design_frozen`, `impl_rd_ready`, `architecture_ready`, or `code_status=landed`, that is only a local milestone. In `--auto` mode, the orchestrator must immediately decide whether the same module still needs another step or whether the next serial module should become `current_module`.

## Stop Condition

The default stop condition for `--auto` is:

- every target module row has at least `impl_status=landed`
- every target module row has `design_source_status=frozen`
- any required architecture outputs for those modules are ready
- every target module row has `code_status=landed`
- required human visual inspection handoff artifacts are ready

When this stop condition is reached, the orchestrator should surface that the project is `workflow_completed_waiting_review` and return control to the user for review or closeout.

`--auto` may stop only when one of these conditions is true:

- all target modules satisfy the completion condition above
- a real blocker appears and the current round cannot safely continue

It must not stop because one module finished its local pre-implementation flow, because one module finished implementation, because a downstream skill recommendation was produced, or because `current_module` changed from one module to another.
