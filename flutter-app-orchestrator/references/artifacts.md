# Artifact Contract

Create these artifacts in the target Flutter app repo as the workflow advances.

For module or page-level UI work, store repeated design artifacts under a page or module scoped path, for example `docs/design/pages/<page-name>/design-freeze.md`, while keeping the same document contract.

## Product

`docs/product/grilling-log.md`

- PRD availability check and reviewed source artifacts.
- One-question-at-a-time decision log, including recommendation and user answer.
- Confirmed decisions, unresolved items, decision dependencies, and rejected alternatives.
- Light visual interrogation answers for the derived expression preset (once before global visual exploration).
- User's explicit shared-understanding confirmation.

`docs/product/product-brief.md`

- Target user.
- Problem and high-value moment.
- MVP promise.
- First-value moment, safe-to-try conditions, and trust evidence.
- Product character, avoided impressions, and decoration rule.
- Visual expression preset: preset ID, category/audience derivation, axis values, wow requirement, light-interrogation commitments, and any later pin/raise/loosen override.
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

`docs/product/market-analysis.md`

- Target market and category context.
- Competitor and adjacent-product patterns.
- User expectations and category visual conventions.
- Differentiation opportunities, commercial risks, and evidence sources.
- Implications for global visual-direction exploration.

## Design

`docs/design/user-flows.md`

- Primary path.
- First-run path.
- First-value path and its time or interaction target.
- Trust, permission, payment, privacy, and recovery points that may interrupt first-time use.
- Account and settings path.
- Payment path when monetized.
- Error recovery path.

`docs/design/screen-spec.md`

- Screen purpose.
- First-value contribution and trust or risk concerns.
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
- Aesthetic verdict, its visual evidence, and required fixes for user-facing UI work.
- First-value, trust, and safe-to-try verification for each applicable user-facing flow.

`docs/design/pages/<page-name>/mockup-brief.md`

- Screen, module, or flow to visualize.
- Product context.
- Device targets.
- Required states.
- Source wireframe spec for page-level module work.
- Active visual expression preset, page-type budget dial, and whether a restatable signature moment is required.
- Image prompt constraints.
- Formal prompt file path.
- PRD alignment status.

`docs/design/global/prompts/visual-direction-prompt.md`

- Template source and version.
- PRD source artifacts: product brief, MVP scope, user stories, user flows, screen specification, and applicable decisions.
- Market-analysis source, relevant findings, and source location.
- Requirement mapping: PRD requirement or market finding, prompt expression, and source location.
- Product-design-principle check: primary user task, scoped functionality, information hierarchy, single primary action where applicable, mobile accessibility, realistic content, and approved visual constraints.
- Active visual expression preset: preset ID, axes, required three-direction mix, scoring-weight emphasis, and light-interrogation commitments.
- Three-direction comparison specification.
- Three recommended candidate directions, each tied to PRD needs, market opportunity, category conventions, differentiation opportunity, and the preset’s required mix; categories are not restricted to template examples, and the set must not collapse into three restrained professional looks.
- User's explicit selected direction; no automatic selection.
- Restatable-signature confirmation when Global Freeze Signature Rule applies, or recorded N/A reason when it does not; any pin / raise / loosen override after selection.
- Autonomously selected representative page and PRD-based selection rationale.
- Shared representative-page task, device, information structure, copy, data, and state.
- Confirmation that the page high-fidelity prompt template was used for each candidate direction without saving separate representative-page prompt files.
- Written only after the selected global direction is explicitly frozen; until then, keep the prompt transient in the conversation.

`docs/design/pages/<page-name>/prompts/hifi-mockup-prompt.md`

- Template source and version.
- PRD and approved design source artifacts.
- Requirement mapping: page task, state, copy, data, actions, visual constraints, and source location.
- Product-design-principle check: primary user task, scoped functionality, information hierarchy, primary-action clarity, mobile accessibility, realistic content, and approved visual constraints.
- Active visual expression preset, page-type budget dial, and whether this page must show a restatable signature moment.
- Final generation prompt used for the page-level effect image.
- Written only after the selected page image is explicitly frozen; until then, keep the prompt transient in the conversation.

`docs/design/global/design-freeze.md`

- Global visual direction.
- Brand tone.
- Visual expression preset in force, including any pin / raise / loosen override.
- Required signature moment commitment for hero-class pages.
- Color system.
- Typography and shape language.
- Illustration and icon style.
- Material, lighting, and texture rules.
- Banned visual styles.
- Reuse rules for visual assets.
- Scope limitation: this baseline does not approve a page effect image, page design freeze, or page implementation. The global exploration's representative-page images are direction-comparison evidence only.
- Frozen image record: `.codex-workflow/visuals/global/frozen-<slug>.png`, source candidate ID, decoded dimensions, SHA-256, and user confirmation time.

`docs/design/pages/<page-name>/pencil-intake.md`

- Low-fidelity Pencil source context.
- Target frames or nodes.
- Screens and states.
- Screenshots, layout snapshots, or exports.
- Open questions.

`docs/design/pages/<page-name>/pencil-flutter-handoff.md`

- Layout constraints.
- Tokens.
- Component mapping.
- Assets.
- State requirements.
- Approved deviations.

`docs/design/pages/<page-name>/pencil-hifi-restoration.md`

- Selected high-fidelity mockup.
- Design-freeze dependency.
- Module or page task.
- Restoration decision and reason.
- Effect-image restoration analysis that classifies each restorable layer or atomic unit as exactly one of: bitmap, UI, or data; composite elements must be split into these units before classification.
- Data placeholders, including the preserved hierarchy, text length, and layout constraints.
- Per-bitmap source, crop, size, background treatment, target Pencil node, and 100% approved-visual-content match verdict. A recorded rasterization or scaling tolerance may not change bitmap content.
- Per-UI native-Flutter feasibility decision, reason, expected implementation approach, and screenshot or golden confirmation. When native Flutter cannot reproduce the unit exactly, record the bitmap-fill requirement, reason, and generated bitmap evidence; otherwise record that no bitmap generation is required.
- Target Pencil frames or nodes.
- Restored visual roles.
- Asset restoration evidence.
- Generated or enhanced bitmap synchronization evidence, including source asset, final asset, and target Pencil node.
- Deviations and approval.
- Flutter handoff constraints.

`docs/design/pages/<page-name>/wireframe-review.md`

- Low-fidelity Pencil evidence.
- Navigation and hierarchy review.
- Missing states.
- Ambiguities.
- Required text-spec changes.

`docs/design/pages/<page-name>/wireframe-spec.md`

- Text-only implementation spec derived from Pencil wireframes.
- Screen structure.
- Navigation behavior.
- Component roles.
- State requirements.
- Constraints and non-goals.

`docs/design/pages/<page-name>/pencil-parity-review.md`

- Wireframe text spec.
- Pencil evidence used only for review questions.
- Flutter evidence.
- Parity findings.
- Accepted deviations.

`docs/design/pages/<page-name>/asset-atlas.md`

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

`docs/design/pages/<page-name>/asset-slicing-manifest.md`

- Export batch.
- Output files.
- Format.
- Logical and pixel size.
- DPR.
- Production mode.
- Background transparentization method when applicable.
- Flutter path.
- `pubspec.yaml` entries.

`docs/design/pages/<page-name>/asset-fidelity-review.md`

- Approved mockup.
- Atlas and slicing manifest.
- Per-asset match verdict.
- Global style consistency.
- Page-level constraint compliance.
- Duplicate generation check.
- Background transparentization and transparent post-processing evidence when applicable.
- Enhanced bitmap parity between the design draft and Flutter production asset.
- Allowed rasterization or scaling tolerance; it must not change approved bitmap content.
- Approved deviations.
- Blocking fixes.

`docs/design/pages/<page-name>/asset-inventory.md`

- Asset list.
- Source and ownership.
- Enhancement lineage and synchronized design-draft location when applicable.
- Production format.
- Flutter path.
- License status.
- Fidelity requirements.
- Loading and error fallbacks.

`docs/design/pages/<page-name>/design-freeze.md`

- Selected frozen mockup path under `.codex-workflow/visuals/pages/<page-name>/`.
- Source candidate ID, decoded dimensions, SHA-256, and user confirmation time.
- Active expression preset and page-type budget dial.
- Required signature moment for this page, or N/A with reason.
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
- Final-integration timing: run device, browser, emulator, simulator, and desktop runtime validation only after all modules/pages and high-fidelity restoration are complete; task-level screenshots or goldens do not verify a platform.
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
- Frozen effect-image path, candidate ID, decoded dimensions, SHA-256, and confirmation time.
- Pencil high-fidelity restoration decision.
- Pencil high-fidelity restoration reason.
- Effect-image bitmap/UI/data analysis and any UI bitmap-fill decision.
- Bitmap enhancement synchronization evidence when applicable.
- Module acceptance result.
- Integration smoke result.
- Confirmed-task cleanup decision, including deleted paths or `N/A`.

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
