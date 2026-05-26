# Screen Architecture Planning

## Goal

Map multi-screen Pencil designs into Flutter screen architecture that is organized by product flow and layout responsibility rather than raw design-tool nesting.

## First Pass

Before looking at individual screens in detail, identify:

- root shells
- navigation families
- repeated headers or toolbars
- list-detail or tab-switching patterns
- global overlays and modal behavior

## Architecture Units

Prefer describing screens through these units:

- app shell
- page shell
- content region
- persistent action region
- transient state region
- overlay layer

## Common Flow Patterns

### Dashboard Or Summary Flows

Look for:

- shared top shell
- stacked insight regions
- pinned actions
- scannable summary rhythm

### List And Detail Flows

Look for:

- filter or sort layer
- grouped list item families
- inline actions versus drill-down actions
- empty, loading, and error placements

### Form Flows

Look for:

- section grouping
- validation surfaces
- confirmation layers
- sticky submission regions

## State Regions

Always account for:

- loading
- empty
- error
- partial content
- blocking overlay

If the design omits them, call that out instead of pretending they are resolved.

## Flutter-Facing Guidance

- Describe structure in terms of shells and regions, not absolute alignment math.
- Note which parts belong to shared layout scaffolds versus feature pages.
- Call out where slivers, tabs, nested scroll, bottom sheets, or dialogs may be appropriate, but do not jump into code.

## Output Expectations

For each major page or page family, summarize:

- structural role in the product
- shell dependencies
- key reusable regions
- special state handling
- risk points
