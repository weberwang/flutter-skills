# Task Brief

仅保留实施者完成当前任务所需的信息。链接权威工件，不复制其内容；不适用的条件工件留空并在“条件”写一行原因。

## 任务

- ID / 名称：
- 模块 / 业务流等级：
- 目标：
- 前置等级证据：
- 任务状态：`.codex-workflow/tasks/<task-id>.yaml`
- 基线提交 / 任务分支 / worktree：
- Controller 集成 worktree / 分支：
- 自动收尾命令：`python <flutter-subagent-delivery>/scripts/finalize-task.py .codex-workflow/tasks/<task-id>.yaml --integration-worktree <集成-worktree> --integration-branch <集成分支>`

## 责任与范围

- DRI 核心角色 / agent ID：
- 独立验收角色 / agent ID：
- 已启用专家席位与原因：
- 读范围：
- 唯一写范围：
- 非目标：
- 共享资源锁：

## 权威输入

- 产品简报：
- UI 规格：
- 技术设计：
- 模块图 / 已确认模块 scope：
- 项目本地 `flutter-dev`：
- 平台验证范围：

## 条件输入

- 页面设计决策：`docs/design/pages/<page-name>/design-decision.md` / 不适用原因：
- 资产清单：`docs/design/pages/<page-name>/asset-manifest.md` / 不适用原因：
- Pencil 节点 ID：`docs/design/app-design.pen` / 不适用原因：
- 冻结图：`.codex-workflow/visuals/pages/<page-name>/...` / 不适用原因：

## 验收

- 功能与状态：
- 可访问性 / 性能 / 安全约束：
- UI 证据（截图或 golden）/ 不适用原因：
- 验证命令：
  - `fvm flutter analyze`
  - `fvm flutter test <相关目标>`

## 交付

实现者只返回：状态、任务提交 SHA、变更文件、验证摘要、阻塞项。独立验收者将快照、发现、测试/截图路径、UI QA（如适用）和最终结论写入 `docs/tasks/<task-id>/review.md`。
