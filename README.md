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

在 Codex 中优先从 `flutter-app-orchestrator` 开始。它先选择最小安全流程，再按需要调用专业技能：

1. 确认真实集成分支、基线、环境、依赖和验证命令。
2. 将任务分为 `light`、`standard`、`high` 或 `release`。
3. 只在存在未决产品、设计、技术或发布选择时进入提问和确认。
4. 在同一分支或 worktree 中完成实现与全部确定性验证。
5. 验证通过后冻结候选提交，并按风险并行执行必要审查。
6. 修复后只重做受影响的 Product、QA、技术或视觉审查。
7. 最终批准后执行一次合并；受控 worktree 任务自动清理分支和 worktree。

## 关键约束

- 轻量任务不创建任务状态、进度账本、worktree 或独立验收报告。
- 标准任务默认使用普通短分支；只有并发写入或高风险任务才创建受控 worktree。
- 一个受控任务只创建一个 worktree，并持续复用到最终验收，不按审查轮次重建。
- 正式审查必须等待静态检查、测试、审计命令和已知回归夹具实际通过。
- 产品范围变化重做 Product 与 QA；脚本、测试或实现变化只重做受影响的 QA/技术审查；视觉变化只重做受影响的视觉审查；格式变化通常不触发人工复审。
- 全局方向和页面效果图默认只生成一个候选；仅在用户要求探索或存在实质设计取舍时生成两到三个。
- 页面只使用与风险相称的语义契约、效果图、资产和 Pencil 证据；普通复用页面不强制完整设计代理链。
- 外部产品设计工具不是依赖；只有用户明确要求时才使用。
- 所有项目只允许一个 `docs/design/app-design.pen`，并串行写入。
- UI 验收需要截图或 golden；完整设备、模拟器、浏览器和桌面矩阵只在最终集成、发布或明确拥有该范围的任务中执行。
- 发布、生产修改、签名、远端分支删除和其他不可逆操作仍需要明确授权。

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
