# Progress Ledger

Create `.codex-workflow/progress.md` in the target app repo.

## Format

```text
# Progress

## Current Phase

- Phase:
- Status:

## Tasks

- [ ] T01: task name
  - Brief:
  - Business-flow level:
  - Required prior-level evidence:
  - Module:
  - Module grilling log entry:
  - Module shared-understanding confirmation:
  - Confirmed module scope:
  - Module function refinement:
  - Page function refinement:
  - Module Effect-Image Interrogation Gate:
  - Page structure agent report:
  - Page/state:
  - Low-fidelity Pencil:
  - Wireframe reviewer report:
  - Wireframe review:
  - Wireframe spec:
  - Page high-fidelity agent report:
  - Final compact image prompt:
  - Prompt quality check:
  - Effect Image Reviewer report:
  - High-fidelity mockup:
  - Frozen mockup path:
  - Mockup candidate ID:
  - Mockup decoded dimensions:
  - Mockup SHA-256:
  - Mockup freeze confirmation time:
  - Mockup approval:
  - Global design freeze:
  - Design freeze:
  - Asset atlas:
  - Bitmap decomposition agent report:
  - Asset planning agent report:
  - Pre-slicing confirmation table version:
  - Pre-slicing user decision/time:
  - Asset production agent report:
  - Asset reuse check:
  - Asset production decision:
  - Asset bitmap source policy:
  - Asset 100%-match evidence:
  - Asset background handling:
  - Asset background transparentization:
  - Asset transparent post-processing:
  - Asset generation evidence:
  - Asset slicing manifest:
  - Asset inventory:
  - Asset fidelity review:
  - Pencil high-fidelity restoration decision:
  - Pencil high-fidelity restoration reason:
  - Pencil high-fidelity restoration:
  - Pencil restoration agent report:
  - Pencil Flutter handoff:
  - Flutter evidence:
  - Runtime platform validation: Deferred to final integration
  - Module acceptance result:
  - Integration smoke result:
  - Implementer report:
  - Review:
  - Visual QA agent report:
  - Verification:
  - Evidence:
  - Commit/diff:

## Open Findings

| Severity | Finding | Owner | Status |
|---|---|---|---|

## Notes

-
```

## Rules

- Update the ledger after each completed task.
- Do not mark a business-flow level complete until all of its required tasks, acceptance paths, and cross-module contracts have passed or are explicitly accepted; record the advancement verdict before dispatching any later-level task.
- Record device, emulator, simulator, browser, and desktop runtime validation in a final-integration section only after all task entries and required high-fidelity restoration are complete; task-level screenshots and goldens are not platform-verification records.
- For UI page tasks, update each page design gate field before dispatching implementation.
- When subagent tools are available, record the assigned design role, report, write scope, and status for every delegable design stage. If unavailable, record the controller-session downgrade explicitly.
- Record the pre-slicing confirmation table version and explicit user decision before dispatching the Asset production agent. Reconfirm and update affected rows after material changes.
- Before creating the first task for a module, record its implementation-stage grilling entry, explicit shared-understanding confirmation, confirmed module scope, and completed function/page refinement. A prior global grilling pass is not a substitute.
- Keep page effect-image candidates, prompts, briefs, and review output transient until the user explicitly confirms a freeze. At freeze, write the exact selected image first under `.codex-workflow/visuals/pages/<page-name>/`; only then write related artifacts and ledger fields. Never create a global frozen effect image.
- For required visual assets, update reuse check, production decision, bitmap source policy, 100%-match evidence, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, atlas, slicing manifest, inventory, and fidelity review before Pencil high-fidelity restoration or implementation. An unmatched icon, image, illustration, logo, texture, or bitmap must record the dedicated bitmap-generation path.
- For fields that do not apply, write `N/A: <reason>` instead of leaving them blank.
- Do not re-dispatch completed tasks after context compaction.
- Record failed commands honestly.
- Record missing screenshots as missing evidence, not as pass.
