# flutter-workflow-orchestrator

`flutter-workflow-orchestrator` 是 Flutter 技能链的总编排器。它负责维护唯一 workflow state，锁定当前阶段、下一个 skill、允许的状态变更，并阻止任何绕过门禁的推进。必要时可以把这些状态落成运行时产物，但它们不属于 skill 的稳定资源。

## 当前主流程

```mermaid
flowchart LR
    A["requirements_brainstorming"] --> B["prd_ready"]
    B --> C["technical_baseline_ready"]
    C --> D["shared_taste_direction"]
    D --> E["product_direction_confirmed"]
    E --> F["global_effect_image_pilot_ready"]
    F --> G["global_effect_images_ready"]
    G --> H["stitch_design_source_ready"]
    H --> I["global_guidelines_frozen"]
    I --> J["design_freeze_ready"]
    J --> K["module_impl_docs_ready"]
    K --> L["module_design_frozen"]
    L --> M["impl_rd_ready"]
    M --> N["architecture_ready"]
    N --> O["project_initialized"]
    O --> P["bootstrap_code_ready"]
    P --> Q["implementing"]
    Q --> R["module_done"]
```

## 关键收敛

1. Stitch 是唯一默认设计源。效果图只是视觉基线，不再把效果图本身当结构化设计源。
2. 全局视觉设计必须先头脑风暴，再确认最终方向，然后才允许出效果图。
3. 出效果图之前必须先同意并冻结统一公共壳，至少包括 `app-shell` / `root-shell`、导航宿主、顶层 tabs/header/footer 和 shell 级 overlay 语言。
4. 效果图采用代表页优先：先出 1 张代表页，等你确认后再生成其余页面。
5. 效果图统一存放在全局目录 `docs/rd/`，不再要求落到模块目录。
6. `project_initialized` 只表示创建目录骨架和项目内 `skills/flutter-dev/`，不包含 bootstrap 代码。
7. `bootstrap_code_ready` 单独成阶段，负责 app 入口、app shell、共享启动 wiring、根路由宿主等全局公共代码。
8. `implementing` 阶段必须先通过 `@superpowers` 的 `Spec`，再通过 `Plan`，之后默认并行实现。
9. `parity_reviewed` 已移除，代码完成后的视觉对齐改为人工检查。
10. `workflow record` 和 `superpowers execution trace` 属于运行期过程产物，不再作为 skill 的稳定文件长期维护。

## 阶段说明

### `requirements_brainstorming`

输入还是原始需求、半成品 brief 或一句话想法。这里先做需求头脑风暴、问题台账、阻塞问题消解，之后才允许生成 PRD。

### `prd_ready`

PRD 已存在，但还不能直接进设计或代码。下一步先用 `flutter-prd-rd-writer` 产出全局技术基线。

### `technical_baseline_ready`

全局技术基线已确定，包括包栈、后端协作、交付边界、存储/网络基线等。下一步进入全局视觉设计头脑风暴。

### `shared_taste_direction`

这里是全局视觉设计头脑风暴阶段。要产出产品气质、信息密度、层级、排版、色彩、组件家族、CTA 姿态、反模板化规则，以及验证平台基线。

这个阶段结束后，还不能直接出图，必须先：

1. 同意统一公共壳
2. 再确认最终产品设计方向

### `product_direction_confirmed`

你已经基于 PRD、技术基线和全局视觉设计头脑风暴结果，明确确认最终产品设计方向。此后才允许进入效果图生成。

### `global_effect_image_pilot_ready`

已生成 1 张代表页浅色效果图，正在等待你确认或提出调整。`--auto` 到这里也必须停。

### `global_effect_images_ready`

代表页已确认，且所有范围内页面的浅色效果图都已生成并批准。只有到这里，才允许进入 Stitch 结构化设计源阶段。

### `stitch_design_source_ready`

所有批准后的页面效果图已经进入 Stitch，并生成或校验了结构化设计源包。这里必须先冻结 `stitch_project_mode` 和 `stitch_project_id`。

进入 Stitch 前先问你二选一：

1. 新建 Stitch 项目
2. 使用已有 Stitch 项目

如果没有明确模式，流程必须中断。页面级 Stitch 设计在子代理中执行，最多 6 个页面并行。

### `global_guidelines_frozen`

全局共享设计规则、主题冻结值、共享组件边界、效果图策略等都已经冻结，但这还不是模块冻结。

### `design_freeze_ready`

共享设计冻结审批准备态。这里要保证层级、排版、对比度、CTA、状态覆盖和高保真约束都已经明确。

### `module_impl_docs_ready`

模块拆分和模块细化已经合并成一步，直接产出可执行级别的 `impl.md`。不再要求单独的模块 `ui/ux` 文档，也不再保留单独 refinement 阶段。

### `module_design_frozen`

当前模块的 `impl.md`、Stitch 设计源包、高保真显示层约束、状态矩阵、视觉证据都已冻结。

### `impl_rd_ready`

模块实现文档已经可直接消费，且明确引用冻结后的 Stitch 设计源和共享基线。

### `architecture_ready`

冻结设计已经被翻译成 Flutter 可实现的 token、组件边界、屏幕结构、位图/原生绘制决策、显示层决策表。

### `project_initialized`

这里只做目录初始化：

1. `flutter create` 干净工程
2. 去掉 demo
3. 创建目录骨架
4. 生成项目内 `skills/flutter-dev/`

这里允许的产物只有：

1. 目录
2. 最小依赖与插件基线
3. 非运行时占位文件或契约占位
4. 项目内 `flutter-dev` 约束

这里不允许偷跑：

1. bootstrap 代码
2. app shell
3. router host / redirect
4. shared wiring
5. 页面代码
6. 业务实现

### `bootstrap_code_ready`

这是全局骨架代码阶段。这里才落：

1. app 入口
2. root app shell
3. router host / redirect policy
4. 全局 DI 或 provider scope 入口
5. storage / logging / error mapping 等共享启动 wiring
6. 模块实现会依赖的公共代码基线

### `implementing`

实现入口固定为：

1. `@superpowers` 产出 `Spec`
2. `@superpowers` 产出 `Plan`
3. 按 `Plan` 默认并行执行独立工作包

显示层实现前，如果存在对应页面效果图，必须先通过 `$image-to-code` 检查页面图。Stitch 还原时允许下载的图片资产可以直接使用，不强制再生。

### `module_done`

模块代码已落地，且人工视觉检查已经通过。

## `--auto` 会推进到哪里

`--auto` 会一直推进到“实现边界之前”，不会直接开始代码实现。

它会自动做这些事：

1. 从需求/PRD推进到技术基线
2. 推进到全局视觉设计头脑风暴
3. 在你尚未确认最终设计方向时停下
4. 你确认后，生成 1 张代表页效果图
5. 再次停下，等待你确认这张代表页
6. 代表页确认后，再生成剩余页面效果图
7. 继续推进 Stitch、共享冻结、模块 `impl.md`、模块冻结、实现前文档、架构、项目初始化、bootstrap code
8. 当所有目标模块都达到实现边界时停止

`--auto` 不会做这些事：

1. 不会跳过全局视觉设计头脑风暴
2. 不会跳过“最终产品设计方向确认”
3. 不会跳过“代表页效果图确认”
4. 不会越过 blocker
5. 不会直接进入 `implementing`
6. 不会直接开始代码实现

## 设计源与高保真还原

### 为什么不再直接用效果图做设计源

只用效果图不稳定，原因有三个：

1. 效果图缺结构语义，难以稳定映射到组件层级、状态矩阵、滚动语义和 overlay 规则。
2. 多页面风格一致性容易靠主观猜测补齐，代码阶段会逐页漂移。
3. 高保真还原时，复杂区域如果只靠一张图，最后往往只能“像”，不能“准”。

### 为什么改成 Stitch 为唯一设计源

更优，前提是流程门禁严格：

1. 先确认全局视觉方向
2. 先确认代表页
3. 再补全所有页面效果图
4. 再把整套页面送进 Stitch
5. 冻结 `stitch_project_id`
6. 用 Stitch 结构化产物驱动冻结、架构和实现

这样效果图负责“视觉基线”，Stitch 负责“结构化实现源”，职责更清楚。

### 如何保证所有页面统一风格

统一风格依赖三层约束一起成立：

1. `shared_taste_direction`：先冻结全局视觉原则
2. `global_effect_images_ready`：所有页面共享同一批批准后的效果图基线
3. `stitch_design_source_ready`：所有页面进入同一个冻结的 Stitch 项目和设计源包

如果缺任意一层，后续代码还原都会漂。

### 高保真显示层最重要，流程里怎么保证

保证方式是硬门禁，而不是“开发时注意一下”：

1. 模块冻结前先检查高保真视觉契约
2. `flutter-uiux-to-architecture` 必须产出 region 级决策
3. 显示层实现前跑 display preflight
4. 对应页面图存在时，先走 `$image-to-code`
5. 代码完成后交给人工视觉检查

## Stitch 规则

1. Stitch 是唯一默认结构化设计源
2. 进入 Stitch 前必须先确认是新建项目还是已有项目
3. `stitch_project_id` 一旦冻结，后续不能随便改
4. 进入 Stitch 之前，必须先冻结一份全局设计母版 packet，所有页面都基于这份 packet 展开
5. Stitch 页面设计在子代理中执行，最多 6 个页面并行
6. 页面子代理只允许展开页面，不允许私自重定义全局风格、CTA 模型、导航壳层或核心组件家族
7. 还原 Stitch 设计稿时，允许下载批准后的图片并直接作为项目资产使用
8. merge 阶段必须检查全局统一性：token、排版层级、组件家族、shell、CTA、密度、图片处理姿态必须一致
9. 不再在仓库文档中记录任何 Stitch MCP 配置或 API key

## 平台记录规则

`platform_baseline` 和真实验证平台必须分开记录。

默认规则是：

- 只要用户没有显式批准别的基线，移动端设计规范就必须严格遵循 `iOS HIG`
- 这里的“严格遵循”至少覆盖 safe area、触控热区、导航、反馈、可读性、破坏性操作和可访问性
- 不能把它弱化成“接近 Apple 风格”或“参考 HIG”

例如：

- `ios_hig` 是行为/设计基线
- `android_emulator`
- `windows_desktop`
- `web_browser`

后面这些属于显式 `platform_identifier`，进入冻结、架构、实现准备时必须明确，不能只写成“移动端”或“桌面端”。

## 默认路由

1. 需求到 PRD：`flutter-workflow-orchestrator` 内部 requirements-to-PRD 流
2. PRD 到技术基线：`flutter-prd-rd-writer`
3. 全局视觉设计头脑风暴：`flutter-taste-router`
4. 共享冻结产物：`design-preview-to-global-guidelines` -> `flutter-design-freeze-gate`
5. 模块可执行文档：`flutter-rd-module-splitter`
6. 设计变更控制：`flutter-design-source-control`
7. Flutter 架构：`flutter-uiux-to-architecture`
8. 目录初始化：`flutter-init`
9. 模块实现：`@superpowers` -> `Spec` -> `Plan` -> 并行实现

## 硬规则

1. 不要跳过 PRD。
2. 不要跳过全局技术基线。
3. 不要跳过全局视觉设计头脑风暴。
4. 不要在确认最终设计方向之前生成效果图。
5. 不要在代表页确认前生成剩余页面效果图。
6. 不要在未确认 Stitch 项目模式和 `stitch_project_id` 前进入 Stitch。
7. 不要把效果图直接当最终结构化设计源。
8. 不要把 `project_initialized` 误解成“项目骨架代码已经完成”。
9. 不要在 `bootstrap_code_ready` 之前开始模块实现。
10. 不要让 `--auto` 进入 `implementing`。
