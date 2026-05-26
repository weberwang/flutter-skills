# Pencil Prompt Pack

## Use This File For

- turning a mobile UI discussion into prompts that can be pasted into Pencil MCP
- producing a reusable prompt pack instead of one vague paragraph
- generating richer results without defaulting to image spam or random effects

## Build Prompts In Layers

Always separate:

1. `direction summary`
2. `master prompt`
3. `negative constraints`
4. `page prompts`
5. `implementation guardrails`

This structure is more reliable than one oversized prompt.

## Master Prompt Template

```text
Design a mobile app screen set for [product type].

Product posture: [precision tool / quiet assistant / expressive consumer app].
Information density: [sparse / balanced / dense].
Visual temperature: [cool precision / warm calm / dark focus].
Primary de-native strategy: [typography and rhythm / material depth / illustration or imagery / motion].

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
2. master prompt
3. negative constraints
4. page prompts
5. implementation guardrails

## Flutter Guardrails

When the user also cares about implementation:

- preserve hierarchy, grouping, spacing ratios, and motion intent
- do not copy every decorative effect literally if it weakens performance or clarity
- keep interaction targets mobile-safe even when the visual style becomes more refined
- preserve state clarity first, polish second
