# Acceptance Checklist

Review the rebuilt Pencil result against the approved preview and freeze card in this order:

1. `structure`: page framing, section ordering, negative space, alignment
2. `hierarchy`: dominant zone, secondary zone, support zone, primary action
3. `typography`: font family, size contrast, weight rhythm, line length
4. `color`: background, surfaces, accents, contrast, semantic highlights
5. `cta`: primary action prominence, label clarity, contrast, and separation from secondary actions
6. `system`: reusable tokens, spacing rhythm, radius logic, material consistency
7. `components`: non-page-level reusable components, naming, state coverage, variant boundaries, reuse decisions
8. `scroll`: viewport strategy, below-the-fold ordering, fixed versus scrolling regions, sticky behavior, continuous frames or equivalent structured scroll notes
9. `platform`: HIG-baseline safe areas, touch targets, navigation, destructive actions, permission flows, readability, feedback, accessibility
10. `assets`: illustration placement, icon clarity, crop quality, transparency edges
11. `states`: ideal, empty, loading, error, permission, partial-data, locked, premium, or success coverage
12. `details`: shadows, radius, texture, separators, decorative balance

## Acceptance Questions

- Does the page hierarchy match the approved preview and freeze card?
- Is the typography ladder strong enough that the page reads clearly without decorative help?
- Is the primary CTA obvious within three seconds, and is it clearly stronger than nearby secondary actions?
- Are any bitmap slices standing in for text, layout, or controls?
- Do icons still look crisp at the rendered size?
- Do illustrations preserve the intended role and balance?
- Are variables and repeated structures maintainable?
- Are non-page-level reusable components complete enough that Flutter does not need to invent their structure, naming, or key states?
- Is the scroll structure explicit enough that Flutter does not need to guess viewport boundaries, sticky regions, or below-the-fold order?
- Does the custom visual direction preserve HIG-baseline behavior?
- Is each remaining difference intentional and documented?
- Can Flutter implementation preserve the design without guessing?

## Closeout Format

Summarize final review as:

- `aligned_items`
- `remaining_gaps`
- `ready_for_handoff`
- `next_actions`
