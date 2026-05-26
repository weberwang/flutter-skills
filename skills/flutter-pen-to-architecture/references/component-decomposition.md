# Component Decomposition

## Goal

Turn design structure into a reusable Flutter component system without over-fragmenting the UI.

## Component Layers

Use these buckets unless the design clearly needs different names:

- primitives
- composite widgets
- business widgets
- page sections

## Primitive Candidates

Usually include:

- buttons
- chips
- badges
- input shells
- icon-label rows
- avatars
- dividers
- pills

Only extract them when their anatomy or styling repeats.

## Composite Widget Candidates

Usually include:

- cards with repeated content zones
- setting rows
- metric blocks
- media list tiles
- segmented pickers
- filter bars
- bottom action areas

These should expose meaningful slots or parameters, not mirror raw layer groups.

## Business Widget Candidates

Use this layer for product-specific constructs such as:

- order status card
- task summary row
- finance insight strip
- profile completion banner

These should stay close to domain language instead of generic visual naming.

## Page Sections

Use page sections when the repeated unit is larger than a widget:

- dashboard hero region
- pinned summary area
- tabbed content body
- form section cluster
- action footer

Do not force page sections into global reuse if they only repeat once.

## Extraction Rules

- Extract a reusable component only when it repeats or obviously will repeat.
- Prefer a small number of expressive components over many thin wrappers.
- Keep local layout private when abstraction would hide more than it clarifies.
- For every extracted component, explain its purpose, inputs or slots, and state changes.

## Anti-Patterns

- one Flutter widget per Pencil node
- components named after geometry instead of meaning
- global reuse for screen-specific one-offs
- abstractions with no stable anatomy or no reuse path
