---
name: flutter-asset-atlas
description: Use when the user explicitly asks to plan or produce bitmap assets from an approved frozen Flutter visual target, or when flutter-app-orchestrator routes the accepted asset stage.
---

# Flutter Asset Atlas

高保真目标冻结并通过合同回对后，依据 [bitmap decomposition standard](references/bitmap-decomposition-standard.md) 完成 ownership、覆盖审计、编号确认和生产。`docs/design/pages/<page-name>/asset-manifest.md` 是 ownership、覆盖审计、编号映射与资产结论的唯一权威；design decision 只链接它。

## 流程

1. 验证冻结目标路径、candidate ID、SHA-256、用户确认、全局方向和页面决策。
2. Asset planning agent 只读执行 ownership-first decomposition、全视觉覆盖审计与现有品牌/应用/共享资产复用检查。运行时 data 只记录 renderer、placeholder、loading 和 fallback。
3. 无 bitmap/exported visual 时，在 manifest 记录 `N/A: no bitmap or exported visual assets` 并结束。
4. 为每个固定视觉记录 100% match evidence。无法证明完全匹配时必须生产专用资产，不能用近似系统图标或组件替代。
5. 填写 [asset manifest](references/asset-manifest-template.md)，再用 `node scripts/render-bitmap-confirmation.js` 从 exact frozen target 生成编号图。Controller 只展示图片并等待用户明确确认。
6. 确认后由独立 production work node 只处理获批编号：依次选择 reuse、adapt、variant、new generation、atlas、或经明确批准的 target extraction。默认基于 `390 x 844` 逻辑参考仅提供精确 `2x` raster；全屏图才是 `780 x 1688 px`。
7. 需要透明合成时优先原生透明输出；否则记录 mask/removal 方法，清理 alpha、matte、color spill，保留 shadow/glow/translucency，并在 checkerboard、亮/暗和实际背景检查。
8. 在同一 manifest 记录 source/license、prompt hash、background、logical/output size、Flutter path、loading/error fallback 与 fidelity verdict。
9. 对照冻结目标、编号图和 manifest 做覆盖与视觉复核；任何映射或边界变化必须重新编号确认。

## 门禁

用户未确认编号图前不得生成、适配、提取、导出、透明化或切片。不得从代表性 runtime data 生产像素，不得把页面截图作为默认生产资产。页面 ownership 未覆盖、资产来源或 license 不清、透明边缘损坏、尺寸不符或 fidelity 未通过时阻断高保真实现。
