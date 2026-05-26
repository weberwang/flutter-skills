# Feature Map

Replace every placeholder in this file during initialization.

## Primary Features

- `{{FEATURE_1}}`: `{{FEATURE_1_SCOPE}}`
- `{{FEATURE_2}}`: `{{FEATURE_2_SCOPE}}`
- `{{FEATURE_3}}`: `{{FEATURE_3_SCOPE}}`

## Ownership Rules

- `presentation` owns pages, widgets, and UI interaction only
- `application` owns use cases, orchestration, and provider exposure
- `infrastructure` owns DTOs, data sources, repository implementations, and external SDK integration
- `domain` owns entities, value objects, and repository contracts

## Extension Rules

- Prefer extending an existing feature when the new task shares the same business language and lifecycle.
- Create a new bounded feature when the task introduces a distinct business capability, ownership boundary, or dependency cluster.
- Document cross-feature collaboration explicitly instead of creating hidden imports.
