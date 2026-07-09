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
npx -y github:weberwang/flutter-skills --dest "$env:USERPROFILE\.agents\skills"
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
- `flutter-subagent-delivery`: 使用 Codex 子代理推进模块实现、审阅和修复。
- `flutter-quality-review`: 商业交付质量审阅。
- `flutter-release-readiness`: 发布前检查。

## 推荐入口

在 Codex 中优先从 `flutter-app-orchestrator` 开始。它会按顺序调度：

1. 产品规格。
2. 全局 UX/UI 方向。
3. 全局高保真效果图确认。
4. 技术方案。
5. Flutter 项目初始化和项目级 `flutter-dev` 生成。
6. 模块拆分和实现计划。
7. 模块页面低保真 Pencil、Wireframe Review、页面级高保真效果图。
8. 必要时生成资产图集、切图清单和资产还原验收。
9. 必要时进行 Pencil 高保真视觉还原。
10. Flutter 实现、截图或 golden 证据、质量审阅。
11. 发布准备检查。

## 关键约束

- 页面 UI 不从纯文字描述直接实现。
- 页面级高保真效果图必须在低保真 Pencil 和 Wireframe Review 之后生成。
- 高保真图中的插图、位图、logo、纹理、生成图等必须先做复用检查；新位图默认使用 product-design 或 image generation 工具生成，Pencil 仅在节点本身是已批准生产资产时允许导出，不能默认使用 Pencil 整页截图或高保真图裁切；必须严格遵守全局和页面设计冻结约束，并先决定透明背景、保留背景或遮罩切图策略。需要透明但来源不透明的资产，必须先进入背景透明化工作节点，记录方法、源文件、输出、移除背景和继续/驳回结论；透明资产还必须完成 alpha 清理、去白边/色边、阴影保留和目标背景验收，再导出、登记和实现。
- Pencil 图不能直接丢给实现代理，必须转成文字规格和 Flutter handoff。
- 固定 Flutter 技术栈：Riverpod、hooks、Freezed、fpdart、json generation、ScreenUtil。
- Freezed 和 JSON 必须使用注解和 `build_runner` 生成。
- 子代理实现前必须有任务简报、模块顺序、验收路径和明确写入范围。
- UI 完成前必须有截图或 golden 证据。
- 在 `docs/architecture/verification-platforms.md` 全局限定验证平台，例如 Android emulator/device、iOS simulator/device、Chrome web、desktop 或 `N/A: <reason>`；任务不得把未列出或未实际运行的平台登记为已验证。

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
