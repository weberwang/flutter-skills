# Artifact Contract

Create these artifacts in the target Flutter app repo as the workflow advances.

For module or page-level UI work, store repeated design artifacts under a page or module scoped path, for example `docs/design/pages/<page-name>/design-freeze.md`, while keeping the same document contract.

## Product

`docs/product/product-brief.md`

- Target user.
- Problem and high-value moment.
- MVP promise.
- Commercial model.
- Success metrics.
- Risks and assumptions.

`docs/product/mvp-scope.md`

- In scope.
- Out of scope.
- Release-blocking acceptance criteria.
- Later backlog.

`docs/product/user-stories.md`

- User stories.
- Given/When/Then acceptance criteria.
- Priority.
- Release status.

## Design

`docs/design/user-flows.md`

- Primary path.
- First-run path.
- Account and settings path.
- Payment path when monetized.
- Error recovery path.

`docs/design/screen-spec.md`

- Screen purpose.
- Information hierarchy.
- Actions.
- Required states.
- Responsive rules.
- Accessibility requirements.

`docs/design/ui-quality-gates.md`

- Screen list.
- Required states per screen.
- Screenshot or golden evidence requirements.
- Visual QA verdicts.

`docs/design/mockup-brief.md`

- Screen, module, or flow to visualize.
- Product context.
- Device targets.
- Required states.
- Source wireframe spec for page-level module work.
- Image prompt constraints.

`docs/design/mockup-review.md`

- Candidate mockups.
- Selection verdict.
- Findings.
- Iteration notes.
- Confirmation that page-level mockups were generated after Wireframe Review when applicable.

`docs/design/pencil-intake.md`

- Low-fidelity Pencil source context.
- Target frames or nodes.
- Screens and states.
- Screenshots, layout snapshots, or exports.
- Open questions.

`docs/design/pencil-flutter-handoff.md`

- Layout constraints.
- Tokens.
- Component mapping.
- Assets.
- State requirements.
- Approved deviations.

`docs/design/pencil-hifi-restoration.md`

- Selected high-fidelity mockup.
- Design-freeze dependency.
- Module or page task.
- Restoration decision and reason.
- Target Pencil frames or nodes.
- Restored visual roles.
- Asset restoration evidence.
- Deviations and approval.
- Flutter handoff constraints.

`docs/design/wireframe-review.md`

- Low-fidelity Pencil evidence.
- Navigation and hierarchy review.
- Missing states.
- Ambiguities.
- Required text-spec changes.

`docs/design/wireframe-spec.md`

- Text-only implementation spec derived from Pencil wireframes.
- Screen structure.
- Navigation behavior.
- Component roles.
- State requirements.
- Constraints and non-goals.

`docs/design/pencil-parity-review.md`

- Wireframe text spec.
- Pencil evidence used only for review questions.
- Flutter evidence.
- Parity findings.
- Accepted deviations.

`docs/design/asset-atlas.md`

- Page or module.
- Approved mockup.
- Asset groups.
- Source or generation plan.
- Flutter mapping.
- Open asset decisions.

`docs/design/asset-slicing-manifest.md`

- Export batch.
- Output files.
- Format.
- Logical and pixel size.
- DPR.
- Flutter path.
- `pubspec.yaml` entries.

`docs/design/asset-fidelity-review.md`

- Approved mockup.
- Atlas and slicing manifest.
- Per-asset match verdict.
- Tolerance.
- Approved deviations.
- Blocking fixes.

`docs/design/asset-inventory.md`

- Asset list.
- Source and ownership.
- Production format.
- Flutter path.
- License status.
- Fidelity requirements.
- Loading and error fallbacks.

`docs/design/design-freeze.md`

- Selected mockup path.
- Frozen layout.
- Tokens.
- Components.
- State requirements.
- Flutter implementation constraints.

`docs/architecture/flutter-init.md`

- Target project.
- Fixed plugin stack status.
- Generated `flutter-dev` skill path.
- Required app setup.
- Verification output.

## Architecture

`docs/architecture/technical-design.md`

- Architecture decisions.
- Data ownership.
- State management.
- Routing.
- Persistence.
- API boundaries.
- Auth, payments, analytics, crash reporting.
- Verification commands.

`docs/plans/module-map.md`

- Module inventory.
- Product responsibility per module.
- Route ownership.
- Data ownership.
- Cross-module contracts.
- Module dependency graph.
- Implementation order.
- Module acceptance paths.
- Integration smoke paths.
- Page interaction order.
- Parallelization limits.

## Delivery

`docs/plans/implementation-plan.md`

- Milestones.
- Task briefs.
- Verification commands.
- Dependencies.

`.codex-workflow/progress.md`

- Task status.
- Commit or diff range.
- Test evidence.
- Review verdict.
- UI page design gate evidence.
- Pencil high-fidelity restoration decision.
- Pencil high-fidelity restoration reason.
- Module acceptance result.
- Integration smoke result.

`.codex-workflow/decisions.md`

- Decision.
- Reason.
- Alternatives rejected.
- Date.

`.codex-workflow/risks.md`

- Risk.
- Severity.
- Owner.
- Mitigation.
- Status.
