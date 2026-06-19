# Global Asset Catalog Contract

Use this reference whenever the workflow must initialize, validate, or update the project-wide bitmap-asset catalog.

## Goal

Maintain one stable resource index that lets shared scope and module scope atlas work reuse existing slices by meaning and scenario, not only by filename.

Suggested path:

- `docs/project/assets/global-asset-catalog.json`

## Required Fields

Each asset row should preserve at least these fields:

- `asset_id`
- `name`
- `semantic`
- `usage_scenarios`
- `asset_mode`
- `source_scope`
- `source_pages`
- `reuse_status`
- `candidate_reuse_reason`
- `atlas_owner`
- `texturepacker_entry`
- `sliced_outputs`
- `notes`

## Field Intent

### `asset_id`

Stable unique id for the asset record.

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

- `atlas_asset`
- `flutter_native`
- `placeholder_only`

Use `flutter_native` when the region should be implemented directly with Flutter SDK standard capabilities rather than through bitmap generation.

Use `placeholder_only` when the current image region is only a schematic stand-in and the real visual content will be created later from runtime data. Placeholder-only rows may stay in the catalog for semantic tracking, but they must not receive atlas ownership, TexturePacker frames, or slice outputs.

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

### `atlas_owner`

Which atlas currently owns the approved bitmap export.

Examples:

- `shared/shared-core-ui`
- `module/orders/orders-status`

### `texturepacker_entry`

The frame key or frame reference used in the active `texturepacker.json`.

### `sliced_outputs`

The final exported slice paths that prototypes and later implementation may consume directly.

## Reuse Rules

- Reuse decisions must consider `name`, `semantic`, and `usage_scenarios` together.
- Do not treat filename similarity alone as proof of reuse.
- If an asset is close in meaning but not certainly reusable, set `reuse_status=candidate_reuse` and stop for confirmation.
- Once a reusable slice is approved, later module atlas work should prefer that slice over regenerating a duplicate bitmap asset.
- Do not convert `placeholder_only` rows into atlas assets unless the workflow explicitly confirms that the region now needs a generated bitmap.

## Maintenance Rules

- Every shared or module atlas run must read the catalog first.
- Every confirmed atlas run must write back atlas ownership and slice paths.
- Do not delete an approved reusable asset row just because a later module no longer needs it.
- If a slice path changes, update the catalog in the same workflow step.

## Validation Checklist

Before approving the catalog update, verify:

- every new atlas asset has `name`
- every new atlas asset has `semantic`
- every new atlas asset has `usage_scenarios`
- every row has the correct `asset_mode`
- every reusable slice has a concrete output path
- every candidate reuse row has a reason
- no row points at a missing atlas owner or missing slice path
