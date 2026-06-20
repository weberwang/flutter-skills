# Effect Image Sheet Atlas Design

**日期**: 2026-06-20
**状态**: 已确认设计，待实现

## 目标

在现有 Flutter 工作流里，把“生成效果图”扩展为“生成效果图的同时生成可切割的 UI sheet 图集”，并且同时覆盖：

1. 全局效果图阶段
2. 模块实现阶段效果图阶段

新增图集必须满足以下硬约束：

1. 图集只包含 UI 层，不包含数据层
2. 图集背景必须透明
3. 图集必须可切割，且切割信息要有稳定清单
4. 图集只是伴生产物，不替代现有“独立 bitmap 资源逐个确认、逐个入 catalog”的主流程

## 设计边界

### 保留现有主流程

不新增新的工作流阶段，不改动现有共享冻结、模块冻结、Pencil 设计源、资源分类、Catalog 复用、逐资源确认这些主门禁。

这次只把 `sheet atlas` 定义成效果图阶段的强制伴生产物：

1. 全局阶段生成共享/页面效果图时，同步生成共享 atlas
2. 模块实现阶段生成模块效果图时，同步生成模块 atlas

### atlas 的角色

atlas 是“预切割 UI 视觉基线”，不是最终实现资源包。

它的职责是：

1. 把当前效果图里的 UI 壳层与稳定视觉层单独输出
2. 提前去掉数据层，避免后续把运行时内容误当成静态资产
3. 提供稳定切片边界和 manifest，支撑后续单资源生成、切割、复用与落盘

它不承担以下职责：

1. 不直接替代最终 bitmap asset 文件
2. 不绕过 `bitmap_required / flutter_native / placeholder_only` 分类
3. 不绕过页面级 bitmap list 确认
4. 不允许把多个最终资源永久打包成一个运行时 atlas 直接消费

## 内容约束

### atlas 允许包含的 UI 层

允许进入 atlas 的内容包括：

1. 导航壳、页头、标签栏、底部壳层
2. 按钮壳、卡片壳、容器壳、输入框壳
3. 图标、插画、徽标、稳定装饰层
4. 空态、错态、加载态中不依赖运行时数据的稳定视觉骨架
5. 固定 CTA 视觉组件
6. 与页面背景解耦后仍可独立复用的 UI 装饰片段

### atlas 禁止包含的数据层

禁止进入 atlas 的内容包括：

1. 用户名、手机号、地址、订单号、聊天正文等运行时文本
2. 列表数据、商品数据、统计数字、价格、图表数据
3. 来自真实业务记录的卡片内容
4. 需要运行时拼装的动态缩略图、头像、封面、图库内容
5. 任何只在真实数据到位后才能成立的业务区域

这些区域必须标记为：

1. `placeholder_only`
2. 或更明确的 `data_excluded_placeholder`

### 背景规则

所有 atlas 输出必须使用透明背景。

原因：

1. 方便后续按切片直接复用到不同运行时表面
2. 避免把页面底色误烘焙进资源
3. 让 UI 壳层切片和页面背景层解耦

只有单个切片在冻结设计里明确要求自带背景时，才允许该切片在后续独立资源阶段保留 baked background；但 atlas 主图本身仍然必须透明。

## 可切割契约

每一张 atlas 都必须同时产出一份 manifest，至少记录：

1. `slice_id`
2. `name`
3. `semantic`
4. `usage_scenarios`
5. `bounds`
6. `background_mode`
7. `slice_type`
8. `cut_safe`
9. `source_scope`
10. `source_page`

其中：

1. `background_mode` 默认必须是 `transparent`
2. `slice_type` 至少支持：
   - `bitmap_required`
   - `flutter_native`
   - `placeholder_only`
3. `cut_safe=true` 表示该切片边界已经足够稳定，后续可以直接切出独立资源

### 可切割的最低要求

一张 atlas 只有满足以下条件，才算“可切割”：

1. 每个候选切片都有明确边界
2. 切片之间不能依赖整页背景才能成立
3. 不能把数据层内容和 UI 壳层混裁在同一个切片里
4. 不能只提供视觉图而不提供切片清单

## 路径约定

共享 atlas 建议路径：

1. `docs/project/assets/atlases/shared/<page-name>/ui-sheet.png`
2. `docs/project/assets/atlases/shared/<page-name>/ui-sheet.manifest.json`

模块 atlas 建议路径：

1. `docs/project/assets/atlases/modules/<module>/<page-name>/ui-sheet.png`
2. `docs/project/assets/atlases/modules/<module>/<page-name>/ui-sheet.manifest.json`

## 对现有工作流的影响

### 全局阶段

在代表页最终效果图和范围内页面效果图生成时，工作流需要同步声明：

1. 页面效果图已生成
2. 对应 UI-only atlas 已生成
3. atlas 为透明背景
4. atlas manifest 已生成并可用于后续切割

### 模块阶段

在实现阶段模块效果图生成时，工作流需要同步声明：

1. 模块页面效果图已生成
2. 对应 UI-only atlas 已生成
3. atlas 为透明背景
4. atlas manifest 已生成并可用于后续切割

### 与资源生成流的关系

atlas 不替代 `asset-atlas-flow` 的后续职责，而是为它补一份更稳定的输入。

后续资源流仍然需要：

1. 先做 `bitmap_required / flutter_native / placeholder_only` 分类
2. 先查 `global-asset-catalog`
3. 逐页确认 bitmap list
4. 每个最终 bitmap asset 独立生成、独立确认、独立落盘

atlas 只能帮助“更稳定切”，不能帮助“跳过确认”。

## 需要修改的文档范围

本次实现应最小化落在这些位置：

1. `README.md`
2. `skills/flutter-workflow-orchestrator/SKILL.md`
3. `skills/flutter-workflow-orchestrator/references/asset-atlas-flow.md`
4. `skills/flutter-workflow-orchestrator/references/routing-rules.md`
5. `skills/flutter-workflow-orchestrator/references/workflow-states.md`
6. `skills/flutter-workflow-orchestrator/references/hard-rules.md`
7. `skills/flutter-workflow-orchestrator/references/global-asset-catalog-contract.md`

## 测试策略

至少补充一组规则回归测试，验证以下约束不会丢失：

1. 全局效果图阶段必须同步生成共享 UI atlas
2. 模块效果图阶段必须同步生成模块 UI atlas
3. atlas 只包含 UI 层，不包含数据层
4. atlas 背景必须透明
5. atlas 必须附带可切割 manifest

## 风险与取舍

### 为什么不新增阶段

不新增阶段是为了保持当前状态机稳定，避免把“伴生产物”错误升级成新的流程门禁中心。

### 为什么 atlas 不直接替代最终 bitmap asset

如果 atlas 直接变成最终资源源头，会和当前仓库“逐资源确认、逐资源 catalog 化”的规则发生更大冲突，改动面会明显扩大。

### 为什么背景必须透明

如果 atlas 背景不透明，后续切片会把页面底色、氛围色或整页底图一起带走，导致资源复用能力下降，也更难判断哪些区域其实应归类为 `flutter_native`。

## 本次实现完成标准

当以下条件同时成立时，这次改动算完成：

1. 主 README 与 orchestrator 文档都明确写入“效果图同步生成 UI-only 透明 atlas”
2. atlas 只保留 UI 层、不含数据层的规则已进入主技能文档和参考文档
3. 可切割 manifest 约束已进入主技能文档和参考文档
4. 共享阶段与模块阶段都被明确覆盖
5. 自动化测试已覆盖上述关键规则
