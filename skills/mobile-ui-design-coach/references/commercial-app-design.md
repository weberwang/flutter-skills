# Commercial App Design

## Use This File For

- turning "商业级", premium, production-ready, or less template-like requests into concrete design work
- preventing the common failure where an app screen becomes prettier but not more usable, sellable, or buildable
- preparing an upstream packet for preview generation, Pencil rebuild, or Flutter implementation

## Commercial Definition

A commercial-grade mobile app design must be:

- `sellable`: the value proposition and business moment are visible without feeling like an ad
- `usable`: the primary path is obvious, thumb-safe, and glanceable
- `complete`: important states are designed, not left to engineering guesses
- `systematic`: typography, spacing, color, surfaces, icons, and motion behave as a coherent system
- `buildable`: the design can become components, tokens, assets, and acceptance checks
- `distinctive`: one memorable visual idea makes the product feel specific without harming task clarity
- `platform-safe`: HIG-baseline behavior is preserved for safe areas, touch targets, navigation, feedback, and accessibility

## Pressure Scenarios This Prevents

- User asks for "commercial polish"; the agent only adds gradients, glass, shadows, or hero art.
- User asks for an app flow; the agent designs only a perfect home screen and ignores empty, loading, error, permission, or paid states.
- User asks for a Pencil or Flutter handoff; the agent gives a mood description without hierarchy, tokens, state map, or implementation guardrails.
- User asks for premium quality; the agent copies web dashboard density into a phone screen.
- User asks for a designer-grade direction; the agent jumps directly to prompts without a brief, critique, or art direction.

## Designer Production Flow

Use this flow before preview generation, Pencil rebuild, or Flutter implementation:

1. `设计简报`: audience, usage moment, product promise, business goal, page scope, hard constraints
2. `平台基线`: default to HIG behavior rules unless the user explicitly chooses another platform baseline
3. `设计诊断`: native-feel symptoms, template signals, missing hierarchy, missing states, weak brand memory
4. `艺术指导`: posture, density, temperature, material language, type personality, icon and illustration posture
5. `移动骨架`: first impression, primary action, result feedback, next best action, return loop, boundary states
6. `视觉系统`: typography, spacing, color roles, surfaces, radii, borders, icons, motion
7. `状态矩阵`: production states and which states must be designed now
8. `冻结卡`: what must stay identical, what may be engineered, and what must be checked later

Do not let a prompt, preview image, or Flutter component decide these items implicitly.

## Commercial Flow

### 1. Product Promise

Lock the commercial purpose before visual styling:

- `目标用户`: who is using this and in what moment
- `核心任务`: what the user must accomplish
- `价值瞬间`: when the user feels the app is worth keeping or paying for
- `业务目标`: activation, retention, subscription, habit, trust, conversion, or referral
- `品牌姿态`: serious, calm, expressive, expert, companion-like, or lifestyle-led

### 2. Core Path

Define the path before polishing screens:

- first impression
- primary action
- feedback or result
- next best action
- return loop
- paid, permission, or account boundary when relevant

### 3. Information Hierarchy

Every key screen needs:

- one dominant zone
- one secondary zone
- one support zone
- one clear primary action
- secondary actions that do not compete with the primary action
- navigation that stays useful but visually quieter than the task

### 4. State Map

Production design must name the important states:

- ideal state
- empty state
- loading state
- error state
- permission or authorization state
- partial-data state
- disabled or unavailable state
- success or completion state
- premium, locked, or upgrade state when monetization exists

### 5. Visual System

Specify the system, not just the mood:

- typography scale and contrast
- spacing rhythm and density
- surface model: flat, layered, carded, editorial, or workspace-like
- color roles: background, surface, text, accent, semantic, warning, success
- corner radius and border logic
- icon and illustration posture
- motion role: feedback, reveal, transition, or attention

### 6. Designer Critique

Before recommending a direction, critique it like a designer:

- `focal intent`: what the eye sees first and why
- `composition balance`: whether the page has a clear dominant, secondary, and support zone
- `brand memory`: what makes this product recognizable after the user leaves
- `affordance`: whether controls still look tappable and stateful
- `content truth`: whether real copy, realistic numbers, and edge states expose layout stress
- `handoff clarity`: whether Pencil or Flutter can preserve the decision without guessing

### 7. Commercial Polish Levers

Choose one or two primary levers:

- `hierarchy`: stronger focal zones, clearer grouping, more intentional rhythm
- `material`: subtle layers, surface contrast, borders, or depth
- `content realism`: real copy, realistic data, sharper empty states
- `brand memory`: distinctive typography, motif, illustration, or shape language
- `state clarity`: polished feedback, errors, permissions, and paywalls
- `motion`: restrained transitions that explain state changes

## Quality Gates

Before calling a design commercial-grade, verify:

- The primary task is understandable within three seconds.
- The business or retention moment is visible but not intrusive.
- The screen does not look like a default iOS or Android settings page.
- The design covers more than the happy path when the feature is production-facing.
- Realistic content replaces lorem ipsum and fake placeholder numbers.
- Components can be reused across adjacent screens.
- Typography, spacing, surfaces, and action hierarchy are consistent.
- Thumb reach, tap target size, and scanning speed are preserved.
- Decorative elements have a job: hierarchy, brand memory, warmth, or state feedback.
- A developer or Pencil rebuild can preserve the design without guessing.
- The design includes a freeze card before production work starts.
- The art direction has a purpose beyond looking trendy.
- HIG-baseline behavior remains intact even when the visual surface becomes custom.

## Design Freeze Card

Return this packet when the user asks for commercial-grade app design or when another skill needs a frozen upstream direction:

- `设计简报`: audience, usage moment, page scope, constraints
- `平台基线`: HIG by default; name any explicit alternative only when the user requires it
- `商业目标`: activation, retention, conversion, trust, habit, or another explicit goal
- `目标用户与场景`: who, when, and why
- `核心路径`: first impression, primary action, result, next best action, return loop
- `页面范围`: screen, section, flow, or full feature
- `艺术指导`: posture, density, temperature, de-native strategy, brand memory, polish lever
- `信息层级`: dominant zone, secondary zone, support zone, primary action
- `视觉系统`: type, spacing, color roles, surfaces, radius, icons, motion
- `状态矩阵`: required states and which ones must be designed now
- `商业化触点`: subscription, upgrade, reminder, sharing, account, or trust moment when relevant
- `必须一致项`: hierarchy, proportions, key copy, colors, assets, motion, or other items that must survive later stages
- `允许工程化调整项`: where Pencil or Flutter may simplify without breaking the direction
- `平台不可偏离项`: safe area, tap target, navigation, destructive action, permission, feedback, readability, accessibility
- `Prompt 约束`: master prompt inputs and negative constraints
- `交付验收门`: what must be checked before preview, Pencil, or Flutter work continues

## Handoff To Preview Or Pencil

When used with `design-preview-to-pen`, stop after the design freeze card unless the user explicitly asks to generate preview images. The card becomes the frozen input for preview prompts, asset planning, Pencil parity review, and Flutter handoff.
