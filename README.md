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
- `adaptive-layout-implementation`: 页面编码前的通用自适应布局规格、约束实施和参数化关系测试工作流。
- `flutter-product-spec`: 产品目标、MVP、用户故事。
- `flutter-ux-ui-quality`: 全局 UX/UI、状态覆盖、视觉质量门禁。
- `flutter-hifi-mockup`: 高保真效果图生成、评审、冻结。
- `flutter-asset-atlas`: 高保真图后的资产复用检查、生图、背景透明化、单图/图集导出、清单和还原验收。
- `flutter-pencil-design`: Pencil 低保真结构稿、高保真还原、Flutter handoff。
- `flutter-tech-design`: Flutter 技术方案和模块边界。
- `flutter-project-init`: Flutter 初始化、按需依赖档、生成项目级 `flutter-dev` skill。
- `flutter-implementation-plan`: 模块拆分、任务简报、验收路径。
- `flutter-subagent-delivery`: 隔离并协调必须同时执行的多个可写 Flutter 任务。
- `flutter-quality-review`: 商业交付质量审阅。
- `flutter-release-readiness`: 发布前检查。

## 推荐入口

在 Codex 中优先从 `flutter-app-orchestrator` 开始。它先选择最小安全流程，再按需要调用专业技能：

1. 确认真实集成分支、基线、环境、依赖和验证命令。
2. 将任务分为 `light`、`standard`、`high` 或 `release`。
3. 只在存在未决产品、设计、技术或发布选择时进入提问和确认。
4. 默认由单写者在普通分支顺序实现，并实际执行项目原生的 F0 命令。
5. F0 通过后冻结候选 SHA；F1 由 Controller 分诊快照、范围、风险和证据。
6. F2 仅开启实际触发的只读 Product、QA、技术、视觉或 Release 通道；互不依赖的只读审核可以并行，F3 由 Controller 收敛同一候选的结论。
7. 修复后重新通过 F0/F1，只重做覆盖事实已变化的 F2 通道。
8. F3 批准后走标准 Git、PR 和 CI 集成；Markdown 只留存决策、证据和结论，不驱动状态机或自动合并。

## 关键约束

- 所有风险等级默认单写者、顺序执行；标准和高风险任务使用普通任务分支，发布任务使用候选分支、PR 和 CI。
- 只有用户明确要求并行写入或明确要求 worktree 时才使用并行分支/worktree；即使如此也不创建 YAML/JSON 运行期状态、不自动合并，并由 Controller 通过 Markdown 简报及 Git/PR/CI 事实协调。
- 持久流程状态、任务简报与审核/决策记录只使用 Markdown，且只记录决策、证据和结论，不作为自动化输入；视觉、设计和代码资产保持原生格式。`docs/tasks/<task-id>/review.md` 只能由 Controller 写入；F2 审阅者返回结构化结论。
- 正式审查必须等待静态检查、测试、审计命令和已知回归夹具实际通过。
- 审核采用 F0 确定性过滤 → F1 变更分诊 → F2 专项审核 → F3 收敛验收；前一级未放行时不占用后一级审查资源。
- F1 只开启变化和风险实际触发的通道；F3 只收敛结论，不能替代缺失的专业审核。
- 产品范围变化重做 Product 与 QA；脚本、测试或实现变化只重做受影响的 QA/技术审查；视觉变化只重做受影响的视觉审查；格式变化通常不触发人工复审。
- 全局方向和页面效果图默认只生成一个候选；仅在用户要求探索或存在实质设计取舍时生成两到三个。
- 页面只使用与风险相称的语义契约、效果图、资产和 Pencil 证据；普通复用页面不强制完整设计代理链。
- 外部产品设计工具不是依赖；只有用户明确要求时才使用。
- 所有项目只允许一个 `docs/design/app-design.pen`，并串行写入。
- 平台验证分层进行：共享基础完成后做代表性启动、路由和插件烟测；关键业务流完成后做主目标平台运行烟测；最终集成或发布执行完整平台矩阵。任务证据不得宣称平台全量通过，也不得自动发起真机验收。
- Flutter 依赖按核心、数据/API、复杂领域和 UI token 能力档按需启用；技术设计记录每个实际依赖的启用原因，质量审核不要求未采用项。
- API/服务端工作按范围记录契约与版本、权限安全、幂等重试、迁移回滚、服务端测试、部署监控、备份恢复和客户端兼容；不负责服务端实现时只记录依赖与边界。
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
