# Acceptance Checklist

Review the rebuilt Pencil result against the approved preview and freeze card in this order:

1. `structure`: page framing, section ordering, negative space, alignment
2. `hierarchy`: dominant zone, secondary zone, support zone, primary action
3. `typography`: font family, size contrast, weight rhythm, line length
4. `color`: background, surfaces, accents, contrast, semantic highlights
5. `system`: reusable tokens, spacing rhythm, radius logic, material consistency
6. `components`: non-page-level reusable components, naming, state coverage, variant boundaries, reuse decisions
7. `platform`: HIG-baseline safe areas, touch targets, navigation, destructive actions, permission flows, readability, feedback, accessibility
8. `assets`: illustration placement, icon clarity, crop quality, transparency edges
9. `states`: ideal, empty, loading, error, permission, partial-data, locked, premium, or success coverage
10. `details`: shadows, radius, texture, separators, decorative balance

## Acceptance Questions

- Does the page hierarchy match the approved preview and freeze card?
- Are any bitmap slices standing in for text, layout, or controls?
- Do icons still look crisp at the rendered size?
- Do illustrations preserve the intended role and balance?
- Are variables and repeated structures maintainable?
- Are non-page-level reusable components complete enough that Flutter does not need to invent their structure, naming, or key states?
- Does the custom visual direction preserve HIG-baseline behavior?
- Is each remaining difference intentional and documented?
- Can Flutter implementation preserve the design without guessing?

## Closeout Format

Summarize final review as:

- `aligned_items`
- `remaining_gaps`
- `ready_for_handoff`
- `next_actions`
