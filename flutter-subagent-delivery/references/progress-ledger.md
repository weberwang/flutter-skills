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
  - Module:
  - Page/state:
  - Low-fidelity Pencil:
  - Wireframe review:
  - Wireframe spec:
  - High-fidelity mockup:
  - Mockup approval:
  - Design freeze:
  - Pencil high-fidelity restoration decision:
  - Pencil high-fidelity restoration reason:
  - Pencil high-fidelity restoration:
  - Pencil Flutter handoff:
  - Asset inventory:
  - Flutter evidence:
  - Module acceptance result:
  - Integration smoke result:
  - Implementer report:
  - Review:
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
- For UI page tasks, update each page design gate field before dispatching implementation.
- For fields that do not apply, write `N/A: <reason>` instead of leaving them blank.
- Do not re-dispatch completed tasks after context compaction.
- Record failed commands honestly.
- Record missing screenshots as missing evidence, not as pass.
