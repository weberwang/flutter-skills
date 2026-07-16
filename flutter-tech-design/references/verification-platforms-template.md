# Verification Platforms Template

Use this file as the single source of truth for the app-wide verification scope. Task briefs, implementation plans, progress records, and review reports must reference it instead of copying platform lists.

## Scope

- Owner:
- Last updated:
- Evidence root:
- Runtime validation timing: final integration only, after all modules, page functionality, and high-fidelity restoration are complete

## Required Platforms

| Platform | Runtime target | Required evidence | Commands | Evidence path | Final integration status |
|---|---|---|---|---|---|
| Android | Emulator or device | | | | |
| iOS | Simulator or device | | | | |
| Web | Browser | | | | |
| Desktop | OS target | | | | |

Remove rows that are out of scope and record them below. Keep this table current as the only platform verification record.

## Out of Scope

| Platform | Reason |
|---|---|

## Evidence Rules

- A platform is verified only during final integration, after all modules/pages and their high-fidelity restoration are complete, and after the required command, runtime evidence, and UI evidence are present when applicable.
- Module/page tasks may capture screenshots or goldens for design review, but they must not mark a platform verified or substitute for final runtime validation.
- Record blocked final validation in the platform row; do not mark the platform verified.
