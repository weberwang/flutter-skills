# Asset Manifest

每个有固定视觉资产的页面维护 `docs/design/pages/<page-name>/asset-manifest.md`。一行同时承担图集、切图、库存和保真审阅职责；不另建四份文档。

- 页面 / 冻结图 SHA：
- 预切图确认时间 / 确认人：
- 整体保真结论：

| ID | 视觉单元与 100% 匹配依据 | 决定与来源/许可 | 背景与处理 | 输出 / Flutter 路径 / 尺寸 | 验收 |
|---|---|---|---|---|---|
| | | reuse / adapt / generate / export / extract | transparent / retained / mask；必要处理 | | pass / blocked |

只记录最终选中来源、必要提示词哈希和失败原因；候选、重复提示词和中间导出保持临时状态。
