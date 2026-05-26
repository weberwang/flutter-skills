# Plugin Rules

Replace project-specific details in this file during initialization.

## Force Switch

- `--force` means: reconfigure plugins in the current task scope, then continue later tasks.
- no `--force` + missing plugin setup means: perform the first-time plugin configuration, then continue later tasks.
- no `--force` + existing plugin setup means: keep the existing plugin setup, skip plugin reconfiguration, and continue later tasks.

## Project Plugin Inventory

- Core plugin set: `{{CORE_PLUGIN_SET}}`
- Platform-sensitive plugins: `{{PLATFORM_PLUGIN_SET}}`
- Cloud or console-backed plugins: `{{CLOUD_PLUGIN_SET}}`

## Reconfigure Notes

- Plugin reconfiguration scope: `{{PLUGIN_RECONFIGURE_SCOPE}}`
- Config files or native entries affected: `{{PLUGIN_CONFIG_FILES}}`
- Post-reconfigure verification: `{{PLUGIN_VERIFY_COMMANDS}}`
