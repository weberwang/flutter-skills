# Progress Ledger

Create `.codex-workflow/progress.md` in the target app repo. This is a Controller-only dashboard; use `.codex-workflow/tasks/<task-id>.yaml` for mutable task state.

## Format

```text
# Progress

## Current Phase

- Phase:
- Status:

## Tasks

- [ ] T01: task name
  - State file: `.codex-workflow/tasks/T01.yaml`
  - Owner / lease:
  - Base commit / task branch:
  - Worktree:
  - Brief:
  - Business-flow level:
  - Required prior-level evidence:
  - Module:
  - Page/state:
  - Low-fidelity Pencil:
  - Wireframe review:
  - Wireframe spec:
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
  - Pencil Flutter handoff:
  - Flutter evidence:
  - Runtime platform validation: Deferred to final integration
  - Module acceptance result:
  - Integration smoke result:
  - Implementer report: `docs/tasks/T01/implementer-report.md`
  - Review: `docs/tasks/T01/review.md`
  - Visual QA: `docs/tasks/T01/visual-qa.md` or `N/A: non-UI task`
  - Evidence manifest: `docs/tasks/T01/evidence/manifest.md`
  - Commit/diff:

## Open Findings

| Severity | Finding | Owner | Status |
|---|---|---|---|

## Notes

-
```

## Rules

- Only the Controller updates the ledger and task-state files. Agents return reports to their task directory and never claim or complete work by editing the ledger.
- Record the task claim before dispatching work, not only after completion. A claimed task must have an owner, lease, base commit, branch, worktree, and non-overlapping write scope.
- Do not mark a business-flow level complete until all of its required tasks, acceptance paths, and cross-module contracts have passed or are explicitly accepted; record the advancement verdict before dispatching any later-level task.
- Record device, emulator, simulator, browser, and desktop runtime validation in a final-integration section only after all task entries and required high-fidelity restoration are complete; task-level screenshots and goldens are not platform-verification records.
- For UI page tasks, update each page design gate field before dispatching implementation. Keep page artifacts under `docs/design/pages/<page-name>/` and global artifacts under `docs/design/global/`.
- Keep effect-image candidates, prompts, and briefs transient until the user explicitly confirms a freeze. At freeze, write the exact selected image first under `.codex-workflow/visuals/global/` or `.codex-workflow/visuals/pages/<page-name>/`; then retain the candidate IDs, prompt hashes, review verdict, confirmation time, frozen file hash, and cleanup list in the task visual-decision record.
- For required visual assets, update reuse check, production decision, bitmap source policy, 100%-match evidence, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, atlas, slicing manifest, inventory, and fidelity review before Pencil high-fidelity restoration or implementation. An unmatched icon, image, illustration, logo, texture, or bitmap must record the dedicated bitmap-generation path.
- For fields that do not apply, write `N/A: <reason>` instead of leaving them blank.
- Do not re-dispatch accepted tasks after context compaction. Resume from the Controller-owned task-state file and verify the branch commit still exists.
- Record failed commands honestly.
- Record missing screenshots as missing evidence, not as pass.
