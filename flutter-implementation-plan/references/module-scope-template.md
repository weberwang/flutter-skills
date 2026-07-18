# Module Scope Template

Use this just in time when a module first becomes eligible for implementation. Do not fill the refinement sections or create task briefs until the module-level grilling confirmation is complete.

## Module

- Name:
- Business-flow level:
- Product responsibility:
- Route ownership:
- Data ownership:
- Source PRD and design artifacts:
- Technical design:
- Existing implementation evidence:

## Module-Level Grilling Gate

- Grilling log entry:
- Questions and user answers:
- Included user outcomes confirmed:
- Explicit non-goals confirmed:
- Dependencies and accepted risks confirmed:
- Shared-understanding confirmation:
- Confirmation time:
- Gate verdict: Confirmed / Blocked

## Confirmed Function Inventory

Fill only after the gate verdict is `Confirmed`.

| Function | User outcome | Included behavior | Excluded behavior | Priority | Source decision | Acceptance evidence |
|---|---|---|---|---|---|---|

## Page Function Refinement

Fill only after the confirmed function inventory is complete.

| Page or state | Function | Entry condition | User action | Success result | Empty/loading/error states | Next interaction | Design gate |
|---|---|---|---|---|---|---|---|

## Cross-Module Refinement

| Contract | Provider | Consumer | Data or event | Failure behavior | Required before |
|---|---|---|---|---|---|

## Module Acceptance Path

- Start state:
- Primary path:
- Success evidence:
- Integration smoke path:
- Deferred functions:

## Task Refinement

| Task ID | Vertical slice | Page or state | Depends on | Expected write scope | Acceptance criteria | Verification |
|---|---|---|---|---|---|---|

## Open Decisions

| Decision | Impact | Owner | Blocking |
|---|---|---|---|
