# Flutter 适配层

## 约束树

- 页面根部使用 `LayoutBuilder` 获取当前父约束，使用 `MediaQuery.sizeOf` 获取视口，使用 `paddingOf`/`viewPaddingOf`/`viewInsetsOf` 读取系统与键盘 inset；不要缓存启动尺寸。
- 用 `ConstrainedBox` + `Center` 表达最大内容宽度，用 `Flexible`/`Expanded`/`Wrap` 表达增长和换行，用 `Align` 表达语义对齐。
- 长内容优先使用一个 `CustomScrollView`/sliver 纵向 owner；表格、代码等独立横向语义才增加横向 owner，并记录手势竞争和焦点顺序。
- 用共享 breakpoint resolver 驱动列、导航和操作区结构；ScreenUtil（若技术设计启用）只提供根初始化和命名 token。

## 系统边界与停靠

- SafeArea 只消费真正需要避让的层级，避免重复叠加 `padding`；edge-to-edge 时同时设置系统栏颜色和图标对比度。
- 底部 fixed/docked/floating 控件按 `viewPadding + 控件高度` 为内容末项预留空间；键盘出现时读取 `viewInsets`，让内容滚到焦点或把动作区改为文档流。
- `Stack` 只承载真实叠层。每个 `Positioned` 必须有语义边界、命中区、遮挡处理和窄高回退；主页面结构留在 flow 中。
- 折叠屏读取 `displayFeatures`，避开铰链和遮挡区；分屏或窗口缩放用当前约束重新计算。

## 文本与测试

- 标题、按钮、错误信息允许换行并随文本增长；关键动作禁止 `maxLines: 1` 截断。
- Widget/集成测试断言相对边界、间距、可达和遮挡关系，不把绝对坐标作为通用标准。Golden 仅在规格声明的冻结视口断言精确像素。
