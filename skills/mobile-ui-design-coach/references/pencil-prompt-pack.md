# Pencil Prompt Pack

## Use This File For

- turning a mobile UI discussion into prompts that can be pasted into Pencil MCP
- producing a reusable prompt pack instead of one vague paragraph
- generating richer results without defaulting to image spam or random effects

## Build Prompts In Layers

Always separate:

1. `direction summary`
2. `design freeze card`
3. `master prompt`
4. `negative constraints`
5. `page prompts`
6. `implementation guardrails`

This structure is more reliable than one oversized prompt.

Prompts should express decisions that already exist. Do not use a generated preview to invent the brief, art direction, or production states.

## Design Freeze Card Inputs

Include these fields before writing the master prompt:

- `设计简报`: audience, usage moment, page scope, constraints
- `平台基线`: HIG behavior baseline unless the user explicitly sets another rule
- `艺术指导`: posture, density, temperature, material language, type personality, visual memory
- `核心路径`: first impression, primary action, result, next best action, return loop
- `状态矩阵`: ideal, empty, loading, error, permission, partial-data, locked or premium
- `必须一致项`: hierarchy, key proportions, copy, tokens, assets, or motion that must survive later stages
- `允许工程化调整项`: details Pencil or Flutter may simplify without breaking the direction

## Master Prompt Template

```text
Design a mobile app screen set for [product type].

Product posture: [precision tool / quiet assistant / expressive consumer app].
Information density: [sparse / balanced / dense].
Visual temperature: [cool precision / warm calm / dark focus].
Primary de-native strategy: [typography and rhythm / material depth / illustration or imagery / motion].
Commercial goal: [activation / retention / conversion / trust / habit / other].
Platform baseline: HIG behavior baseline for safe areas, touch targets, navigation, feedback, readability, and accessibility.
Core path: [first impression -> primary action -> result -> next best action -> return loop].
Required states: [ideal / empty / loading / error / permission / partial-data / locked or premium].
Must stay consistent: [hierarchy / proportions / key copy / palette / asset posture / motion role].
Allowed engineering adjustments: [minor spacing normalization / asset redraw / component simplification].

Visual goal: make the interface feel commercially polished and product-specific, not like default iOS or Android system components.

Layout goal: create a clear focal hierarchy, distinct information zones, and a strong rhythm between headline content, supporting information, and actions.

Surface goal: use [surface approach], with [border / shadow / contrast] treatment kept restrained and intentional.

Interaction goal: prioritize thumb reach, glanceability, and fast state recognition. This is a mobile interface, not a web dashboard compressed into a phone.

Brand feeling: [short tone sentence].
```

## Negative Constraints Template

```text
Avoid default iOS and Android settings-screen aesthetics.
Avoid identical card weights across every section.
Avoid generic SaaS dashboard layouts on a phone.
Avoid using gradients, glow, glass, photos, or illustration unless they have a clear role.
Avoid equal emphasis on all actions.
Avoid oversized banner areas that weaken task focus.
Avoid default button, input, and list proportions if they make the UI feel like a stock component gallery.
Avoid portfolio-only mockups that ignore empty, loading, error, permission, and paid states.
Avoid decorative premium effects that do not clarify hierarchy, brand memory, or state feedback.
Avoid letting preview composition override the approved design freeze card.
Avoid custom visuals that break HIG-baseline behavior or interaction expectations.
```

## Page Prompt Templates

### Primary Screen

```text
Design the primary screen as a product surface, not a marketing page or default settings view.
Use one dominant zone, one secondary zone, and one support zone.
Make the main action or the main information focus obvious but not loud.
Use spacing and hierarchy to make the screen feel intentional and product-specific.
```

### Collection Screen

```text
Design the collection screen for scanning speed and structured comparison.
Use grouping, metadata rhythm, and surface hierarchy to prevent the screen from reading like a plain system list.
Reduce repetitive separators and rely on spacing, typography, and subtle surfaces.
Make selection, filtering, and state changes feel precise and mobile-safe.
```

### Detail Screen

```text
Design the detail view as a focused workspace.
Use a strong title hierarchy, clearly separated metadata, and a calm editing or reading surface.
Keep high-frequency actions close, but avoid turning the screen into a toolbar wall.
Use structure and spacing to create depth before adding decoration.
```

### Creation Or Editing Surface

```text
Design the creation or editing surface to feel intentional and refined, not like a stock form.
Group related inputs, reduce visual noise, and make the submit path very clear.
Use section rhythm, label hierarchy, and subtle material shifts to differentiate the screen from default system forms.
```

## Output Shape

Return the prompt pack in this order:

1. direction summary
2. design freeze card
3. master prompt
4. negative constraints
5. page prompts
6. implementation guardrails

## Flutter Guardrails

When the user also cares about implementation:

- preserve hierarchy, grouping, spacing ratios, and motion intent
- do not copy every decorative effect literally if it weakens performance or clarity
- keep interaction targets mobile-safe even when the visual style becomes more refined
- preserve state clarity first, polish second
- preserve the commercial state map so production screens do not regress to happy-path-only design
- preserve HIG-baseline safe areas, touch targets, navigation, readability, feedback, and accessibility
