# flutter-prd-rd-writer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增一个可根据 PRD 产出完整 Flutter 研发文档的 skill，覆盖技术方案、第三方包选型与最佳搭档、以及产品全链路交付内容。

**Architecture:** 采用一个轻量 `SKILL.md` 加四份按职责拆分的参考文档。主文件负责触发条件、执行顺序和输出约束，参考文件分别承载 PRD 拆解、Flutter 技术方案模板、第三方包策略、全链路交付清单。

**Tech Stack:** Markdown skill files, YAML metadata, Python validation scripts

---

### Task 1: 初始化 skill 目录

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/`
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/agents/openai.yaml`
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/references/`

- [ ] **Step 1: 运行初始化脚本创建 skill 目录**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\init_skill.py" flutter-prd-rd-writer --path "E:\Git\flutter-skills\skills" --resources references --interface display_name="Flutter PRD RD Writer" --interface short_description="Generate full Flutter RD docs from PRDs" --interface default_prompt="Use $flutter-prd-rd-writer to turn a PRD into a full Flutter研发文档 with architecture, package choices, best bundles, and fullchain delivery guidance."
```
Expected: 生成 skill 目录、`SKILL.md`、`agents/openai.yaml` 和 `references/` 目录。

- [ ] **Step 2: 检查初始化结果**

Run:
```powershell
rtk powershell -NoProfile -Command "Get-ChildItem -Recurse -Force 'E:\Git\flutter-skills\skills\flutter-prd-rd-writer'"
```
Expected: 能看到 `SKILL.md`、`agents/openai.yaml`、`references/`。

### Task 2: 编写主 skill 文件

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/SKILL.md`

- [ ] **Step 1: 写入触发条件与主工作流**

写入内容应覆盖：
- frontmatter 中的 `name` 与 `description`
- 触发场景
- 主工作流
- 输出规则
- 参考文件读取时机

- [ ] **Step 2: 补充中文注释式说明与严格约束**

在关键段落中用简体中文说明：
- 先输出假设前提与待确认项的原因
- 为什么要给出主方案、备选方案、取舍理由
- 为什么包选型必须写最佳搭档与避免混搭

### Task 3: 编写 PRD 拆解与技术方案参考文件

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/references/prd-intake-and-gap-analysis.md`
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/references/flutter-technical-solution-template.md`

- [ ] **Step 1: 写 PRD 拆解参考文件**

内容至少包含：
- PRD 输入检查清单
- 需求抽取维度
- 缺失信息识别规则
- 假设前提与待确认项输出模板

- [ ] **Step 2: 写 Flutter 技术方案模板参考文件**

内容至少包含：
- 研发文档章节骨架
- 架构、分层、状态管理、路由、网络、存储、鉴权、测试、发布等章节写法
- 每章必须给出推荐方案、备选方案、取舍理由

### Task 4: 编写包选型与全链路参考文件

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/references/package-selection-and-best-bundles.md`
- Create: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/references/fullchain-delivery-checklist.md`

- [ ] **Step 1: 写第三方包选型参考文件**

内容至少包含：
- 选型总原则
- 能力域矩阵
- 场景化最佳搭档组合
- 避免混搭清单
- 替换与迁移建议

- [ ] **Step 2: 写全链路交付清单参考文件**

内容至少包含：
- 前后端协作约定
- 数据与安全
- 埋点、监控、风控、灰度、发布、验收
- 里程碑与风险章节建议

### Task 5: 校验与验证

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-prd-rd-writer/**`

- [ ] **Step 1: 运行 skill 结构校验**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "E:\Git\flutter-skills\skills\flutter-prd-rd-writer"
```
Expected: 校验通过，无 frontmatter 或命名错误。

- [ ] **Step 2: 做一次文本级自检**

Run:
```powershell
rtk powershell -NoProfile -Command "Get-ChildItem -Recurse -File 'E:\Git\flutter-skills\skills\flutter-prd-rd-writer' | ForEach-Object { Select-String -Path $_.FullName -Pattern 'TODO|TBD|占位|待补充' -Encoding UTF8 }"
```
Expected: 无结果。

- [ ] **Step 3: 人工检查最终结构**

Run:
```powershell
rtk powershell -NoProfile -Command "Get-ChildItem -Recurse -Force 'E:\Git\flutter-skills\skills\flutter-prd-rd-writer'"
```
Expected: 目录结构与 spec 一致。
