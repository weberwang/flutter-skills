# Visual QA Rubric

Review screenshots or golden evidence, not intent.

## Required Viewports

- Small phone: 360x640 or close equivalent.
- Standard phone: 390x844 or close equivalent.
- Tablet: 768x1024 or close equivalent.
- Any app-specific landscape or foldable layout when relevant.

## Findings

Report by severity:

- Critical: core action unusable, unreadable content, broken navigation, severe overflow, privacy/payment risk.
- Important: unclear hierarchy, missing required state, weak recovery, contrast failure, inconsistent component style.
- Minor: polish issue that does not block task acceptance.

## Checklist

- Main user goal is obvious in 3 seconds.
- Primary CTA is visually dominant and reachable.
- Text does not clip or overflow.
- Loading, empty, error, disabled, and success states match the UI brief.
- Spacing and typography use the chosen design system.
- Screen remains usable with long content.
- Mobile layout is not a compressed desktop layout.
- No generic AI UI tells: random gradients, fake metrics, filler avatars, inconsistent card shapes.
- Motion supports state or hierarchy and respects reduced motion.
- `@product-design audit` findings for the user-facing flow are resolved or explicitly accepted.

## Output Shape

1. Verdict: Pass / Fail.
2. Findings.
3. Missing evidence.
4. Required fixes.
5. Optional polish.
