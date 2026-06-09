# PRD Completeness Gate

Use this gate before promoting `requirements_brainstorming` to `prd_ready`.

## Purpose

This gate converts "the PRD exists" into a stronger claim:

- the PRD is structurally complete enough
- decision-blocking ambiguity is controlled
- downstream skills can consume the PRD without re-opening basic product scope

## How To Score

Use a 0-2 score for each dimension:

- `0`: missing or unusable
- `1`: present but weak, assumption-heavy, or still ambiguous
- `2`: explicit, actionable, and stable enough for downstream use

## Scoring Dimensions

### 1. Problem And Goal

Check whether the PRD clearly states:

- problem statement
- business goal
- user outcome

### 2. User Roles

Check whether the PRD clearly states:

- primary role
- secondary role if relevant
- role differences when behavior changes by role

### 3. Core Scenarios

Check whether the PRD clearly states:

- happy path
- main completion flow
- key exception path

### 4. Scope And Non-Goals

Check whether the PRD clearly states:

- what is in scope
- what is explicitly out of scope

### 5. States And Edge Cases

Check whether the PRD covers:

- empty
- loading
- error
- permission or access failure when relevant
- business exception path when relevant

### 6. Data And Dependencies

Check whether the PRD clearly states:

- required data
- integrations
- permissions
- media, push, payment, or real-time needs when relevant

### 7. Platform And UX Boundary

Check whether the PRD clearly states:

- target platform hints
- validation surface hints
- UX posture or information-density posture

### 8. Constraints And Compliance

Check whether the PRD clearly states:

- privacy
- compliance
- accessibility
- localization
- timeline or delivery constraints

### 9. Success Metrics

Check whether the PRD includes:

- measurable success metrics
- or explicit acceptance criteria

### 10. Question Ledger Quality

Check whether:

- decision-blocking questions are separated clearly
- defaults are justified
- deferred items are recorded explicitly

## Readiness Threshold

Use this threshold:

- `ready_for_prd_ready`
  - total score >= 16/20
  - no `decision_blocking` item remains unresolved
- `review_but_not_ready`
  - total score between 12 and 15
  - or no blocker remains but multiple critical sections are still weak
- `blocked`
  - total score < 12
  - or any unresolved `decision_blocking` item remains

## Required Output

When running this gate, record:

- total score
- weak dimensions
- unresolved blockers
- whether the PRD can advance

Recommended shape:

```text
PRD completeness:
- total_score: 17/20
- weak_dimensions: 平台与体验边界, 约束条件
- unresolved_decision_blocking: none
- outcome: ready_for_prd_ready
```

## Hard Rules

- Do not promote to `prd_ready` only because a PRD file exists.
- Do not hide unresolved decision-blocking items behind a high numeric score.
- Do not treat copy polish or formatting polish as completeness.
- Do not let downstream technical baseline generation absorb missing core product scope.
