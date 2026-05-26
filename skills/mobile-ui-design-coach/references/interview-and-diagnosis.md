# Interview and Diagnosis

## Use This File For

- choosing the right clarifying question when the design direction is vague
- explaining why a mobile screen feels too native, plain, or generic
- selecting a stronger commercial direction before writing prompts

## Four-Axis Interview

Ask one question at a time. If the user already answered one or more axes, only ask for the missing ones.

### 1. Product Posture

What kind of product should this feel like?

- `precision tool`: calm, exact, professional, focused
- `quiet assistant`: helpful, soft, low-friction, friendly
- `expressive consumer app`: emotional, branded, memorable, lifestyle-led

### 2. Information Density

How much should fit on the screen?

- `sparse`: strong focus, large breathing room, few actions
- `balanced`: moderate density, the safest default
- `dense`: more data, more controls, still clearly grouped

### 3. Visual Temperature

What emotional temperature should the UI carry?

- `cool precision`: silver, graphite, slate, clinical confidence
- `warm calm`: off-white, sand, muted olive, paper-like quietness
- `dark focus`: charcoal, ink, graphite, immersive concentration

### 4. De-Native Strategy

What should do the heavy lifting when removing the default system look?

- `typography and rhythm`: hierarchy, spacing, grouping, cadence
- `material depth`: subtle layers, contrast, borders, surface changes
- `illustration or imagery`: controlled hero assets, not decoration spam
- `motion`: restrained transitions, feedback, reveal timing

## Native-Feel Diagnosis Checklist

Use these signals to explain why a screen feels too native:

- every card, block, and control has the same visual weight
- system-default radii, padding, and proportions dominate the page
- the screen reads like a settings page or form, not a product surface
- there is no focal point or hero hierarchy
- actions and data are all presented at the same level
- decoration is missing, or present but purposeless
- the motion language is unspecified, so the result feels static
- the page copies web dashboard conventions into a phone layout

When diagnosing, translate symptoms into design action. Example: “All modules look equal” should become “Create one dominant zone, one secondary zone, and one passive support zone.”

## Direction Archetypes

### Precision-Led

Use when the product should feel exact, calm, and professional.

- strong typography hierarchy
- minimal ornament
- clear rhythm and grouping
- surfaces used sparingly
- no real-photo dependency
- no hero image by default

### Material-Led

Use when the product needs more polish without becoming decorative.

- subtle layer separation
- low-contrast surface shifts
- fine borders instead of heavy shadows
- restrained highlights

### Expressive Utility

Use when the product needs stronger brand presence or a more memorable mood.

- stronger section framing
- richer text rhythm
- controlled imagery or illustration
- still mobile-first, not visual noise

## Recommendation Heuristic

- If the user wants a more serious or premium result, start with structure and hierarchy before adding decoration.
- If the screen feels boring but should stay serious, add material polish before adding imagery.
- If the user asks for “more commercial” but the product is still utility-first, upgrade hierarchy and material first, then consider controlled illustration or motion.
- If the user asks for more pictures or effects, ask whether they want brand memory, emotional warmth, or clearer hierarchy. The answer decides the tool.

## Output Pack Shape

After diagnosis, structure the answer in this order:

1. short direction summary
2. why the current UI feels native
3. recommended direction
4. prompt pack or page guidance
5. implementation guardrails
