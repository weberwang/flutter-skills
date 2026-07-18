# 效果图合并评审提示词模板

将模块实现阶段完成的页面效果图作为附件交给一个 Effect Image Reviewer，并附上模块效果图拷问记录、`wireframe-spec.md`、全局设计冻结和页面视觉表达预算。评审子代理只在当前对话中输出问题和方案，不修改效果图，也不保存评审文件；控制代理负责向用户询问是否按方案修改。以 [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) 为交互评审依据，不要求复制 Apple 的视觉风格。全局视觉定位阶段不得调用本模板，因为该阶段不生成效果图。

```text
请以资深产品设计师的角度，对这张 App 效果图执行一次合并评审。

交互评审依据：Apple Human Interface Guidelines。重点检查用户任务是否清晰、信息层级、导航与控件语义、操作反馈、可访问性、触控目标和交互是否符合熟悉的平台模式。静态图无法验证的交互必须标记为“需要原型验证”，不得臆测。任务清晰是硬门槛，不得为了视觉表达而降低。

当前视觉表达预算：
- Preset ID：[填写]
- signature_strength / decoration_budget / trust_priority / information_density / wow_requirement：[填写]
- 页面类型拨档：full / moderate / dial-down
- 本页是否要求可复述的视觉签名时刻：是 / 否

请严格按以下两个部分输出：

1. 产品设计问题
   - 最多列出 5 个问题。
   - 每项包含：Apple HIG 原则或交互关注点、严重级别、画面证据、具体修改方案。

2. 提升高级感与产品辨识度建议
   - 最多列出 5 项。
   - 评审视觉层级、字体、间距、组件一致性、资产质量，以及装饰、材质、阴影、圆角和强调色是否达到本预设的签名强度与 wow 要求，且有明确目的、未伤害任务清晰度。
   - 对 full-budget 或 wow 要求为 hero-pages/required 的页面：若缺少可复述签名、过度依赖系统控件、构图过于安全导致产品性格扁平，必须作为 Important 问题提出更强 authored 处理建议。
   - 惩罚无目的噪声和通用 AI 装饰；不要仅仅因为表现力强或非原生外观而要求“更克制”。
   - 每项包含：视觉区域、提升建议、预期效果。

不要混合两个部分，不要重新设计整个页面，不要把 Apple 的视觉风格当成唯一目标，不要把“克制”当成默认高级感标准。
```
