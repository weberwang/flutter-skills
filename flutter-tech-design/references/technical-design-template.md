# Technical Design Template

## Context

- Product:
- MVP:
- App type:
- Verification platform scope: `docs/architecture/verification-platforms.md`

## Architecture Decisions

| Area | Decision | Reason | Rejected alternatives |
|---|---|---|---|
| State management | | | |
| Routing | | | |
| Persistence | | | |
| Networking | | | |
| Auth | | | |
| Payments | | | |
| Analytics | | | |
| Crash reporting | | | |
| Fixed Flutter stack | Riverpod, hooks, Freezed, fpdart, json generation, ScreenUtil | | |
| Code generation | Freezed/json annotations plus build_runner | | |

## Module Boundaries

| Module | Responsibility | Route ownership | State owner | Data owner | External dependencies |
|---|---|---|---|---|---|

## Cross-Module Contracts

| Contract | Provider | Consumer | Data or event | Failure mode |
|---|---|---|---|---|

## Shared Foundations

- Design system:
- Routing shell:
- Auth/session:
- Error model:
- Analytics/crash reporting:
- Test utilities:

## Data Model

| Entity | Owner | Persistence | Privacy sensitivity |
|---|---|---|---|

## Error Handling

- Network:
- Auth:
- Payment:
- Offline:
- Data corruption:

## Environment and Secrets

- Dev:
- Staging:
- Production:
- Secret handling:

## Flutter Init

- `flutter-project-init` required: Yes / No
- Generated `flutter-dev` path:
- Flutter environment: FVM
- Fixed stack deviations:
- Approved package additions:

## Testing Strategy

- Unit:
- Widget:
- Golden:
- Integration:
- Manual release checks:

## Verification Commands

- `fvm flutter analyze`
- `fvm flutter test`
- `fvm flutter test integration_test`

## Risks

| Risk | Mitigation |
|---|---|
