# Flutter Adapter

- 使用 `LayoutBuilder`、`MediaQuery`、`SafeArea`、`ConstrainedBox`、`Flexible`、`Wrap` 或 Sliver 把语义关系翻译为生产布局。
- 页面只保留一个明确滚动 owner；键盘、SafeArea、系统栏、折叠与分屏边界不得重复应用 inset。
- 为合同元素和参照边界提供稳定 Flutter key，Widget 测试读取实际 RenderBox 几何并输出可复算测量。
- `Stack/Positioned` 仅用于真实叠层；登记 boundary、viewport scope、occlusion、fallback 和 test id。不得从目标图绝对坐标直接生成实现。
- 高保真阶段对每条关键对齐同时运行关系断言与 target/Flutter 同视口截图复核。任一缺失都不能 PASS。
