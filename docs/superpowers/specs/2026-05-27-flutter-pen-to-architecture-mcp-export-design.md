# flutter-pen-to-architecture MCP 导出重构设计

## 1. 背景

当前 `flutter-pen-to-architecture` 已经补充了图片导出能力，但这套能力建立在仓库内脚本之上：

- `scripts/export_pen_assets.mjs` 负责解析 `.pen`、导出图片并在必要时读取 MCP 资源清单回退
- `scripts/ensure_flutter_assets.mjs` 负责修改 Flutter 项目的 `pubspec.yaml`

这条链路虽然能工作，但它与 `Pencil MCP` 已提供的设计节点读取与导出能力形成了双轨：

- 一条链路是技能通过 `Pencil MCP` 做设计结构分析
- 另一条链路是仓库脚本直接处理 `.pen` 和本地文件

这种双轨会带来额外复杂度：

- 导出行为不再完全依赖 `Pencil MCP`
- 技能文档与实现边界不够统一
- `.pen` 解析、回退策略、覆盖策略需要在仓库里长期维护
- `pubspec.yaml` 自动修改让 skill 从“分析与导出流程”扩大成了“本地工程修改工具”

本次重构目标是把导出能力彻底收口到 `Pencil MCP`，并去掉本地脚本自动接入 Flutter 资源配置的职责。

## 2. 目标

本次重构完成后，`flutter-pen-to-architecture` 应满足以下目标：

- 图片导出只允许通过 `Pencil MCP` 完成
- 图片导出单位从“`.pen` 包内原始资源文件”切换为“设计节点”
- skill 输出继续稳定包含图片资源导出结果、映射关系与 Flutter 接入建议
- 不再通过仓库脚本自动修改 `pubspec.yaml`
- 不再保留“脚本导出”和“MCP 导出”双轨方案

## 3. 非目标

本次重构不包含以下内容：

- 不生成 Flutter 页面代码或组件代码
- 不新增 Dart 侧资源常量文件生成能力
- 不保留旧脚本兼容层或过渡入口
- 不把整页默认导出为位图
- 不通过 skill 自动重命名 `export_nodes` 生成的文件

## 4. 设计原则

### 4.1 单一路径

图片导出只走 `Pencil MCP`：

- 结构读取使用 `batch_get`、`snapshot_layout`、必要时 `get_variables`
- 导出使用 `export_nodes`

不再允许 skill 依赖本地脚本解 `.pen` 压缩包或读取 MCP manifest。

### 4.2 节点导出优先于资源提取

导出目标不是“尽可能提取所有内嵌图片”，而是“导出对 Flutter 还原有独立价值的设计节点”。

这意味着导出行为以设计语义和实现价值为中心，而不是以压缩包内容为中心。

### 4.3 技能负责流程与判断，不负责本地自动改造

`flutter-pen-to-architecture` 继续负责：

- 识别输入
- 定位可导出节点
- 调用 MCP 导出
- 组织输出映射表
- 给出 Flutter 接入建议

但不再负责：

- 自动修改 `pubspec.yaml`
- 自动生成重命名后的业务文件名
- 自动修复文件冲突

### 4.4 输出结构稳定

虽然底层实现从脚本切换到 MCP，但 skill 的最终输出仍需保持稳定、可消费、可交接，避免下游 agent 因为实现切换而失去一致的结果结构。

## 5. 重构后的能力边界

### 5.1 输入识别

skill 接收以下主要输入：

- `.pen` 文件路径
- Flutter 项目根目录
- 可选的目标节点范围、页面范围或候选区域描述

skill 不再把 `.pen` 当作 ZIP 自行解析，只把它作为 `Pencil MCP` 的输入源。

### 5.2 节点定位

skill 通过 `Pencil MCP` 完成候选节点定位：

- 使用 `batch_get` 读取页面结构、候选节点与可复用组件
- 使用 `snapshot_layout` 辅助判断层级、尺寸、裁剪关系和节点边界
- 使用 `get_variables` 辅助理解主题变量、颜色和语义样式，但不直接决定导出节点

节点定位的结果是一组“值得导出的节点 ID”，而不是一组原始资源文件路径。

### 5.3 MCP 导出

skill 使用 `export_nodes` 将选中的节点直接导出到：

```text
<projectRoot>/assets/images/
```

导出结果以 `export_nodes` 返回的绝对路径为准，并在最终输出中整理成 Flutter 可消费的相对路径。

### 5.4 Flutter 接入提示

skill 只检查与提示，不自动修改：

- 是否存在 `pubspec.yaml`
- 是否已经声明 `assets/images/`
- 如果未声明，应补充的最小片段是什么
- 哪些资源建议直接通过 `Image.asset(...)` 使用

## 6. 导出规则与节点筛选

### 6.1 适合导出的节点

默认优先导出以下节点：

- 品牌插画
- Banner 主视觉
- 头像、商品图、内容配图
- 复杂装饰图形
- 明显不适合通过 Flutter 原生布局与样式低成本还原的视觉元素

### 6.2 不适合默认导出的节点

默认不导出以下节点，除非用户明确要求高保真位图保留：

- 普通按钮
- 输入框
- 纯色背景块
- 简单分割线
- 可直接通过 Flutter 组件与布局表达的基础界面元素

### 6.3 优先级

节点筛选顺序如下：

1. 明确的 `image` 节点
2. 由多个图形组成、但 Flutter 复刻成本明显偏高的 `group` 或 `frame`
3. 业务上明确要求高保真的整块视觉区域

### 6.4 页面与节点的关系

默认不要整页导出。

优先导出页面中的独立图片节点或局部视觉组合节点。只有当某个视觉区域本身不可拆、拆开后失去还原价值时，才允许导出 `group` 或 `frame` 级复合节点。

### 6.5 导出格式

默认导出格式建议为 `png`，原因如下：

- Flutter 中直接消费最稳定
- 对透明背景与复杂插画更稳妥
- 更适合作为跨页面复用素材

在没有特殊理由时，不把 `jpeg`、`webp` 作为默认导出格式。

### 6.6 导出倍率

默认使用较高导出倍率，确保移动端显示时不会出现明显失真。具体倍率以 `export_nodes` 调用参数为准，但 skill 文档应明确高质量导出的意图，而不是要求执行者自行猜测。

## 7. 文件命名与映射约定

### 7.1 MCP 实际落盘

`export_nodes` 默认按节点 ID 写出文件。skill 不在本次重构中自动重命名这些文件。

### 7.2 技能输出中的命名建议

虽然不自动重命名，skill 仍需在输出中提供：

- 当前落盘文件名
- Flutter 相对路径
- 建议业务命名

例如：

- MCP 实际导出：`assets/images/node_17a2c.png`
- 建议业务命名：`home_banner.png`

### 7.3 映射表以节点为中心

映射表的核心不再是“原始资源文件来自哪里”，而是：

- 哪个节点被导出了
- 为什么导出这个节点
- 导出结果在 Flutter 中如何使用

## 8. 覆盖与冲突策略

重构后不再沿用旧脚本中“默认覆盖”的硬编码假设。

覆盖与重名行为应遵循以下原则：

- 以 `export_nodes` 实际导出行为为准
- skill 输出必须显式记录是否存在重名风险
- 如发生冲突，输出中需要给出保留或替换建议

在文档层面，不应先验写死 MCP 的覆盖行为，必须在真实 smoke 验证后再将观察结果固化到文档措辞中。

## 9. 输出契约调整

### 9.1 固定输出小节

最终输出保留原有架构分析主干，同时固定包含以下 3 个小节：

1. `图片资源导出结果`
2. `图片资源映射表`
3. `Flutter 资源接入结果`

### 9.2 图片资源导出结果

该小节至少包含：

- 导出的 `.pen` 文件
- 导出目标目录
- 导出格式
- 导出的节点数量
- 导出成功的文件列表
- 未导出的候选节点及原因

这一节强调“本次导出了哪些设计节点”，而不是“从压缩包中提取了哪些资源”。

### 9.3 图片资源映射表

建议字段调整为：

- `节点 ID`
- `节点名称`
- `导出文件绝对路径`
- `Flutter 相对路径`
- `建议业务命名`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

### 9.4 Flutter 资源接入结果

该小节至少包含：

- 是否找到 `pubspec.yaml`
- 是否检测到 `assets/images/` 声明
- 如果未声明，建议补充的最小配置片段
- 建议代码引用方式，例如 `Image.asset('assets/images/xxx.png')`

此处只给出检查结果和接入建议，不自动修改工程文件。

## 10. 仓库结构调整

### 10.1 需要删除的文件

以下文件在重构后应删除：

- `skills/flutter-pen-to-architecture/scripts/export_pen_assets.mjs`
- `skills/flutter-pen-to-architecture/scripts/ensure_flutter_assets.mjs`
- `skills/flutter-pen-to-architecture/scripts/tests/test_export_pen_assets.test.mjs`
- `skills/flutter-pen-to-architecture/scripts/tests/test_ensure_flutter_assets.test.mjs`
- `skills/flutter-pen-to-architecture/scripts/package.json`
- `skills/flutter-pen-to-architecture/scripts/package-lock.json`

### 10.2 需要更新的文件

以下文件需同步更新，确保文档、agent 入口与输出契约一致：

- `skills/flutter-pen-to-architecture/SKILL.md`
- `skills/flutter-pen-to-architecture/agents/openai.yaml`
- `skills/flutter-pen-to-architecture/references/asset-extraction-and-mapping.md`
- `skills/flutter-pen-to-architecture/references/pen-input-contract.md`
- `skills/flutter-pen-to-architecture/references/output-blueprint.md`
- `docs/superpowers/plans/2026-05-26-flutter-pen-to-architecture-assets.md`
- `docs/superpowers/specs/2026-05-26-flutter-pen-to-architecture-assets-design.md`

## 11. 工作流改写方向

`SKILL.md` 的工作流应从“脚本导出 + 脚本接入”改写为“Pencil MCP 分析 + 节点导出 + 接入提示”：

1. 识别 `.pen` 与 Flutter 项目根目录
2. 通过 `Pencil MCP` 定位可导出节点
3. 使用 `export_nodes` 直接导出到 `assets/images/`
4. 整理导出结果与映射表
5. 检查 `pubspec.yaml` 状态
6. 输出接入建议、而不是自动修改
7. 继续完成 token、主题、组件拆解与页面架构分析

## 12. 验证方式调整

### 12.1 放弃脚本级单测

由于本次重构明确删除本地导出脚本和接入脚本，不再保留 `node:test` 风格的脚本单测。

### 12.2 改为 MCP 流程验收

skill 文档应显式要求执行者完成最小 smoke 流程：

1. `get_editor_state(include_schema: true)`
2. 使用 `batch_get` 或 `snapshot_layout` 选出候选节点
3. 使用 `export_nodes` 导出到目标 Flutter 项目的 `assets/images/`
4. 确认 MCP 返回的绝对路径确实存在
5. 最终输出必须包含固定的图片导出、映射与接入结果小节

### 12.3 验收标准

重构完成后，应满足以下验收标准：

- skill 主流程中不再出现“解 `.pen` ZIP 导图”或“读 MCP manifest 回退”的描述
- 图片导出明确依赖 `Pencil MCP` 的 `export_nodes`
- 输出映射表以节点 ID、节点名称、导出文件与 Flutter 路径为核心
- `pubspec.yaml` 只做检查与提示，不做自动修改
- 该 skill 目录下不再依赖本次新增的 Node 导出脚本和测试骨架

## 13. 风险与约束

### 13.1 文件名技术化

`export_nodes` 默认使用节点 ID 作为文件名，落盘文件名会偏技术化，不利于直接进入业务代码。

对应策略：

- 输出中保留 `建议业务命名`
- 由后续实现者决定是否手动重命名

### 13.2 覆盖行为不应先验假设

旧脚本可以显式决定覆盖行为，但 MCP 导出行为需要以真实工具表现为准。

对应策略：

- 在真实 smoke 验证前，不把覆盖行为写死进规则
- 文档只要求显式记录冲突与建议

### 13.3 自动化程度下降

删除接入脚本后，`pubspec.yaml` 的补齐需要人工或下游 agent 执行。

对应策略：

- 在结果中提供最小配置片段
- 明确缺失状态和后续动作

## 14. 结论

本次重构不是把脚本换一种实现，而是把 `flutter-pen-to-architecture` 的图片导出能力从“仓库内脚本能力”收口为“Pencil MCP 驱动的技能流程能力”。

重构完成后：

- 导出路径更单一
- 技能边界更清晰
- 文档、能力和执行方式更一致
- 后续 agent 不需要再在脚本导出和 MCP 导出之间做路径选择
