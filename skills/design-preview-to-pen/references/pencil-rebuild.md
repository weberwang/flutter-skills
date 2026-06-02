# Pencil Rebuild

## Preconditions

- The user has approved a preview direction.
- The design freeze card exists.
- The asset plan exists.
- The Pencil desktop app is running and connected to MCP.

## Mandatory Tool Sequence

1. `pencil.get_editor_state(include_schema: true)`
2. `pencil.get_guidelines(...)` when a guide or style is needed
3. `pencil.set_variables(...)` for tokens
4. `pencil.batch_design(...)` for section construction
5. `pencil.snapshot_layout(...)` for structural review
6. `pencil.get_screenshot(...)` for visual comparison
7. `pencil.export_nodes(...)` for external review artifacts when needed

## Rebuild Order

Use this order to preserve editability:

1. root frame and page bounds
2. spacing, color, typography, radius, shadow, and border variables
3. major sections and containers
4. headings, body text, controls, cards, and navigation
5. icons and illustrations
6. decorative accents and polish
7. redline notes for Flutter handoff

## Designer Reconstruction Rules

- Use variables before large section passes so tokens stay consistent.
- Name sections by their product role, not just visual shape.
- Preserve the dominant, secondary, and support zones from the approved direction.
- Keep text and controls editable unless the freeze card explicitly permits rasterization.
- Translate preview-only artifacts into maintainable Pencil structure.
- Preserve HIG-baseline safe areas, tap targets, navigation behavior, readability, feedback, and accessibility.

## Recovery Rule

If `get_editor_state(include_schema: true)` fails because the desktop app is disconnected:

- stop before any Pencil write operation
- report the blocker clearly
- keep the workflow at the prepared state: approved preview, design freeze card, asset manifest, and rebuild plan

## Rebuild Principle

The target is not "same pixels by any means." The target is "same approved direction with maintainable Pencil structure."
