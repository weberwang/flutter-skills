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

| Business-flow level | Work item | Can run parallel | Why | Shared files to avoid | Task branch/worktree |
|---|---|---|---|---|---|

## Shared-Path Ownership

| Path or path group | Sole owner task | Why it must be serialized | Handoff evidence |
|---|---|---|---|

## Risks

| Risk | Module | Impact | Mitigation |
|---|---|---|---|
