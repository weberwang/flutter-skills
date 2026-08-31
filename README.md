# Flutter Skills

一组用于 Codex 交付 Flutter App 的阶段化 skills。推荐从 `flutter-app-orchestrator` 进入；它先路由最小流程，再按需要加载产品、设计、技术、实现、审核或发布 skill。

## 安装

```powershell
npx -y github:weberwang/flutter-skills
```

默认安装到当前目录的 `.agents/skills`。也可指定目录或预览：

```powershell
npx -y github:weberwang/flutter-skills --dest "D:\codex-skills"
npx -y github:weberwang/flutter-skills --dry-run
```

## 最短工作流

1. 预检仓库、既有决策、依赖、健康服务和项目原生命令。
2. 按[风险分级](flutter-subagent-delivery/references/task-risk-tiers.md)选择 `light`、`standard`、`high` 或 `release`。
3. 在当前对话填写[八字段任务契约](flutter-implementation-plan/references/task-brief-template.md)：目标、验收条件、写入范围、禁止改动、确认事实、风险等级、验证命令、授权边界。
4. 默认当前 checkout、单写者、顺序执行；普通单代理不创建 brief。只有跨角色、高风险持久审核或用户明确要求时才创建 Markdown 工件。
5. 单写者完成改动后，报告推荐测试等级和命令并等待人工选择；选择后实现者执行 F0。未执行的命令不能作为通过证据。
6. F1 只按真实变更分诊，普通审核使用 `workflow:snapshot` 的可复算 `snapshot-id`；已有且获授权的提交才绑定 SHA。
7. 只派发触发的只读 F2，F3 由 Controller 收敛。修复后只重跑失败或受影响命令，只重开输入指纹变化的通道。

分支、worktree、提交、PR、并行写入、外部写入、发布和真机验收都必须单独获得用户明确授权；Markdown 不驱动状态机、合并或发布。

## Skills

- `flutter-app-orchestrator`：唯一工作流入口和阶段路由。
- `flutter-product-spec` / `flutter-ux-ui-quality`：产品范围与 UX/UI 输入。
- `adaptive-layout-implementation` / `flutter-code-sketch`：布局规格与生产骨架草图。
- `flutter-hifi-mockup` / `flutter-asset-atlas`：冻结目标与确认后的视觉资产。
- `flutter-tech-design` / `flutter-project-init`：技术设计与工程初始化。
- `flutter-implementation-plan`：模块、任务和验收拆分。
- `flutter-quality-review`：按风险触发 F0–F3 审核。
- `flutter-release-readiness`：发布范围内的证据检查。
- `flutter-subagent-delivery`：仅用于明确授权的并行可写任务或 worktree。

专业 skill 只在用户明确请求对应阶段，或 orchestrator 已路由到该阶段时加载；保持自动发现，不要求用户记住内部文件名。

## 本地工作流工具

```powershell
npm run workflow:snapshot -- --base HEAD
npm run validate:workflow
npm run install:remote -- --dry-run
```

`workflow:snapshot` 只向 stdout 输出确定性 JSON，不写运行时状态；它包含基线、排序后的变更和工作树文件 blob ID，也覆盖未跟踪、删除、重命名、空工作树和含空格路径。`validate:workflow` 检查 skill 结构、Markdown 链接、包装清单、权威规则、提示契约和五类内置路由场景。

## 验证授权停点

代码修改完成后，代理必须先说明推荐测试等级、理由和命令；在人工选择前不运行测试、lint、构建或审核命令。测试结束须报告实际等级、结果、失败项和未执行项。完整平台矩阵属于最终集成/发布，不能由局部任务证据代替。

## 开发与重装

```powershell
node .\bin\install-flutter-skills.js --dry-run
npx -y github:weberwang/flutter-skills --force
```

安装器默认拒绝覆盖已有同名 skill；需要重装时显式使用 `--force`。
