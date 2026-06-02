# Acceptance Checklist

Review the rebuilt Pencil result against the approved preview and freeze card in this order:

1. `结构`: page framing, section ordering, negative space, alignment
2. `层级`: dominant zone, secondary zone, support zone, primary action
3. `排版`: font family, size contrast, weight rhythm, line length
4. `颜色`: background, surfaces, accents, contrast, semantic highlights
5. `系统`: reusable tokens, component-like groups, spacing rhythm, radius logic
6. `平台`: HIG-baseline safe areas, touch targets, navigation, destructive actions, permission flows, readability, feedback, accessibility
7. `资产`: illustration placement, icon clarity, crop quality, transparency edges
8. `状态`: ideal, empty, loading, error, permission, partial-data, locked, premium, or success coverage
9. `细节`: shadows, radius, texture, separators, decorative balance

## Acceptance Questions

- Does the page hierarchy match the approved preview and freeze card?
- Are any bitmap slices standing in for text, layout, or controls?
- Do icons still look crisp at the rendered size?
- Do illustrations preserve the intended role and balance?
- Are variables and repeated structures maintainable?
- Does the custom visual direction preserve HIG-baseline behavior?
- Is each remaining difference intentional and documented?
- Can Flutter implementation preserve the design without guessing?

## Closeout Format

Summarize final review as:

- `已对齐项`
- `剩余差异`
- `是否可接受`
- `下一轮动作`
