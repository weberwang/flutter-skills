# design-preview-to-global-guidelines 设计文档

## 1. 背景

当前仓库已经具备以下几类能力：

- `mobile-ui-design-coach`：负责设计诊断、商业化质感提升、方向冻结。
- `design-preview-to-pen`：负责预览稿探索、素材规划与 Pencil 重建。
- `flutter-pen-to-architecture`：负责从 `.pen` 或 Pencil MCP 结果提取 Flutter 导向的 token、主题、组件与页面架构。

现有链路缺少一个稳定的中间层：当用户已经拿到效果图、截图、视觉预览图或审批后的静态稿时，系统还不能把这些视觉证据直接收敛成一份全局 UI/UX 指导文档，以及两套可被后续 skill 直接消费的亮色/暗色主题冻结配置。

这会导致下游 skill 在消费设计信息时出现分支：

- 有时读设计冻结卡。
- 有时读预览图。
- 有时自行推断主题值。
- 有时在实现阶段重新解释视觉层级。

这与当前仓库强调的“冻结后不重解释”原则冲突。

## 2. 目标

新增一个名为 `design-preview-to-global-guidelines` 的 skill，使其能够在用户提供效果图、截图、视觉预览图或审批后的静态设计稿时，完成以下工作：

- 从视觉证据中提取产品层面的设计定位、产品气质、全局体验原则与视觉系统规则。
- 输出一份固定结构、可长期引用的全局设计指导文档。
- 在同一个 skill 中冻结亮色与暗色两套主题的具体语义值，而不是只给出方向性描述。
- 为下游 Pencil、Flutter 架构、实现与对齐评审 skill 提供统一输入契约，避免工作流分支。
- 当输入信息不足时，保持输出结构不变，只允许标记缺失状态，不允许省略章节。

## 3. 非目标

- 不负责生成设计预览图；预览探索仍由 `mobile-ui-design-coach` 或 `design-preview-to-pen` 负责。
- 不负责直接重建 Pencil 文件。
- 不负责直接生成 Flutter 页面代码。
- 不负责替代 `flutter-design-freeze-gate` 的审批职责。
- 不负责在下游 skill 中二次改写主题值或重新发明全局设计原则。

## 4. 固定输出契约

本 skill 必须固定产出 3 份核心结果：

1. `global-design-guidelines.md`
2. `light-theme-freeze.yaml`
3. `dark-theme-freeze.yaml`

### 4.1 `global-design-guidelines.md`

该文档必须包含固定元信息与固定章节顺序。

固定元信息：

```yaml
artifact_type: global_design_guidelines
freeze_status: frozen | blocked
source_type: screenshot | preview_comp | multi_screen_pack | mixed
theme_freeze_files:
  light: light-theme-freeze.yaml
  dark: dark-theme-freeze.yaml
```

固定章节：

- `design_position`
- `product_personality`
- `target_users_and_core_scenarios`
- `global_experience_principles`
- `information_hierarchy_principles`
- `layout_and_page_structure_principles`
- `component_system_principles`
- `interaction_behavior_principles`
- `state_and_feedback_principles`
- `content_and_copy_principles`
- `visual_system_rules`
- `light_theme_rationale`
- `dark_theme_rationale`
- `design_prohibitions`
- `engineering_guardrails`
- `downstream_reference_index`

允许的缺失值写法只有：

- `not_provided`
- `not_applicable`
- `needs_confirmation`

不允许删除章节，不允许改名，不允许合并章节。

### 4.2 `light-theme-freeze.yaml` 与 `dark-theme-freeze.yaml`

两份主题配置都必须提供可直接消费的具体值，而不是抽象描述。

固定字段：

- `artifact_type`
- `theme_id`
- `platform_baseline`
- `color_roles`
- `surface_roles`
- `text_roles`
- `icon_roles`
- `border_roles`
- `status_roles`
- `shadow_or_overlay_roles`
- `component_state_roles`
- `contrast_rules`
- `forbidden_overrides`

字段约束：

- 叶子节点必须是具体值，例如 `#RRGGBB`、`rgba(...)`、数字、固定字符串规则。
- 不允许写“同亮色”“自动推导”“实现时决定”“按系统默认”。
- 不允许把暗色主题当作亮色主题的反相结果。
- 即使原图没有完整状态，也必须在本 skill 内补齐全局主题所需的状态值。

## 5. 技能结构

采用“轻主文件 + 多参考文档”的结构：

```text
skills/
  design-preview-to-global-guidelines/
    SKILL.md
    agents/
      openai.yaml
    references/
      image-intake-and-analysis.md
      global-guideline-contract.md
      theme-freeze-schema.md
      value-freeze-strategy.md
      downstream-linking-rules.md
```

各文件职责如下：

- `SKILL.md`：定义触发条件、主流程、硬规则与交付契约。
- `image-intake-and-analysis.md`：定义哪些视觉输入足够触发分析、哪些情况下需要阻塞。
- `global-guideline-contract.md`：定义全局设计指导文档的固定结构。
- `theme-freeze-schema.md`：定义亮暗主题冻结文件的字段与格式。
- `value-freeze-strategy.md`：定义如何从视觉证据推导出稳定的具体值。
- `downstream-linking-rules.md`：定义下游 skill 如何强引用这 3 份产物。

## 6. 下游强引用策略

### 6.1 `flutter-design-freeze-gate`

必须检查：

- `global-design-guidelines.md` 是否存在。
- 固定章节是否齐全。
- `light-theme-freeze.yaml` 与 `dark-theme-freeze.yaml` 是否存在。
- 主题字段是否都是具体值。

如果缺失，则返回 `blocked`，不能放行到 Pencil 或代码阶段。

### 6.2 `design-preview-to-pen`

必须把以下结果视为上游真源：

- `layout_and_page_structure_principles`
- `component_system_principles`
- `visual_system_rules`
- `design_prohibitions`
- `engineering_guardrails`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`

不允许在 Pencil 阶段重定主题角色或视觉层级。

### 6.3 `flutter-pen-to-architecture`

必须优先消费冻结后的主题值，而不是重新从 `.pen` 猜测一遍全局色值。

允许做的只有：

- 映射到 `ThemeData`
- 映射到 `ThemeExtension`
- 映射到组件级 token

不允许改名、重定义语义角色或重算颜色。

### 6.4 `flutter-design-source-control`

必须把这 3 份产物纳入冻结设计源优先级；实现阶段如果想改布局原则、状态原则或主题值，必须回退到设计工作流。

### 6.5 `flutter-design-parity-reviewer`

必须同时依据：

- `.pen`
- `global-design-guidelines.md`
- `light-theme-freeze.yaml`
- `dark-theme-freeze.yaml`

来判断实现是否偏离冻结设计源。

## 7. 方案选择

本次采用“新增独立 skill + 改造下游强引用”的方案，而不是扩展现有 skill，原因如下：

- 现有 `mobile-ui-design-coach` 更适合设计诊断与方向收敛，不适合承担固定契约输出。
- 现有 `design-preview-to-pen` 更适合在预览冻结后进入 Pencil 工作流，不适合承担全局设计指导文档职责。
- 现有 `flutter-pen-to-architecture` 假设输入主要是 `.pen` 或 Pencil 数据，不适合直接承接静态效果图分析。
- 独立 skill 更容易在工作流中被明确路由，也更容易被下游 skill 强引用。

## 8. 验收标准

当用户提供一组静态效果图、预览图或审批截图时，本 skill 应能稳定输出：

- 一份结构固定的 `global-design-guidelines.md`
- 两份字段固定、值具体的主题冻结 YAML
- 明确的 `freeze_status`
- 明确的下游引用索引

并且下游相关 skill 的 `SKILL.md` 中都能看到对这份契约的直接引用或阻塞规则。
