# Execution Modes

Use this reference when `flutter-workflow` is invoked with `--auto`, `--full-auto`, or when it must decide whether to continue routing after a local module milestone.

## Contents

- [`--auto`](#--auto)
- [`--full-auto`](#--full-auto)
- [Auto Loop Contract](#auto-loop-contract)
- [Stop Condition](#stop-condition)

## `--auto`

This skill supports an `--auto` execution parameter.

When `--auto` is present, the orchestrator must keep routing and applying workflow transitions without stopping for ordinary downstream confirmation gates, as long as the next move is deterministic and no blocker is hit.

`--auto` includes both automatic confirmation and automatic execution for ordinary orchestrator-owned workflow gates. After a specialist receipt is validated and the route lock is still satisfied, the orchestrator should auto-apply its queued stage transitions and queued status updates, then immediately invoke the next authorized serial step instead of stopping at a reviewable milestone.

`--auto` is a full-workflow advancement mode, not a current-module recommendation mode. It must keep working through the remaining target modules in the confirmed serial module order until every target module has been fully implemented and no further workflow move is available.

The `--auto` goal is:

- finish the global technical baseline first
- freeze the target design-device preset and base resolution before global visual design work begins
- finish Product Design brief confirmation, shared public-shell convergence, and shared freeze preparation from the PRD and technical baseline first
- lock a structured Product Design clarification packet before module splitting so later module docs do not have to infer user journeys, page families, critical states, interaction goals, platform fit, or information density from screenshots or page count
- stop only if Product Design brief confirmation, public-shell confirmation, or final product design direction confirmation from the user is still missing
- route through `@product-design` for design brief playback and design-direction recommendation before `DESIGN.md`
- use `https://mobbin.com/` as the mandatory first-stop inspiration library during shared/global design-direction exploration, and do not allow direction recommendation or effect-image generation before the Mobbin pass is complete
- in manual mode, surface three comparable design directions with one primary recommendation before shared/global freeze and wait for confirmation
- when explicitly requested, allow a pre-direction Creative Production exploration pass as direction evidence before final product-direction confirmation
- in `--auto`, if the Mobbin-backed recommendation pass already produced one clear primary style recommendation among the three compared directions, adopt it directly and continue
- write the confirmed direction into `DESIGN.md`
- after shared/global design freeze, start project initialization and bootstrap preparation as soon as the shared baseline is explicit enough
- when the active route explicitly requires additional effect-image evidence, generate the in-scope light-mode effect images automatically after the relevant prerequisites are ready, using the approved Product Design visual target as the first baseline when available
- when no additional effect-image evidence is required, skip automatic effect-image generation
- route into mandatory shared Pencil design execution before shared freeze, then into post-review shared image-asset generation only when still required; do not generate final module page implementation code at global scope
- complete the shared/global design freeze before any module-related work begins
- generate module boundaries and executable module `impl.md` documents in one pass only after the shared/global design freeze
- treat every generated module `impl.md` as a detailed module task implementation document constrained by the frozen shared design and interaction principles, the confirmed Product Design clarification packet, and the target platform's information-density expectations, and strong enough to drive a later implementation-stage visual restoration loop covering the active module's effect-image generation, display-evidence-pack confirmation, mandatory module Pencil design execution, and post-review module image-asset generation when needed; separate refinement documents are not required
- freeze each active module's contract before implementation-side visual restoration begins; module effect images and module display evidence now belong to that later implementation-stage loop rather than the pre-implementation freeze gate
- treat each module's high-fidelity visual contract as the first acceptance criterion for module design freeze
- advance each module through implementation-ready maturity, architecture, bootstrap prerequisites, and real code implementation
- continue until every target module is fully implemented and ready for human visual inspection or workflow completion
- automatically confirm ordinary orchestrator-owned stage promotions, maturity promotions, and reviewable receipts after validation instead of pausing for per-module acknowledgment
- automatically invoke the next route-locked skill or serial module step after each successful receipt instead of leaving a passive recommendation behind

`--auto` is not allowed to:

- produce implementation execution before `@superpowers` `Spec` and `@superpowers` `Plan` exist for the active module
- bypass real blockers or missing inputs
- invent approvals for ambiguous design choices
- wait for a manual "continue" acknowledgment after an ordinary module milestone when downstream work is still authorized
- stop just because one active module reached a local stable milestone such as `implementation_final`, `module_design_frozen`, `impl_rd_ready`, `architecture_ready`, or `code_status=landed`
- leave a module-complete handoff behind as a mere `next_skill` suggestion when other target modules are still unfinished

When `--auto` reaches shared freeze, it must first verify that the design viewport is already frozen; if not, auto-freeze `390 x 844 px` as the global design viewport. Then verify that the Product Design brief has been confirmed from the PRD and technical baseline, that the structured Product Design clarification packet for later module splitting is already locked, that the public shell is explicitly agreed, that the final product design direction was explicitly confirmed from the approved Product Design recommendation or representative sketch, and that `DESIGN.md` exists. If confirmation is missing, stop and request confirmation instead of advancing. If the active route requires additional light-mode effect images, first ensure the representative sketch already exists or generate it through `Product Design:ideate` when the route allows auto adoption, then complete the Product Design-owned final effect-image direction pass before continuing without waiting for ordinary user confirmation. If the active route requires additional final images but the selected final effect-image direction path is blocked by missing access, credentials, or upstream capability, stop and record a blocker for that branch. If no additional image evidence is required, skip effect-image generation entirely. The shared/global freeze packet must stop at shared theme/public-shell design and must not include page design. Only after the shared/global design freeze is complete may `--auto` enter module `impl.md` generation, per-module serial advancement, and later code implementation.

Auto-generated effect images do not remove the need for freeze-quality evaluation; they only provide optional supplemental static visual evidence.

`--auto` does not automatically open the Creative Production branch by default. That branch is scope-driven and should be entered only when the current request explicitly includes asset-oriented work such as campaign visuals, mood boards, ad routes, hero variations, or publish-bound marketing assets. When that branch is active before final direction confirmation, it is direction evidence only. When it is active after `DESIGN.md`, it is an asset-production branch. In both cases, the orchestrator should still preserve the same upstream design-direction gates and should not let asset exploration rewrite the already confirmed product direction silently.

## `--full-auto`

This skill also supports a `--full-auto` execution parameter.

`--full-auto` includes everything in `--auto`, but expands auto-confirmation to deterministic human-facing workflow gates when existing artifacts collapse the decision to exactly one supported default.

`--full-auto` may auto-confirm:

- Product Design brief confirmation when the PRD, technical baseline, and required clarification packet already prove one brief interpretation strongly enough for downstream work
- public-shell confirmation when the current shared-shell packet has one uniquely supported option and no competing shell contract remains in scope
- final product direction confirmation when the Mobbin-backed recommendation pass yields one clear primary direction and no competing approved direction remains unresolved
- primary-platform device selection when validation sees exactly one eligible device, or exactly one already-booted eligible device, or no eligible device and the platform supports starting a single emulator or simulator fallback
- ordinary orchestrator-owned review gates that `--auto` already consumes

`--full-auto` must still stop when:

- the available artifacts still support multiple plausible defaults
- the shell, brief, direction, or device choice would require taste judgment rather than deterministic selection
- route lock validation, receipt validation, or no-progress rules fail
- required artifacts, credentials, tools, or generated evidence are missing
- a blocker would already stop `--auto`

`--full-auto` is not allowed to:

- invent a brief, shell, direction, or device decision when more than one reasonable choice still exists
- bypass the Mobbin-backed recommendation pass, Product Design artifacts, or required effect-image and freeze gates
- weaken route-lock, receipt, blocker, or no-progress enforcement
- convert an unresolved ambiguity into a silent approval just to keep the loop moving

When `--full-auto` reaches shared freeze, it should apply the same `390 x 844 px` viewport default as `--auto` when no frozen viewport exists. Then it should attempt deterministic confirmation in this order: Product Design brief, public shell, final product direction. If any one of those gates still has more than one supported answer, stop and record the ambiguity as a blocker instead of advancing. If the active route requires additional light-mode effect images, generate the representative sketch through `Product Design:ideate`, then complete the Product Design-owned final effect-image direction pass and continue. If final image generation is blocked, stop and record that blocker.

## Auto Loop Contract

After the shared/global design freeze is complete and module `impl.md` generation begins, `--auto` and `--full-auto` must behave as a serial loop:

1. Select the next target module in the confirmed serial module order that is not yet fully implemented.
2. Set that module as `current_module` and update the workflow record immediately.
3. Verify that the selected module really exists in the module index, that the shared/global design freeze is already complete, that the confirmed Product Design clarification packet exists for the relevant journeys or page families, that its executable `impl.md` exists on disk, that its frozen structured design-source packet is available, and that `display_restoration_blueprint_ready` is already satisfied before implementation readiness. If any required artifact is missing, record a real blocker and stop auto-advancement instead of inventing the module state.
4. Record why that module is the correct next serial module right now before module `impl.md` refinement, module freeze, or code execution begins.
5. If the module `impl.md` is not executable enough as a detailed task implementation document constrained by the frozen shared design and interaction principles, route back to the combined module document generation step for a scope-matched regeneration and stop instead of opening a separate refinement stage.
6. If combined module document generation did not truly execute, mark that step as `not_executed` or `未执行` in the workflow record and any project-level execution trace, then stop instead of promoting later stages.
7. Run the active module's freeze preparation first, then execute the implementation-stage visual restoration loop, and freeze the design-source packet only when the packet is explicit enough and the high-fidelity visual contract has passed as the first freeze priority.
8. Advance the module through implementation-ready maturity.
9. Produce any required architecture output for that module.
10. Run `@superpowers` `Spec`, then `@superpowers` `Plan`, then execute the active module's serial implementation loop to real code completion.
11. Update `current_stage`, `next_skill`, `module_status_table`, `code_status`, and `decision_log`.
12. Re-evaluate the remaining modules and immediately continue with the next serial module.

`current_module` is only the module being processed right now. It must never be interpreted as the only module covered by the current `--auto` or `--full-auto` run.

If one module reaches `implementation_final`, `module_design_frozen`, `impl_rd_ready`, `architecture_ready`, or `code_status=landed`, that is only a local milestone. In `--auto` or `--full-auto` mode, the orchestrator must immediately decide whether the same module still needs another step or whether the next serial module should become `current_module`, then continue execution without asking for an ordinary continuation confirmation.

## Stop Condition

The default stop condition for `--auto` and `--full-auto` is:

- every target module row has at least `impl_status=landed`
- every target module row has `design_source_status=frozen`
- any required architecture outputs for those modules are ready
- every target module row has `code_status=landed`
- required human visual inspection handoff artifacts are ready

When this stop condition is reached, the orchestrator should surface that the project is `workflow_completed_waiting_review` and return control to the user for review or closeout.

`--auto` and `--full-auto` may stop only when one of these conditions is true:

- all target modules satisfy the completion condition above
- a real blocker appears and the current round cannot safely continue

It must not stop because one module finished its local pre-implementation flow, because one module finished implementation, because a downstream skill recommendation was produced, because `current_module` changed from one module to another, or because a validated ordinary review gate would normally wait for manual acknowledgment in non-auto mode.
