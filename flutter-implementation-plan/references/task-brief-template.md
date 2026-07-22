# Task Brief Template

Replace every placeholder before dispatching this brief to its routed App team role.

## Task

- ID:
- Name:
- Milestone:
- Business-flow level:
- Required prior-level evidence:
- Task state: `.codex-workflow/tasks/<task-id>.yaml`
- Base commit / task branch / worktree:
- Controller integration worktree / branch:
- 活动任务状态：仅在 Controller 集成 worktree 中未提交保存；任务分支不得携带该文件。
- 自动收尾命令：`python <flutter-subagent-delivery>/scripts/finalize-task.py .codex-workflow/tasks/<task-id>.yaml --integration-worktree <集成-worktree> --integration-branch <集成分支>`
- Runtime platform validation: Final platform matrix; level integration smoke is scheduled after merge
- Module grilling log entry:
- Module shared-understanding confirmation:
- Confirmed module scope: `docs/plans/modules/<module-name>-scope.md`
- Module Effect-Image Interrogation Gate: Required for UI / N/A — evidence:
- Goal:

## Team Assignment

- Task profile:
- Current Gate:
- DRI core role:
- DRI agent ID: Assigned at dispatch
- Specialist seat:
- Independent acceptance role:
- Reviewer/approver agent ID: Assigned at dispatch; must differ from producer
- Consulted roles:
- Omitted roles and `N/A: <reason>`:
- Role routing source: `flutter-app-orchestrator/references/subagent-map.md`
- Accepted upstream evidence/version:
- Shared-resource locks:
- Evidence manifest: `docs/tasks/<task-id>/evidence/manifest.md`
- Report directory: `docs/tasks/<task-id>/`
- Execution mode: serial / parallel-safe
- Review snapshot requirement: commit/diff ID plus artifact and evidence versions

## Scope

Must do:

- 

Must not do:

- 

## Inputs

- Product spec:
- Local `flutter-dev` skill:
- Module map:
- Confirmed module scope:
- Module Effect-Image Interrogation Gate:
- UI brief:
- Global design freeze:
- Design freeze:
- Wireframe spec:
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
- Pencil handoff:
- Pencil high-fidelity restoration decision:
- Pencil high-fidelity restoration reason:
- Pencil high-fidelity restoration:
- Technical design:
- Existing files:

## Page Design Gate

Required for UI page task: Yes / No

If yes:

- Page or module:
- Low-fidelity Pencil source:
- Wireframe review:
- Wireframe text spec:
- High-fidelity mockup brief:
- Selected frozen high-fidelity mockup: `.codex-workflow/visuals/pages/<page-name>/frozen-<slug>.png`
- Mockup candidate ID / SHA-256 / confirmation time:
- Approval record:
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
- Required assets:
- Allowed deviations:

## Module Context

- Module:
- Confirmed included functions:
- Confirmed non-goals:
- Refined page functions:
- Module responsibility:
- Route ownership:
- Data ownership:
- Depends on modules:
- Blocks modules:
- Cross-module contracts:
- Page interaction order:
- Module acceptance path:
- Module acceptance result:
- Integration smoke path:
- Integration smoke result:

## Expected Write Scope

- 

## Read and Non-Scope

- Read scope:
- Must not write:
- Must not decide:

## Acceptance Criteria

- 

## Verification Commands

- `fvm flutter analyze`
- `fvm flutter test`

## UI Evidence

Required: Yes / No

If yes:

- Viewports:
- Golden test:
- Screenshot path:
- Mockup source:
- Runtime platform validation: Final platform matrix; screenshot/golden is design evidence only and level smoke runs only after integration-branch merge
- Global design freeze:
- Required assets:
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
- Low-fidelity Pencil source:
- Pencil high-fidelity restoration decision:
- Pencil high-fidelity restoration reason:
- High-fidelity Pencil restoration:
- Wireframe text spec:
- Allowed deviations:

## Report Contract

Return:

- Status: DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED
- Changed files.
- Tests run and output summary.
- Screenshots or golden evidence.
- Module acceptance result.
- Integration smoke result.
- Task branch commit SHA.
- 自动合并提交 / 状态提交 / worktree 与分支清理结果。
- Concerns.
- Gate verdict.
- Missing evidence.
- Recommended next role.
