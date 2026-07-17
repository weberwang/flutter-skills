# Flutter Commercial Review Rubric

## Spec Compliance

- MVP scope implemented and no extra scope added.
- Acceptance criteria are met.
- Required states and flows exist.
- Product assumptions are not silently changed.
- Task follows `docs/plans/module-map.md` for business-flow level, module dependency order, cross-module contracts, and page interaction order.
- No task started before all required tasks, acceptance paths, and cross-module contracts of its preceding business-flow level passed or were explicitly accepted.
- Cross-module contracts are implemented before dependent UI or service work consumes them.
- Module acceptance path and integration smoke path are preserved or updated when module behavior changes.
- Module acceptance result and integration smoke result are reported when module boundaries, routes, cross-module contracts, or user flows change.
- `docs/architecture/verification-platforms.md` records the global platform scope; unlisted platforms are not claimed as verified, and device/emulator/simulator/browser/desktop runtime validation is deferred to final integration.

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
- `@product-design audit` findings for user-facing flows are resolved or explicitly accepted.
- Page implementation order does not skip required prior interactions, states, or transitions from the module map.
- Page-level high-fidelity mockup was generated after low-fidelity Pencil structure, Wireframe Review, and `docs/design/wireframe-spec.md`.
- Pencil high-fidelity restoration decision and reason are recorded; required restoration evidence exists for critical, complex, asset-heavy, or visual-parity-sensitive pages.
- High-fidelity Pencil restoration uses the selected page-level mockup and page design freeze as the visual source of truth; the wireframe is applied only to page scope, structure, states, and interactions.
- Implemented UI respects the selected mockup and recorded design-freeze constraints when present.
- Asset reuse check, production decision, generation evidence when used, atlas, slicing manifest, inventory, and fidelity review exist when approved mockups include required visual assets.
- Required assets are listed in `docs/design/asset-inventory.md`.
- Asset source, reuse decision, generation prompt constraints, background handling, background transparentization when applicable, license status, slicing/export output, Flutter path, loading fallback, and error fallback are recorded.
- New bitmap assets use product-design or image generation evidence by default; Pencil exports are approved only when the exported node is the recorded production asset source.
- Every icon, image, illustration, logo, texture, and bitmap unit has 100%-match evidence and a separate-asset review verdict. An unmatched resource completed dedicated bitmap generation and asset fidelity review; near-match system icons, Flutter components, and existing assets are rejected.
- Transparent or composited assets have clean alpha edges, preserved shadows/glows, and no unintended background halos.
- Transparent-background post-processing records matte removal, alpha cleanup, edge decontamination, padding, and target-background QA when applicable.
- New generated assets reference global and page design-freeze constraints and explain why existing assets were not reused.
- Icon, image, illustration, logo, texture, and bitmap fidelity matches the approved mockup 100%; only documented rasterization or scaling tolerance is allowed.
- Implemented UI respects `docs/design/wireframe-spec.md` for page scope, structure, states, and interactions when low-fidelity Pencil wireframes are used.
- Implemented UI respects `docs/design/pencil-hifi-restoration.md` when Pencil carries high-fidelity visual restoration.
- Raw Pencil screenshots are not used as the sole implementation spec.
- Layout works on target viewports.
- Empty, loading, error, success, disabled, and permission-denied states are covered where relevant.
- CTA hierarchy is clear.
- The first-value path is understandable, and the user sees applicable privacy, payment, permission, or recovery conditions before a high-friction or irreversible step.
- Text is readable and not clipped.
- Accessibility basics are respected.

## Visual Aesthetics And Premium Feel

- Compare the implementation screenshot with the approved mockup and design-freeze constraints before judging aesthetics.
- Verify hierarchy, alignment, spacing rhythm, typography, color and contrast, component consistency, and asset quality as one visual system.
- Verify that decoration, borders, shadows, corner radii, and accent colors are purposeful and match the active expression preset and page-type budget; flag visual noise, generic treatment, competing focal points, and missing signature on full-budget or wow-required pages. Do not require austerity when the preset calls for higher signature strength.
- Verify that the screen gives visual priority to the primary user task and uses content imagery or assets that fit the product and target audience.
- Verify that the visual system supports the documented product character and that polish does not conceal unclear value, unnecessary friction, or unresolved trust concerns.
- Record an explicit verdict: `approved`, `approved with Minor findings`, or `not approved`. A Critical or Important aesthetic finding results in `not approved` until resolved or explicitly accepted.

## Commercial Readiness

- Account lifecycle is handled when accounts exist.
- Privacy and data deletion paths are not broken.
- Payments handle failure and restoration when monetized.
- Analytics and crash reporting are present or explicitly out of scope.

## Testing

- `fvm flutter analyze` output is reported.
- Relevant unit/widget tests are reported.
- Golden or screenshot evidence exists for UI work.
- Integration tests are run when a user path is changed and tests exist.
- Task-level review reports static analysis, relevant tests, and screenshot/golden design evidence without claiming runtime platform verification. Final-integration review, after all modules/pages and high-fidelity restoration are complete, requires each globally in-scope platform's matching command output and runtime UI evidence; missing device, simulator, emulator, browser, or desktop evidence blocks final delivery and release claims.

## Output

Start with findings. Use this shape:

```text
Findings
- [Critical] ...
- [Important] ...
- [Minor] ...

Aesthetic verdict
- approved / approved with Minor findings / not approved
- Evidence and remaining actions: ...

Missing evidence
-

Open questions
-

Summary
-
```
