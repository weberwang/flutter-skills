# PRD Template

Use this template when `requirements_brainstorming` must produce or rewrite a PRD artifact from raw demand.

## Purpose

This template standardizes what a workflow-valid PRD must contain before the run can move to `prd_ready`.

The goal is not visual polish. The goal is downstream clarity:

- the orchestrator can prove the PRD exists
- `flutter-prd-rd-writer` can consume it without guessing
- Product Design can confirm the brief without reopening product scope
- module splitting can inherit clean scope boundaries later

## Preferred Artifact Path

Unless the project already has a stronger convention, store the PRD under:

`docs/prd/<project-or-feature-slug>.prd.md`

If the workflow is still in discovery and a final slug is not stable yet, use a temporary but explicit name rather than leaving the PRD untracked in chat.

## Required Companion Artifact Path

Unless the project already has a stronger convention, store the companion page navigation artifact under:

`docs/project/page-navigation-flow.md`

This artifact must be generated and confirmed before the PRD can be drafted for `review_ready` or promoted to `prd_ready`.

## Required Front Matter

Put a small metadata block at the top:

```yaml
---
artifact_type: prd
name: <project-or-feature-name>
status: draft | review_ready | approved
owner: <team-or-role>
source_input: raw_requirement | brief | rewrite
scope_level: app | feature | workflow
last_updated: YYYY-MM-DD
---
```

## Required Companion Navigation Artifact

Before the PRD is drafted, revised, or marked `review_ready` or `approved`, generate or update the companion `docs/project/page-navigation-flow.md` artifact and confirm it first.

Use a Mermaid flowchart and make sure it shows:

- every in-scope page using names consistent with the PRD
- the main entry point for the current scope
- the primary task path across pages
- important branch routes, modal jumps, and return paths when they affect scope understanding
- any deferred pages or states clearly marked as deferred instead of silently mixed into the main path

The PRD should be refined from this confirmed artifact and reference it in its scenario or scope prose instead of duplicating the same navigation logic in multiple sections.

## Required Chapter Order

Use this order unless a project convention already enforces a stricter one:

1. `背景与问题陈述`
2. `目标与成功标准`
3. `目标用户与角色`
4. `核心场景与用户旅程`
5. `范围内功能`
6. `明确不做`
7. `关键状态与异常场景`
8. `数据、权限与外部依赖`
9. `平台与体验边界`
10. `约束条件`
11. `问题台账`
12. `假设、风险与后续事项`
13. `变更记录`

## Chapter Expectations

### 1. 背景与问题陈述

State:

- what business or user problem exists
- why now
- what happens if the problem stays unresolved

### 2. 目标与成功标准

State:

- primary business goal
- primary user outcome
- measurable success metrics or acceptance criteria

Avoid vague phrases such as "improve experience" unless they are paired with observable outcomes.

### 3. 目标用户与角色

State:

- primary role
- secondary role if relevant
- permission or access differences when relevant

### 4. 核心场景与用户旅程

State:

- happy path
- main entry points
- completion path
- critical fallback or retry path

### 5. 范围内功能

List the feature scope in concrete product language.

Each item should be specific enough that downstream technical and design work can tell whether it belongs in the first delivery scope.

### 6. 明确不做

List what is intentionally excluded from this PRD.

This section is mandatory. It prevents later stages from silently expanding scope.

### 7. 关键状态与异常场景

Cover at least:

- empty
- loading
- error
- permission denied
- long-content or short-content edge cases when relevant
- business failure or rollback path when relevant

### 8. 数据、权限与外部依赖

State:

- required entities or data inputs
- upload/download/media needs
- login or session needs
- role/permission gating
- external systems or vendor dependencies

### 9. 平台与体验边界

State:

- target surface when known
- platform hints
- UX posture
- information density expectations
- whether the requirement is MVP-first, growth-first, or enterprise-first

Do not freeze detailed UI here.

### 10. 约束条件

Cover:

- compliance
- privacy
- accessibility
- localization
- performance
- schedule or delivery constraints

### 11. 问题台账

Use three subsections:

- `decision_blocking`
- `defaultable`
- `deferred`

For each question, record:

- question
- current answer or status
- why it matters
- owner if follow-up is required

### 12. 假设、风险与后续事项

Make assumptions explicit instead of hiding them in prose.

For each major assumption, include:

- assumption
- rationale
- risk if wrong

### 13. 变更记录

Record at least:

- what changed
- why it changed
- whether scope expanded, shrank, or only clarified

## Minimum Ready Conditions

A PRD using this template is ready for `prd_ready` only when:

- the artifact exists on disk
- the companion `docs/project/page-navigation-flow.md` artifact exists on disk, has already been confirmed, and matches the PRD scope
- all `decision_blocking` questions are resolved or explicitly approved as defaults
- scope and non-goals are both explicit
- success metrics or acceptance criteria exist
- assumptions and risks are visible

If any of those are missing, keep the workflow in `requirements_brainstorming`.
