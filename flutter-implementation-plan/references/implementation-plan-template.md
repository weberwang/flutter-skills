# Implementation Plan Template

## Global Constraints

- Flutter app, mobile first.
- Follow the approved product, UI, and technical specs.
- Use the generated project-local `flutter-dev` skill for implementation tasks.
- Do not add features outside MVP scope.
- UI tasks require screenshot or golden evidence.
- UI page tasks require low-fidelity Pencil structure, Wireframe Review, page-level high-fidelity mockup approval, an exact frozen image under `.codex-workflow/visuals/pages/<page-name>/`, global and page design-freeze constraints, required asset atlas evidence, Pencil high-fidelity restoration decision, required restoration evidence, and Flutter handoff before page code starts.
- Module and page tasks must follow `docs/plans/module-map.md` for business-flow levels, module dependencies, cross-module contracts, and page interaction order. Finish and verify each level before starting the next; parallel work is limited to explicitly parallel-safe tasks in the same level.
- Treat the cross-module task list as provisional until the current module becomes eligible. Re-run grilling for that module, record explicit shared understanding, then refine its functions, page functions, states, acceptance path, and task briefs in `docs/plans/modules/<module-name>-scope.md`.
- Follow the global platform scope in `docs/architecture/verification-platforms.md`. Do not treat unlisted platforms as verified.
- Defer device, emulator, simulator, browser, and desktop runtime validation until final integration after all module/page tasks and required high-fidelity restoration are complete. Task-level screenshots or goldens are design evidence only.
- Every task requires verification output.

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
- Design-freeze outputs:
- Asset atlas outputs:
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

| ID | Business-flow level | Module | Module scope confirmation | Task | Depends on and prior-level evidence | Write scope | Design gate | Verification | UI evidence |
|---|---|---|---|---|---|---|---|---|---|
