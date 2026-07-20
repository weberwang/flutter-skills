# App Team and Subagent Map

Use this file as the single source of truth for App team assembly, task routing, and subagent boundaries. Read [app-team-role-prompts.md](../../flutter-subagent-delivery/references/app-team-role-prompts.md) before creating role cards and [design-subagent-orchestration.md](../../flutter-subagent-delivery/references/design-subagent-orchestration.md) for the design-only production sequence.

## Operating Model

Form a temporary feature squad for the current task instead of dispatching every available specialist:

- Controller: orchestration, user decisions, Gate recording, conflict resolution, and final integration.
- Product Manager: product value, scope, priority, metrics, and business acceptance criteria.
- UX/UI Lead: flows, interaction, visual system, accessibility, assets, and design handoff.
- Tech Lead: architecture, contracts, non-functional requirements, engineering order, and technical verdict.
- Flutter Engineer: client implementation and client-side tests.
- Backend/Data Engineer: APIs, auth, schemas, migrations, data quality, and service-side tests.
- QA Engineer: independent test strategy, review evidence, regression, and quality verdict.
- DevOps/Release Engineer: build, CI/CD, environments, signing, artifacts, monitoring, rollout, and rollback.

Specialized design, research, implementation, and review agents are temporary seats under one core role. Map them with [app-team-role-prompts.md](../../flutter-subagent-delivery/references/app-team-role-prompts.md); do not treat them as permanent team members.

## Team Assembly Gate

Before dispatching work, the Controller must record:

1. Task profile and current workflow Gate.
2. Enabled core roles and `N/A: <reason>` for omitted roles.
3. One DRI role and agent.
4. One independent reviewer or acceptance role and agent.
5. Consulted roles, if any.
6. Exact read and write scopes.
7. Accepted upstream evidence and blocking dependencies.
8. Parallel or serialized execution decision.

Do not dispatch a task without a DRI, independent acceptance owner, and role activation reason.

## Task Routing

| Task profile | DRI | Independent acceptance | Consult when needed | Gate |
|---|---|---|---|---|
| Product discovery, PRD, scope, metrics | Product Manager | Controller records user acceptance | UX/UI Lead, Tech Lead, QA Engineer | Product |
| User flow, page structure, visual direction, design assets | UX/UI Lead specialist | Independent UX/UI reviewer; QA for implementation evidence | Product Manager, Flutter Engineer | Design |
| Architecture, cross-module contract, technical risk | Tech Lead | Independent Tech Lead reviewer or QA evidence review | Flutter, Backend/Data, DevOps | Technical |
| Flutter page, state, route, client feature | Flutter Engineer | QA Engineer; Tech Lead for high-risk code | UX/UI Lead, Backend/Data Engineer | Task implementation |
| API, auth, payment, sync, schema, migration, analytics pipeline | Backend/Data Engineer | QA Engineer; Tech Lead for contract/security | Flutter Engineer, DevOps/Release Engineer | Data/service implementation |
| Test strategy, regression, acceptance, visual QA | QA Engineer | Controller validates independence and evidence | Product Manager, UX/UI Lead, Tech Lead | Quality |
| CI/CD, signing, build, store, rollout, rollback | DevOps/Release Engineer | QA Engineer plus Controller authorization | Tech Lead, Flutter, Backend/Data, Product Manager | Release |
| Bug fix | Owning Flutter or Backend/Data Engineer | QA Engineer | Tech Lead, UX/UI Lead | Task implementation |
| Cross-cutting refactor or performance work | Tech Lead or owning engineer | Independent Tech Lead reviewer plus QA Engineer | DevOps/Release Engineer | Technical and Quality |

### Activation Conditions

- Enable Backend/Data for API, account, auth, payment, cloud sync, remote data, schema, migration, server analytics, or service observability work. For a verified local-only App, record `N/A: no service or persisted remote-data scope`.
- Enable UX/UI for any user-visible structure, copy hierarchy, interaction, state, visual, asset, or accessibility change.
- Enable Tech Lead for architecture, shared foundations, cross-module contracts, dependency changes, security/privacy risk, migrations, performance budgets, or integration decisions.
- Enable QA before implementation planning when acceptance or regression scope must be defined, not only after coding.
- Enable DevOps/Release during technical design when environments, CI/CD, signing, store distribution, observability, rollout, or rollback are in scope; it owns the Release Gate.
- For a narrow, already-confirmed client task, Product Manager may be `N/A` when the task brief already carries accepted business scope.

## Specialist Seats

| Core role | Specialist seats |
|---|---|
| Product Manager | Market analysis agent, product-spec agent |
| UX/UI Lead | UX agent, Global direction agent/reviewer, Page structure agent, Wireframe reviewer, Page high-fidelity agent, Effect Image Reviewer, Bitmap decomposition agent, Asset planning/production agent, Pencil restoration agent |
| Tech Lead | Architecture agent, Module planner, technical reviewer |
| Flutter Engineer | Flutter init agent, Flutter implementer, Flutter fixer |
| Backend/Data Engineer | API/data implementer, migration implementer, service fixer |
| QA Engineer | Task reviewer, Visual QA agent, acceptance reviewer, Final reviewer |
| DevOps/Release Engineer | Release agent, CI/CD implementer, rollout/rollback reviewer |

Each specialist receives the core role prompt plus exactly one specialist prompt. The narrower specialist scope wins. A producer and reviewer must be different agent instances even when they share the same core discipline.

## Parallel Safe

- Read-only product, market, architecture, risk, or release exploration.
- UX/UI and technical exploration after accepted product scope, when outputs do not overlap.
- Independent vertical slices in the same business-flow level after contracts are accepted and write scopes are disjoint.
- Independent page or asset production after shared design freezes and with disjoint paths.
- Independent read-only reviews.

## Parallel Unsafe

- A producer and its reviewer before production is complete.
- Flutter initialization and feature implementation in the same project.
- Client and service implementation before their API/data contract is accepted.
- Asset planning and production before explicit user confirmation.
- Schema migration and a release that depends on it.
- Any overlapping file, generated output, dependency, route, theme, state container, app configuration, environment, or secret reference.
- Any two writers to `docs/design/app-design.pen`, even with disjoint node assignments.

## Dispatch Contract

Every subagent receives the role-card envelope from [app-team-role-prompts.md](../../flutter-subagent-delivery/references/app-team-role-prompts.md), plus:

- one core role and, when applicable, one specialist seat;
- one task brief or artifact path;
- accepted upstream Gate evidence;
- exact scope and non-scope;
- exact read and write paths;
- required output and verification;
- independent reviewer identity;
- instruction to return `NEEDS_CONTEXT` instead of inferring confirmation;
- status shape: `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`.

Do not paste full session history into subagent prompts. Package only the accepted facts and artifacts needed by the assigned role.

## Decision Authority

- Product Manager recommends the product verdict; the user or Sponsor approves business scope.
- UX/UI Lead and independent design reviewers issue design verdicts; the user selects candidates and the Controller records freezes.
- Tech Lead issues technical verdicts and integration constraints.
- QA Engineer has evidence-based quality veto for Critical, unresolved Important, failed acceptance, or missing mandatory evidence.
- DevOps/Release Engineer issues release-readiness verdicts; actual external release requires explicit Controller-recorded authorization.
- Controller validates process completeness and records Gate outcomes but must not impersonate a missing product, design, technical, quality, or release verdict.
