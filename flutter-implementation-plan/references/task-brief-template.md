# Task Brief

仅保留实施者完成当前任务所需的信息。链接权威工件，不复制其内容；不适用的条件字段直接删除。

## 任务

- ID / 名称：
- 风险等级：light / standard / high / release
- 模块 / 业务流等级：
- 目标：
- 前置等级证据：
- 已验证集成分支 / 基线提交：
- 任务分支：
- 高风险、发布或并发任务的状态 / worktree：
- 条件自动收尾命令：

## 责任与范围

- DRI 核心角色 / agent ID：
- 独立验收角色 / agent ID（按风险需要）：
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

- 页面设计决策：`docs/design/pages/<page-name>/design-decision.md`
- 资产清单：`docs/design/pages/<page-name>/asset-manifest.md`
- Pencil 节点 ID：`docs/design/app-design.pen`
- 冻结图：`.codex-workflow/visuals/pages/<page-name>/...`

## 验收

- 功能与状态：
- 可访问性 / 性能 / 安全约束：
- UI 证据（截图或 golden）：
- 验证命令：
  - `fvm flutter analyze`
  - `fvm flutter test <相关目标>`
- 已知回归夹具：
- 审查就绪条件：以上确定性检查全部实际通过

## 交付

实现者先完成全部确定性验证，再返回：状态、候选提交 SHA、变更文件、验证摘要、阻塞项。需要独立验收时，审阅者将覆盖范围、快照、发现、测试/截图路径和结论写入同一个 `docs/tasks/<task-id>/review.md`；修复后只重做受影响的审查小节。
