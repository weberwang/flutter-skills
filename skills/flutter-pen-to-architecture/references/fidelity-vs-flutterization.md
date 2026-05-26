# Fidelity Versus Flutterization

## Goal

Explain which parts of a Pencil design should be restored closely and which should be adapted to Flutter-native structure for maintainability and semantic clarity.

## Decision Classes

Always classify meaningful decisions into one of these buckets:

- `建议高保真还原`
- `建议 Flutter 化重构`
- `建议简化处理`

## 建议高保真还原

Use this when the design detail carries:

- brand identity
- hierarchy that users rely on
- strong product differentiation
- interaction posture that would materially change if simplified

Examples:

- signature card proportions
- branded accent usage
- distinct chip or tab anatomy
- critical dashboard hierarchy

## 建议 Flutter 化重构

Use this when the design intent matters more than the exact layer structure.

Typical cases:

- deeply nested layout stacks that can become cleaner shell-region structures
- repeated style variants that should become theme tokens
- ad hoc repeated groups that should become configurable widgets
- spacing or typography values that should be normalized

## 建议简化处理

Use this when the cost of literal recreation outweighs the product value.

Typical cases:

- decorative shadows with no semantic role
- noisy micro-differences between nearly identical cards
- visual flourishes that complicate accessibility or maintenance
- one-off geometry tricks that do not affect understanding

## Decision Rules

- Preserve meaning before preserving pixels.
- Preserve interaction posture before decorative detail.
- Prefer a stable theme or component contract over repeated local exceptions.
- If simplification changes user understanding, it is not simplification anymore and should move to another class.

## Output Expectations

For every classified item, explain:

- what the original design is doing
- why the chosen class fits
- what the Flutter-facing landing should be
- what risk is introduced by the decision
