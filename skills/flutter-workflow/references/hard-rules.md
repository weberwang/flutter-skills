# Hard Rules

Use this reference before applying any state promotion, freeze decision, implementation handoff, or downstream delegation.

- Do not route raw requirements directly into technical baseline, design-source work, or implementation before the PRD flow is complete.
- Do not begin any phase-specific design work before the technical baseline is ready.
- Do not skip the prototype step in either phase.
- Do not generate an effect image before the matching phase prototype structure is confirmed.
- Do not skip the Pencil step in either phase.
- Do not skip asset-enhancement resolution in either phase.
- Do not treat an effect image as the frozen design source.
- Do not restore Flutter code directly from effect images when the active phase requires a Pencil design source.
- Do not freeze a launch design before the launch Pencil design source is confirmed.
- Do not freeze a premium visual upgrade before the premium Pencil design source is confirmed.
- Do not treat the launch phase as a low-quality validation mode. It must reach release readiness.
- Do not let the premium phase silently rewrite the launch product's core task path, primary CTA goal, page flow, required state semantics, or module ownership.
- Do not treat the premium phase itself as optional once Phase 2 has started. Only specific asset-enhancement methods inside the premium phase may remain conditional on actual design needs.
- If a premium request changes core task path, primary CTA goal, page flow, required state semantics, or module ownership, trigger `scope_reopen`.
- Do not let `scope_reopen` be silently absorbed as a visual-only delta.
- Do not run multiple subagents in parallel against the same active module or workflow record when outputs could race.
- Do not enter implementation execution in any phase until the corresponding phase freeze and restoration contract exist.
- Do not enter implementation execution in any phase until the corresponding asset-enhancement resolution node is complete. If any region was marked `atlas_required`, complete the required atlas-analysis, generation, background-processing, slicing, and asset-integration chain before implementation proceeds.
- Do not bypass `@superpowers` `Spec` and `Plan` before code execution.
- Do not treat `@product-design design-qa` as final human acceptance.
- Do not mark a phase complete while its required Pencil design source, restoration contract, or implementation proof is still missing.
