---
name: visual-design-reviewer
description: Use when a complete design draft, preview pack, approved static comp, effect mockup, or Pencil-ready page design needs a commercial designer review before freeze, module splitting, Pencil handoff, or downstream implementation.
---

# Visual Design Reviewer

## Overview

Review complete design drafts the way a strong commercial product designer would review them, not the way a mood-board critic would. This review must run in a fresh subagent with a deliberately minimal context packet so design judgment stays focused and does not inherit polluted parent-thread context. For freeze workflows, the primary review target is the effect image, preview comp, static visual draft, or complete visual result that represents what the frozen direction will look like. Prioritize information hierarchy, key-task guidance, typography hierarchy, contrast, CTA clarity, business focus, state completeness, and handoff readiness, then return strengths, weaknesses, risks, and a final 100-point score.

## Quick Start

- Use this skill only when the design is complete enough to judge as a real product surface, not a loose direction fragment.
- If the work is still choosing between broad art directions, use `mobile-ui-design-coach` or the preview exploration parts of `design-preview-to-pen` first.
- If the workflow question is “can we freeze or hand this design off yet,” run this skill before `flutter-design-freeze-gate`.
- If the target is implemented Flutter UI rather than a design draft, use `flutter-design-parity-reviewer` instead.
- Always execute this skill in a fresh subagent. Do not run it inline inside the parent orchestration thread.
- For freeze decisions, review the effect image, preview pack, approved static comp, or completed visual result itself, not only the written freeze packet.

## Required Inputs

- Review target type:
  - `shared_visual_draft`
  - `module_page_draft`
  - `pencil_rebuild`
  - `static_preview_pack`
- The design brief, freeze card, or the closest upstream design packet.
- Screenshots, preview comps, Pencil screenshots, or equivalent visual evidence for the draft.
- The primary task, next best action, and intended completion path for the screen or flow.
- The primary business moment and the intended primary CTA.
- Expected state coverage for this design.
- Any frozen global guidance or theme artifacts when they already exist.
- A compact context packet prepared by the parent agent. Pass only the artifacts needed for the review; do not fork the full thread by default.

## Workflow

1. Confirm that you are running as a fresh subagent with a bounded context packet. If the parent tried to run this review inline or passed the whole thread history without need, return `review_decision: blocked`.
2. Read `references/draft-completeness-gate.md` and decide whether the visual evidence is complete enough for review. If not, return `review_decision: blocked`.
3. Read `references/commercial-review-rubric.md`.
4. Evaluate the first three seconds: what the eye sees first, whether the dominant zone is correct, and whether the page tells the user what matters now.
5. Evaluate key-task guidance: whether the primary task path, next best action, and completion path are explicit enough that the user does not have to interpret the screen manually.
6. Evaluate typography and contrast: whether the reading ladder, text-to-surface contrast, and CTA versus surrounding actions are clear enough for speed and trust.
7. Evaluate commercial focus: business moment visibility, trust cues, retention or conversion pressure, and whether the design looks product-specific instead of template-specific.
8. Evaluate system quality: spacing rhythm, surfaces, icon posture, reusable patterns, and whether the design can survive Pencil or Flutter handoff without guessing.
9. Evaluate state completeness: ideal, empty, loading, error, permission, disabled, and paid or locked states when relevant.
10. Score the draft with the rubric and return a concise but designer-grade review.
11. For freeze workflows, treat `90` as the minimum pass line. Any score below `90`, or any review that still requires design changes, must return to exactly one scope-matched revision pass. That revision pass ends the current review cycle and must not trigger another `visual-design-reviewer` run automatically.
12. Route the next move:
  - `ready_for_freeze_review` -> `flutter-design-freeze-gate`
  - `needs_shared_single_revision` -> `mobile-ui-design-coach` -> shared preview regeneration once -> stop and wait for explicit user restart if another review cycle is desired
  - `needs_module_single_revision` -> update the active module `ui/ux` documentation -> modify the active module design draft in Pen through `design-preview-to-pen` once -> stop and wait for explicit user restart if another review cycle is desired
  - `blocked` -> whichever upstream skill must provide the missing evidence

## Hard Rules

- Do not reward a pretty but generic screen with a high score if information hierarchy is muddy or the key task path is weak.
- Do not excuse low contrast as “subtle” or “premium.”
- Do not call a draft complete when it only shows a polished happy path and hides production states.
- Do not give full credit when typography sizes, weights, and spacing collapse into one flat reading plane.
- Do not let decorative polish compensate for weak task guidance or unclear next-step decisions.
- Do not allow a freeze workflow to proceed on a review score below `90`.
- Do not route a sub-90 shared draft into the module implementation loop.
- Do not route a sub-90 module implementation draft back into the shared global-analysis loop unless the problem is genuinely global.
- Do not treat a module-stage design review failure as a reason to redo module splitting.
- Do not ask for or imply a second review inside the same failed-review correction cycle.
- Do not turn one failed review into an endless regenerate -> re-review loop.
- Do not run this review inline in the parent thread.
- Do not inherit the full upstream conversation when a compact review packet would suffice.
- Do not review implementation screenshots as if they were the design source when frozen design artifacts already exist.
- Do not redesign the page here. Critique it, score it, and route the next design move.

## Output Contract

Return:

- `review_decision`
- `review_execution_mode`
- `final_score`
- `score_breakdown`
- `strengths`
- `weaknesses`
- `risks`
- `hierarchy_assessment`
- `task_guidance_assessment`
- `cta_assessment`
- `revision_required`
- `revision_scope`
- `revision_limit`
- `post_revision_policy`
- `recommended_fixes`
- `next_skill`
- `freeze_readiness_note`

## Score Interpretation

- `90-100`: strong commercial draft, freeze-ready if no critical blocker remains.
- `<90`: not ready for freeze; must receive one scope-matched revision pass and then stop without another review in the same cycle.

If information hierarchy, key-task guidance, typography hierarchy, contrast, or CTA clarity has a critical failure, do not return a freeze-ready decision even when the total score is otherwise high.

Set `review_execution_mode` to `fresh_subagent` for successful reviews.
Set `revision_required` to `true` whenever the score is below `90` or design changes are still required.
Set `revision_scope` to `shared_single_revision` or `module_single_revision` when revision is required.
Set `revision_limit` to `one_pass_only` when revision is required; otherwise use `none`.
Set `post_revision_policy` to `stop_no_re_review` when revision is required; otherwise use `none`.

## References

- Read `references/draft-completeness-gate.md` to decide whether the draft is reviewable yet.
- Read `references/commercial-review-rubric.md` for category weights, critical failures, and scoring language.
