# Design Subagent Orchestration

Use this contract whenever subagent tools are available. The controller orchestrates; specialized subagents perform design production and evidence work.

## Controller-Only Authority

The controller must retain:

- user questions and confirmation requests;
- scope, priority, cost, risk, and acceptance decisions;
- candidate presentation and user-choice recording;
- global direction, page design, and pre-slicing confirmation gates;
- freeze, unfreeze, and final artifact acceptance;
- cross-agent conflict resolution, sequencing, ledger state, and final integration.

No subagent may select its own proposal, infer user approval, freeze a design, broaden scope, or continue past a missing confirmation.

## Required Design Roles

| Role | Performs | May write | Must not do |
|---|---|---|---|
| Product/UX agent | Draft product, flow, state, and screen artifacts from confirmed decisions | Assigned product/design artifact paths | Ask or answer decision questions |
| Market agent | Produce market and category analysis | `market-analysis.md` | Select a visual direction |
| Global direction agent | Produce exactly three traceable visual-system definitions | Transient response or assigned draft | Generate page images or freeze a direction |
| Global direction reviewer | Independently check traceability, differentiation, accessibility, cost, and preset compliance | Review report only | Redesign or select |
| Page structure agent | Select Full, Lightweight, or Reuse and create the semantic contract; create Pencil evidence only for Full | Assigned page-scoped Pencil/spec paths | Add scope, freeze visual geometry, or add high-fidelity styling |
| Wireframe reviewer | Independently review level choice, semantic coverage, states, and interaction | Review report only | Modify the contract or judge low-fidelity visual polish |
| Page high-fidelity agent | Generate required candidates with the compact image-prompt principles | Transient candidates only | Paste planning evidence into prompts; persist, select, or freeze candidates |
| Effect Image Reviewer | Independently review completed candidates | Review report only | Modify or select a candidate |
| Bitmap decomposition agent | Perform ownership classification, visual sweep, and coverage audit | Assigned restoration-analysis path | Generate or cut assets |
| Asset planning agent | Perform reuse checks and prepare the complete pre-slicing confirmation table | Assigned asset-atlas draft | Produce assets before confirmation |
| Asset production agent | Generate with compact prompts, adapt, extract, transparentize, export, and slice confirmed rows | Confirmed asset paths and manifests | Paste planning evidence into prompts, change confirmed rows, or create unconfirmed assets |
| Pencil restoration agent | Restore the frozen page and write Flutter handoff | Assigned Pencil/restoration paths | Change the frozen design |
| Visual QA agent | Compare implementation evidence with approved design | Review report only | Self-approve implementation |

## Dispatch Sequence

```text
confirmed product decisions
→ Product/UX agent + Market agent
→ Global direction agent
→ Global direction reviewer
→ controller presents and freezes user selection
→ Page structure agent
→ Wireframe reviewer
→ Page high-fidelity agent
→ Effect Image Reviewer
→ controller presents and freezes user selection
→ Bitmap decomposition agent
→ Asset planning agent
→ controller presents pre-slicing table and waits
→ Asset production agent
→ Pencil restoration agent when required
→ Implementer
→ Visual QA agent
```

## Dispatch Rules

- Give each agent one role, exact inputs, exact output shape, write scope, non-scope, and blocking conditions.
- Keep producer and reviewer roles on different agents.
- Require `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`; the controller validates the result before advancing.
- Never let concurrent agents write the same artifact, Pencil frame, asset path, design freeze, ledger entry, theme, navigation, or shared configuration.
- Parallelize only read-only research/review or independent page/asset scopes after their shared freeze exists.
- When subagents are unavailable, execute the same roles sequentially in the controller session and record the downgrade; do not silently collapse the role boundaries.
