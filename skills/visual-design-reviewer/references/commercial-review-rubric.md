# Commercial Review Rubric

Score the design out of 100 using these weighted categories.

## 1. Information Hierarchy And Scan Order — 25

Judge:

- whether the dominant zone is correct for the user’s current moment
- whether the screen makes the first, second, and third reading targets obvious
- whether supporting information stays subordinate to the main job

Critical failures:

- the eye does not know where to land first
- multiple areas compete as if they are equally important
- the screen requires manual interpretation before the user can orient

## 2. Key Task Guidance And Primary Path — 25

Judge:

- whether the primary task is obvious within three seconds
- whether the next best action is explicit after the user reads the main content
- whether the page leads the user toward completion instead of only presenting content

Critical failures:

- the user can see content but not what to do next
- the primary task path is buried under secondary actions or passive information
- the design looks polished but does not guide the user toward completion

## 3. Typography Hierarchy — 15

Judge:

- whether the user can tell what to read first, second, and third
- whether sizes, weights, spacing, and grouping create a clear reading ladder
- whether the page feels premium through structure rather than noise

Critical failures:

- every text block looks equally important
- headings, metadata, and body copy collapse into one flat layer
- the draft depends on decoration because typography is not carrying hierarchy

## 4. Contrast And Legibility — 15

Judge:

- text against background and surfaces
- CTA against adjacent controls
- whether contrast is strong enough for speed, trust, and production use

Critical failures:

- body text is too low-contrast to scan quickly
- primary CTA does not stand apart from secondary actions
- subtle styling reduces clarity instead of improving it

## 5. CTA And Conversion Focus — 10

Judge:

- whether the primary CTA is obvious within three seconds
- whether the CTA label, placement, and weight match the business moment
- whether supporting actions stay visibly subordinate

Critical failures:

- multiple actions compete at the same visual weight
- the user cannot tell what action matters most
- the design looks polished but does not help the user commit

## 6. System Consistency And Polish — 5

Judge:

- spacing rhythm and grouping
- surfaces, borders, radii, and icon posture
- whether the page feels like part of a system rather than a lucky one-off

Critical failures:

- polish is inconsistent across sections
- local styling decisions fight the larger system
- the page looks manually arranged instead of intentionally systemized

## 7. State Completeness And Handoff Readiness — 5

Judge:

- whether important states are represented or clearly specified
- whether Flutter or Pencil can rebuild the result without guessing
- whether the design packet exposes edge cases instead of hiding them

Critical failures:

- only the happy path exists
- the draft cannot be handed off without inventing states or component behavior
- the design packet hides real constraints behind placeholder content

## Score Bands

- `90-100`: excellent commercial draft
- `<90`: not freeze-ready and must take exactly one scope-matched revision pass, then stop without another review in the same cycle

## Review Language

Always write:

- `strengths`: what is already working
- `weaknesses`: what is visibly weak now
- `risks`: what could break downstream freeze or implementation
- `recommended_fixes`: the smallest changes that would most improve quality
- `revision_required`: whether the draft must take a scope-matched revision pass
- `revision_scope`: `shared_single_revision` or `module_single_revision`
- `revision_limit`: `one_pass_only` when revision is required
- `post_revision_policy`: `stop_no_re_review` when revision is required

Be specific about typography hierarchy, contrast, and CTA before discussing decorative polish.
Be even more specific about information hierarchy and key-task guidance before discussing visual polish.
For freeze-facing reviews, a score below `90` is an automatic fail even if the design looks close.
Choose the revision scope by scope:

- `shared_single_revision`: for global/shared drafts before `modules_split`
- `module_single_revision`: for active-module drafts during implementation preparation, where the current module `ui/ux` doc is adjusted and the current module design draft is modified in Pen once
