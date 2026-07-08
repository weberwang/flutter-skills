# Design Quality Guidance

Use this reference when the workflow is defining global visual direction, writing `DESIGN.md`, generating tool-selected design sources, or evaluating whether a design is strong enough to freeze.

## Core Principle

Design quality does not start from decoration. It starts from helping the user complete the right task with the least confusion.

Always optimize in this order:

1. user intent
2. task clarity
3. content structure
4. interaction feedback
5. visual polish

A design may look impressive and still be weak if the main task is hard to find, hard to understand, or hard to complete.

## 1. Start From User Intent

Before choosing layout, style, or animation, answer:

- What is the user's main goal on this screen?
- What is the primary action?
- What information must be visible immediately?
- What can be delayed, collapsed, paged, or hidden behind interaction?

Do not begin from:

- icon style
- hero art
- decorative backgrounds
- novelty layouts

Those are secondary decisions.

## 2. Treat Design As Guided Storytelling

Think of each screen as a guided story:

- where the eye lands first
- what the user understands in the first 3 seconds
- what action the interface invites next
- how the system reduces uncertainty before the user commits

The main CTA should not compete with decorative elements, secondary metadata, or unrelated promotions.

## 3. Respect Familiar Layout Expectations

Users already carry strong mental models.

Default expectations usually include:

- information flows top to bottom
- scanning tends to move left to right
- navigation is easy to locate
- important actions are prominent and predictable

You may break conventions intentionally, but only when the user outcome is clearly better, not just because the layout looks novel.

## 4. Design Around Real Content

Content quality determines design quality.

Always design for:

- long titles
- short titles
- missing thumbnails
- bright and low-contrast imagery
- dense metadata
- empty lists
- error messages

Do not evaluate only with ideal placeholder content.

When content becomes long or noisy:

- truncate intentionally
- preserve critical metadata
- protect contrast
- simplify surrounding chrome

## 5. Expand Function Only When Intent Expands

Do not add filters, panels, cards, or actions just because there is room.

Expand functionality only when the user's intent becomes broader:

- direct search intent -> show search first
- browsing intent -> add discovery or filtering
- comparison intent -> surface scan-friendly attributes
- editing intent -> reveal editing tools in context

This keeps the interface purposeful instead of cluttered.

## 5A. Commercial Product Copy Compression

Commercial product surfaces should communicate through recognition before explanation.

Prefer:

- recognition over explanation
- visual state over descriptive paragraphs
- progressive disclosure over always-visible explanation
- compact status language over support-copy blocks

When a screen feels clear only after reading, treat that as a design defect rather than a harmless copy choice.

On the first screenful of a product page, keep only:

- the main task
- the current state
- the next action
- the minimum context required to act safely

Push broad education, repeated explanation, and policy-style detail behind disclosure or onto secondary surfaces whenever the user can already understand the screen from structure and state.

## 5B. Commercial Product Image Constraint

When a workflow step generates preview images, page-sketch drafts, or final effect images for product surfaces, the target must remain a commercial product interface.

Treat these as required visual qualities:

- real app-screen hierarchy
- believable control density
- actionable primary CTA placement
- production-grade component rhythm
- realistic product-state structure
- product-task clarity before visual spectacle

Treat these as disallowed failure modes unless the workflow has explicitly switched into a marketing or asset branch:

- poster composition
- ad creative framing
- landing-page hero styling
- slogan-first layout
- mood-board composition
- concept-art treatment
- flighty concept mock treatment
- wireframe-like draft output
- explanatory requirements mock styling

If an image feels impressive but the user cannot imagine shipping it as an actual app screen, the image is off-target.
If an image feels flashy before it feels shippable as a product screen, reject it.
visual experience must still serve product-task clarity.

## 5C. Commercial Trust And Premium Confidence

High-commercial-value product surfaces must create confidence before they ask for effort, data, money, or commitment.

Design for trust through concrete product signals such as:

- clear current status
- believable data freshness
- visible safety or permission posture
- outcome confidence cues
- pricing or subscription clarity when relevant
- identity and ownership cues when the surface involves account, payment, security, or creator value

Do not confuse trust with explanation density.

If a product only feels safe after reading multiple paragraphs, the trust design is weak. Prefer:

- short confidence labels
- visible system state
- recognizable controls
- stable hierarchy
- credible empty, loading, and error behavior

Premium quality on a commercial surface should feel:

- restrained rather than loud
- precise rather than decorative
- trustworthy rather than theatrical
- dense enough to feel real, but never cluttered

If "premium" depends mainly on oversized art direction, dramatic negative space, or slogan-led composition, the result is usually drifting toward marketing instead of product.

## 5D. Reference Inheritance Discipline

Commercial quality improves when references are treated as explicit decisions, not vague mood.

When the workflow uses Mobbin or other mature-product references:

- bind `2-3` references that match the target market band
- state what is intentionally inherited from each one
- keep those inherited choices concrete

Useful inherited categories include:

- hierarchy posture
- information density
- CTA treatment
- trust-signal placement
- copy compression
- card rhythm
- navigation or shell posture

Avoid statements such as "inspired by modern fintech apps" without naming which decisions were actually carried forward.

## 5E. Brand Visual World Extraction

When the user provides a high-quality brand or visual prompt, extract the reusable common layer before sending anything downstream.

Keep the extracted packet project-agnostic first, then bind project-specific nouns such as company name, logo subject, mascot subject, hero object, or campaign title later.

For premium-but-playful brand systems, capture the core tension explicitly:

- playful energy and premium creative-tech polish
- approachable_but_art_directed

Prefer reusable brand-language primitives such as:

- high-saturation bright color
- clean geometric form
- modern typography system
- dynamic visual rhythm
- light surreal image posture

When the prompt points to a broader brand world, preserve cross-surface world-building goals rather than only local screen styling:

- product obsession
- visual experimentation
- packaging exploration
- editorial photography
- immersive retail
- cross-platform brand application

Do not copy project-private nouns into the reusable layer unless they are required downstream as explicit placeholders.
Do not let one good prompt collapse into one aesthetic adjective. Extract the tension, visual language, world-building surfaces, and avoid-list separately so later workflow steps can reuse them without restating the whole prompt.

## 6. Mobile UI Is Not A Shrunk Desktop UI

Mobile requires re-composition, not compression.

Before the global design direction is explored, freeze one base mobile viewport for the whole design cycle. Do not let page ideation, effect-image generation, or downstream design-source work switch widths opportunistically from page to page.

Do not design any page at a width or height smaller than the frozen base design viewport for the active design cycle. For effect-image generation, keep the frozen width fixed and treat the frozen viewport height as the minimum logical canvas height. Always carry the frozen `image_output_scale` separately so the final workflow output size is derived from the logical viewport instead of reusing viewport pixels as generated image pixels. If a page or region is intentionally scrollable, extend the design vertically as needed instead of shrinking the width or compressing the layout to avoid extra height. If content does not fit, solve it through hierarchy, disclosure, paging, or layout restructuring rather than shrinking the page below the frozen design size.

For iPhone-first product work, offer at least these common presets unless the user already chose another target:

- `375 x 667 px` for compact iPhone baseline
- `390 x 844 px` for standard iPhone baseline
- `393 x 852 px` for Pro baseline
- `430 x 932 px` for Pro Max baseline

If the run is `--auto` and no viewport has been frozen yet, default to `390 x 844 px`.

### Navigation

- Bottom navigation works well when the app has a few primary destinations.
- Keep primary nav count lean. Fewer than five is healthier than five.
- Touch targets must be comfortably tappable.
- Actions can change by page context.

If there are too many destinations, use a dedicated navigation page or alternate top-level structure instead of overloading a bottom bar.

### Scale

Do not assume smaller screens need smaller typography.

On mobile:

- typography often stays similar to desktop or grows larger
- spacing still needs breathing room
- dense layouts quickly become fragile
- leave enough whitespace and structural gaps so the screen can breathe at the frozen design size

### Layout Direction

A mobile section should usually move in one dominant direction:

- vertical stack
- or horizontal rail

Avoid trying to preserve multi-axis dashboard thinking on every screen.

## 7. One Screen, One Primary Job

Outside of special hub or home surfaces, a screen should mainly do one thing.

Examples:

- settings screen -> settings
- detail screen -> detail
- editor screen -> editing

When new needs appear, prefer:

- a new page
- a bottom sheet
- a modal flow
- a contextual panel

Do not keep injecting unrelated content into the current screen.

## 8. Use Cards Carefully

Cards are valuable because they group information in constrained spaces, especially on mobile.

But avoid card-over-card nesting when possible.

Why:

- it creates padding on padding
- reduces usable space
- makes layouts feel cramped
- weakens hierarchy

Prefer grouping with whitespace first, then containers only where semantic separation is needed.

## 9. Progressive Disclosure Beats Constant Exposure

Show the user what they need now, then reveal more when required.

Good uses:

- expanding search bars
- collapsible filters
- contextual menus
- bottom sheets
- load-more interactions

Progressive disclosure is especially useful when:

- screen space is limited
- the task has multiple levels of detail
- exposing everything at once would reduce clarity

## 10. Motion Must Add Meaning

Animation should add one or more of:

- clarity
- continuity
- hierarchy
- feedback
- delight without confusion

Good motion examples:

- menu revealing hidden navigation
- sheet preserving context while opening secondary actions
- shrinking search field that stays accessible while browsing
- subtle button feedback that confirms tap readiness

Use motion sparingly when it:

- blocks reading
- delays action
- distracts from the primary path
- imitates complexity without adding understanding

## 11. Gestures Must Preserve Context

Mobile gestures are powerful when they reduce navigation cost without hiding core meaning.

Useful patterns:

- swipe to go back
- swipe to search
- swipeable contextual actions
- long press for secondary actions
- bottom sheet drag interactions

If gestures are essential:

- ensure discoverability
- give feedback
- avoid making core actions gesture-only when visibility matters

## 12. Empty States Are Part Of The Design

There are at least two important empty states:

- first-use empty state
- no-results / exhausted-data state

Good empty states do one or more of:

- reassure the user
- explain the situation
- suggest next actions
- keep the main task alive

Do not leave empty states as blank containers with placeholder text.

## 13. Feedback Consistency Matters More Than Flair

The user should feel the system behaves predictably in:

- hover
- press
- focus
- loading
- success
- warning
- error
- disabled
- permission denied

If the visual language for these states changes randomly between pages, the experience feels lower quality even if the screens are individually attractive.

## 14. Design Systems Are A Shared Language

A good design system is not about making every screen identical.

It is about giving the team:

- shared tokens
- shared components
- shared spacing rules
- shared interaction patterns
- shared naming
- shared decisions about when to bend the rules

System quality comes from clarity plus intentional exceptions.

## 15. Practical Quality Checklist

Before freezing a design, confirm:

- The main task is obvious quickly.
- The primary CTA is visible or easily discoverable.
- The content hierarchy survives with realistic data.
- The shell stays consistent across screens.
- Shared components stay recognizable across screens.
- States are intentionally designed, not implied.
- Motion supports understanding.
- Responsive behavior does not create a second visual language.
- Copy tone fits both ideal flow and recovery flow.
- Visual polish does not undermine usability.

## 16. Platform-Aware Premium Quality

High-quality design in this workflow must be both platform-aware and premium by default when the module or product positioning expects a high-confidence feel.

Platform-aware means:

- navigation matches the real target surface
- safe areas, touch targets, hover, focus, gestures, and density fit the target platform
- interaction feedback feels native enough for the target validation surface

Platform-aware information density means:

- phone surfaces expose only the primary task, key status, and essential metadata immediately; secondary tools, diagnostics, and long-tail attributes should move below the fold, behind disclosure, or onto a follow-up surface
- tablet surfaces may add a secondary pane or broader comparison context when it still supports the same primary task instead of competing with it
- desktop or large-screen surfaces may raise scanning and comparison density, but they must not fill empty space with low-value chrome, duplicate cards, or competing CTAs
- no surface should be judged by raw item count alone; density is correct only when the user can still identify the primary job, the current state, and the next action quickly

Premium means:

- hierarchy is crisp and immediate
- spacing feels intentional rather than compressed
- typography carries confidence and restraint
- contrast is controlled, not muddy
- CTA dominance is obvious without shouting
- depth, texture, and polish support clarity instead of distracting from it
- trust signals appear where the product class needs reassurance
- the surface can stand beside mature category references without looking like a concept mock

Do not confuse premium quality with ornament. Premium quality fails if the result is attractive but unclear, fragile under real content, or mismatched to the target platform.

## 17. How To Apply This In This Workflow

When brainstorming global visual direction:

- begin from task intent and shell logic
- not from styling first

When writing `DESIGN.md`:

- encode task hierarchy
- encode CTA posture
- encode state behavior
- encode responsive behavior
- encode content tone

When generating downstream structured design source:

- use the frozen global design, the active module design package, and `DESIGN.md` as the only design-guidance inputs
- preserve shared style direction
- preserve shared theme system
- preserve shared shell
- preserve shared component families
- preserve task and feedback logic

When freezing:

- reject designs that are attractive but weak in task clarity
- reject designs that only work in ideal content states
- reject designs that break under mobile constraints or multi-device adaptation
- reject module designs that have not yet been tested conceptually against the explicit target platform and premium quality bar
- reject module designs whose first-screen information density is still unresolved for the target platform, whether that means overstuffed content, under-specified content, or unclear disclosure boundaries
