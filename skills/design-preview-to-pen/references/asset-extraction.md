# Asset Extraction

## Classification First

Do not extract by canvas region alone. Classify each element by design role:

- `布局结构`: rebuild structurally in Pencil
- `文本`: retype in Pencil
- `控件`: rebuild as editable controls or component-like groups
- `图标`: redraw, re-generate, or replace with cleaner vector-safe sources
- `插图`: isolate as image assets only when they carry style information
- `纹理/背景`: keep as raster only if Pencil structure would be wasteful
- `装饰细节`: rebuild when simple, rasterize only when the texture is the design value

## Extraction Rules

- Prefer source regeneration over low-resolution bitmap crops.
- Prefer transparent illustration assets for floating decorative pieces.
- Prefer redraw for icons that need crisp scaling.
- Preserve the approved art direction, not every accidental pixel from a preview.
- Keep text, layout, and controls editable unless the user explicitly accepts a non-editable result.
- Keep one asset manifest row per exported, regenerated, redrawn, or replaced asset.

## Asset Manifest Fields

- `名称`
- `类型`
- `设计角色`
- `来源`
- `处理方式`
- `透明需求`
- `目标位置`
- `必须一致项`
- `可调整项`
- `备注`

## Do Not

- Do not flatten text into exported images.
- Do not mix icon and illustration handling into one rule.
- Do not reuse an approved preview as the only source of all final assets.
- Do not crop fuzzy bitmap icons when a clean redraw is practical.
