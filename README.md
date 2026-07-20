# Flutter Skills

一组用于 Codex 交付商业化 Flutter App 的独立 skills。工作流覆盖产品定义、UX/UI 质量、高保真效果图、Pencil 设计稿、Flutter 初始化、模块拆分、子代理交付、质量审阅和发布检查。

## 一句命令安装

不克隆仓库，不使用压缩包 URL。直接从 GitHub 仓库安装：

```powershell
npx -y github:weberwang/flutter-skills
```

默认安装到当前执行命令目录下的 `.agents/skills`。安装完成后重启 Codex，让新 skills 生效。

例如在 `D:\Git\my-app` 下执行，默认安装到：

```text
D:\Git\my-app\.agents\skills
```

## 可选参数

安装到指定目录：

```powershell
npx -y github:weberwang/flutter-skills --dest "D:\codex-skills"
```

安装到 Codex 个人 skills 目录：

```powershell
npx -y github:weberwang/flutter-skills --dest "$env:USERPROFILE\.codex\skills"
```

覆盖已存在的同名 skill：

```powershell
npx -y github:weberwang/flutter-skills --force
```

只查看将要安装的内容，不写入文件：

```powershell
npx -y github:weberwang/flutter-skills --dry-run
```

也可以用环境变量覆盖默认安装目录：

```powershell
$env:FLUTTER_SKILLS_DEST = "D:\codex-skills"
npx -y github:weberwang/flutter-skills
```

## 包含的 Skills

- `flutter-app-orchestrator`: 主流程编排入口。
- `flutter-product-spec`: 产品目标、MVP、用户故事。
- `flutter-ux-ui-quality`: 全局 UX/UI、状态覆盖、视觉质量门禁。
- `flutter-hifi-mockup`: 高保真效果图生成、评审、冻结。
- `flutter-asset-atlas`: 高保真图后的资产复用检查、生图、背景透明化、单图/图集导出、清单和还原验收。
- `flutter-pencil-design`: Pencil 低保真结构稿、高保真还原、Flutter handoff。
- `flutter-tech-design`: Flutter 技术方案和模块边界。
- `flutter-project-init`: Flutter 初始化、固定插件栈、生成项目级 `flutter-dev` skill。
- `flutter-implementation-plan`: 模块拆分、任务简报、验收路径。
- `flutter-subagent-delivery`: 使用专业 Codex 子代理推进产品/UX 草拟、视觉方向、页面设计、位图拆解、资产生产、Pencil 还原、Flutter 实现、独立审阅和修复。
- `flutter-quality-review`: 商业交付质量审阅。
- `flutter-release-readiness`: 发布前检查。

## 推荐入口

在 Codex 中优先从 `flutter-app-orchestrator` 开始。它会按顺序调度：

1. 产品规格。
2. 全局 UX/UI 方向。
3. 全局视觉方向定位与冻结，不生成页面效果图。
4. 技术方案。
5. Flutter 项目初始化和项目级 `flutter-dev` 生成。
6. 粗粒度模块拆分、业务流程等级和实现顺序。
7. 每个模块开始实现前再次拷问，确认模块功能范围；确认后再细化模块功能、页面功能和任务简报。
8. 模块效果图拷问、页面低保真语义契约分级、Wireframe Review、页面级高保真效果图。
9. 必要时生成资产图集、切图清单和资产还原验收。
10. 必要时进行 Pencil 高保真视觉还原。
11. Flutter 实现、截图或 golden 证据、质量审阅。
12. 发布准备检查。

## 关键约束

- 页面 UI 不从纯文字描述直接实现。
- 生图提示词必须将完整规划证据与实际生成正文分离：正文只保留目标、关键结构和内容、简洁视觉方向、真正不可协商项与输出要求；删除重复、矛盾、辞藻堆叠、设计理由、组件穷举和冗长负面清单，并为未冻结的次要构图与细节保留发挥空间。
- 页面级高保真效果图必须在低保真语义契约和 Wireframe Review 之后生成。低保真分为 Full、Lightweight、Reuse：只有核心、复杂或高风险页面的 Full 级必须制作 Pencil；常规页面可使用文本契约，复用页面可记录已批准模式及差异。低保真只约束范围、必需内容、信息优先级、任务、状态、导航、交互结果、可访问性语义和内容归属，不约束高保真的精确几何、容器、留白、组件轮廓、图像比例/裁切和装饰位置。
- 模块页面效果图候选、提示词草案和评审结果在用户明确确认冻结前仅保留在当前对话中；冻结时先将原始选中图片写入 `.codex-workflow/visuals/pages/<page-name>/`，再写入提示词、简报、页面设计冻结和进度记录，并登记候选 ID、尺寸、SHA-256 与确认时间。
- 全局视觉定位优先确认产品性格、视觉语言差异、情绪强度和任务清晰度；先由品类与受众推导视觉表达预算预设，并在定位前做一次轻量视觉拷问。以 Apple Human Interface Guidelines 和 iOS/Cupertino 语义作为交互、无障碍与平台基线，但不得以普通 Flutter Widget、原生 Cupertino 外观、普遍克制或后续资产工作量作为视觉上限；方向选定后记录原生组件、自定义组件、`CustomPainter`、Shader/动效或位图资产的预期路径和成本。
- 全局视觉阶段只定位和冻结跨页面视觉方向、视觉签名、设计系统原则及表达预算，不生成代表页面、模块或页面效果图，也不写入 `.codex-workflow/visuals/global/`。
- 每个 UI 模块进入效果图阶段前必须再次拷问，确认模块视觉目标、需要效果图的页面和状态、页面预算、签名要求及可接受的实现和资产成本；确认后才生成页面级效果图，不对每个页面机械重复同一轮拷问。
- 高清 Pencil 还原以已确认的页面级效果图及页面设计冻结为视觉准据；草图和 Wireframe 仅约束页面范围、结构、状态与交互，不得替代或反向覆盖效果图的视觉细节。
- 位图拆解必须先判断内容归属，再判断是否需要生产资产：运行时数据及其代表性像素不得切成位图；数据渲染器归 UI，固定外观单独归 UI 或位图。完成首轮分类后必须按图层和画面顺序二次扫漏，逐项覆盖背景装饰、低透明度或裁切元素、纹理、叠层及每个图标位置和状态，确保无未归属元素。
- 切图前必须在对话中展示完整确认表，列出资产用途、位置和状态、生产方式、来源、裁切、背景与透明处理、尺寸、风险及包含/排除建议；只有用户明确确认后才能生成、调整、提取、导出、透明化或切图，表格内容发生实质变化时必须重新确认受影响项。
- 图标、图片、插图、logo、纹理及其他视觉资源必须逐项验证与已确认效果图的视觉内容 100% 一致；无法一致时，禁止使用近似组件、系统图标或替代资源，必须进入独立位图生成、资产图集与保真验收流程。
- 全局视觉冻结仅固定跨页面复用的视觉语言和设计系统，不包含效果图，不得作为任何页面效果图确认、页面设计冻结或实现批准依据。
- 高保真图中的插图、位图、logo、纹理、生成图等必须先做复用检查；新位图默认使用 product-design 或 image generation 工具生成，Pencil 仅在节点本身是已批准生产资产时允许导出，不能默认使用 Pencil 整页截图或高保真图裁切；必须严格遵守全局和页面设计冻结约束，并先决定透明背景、保留背景或遮罩切图策略。需要透明但来源不透明的资产，必须先进入背景透明化工作节点，记录方法、源文件、输出、移除背景和继续/驳回结论；透明资产还必须完成 alpha 清理、去白边/色边、阴影保留和目标背景验收，再导出、登记和实现。
- Pencil 图不能直接丢给实现代理，必须转成文字规格和 Flutter handoff。
- 固定 Flutter 技术栈：Riverpod、hooks、Freezed、fpdart、json generation、ScreenUtil。
- Freezed 和 JSON 必须使用注解和 `build_runner` 生成。
- 子代理实现前必须有任务简报、模块顺序、验收路径和明确写入范围。
- 子代理工具可用时，产品/UX 草拟、市场分析、全局方向、页面结构、高保真效果图、位图拆解、资产规划与生产、Pencil 还原和视觉 QA 必须由对应专业子代理执行；主代理只保留用户问答、选择确认、设计冻结、冲突裁决、顺序控制和最终集成。生产者不得评审或批准自己的输出。
- 每个模块进入实现前必须重新执行一次模块级拷问，先确认该模块包含和不包含的功能；用户确认共同理解后，才能细化该模块的功能、页面、状态、验收路径和任务简报。
- 模块与模块内页面必须按业务流程依赖划分推进等级；同一等级完成其验收和跨模块契约后，才能开始下一等级。仅在写入范围无重叠且模块图明确标记为安全时，才可并行执行同一等级的任务。
- UI 完成前必须有截图或 golden 证据。
- 在 `docs/architecture/verification-platforms.md` 全局限定验证平台，例如 Android emulator/device、iOS simulator/device、Chrome web、desktop 或 `N/A: <reason>`；任务不得把未列出或未实际运行的平台登记为已验证。
- 设备、模拟器、浏览器和桌面的运行验证统一放在全部模块、页面功能及高保真还原完成后的最终集成阶段；模块任务只执行静态分析、相关测试和非运行时设计证据，不得提前声明平台已验证。

## 本地开发调试

克隆仓库后可以直接运行本地 CLI：

```powershell
npm run install:remote -- --dry-run
```

或：

```powershell
node .\bin\install-flutter-skills.js --dry-run
```

## 重装

安装器默认拒绝覆盖已存在的 skill，避免覆盖本地修改。需要重装时，使用：

```powershell
npx -y github:weberwang/flutter-skills --force
```

如果只想删除当前目录下的某一个 skill：

```powershell
Remove-Item -Recurse -Force ".\flutter-app-orchestrator"
```
