# docs/project

默认项目产物目录。

除非用户明确指定其他位置，或某个下游技能/工具契约强制要求不同路径，增强工作流产生的稳定产物统一放在 `docs/project/` 下。

当前默认约定：

- 全局产物：`docs/project/`
- 模块产物：`docs/project/modules/<module>/`
- 模块索引：`docs/project/00-module-index.md`

运行时状态、临时追踪文件和一次性过程记录不属于稳定产物，仍应放在 `tmp/` 等运行时目录，而不是提交到这里。
