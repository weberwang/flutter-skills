---
name: pencil-design-to-flutter-restoration
description: Use when a frozen Pencil design source must be restored into high-fidelity Flutter implementation strategy, library-fit decisions, and restoration constraints before code execution or architecture mapping.
---

# Pencil Design To Flutter Restoration

## Overview

Turn a frozen Pencil design source into a Flutter restoration contract.

This skill sits between design freeze and code execution. It does not generate final page code. Instead, it decides how the frozen Pencil design should be restored in Flutter while preserving fidelity and respecting the real technology stack.

It must explicitly evaluate:

- what Flutter standard library can restore faithfully
- where third-party plugins are appropriate
- where native reconstruction is too brittle
- where approved bitmap assets must remain in use
- which Pencil details are fidelity-critical and must not be flattened for engineering convenience

## When To Use

- A shared or module Pencil design source is frozen.
- The workflow is preparing architecture or code restoration.
- The team needs a concrete restoration contract before implementation.

Do not use this skill when:

- the Pencil design source is not frozen
- the effect image or state coverage is still unresolved
- the request is still a design-change request instead of restoration planning

## Required Inputs

- frozen Pencil design file path
- approved effect image and visual evidence
- `DESIGN.md`
- module `impl.md`
- approved generated image assets and global asset catalog when relevant
- target Flutter technical baseline and package stack
- explicit `platform_identifier`

If any required input is missing, stop and return `blocked`.

## Restoration Workflow

1. Read the frozen restoration inputs in this priority:
   - frozen Pencil design source
   - frozen module or shared design-source packet
   - `DESIGN.md`
   - module `impl.md`
   - approved effect image and display evidence pack
   - generated image assets and global asset catalog
   - technical baseline and package stack
2. Identify fidelity-critical regions and state variants.
3. For each important region, classify restoration strategy:
   - `flutter_standard_library`
   - `approved_third_party_plugin`
   - `approved_bitmap_asset`
   - `mixed_strategy`
4. For every third-party plugin decision, explain:
   - why standard Flutter is not enough
   - which plugin capability is needed
   - what new risk or maintenance cost that plugin introduces
5. For every standard-library decision, explain why it is sufficient for high-fidelity restoration.
6. For every bitmap decision, confirm why native reconstruction would lose fidelity or become brittle.
7. Produce a restoration contract that downstream architecture and implementation must follow.
8. Hand off the restoration contract to `flutter-uiux-to-architecture` or the active code-restoration stage.

## Evaluation Dimensions

Evaluate every region through these dimensions:

- `structure`: layout, scroll ownership, sticky behavior, overlay zoning
- `visual`: spacing, typography, radius, depth, texture, imagery, icon posture
- `state`: ideal, loading, empty, error, permission, success, premium, locked
- `stack_fit`: Flutter standard library fit, plugin fit, asset fit, maintenance cost

## Output Contract

Return:

- `receipt_status`
- `restoration_contract_path_or_inline_pack`
- `design_source_inputs`
- `fidelity_critical_regions`
- `flutter_standard_library_decisions`
- `third_party_plugin_decisions`
- `bitmap_asset_decisions`
- `region_level_tradeoffs`
- `blocked_regions`
- `downstream_requirements`

## Hard Rules

- Do not jump straight from Pencil to page code without a restoration contract.
- Do not assume Flutter standard library is always enough.
- Do not assume a third-party plugin is justified just because it exists.
- Do not downgrade a fidelity-critical region to generic Flutter styling for convenience.
- Do not ignore state-specific visual language.
- Do not propose plugin usage without naming the exact capability gap it closes.
- Do not treat the effect image as more authoritative than the frozen Pencil design when the Pencil design has already passed parity confirmation.

## Pressure Scenarios

- Developer says "先按标准控件做，差一点后面再抠": block. Fidelity strategy must be explicit up front.
- User says "插件以后再看": block when the design clearly depends on capabilities beyond standard Flutter.
- Developer says "这块图直接不要了": classify as design rollback, not restoration.
- Design is pretty but state coverage is missing: block until the missing state restoration contract is explicit.
