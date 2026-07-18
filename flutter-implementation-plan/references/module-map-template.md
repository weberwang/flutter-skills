# Module Map Template

Use this before implementation planning. It turns global design and architecture into module boundaries, business-flow levels, and page interaction order. A level is determined by prerequisite business outcomes and dependencies, not by folder or technical-layer naming.

## Global Context

- Product scope:
- Primary user path:
- Navigation model:
- Technical design:
- Flutter init:
- Generated `flutter-dev` skill:

## Module Inventory

| Module | Product responsibility | Route ownership | Data ownership | Shared dependencies | Release priority |
|---|---|---|---|---|---|

## Cross-Module Contracts

| Contract | Provider module | Consumer module | Data or event | Required before |
|---|---|---|---|---|

## Module Dependency Graph

| Module | Depends on | Blocks | Reason |
|---|---|---|---|

## Business-Flow Levels

| Level | Module | Business-flow prerequisite | Entry task | Exit evidence | Required before next level |
|---|---|---|---|---|---|

## Module Refinement Status

The initial plan may leave refinement pending. Complete each row just in time when the module first becomes eligible for implementation.

| Module | Eligible after | Module grilling status | Grilling confirmation | Confirmed scope file | Function/page refinement status |
|---|---|---|---|---|---|

## Level Advancement Gate

| Level | Required task and contract evidence | Acceptance path | Advancement verdict | Explicitly accepted exception |
|---|---|---|---|---|

## Module Acceptance Paths

| Module | Acceptance path | Start state | Success evidence | Integration smoke path |
|---|---|---|---|---|

## Page Interaction Levels

| Level | Module | Page or state | Previous interaction | Next interaction | Required design gate | Exit evidence |
|---|---|---|---|---|---|---|

## Parallelization

| Business-flow level | Work item | Can run parallel | Why | Shared files to avoid |
|---|---|---|---|---|

## Risks

| Risk | Module | Impact | Mitigation |
|---|---|---|---|
