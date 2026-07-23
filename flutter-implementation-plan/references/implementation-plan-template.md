# Implementation Plan Template

## Global Constraints

- Flutter app, mobile first.
- Follow the approved product, UI, and technical specs.
- Use the generated project-local `flutter-dev` skill for implementation tasks.
- Do not add features outside MVP scope.
- UI tasks require screenshot or golden evidence.
- UI page tasks require only the design evidence selected by page and task risk. Complex or high-risk pages may require wireframe review, high-fidelity freeze, assets, or Pencil handoff; ordinary reuse work may rely on the approved UI spec and page decision.
- Module and page tasks must follow `docs/plans/module-map.md` for business-flow levels, module dependencies, cross-module contracts, and page interaction order. Finish and verify each level before starting the next; parallel work is limited to explicitly parallel-safe tasks in the same level.
- Treat the cross-module task list as provisional until the current module becomes eligible. Audit existing decisions, run grilling only for material unresolved choices, then refine functions, states, acceptance paths, and task briefs.
- Follow the global platform scope in `docs/architecture/verification-platforms.md`. Do not treat unlisted platforms as verified.
- Run an integration smoke after each business-flow level merges to the integration branch. Defer the full device, emulator, simulator, browser, and desktop runtime matrix until final integration after all module/page tasks and required high-fidelity restoration are complete. Task-level screenshots or goldens are design evidence only.
- Every task requires executed verification output before formal review.

## Module Map

- Module map:
- Business-flow levels:
- Level advancement gates:
- Module acceptance paths:
- Cross-module contracts:
- Page interaction levels:
- Parallelization limits:
- Module refinement status:
- Confirmed module scope files:

## Milestones

### M0: Foundation

- Goal:
- Flutter init:
- Generated `flutter-dev` skill:
- Tasks:
- Verification:

### M1: Design System and Navigation

- Goal:
- Tasks:
- Verification:

### M1.5: Confirmed High-Fidelity Inputs

- Goal:
- Screens or flows:
- Mockup evidence:
- Page design decisions:
- Asset manifests:
- Verification:

### M2: Core Data and Services

- Goal:
- Tasks:
- Verification:

### M3: Primary User Path

- Goal:
- Tasks:
- Verification:

### M4: Account, Privacy, and Settings

- Goal:
- Tasks:
- Verification:

### M5: Monetization

- Goal:
- Tasks:
- Verification:

### M6: Release Hardening

- Goal:
- Tasks:
- Verification:

### M6.5: Final Platform Runtime Validation

- Entry condition: all business-flow levels, module/page functionality, and required high-fidelity restoration are complete.
- Platforms: `docs/architecture/verification-platforms.md`
- Runtime evidence:
- Blocking findings and fixes:
- Verification:

## Task List

| ID | Risk | Business-flow level | Module | Task | Depends on and prior-level evidence | Isolation | Write scope | Design gate | Verification | UI evidence |
|---|---|---|---|---|---|---|---|---|---|---|
