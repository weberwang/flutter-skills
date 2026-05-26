# flutter-pen-to-architecture 图片资源导出扩展设计文档

## 1. 背景

当前 `flutter-pen-to-architecture` 已能把 `Pencil` 的 `.pen` 设计稿和 `Pencil MCP` 结构化结果转换成 Flutter 导向的设计解构、主题、组件和页面架构方案，但仍缺少一段关键能力：

- 把设计稿中的图片资源真实导出到 Flutter 项目
- 自动接入 Flutter 项目的资源声明
- 在还原方案中明确这些图片资源应如何使用

如果没有这段能力，skill 仍然停留在“只给方案、不落资源”的阶段，后续实现 agent 需要再次手动定位、下载、整理图片资源，执行稳定性不足。

## 2. 目标

在现有 `flutter-pen-to-architecture` 上增量扩展图片资源能力，使其能够：

- 优先从 `.pen` 原始内容中提取图片资源
- `.pen` 不足时回退使用 `Pencil MCP` 提供的资源引用补充
- 默认把图片导出到 Flutter 项目的 `assets/images/`
- 自动检查并更新 `pubspec.yaml`，确保该资源目录已声明
- 在最终还原方案中输出图片资源映射表和使用建议

## 3. 非目标

- 不直接生成 Flutter 页面或组件代码
- 不把所有视觉节点都导出成图片
- 不自动拆分页级子目录
- 不在第一版生成 Dart 资源常量类
- 不自动修改 `pubspec.yaml` 中与 `assets/images/` 无关的其他配置

## 4. 扩展后的能力边界

扩展后的 skill 由三段能力串联组成：

### 4.1 资源提取

- 输入 `.pen` 文件路径
- 可选输入 `Pencil MCP` 的资源清单、节点树或资源引用结果
- 优先从 `.pen` 提取图片
- `.pen` 资源不足时，回退到 `Pencil MCP` 引用补全

### 4.2 资源接入

- 输入 Flutter 项目根目录
- 找到 `pubspec.yaml`
- 确保 `flutter/assets` 下声明了 `assets/images/`
- 若已存在相同声明，则保持幂等，不重复写入

### 4.3 还原消费

- 在原有设计解构结果基础上，新增图片资源导出结果、资源映射表和使用建议
- 明确图片应如何纳入后续 Flutter 还原，而不是只做下载结果汇报

## 5. 目录与文件设计

扩展后的 skill 目录结构如下：

```text
skills/
  flutter-pen-to-architecture/
    SKILL.md
    agents/
      openai.yaml
    scripts/
      export_pen_assets.mjs
      ensure_flutter_assets.mjs
    references/
      pen-input-contract.md
      design-token-extraction.md
      dual-theme-strategy.md
      component-decomposition.md
      screen-architecture-planning.md
      fidelity-vs-flutterization.md
      output-blueprint.md
      asset-extraction-and-mapping.md
```

### 5.1 新增脚本职责

#### `scripts/export_pen_assets.mjs`

负责：

- 读取 `.pen` 输入
- 提取可导出的图片资源
- 在 `.pen` 资源不足时，允许接收 `Pencil MCP` 补充输入
- 把资源写入 Flutter 项目的 `assets/images/`
- 输出结构化导出结果

该脚本输出的结构应至少包含：

- 原始资源标识
- 导出后的文件名
- 导出目标路径
- 来源类型：`.pen` 或 `Pencil MCP`
- 是否成功导出
- 失败原因

#### `scripts/ensure_flutter_assets.mjs`

负责：

- 定位 Flutter 项目的 `pubspec.yaml`
- 判断 `flutter/assets` 下是否已有 `assets/images/`
- 没有则补齐
- 已有则不重复写入

该脚本应保证幂等，多次执行后 `pubspec.yaml` 不出现重复资源项。

### 5.2 新增参考文件职责

#### `references/asset-extraction-and-mapping.md`

负责定义：

- 哪些图片资源值得导出
- `.pen` 与 `Pencil MCP` 同时存在时的优先级
- 导出的命名与路径约定
- 图片在还原中的使用分级
- 最终映射表的字段要求

## 6. 默认输入与输出约定

### 6.1 默认输入

扩展后的 skill 默认接收：

- `.pen` 文件路径
- Flutter 项目根目录
- 可选的 `Pencil MCP` 结构化资源信息

### 6.2 默认导出目录

图片资源默认导出到：

```text
assets/images/
```

这是 Flutter 项目内最常见、最直接的资源目录，便于后续直接通过 `Image.asset(...)` 使用。

### 6.3 默认覆盖策略

当目标目录下存在同名文件时，默认行为为：

- 直接覆盖旧文件

这样更适合设计资源持续迭代场景，避免旧图片残留造成误用。

## 7. 执行流程

扩展后的完整流程如下：

1. 识别输入
2. 校验 `.pen` 文件与 Flutter 项目根目录
3. 解析 `.pen` 图片资源
4. `.pen` 解析不足时回退到 `Pencil MCP`
5. 把图片导出到 `assets/images/`
6. 检查并更新 `pubspec.yaml`
7. 继续执行全局设计扫描、token、主题、组件与页面架构分析
8. 把图片资源纳入最终还原方案
9. 输出资源导出结果、映射表和 Flutter 接入结果

## 8. 输出契约扩展

在原有输出基础上，新增以下部分：

### 8.1 图片资源导出结果

至少包含：

- 导出成功数量
- 导出失败数量
- 输出目录
- 资源来源分布：`.pen` / `Pencil MCP`

### 8.2 图片资源映射表

建议至少包含以下字段：

- `原始资源标识`
- `导出文件`
- `Flutter 路径`
- `来源`
- `页面/组件归属`
- `建议用途`
- `是否建议高保真使用`
- `备注`

### 8.3 Flutter 资源接入结果

至少包含：

- 是否找到 `pubspec.yaml`
- 是否已声明 `assets/images/`
- 是否新增声明
- 是否发生覆盖
- 是否存在失败项

### 8.4 图片在还原中的使用建议

每个核心图片资源应归类为：

- `建议直接作为 Image.asset 使用`
- `建议作为装饰性素材使用`
- `建议简化或替代`

## 9. `SKILL.md` 与现有 references 的更新方向

### 9.1 `SKILL.md`

需要补充：

- 图片资源提取与导出步骤
- `pubspec.yaml` 资源接入步骤
- 导出后的图片如何进入还原方案
- 不直接生成 Flutter 页面代码的职责边界

### 9.2 `references/pen-input-contract.md`

需要补充：

- `.pen` 文件与 `Pencil MCP` 资源输入如何共同工作
- 何时允许回退到 `Pencil MCP`

### 9.3 `references/output-blueprint.md`

需要补充：

- 图片导出结果
- 图片资源映射表
- Flutter 资源接入结果

## 10. 错误处理策略

### 10.1 阻断错误

以下情况应停止资源接入并明确报错：

- `.pen` 文件不存在
- Flutter 项目根目录不存在
- `pubspec.yaml` 不存在
- `.pen` 无法解析且没有 `Pencil MCP` 可回退

### 10.2 可降级错误

以下情况可继续执行，但必须在结果中显式标出：

- 只导出出部分图片
- 某些资源格式不支持
- `Pencil MCP` 引用不完整
- 无法判断某个图片的页面归属

### 10.3 非阻断提示

以下情况只需记入结果摘要：

- `assets/images/` 已存在
- `pubspec.yaml` 已声明资源目录
- 同名文件被覆盖

## 11. 验证要求

扩展完成后，至少要验证以下能力：

1. 给定真实 `.pen` 文件时，脚本能导出图片到 `assets/images/`
2. 重复运行 `ensure_flutter_assets.mjs` 不会重复写入同一资源目录
3. 导出结果能稳定生成结构化映射表
4. 最终 skill 输出能把图片资源纳入“还原方案”，而不是孤立下载结果

## 12. 风险与对策

### 风险一：`.pen` 结构复杂，图片提取路径不稳定

对策：优先支持主路径，补充 `Pencil MCP` 回退路径，避免只依赖单一数据源。

### 风险二：覆盖同名文件可能替换掉用户已有资源

对策：在结果中显式记录覆盖行为，并在脚本输出里打印被覆盖文件清单。

### 风险三：`pubspec.yaml` 缩进与格式处理出错

对策：资源接入脚本只修改最小范围，且保持幂等与保守写入。

### 风险四：图片导出成功但不适合直接还原

对策：在输出契约中强制加入“建议用途”和“是否建议高保真使用”字段，避免下载即视为可直接使用。

## 13. 验收标准

当用户提供 `.pen` 文件、Flutter 项目目录，以及可选的 `Pencil MCP` 资源信息时，扩展后的 skill 应能稳定实现：

- 导出设计稿中的图片资源到 `assets/images/`
- 自动补齐 `pubspec.yaml` 的资源目录声明
- 输出图片资源映射表
- 在设计解构与还原方案中纳入这些图片资源的使用建议
- 保持现有 token、主题、组件和页面架构分析能力不退化
