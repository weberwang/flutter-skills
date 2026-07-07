---
name: effect-image-to-pencil-design
description: Use when approved Flutter effect images and DESIGN.md must be turned into a mandatory high-fidelity Pencil design source through MCP, then checked against the source image, repaired once after diff confirmation, and handed to human acceptance before later bitmap-generation decisions are finalized.
---

# Effect Image To Pencil Design

## Overview

Turn approved effect images into a mandatory high-fidelity Pencil design source.

This skill uses Pencil MCP as the design-file execution owner. It does not treat Pencil as a loose redraw step. The `.pen` file becomes a frozen structured design source that must stay visually close to the approved effect image and must preserve the page hierarchy, spacing, component boundaries, state language, and reusable asset bindings needed by later Flutter restoration.
Treat the approved effect image as the only visual input source for later design-file generation on this route. Do not fill missing layout, style, or asset decisions from prototype screenshots, ad references, or marketing redraws.

The default workflow is:

1. build Pencil design from the frozen design packet
2. compare Pencil output against the approved effect image
3. list visible gaps plus concrete repair actions
4. wait for confirmation
5. repair exactly one focused revision
6. hand off to human acceptance

## When To Use

- Shared or module page imagery is already approved.
- The workflow needs a real design file instead of only screenshots and prose.
- Later Flutter restoration is expected to use a frozen Pencil design source as its primary design artifact.

Do not use this skill when:

- the effect image is not approved yet
- `DESIGN.md` is missing
- the page is still in broad direction exploration rather than fidelity implementation

## Required Inputs

- approved effect image for the target scope
- `DESIGN.md`
- page or module state requirements
- frozen base design viewport width and height
- target `.pen` file path
- target page list or node ownership plan

If any required input is missing, stop and return `blocked`.

## MCP Contract

Use Pencil only through MCP.

- Always call `get_editor_state(include_schema: true)` before other Pencil operations when the schema is not already in context.
- Use `batch_design` as the primary write path for creating or repairing the `.pen` design.
- Use `snapshot_layout` for structural verification.
- Use `get_screenshot` for visual fidelity checks after a meaningful batch is complete.
- Use `batch_get`, `get_variables`, `set_variables`, and `export_nodes` only when they directly support fidelity, reuse, or downstream restoration.

Do not inspect `.pen` files with filesystem reads or grep.

## Workflow

1. Confirm the effect image, `DESIGN.md`, and state scope are already frozen enough for design execution.
2. Call Pencil MCP and load schema with `get_editor_state(include_schema: true)`.
3. Build the target design file with `batch_design`.
4. Make the design high fidelity from the start:
   - preserve layout hierarchy
   - preserve spacing and proportions
   - preserve typography tone
   - preserve component shapes, radius, depth, and visual grouping
   - preserve state-specific visual language
   - preserve the frozen design width
   - keep every Pencil page height at or above the frozen base design viewport height
   - allow a taller Pencil page only when the page or a major region is intentionally scrollable and the extra height is needed to show that designed scroll range
   - bind already approved reusable raster assets when they already exist, but do not require new image-asset generation before Pencil review
5. Run `snapshot_layout` to check obvious structural problems before visual review.
6. Run `get_screenshot` on the smallest meaningful page or section needed for parity review.
7. Compare the Pencil result against the approved effect image and produce:
   - `gap_list`
   - `root_causes`
   - `proposed_fixes`
   - `bitmap_generation_implications`
8. Wait for explicit confirmation before repair.
9. Apply one focused repair pass through `batch_design`.
10. Re-check with `snapshot_layout` and `get_screenshot`.
11. Hand off to human acceptance. Do not silently self-approve the design as frozen.
12. Use the confirmed review result as the basis for any later bitmap-generation decision. Do not freeze bitmap scope from the pre-repair image alone.

## Fidelity Requirements

- The Pencil design must be a high-fidelity restoration, not a schematic layout.
- The design must remain visually aligned with the approved effect image in:
  - hierarchy
  - spacing
  - proportions
  - radius
  - borders
  - shadows
  - typography scale and posture
  - color usage
  - asset placement
  - state composition
- The Pencil page size must keep the frozen design width unchanged.
- The Pencil page height must never be smaller than the frozen base design viewport height.
- If the page or a major region is intentionally scrollable, the Pencil page height may exceed that minimum to show the designed scroll range, but it must not compress the layout just to fit into one screen.
- If the effect image does not fully cover important states such as `empty`, `error`, `loading`, or permission-related states, the design file must still represent those states when the frozen module contract requires them.

## Output Contract

Return:

- `receipt_status`
- `pencil_file_path`
- `artifacts_produced`
- `layout_check_result`
- `comparison_scope`
- `gap_list`
- `proposed_fixes`
- `bitmap_generation_implications`
- `confirmation_required`
- `post_fix_review_artifacts`
- `blockers`

## Hard Rules

- Do not skip Pencil MCP and replace the design file with image markup or prose.
- Do not freeze the Pencil design before a compare-and-fix loop has happened.
- Do not repair multiple speculative rounds before the user confirms the first diff summary.
- Do not let the Pencil design silently drift from the effect image just because the tool can draw a cleaner version.
- Do not force new image-asset generation before the Pencil compare-confirm-fix loop is complete.
- Do not replace already approved reusable assets with newly improvised artwork.
- Do not set a Pencil page height below the frozen base design viewport height.
- Do not flatten an intentionally scrollable page or scrollable region just to keep the Pencil page inside one screen height.
- Do not treat a full-document screenshot as enough when the fidelity problem is local to one page or section.
- Do not mark the design accepted without human acceptance after the repair pass.

## Pressure Scenarios

- User says "直接生成 design file，不用对比效果图": block. Compare-first parity review is mandatory.
- User says "差一点没关系，先冻结": block. Pencil is the mandatory frozen design source.
- User says "先修三轮再给我看": decline in this skill. One compare-confirm-fix loop comes first.
- User says "用文件读写 .pen": block. Pencil files must only be accessed through MCP.
