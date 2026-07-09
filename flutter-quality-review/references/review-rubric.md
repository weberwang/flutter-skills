# Flutter Commercial Review Rubric

## Spec Compliance

- MVP scope implemented and no extra scope added.
- Acceptance criteria are met.
- Required states and flows exist.
- Product assumptions are not silently changed.
- Task follows `docs/plans/module-map.md` for module dependency order, cross-module contracts, and page interaction order.
- Cross-module contracts are implemented before dependent UI or service work consumes them.
- Module acceptance path and integration smoke path are preserved or updated when module behavior changes.
- Module acceptance result and integration smoke result are reported when module boundaries, routes, cross-module contracts, or user flows change.

## Flutter Code Quality

- Project-local `flutter-dev` rules are present, read, and followed.
- State ownership is clear.
- Widgets are focused and not oversized.
- Shared UI primitives are reused.
- Existing plugins and primitives are preferred before new dependencies.
- Riverpod, hooks, Freezed, fpdart, json generation, and ScreenUtil are used according to the fixed stack.
- Annotation-based generation is used for Freezed and JSON models; generated boilerplate is not handwritten.
- `build_runner` was run after annotated model, state, failure, union, or DTO changes.
- State changes are minimal and rebuild scope is controlled.
- Async work handles loading, error, retry, and cancellation where relevant.
- Platform permissions are requested with clear user value.
- No hardcoded secrets or production keys.

## UX/UI

- UI evidence exists for screen changes.
- Page implementation order does not skip required prior interactions, states, or transitions from the module map.
- Page-level high-fidelity mockup was generated after low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- Pencil high-fidelity restoration decision and reason are recorded; required restoration evidence exists for critical, complex, asset-heavy, or visual-parity-sensitive pages.
- Implemented UI respects the selected mockup and recorded design-freeze constraints when present.
- Asset reuse check, production decision, generation evidence when used, atlas, slicing manifest, inventory, and fidelity review exist when approved mockups include required visual assets.
- Required assets are listed in `docs/design/asset-inventory.md`.
- Asset source, reuse decision, generation prompt constraints, background handling, background transparentization when applicable, license status, slicing/export output, Flutter path, loading fallback, and error fallback are recorded.
- New bitmap assets use product-design or image generation evidence by default; Pencil exports are approved only when the exported node is the recorded production asset source.
- Transparent or composited assets have clean alpha edges, preserved shadows/glows, and no unintended background halos.
- Transparent-background post-processing records matte removal, alpha cleanup, edge decontamination, padding, and target-background QA when applicable.
- New generated assets reference global and page design-freeze constraints and explain why existing assets were not reused.
- Bitmap and illustration fidelity matches the approved mockup or Pencil evidence within recorded tolerances.
- Implemented UI respects `docs/design/wireframe-spec.md` when low-fidelity Pencil wireframes are used.
- Implemented UI respects `docs/design/pencil-hifi-restoration.md` when Pencil carries high-fidelity visual restoration.
- Raw Pencil screenshots are not used as the sole implementation spec.
- Layout works on target viewports.
- Empty, loading, error, success, disabled, and permission-denied states are covered where relevant.
- CTA hierarchy is clear.
- Text is readable and not clipped.
- Accessibility basics are respected.

## Commercial Readiness

- Account lifecycle is handled when accounts exist.
- Privacy and data deletion paths are not broken.
- Payments handle failure and restoration when monetized.
- Analytics and crash reporting are present or explicitly out of scope.

## Testing

- `flutter analyze` output is reported.
- Relevant unit/widget tests are reported.
- Golden or screenshot evidence exists for UI work.
- Integration tests are run when a user path is changed and tests exist.

## Output

Start with findings. Use this shape:

```text
Findings
- [Critical] ...
- [Important] ...
- [Minor] ...

Missing evidence
-

Open questions
-

Summary
-
```
