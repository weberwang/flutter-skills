# Subagent Map

Use subagents when work is independent and the controller can continue or integrate safely.

## Recommended Agents

| Agent | Use | Writes code |
|---|---|---|
| Product agent | Product brief, MVP, user stories | No |
| UX agent | Flows, screen states, usability risks | No |
| Mockup agent | Generate high-fidelity screen directions and visual prompts | No |
| Mockup reviewer | Select or reject mockups against product and Flutter feasibility | No |
| Pencil handoff agent | Convert low-fidelity Pencil evidence into Flutter text specs | No |
| Pencil visual restoration agent | Restore approved high-fidelity visuals into Pencil and produce text handoff | No |
| Bitmap enhancement agent | Enhance approved bitmap assets and synchronize each final output to the corresponding design-draft asset or Pencil node | No |
| Wireframe reviewer | Review low-fidelity Pencil wireframes before implementation | No |
| Module planner | Convert global design and architecture into module order and page interaction order | No |
| Flutter init agent | Initialize fixed plugin stack and generate `flutter-dev` | Yes |
| Visual QA agent | Screenshot and golden review | No |
| Architecture agent | Technical design review or alternatives | No |
| Implementer agent | One task brief | Yes |
| Task reviewer agent | Spec and code quality review | No |
| Release agent | Store and production readiness | No |

## Parallel Safe

- Product exploration and UX exploration.
- Mockup generation for different visual directions.
- Architecture alternatives and release risk scan.

## Parallel Unsafe

- Flutter init and feature implementation in the same project.
- Dependency edits and code generation from multiple agents.
- Independent read-only reviews.

## Serialize

- Code implementation in the same Flutter project.
- Tasks that touch shared navigation, theme, generated files, app config, dependency graph, or state container.

## Dispatch Contract

Each subagent receives:

- One role.
- One artifact or task brief path.
- Exact scope.
- Non-scope.
- Required output file or output shape.
- Verification expectations.

Do not paste full session history into subagent prompts.
