# flutter-pen-to-architecture MCP 导出实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `flutter-pen-to-architecture` 的图片导出能力从仓库内脚本彻底切换为 `Pencil MCP` 直出，移除本地导出脚本与 `pubspec.yaml` 自动修改脚本，并让 skill 文档、参考文档与历史设计文档统一到新的 MCP 流程。

**Architecture:** 本次实现不新增运行时代码，而是收口 skill 规范。核心做法是重写 `SKILL.md`、参考文档与 agent prompt，让导出流程统一依赖 `get_editor_state`、`batch_get`、`snapshot_layout` 和 `export_nodes`；同时删除 `scripts/` 下新增的导出脚本、测试和 Node 依赖，并把旧的脚本方案文档改成“已废弃”说明，避免仓库内存在相互冲突的实现指引。

**Tech Stack:** Markdown skill 文档、YAML agent 配置、`apply_patch` 文件改写与删除、`rg`/PowerShell 文本审计、Pencil MCP 工具契约

---

### Task 1: 重写 skill 入口与 agent 提示

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/agents/openai.yaml`

- [ ] **Step 1: 先做脚本时代措辞审计，确认当前文案仍然依赖旧实现**

Run:
```powershell
rtk rg -n "register the folder in pubspec.yaml|embedded assets|manifest fallback|export_pen_assets|ensure_flutter_assets" "skills/flutter-pen-to-architecture/SKILL.md" "skills/flutter-pen-to-architecture/agents/openai.yaml"
```
Expected: FAIL 风格的审计结果，即命中旧的脚本导出或自动修改 `pubspec.yaml` 表述。

- [ ] **Step 2: 用完整 YAML 替换 `agents/openai.yaml`**

```yaml
interface:
  display_name: "Flutter Pen To Architecture"
  short_description: "Export Flutter-facing image assets from Pencil nodes via MCP"
  default_prompt: "Use $flutter-pen-to-architecture to inspect a Pencil .pen file through Pencil MCP, export reusable design nodes into a Flutter project's assets/images/ via export_nodes, check pubspec.yaml without modifying it, and fold those assets into Flutter-oriented restoration guidance with tokens, themes, reusable components, and fidelity-versus-Flutterization decisions."
```

- [ ] **Step 3: 用完整文档替换 `SKILL.md`，把工作流彻底切到 MCP**

```md
---
name: flutter-pen-to-architecture
description: Use when translating Pencil `.pen` design files or Pencil MCP structured output into a Flutter-oriented design architecture plan, especially when the task is to export reusable design nodes into a Flutter project's `assets/images/` via Pencil MCP `export_nodes`, audit `pubspec.yaml` without modifying it, extract global design tokens, define light and dark themes, decompose reusable components, and decide what should be restored faithfully versus refactored to fit Flutter design philosophy instead of generating code directly.
---

# Flutter Pen To Architecture

## Overview

Turn Pencil design sources into a Flutter-facing implementation architecture instead of a node-by-node rebuild. Default to whole-project analysis: extract global tokens, derive light and dark themes, decompose reusable components, plan multi-screen page structure, and explain where high fidelity should yield to Flutter-native structure.

When asset export is part of the task, use Pencil MCP node analysis and `export_nodes` as the only export path.

## Quick Start

- Treat `.pen` files as Pencil MCP inputs, not ZIP archives.
- Call `get_editor_state(include_schema: true)` before any Pencil MCP read or export operation.
- Use `batch_get` and `snapshot_layout` to identify candidate export nodes.
- Use `export_nodes` to write selected assets to `<projectRoot>/assets/images/`.
- Check whether `pubspec.yaml` already declares `assets/images/`, but do not modify it in this skill.
- Continue with tokens, themes, components, and screen architecture after export decisions are stable.

## Workflow

1. Identify the real input surface: `.pen`, MCP node tree, variables, layout, reusable instances, missing structural data, and whether a Flutter project root is available.
2. Load the Pencil MCP schema with `get_editor_state(include_schema: true)` before any read or export action.
3. Use `batch_get` to inspect candidate pages, reusable nodes, and obvious image-bearing regions.
4. Use `snapshot_layout` when sizing, clipping, or container boundaries matter for export decisions.
5. Export only the selected nodes through `export_nodes` into `<projectRoot>/assets/images/`.
6. Audit `pubspec.yaml` and report whether `assets/images/` is already declared; if not, include the exact snippet the Flutter project should add.
7. Scan the whole design system: page families, navigation shells, information hierarchy, repeated motifs, and semantic surfaces.
8. Extract design tokens for color, typography, spacing, radius, elevation, and status semantics.
9. Build a dual-theme strategy for light and dark instead of treating dark mode as a color inversion.
10. Decompose the UI into reusable layers: primitives, composite widgets, business widgets, and page sections.
11. Plan screen architecture across the whole flow: shells, content regions, state zones, overlays, and transitions between screens.
12. Classify key decisions into `建议高保真还原`、`建议 Flutter 化重构`、`建议简化处理`, and explain why.
13. Produce an output pack that a Flutter team and `flutter-init` can consume directly, including node export and mapping results.

## Hard Rules

- Do not parse `.pen` files as ZIP archives.
- Do not rely on a local export script or an MCP manifest fallback.
- Do not modify `pubspec.yaml` in this skill.
- Do not default to full-page exports.
- Do not auto-rename exported files; report the current filename and a suggested business filename separately.
- Do not assume how `export_nodes` handles same-name conflicts; report observed conflicts and give a recommendation.
- Do not translate absolute coordinates or raw node hierarchy into Flutter layout literally.
- Do not treat every visual node as a reusable widget; only extract components that improve reuse, clarity, or maintenance.
- Do not treat dark mode as light mode with reversed colors.
- Do not return generic design commentary. Always land on Flutter-facing tokens, themes, components, screen architecture, and implementation boundaries.

## Deliverables

Every result should cover at least:

- `输入摘要`
- `图片资源导出结果`
- `图片资源映射表`
- `Flutter 资源接入结果`
- `全局设计结构`
- `设计 Token 归纳`
- `亮色主题方案`
- `暗色主题方案`
- `组件拆解清单`
- `页面实现骨架`
- `高保真 / Flutter 化取舍说明`
- `实现边界建议`
- `可供 flutter-init 消费的规范摘要`
- `风险与待确认项`

For important exported assets, prefer a structured row with:

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

## Output Contract

The final output must help another Flutter-focused agent continue without reopening the design tree. That means:

- Group tokens into maintainable categories instead of dumping raw style values.
- Distinguish theme-level decisions from component-level decisions.
- Separate global shell patterns from page-specific structure.
- State clearly what should go into `ThemeData`, what belongs in `ThemeExtension`, and what should stay inside feature widgets.
- Keep exported asset reporting node-centric instead of archive-centric.
- End with a `flutter-init` summary that can be turned into project guardrails or implementation constraints.

## Verification

When the workspace contains a real `.pen` file, verify the export flow with:

1. `get_editor_state(include_schema: true)`
2. `batch_get` and, when necessary, `snapshot_layout`
3. `export_nodes` into `<projectRoot>/assets/images/`
4. A check that the returned absolute file paths exist

If the workspace has no `.pen` file, explicitly report that the live Pencil MCP smoke test remains pending and do not claim it was completed.

## References

- Read `references/pen-input-contract.md` to decide whether the available `.pen` and MCP data are sufficient and how to downgrade safely when they are not.
- Read `references/asset-extraction-and-mapping.md` to decide which nodes should be exported, how they map into `assets/images/`, and how overwrite or naming behavior should be reported.
- Read `references/design-token-extraction.md` to normalize raw design styles into Flutter-ready tokens.
- Read `references/dual-theme-strategy.md` to derive light and dark themes with semantic consistency.
- Read `references/component-decomposition.md` to decide which parts deserve reusable widgets and which should stay local to a screen.
- Read `references/screen-architecture-planning.md` to map multi-screen designs into shells, flows, and state regions.
- Read `references/fidelity-vs-flutterization.md` to explain what should remain visually faithful and what should be adapted for Flutter design philosophy.
- Read `references/output-blueprint.md` to keep the final answer structure stable and `flutter-init`-friendly.
```

- [ ] **Step 4: 运行通过性审计，确认 skill 文档已经切换到 MCP 路径**

Run:
```powershell
rtk rg -n "get_editor_state|batch_get|snapshot_layout|export_nodes|do not modify `pubspec.yaml`|建议业务命名" "skills/flutter-pen-to-architecture/SKILL.md"
```
Expected: PASS，命中新工作流关键词；旧的脚本导出词不再作为当前流程出现。

### Task 2: 重写导出参考文档

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/asset-extraction-and-mapping.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/pen-input-contract.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/output-blueprint.md`

- [ ] **Step 1: 先确认参考文档还在描述脚本时代的资源提取与回退**

Run:
```powershell
rtk rg -n "embedded assets|manifest fallback|same-name conflicts|assets/images/ already declared|原始资源标识" "skills/flutter-pen-to-architecture/references"
```
Expected: FAIL 风格的审计结果，即命中旧的归档资源、manifest 回退或脚本接入措辞。

- [ ] **Step 2: 用完整内容替换 `references/asset-extraction-and-mapping.md`**

```md
# Asset Extraction And Mapping

## Purpose

Define which Pencil nodes should be exported, how they land in `assets/images/`, and how they should be consumed during Flutter restoration.

## Priority

1. Explicit `image` nodes with independent reuse value
2. Composite `group` or `frame` nodes that are expensive to rebuild in Flutter
3. User-requested high-fidelity visual regions

## Export Rules

- Use Pencil MCP node inspection, not archive extraction.
- Default export target is `<projectRoot>/assets/images/`.
- Default export format is `png` unless the task explicitly requires another format.
- Prefer node-level exports over full-page exports.
- Export only nodes that carry independent restoration value.
- Keep the actual exported filename and the suggested business filename as separate fields.
- Do not assume overwrite behavior; report conflicts based on observed export results.
- `pubspec.yaml` is audited and reported, not modified.

## Output Fields

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`
```

- [ ] **Step 3: 用完整内容替换 `references/pen-input-contract.md`**

```md
# Pencil Input Contract

## Purpose

Define what input quality is required before this skill can make reliable Flutter architecture and asset-export recommendations.

## Preferred Input Order

1. `.pen` file opened through Pencil MCP
2. Pencil MCP node tree
3. Pencil MCP variables
4. Pencil MCP layout snapshots or structural geometry summaries
5. Screenshots only as supporting evidence, never as the primary source

## Minimum Acceptable Input

Use the skill normally when you have:

- at least one `.pen` file or an MCP node tree
- enough screen structure to identify major page regions
- enough styling clues to infer typography and color groupings

If reusable component instances or variables are present, treat them as higher-confidence signals than screenshots or absolute coordinates.

## When Input Is Strong Enough For Global Analysis

Proceed with whole-system analysis when most of the following are available:

- multiple related screens or a single `.pen` document with multiple top-level flows
- reusable instances or repeated structural patterns
- variables or clearly repeated style values
- navigation or shell clues

In this mode, bias toward extracting a shared token system and component families first.

## When Input Is Only Strong Enough For Partial Analysis

Downgrade the output when:

- only one screen is available
- variables are absent
- node names are noisy or non-semantic
- repeated components cannot be identified confidently
- dark-theme clues do not exist

In this case, output:

- `前提假设`
- `待确认项`
- `局部结论`

Do not pretend the design system is fully known.

## Unsupported Primary Inputs

Do not treat these as the main trigger for this skill:

- raw screenshots without structure
- textual design descriptions without `.pen` or MCP data
- visual moodboards with no layout or interaction context

If the user only has those inputs, recommend a design-direction skill first or explain that the output will be approximate.

## Asset Export Constraints

- Export decisions must be based on Pencil MCP node inspection.
- Call `get_editor_state(include_schema: true)` before any read or export operation.
- Use `batch_get` and `snapshot_layout` to decide what is worth exporting.
- Use `export_nodes` as the only export mechanism.
- If two data sources conflict, trust the MCP node tree and reusable-instance relationships before screenshot appearance.
```

- [ ] **Step 4: 用完整内容替换 `references/output-blueprint.md`**

```md
# Output Blueprint

## Goal

Keep every result from this skill structurally stable so that human teams and downstream skills can consume it without re-parsing the design.

## Recommended Output Order

1. `输入摘要`
2. `图片资源导出结果`
3. `图片资源映射表`
4. `Flutter 资源接入结果`
5. `全局设计结构`
6. `设计 Token 归纳`
7. `亮色主题方案`
8. `暗色主题方案`
9. `组件拆解清单`
10. `页面实现骨架`
11. `高保真 / Flutter 化取舍说明`
12. `实现边界建议`
13. `可供 flutter-init 消费的规范摘要`
14. `风险与待确认项`

## Required Asset Sections

### 图片资源导出结果

At minimum include:

- exported `.pen` file
- export target directory
- export format
- exported node count
- exported file list
- skipped candidate nodes and reasons

### 图片资源映射表

At minimum include:

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

### Flutter 资源接入结果

At minimum include:

- whether `pubspec.yaml` was found
- whether `assets/images/` is already declared
- the exact snippet to add when the declaration is missing
- recommended usage such as `Image.asset('assets/images/xxx.png')`

Do not claim the file was modified unless the task explicitly included that work outside this skill.

## Required Row Schema

For important sections, components, or theme decisions, prefer a row or grouped bullets containing:

- `设计原意`
- `Flutter 落法`
- `是否高保真`
- `是否进入主题层`
- `是否抽成复用组件`
- `风险/备注`

## flutter-init Summary Contract

The `可供 flutter-init 消费的规范摘要` section should include at least:

- theme constraints
- token constraints
- component constraints
- page-shell constraints
- high-fidelity boundaries
- Flutterization boundaries

## Quality Bar

The final output should make these handoffs easy:

- a Flutter architect can decide shared theming structure
- a UI engineer can identify which widgets deserve reuse
- a project-guardrails skill can extract durable constraints
- an implementation skill can continue without reopening the design tree
```

- [ ] **Step 5: 运行参考文档通过性审计，确认字段和流程已改成节点导出**

Run:
```powershell
rtk rg -n "节点 ID|建议业务命名|get_editor_state|export_nodes|Do not claim the file was modified" "skills/flutter-pen-to-architecture/references"
```
Expected: PASS，命中节点导出和“只提示不修改”相关字段；旧的 manifest fallback 与原始资源标识不再作为当前规则存在。

### Task 3: 删除脚本实现、测试与 Node 依赖

**Files:**
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/export_pen_assets.mjs`
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.mjs`
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.test.mjs`
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.test.mjs`
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/package.json`
- Delete: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/scripts/package-lock.json`

- [ ] **Step 1: 先确认待删除文件都真实存在**

Run:
```powershell
rtk rg --files "skills/flutter-pen-to-architecture/scripts"
```
Expected: PASS，列出 6 个待删除文件。

- [ ] **Step 2: 用一次 `apply_patch` 删除脚本、测试和依赖文件**

```diff
*** Begin Patch
*** Delete File: skills/flutter-pen-to-architecture/scripts/export_pen_assets.mjs
*** Delete File: skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.mjs
*** Delete File: skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.test.mjs
*** Delete File: skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.test.mjs
*** Delete File: skills/flutter-pen-to-architecture/scripts/package.json
*** Delete File: skills/flutter-pen-to-architecture/scripts/package-lock.json
*** End Patch
```

- [ ] **Step 3: 验证脚本目录只剩空目录或不再包含文件**

Run:
```powershell
rtk rg --files "skills/flutter-pen-to-architecture/scripts"
```
Expected: PASS，输出为空。

- [ ] **Step 4: 审计仓库，确认当前实现路径不再依赖脚本文件**

Run:
```powershell
rtk rg -n "export_pen_assets|ensure_flutter_assets|package-lock.json|jszip|manifest fallback" "skills/flutter-pen-to-architecture" "docs/superpowers"
```
Expected: 只允许命中历史说明或新 spec 中明确的“已废弃/历史背景”文字；不应再命中当前 `SKILL.md`、`openai.yaml` 或参考文档。

### Task 4: 处理历史设计文档冲突

**Files:**
- Modify: `E:/Git/flutter-skills/docs/superpowers/specs/2026-05-26-flutter-pen-to-architecture-assets-design.md`
- Modify: `E:/Git/flutter-skills/docs/superpowers/plans/2026-05-26-flutter-pen-to-architecture-assets.md`

- [ ] **Step 1: 用“已废弃”说明替换旧设计文档，避免仓库内继续推荐脚本方案**

```md
# flutter-pen-to-architecture 图片资源导出扩展设计文档（已废弃）

> 状态：已废弃
> 
> 替代文档：`docs/superpowers/specs/2026-05-27-flutter-pen-to-architecture-mcp-export-design.md`

## 废弃原因

- 旧方案依赖 `export_pen_assets.mjs` 解析 `.pen`
- 旧方案依赖 `ensure_flutter_assets.mjs` 自动修改 `pubspec.yaml`
- 当前方案已统一切换为通过 `Pencil MCP` 的 `export_nodes` 直接导出节点
- `pubspec.yaml` 在当前方案中只检查与提示，不再自动修改

## 历史备注

这份文档仅保留为脚本方案历史记录，不再作为当前实现依据。
```

- [ ] **Step 2: 用“已废弃”说明替换旧实现计划，避免执行者继续按脚本计划落地**

```md
# flutter-pen-to-architecture 图片资源导出实现计划（已废弃）

> 状态：已废弃
> 
> 替代计划：`docs/superpowers/plans/2026-05-27-flutter-pen-to-architecture-mcp-export.md`

## 废弃原因

- 旧计划围绕 `export_pen_assets.mjs` 与 `ensure_flutter_assets.mjs` 展开
- 当前实现已不保留本地导出脚本、测试骨架与 Node 依赖
- 当前实现以 Pencil MCP 工具流为唯一导出路径

## 历史备注

这份计划仅保留为脚本方案历史记录，不再作为当前实现步骤。
```

- [ ] **Step 3: 运行历史文档验证，确认旧文件已经变成归档说明**

Run:
```powershell
rtk rg -n "已废弃|替代文档|替代计划|历史记录" "docs/superpowers/specs/2026-05-26-flutter-pen-to-architecture-assets-design.md" "docs/superpowers/plans/2026-05-26-flutter-pen-to-architecture-assets.md"
```
Expected: PASS，两个文件都只承担归档说明职责，不再包含可执行的脚本落地步骤。

### Task 5: 全仓校验与验证缺口记录

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/asset-extraction-and-mapping.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/pen-input-contract.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/output-blueprint.md`
- Modify: `E:/Git/flutter-skills/docs/superpowers/specs/2026-05-26-flutter-pen-to-architecture-assets-design.md`
- Modify: `E:/Git/flutter-skills/docs/superpowers/plans/2026-05-26-flutter-pen-to-architecture-assets.md`

- [ ] **Step 1: 运行占位符扫描，确认新旧文档都没有半成品标记**

Run:
```powershell
@'
from pathlib import Path

paths = [
    Path("skills/flutter-pen-to-architecture/SKILL.md"),
    Path("skills/flutter-pen-to-architecture/references/asset-extraction-and-mapping.md"),
    Path("skills/flutter-pen-to-architecture/references/pen-input-contract.md"),
    Path("skills/flutter-pen-to-architecture/references/output-blueprint.md"),
    Path("docs/superpowers/specs/2026-05-26-flutter-pen-to-architecture-assets-design.md"),
    Path("docs/superpowers/plans/2026-05-26-flutter-pen-to-architecture-assets.md"),
]
patterns = ["TO" + "DO", "TB" + "D", "待补", "占位", "implement" + " later"]
hits = []
for path in paths:
    text = path.read_text(encoding="utf-8")
    for pattern in patterns:
        if pattern in text:
            hits.append(f"{path}: {pattern}")
if hits:
    raise SystemExit("\n".join(hits))
print("no-placeholders")
'@ | python -
```
Expected: PASS，输出 `no-placeholders`。

- [ ] **Step 2: 运行路径一致性审计，确认当前 skill 只描述 MCP 直出**

Run:
```powershell
rtk rg -n "export_nodes|get_editor_state|batch_get|snapshot_layout|assets/images/" "skills/flutter-pen-to-architecture/SKILL.md" "skills/flutter-pen-to-architecture/references"
```
Expected: PASS，命中 MCP 工具链和 `assets/images/` 目标目录。

- [ ] **Step 3: 运行反向审计，确认当前活跃文档中不再把脚本当成实现方案**

Run:
```powershell
rtk rg -n "export_pen_assets|ensure_flutter_assets|manifest fallback|register the folder in pubspec.yaml" "skills/flutter-pen-to-architecture/SKILL.md" "skills/flutter-pen-to-architecture/references" "skills/flutter-pen-to-architecture/agents/openai.yaml"
```
Expected: PASS，输出为空。

- [ ] **Step 4: 检查仓库是否存在可用于 live smoke 的 `.pen` 样例**

Run:
```powershell
rtk rg --files -g "*.pen"
```
Expected: 当前仓库输出为空。

- [ ] **Step 5: 在执行总结中显式记录 live Pencil MCP smoke 仍待真实 `.pen` 文件验证**

执行总结必须包含下面这段原文，避免把未做的验证说成已完成：

```text
仓库当前没有 `.pen` 样例文件，因此本次只完成了 MCP 工作流文档化与仓库路径收敛；真实的 Pencil MCP 导出 smoke test 仍待后续拿到 `.pen` 文件后执行。
```

- [ ] **Step 6: 如果后续获得 `.pen` 样例，再按固定 MCP 流程补做 live smoke**

Tool calls:
```json
{"recipient":"mcp__pencil__.get_editor_state","parameters":{"include_schema":true}}
{"recipient":"mcp__pencil__.batch_get","parameters":{"filePath":"<sample.pen>","patterns":[{"type":"image"},{"type":"frame"},{"type":"group"}],"readDepth":2,"searchDepth":3}}
{"recipient":"mcp__pencil__.snapshot_layout","parameters":{"filePath":"<sample.pen>","parentId":"<candidate-node-id>","maxDepth":1}}
{"recipient":"mcp__pencil__.export_nodes","parameters":{"filePath":"<sample.pen>","nodeIds":["<approved-node-id>"],"outputDir":"<flutter-project>/assets/images","format":"png","scale":2}}
```
Expected: 只有在拿到真实 `.pen` 文件时才执行；执行后需要核对 MCP 返回的绝对路径确实存在。

## 计划自检

- 本计划覆盖了 spec 中要求的 4 个方向：skill 流程重写、参考文档重写、脚本删除、历史文档去冲突。
- 本计划没有要求新增兼容层，也没有保留脚本与 MCP 双轨。
- 本计划明确记录了仓库缺少 `.pen` 样例文件，因此 live smoke 只能作为后续补验，不会在执行时被伪造成已完成。
- 根据仓库 `AGENTS.md` 的提交约束，执行阶段完成所有改动后不要直接提交，必须先询问用户选择 `仅提交`、`提交并推送`、`忽略`。
