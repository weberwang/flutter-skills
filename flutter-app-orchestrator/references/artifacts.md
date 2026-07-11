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
- Formal prompt file path.
- PRD alignment status.

`docs/design/prompts/global-visual-direction-prompt.md`

- Template source and version.
- PRD source artifacts: product brief, MVP scope, user stories, user flows, screen specification, and applicable decisions.
- Requirement mapping: PRD requirement, prompt expression, and source location.
- Product-design-principle check: primary user task, scoped functionality, information hierarchy, single primary action where applicable, mobile accessibility, realistic content, and approved visual constraints.
- Three-direction comparison specification; representative-page image prompts are stored in the per-candidate page prompt files.

`docs/design/prompts/global-visual-directions/<direction-name>-representative-page-hifi-mockup-prompt.md`

- Page high-fidelity prompt template source and candidate direction name.
- Shared representative-page task, device, information structure, copy, data, and state.
- Candidate-only visual-direction fields.
- PRD requirement mapping and product-design-principle check.
- Final generation prompt used for that candidate's representative-page effect image.

`docs/design/prompts/pages/<page-name>-hifi-mockup-prompt.md`

- Template source and version.
- PRD and approved design source artifacts.
- Requirement mapping: page task, state, copy, data, actions, visual constraints, and source location.
- Product-design-principle check: primary user task, scoped functionality, information hierarchy, primary-action clarity, mobile accessibility, realistic content, and approved visual constraints.
- Final generation prompt used for the page-level effect image.

`docs/design/mockup-review.md`

- Candidate mockups.
- Selection verdict.
- Independent reviewer findings: the five highest-impact problems or an explicit “no material issue” verdict, each tied to the reviewed image and with a concrete fix.
- Iteration notes.
- User decision to apply or decline the proposed changes.
- Confirmation that page-level mockups were generated after Wireframe Review when applicable.

`docs/design/global-design-freeze.md`

- Global visual direction.
- Brand tone.
- Color system.
- Typography and shape language.
- Illustration and icon style.
- Material, lighting, and texture rules.
- Banned visual styles.
- Reuse rules for visual assets.

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
- Generated or enhanced bitmap synchronization evidence, including source asset, final asset, and target Pencil node.
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
- Global design freeze.
- Page design freeze.
- Reuse check.
- Production decision.
- Background handling and transparentization work node when applicable.
- Asset groups.
- Source or generation plan.
- Bitmap enhancement plan and the design-draft synchronization target when enhancement is required.
- Generation prompts and selected outputs when assets are generated.
- Enhanced output, replaced design-draft asset or Pencil node, and updated design evidence.
- Flutter mapping.
- Open asset decisions.

`docs/design/asset-slicing-manifest.md`

- Export batch.
- Output files.
- Format.
- Logical and pixel size.
- DPR.
- Production mode.
- Background transparentization method when applicable.
- Flutter path.
- `pubspec.yaml` entries.

`docs/design/asset-fidelity-review.md`

- Approved mockup.
- Atlas and slicing manifest.
- Per-asset match verdict.
- Global style consistency.
- Page-level constraint compliance.
- Duplicate generation check.
- Background transparentization and transparent post-processing evidence when applicable.
- Enhanced bitmap parity between the design draft and Flutter production asset.
- Tolerance.
- Approved deviations.
- Blocking fixes.

`docs/design/asset-inventory.md`

- Asset list.
- Source and ownership.
- Enhancement lineage and synchronized design-draft location when applicable.
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

`docs/architecture/verification-platforms.md`

- Target verification platforms.
- Unsupported platforms with `N/A: <reason>`.
- Required command, device, browser, emulator, simulator, screenshot, or golden evidence per platform.
- Evidence storage location and update owner.

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
- Bitmap enhancement synchronization evidence when applicable.
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
