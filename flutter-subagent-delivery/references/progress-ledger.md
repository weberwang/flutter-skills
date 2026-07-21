# Progress Ledger

Create `.codex-workflow/progress.md` in the target app repo. This is a Controller-only dashboard; use `.codex-workflow/tasks/<task-id>.yaml` for mutable task state.

## Format

```text
# Progress

## Current Phase

- Phase:
- Status:
- Current Gate:
- Gate state: PENDING / BLOCKED / PASSED / WAIVED / STALE
- Gate owner roles:
- Gate evidence/version:
- Controller validation/time:

## App Team Role Activation

| Core role | Enabled | Reason or N/A | Default responsibility | Assigned agent ID |
|---|---|---|---|---|
| Controller | Yes | Required | Orchestration, decisions, Gate recording, integration | |
| Product Manager | | | Scope, value, metrics, business criteria | |
| UX/UI Lead | | | Flow, interaction, visual, accessibility, handoff | |
| Tech Lead | | | Architecture, contracts, technical verdict | |
| Flutter Engineer | | | Client implementation and tests | |
| Backend/Data Engineer | | | API, data, auth, migration, service tests | |
| QA Engineer | | | Independent evidence and quality verdict | |
| DevOps/Release Engineer | | | Build, CI/CD, signing, rollout, rollback | |

## Tasks

- [ ] T01: task name
  - Task state: `.codex-workflow/tasks/T01.yaml`
  - Task owner / lease:
  - Integration base commit / task branch:
  - Worktree:
  - Task profile:
  - Current Gate:
  - DRI role:
  - DRI agent ID:
  - Independent acceptance role:
  - Reviewer/approver agent ID:
  - Consulted roles:
  - Role routing source: `flutter-app-orchestrator/references/subagent-map.md`
  - Accepted upstream evidence/version:
  - Read scope:
  - Write scope:
  - Shared-resource locks:
  - Execution mode: serial / parallel-safe
  - Review snapshot ID/hashes:
  - Gate verdict: PENDING / BLOCKED / PASSED / WAIVED / STALE
  - Gate owner verdicts:
  - Controller validation/time:
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
  - Canonical Pencil file: `docs/design/app-design.pen`
  - Canonical Pencil section/node IDs:
  - Other project `.pen` files: `0` / consolidation required
  - Wireframe level:
  - Wireframe level reason:
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
  - Runtime platform validation: Final platform matrix; level smoke runs after integration-branch merge
  - Module acceptance result:
  - Integration smoke result:
  - Implementer report: `docs/tasks/T01/implementer-report.md`
  - Review: `docs/tasks/T01/review.md`
  - Visual QA agent report: `docs/tasks/T01/visual-qa.md` or `N/A: non-UI task`
  - Verification:
  - Evidence manifest: `docs/tasks/T01/evidence/manifest.md`
  - Commit/diff:

## Assignments and Reports

| Task | Stage | Core role | Specialist seat | Agent ID | Scope | Status | Evidence/version | Independent |
|---|---|---|---|---|---|---|---|---|

## Open Findings

| Severity | Finding | Owner | Status |
|---|---|---|---|

## Notes

-
```

## Rules

- Only the Controller updates the ledger and task-state files. Agents write their reports to the assigned task directory and never claim or complete work by editing the ledger.
- Record the task claim before dispatching work, not only after completion. A claimed task must have an owner, lease, base commit, branch, worktree, and non-overlapping write scope.
- Record team activation before dispatching the first task. Every omitted core role requires `N/A: <reason>`; do not dispatch ceremonial roles.
- Record one DRI and one independent acceptance owner for every task. Producer and reviewer agent IDs must differ, including product, architecture, design, asset, Pencil, code, quality, and release work.
- Record immutable commit/diff identifiers and artifact or evidence versions for every review. Any producer or fixer change marks the previous verdict `STALE` and requires re-review.
- Treat a same-session producer/reviewer fallback as `Independent: No`; it cannot alone pass a high-risk Product, Design, Technical, Quality, or Release Gate.
- Do not advance a Gate when `DONE_WITH_CONCERNS` contains a Critical or Important finding, when mandatory evidence is missing, or when the current review is stale.
- The Controller records Gate state and validates completeness but must not impersonate a missing Product Manager, UX/UI Lead, Tech Lead, QA Engineer, or DevOps/Release verdict.
- Do not mark a business-flow level complete until all of its required tasks, acceptance paths, and cross-module contracts have passed or are explicitly accepted; record the advancement verdict before dispatching any later-level task.
- Run the planned integration smoke after each business-flow level merges to the integration branch, without marking a platform verified. Record device, emulator, simulator, browser, and desktop runtime validation in a final-integration section only after all task entries and required high-fidelity restoration are complete; task-level screenshots and goldens are not platform-verification records.
- For UI page tasks, update each page design gate field before dispatching implementation.
- Keep the canonical Pencil file field fixed to `docs/design/app-design.pen`, record stable section/node IDs, and block Pencil work when another project `.pen` file or active Pencil writer exists.
- Record Full, Lightweight, or Reuse for every UI page. Full requires `390 x 844 px` Pencil evidence; Lightweight records optional Pencil evidence or `N/A`; Reuse records the approved pattern and page-specific delta contract.
- When subagent tools are available, record the assigned design role, report, write scope, and status for every delegable design stage. If unavailable, record the controller-session downgrade explicitly.
- Record the pre-slicing confirmation table version and explicit user decision before dispatching the Asset production agent. Reconfirm and update affected rows after material changes.
- Before creating the first task for a module, record its implementation-stage grilling entry, explicit shared-understanding confirmation, confirmed module scope, and completed function/page refinement. A prior global grilling pass is not a substitute.
- Keep page effect-image candidates, prompts, briefs, and review output transient until the user explicitly confirms a freeze. At freeze, write the exact selected image first under `.codex-workflow/visuals/pages/<page-name>/`; only then write related artifacts and ledger fields. Never create a global frozen effect image.
- For required visual assets, update reuse check, production decision, bitmap source policy, 100%-match evidence, background handling, background transparentization when applicable, transparent post-processing when applicable, generation evidence when used, atlas, slicing manifest, inventory, and fidelity review before Pencil high-fidelity restoration or implementation. An unmatched icon, image, illustration, logo, texture, or bitmap must record the dedicated bitmap-generation path.
- For fields that do not apply, write `N/A: <reason>` instead of leaving them blank.
- Do not re-dispatch accepted tasks after context compaction. Resume from the Controller-owned task-state file and verify the branch commit still exists.
- Record failed commands honestly.
- Record missing screenshots as missing evidence, not as pass.
