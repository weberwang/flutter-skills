# Phaser → Flutter 工作流迁移与合并方案

版本：2026-09-05

文档状态：迁移提案。本文整理如何把 Phaser 工作流中有价值的控制与视觉方法迁入当前 Flutter 技能链；目标不是移植 Phaser 应用，也不是建设新的调度 App。本文不修改现有 skill、脚本、schema 或项目状态，也不代表下文建议已经实现。

## 1. 读法与范围

本文把信息分为两类：

- **当前事实**：能在本仓库 README、skill、reference 或脚本中直接核对的规则。
- **迁移建议**：为把 Phaser 工作流中有价值的控制与视觉方法迁入 Flutter 技能链而新增的页面、映射、产物或门禁。建议必须在后续任务中更新对应的权威文件后才可以执行。

原 Phaser 文档只作为可选参考输入。它提到的控制状态、字段、编号、V 阶段、图片流程或路径，若没有当前 Flutter 文件或已核验的源项目实现支持，均不能写成 Flutter 现状，也不能被前端界面默认为有效 schema。

本方案的边界如下：

1. 主流程以当前 `flutter-app-orchestrator` 为入口，按需加载产品、UX/UI、布局、草图、高保真、资产、技术、实现、审核和发布能力。
2. 风险仍使用 `light`、`standard`、`high`、`release` 四级；八字段任务契约仍是唯一交接格式。
3. 默认使用当前 checkout、一个写入者、顺序执行；分支、worktree、提交、PR、并行写入、外部写入、发布和真机验收都必须单独获得用户明确授权。
4. `F0`、`F1`、`F2`、`F3` 只按当前 Flutter 审核漏斗使用：F0 执行、F1 分诊、F2 独立只读、F3 收敛。它们不是产品阶段、页面阶段或运行时状态。
5. 本文不引入 Phaser 专属工作项状态机、操作级别编号、G 门、数据库队列、租约状态或由 JSON 驱动的隐式状态机。需要持久事实时，沿用当前工件和审计规则。
6. 视觉链条中的确认、测试等级选择和高影响操作授权彼此独立，不能用“继续”“已完成”或一次截图互相替代。

## 2. 合并后的目标流程

这是把 Phaser 工作流中有价值的控制与视觉方法并入 Flutter 技能链的主线，用于形成可核对的产品语义、Flutter 布局合同和运行证据；它不要求迁移 Phaser 应用，也不建立调度 App，顺序如下：

```text
迁入 Phaser 工作流方法的产品语义与范围
  → 技术基础与模块边界
  → 页面语义合同
  → phase: sketch 的 layout-spec
  → 生产 Flutter 骨架中的 Code Sketch
  → 按 Full / Lightweight / Reuse 选择结构证据并独立审阅
  → 高保真单图生成、用户冻结
  → 冻结目标与合同回对
  → 状态分析与 data / UI / asset ownership 拆解
  → 全元素拆解确认图与独立确认
  → 从已确认拆解推导唯一布局
  → 布局层级确认图与独立确认
  → 必要的固定视觉资产与资产证据
  → 同一 layout-spec 升级为 phase: fidelity
  → 同一生产骨架还原并实现
  → F0 验证、F1 分诊、触发的 F2、F3 收敛
  → 全部获授权范围的集成
  → 按需进入发布准备与发布授权
```

这条主线有三个必须分开的关系：

- `phase: sketch` 负责结构、语义关系和响应式合同；它不是最终几何蓝图。
- 高保真冻结后，拆解确认先于布局确认；布局由确认的元素推导出唯一方案，不是重新设计或多方案投票。
- `phase: fidelity` 在同一布局文件和同一生产骨架上还原目标；低保真截图进入高保真后失效或由新的证据替代。

页面没有结构或视觉变化时，不能因为参考了 Phaser 工作流就强行走完整 UI 链。页面复用、普通功能、服务端或发布任务按第 8 节分流。

## 3. 当前 Flutter 工作流事实

### 3.1 入口、拓扑和工件

当前入口规则见 [`flutter-app-orchestrator/SKILL.md`](flutter-app-orchestrator/SKILL.md)。它要求先预检仓库、已有决策、依赖、健康服务和项目原生命令，再按风险选择最小流程。

风险只改变验证和审核深度，不改变默认拓扑。风险分级、快照和平台证据规则见 [`task-risk-tiers.md`](flutter-subagent-delivery/references/task-risk-tiers.md)。普通单代理任务在对话中传递八字段，不创建占位 brief、账本或运行时状态。

工件只有在对应阶段真实发生并需要决策或可复现证据时才创建。工件条件和唯一权威位置见 [`artifacts.md`](flutter-app-orchestrator/references/artifacts.md)。一个事实只保留一个权威位置，其他页面只引用路径。

### 3.2 产品、技术和模块基础

新产品范围需要产品 brief、MVP 非目标、用户故事和可观察验收；进入商业流程时还需要 grilling log 中的共享理解确认。规则见 [`flutter-product-spec/SKILL.md`](flutter-product-spec/SKILL.md)。已有 Flutter 项目应先读取现状，不把 Phaser 目录结构直接当作 Flutter 模块边界。

技术设计先读取产品和 UX 输入，只选择 MVP 真正需要的状态、路由、持久化、网络、认证、依赖和平台能力。它必须说明模块、数据 ownership、跨模块合同、服务边界、迁移回退和分层平台验证，规则见 [`flutter-tech-design/SKILL.md`](flutter-tech-design/SKILL.md)。

已有项目跳过不必要的初始化；新项目和依赖能力按 FVM 与能力档处理。`flutter-project-init` 要求所有 Flutter/Dart 命令经过 `fvm flutter` 或 `fvm dart`，并生成反映实际依赖的项目本地 `flutter-dev` skill。它不因初始化而默认安装 Riverpod、Freezed、ScreenUtil 或 JSON 生成器。

模块、业务流级别和页面交互顺序在模块首次可实施时再细化。实施计划遵守 [`implementation-plan-template.md`](flutter-implementation-plan/references/implementation-plan-template.md)；不为了迁移外观预先创建没有事实支撑的模块或任务文件。

### 3.3 页面结构链

UX/UI Lead 负责页面语义、视觉方向、无障碍和设计交接，不写页面代码。页面语义合同至少覆盖范围、内容优先级、状态、交互结果、导航、滚动 owner、断点重排、文本增长、SafeArea/键盘/系统栏、无障碍以及 data/UI/asset ownership。

自适应页面每页只维护一个 `layout-spec.yaml`。`phase: sketch` 先描述 regions、anchors、breakpoints、content、system avoidance、scroll、text behavior、overlays、implementation、invariants、implementation signals 和 evidence matrix；它不得预填 `critical_alignments` 或 `parity_cases`。

Code Sketch 在生产骨架、生产路由和真实状态模型中实现中性结构。稳定语义节点使用 Flutter key；结构测试验证关系、状态、滚动、断点、文本增长和系统避让。`Stack`/`Positioned` 只用于已登记的真实叠层，不能把目标图绝对坐标直接变成页面实现。

Code Sketch 级别由页面决策选择：Full 适用于核心路径、新颖交互、复杂状态或复杂响应式；Lightweight 适用于常规页面；Reuse 适用于已批准模式的直接复用。级别标准见 [`code-sketch-level-standard.md`](flutter-code-sketch/references/code-sketch-level-standard.md)。级别不会删除语义合同或布局规格。

### 3.4 高保真和布局事实

Code Sketch Review 通过后才可以生成高保真页面目标。当前图、brief、prompt 和评审草稿在冻结前保持临时；用户明确确认后才持久化目标及 SHA-256。当前目标图输出要求精确 `780 x 1688 px`，其常用逻辑参考是 `390 x 844`、`2x`。

根据本轮用户决定，每个具体页面/状态目标每轮只生成一张高保真图。效果不好时，代理不得自行批量或反复重生；只有用户明确要求，才按用户反馈重新生成一张并再次确认。多页面或多状态分别生成各自的一张，不构成同一目标的多候选。现有 [`flutter-hifi-mockup/SKILL.md`](flutter-hifi-mockup/SKILL.md) 仍写有“默认一张、探索时两到三张”，属于待同步冲突，本文不冒充该 skill 已经修改。

冻结目标必须与已审语义合同和 sketch spec 回对。若范围、状态、导航、滚动 owner、断点、无障碍或 ownership 改变，必须回到语义/草图阶段更新并重审。

高保真阶段把同一个 `layout-spec.yaml` 升级为 `phase: fidelity`，增加关键对齐和 parity case。每个 parity case 绑定一个明确 viewport、state、orientation、target SHA、候选代码内容身份和同视口双方截图。

当前关键对齐容差是 `<= 1 logical px`。它是关键关系的容差，不是整屏逐像素相等承诺。文字、Logo 和不规则轮廓还要区分容器中心与可见内容的 optical center；未解决的光学偏移会阻断视觉通过。

多设备、多方向和不同高度必须按技术合同和布局合同分别验证。`780 x 1688` 只说明当前高保真目标图规格，不能据此宣称所有屏幕尺寸都达到 parity。

### 3.5 资产与非资产事实

资产分类先按 ownership，再决定是否需要 bitmap。运行时 data 包括文本、数值、日期、图表值、进度、用户内容、远程媒体、运行时头像、地图、二维码和签名；runtime UI 包括容器、控件、布局、mask、renderer、确定性形状和 Flutter 可还原的效果；fixed visual 才可能需要 bitmap。权威标准见 [`bitmap-decomposition-standard.md`](flutter-asset-atlas/references/bitmap-decomposition-standard.md)。

页面有固定视觉资产时，`asset-manifest.md` 是 ownership、覆盖审计、编号映射、生产决定和保真结论的唯一权威；design decision 只链接它。若页面确实没有 bitmap 或导出视觉资产，可在适用清单中记录精确文本 `N/A: no bitmap or exported visual assets`，并关闭资产分支，不伪造资产门。

固定视觉生产可以按实际合同选择 `reuse`、`adapt`、`variant`、`new generation`、`atlas` 或经明确批准的 target extraction。不得从代表性 runtime data 导出位图，也不能因为实现方便把所有 Flutter UI 变成一张截图或一组位图。

透明资源优先使用原生透明输出。若确需 mask 或背景处理，应按当前资产合同记录方法、边缘和目标背景检查；不把 Phaser 来源中可能存在的“一次强制去背”规则迁入 Flutter。ImageGen、切片和输出格式仍以实际冻结合同为准。

### 3.6 证据、快照和验证事实

当前审核漏斗见 [`review-funnel.md`](flutter-quality-review/references/review-funnel.md)：

- F0：实现者执行获授权的项目原生分析、测试、构建、审计或回归命令。
- F1：Controller 检查范围、风险、验收、输入指纹和 F0 证据，并选择触发通道。
- F2：与 producer 不同的独立只读审阅者检查被触发的 Product、QA、technical、visual 或 Release 事实。
- F3：Controller 收敛有效通道、阻塞和当前层级集成条件。

`workflow:snapshot` 输出 `baseRef`、`baseSha`、排序后的变更、每个当前工作树文件的 blob ID 和 `snapshotId`。`snapshotId` 是 `sha256:<64 位摘要>`，包含未跟踪文件，命令只写 stdout，不保存运行时状态。F1/F2 以它绑定整次审核范围；已有且获授权的提交才补充 commit SHA。

`layout-spec` 的 `candidate_code_sha` 字段当前由 validator 检查为 40–64 位小写 commit/content SHA。它不等于必须有提交，也不等于 `workflow:snapshot` 的 `sha256:` 字符串。当前脚本没有替迁移定义“代码候选边界”。

建议后续为候选代码定义独立内容摘要边界：包含会影响运行候选的代码、runtime 资源、配置和锁文件，排除审核、报告和证据自身；把该 40–64 位小写摘要绑定 parity，把完整工作树 `snapshot-id` 绑定 F1/F2。两者用途不同，且不把 layout-spec 自身的 SHA 写回自身造成自引用。这个摘要边界是迁移建议，不冒充现有脚本已支持。

## 4. 风险、授权和路由

### 4.1 四级风险

| 风险 | 典型输入或改动 | 默认审核深度 |
| --- | --- | --- |
| `light` | 文档、文案、确定性小修复 | F0/F1/F3 合并为一次自检，不创建独立审核工件 |
| `standard` | 边界明确的功能或单模块改动 | F0/F1；行为或验收变化才触发 QA F2 |
| `high` | 认证、支付、迁移、共享架构、跨模块合同、复杂 UI | F0/F1；QA 加实际触发的 Product、technical、visual 或 Release 通道；需要时持久化 review |
| `release` | 发布准备、签名、分发、生产变更、完整平台矩阵 | F0/F1；QA、technical、Release 必审，Product/visual 按变化触发 |

敏感数据、安全边界、不可逆外部修改、破坏性 API、数据迁移、共享生成文件或难回滚部署至少按 `high` 处理。风险选择不能授权外部写入、发布或真机。

### 4.2 八字段任务契约

每个迁移任务都在当前对话传递下面八项；只有跨角色、高风险持久上下文或用户明确要求时才写入 `docs/tasks/<task-id>/brief.md`：

```text
目标：<一个可观察结果>
验收条件：<可执行、可判定的条件>
写入范围：<唯一允许修改的路径>
禁止改动：<非目标、共享资源和明确禁止事项>
确认事实：<已接受的路径、版本、决定和前置证据>
风险等级：<light | standard | high | release>
验证命令：<获授权后执行的项目原生命令>
授权边界：<测试等级、分支、worktree、提交、外部写入、发布、真机；未授权写“无”>
```

任务交接唯一格式见 [`task-brief-template.md`](flutter-implementation-plan/references/task-brief-template.md)。设计确认是对目标或结构的选择；测试等级选择是对验证范围的选择。已授权本地代码范围内的接线集成随任务授权执行；超范围或破坏性修改，以及分支、worktree、提交、PR、外部写入、发布和真机验收，才需要针对精确动作的单独授权。

### 4.3 触发矩阵

| 任务事实 | DRI | 按需触发的独立通道 |
| --- | --- | --- |
| 文档或窄修复 | 当前范围所有者 | `light` 自检 |
| 普通 Flutter 功能或 Bug | Flutter Engineer | 行为/验收变化时 QA |
| 页面结构或视觉变化 | UX/UI 与 Flutter Engineer | QA + visual；技术事实变化才加 technical |
| 认证、支付、数据、迁移或共享合同 | Tech Lead / Backend/Data | QA + technical；范围或视觉变化再加 Product/visual |
| 发布、生产配置或完整平台矩阵 | Release | QA + technical + Release；其他通道按变化触发 |

只读探索和互不依赖的 F2 可以并行；可写并行必须有用户授权、共同基线和互斥范围。Controller 负责路由、用户决定和持久审核记录；不能用角色名替代缺失的专业结论。

## 5. Phaser 工作流方法到 Flutter 语义的映射

本节是概念映射，说明哪些 Phaser 工作流方法可以迁入 Flutter 技能链；它不是要求 Flutter 项目包含 Phaser 源码，也不表示旧 Phaser 名称已经在当前 Flutter schema 中存在。

| Phaser 输入概念 | Flutter 消费位置 | 迁移规则 |
| --- | --- | --- |
| 场景、状态和进入/退出流程 | 模块、页面/状态、module map、页面语义合同 | 先确认用户结果、状态和导航；不按目录名自动生成模块 |
| GameObject、容器和显示层 | Widget tree、页面 region、真实 overlay | 以语义关系、scroll owner、SafeArea 和键盘合同为准；不照搬绝对坐标 |
| Canvas、viewport、DPR、缩放 | layout-spec、技术设计的 breakpoint/constraint 基础设施 | 为每个目标 viewport 写合同；不把一张 Phaser 截图当全设备规格 |
| Phaser 图形或可程序绘制形状 | Flutter UI、CustomPainter 或已批准资产 | 先判定 UI ownership；可由 Flutter 准确还原的效果不转成 bitmap |
| 固定插画、Logo、纹理、背景装饰 | asset-manifest 和 Flutter 资源路径 | 只保留 fixed visual；来源、许可、状态和使用位置可追溯 |
| 运行时文本、数值、头像、进度和远程内容 | data owner 与 Widget renderer | 禁止裁切、生成或打包为生产位图 |
| 纹理键、加载和 fallback | Flutter asset path、loading/error/fallback 合同 | 记录真实消费和失败行为；loaded 不等于功能完成 |
| 场景弹窗、HUD、toast、drawer | 宿主页面的 display layer | persistent 与 transient 分开；瞬态必须保留宿主上下文和焦点恢复 |
| 场景交互重放 | 关键业务流 smoke、Widget/集成测试 | 在主目标平台验证实际打开、交互、关闭、恢复；不以资源加载代替运行证据 |
| Phaser 截图 parity | `phase: fidelity` 的 target/Flutter parity case | 同一 viewport/state/orientation 对照；不得声称整屏逐像素或全平台 parity |
| Phaser 原始流程文档 | 产品、UX、技术输入或变更记录 | 只作为待核验输入；当前 Flutter 文件优先，冲突必须显式裁决 |

### 5.1 冲突裁决

| 原稿或旧输入的倾向 | 当前 Flutter 规则 | 合并决定与原因 |
| --- | --- | --- |
| 全局高保真候选固定为三张，或同一目标探索多个候选 | 本轮用户决定每个具体页面/状态目标每轮只生成一张；重生成只能由用户明确要求触发 | 采用单图规则；现有 hifi skill 的两到三张探索文字列为待同步，不由本文假称已改 |
| 用旧 V 阶段、控制状态或工作项驱动页面 | Flutter 以产品/技术事实、页面链和 F0–F3 证据驱动 | 旧名称只保留为迁移追踪字段，不能成为新状态机 |
| 在拆解时同时决定或冻结布局 | 先完成状态与 ownership 拆解，再推导唯一布局 | 采用串行依赖，避免未确认元素被布局方案固化 |
| 多个布局候选供“优化” | 从已确认拆解和冻结目标推导一个布局方案 | 允许修改并重新确认当前方案，不重新设计参考图 |
| 拆解图带中文说明、图例或箭头 | 当前位图脚本只支持数字紧框，标准也禁止名称、说明、图例、箭头 | 现阶段按当前数字图运行；增强版须先更新标准、脚本和模板，见第 6 节 |
| 把一个数字视为一张独立文件或把重复实例重复批准 | asset-manifest 以 asset identity 绑定所有 placements/states | 同一固定资产保留一个 `asset_no`，membership 显式列出全部位置和状态 |
| 透明资源强制一次去背 | 当前 Flutter 资产流程优先原生透明 | 不迁入强制去背；确需处理时依合同记录方法和 QA |
| 所有 UI、数据或整屏都导出为图片 | ownership-first，只有 fixed visual 才判断 bitmap | data 和可还原 UI 留在运行时，保持可访问性、响应式和状态真实 |
| 一张 `780 x 1688` 图代表所有设备 | 当前布局合同要求目标 viewport、断点和文本增长证据 | 只对绑定的 viewport/state 宣称 parity；多设备分别验证 |
| 将整仓 snapshot 当候选代码身份 | snapshot 绑定审核范围，candidate code sha 绑定实现候选 | 两个身份并存；候选摘要边界需要后续统一，不能把 `sha256:` 直接填入字段 |
| hifi 之后静默改合同或 ownership | 回对失败即回到语义/草图并使下游证据失效 | 任何冻结事实变化都可追溯，不能用状态字段掩盖漂移 |

## 6. 视觉确认图的合并方案

### 6.1 当前可核对能力

当前 [`render-bitmap-confirmation.js`](flutter-asset-atlas/scripts/render-bitmap-confirmation.js) 读取一张冻结输入图、一个 regions JSON 和输出路径，并读取、校验每个 region 的 `number`、整数 `[x, y, width, height]` 和十六进制 `color` 字段；当前实现不会因 JSON 含有其他字段而拒绝输入。数字必须从 1 连续编号，重复实例可重复使用同号，边界不能越出原图。

脚本把框和数字叠加到原尺寸副本，拒绝覆盖冻结输入图，最后输出 PNG 的 SHA-256。它不会解释业务 ownership，也不会验证用户确认、父子层级、布局关系、中文说明或字节级结构重建。

当前脚本及 [`bitmap-decomposition-standard.md`](flutter-asset-atlas/references/bitmap-decomposition-standard.md) 的数字图限制包括：

- 不在图中放名称、说明、图例、箭头或尺寸文字。
- 只框候选 fixed bitmap，不能框 runtime data、native Flutter UI 或仅包含 bitmap 的整个容器。
- `regions` JSON 是渲染输入，不是业务状态机；它可由唯一事实确定性派生，不能反向成为工作流状态。
- 脚本没有全元素 ownership 拆解、父子布局层级、人工确认校验或技术提案逐字节重建门。

因此，旧迁移稿中“左图标注、右侧中文说明、图和 JSON 一起确认”的描述不能冒充当前 Flutter 能力。

### 6.2 建议的增强版

迁移落地时，建议把旧的“资产编号展示”增强为两张串行确认图，并同步更新标准、渲染脚本和模板。它们是新的迁移建议，尚未由本仓库现有脚本实现：

两张增强图都必须是 PNG，版式统一为左侧冻结目标原图、右侧中文说明或关系摘要。左侧原图区域的像素坐标和尺寸保持不变，不因说明栏缩放、裁剪或重采样；总画布允许向右增宽以容纳说明。因此增强图只要求原图区域保持原尺寸，不要求整张输出仍保持当前数字图的原始总宽度。

1. **全元素拆解确认图**：在冻结目标的 exact copy 上呈现完整视觉元素的 ownership 分解，至少能区分 data、runtime UI 和 fixed visual，并保留元素顺序、状态、组件与重复 placements 的结构身份。fixed visual 仍有独立 `asset_no`，manifest 通过 membership 映射到全部位置/状态。
2. **布局层级确认图**：只消费已确认的拆解。它在原图上表现父容器、子组件、同层级关系和空容器；同层级使用同色，并提供可读的关系信息。它不能重新排序元素、重画参考效果或产生多个布局候选。

两张图分别生成、分别允许修改、分别接收用户确认；第二张必须依赖第一张的已确认版本。两张图之外不新增一套重复的 bitmap 资产批准。asset-manifest 仍保留固定资产的 `asset_no`、membership、source、crop、background、size、Flutter path 和 production verdict。

编号规则也要明确：不同视觉 state 或不同输出使用不同 `asset_no`；同一输出在多个 placement 使用同一个 `asset_no`，并在 manifest 中列出全部 placement/state。无 bitmap 时全元素图仍可存在，但 fixed visual 的 asset mapping 为空。

为了避免规则与工具再次分叉，后续实现任务必须成套更新：

- `flutter-asset-atlas/references/bitmap-decomposition-standard.md`：定义全元素图的 ownership 标记、父子容器、序列化顺序和确认边界，同时保留 fixed visual 编号映射规则。
- `flutter-asset-atlas/scripts/render-bitmap-confirmation.js`：增加增强图所需的确定性输入和输出校验，不能破坏当前冻结图不覆盖、尺寸不变和 SHA 输出约束。
- `flutter-asset-atlas/references/asset-manifest-template.md`：明确全元素图、布局图、fixed visual `asset_no` 和 membership 的唯一关联。
- 如需独立布局数据模板，应新增并由同一变更说明其与 `layout-spec.yaml`、manifest 的边界；不能把渲染 JSON 当业务状态。

在这组文件落地前，现有项目继续使用当前数字图能力。不得在没有实现支持时宣称这两张增强图可用，也不得通过给当前 regions JSON 加中文字段来伪造增强能力。

### 6.3 版本与失效

用户确认必须绑定他实际看到的图、结构数据、冻结目标和版本身份。图在查看期间被替换时，旧确认不能接受到新版本上。

拆解的元素 membership、bounds、state、component 或 ownership 变化，会使拆解确认、布局图、布局确认、资产生产计划和 fidelity 证据失效。

只有布局关系变化而拆解元素、membership 和冻结目标不变时，只重生成布局图并重新确认布局；不无故重做拆解或重新批准相同 bitmap。

固定资产的编号归属、bounds、placement/state、crop、source、background、尺寸或 production verdict 变化时，必须生成新的确认版本，并使受影响资产及 fidelity 证据失效。

冻结目标的 candidate ID、SHA、viewport、state 或方向变化时，后续拆解、布局、资产和 fidelity 需要按影响范围重新绑定；不能继续沿用旧版本。

## 7. 页面主线的可执行阶段

以下阶段是把 Phaser 工作流方法落入 Flutter 技能链的执行顺序，正常 Flutter 产品同样适用。阶段名称是业务流程投影，不能被实现成一套新的运行时状态机。

### 7.1 预检与任务分诊

输入是用户意图、当前 Flutter 项目和已有工件；如有 Phaser 工作流原稿，可作为可选参考输入。Controller 先识别是新范围、页面变化、普通 Bug、技术迁移、服务任务还是发布任务，读取未提交改动，并确认项目原生命令。

在需要启动验证服务时，先查同项目已有健康实例并复用；没有可复用实例才启动。不得终止归属不明进程，不自动启动物理设备验收。

在对话中形成八字段契约，明确唯一写入范围、禁止触碰的共享文件、已确认输入、风险和授权边界。Phaser 文件的未知字段标为待核验，不把猜测写进确认事实。

退出条件是目标、范围、owner、验收和下一动作清楚；缺关键事实返回 `NEEDS_CONTEXT`，普通非 UI 任务进入第 8 节的最小分支。

### 7.2 产品语义与技术基础

新产品或实质范围变化先完成产品 brief、用户结果、MVP 非目标、状态和验收。已有项目复用已接受产品事实，只补真正变化的部分。

技术设计建立最小 Flutter 基础：状态、路由、持久化、网络、认证、权限、错误恢复、环境和依赖能力。跨模块合同先于依赖它的页面和服务实现。

Flutter 初始化只在确有需要时执行。已有项目保持当前结构和依赖；新项目用 FVM；启用的依赖必须有能力理由，拒绝更轻选项的原因写进技术设计；生成的本地 `flutter-dev` 必须反映实际档位。

共享布局基础设施由技术设计统一定义：breakpoint resolver、页面最大宽度和列/间距、scroll owner、固定/浮动/停靠原语、SafeArea、系统栏、键盘、折叠和分屏避让。页面不可各自重新发明这些规则。

模块 map 在模块首次进入实施前细化职责、路由 owner、data owner、跨模块合同、业务流级别和页面交互顺序。技术基础烟测只证明共享启动、路由和启用插件的命名覆盖。

### 7.3 页面语义合同

UX/UI Lead 将已确认的页面或场景目的、状态和交互转换为 Flutter 页面语义，不直接复制 Canvas 坐标；这一步对正常 Flutter 产品同样适用。每个页面记录：

- 用户目标、业务结果、内容优先级和可见状态；
- 进入条件、用户动作、成功/空/加载/错误/禁用/权限结果；
- 导航方向、返回行为、滚动 owner、固定/浮动元素和触摸目标；
- 断点、结构重排、同宽不同高、方向变化、文本增长和本地化增长；
- SafeArea、系统栏、键盘、焦点顺序、可访问性和恢复路径；
- data、runtime UI、fixed asset 的 ownership、来源和 fallback。

显示层必须绑定宿主。HUD 或 persistent layer 作为宿主页面的一部分；modal、popup、drawer、toast 等 transient layer 记录触发、关闭、输入阻断、z-order、遮罩、焦点恢复、互斥/共存和响应式回退。孤立弹窗图可以辅助审阅，但不能代替宿主同屏语义。

### 7.4 `phase: sketch` 布局规格

从已审语义合同创建页面唯一 `layout-spec.yaml`，使用 [`layout-spec-template.yaml`](adaptive-layout-implementation/assets/layout-spec-template.yaml)。先运行当前 validator，再进入 Code Sketch。sketch 阶段不写尚未生成的 target、测量、parity 或 critical alignment 字段。

`text_behavior.line_break` 必须按正文、标题/关键文案、控件标签和原子文本分别声明；最长文案与大字号组合必须执行实际 Widget 关系测试。适配顺序是扩宽容器、父级重排、增加可用高度、语义换行；不得用固定高度、改展示字符串、`FittedBox` 或缩字号掩盖约束缺陷。

对于冻结目标对应的 viewport/state，后续还原应保留已确认元素的顺序、原图位置、尺寸和构图。这个保序规则不适用于其他 viewport 的响应式实现：其他尺寸仍按已审断点、文本增长、SafeArea、滚动和系统避让合同重排。

### 7.5 生产骨架 Code Sketch

Flutter Engineer 在生产路由、状态模型和页面骨架中实现中性色、基础排版和占位内容，证明层级、关系、状态、交互、滚动和系统避让。不得建立一次性重复页面。

关系测试读取真实 RenderBox 或 `TextPainter`/`RenderParagraph` 结果。evidence matrix 覆盖各适用断点的 b-1/b/b+1、同宽不同高、横竖屏、默认/大字号、默认/最长文案、零/非零安全区和关键动作状态。

按 Code Sketch Level 提供结构证据：Full 要完整骨架、关系测试、确定性截图和独立 Code Sketch Review；Lightweight 默认骨架和关系测试，风险或结构歧义才补截图/独立审阅；Reuse 记录批准来源和 delta，结构事实变化才完整重审。

这里采用的迁移建议是：Full 的独立 Code Sketch Review 必需；Lightweight 可按风险以独立审阅作为高保真前置，或在结构事实稳定且 Controller 接受结构证据时继续；Reuse 在结构事实不变时以已批准模式和 delta 的接受记录作为高保真前置，变化时恢复完整审阅。当前 `flutter-hifi-mockup`/UX/UI 文案对所有页面要求 Review 通过，而 Code Sketch Level 标准对 Lightweight/Reuse 采用条件性证据，两者存在待统一的表述冲突；本段是待落地建议，不能冒充现状已经统一。

Code Sketch Reviewer 只读且与 producer 不同。它检查语义、状态、导航、滚动、断点、文本、无障碍、系统避让和生产骨架，不能批准最终视觉几何。缺 snapshot、spec hash、validator、必要测试或截图证据时按实际级别返回缺失，而不是猜通过。

### 7.6 高保真单图生成与用户冻结

Code Sketch Review 通过后准备临时 brief 和 prompt。提示词只包含页面结果、必要结构、已批准视觉方向、关键约束和输出规格；不把完整规划、源路径和审计细节塞进图片提示词。

针对每个具体页面/状态目标，每轮只生成一张高保真图，精确 `780 x 1688 px`；其 target 身份还要绑定页面、状态、viewport、orientation、来源和 SHA-256。效果不好时不由代理批量或反复重生，只有用户明确要求才按反馈重新生成一张并再次确认。

高风险或核心页面由独立只读 Effect Image Reviewer 检查任务清晰度、层级、可读性、无障碍、系统区域、产品范围、Flutter 实现路径和页面预算。用户确认当前图前，图和评审草稿不写进仓库；确认后才持久化到 `.codex-workflow/visuals/pages/<page-name>/`，再写 page design decision。冻结后若用户要求重生成，按既有冻结目标失效规则处理，不覆盖旧目标。

### 7.7 合同回对

Controller 或 UX/UI Lead 将冻结目标与语义合同、Code Sketch Review 和 sketch layout-spec 逐项回对。检查范围、内容优先级、状态、导航、交互、滚动 owner、断点、文本、无障碍、系统区域和 ownership。

高保真可以改变低保真中的几何、容器、留白、图像构图和装饰；它不能静默改变已审功能语义或 ownership。发现变化就返回语义/草图更新，并重新运行受影响的结构审阅。

回对通过后，页面设计决策只保存冻结目标、candidate ID、SHA、确认时间、约束、允许偏差和证据引用。资产明细、ownership 和编号映射留在 manifest，不复制进 design decision。

### 7.8 状态与 ownership 拆解

在资产或布局生产前，先针对每个 page/state 识别适用状态：普通、selected/active、disabled、pressed/hover、loading、empty、error、success、permission denied，以及产品合同要求的其他状态。对不适用状态写原因，不用默认值补齐。

然后建立按顺序的元素清单：component、required state、重复 placements、交互热区、region 和 production origin。`component` 是可复用视觉部件，重复出现的 instance 放在 placements；热区是交互事实，不自动计为 bitmap。

每个元素必须声明 data、runtime UI 或 fixed visual ownership，并为 fixed visual 决定 reuse、adapt、variant、new generation、atlas 或明确批准提取。程序绘制和原生 Flutter 组件不因为在参考图中可见就自动变成位图。

迁移到 Flutter 时还要拆清宿主 overlay、键盘、导航、焦点、系统避让、滚动 owner 和恢复行为。仅有一张孤立 Phaser 弹窗图时，必须补充它在宿主页面中的状态和上下文合同。

### 7.9 拆解确认

在增强版工具可用后，从冻结目标 exact copy 生成全元素拆解确认图；其结构输入必须可复现，版本绑定 target、page/state、ownership、元素顺序和候选身份。

Controller 只展示当前版本，用户可修改元素、状态、归属或 membership；修改后更新结构输入并重生成图，再等待对当前版本的明确确认。只改 PNG 像素、不改结构数据的提交不能通过。

拆解确认通过的退出事实包括：全画布扫描完成、零无 owner 元素、零 data-derived bitmap、所有固定背景/图标/纹理/遮罩和 placements 有归属、每个 bitmap candidate 只有一个 production verdict。即使页面没有 bitmap，只要需要结构或布局确认，仍要完成全元素拆解；此时 fixed visual 的资产映射可以为空。

在增强版落地前，按当前数字图生成规则完成固定 bitmap 的编号确认，但这只证明编号区域和图像版本，不能描述为全元素 ownership 或布局层级确认。

### 7.10 唯一布局推导与确认

只有拆解确认有效后，才从确认元素和冻结目标推导布局。对冻结目标 viewport/state，按原顺序作 left/center/right 与 top/center/bottom 的视觉关系判断，再把关系映射为 Flutter 的父子容器、约束、停靠和响应式参数。

左/中/右、上/中/下主要由原图构图、视觉重心和元素语义判断；几何测量用于工程参数和验证，不能替代视觉判断。两个轴的 `center` 都是有效选择。

布局是唯一方案。禁止重新排列确认元素、擅自改变冻结目标位置尺寸、重新生成参考效果图或从旧布局节点偷偷导入。确有变化时编辑当前布局提案并重新确认，而不是新增布局候选。

从唯一布局生成第二张布局层级确认图。图中表达父子容器、同层级同色、空容器和关系说明；布局确认不能替代拆解确认，也不能反向批准资产生产。

布局确认后才形成实现参数。对其他 viewport 仍使用 `LayoutBuilder`、`MediaQuery`、`SafeArea`、`ConstrainedBox`、`Flexible`、`Wrap` 或 Sliver 等关系实现；`Positioned` 只能用于合同登记的真实 overlay。

### 7.11 必要资产与无资产分流

资产规划只消费冻结目标、有效拆解确认和布局确认。先运行 ownership/coverage audit，再决定是否生产 fixed bitmap。运行 data、可访问 UI 和 Flutter 可还原形状留在实现中。

存在 fixed visual 时创建一个 `asset-manifest.md`，记录 region/layer、owner、runtime variability、classification、asset identity、证据、source/license、方法、背景、尺寸、路径、fallback 和 fidelity verdict。manifest 是唯一明细来源。

零 bitmap 或 exported visual assets 时，适用 manifest 记录 `N/A: no bitmap or exported visual assets`，资产分支结束，不生成 bitmap 编号图、不请求重复资产批准、不伪造 bitmap 生产门；这不等于跳过全元素拆解图。若目标仍要求结构或布局还原，应先完成全元素拆解确认，再做布局确认，资产 mapping 为空。

复用资源必须绑定不可变来源和兼容证据；accepted 文件不能静默覆盖。新资源必须有明确生产方法和完整记录；ImageGen、透明输出、atlas 和抽取都不能由 UI 方便选项自动降级或替换。

### 7.12 升级 fidelity 并实现

先确认布局与还原计划，再把同一 layout-spec 从 `phase: sketch` 升级为 `phase: fidelity`，使用 [`layout-spec-fidelity-template.yaml`](adaptive-layout-implementation/assets/layout-spec-fidelity-template.yaml)。此时可以记录将要测量的关键元素、关系、viewport/state 和 parity case 身份，但不能预填实际截图、测量输出、测试结果或通过状态。

Flutter Engineer 随后在同一生产骨架中正常重构和还原。禁止用一个绝对定位 Stack 覆盖旧草图来凑像素，禁止固定高截断动态文案，禁止通过改字符串或缩字号修饰截图。

实现完成后，补入每个关键对齐的稳定 Flutter key、参照边界、typed 水平/垂直关系、target/Flutter 双方几何、双轴 delta、`<= 1 logical px` 容差、实际 Widget measurement、同视口截图和已执行测试 ID。真实证据必须来自当前候选，不能用规划值或旧批次替代。

最后运行 fidelity validator，并结合实际 Widget 关系测量、target/Flutter 同视口 screenshot parity、响应式矩阵、适用功能/性能/无障碍和独立 Visual QA 收敛。validator 只有在实际字段和证据填入后才能作通过，且只证明 schema 和元数据；它不能替代测量或 Visual QA。低保真 Golden 不再作为最终视觉证据。

### 7.13 F0–F3 与全范围集成

代码改动完成后，先说明推荐测试等级、理由、覆盖和命令，等待人工选择；未选择时标记“待人工选择测试等级”，不运行命令。获授权后实现者执行 F0，Controller 再按实际变更计算 snapshot 并进行 F1 分诊。

F2 只检查被触发的事实。页面变化触发 visual/QA，认证或数据变化触发 technical/QA，发布范围触发 Release/technical/QA；未触发的通道不因迁移文档而变成必做。

修复后只重跑失败或受影响命令，只重开输入指纹变化的通道。新代码候选使相关 parity 和审核证据过期时，更新 candidate 内容摘要和 snapshot；未变化的结论可继续使用。

只有全部获授权模块、页面、状态和关键业务流完成，才进入完整集成。完整平台矩阵属于最终集成或发布，早期 foundation smoke 和 primary-target critical-flow smoke 不能宣称全平台通过。

已授权本地代码范围内的接线集成随任务授权执行；超范围或破坏性迁移/删除、分支或 worktree、提交或 PR、外部构建或渠道配置、发布和真机验收，仍需针对精确动作单独授权。开发完成不自动等于发布批准。

## 8. 非 UI、复用和无 bitmap 分支

### 8.1 文档、文案和窄修复

只修改文档、注释、文案或确定性小修复时，风险通常为 `light`。直接自检范围、链接和差异即可，不创建页面 layout-spec、hifi、资产 manifest 或临时确认图。

本迁移文档自身属于文档任务。它不应因为讨论视觉流程而执行 Flutter 命令、启动服务或生成图片。

### 8.2 普通功能或 Bug

如果行为、验收、状态或业务路径变化，按 `standard` 进入 Flutter/Backend 实现和 QA 分流；没有页面结构或视觉事实变化就跳过 hifi、资产和 fidelity 链。

如果 Bug 只影响现有页面实现而不改变结构合同，优先在同一模块和同一 layout-spec 上修复，按受影响测试验证。若修复改变语义、状态、滚动、断点、ownership 或目标几何，再升级到对应 UI 阶段。

### 8.3 Reuse

Reuse 只消费一个已批准的页面模式，记录批准来源和 delta。没有结构事实变化时，验证 delta 和受影响测试；结构变化时重新走相应的语义合同、layout-spec、Code Sketch Review 或 Visual QA。

Reuse 不自动批准新 bitmap。目标只有布局或容器变化时，布局确认仍可能适用；没有固定视觉资产时不生成资产门，适用清单写 N/A。

### 8.4 服务、数据和技术迁移

普通隔离 API 接入可按 `standard` 分流；认证、支付、数据迁移、敏感数据、共享状态、破坏性或难回滚 API、跨模块合同以及其他高影响技术变化至少按 `high` 分流。读取技术设计和对应服务合同，按适用范围补齐认证授权、版本兼容、幂等、重试、超时、迁移回退、监控、备份和恢复证据。

服务实现不在当前项目范围时，只记录外部 owner、依赖、客户端边界、兼容范围和升级路径；不为了完成 Flutter 页面而伪造服务端测试或上线回执。

### 8.5 音频、动画、复杂渲染和图片优化

音频按触发 ID、来源许可、格式、时长、循环、响度、加载、前后台和静音策略验证，并要有实际消费证据。动画、逐帧、骨骼、Tilemap、VFX 或 shader 作为技术/资源分支处理，不创建新的全局页面阶段。

图片压缩或优化只有用户明确要求该独立工作流时才进入，限定资源范围并保留身份、质量对照和单独报告；不把压缩任务插入默认的资产确认或发布阶段。

### 8.6 无 bitmap 页面

判断顺序是 ownership → fixed visual → bitmap need。若固定视觉不存在，页面才可不启动 bitmap 生产；如果存在复用 bitmap，仍须在 manifest 中记录 `reuse`、不可变来源、确认、消费和 fidelity，不得写 N/A。只有零 bitmap 或 exported visual assets 时，适用清单才记录精确 N/A。

无 bitmap 不代表没有 UI 证据。语义合同、layout-spec、关系测试、响应式和必要的 target/layout 确认仍按页面变化执行；需要布局确认时先做全元素拆解确认，资产映射保持为空。也不把 manifest N/A 写成“资产通过”或“全页面完成”。

## 9. 控制事实、角色和文件所有权

### 9.1 不引入新的控制状态机

当前 Flutter 工作流用工件、任务契约、F0–F3 证据和用户决定表达事实，不要求新增 Phaser 工作项实体、队列、数据库状态表或 JSON 状态机。

页面阶段可在 UI 中作为只读投影显示，例如“语义已接受”“草图待审”“目标已冻结”“回对需返回”“fidelity 待验证”；这些文字必须由真实工件和证据计算，未知就显示未知，不通过手工勾选伪造完成。

`phase: sketch` 和 `phase: fidelity` 是 `layout-spec` 的两阶段内容，不是运行时状态、合并信号或发布状态。资产的 planned/produced/pass 等记录若由 manifest 表达，也不等于整个页面或项目完成。

### 9.2 角色边界

| 角色 | 负责 | 不负责 |
| --- | --- | --- |
| Controller | 路由、风险、用户决定、门禁、冲突、集成和必要持久记录 | 冒充缺失的产品、技术或视觉结论 |
| Product Manager | 价值、范围、MVP、业务验收和商业约束 | 写生产代码或代替用户做实质取舍 |
| UX/UI Lead | 语义合同、视觉方向、无障碍、布局输入和设计交接 | 写页面代码或静默改变已审范围 |
| Tech Lead | 架构、依赖、模块/数据 ownership、跨模块合同和技术风险 | 扩大未确认产品范围 |
| Flutter Engineer | 生产实现、Widget/关系测试、代码候选和 F0 证据 | 自审放行或声称未运行的平台通过 |
| Backend/Data Engineer | API、数据、认证、迁移、服务测试和恢复边界 | 改变未确认 UI 或产品范围 |
| QA Engineer | 被触发质量维度的独立只读证据和结论 | 修代码或审查未触发范围 |
| Release Engineer | 构建、环境、签名、渠道、监控和回退判断 | 未授权外部写入或发布 |

当前默认单写者。layout-spec、共享路由、主题、生成文件、迁移文件和集成边界保持单写者串行；只读探索和独立审阅可并行。

### 9.3 建议保存的事实实体

这只是 App 展示或后续实现需要的事实清单，不是新的控制 schema：

| 事实 | 最小内容 | 权威来源 |
| --- | --- | --- |
| 项目上下文 | 项目身份、产品范围、平台范围、当前全局方向引用 | product/technical 文档 |
| 模块和页面 | 责任、路由 owner、data owner、业务流级别、入口/出口 | module map、module scope、语义合同 |
| 页面语义 | 状态、交互、导航、滚动、断点、无障碍、ownership | 页面语义合同 |
| sketch 布局 | regions、anchors、breakpoints、invariants、测试矩阵 | `layout-spec.yaml` 的 sketch |
| 冻结目标 | candidate ID、路径、SHA、viewport、state、确认时间、允许偏差 | page design decision |
| 拆解事实 | 状态、组件、placements、data/UI/asset 分类、区域生产路线；无 bitmap 时仍可记录 coverage | `asset-manifest.md`；无 bitmap 时保留 coverage 和 N/A |
| 布局确认 | 父子容器、关系、顺序、对齐、空容器、版本 | `layout-spec.yaml` 的布局关系字段；若需新增计划字段，先更新模板，不放未来测量证据 |
| 资产 | asset identity、membership、来源、许可、输出、fallback、fidelity | asset manifest |
| fidelity 证据 | target/Flutter 截图、测量、parity、candidate code SHA、测试 ID | fidelity layout-spec 与外部 review |
| 审核 | snapshot、F0/F1/F2/F3、发现、缺失证据、失效关系 | review；仅 Controller 持久化 |

拆解与布局的结构 JSON 只能从当前 `asset-manifest.md` 和 `layout-spec.yaml` 的已确认事实确定性派生；拆解确认记录 manifest 版本，布局确认记录 page design decision 与同一 layout-spec 版本。不要新增第二套 layout spec。若未来用数据库或对象存储展示这些事实，必须保留不可变版本、原始文件身份、用户确认和失效关系；“有数据库记录”不能替代当前文件、SHA 和证据链。

## 10. 门禁、工件和失效清单

### 10.1 按阶段的文件清单

以下路径是当前 Flutter 工作流的目标工件位置。没有对应事实时不创建占位文件；`docs/...` 路径由实际 Flutter 项目承载，本仓库只提供模板和规则。

| 阶段 | 文件或产物 | 创建条件 | 权威角色/内容 | 下一阶段门 |
| --- | --- | --- | --- | --- |
| 产品 | `docs/product/product-brief.md`、`docs/product/grilling-log.md` | 新范围或商业产品事实变化 | Product；范围、非目标、用户结果、确认 | 范围可测试 |
| 技术 | `docs/architecture/technical-design.md`、`docs/architecture/verification-platforms.md` | 架构、服务、平台或依赖需要决策 | Tech；边界、依赖、合同、验证平台 | 基础可实施 |
| 计划 | `docs/plans/module-map.md`、module scope、implementation plan | 模块或业务流进入实施 | Controller/Planner；模块、级别、契约、顺序 | 当前模块 eligible |
| 语义 | 页面语义合同、UI spec | 页面结构/交互/视觉变化 | UX/UI；状态、导航、系统和 ownership | 可建立 layout-spec |
| sketch | `docs/design/pages/<page>/layout-spec.yaml`，`phase: sketch` | 自适应页面或结构事实需要合同 | UX/UI/Flutter；关系、不变量和测试矩阵 | validator + Code Sketch |
| 草图审核 | 生产骨架、关系测试、风险需要的截图、snapshot、spec hash | Code Sketch 级别要求 | Flutter + 独立 Reviewer；结构证据 | Code Sketch approved |
| 高保真 | `.codex-workflow/visuals/pages/<page>/`、design decision | 用户选择页面视觉目标 | Controller/UX/UI；选中目标、SHA、回对 | 目标冻结且回对通过 |
| 拆解 | 全元素拆解图、结构数据；现阶段可用数字图 | 目标需要拆解/布局确认或 ownership 核对；无 fixed visual 时 asset mapping 可为空 | Asset Planning；ownership、状态、placements | 拆解确认 |
| 布局确认 | 布局层级图、关系数据 | 拆解确认后且布局关系需要确认 | UX/UI/Controller；唯一关系方案 | 布局确认 |
| 资产 | `docs/design/pages/<page>/asset-manifest.md` | 冻结目标含 fixed visual；无资产则 N/A | Asset Planning；coverage、mapping、生产与保真 | 资产可消费 |
| fidelity | 同一 layout-spec，`phase: fidelity` | 需要目标还原或关键视觉对齐 | Flutter/Visual QA；测量、parity、截图 | fidelity + Visual QA |
| 任务交接 | `docs/tasks/<id>/brief.md` | 跨角色、高风险持久上下文或用户要求 | Controller；八字段 | 角色输入明确 |
| 审核 | `docs/tasks/<id>/review.md` | high/release 持久独立验收或用户要求 | Controller 唯一写入；F0–F3、失效和结论 | 当前候选可收敛 |
| 发布 | `docs/release/release-checklist.md` | 发布在范围内 | Release；构建、商店、隐私、平台和回退 | 独立发布授权 |

页面 brief、prompt、未选候选和评审草稿在用户冻结前保持临时，不写入上述目录。snapshot 是命令输出，不作为运行时状态文件。

### 10.2 门禁顺序

| 门 | 放行事实 | 缺失或失败处理 |
| --- | --- | --- |
| 产品/技术门 | 范围、非目标、模块责任、平台和合同可观察 | 补事实或 `NEEDS_CONTEXT`，不进入页面实现 |
| 语义门 | 页面状态、交互、导航、滚动、断点、无障碍和 ownership 完整 | 返回 UX/UI，不由实现者猜测 |
| sketch 门 | layout-spec validator 通过，结构测试输入可执行 | 修 spec；不填未来 fidelity 字段 |
| Code Sketch 门 | 生产骨架、关系测试和适用级别审阅通过 | 修同一骨架并重新计算输入指纹 |
| hifi 门 | 目标候选被用户明确选择并持久化 | 保持候选临时，不开始资产或还原 |
| 回对门 | 冻结目标没有未处理语义、范围或 ownership 变化 | 返回语义/草图并使下游失效 |
| 拆解门 | 状态和 ownership 全覆盖，当前拆解图和数据获得确认 | 停在拆解；不生成或提取资产，不推导布局 |
| 布局门 | 唯一布局由已确认拆解推导，布局图和关系获得独立确认 | 修当前方案并重新确认 |
| 资产门 | manifest coverage 完整、来源清楚、资源可消费，或记录 N/A | 修 manifest/资源；无资产不伪造门 |
| fidelity 门 | 同一 layout-spec、实际测量、同视口 parity、响应式和 Visual QA 有证据 | 只重跑受影响范围，不能目测代替 |
| F0–F3 门 | 测试等级已选、F0 真实完成、F1/F2/F3 当前 snapshot 有效 | 标为待验证、changes requested 或 blocked |
| 集成门 | 全部获授权范围和跨模块合同闭合，平台层级不被夸大 | 返回具体模块/流，不用集成测试掩盖缺口 |
| 发布门 | release checklist、构建、平台、商店和外部授权齐全 | 独立发布任务等待授权；不宣称上线 |

### 10.3 失效传播

| 变化 | 立即失效 | 可保留的事实 |
| --- | --- | --- |
| 产品范围、核心状态或模块合同变化 | 受影响语义、sketch、hifi、资产、fidelity 和审核 | 未受影响模块的已接受输入 |
| 共享 breakpoint、系统避让或路由基础变化 | 依赖它的 layout-spec、Code Sketch、测量、parity | 独立产品和资产来源事实 |
| 冻结目标图、viewport、state 或方向变化 | 回对之后的拆解、布局、资产和 fidelity | 上游产品语义，若回对证明未变 |
| 拆解元素、ownership、membership 或状态变化 | 旧拆解确认、布局、资产生产和 fidelity | 未受影响的产品/技术合同 |
| 只有布局关系变化 | 布局图、布局确认、受影响 fidelity | 拆解确认和未受影响资产 mapping |
| 资产来源、编号 bounds、crop、background、尺寸或 verdict 变化 | 受影响资产确认、输出、fidelity 和视觉审核 | 其他资产的独立确认 |
| 代码、runtime 资源、配置或锁文件变化 | 相关 candidate code SHA、parity、F2/F3 证据 | 输入指纹未变的独立通道 |
| F0 命令失败、缺失或证据过期 | 当前批次和后续审核结论 | 上一候选历史记录，不能当当前通过 |
| 用户只发修改而未确认 | 当前展示版本保持待确认 | 已确认且身份完全相同的上游事实 |

每次 return/repair/revalidate 都记录最小影响 stage、page/state、artifact、失效对象、旧证据、修复结果和新版本身份。不能删除历史或只改一个状态字段绕过失效。

## 11. 验收标准

### 11.1 当前工作流合并验收

- [ ] 文档明确区分当前 Flutter 事实、Phaser 待核验输入和迁移建议。
- [ ] 主线按产品/技术基础、sketch、Code Sketch、高保真冻结、合同回对、拆解、唯一布局、资产、fidelity、实现、审核、集成和按需发布排序。
- [ ] 风险只有 `light`、`standard`、`high`、`release`；每个任务使用八字段契约。
- [ ] 默认当前 checkout、单写者、顺序执行；没有隐含 worktree、分支、提交、并行或外部写入。
- [ ] F0/F1/F2/F3 的职责分别是执行、分诊、独立只读和收敛，没有混入产品或运行时状态。
- [ ] Code Sketch Level 对 Full、Lightweight、Reuse 的结构证据和触发条件有明确说明。
- [ ] sketch layout 与高保真 fidelity 的职责、同一文件升级关系和低保真证据失效规则清楚。
- [ ] 每个具体页面/状态目标每轮只生成一张高保真图；效果不好只能由用户明确要求重新生成一张并再次确认，冻结前图与草稿 transient，确认后才持久化。
- [ ] `780 x 1688`、`390 x 844`、`2x` 被写成当前目标规格，而不是全设备 parity 承诺。
- [ ] 关键对齐容差写为 `<= 1 logical px`，并要求实际测量、同视口截图和独立 Visual QA。
- [ ] 多 viewport/方向按合同分别验证，不能用一张截图宣称所有设备通过。
- [ ] 状态分析先于 component inventory；component、placements、交互热区和 data/UI/asset ownership 分开。
- [ ] 宿主 overlay、键盘、导航、焦点、系统避让和恢复关系在迁移输入中有归属。

### 11.2 确认图和资产验收

- [ ] 当前数字图能力被准确描述为 `regions(number,bounds,color)` 渲染器，包含连续编号、整数边界、不覆盖原图、原尺寸 PNG 和 SHA。
- [ ] 文档没有把当前数字图说成支持中文说明、图例、箭头、全元素 ownership、父子布局或用户确认校验。
- [ ] 增强版明确为两张串行确认图：全元素拆解图先确认，唯一布局层级图后确认。
- [ ] fixed visual 保留独立 `asset_no`，重复 placements/states 通过 manifest membership 关联，不新增重复 bitmap 批准。
- [ ] 增强版被标为建议，并要求标准、脚本、模板成套更新；落地前仍按当前数字图运行。
- [ ] 零 bitmap 时记录 `N/A: no bitmap or exported visual assets`，不伪造资产门；需要布局确认时仍先完成全元素拆解确认，目标布局变化仍可触发布局确认。
- [ ] 资产方法覆盖 reuse、adapt、variant、new generation、atlas 和明确批准的 extraction。
- [ ] 透明资产优先原生透明，不迁入强制一次去背；不把 data 或所有 UI 变成位图。
- [ ] asset-manifest 是 ownership、coverage、mapping、生产和保真唯一权威，design decision 只链接。

### 11.3 验证和交付验收

- [ ] F0 只有在人工选择测试等级后执行；未选择时明确“待人工选择测试等级”。
- [ ] 普通审核用 `snapshot-id`；代码候选摘要与整工作树 snapshot 的不同用途已说明。
- [ ] `candidate_code_sha` 写成合法小写 commit/content SHA 语义，不要求为了适配字段创建提交。
- [ ] `workflow:snapshot` 的 `sha256:` 输出没有被直接当作 `candidate_code_sha`。
- [ ] 修复只重跑失败/受影响命令，只重开输入指纹变化的通道。
- [ ] foundation smoke、primary-target critical-flow smoke 和 final platform matrix 分层，不夸大覆盖。
- [ ] 完整集成只在全部获授权范围闭合后开始；发布、外部写入、真机和线上回滚仍需精确授权。
- [ ] 角色、文件所有权、门禁产物、创建条件和失效传播有明确表格。
- [ ] 原稿失效的 Phaser 链接不被当作当前实现引用；所有仓库链接指向现存文件。

## 12. 分阶段落地文件清单

本节是后续真正实现迁移方案时的建议顺序。本次文档任务不执行这些改动。

每批必须把相关规则、模板、脚本、validator 和 fixture 一起完成并验收后才可启用；不启用半套规则，新规则成套替换旧规则。下列命令均为人工选择测试等级后的拟执行命令，本次不执行。

| 批次 | 需同步的实际文件 | 完整验收条件 | 拟命令 |
| --- | --- | --- | --- |
| A：主线与角色 | `flutter-app-orchestrator/SKILL.md`、`flutter-ux-ui-quality/SKILL.md`、`flutter-code-sketch/SKILL.md`、`flutter-hifi-mockup/SKILL.md`、`flutter-asset-atlas/SKILL.md`、`flutter-app-orchestrator/references/artifacts.md` | 主线、Full/Lightweight/Reuse、每个页面/状态每轮单图、用户触发重生成、用户冻结、资产 N/A、单写者和待统一的 hifi Review 冲突一致；不新增控制状态机 | `npm run validate:workflow`；`npm run workflow:snapshot -- --base HEAD` |
| B：布局合同 | `adaptive-layout-implementation/references/` 下的 layout-spec、workflow、adapter、test-matrix、alignment-gate；`assets/layout-spec-template.yaml`、`assets/layout-spec-fidelity-template.yaml`；`scripts/validate-layout-spec.js` | sketch 不含未来视觉字段；fidelity 按“计划→实现→真实证据”收敛；同一 spec、候选内容摘要与整仓 snapshot 语义清楚；不新增第二套 layout spec | `npm run validate:workflow`；`npm run test:layout-fixtures`；`npm run validate:layout-spec -- <spec>` |
| C：确认图与资产 | `flutter-asset-atlas/references/bitmap-decomposition-standard.md`、`flutter-asset-atlas/references/asset-manifest-template.md`、`flutter-asset-atlas/scripts/render-bitmap-confirmation.js` | 两张串行 PNG 均为左原图右中文说明，原图区域像素尺寸不变、总画布可增宽；asset_no/membership、复用、零 bitmap N/A 与全元素拆解边界完整 | `npm run validate:workflow`；`node flutter-asset-atlas/scripts/render-bitmap-confirmation.js --help`；使用专用 fixture 渲染并检查 PNG/SHA |
| D：路由与夹具 | `scripts/validate-workflow.js`、`adaptive-layout-implementation/scripts/fixtures/` 及其运行脚本 | 文档、普通功能、页面功能、认证迁移、发布、Reuse 和无 bitmap 路由覆盖当前规则；旧 Phaser 名称不被当作可执行状态；链接和正/负夹具一致 | `npm run validate:workflow`；`npm run test:layout-fixtures` |

实际 Flutter 项目按当前路由继续执行：先把已核验的 Phaser 方法映射为模块、页面、状态和宿主 display layer；自适应页面依次完成 sketch、Code Sketch、高保真冻结、合同回对、拆解确认、布局确认、必要资产、fidelity 和 Visual QA；最后由 Controller 对获授权范围集成并按需进入发布流程。每一步仍使用八字段契约、当前 checkout 和单写者边界。

## 13. 权威依据索引

下列链接均指向本仓库现有文件；生成到实际 Flutter 项目中的 `docs/...` 产物应按这些模板建立，不在本仓库文档中伪造实例。

- 入口与路由：[`flutter-app-orchestrator/SKILL.md`](flutter-app-orchestrator/SKILL.md)
- 工件条件：[`artifacts.md`](flutter-app-orchestrator/references/artifacts.md)
- 风险、snapshot 和平台分层：[`task-risk-tiers.md`](flutter-subagent-delivery/references/task-risk-tiers.md)
- 协作、单写者和授权：[`collaboration-protocol.md`](flutter-subagent-delivery/references/collaboration-protocol.md)
- 任务契约：[`task-brief-template.md`](flutter-implementation-plan/references/task-brief-template.md)
- F0–F3 审核漏斗：[`review-funnel.md`](flutter-quality-review/references/review-funnel.md)
- 页面 UX/UI：[`flutter-ux-ui-quality/SKILL.md`](flutter-ux-ui-quality/SKILL.md)
- Code Sketch：[`flutter-code-sketch/SKILL.md`](flutter-code-sketch/SKILL.md)、[`code-sketch-level-standard.md`](flutter-code-sketch/references/code-sketch-level-standard.md)、[`code-sketch-review-rubric.md`](flutter-code-sketch/references/code-sketch-review-rubric.md)
- 自适应布局：[`adaptive-layout-implementation/SKILL.md`](adaptive-layout-implementation/SKILL.md)、[`layout-spec.md`](adaptive-layout-implementation/references/layout-spec.md)、[`implementation-workflow.md`](adaptive-layout-implementation/references/implementation-workflow.md)、[`flutter-adapter.md`](adaptive-layout-implementation/references/flutter-adapter.md)、[`test-matrix.md`](adaptive-layout-implementation/references/test-matrix.md)、[`critical-alignment-gate.md`](adaptive-layout-implementation/references/critical-alignment-gate.md)
- 高保真：[`flutter-hifi-mockup/SKILL.md`](flutter-hifi-mockup/SKILL.md)、[`mockup-brief-template.md`](flutter-hifi-mockup/references/mockup-brief-template.md)、[`mockup-review-rubric.md`](flutter-hifi-mockup/references/mockup-review-rubric.md)、[`page-design-decision-template.md`](flutter-hifi-mockup/references/page-design-decision-template.md)
- 资产：[`flutter-asset-atlas/SKILL.md`](flutter-asset-atlas/SKILL.md)、[`bitmap-decomposition-standard.md`](flutter-asset-atlas/references/bitmap-decomposition-standard.md)、[`asset-manifest-template.md`](flutter-asset-atlas/references/asset-manifest-template.md)、[`render-bitmap-confirmation.js`](flutter-asset-atlas/scripts/render-bitmap-confirmation.js)
- 技术和初始化：[`flutter-tech-design/SKILL.md`](flutter-tech-design/SKILL.md)、[`technical-design-template.md`](flutter-tech-design/references/technical-design-template.md)、[`verification-platforms-template.md`](flutter-tech-design/references/verification-platforms-template.md)、[`flutter-project-init/SKILL.md`](flutter-project-init/SKILL.md)、[`dependency-profiles.md`](flutter-project-init/references/dependency-profiles.md)
- 计划和角色：[`implementation-plan-template.md`](flutter-implementation-plan/references/implementation-plan-template.md)、[`module-map-template.md`](flutter-implementation-plan/references/module-map-template.md)、[`module-scope-template.md`](flutter-implementation-plan/references/module-scope-template.md)、[`subagent-map.md`](flutter-app-orchestrator/references/subagent-map.md)、[`app-team-role-prompts.md`](flutter-subagent-delivery/references/app-team-role-prompts.md)
- 质量和发布：[`flutter-quality-review/SKILL.md`](flutter-quality-review/SKILL.md)、[`review-rubric.md`](flutter-quality-review/references/review-rubric.md)、[`flutter-release-readiness/SKILL.md`](flutter-release-readiness/SKILL.md)、[`release-checklist.md`](flutter-release-readiness/references/release-checklist.md)
- 本仓库概览与命令说明：[`README.md`](README.md)
- 快照实现：[`workflow-snapshot.js`](scripts/workflow-snapshot.js)
- 布局规格校验实现：[`validate-layout-spec.js`](adaptive-layout-implementation/scripts/validate-layout-spec.js)

## 14. 本次文档交付边界

本次只重写 `workflow-app-migration.md`，不修改其他文件，不创建分支或 worktree，不提交，不启动服务，不运行测试、lint、构建、审核或真机验收。

建议本次文档变更按 `light` 风险、T0 处理：人工阅读差异、确认现状与建议边界即可。测试等级仍须由人工选择；当前未执行自动验证，不能把未执行命令写成通过。
