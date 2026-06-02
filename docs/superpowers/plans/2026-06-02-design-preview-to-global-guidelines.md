# Design Preview To Global Guidelines Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增一个 `design-preview-to-global-guidelines` skill，把静态效果图与视觉预览图收敛为全局设计指导文档与可直接消费的亮暗主题冻结配置，并改造下游 skill 强引用这套契约。

**Architecture:** 采用一个轻量 `SKILL.md` 配合五份单职责 `references/` 文档的结构。新 skill 负责固定输出契约，下游 skill 只允许引用与消费，不再重新解释全局设计原则或主题值。

**Tech Stack:** Markdown skill files, YAML metadata, Python validation scripts

---

### Task 1: 初始化并整理新 skill 骨架

**Files:**
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/agents/openai.yaml`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/`

- [ ] **Step 1: 用 skill-creator 初始化骨架**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\init_skill.py" design-preview-to-global-guidelines --path "E:\Git\flutter-skills\skills" --resources references --interface display_name="Design Preview To Global Guidelines" --interface short_description="Extract a global design guide and frozen dual themes" --interface default_prompt="Use $design-preview-to-global-guidelines to analyze design previews or screenshots, extract the product's global visual and UI/UX guidance, and freeze concrete light and dark theme values that downstream Flutter and Pencil skills must consume without reinterpretation."
```

- [ ] **Step 2: 检查初始化目录是否完整**

Run:
```powershell
rtk proxy powershell -NoProfile -Command "Get-ChildItem -Recurse -Force 'E:\Git\flutter-skills\skills\design-preview-to-global-guidelines'"
```

### Task 2: 固化新 skill 的主契约与参考文档

**Files:**
- Modify: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/SKILL.md`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/image-intake-and-analysis.md`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/global-guideline-contract.md`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/theme-freeze-schema.md`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/value-freeze-strategy.md`
- Create: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/references/downstream-linking-rules.md`

- [ ] **Step 1: 写入触发条件、主流程、硬规则与交付物**
- [ ] **Step 2: 固定 `global-design-guidelines.md` 的章节顺序与缺失值写法**
- [ ] **Step 3: 固定 `light-theme-freeze.yaml` 与 `dark-theme-freeze.yaml` 的字段结构与具体值要求**
- [ ] **Step 4: 写清楚从视觉证据推导具体主题值的规则与边界**
- [ ] **Step 5: 写清楚下游 skill 的消费规则与阻塞条件**

### Task 3: 改造入口与路由层

**Files:**
- Modify: `E:/Git/flutter-skills/skills/mobile-ui-design-coach/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-workflow-orchestrator/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-rd-module-splitter/SKILL.md`

- [ ] **Step 1: 给设计诊断入口补充“视觉稿 -> 全局指导冻结”的分流规则**
- [ ] **Step 2: 给工作流编排器补充新 skill 的路由规则与状态说明**
- [ ] **Step 3: 给模块拆分 skill 补充未来全局设计契约路径占位要求**

### Task 4: 改造下游消费层

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-design-freeze-gate/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/design-preview-to-pen/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-design-source-control/SKILL.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-design-parity-reviewer/SKILL.md`

- [ ] **Step 1: 冻结门禁必须校验 3 份固定产物是否完整**
- [ ] **Step 2: Pencil 重建必须把主题冻结文件视为上游真源**
- [ ] **Step 3: Flutter 架构提取必须保留冻结主题角色和值**
- [ ] **Step 4: 设计源控制必须把全局指导与主题 YAML 纳入优先级**
- [ ] **Step 5: 视觉对齐评审必须用这套契约判断偏差**

### Task 5: 校验与收尾

**Files:**
- Modify: `E:/Git/flutter-skills/docs/superpowers/specs/2026-06-02-design-preview-to-global-guidelines-design.md`
- Modify: `E:/Git/flutter-skills/skills/design-preview-to-global-guidelines/**`

- [ ] **Step 1: 运行新 skill 的结构校验**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "E:\Git\flutter-skills\skills\design-preview-to-global-guidelines"
```

- [ ] **Step 2: 扫描占位符与遗漏项**

Run:
```powershell
rtk rg -n "TODO|TBD|not done|placeholder|示例待写|待补充" "E:\Git\flutter-skills\skills\design-preview-to-global-guidelines"
```

- [ ] **Step 3: 检查变更后的 skill 路由文本是否都引用了新契约**

Run:
```powershell
rtk rg -n "design-preview-to-global-guidelines|global-design-guidelines.md|light-theme-freeze.yaml|dark-theme-freeze.yaml" "E:\Git\flutter-skills\skills"
```
