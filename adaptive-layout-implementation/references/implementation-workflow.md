# Implementation Workflow

1. 完成 preflight 和页面语义合同，建立 `phase: sketch` 的 layout-spec。
2. validator 通过后，在生产 Flutter 骨架中实现中性 Code Sketch；禁止建立一次性重复页面。
3. 运行 analyze 与参数化 Widget/关系测试。结构通过后才渲染风险需要的确定性截图。
4. 独立 Code Sketch Reviewer 审阅不可变 candidate diff/commit、spec hash、测试输出和截图 hash。
5. 高保真目标冻结后回对语义合同。若范围、状态、导航、滚动 owner、断点、无障碍或 ownership 改变，退回更新 sketch 并重审。
6. 将同一 layout-spec 升级为 `phase: fidelity`，在同一骨架中正常重构；禁止用绝对叠层覆盖旧草图凑像素。
7. 依次执行 fidelity validator、实际 Widget 几何测量、target/Flutter 同视口截图 parity 和独立 Visual QA。

仅导航、键盘、SafeArea、系统栏或插件行为需要时复用健康 runtime 实例。真机验收必须用户明确授权。
