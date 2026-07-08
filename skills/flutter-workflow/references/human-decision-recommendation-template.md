# Human Decision Recommendation Package Template

Use this reference when `flutter-workflow` reaches a point where human approval is still required, but the workflow should reduce confirmation churn by giving the human a constrained, recommended option set instead of a blank question.

This is an outward-facing design artifact.
It exists to support human decisions, not to store runtime execution state.

## Purpose

The package should answer:

- what exactly must be decided by a human
- why automation cannot safely finalize it alone
- which 2-3 options are worth considering
- which option is the default recommendation
- what tradeoff the team accepts by choosing each option

## Output Language

When instantiated for a real project, all human-readable content in this artifact must default to Simplified Chinese unless the user explicitly requests another language.

## When To Use

Use this package for decisions such as:

- final style direction
- reference band selection
- commercial confidence vs expressive experimentation tradeoff
- `flutter_native` vs atlas-backed restoration choice when both are plausible
- brand-forward vs efficiency-forward first-screen posture

Do not use it for deterministic routing decisions that the orchestrator can prove automatically.

## Required Fields

Keep these fields visible in the final human-facing artifact:

- `decision_topic`
- `why_human_confirmation_is_required`
- `default_recommendation`
- `human_action_required`

For each recommended option, include:

- `id`
- `title`
- `summary`
- `fit_reason`
- `risks`
- `implementation_cost`
- `recommendation_strength`

## Recommendation Rules

- Always provide 2-3 options unless there is only one supported route left.
- Mark the strongest option as the default recommendation.
- State why the recommended option fits the current PRD and design constraint package.
- Keep risk statements concrete.
- Do not present options that are already blocked by workflow rules.
- Do not ask the human to write their own style direction from scratch.

## Template

```md
# Human Decision Recommendation Package

## Decision Topic
- decision_topic:
- why_human_confirmation_is_required:

## Default Recommendation
- default_recommendation:
- why_this_is_the_default:
- cost_of_not_choosing_default:

## Recommended Options

### Option A
- id:
- title:
- summary:
- fit_reason:
- expected_visual_result:
- expected_experience_gain:
- risks:
- implementation_cost:
- recommendation_strength:

### Option B
- id:
- title:
- summary:
- fit_reason:
- expected_visual_result:
- expected_experience_gain:
- risks:
- implementation_cost:
- recommendation_strength:

### Option C
- id:
- title:
- summary:
- fit_reason:
- expected_visual_result:
- expected_experience_gain:
- risks:
- implementation_cost:
- recommendation_strength:

## Human Action Required
- human_action_required:
- confirm_one_option_or_merge:
- hard_no_go_visuals:
- cost_tolerance_for_assets:
- reference_band_red_lines:
```

## Writing Rules

- Keep option labels short enough for fast approval.
- Keep the decision scoped to one real topic.
- If the PRD already rules out an option, do not list it.
- If one option is safer but weaker visually, say that directly.
- If one option is stronger visually but increases atlas or restoration cost, say that directly.
