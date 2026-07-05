# Global Asset Catalog Contract

Use this reference whenever the workflow must initialize, validate, or update the project-wide generated-image and bitmap-asset catalog.

## Goal

Maintain one stable resource index that records every workflow-generated image and every implementation bitmap asset, so shared scope and module scope can reuse existing outputs by meaning and scenario, not only by filename.

Suggested path:

- `docs/project/assets/global-asset-catalog.json`

## Required Fields

Each catalog row should preserve at least these fields:

- `asset_id`
- `record_type`
- `name`
- `semantic`
- `usage_scenarios`
- `asset_mode`
- `artifact_status`
- `generation_stage`
- `source_scope`
- `source_pages`
- `reuse_status`
- `candidate_reuse_reason`
- `final_output_paths`
- `sheet_atlas`
- `atlas_manifest`
- `background_state`
- `background_processing_allowed`
- `notes`

## Field Intent

### `asset_id`

Stable unique id for the asset record.

### `record_type`

One of:

- `effect_image_draft`
- `effect_image_final`
- `bitmap_asset`
- `sheet_atlas`
- `flutter_native`
- `placeholder_only`

Use `effect_image_draft` for review-stage generated draft effect images that are still in the workflow.

Use `effect_image_final` for approved final effect images that become workflow evidence.

Use `bitmap_asset` for generated image assets that downstream design-source work, HTML, or Flutter implementation will reference directly.

Use `sheet_atlas` for the matching UI-only atlas artifact that is generated together with a qualifying effect-image step. Record whether the path is the confirmed solid-background atlas or the confirmed transparent atlas that later supports cut-safe slicing decisions.

### `name`

Human-readable resource name. Prefer semantic names over purely visual names.

Good:

- `empty-orders-box`
- `error-network-illustration`
- `icon-premium-badge`

Avoid:

- `blue-icon-1`
- `image-final-fixed`

### `semantic`

What the asset means in product terms.

Examples:

- `empty_state_orders`
- `network_error_feedback`
- `premium_membership_badge`

### `usage_scenarios`

The concrete scenes where the asset is allowed or expected to appear.

Examples:

- `orders_empty_state`
- `checkout_error_banner`
- `profile_membership_card`

### `asset_mode`

One of:

- `bitmap_asset`
- `effect_image`
- `sheet_atlas`
- `flutter_native`
- `placeholder_only`

Use `flutter_native` when the region should be implemented directly with Flutter SDK standard capabilities rather than through bitmap generation.

Use `effect_image` when the row tracks a generated final effect image or implementation-stage module effect image.

Use `sheet_atlas` when the row tracks the pre-cut atlas artifact that belongs to an approved shared or module effect-image step. The row must also distinguish whether that artifact is the confirmed solid-background atlas or the confirmed transparent atlas.

Use `placeholder_only` when the current image region is only a schematic stand-in and the real visual content will be created later from runtime data. Placeholder-only rows may stay in the catalog for semantic tracking, but they must not receive final generated image output paths.

### `artifact_status`

One of:

- `draft`
- `approved`
- `rejected`
- `deleted`

Use `draft` before final confirmation.

Use `approved` for workflow-selected images and approved bitmap assets.

Use `rejected` for superseded generated images that are still temporarily retained for review traceability.

Use `deleted` when the file has been removed from disk and only the audit trail remains.

### `generation_stage`

Which workflow step generated the image.

Examples:

- `design_recommendation_ready`
- `product_direction_confirmed`
- `implementing`
- `module_asset_resources_ready`
- `module_asset_resources_ready`

### `source_scope`

One of:

- `shared`
- `module`

### `source_pages`

Which pages or surfaces revealed the need for this asset.

### `reuse_status`

One of:

- `reusable`
- `candidate_reuse`
- `shared_only`
- `module_only`

### `candidate_reuse_reason`

Why the workflow could not safely decide whether an existing asset should be reused.

### `final_output_paths`

One or more final file paths written by the generation step.

For draft or final effect images, this usually contains the generated image path itself.

For generated bitmap assets, this contains the final asset file path that downstream design or implementation consumes.

### `sheet_atlas`

The final atlas image path for the matching UI-only atlas when that record tracks atlas evidence.

### `atlas_manifest`

The manifest path for the matching atlas. This manifest should preserve slice bounds, background mode, slice type, and cut-safety so later flows can cut approved regions without guessing.

### `background_state`

The detected background state for the atlas or slice candidate.

Allowed values:

- `transparent`
- `solid_color`
- `non_solid`

### `background_processing_allowed`

Whether a generation-based transparency repair step is still allowed for this atlas or slice candidate.

Rules:

- `false` when the input is already transparent
- `true` when `background_state=solid_color`
- `true` when `background_state=non_solid`

## Reuse Rules

- Reuse decisions must consider `name`, `semantic`, and `usage_scenarios` together.
- Do not treat filename similarity alone as proof of reuse.
- If an asset is close in meaning but not certainly reusable, set `reuse_status=candidate_reuse` and stop for confirmation.
- Once an approved reusable generated image asset exists, later shared or module work should prefer that asset over regenerating a duplicate bitmap.
- Do not convert `placeholder_only` rows into bitmap assets unless the workflow explicitly confirms that the region now needs a generated bitmap.

## Maintenance Rules

- Every shared or module image-generation run must read the catalog first.
- Every generated final effect image, implementation-stage module effect image, matching `sheet_atlas`, shared bitmap asset, and module bitmap asset that enters workflow evidence or downstream consumption must be written into the catalog in the same workflow step.
- Do not delete an approved reusable asset row just because a later module no longer needs it.
- If a generated image file is replaced, rejected, or deleted after freeze or review, update `artifact_status` and `final_output_paths` in the same workflow step.
- If an obsolete generated image is deleted from disk, keep the row or audit note explicit enough that later workflow steps do not silently recreate or reference the stale file by mistake.

## Validation Checklist

Before approving the catalog update, verify:

- every new generated-image row has `name`
- every new generated-image row has `semantic`
- every new generated-image row has `usage_scenarios`
- every row has the correct `record_type`
- every row has the correct `asset_mode`
- every approved generated image has a concrete output path
- every approved atlas row has both `sheet_atlas` and `atlas_manifest`
- every atlas or slice candidate row has the correct `background_state`
- every atlas or slice candidate row has the correct `background_processing_allowed`
- every candidate reuse row has a reason
- no row points at a missing generated file path when `artifact_status=approved`
