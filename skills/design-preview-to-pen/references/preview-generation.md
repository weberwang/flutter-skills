# Preview Generation

## Tool Policy

- Use `$gpt-image-2-generator` for every generated preview comp.
- Keep preview generation pinned to `gpt-image-2` through `$gpt-image-2-generator`; do not route preview creation through a generic image tool or substitute another model.
- If `$gpt-image-2-generator` cannot confirm `gpt-image-2`, or its required environment is unavailable, stop before generation and report the blocker instead of substituting another model.
- Generate one to three options in a round.
- Change one major design variable per round.
- Keep each round labeled clearly: `preview-v1`, `preview-v2`, `preview-v3`.
- Treat previews as design conversation artifacts, not final production assets.

## Prompt Scaffold

Structure prompts in this order:

1. `Use case`
2. `Approved brief`
3. `Platform baseline`
4. `Asset type`
5. `Primary request`
6. `Subject`
7. `Art direction`
8. `Composition and framing`
9. `Color palette`
10. `Typography or text rules`
11. `State or content coverage`
12. `Constraints`
13. `Avoid`

## Direction Strategy

- If the user is choosing a direction, maximize contrast between options.
- If the user is refining one direction, keep the layout stable and change one detail.
- If text fidelity matters, keep text sparse in the preview and rebuild final copy in Pencil.
- If transparency is needed later, note that during freeze and generate isolated assets separately instead of expecting the preview to serve as the final transparent source.
- If commercial quality matters, include realistic content, edge states, and a visible business or retention moment.
- If the preview becomes visually ambitious, explicitly keep HIG-baseline behavior for safe areas, tap targets, navigation, feedback, readability, and accessibility.

## Designer Critique After Each Round

Summarize each option with:

- `保留价值`: what direction or motif is worth keeping
- `主要风险`: hierarchy, usability, brand fit, state coverage, or buildability concern
- `与简报差异`: where it diverges from the approved brief
- `平台风险`: whether the preview violates HIG-baseline behavior
- `推荐动作`: choose, merge, revise, or reject

## Output Summary

After every generation round, summarize:

- what changed
- what stayed fixed
- which option is recommended
- what decision is needed from the user
