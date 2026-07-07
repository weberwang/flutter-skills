# Execution Modes

Use this reference when `flutter-workflow` is invoked with `--auto`, `--full-auto`, or when it must decide whether to continue routing after a local milestone.

## `--auto`

When `--auto` is present, the orchestrator must keep routing and applying workflow transitions without stopping for ordinary downstream confirmation gates, as long as the next move is deterministic and no blocker is hit.

`--auto` is phase-aware:

- finish the shared pre-phase work first
- enter `current_phase=launch`
- complete the launch phase through release readiness
- enter `current_phase=premium` only when premium scope is explicitly selected

`--auto` includes both automatic confirmation and automatic execution for ordinary orchestrator-owned workflow gates.

The `--auto` goal is:

- finish PRD and technical baseline first
- complete the launch phase chain in order:
  `launch prototype -> launch effect image -> launch Pencil -> launch freeze -> launch restoration -> launch asset-enhancement resolution -> launch implementation -> launch QA -> release readiness`
- if premium enhancement is explicitly in scope, continue into the mandatory premium phase chain in order:
  `premium prototype -> premium effect image -> premium Pencil -> premium freeze -> premium restoration -> premium asset-enhancement resolution -> blueprint -> premium implementation -> parity QA`
- do not treat the premium phase as an optional postscript once Phase 2 has started; only specific asset-enhancement methods inside that phase may remain conditional on actual design needs
- stop only when workflow completion or a real blocker appears

`--auto` is not allowed to:

- skip the prototype step in either phase
- skip the Pencil step in either phase
- restore Flutter code directly from effect images
- bypass `@superpowers` `Spec` and `Plan`
- continue a premium route after `scope_reopen_required=yes`

## `--full-auto`

`--full-auto` includes everything in `--auto`, but expands auto-confirmation to deterministic human-facing workflow gates when existing artifacts collapse the decision to exactly one supported default.

`--full-auto` may auto-confirm:

- deterministic shared clarification gates
- deterministic launch-phase review gates
- deterministic premium-phase review gates
- deterministic device selection when exactly one supported default exists

`--full-auto` must still stop when:

- the available artifacts support multiple plausible defaults
- `scope_reopen_required=yes`
- route lock validation, receipt validation, or no-progress rules fail
- required tools, credentials, or artifacts are missing

## Auto Loop Contract

In both `--auto` and `--full-auto`:

1. Select the next valid step from the current phase and current stage.
2. Persist the route lock immediately.
3. Verify that the required phase artifacts already exist.
4. Run the next specialist step only if the route lock and preflight gate still authorize it.
5. Apply deterministic queued transitions immediately after receipt validation.
6. Re-evaluate whether the workflow should stay in the same phase, move to the next phase, or stop on a blocker.

If a premium request triggers `scope_reopen_required=yes`, the auto loop must stop premium advancement and route back to the matching launch scope or contract step instead of continuing as a normal enhancement.

## Stop Condition

The default stop condition is:

- the launch phase has reached `phase_1_release_ready`
- and either:
  - premium scope was not requested
  - or the premium phase has reached `phase_2_done`

`--auto` and `--full-auto` may stop only when:

- all required phases satisfy the completion condition
- or a real blocker appears and the current round cannot safely continue
