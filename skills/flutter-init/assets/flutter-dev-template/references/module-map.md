# Module Map

Replace every placeholder in this file during initialization.

## Primary Modules

- `{{MODULE_1}}`: `{{MODULE_1_SCOPE}}`
- `{{MODULE_2}}`: `{{MODULE_2_SCOPE}}`
- `{{MODULE_3}}`: `{{MODULE_3_SCOPE}}`

## Ownership Rules

- `presentation` owns pages, widgets, and UI interaction only
- `application` owns use cases, orchestration, and provider exposure
- `infrastructure` owns DTOs, data sources, repository implementations, and external SDK integration
- `domain` owns entities, value objects, and repository contracts

## Extension Rules

- Prefer extending an existing module when the new task shares the same business language and lifecycle.
- Create a new bounded module when the task introduces a distinct business capability, ownership boundary, or dependency cluster.
- Document cross-module collaboration explicitly instead of creating hidden imports.
