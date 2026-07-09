# Verification Platforms Template

Use this file as the single source of truth for the app-wide verification scope. Task briefs, implementation plans, progress records, and review reports must reference it instead of copying platform lists.

## Scope

- Owner:
- Last updated:
- Evidence root:

## Required Platforms

| Platform | Runtime target | Required evidence | Commands | Evidence path | Status |
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

- A platform is verified only after the required command, runtime evidence, and UI evidence are present when applicable.
- Use screenshots or goldens for UI work only when required by the platform row or UI quality gate.
- Record blocked verification in the platform row; do not mark the platform verified.
