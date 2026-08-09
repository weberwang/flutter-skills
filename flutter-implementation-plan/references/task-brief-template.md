# Task Brief

This Markdown file is a human handoff record, not runtime state or automation input. Delete conditional sections that do not apply.

## Task

- ID / name:
- Risk tier / business-flow level:
- Goal:
- Verified integration branch / base SHA:
- Ordinary task branch:
- Prior-level evidence:

## Ownership And Scope

- DRI:
- Read scope:
- Unique write scope:
- Non-goals / prohibited changes:
- Shared resources and single owner:
- Independent acceptance role when required:

## Explicit Parallel Authorization (Conditional)

- User authorization and date:
- Parallel writer or worktree scope explicitly requested:
- Disjoint branch/write scope:
- Controller coordination boundary:

No YAML/JSON workflow state or automatic merge is created even when this section applies.

## Canonical Inputs

- Product / design / technical / module references:
- API contract and version:
- Candidate design/asset evidence:

## API / Service Conditions (Conditional)

- Service implementation owned by this task: Yes / No
- External service owner/dependency when No:
- Auth/permission and security boundary:
- Idempotency, retry, timeout and rate limit:
- Migration/rollback:
- Service tests and contract tests:
- Deployment/monitoring and backup/recovery:
- Client compatibility/deprecation:

## Acceptance

- Functional and failure-state criteria:
- API/service criteria when applicable:
- UI evidence when applicable:
- Security/privacy/data criteria when applicable:

## Verification

- F0 project-native commands:
- Known regression fixtures:
- Foundation startup/routing/plugin smoke (foundation tasks):
- Primary-target runtime smoke (critical-flow tasks):
- Full matrix owner/reference: `docs/architecture/verification-platforms.md`

Task evidence proves only the named scope and cannot claim the complete platform matrix. Do not automatically start physical-device acceptance.

## Review Funnel

- F1 expected change/risk dimensions:
- Conditional F2 read-only lanes and triggers:
- F2 return shape: lane, candidate SHA, covered facts, findings, missing evidence, questions, verdict
- F3 required evidence and authorization:

The implementer returns candidate SHA, changed files, F0 evidence and blockers. Only the Controller writes `docs/tasks/<task-id>/review.md` and copies F2 conclusions into it.
