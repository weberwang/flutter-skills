# Flutter Design System Baseline

Use Material 3 unless the product or platform requires another system.

## Required Tokens

- `AppColors`: semantic colors, not raw brand names.
- `AppTypography`: display, title, body, label scales.
- `AppSpacing`: 4/8 based scale.
- `AppRadius`: consistent radius levels.
- `AppElevation`: shadows or surfaces.
- `AppMotion`: durations and curves.

## Required Primitives

- App scaffold.
- Primary, secondary, destructive, and disabled buttons.
- Text field with label, helper, error, disabled, loading.
- Empty state.
- Error state with recovery action.
- Loading skeleton that matches final layout.
- Toast/snackbar for transient feedback.
- Dialog or bottom sheet for blocking choices.

## Flutter Implementation Notes

- Prefer `ThemeData(useMaterial3: true)`.
- Use semantic color roles from `ColorScheme`.
- Avoid hardcoded sizes inside screens when a token exists.
- Avoid one-off buttons or fields that bypass shared primitives.
- Add Chinese comments only for non-obvious logic in source code, not for simple widget declarations.

## Accessibility

- Check contrast for text and CTAs.
- Support text scaling unless the screen is a fixed-format canvas.
- Keep touch targets at least 48x48 logical pixels where practical.
- Provide semantic labels for icon-only actions.
