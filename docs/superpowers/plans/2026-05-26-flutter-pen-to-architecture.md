# flutter-pen-to-architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增一个 `flutter-pen-to-architecture` skill，用于把 `Pencil` 的 `.pen` 文件和 `Pencil MCP` 结构化结果转成 Flutter 导向的设计解构、双主题方案、组件体系和页面架构方案，而不是直接生成代码。

**Architecture:** 采用一个轻量 `SKILL.md` 搭配七份单职责 `references/` 文档的结构。主文件只负责触发条件、主流程、硬规则和输出契约，参考文档分别沉淀输入契约、token 提取、双主题策略、组件拆解、页面架构、高保真取舍与输出蓝图，并在最终输出中专门留出可供 `flutter-init` 消费的规范摘要。

**Tech Stack:** Markdown skill files, YAML metadata, Python validation scripts

---

### Task 1: 初始化 skill 目录

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/agents/openai.yaml`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/`

- [ ] **Step 1: 运行初始化脚本创建 skill 骨架**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\init_skill.py" flutter-pen-to-architecture --path "E:\Git\flutter-skills\skills" --resources references --interface display_name="Flutter Pen To Architecture" --interface short_description="Turn Pencil .pen designs into Flutter architecture guidance" --interface default_prompt="Use $flutter-pen-to-architecture to translate Pencil .pen files or Pencil MCP output into Flutter-oriented design tokens, light and dark themes, reusable component plans, page architecture, and fidelity-versus-Flutterization decisions without generating code directly."
```
Expected: 生成 `skills/flutter-pen-to-architecture/`、`SKILL.md`、`agents/openai.yaml` 和 `references/` 目录。

- [ ] **Step 2: 检查初始化结果**

Run:
```powershell
rtk proxy powershell -NoProfile -Command "Get-ChildItem -Recurse -Force 'E:\Git\flutter-skills\skills\flutter-pen-to-architecture'"
```
Expected: 能看到 `SKILL.md`、`agents/openai.yaml` 与空的 `references/` 目录。

### Task 2: 编写主 skill 文件

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/SKILL.md`

- [ ] **Step 1: 写入 frontmatter 与 Overview**

写入内容必须覆盖：
- `name: flutter-pen-to-architecture`
- 触发描述，明确 `.pen`、`Pencil MCP`、Flutter 双主题、组件化、页面架构、非代码输出边界
- `Overview` 说明该 skill 的职责是设计解构与实现方案，不是代码生成

- [ ] **Step 2: 写入 Quick Start、Workflow、Hard Rules、Deliverables、References**

写入内容必须覆盖：
- 默认输入边界与信息不足时的 `前提假设` / `待确认项`
- 全局扫描、token 提取、亮暗主题策略、组件拆解、页面架构、高保真取舍的主流程
- 不机械翻译节点树、不把暗色主题当反相、不直接生成代码等硬规则
- 输出契约及 `flutter-init` 规范摘要
- 对七份参考文件的引用关系

### Task 3: 编写输入契约与 token/主题参考文件

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/pen-input-contract.md`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/design-token-extraction.md`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/dual-theme-strategy.md`

- [ ] **Step 1: 写入输入契约参考文件**

内容至少包含：
- `.pen`、节点树、variables、layout 的优先级
- 信息充分与不足的判断标准
- 不支持纯截图作为主入口的边界
- 何时必须输出 `前提假设` 与 `待确认项`

- [ ] **Step 2: 写入 token 提取参考文件**

内容至少包含：
- 颜色、字体、字重、圆角、间距、阴影、层级等 token 提取规则
- 零散样式归并为 Flutter token 的方法
- `ThemeData`、`ColorScheme`、`TextTheme`、`ThemeExtension` 的映射建议

- [ ] **Step 3: 写入亮色/暗色主题参考文件**

内容至少包含：
- 亮暗主题共用 token 与分叉 token
- 色彩语义、可读性、表面层级策略
- 为什么不能直接反相
- 当暗色线索不足时的推断边界

### Task 4: 编写组件、页面架构与取舍参考文件

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/component-decomposition.md`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/screen-architecture-planning.md`
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/fidelity-vs-flutterization.md`

- [ ] **Step 1: 写入组件拆解参考文件**

内容至少包含：
- 基础组件、组合组件、业务组件、页面区块的定义
- 什么时候应该抽复用组件
- 什么时候保留页面内私有结构即可
- 组件输出时应说明职责、插槽、状态变化点

- [ ] **Step 2: 写入页面架构参考文件**

内容至少包含：
- 多页面稿的页面家族识别方法
- 导航壳、列表详情流、表单流、弹层体系、状态区块的规划方法
- 页面骨架如何面向 Flutter 布局组织，而不是面向设计工具层级组织

- [ ] **Step 3: 写入高保真取舍参考文件**

内容至少包含：
- `建议高保真还原`
- `建议 Flutter 化重构`
- `建议简化处理`
- 三类判断标准与输出理由

### Task 5: 编写输出蓝图与元数据

**Files:**
- Create: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/references/output-blueprint.md`
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/agents/openai.yaml`

- [ ] **Step 1: 写入输出蓝图参考文件**

内容至少包含：
- 固定输出结构
- `设计原意`、`Flutter 落法`、`是否高保真`、`是否进入主题层`、`是否抽成复用组件`、`风险/备注` 字段
- 可供 `flutter-init` 消费的规范摘要模板

- [ ] **Step 2: 校正 agents 元数据**

检查并确保：
- `display_name` 为 `Flutter Pen To Architecture`
- `short_description` 明确 `.pen -> Flutter 架构方案`
- `default_prompt` 明确双主题、组件化与非代码输出边界

### Task 6: 校验与自检

**Files:**
- Modify: `E:/Git/flutter-skills/skills/flutter-pen-to-architecture/**`

- [ ] **Step 1: 运行 skill 结构校验**

Run:
```powershell
rtk python "C:\Users\forjs\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "E:\Git\flutter-skills\skills\flutter-pen-to-architecture"
```
Expected: 校验通过，无命名、frontmatter 或结构错误。

- [ ] **Step 2: 扫描占位符与遗漏项**

Run:
```powershell
rtk rg -n "TODO|TBD|待补充|占位|示例待写" "E:\Git\flutter-skills\skills\flutter-pen-to-architecture"
```
Expected: 无结果。

- [ ] **Step 3: 人工复核目录与内容边界**

Run:
```powershell
rtk proxy powershell -NoProfile -Command "Get-ChildItem -Recurse -Force 'E:\Git\flutter-skills\skills\flutter-pen-to-architecture'"
```
Expected: 目录结构与 spec 一致，主文件简洁，参考文件单职责，且明确提到 `flutter-init` 的消费摘要。
