---
name: flutter-design-freeze-gate
description: Use when shared Flutter design direction, shared/public component freeze, module-level design-source freeze, approval status, or code handoff must be checked before work proceeds to module splitting, architecture, or implementation.
---

# Flutter Design Freeze Gate

## Overview

Decide whether a Flutter design freeze request is approved enough to move forward.

This gate has two different responsibilities:

1. Before `modules_split`, it validates only the shared/public freeze needed to split modules safely.
2. During active module implementation preparation, it validates the active module's page-level hierarchy, module-private component freeze, state coverage, and design-source packet before architecture or code handoff.

It validates explicit design approval, state coverage, immutable constraints, and the presence of required freeze artifacts. It does not create the design or rebuild it in Pencil. The default workflow no longer requires `.pen` or Pencil MCP data.

For module implementation handoff, high-fidelity visual fidelity is the first freeze priority. The gate must evaluate the module's visual contract before secondary implementation-readiness concerns: hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and any approved Flutterization or bitmap fallback.

A successful module freeze decision is only a local gate result. In `flutter-workflow-orchestrator --auto`, it must be consumed as one step inside the broader all-module advancement loop, not as a reason to stop the run.

## Required Inputs

- Freeze target type:
  - `shared_pre_split`
  - `module_impl_prep`
- Module name when the target is module-specific.
- Current workflow state.
- Paired UI/UX RD path when the target is module-specific.
- Consolidated design packet from `flutter-taste-router` when the target is module-specific.
- High-fidelity visual contract when the target is module-specific, including locked hierarchy, spacing, typography, layer depth, state coverage, fidelity-critical region handling, and approved asset fallback or Flutterization decisions.
- When static previews are the frozen source, artifacts from `design-preview-to-global-guidelines`.
- Preview decision when previews were generated.
- State matrix and acceptance gates.
- Reference screenshots or preview images when the workflow claims `global_guidelines_frozen` from static visual sources.
- `global-design-guidelines.md`, `light-theme-freeze.yaml`, and `dark-theme-freeze.yaml` when the workflow relies on approved screenshots or preview comps as a reusable source contract.
- Explicit user approval or a documented approval marker.

## Freeze Checklist

### Shared freeze before `modules_split`

Approve `shared_pre_split` only when all items are present:

- Business intent and target user.
- Platform baseline, which for mobile work must default to strict iOS HIG unless the user explicitly approved another baseline.
- Shared art direction, information hierarchy, and key-task guidance decisions.
- Visual system contract: typography hierarchy, contrast strategy, CTA posture, spacing, color roles, radius, surfaces, icon posture, motion role.
- The freeze-facing visual draft, preview pack, or approved screenshot evidence is complete enough that hierarchy, task guidance, typography, contrast, CTA clarity, and state scope can be judged directly from the design package.
- Shared/public component freeze exists for reusable controls that should be stable before module splitting.
- Global design freeze artifacts exist when the workflow depends on static visual sources:
  - `global-design-guidelines.md`
  - `light-theme-freeze.yaml`
  - `dark-theme-freeze.yaml`
- The global design freeze artifacts explicitly freeze the global public component set, including globally allowed states or variants and immutable component rules.
- The guideline document keeps its required sections and the theme files contain concrete values instead of downstream TODOs.
- Immutable items that later modules and code may not change without returning to design control.
- Explicit approval from the user.

Do not require page-level freeze or module-private component freeze at this stage.

### Module freeze during implementation preparation

Approve `module_impl_prep` only when all items are present:

- Active module name and paired UI/UX RD.
- Shared freeze inputs that the module depends on.
- Taste direction and any inherited anti-template constraints.
- Page scope and navigation entry for the active module.
- Core path and return loop.
- Page hierarchy, key-task guidance, and state details at implementation-final granularity.
- Either:
  - the freeze-facing visual draft, preview pack, or approved screenshot evidence is complete enough that hierarchy, task guidance, typography, contrast, CTA clarity, and state scope can be judged directly from the design package
  - or the consolidated design packet from `flutter-taste-router` is explicit enough that the module UI/UX can be judged and frozen without static images
- High-fidelity visual contract is evaluated first and is either accepted for implementation or explicitly reduced by design-source control. The accepted contract must cover hierarchy, spacing, typography, layer depth, image or texture treatment, component states, fidelity-critical regions, and approved Flutterization or bitmap fallback.
- Module-private component freeze exists for repeated building blocks inside that module, including frozen states, variant boundaries, immutable parts, and allowed adjustments.
- State matrix: ideal, empty, loading, error, permission, partial data, disabled, success, locked or premium when relevant.
- Immutable items that code may not change.
- Engineering adjustments that are explicitly allowed.
- Acceptance criteria for Flutter parity.
- Explicit approval from the user.

## Gate Decisions

Use these outcomes:

- `blocked`: required design evidence is missing.
- `needs_user_approval`: design evidence exists but approval is not explicit.
- `frozen_shared_for_split`: approved shared/public design can move to `flutter-rd-module-splitter`.
- `frozen_module_for_architecture`: approved active-module design-source packet can move to architecture planning.
- `frozen_for_code`: UI/UX RD, implementation RD, frozen theme artifacts, visual evidence, and design-source references are ready for code consumption.

## Hard Rules

- Do not infer approval from silence or enthusiasm.
- Do not treat the mobile platform baseline as negotiable or approximate when the workflow still uses the default; if the user did not explicitly approve another baseline, freeze review must enforce strict iOS HIG behavior expectations.
- Do not let a visually complete draft skip direct freeze-quality evaluation before freeze.
- Do not evaluate secondary architecture or implementation handoff readiness before evaluating high-fidelity visual fidelity for module implementation.
- Do not freeze a module when high-fidelity visual fidelity is vague, missing, or deferred to implementation polish.
- Do not let strong decorative polish mask unclear information hierarchy or weak task guidance.
- Do not allow a draft with unresolved hierarchy, task guidance, typography, contrast, CTA, or state-coverage defects to enter freeze.
- Do not treat a post-failure single revision without a new explicit freeze decision as a substitute for a valid freeze result.
- Do not treat “close enough” as a valid exception when the design package still leaves critical ambiguity.
- Do not allow module splitting to treat shared freeze as page-level freeze.
- Do not allow Flutter implementation to reinterpret hierarchy, spacing, states, or visual tokens.
- Do not treat premium decoration as compensation for weak typography hierarchy, low contrast, or a buried CTA.
- Do not allow module-private or other module-level reusable components to enter Flutter handoff without an explicit component-freeze decision for that active module.
- Do not require static images for module freeze when the `flutter-taste-router` design packet already makes hierarchy, task guidance, CTA posture, state coverage, and component freeze explicit enough to implement safely.
- Do not allow global public components to remain only implied inside theme files or prose; require explicit frozen global component decisions.
- Do not allow global design freeze to pass when reference screenshots or preview images are missing; block and ask the user whether to fall back.
- Do not let downstream skills infer missing theme values from static previews; require `design-preview-to-global-guidelines` to freeze them first.
- Do not decide visual alternatives here; route unresolved choices to `flutter-taste-router` or `design-preview-to-global-guidelines` depending on whether the missing work is exploratory or contract-freezing.
- Do not treat a pretty preview as frozen unless it has an approval record.
- Do not treat `frozen_module_for_architecture` as proof that `--auto` may stop. That result only means the active module may continue toward implementation-readiness or architecture, while the orchestrator still has to process remaining target modules.

## Output Contract

Return:

- `freeze_decision`
- `high_fidelity_freeze_status`: `passed`, `approved_reduction`, `blocked`, or `not_evaluated`
- `missing_items`
- `required_artifacts`
- `review_requirement_status`
- `immutable_items`
- `allowed_engineering_adjustments`
- `next_skill`
- `approval_record`

## Pressure Scenarios

- User says "this direction is fine, continue": ask whether that is explicit approval if the target artifact is module splitting, architecture, or code.
- User says "there is no reference image, freeze the global design first": block and ask whether to fall back.
- User says "shared styles are frozen, pages can be decided later": allow shared freeze only for module splitting, not for code handoff.
- User says "the page is frozen, components can be decided later": block until module-private or other module-level component freeze is explicit for that active module.
- User says "there is no static preview for this module": allow module freeze only if the `flutter-taste-router` packet is explicit enough to freeze without images; otherwise block.
- User says "the theme is frozen, global shared components can be decided later": block until the global public component freeze is explicit.
- User says "we can add states later": block production freeze.
- User says "Flutter can decide the dark theme later": block until `light-theme-freeze.yaml` and `dark-theme-freeze.yaml` are frozen.
- User says "the draft looks premium enough, skip review": block and evaluate the freeze package directly.
- User says "I already reviewed it in the main thread": ignore the informal review and judge the freeze package directly.
- User says "we will polish later": block and send the work back through exactly one correct scope-matched revision pass; after that pass, keep freeze blocked until the user explicitly restarts a new design cycle.
- User says "make it high fidelity during implementation": block module freeze; high-fidelity visual fidelity must be resolved before the module design-source packet is frozen.
- User says "the module draft failed review, rerun module splitting": block unless the problem is actually global; default to updating the current module `ui/ux` doc and refreshing module visual evidence once.
- User says "users can figure out the flow after reading carefully": block if the key task still needs interpretation instead of guidance.
- User says "the CTA is subtle on purpose": block if the primary action is no longer clearly dominant.
- User says "optimize visuals during implementation": block and route to `flutter-design-source-control`.
