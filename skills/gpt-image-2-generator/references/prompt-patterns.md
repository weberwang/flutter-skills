# Prompt Patterns

Use these patterns when the user gives a broad visual request and the first draft prompt would otherwise be too vague.

## Core Prompt Frame

Keep the prompt grounded in this order:

1. `Use case`
2. `Primary request`
3. `Scene or background`
4. `Subject`
5. `Style or medium`
6. `Composition or framing`
7. `Lighting or mood`
8. `Color palette`
9. `Materials or textures`
10. `Visible text`
11. `Constraints`
12. `Avoid`

The bundled script can assemble this structure automatically when `--augment` is enabled.

## Good Uses

- UI preview boards
- Marketing hero concepts
- Product mockups
- Icon or sticker explorations
- Editorial illustrations

## Prompt Examples

### UI preview

```text
Use case: Mobile App Store preview
Primary request: Design preview for a premium budgeting app
Subject: Three modern phone screens showing onboarding, analytics, and recurring expenses
Style/medium: Product render with polished UI realism
Composition/framing: Centered triptych with generous breathing room
Lighting/mood: Soft studio light, optimistic, premium
Color palette: Emerald, charcoal, warm white
Constraints: Keep screens legible and aligned, no decorative background cards
Avoid: warped devices, fake charts, excessive gradients
```

### Illustration

```text
Use case: Blog cover art
Primary request: Illustration for an article about AI developer workflows
Scene/background: Calm studio desk with layered screens
Subject: Laptop, note cards, and a code assistant visualized as light-based interface elements
Style/medium: Editorial 3D illustration
Lighting/mood: Late afternoon warmth with precise highlights
Palette: Slate, amber, teal
Avoid: sci-fi clutter, unreadable interface text, cyberpunk neon overload
```

## Prompt Review Checklist

- Is the user goal visible in the image without extra explanation?
- Is the subject concrete enough to render consistently?
- Are composition and lighting specified when polish matters?
- Does the prompt explicitly call out what to avoid?
- If visible text matters, is the exact text provided verbatim?
