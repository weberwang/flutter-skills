# Subagent Map

Use specialized subagents for delegable design production and review whenever subagent tools are available. Keep user decisions, confirmations, freezes, sequencing, conflict resolution, and final integration in the controller. Follow [design-subagent-orchestration.md](../../flutter-subagent-delivery/references/design-subagent-orchestration.md).

## Recommended Agents

| Agent | Use | Write scope |
|---|---|---|
| Product/UX agent | Draft product brief, MVP, user stories, flows, states, and screen specs from confirmed decisions | Assigned product/design docs |
| Market analysis agent | Market context, competitor patterns, category conventions, differentiation opportunities, and evidence sources | `market-analysis.md` |
| Global direction agent | Produce exactly three traceable visual-system definitions | Transient response or assigned draft only |
| Global direction reviewer | Independently review direction traceability, differentiation, accessibility, implementation cost, and preset compliance | Review report only |
| Page structure agent | Create low-fidelity Pencil structure and text specification | Assigned page Pencil/spec paths |
| Wireframe reviewer | Independently review structure, states, interaction, and scope compliance | Review report only |
| Page high-fidelity agent | Generate exactly three page candidates from frozen inputs | Transient candidates only |
| Effect Image Reviewer | Independently review completed mockups against product goals, Flutter feasibility, Apple HIG, and the active visual expression preset | Review report only |
| Bitmap decomposition agent | Perform ownership classification, visual sweep, and coverage audit | Assigned restoration-analysis path |
| Asset planning agent | Prepare reuse decisions and complete pre-slicing confirmation table | Assigned asset-atlas draft |
| Asset production agent | Produce only confirmed assets and evidence | Confirmed asset, manifest, inventory, and review paths |
| Pencil visual restoration agent | Restore approved visuals and produce Flutter handoff | Assigned Pencil/restoration paths |
| Module planner | Refine one eligible module after controller-recorded confirmation | Assigned module plan paths |
| Flutter init agent | Initialize fixed plugin stack and generate `flutter-dev` | Project initialization scope |
| Visual QA agent | Screenshot and golden review | Review report only |
| Architecture agent | Technical design review or alternatives | Assigned architecture docs |
| Implementer agent | One task brief | Explicit code scope |
| Task reviewer agent | Spec and code quality review | Review report only |
| Release agent | Store and production readiness | Release report only |

## Parallel Safe

- Product exploration and UX exploration.
- Market analysis and confirmed-scope UX drafting.
- Independent page or asset production only after shared freezes and with disjoint write scopes.
- Architecture alternatives and release risk scan.
- Independent read-only reviews.

## Parallel Unsafe

- Flutter init and feature implementation in the same project.
- Dependency edits and code generation from multiple agents.
- A producer and its reviewer before production has completed.
- Asset planning and asset production before user confirmation.

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
- For implementation work, the confirmed module scope and its grilling-log entry.
- Required user-confirmation dependency and explicit instruction to return `NEEDS_CONTEXT` rather than infer approval.
- Exact status/report shape: `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`.

Do not paste full session history into subagent prompts.
