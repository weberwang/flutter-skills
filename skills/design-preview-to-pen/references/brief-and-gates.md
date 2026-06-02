# Brief And Gates

## Brief Contract

Lock these fields before image generation:

- `设计目标`: what the screen, flow, poster, or panel must communicate
- `平台基线`: HIG by default for mobile behavior unless the user explicitly chooses another baseline
- `页面范围`: one page, one section, one card, or a full flow
- `目标平台`: mobile, desktop, poster, splash, or marketing panel
- `目标用户与场景`: who sees it, when, and why it matters
- `商业目标`: activation, retention, trust, conversion, habit, or other measurable intent
- `艺术指导`: layout posture, density, palette, material language, type personality, icon posture, illustration posture
- `状态范围`: ideal, empty, loading, error, permission, partial-data, locked, premium, or success states
- `品牌约束`: palette, logo, forbidden colors, forbidden motifs, or existing component language
- `禁止项`: visual tropes, competitors, effects, or layout patterns to avoid
- `验收标准`: what must look right for the user to approve

## Designer Discovery Questions

Ask only what is necessary to reduce ambiguity:

1. What is the primary job of this preview?
2. Should HIG remain the behavior baseline, or is there an explicit alternative?
3. What must be preserved exactly in the final Pencil rebuild?
4. What can be cleaned up during structured reconstruction?
5. Which state or edge case must be represented now?
6. Are icons allowed to be redrawn?
7. Should illustrations be regenerated as independent transparent assets?
8. Is the target exact restoration or structured restoration with minor engineering cleanup?

## Approval Gates

Never cross these gates silently:

1. `需求门`: brief is clear enough to generate preview options
2. `方向门`: one preview direction is explicitly approved
3. `冻结门`: must-match items and allowed adjustments are recorded
4. `素材门`: the asset strategy is accepted
5. `Pencil 门`: the app is connected and schema is available
6. `验收门`: the rebuilt result is compared against the approved preview and freeze card

## Design Freeze Card Template

Use this record after approval:

- `采用版本`:
- `必须一致项`:
- `允许工程化调整项`:
- `平台不可偏离项`:
- `图标处理策略`:
- `插图处理策略`:
- `状态范围`:
- `是否允许局部重构`:
- `验收标准`:
- `备注`:

## Gate Failure Rule

If a gate is missing, stop at that phase and ask for the smallest decision needed. Do not continue by assuming approval.
