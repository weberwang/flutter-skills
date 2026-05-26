# flutter-pen-to-architecture 设计文档

## 1. 背景

当前仓库已经有面向 Flutter UI 方向、PRD/RD 生成方向、约束规范方向的 skill，但还缺少一个能把 `Pencil` 的 `.pen` 设计稿与 `Pencil MCP` 结构化结果，稳定还原成 Flutter 可实施方案的中间层 skill。

这个 skill 的目标不是直接生成页面代码，而是先把设计稿转化为一份适合 Flutter 团队消费的实现架构方案，帮助后续的规范生成、项目初始化和实现型 skill 建立统一输入。

## 2. 目标

新增一个名为 `flutter-pen-to-architecture` 的 skill，使其能够基于 `.pen` 文件和 `Pencil MCP` 输出，默认按全局、多页面、双主题视角完成以下工作：

- 识别整套设计稿的页面家族、导航结构和信息分层
- 提取全局设计 token，并区分亮色与暗色主题策略
- 拆解可复用组件体系，而不是逐节点翻译
- 规划页面骨架、壳层结构、状态区块和弹层体系
- 明确哪些设计应高保真还原，哪些应 Flutter 化重构，哪些应简化处理
- 输出一份可供 `flutter-init` 消费的规范摘要，作为后续约束规范生成的输入

## 3. 非目标

- 不直接生成 Flutter 页面、组件或主题代码
- 不依赖纯截图推断设计结构，截图最多只作为辅助佐证
- 不把 `.pen` 的绝对坐标、层级树原样映射为 Flutter Widget 树
- 不为了兼容旧方案而保留过渡性结构
- 不承担项目初始化、代码脚手架落地或业务实现职责

## 4. 输入边界

### 4.1 默认输入

这个 skill 默认接受以下输入：

- `.pen` 文件结构本身
- `Pencil MCP` 读取到的节点树
- `Pencil MCP` 读取到的 variables、layout、组件实例结构等结构化结果

### 4.2 非默认输入

以下输入不作为主入口：

- 纯设计截图
- 纯文本视觉描述

当只有截图或文本时，不应强行触发该 skill，除非用户明确要求按近似方案输出。

### 4.3 信息不足时的处理

当缺少 variables、组件实例关系、关键页面节点树或主题线索时，skill 必须先输出：

- `前提假设`
- `待确认项`

然后再继续给出有限度的分析结果，不能伪造设计系统细节。

## 5. skill 定位

### 5.1 名称与触发描述

- skill 名称：`flutter-pen-to-architecture`
- 触发方向：当用户希望把 `Pencil/.pen` 或 `Pencil MCP` 结果转为 Flutter 导向的设计架构方案时触发

### 5.2 默认设计哲学

该 skill 默认采用“折中策略”：

- 先判断设计稿中哪些内容应尽量高保真还原
- 再判断哪些内容应优先转成 Flutter 的主题、token、语义层级和复用组件
- 最后明确哪些装饰、效果或结构应简化处理

其核心不是“像素级复刻”，而是“保留设计原意并形成可维护的 Flutter 方案”。

## 6. 方案选择

本 skill 采用“主 skill + 参考手册”的结构，而不是重资产模板或脚本优先方案。

### 6.1 采用方案

- `SKILL.md` 负责触发条件、主流程、硬规则、交付物和引用关系
- `references/` 负责沉淀输入契约、token 提取、双主题策略、组件拆解、页面架构和取舍规则

### 6.2 采用原因

- 符合当前仓库已有 Flutter skill 的组织风格
- 便于后续继续增加案例和规则，不会让主文件过重
- 更适合“输出实现方案而非代码”的能力定位

## 7. 目录结构

```text
skills/
  flutter-pen-to-architecture/
    SKILL.md
    agents/
      openai.yaml
    references/
      pen-input-contract.md
      design-token-extraction.md
      dual-theme-strategy.md
      component-decomposition.md
      screen-architecture-planning.md
      fidelity-vs-flutterization.md
      output-blueprint.md
```

### 7.1 文件职责

#### `SKILL.md`

负责定义：

- 何时使用这个 skill
- 触发后的执行流程
- 输出契约
- 硬规则
- 何时读取哪个参考文件

#### `agents/openai.yaml`

负责定义：

- 展示名称
- 简短描述
- 默认调用提示语

#### `references/pen-input-contract.md`

负责定义：

- `.pen` 与 `Pencil MCP` 输入优先级
- 节点树、variables、layout 的最小分析要求
- 信息不足时的降级分析边界

#### `references/design-token-extraction.md`

负责定义：

- 颜色、字号、字重、圆角、间距、阴影等 token 的抽取方法
- 如何从零散视觉样式归并为 Flutter 可维护 token
- 哪些 token 适合进入 `ThemeData`，哪些适合进入 `ThemeExtension`

#### `references/dual-theme-strategy.md`

负责定义：

- 亮色主题与暗色主题的共用 token 和分叉 token
- 色彩语义、层级语义、文本可读性策略
- 暗色主题不能简单反相的判断规则

#### `references/component-decomposition.md`

负责定义：

- 基础组件、组合组件、业务组件、页面区块的拆解规则
- 组件抽象的边界
- 什么情况必须复用，什么情况不值得抽象

#### `references/screen-architecture-planning.md`

负责定义：

- 多页面稿的页面家族识别
- 导航壳、列表详情流、表单流、弹层体系、状态层的规划方法
- 页面骨架与共享壳层的抽象方式

#### `references/fidelity-vs-flutterization.md`

负责定义：

- 高保真还原、Flutter 化重构、简化处理三类判断标准
- 如何解释取舍原因
- 如何避免把设计稿机械翻译成 Widget 树

#### `references/output-blueprint.md`

负责定义：

- 固定输出结构
- 建议表格字段
- 可供 `flutter-init` 消费的规范摘要格式

## 8. 核心工作流

skill 触发后按以下顺序工作：

1. 识别输入范围，确认 `.pen`、节点树、variables、layout 是否齐全
2. 做全局设计扫描，识别页面集合、导航关系、信息层级和视觉语义
3. 提取设计 token，并归纳全局视觉规则
4. 产出亮色与暗色双主题策略
5. 拆解组件体系，形成基础组件到页面区块的层级
6. 规划页面架构，包括页面骨架、壳层结构、状态区块和弹层体系
7. 对关键视觉决策进行“高保真还原 / Flutter 化重构 / 简化处理”分类
8. 输出一份完整分析结果，并附带可供 `flutter-init` 消费的规范摘要

## 9. 输出契约

skill 每次输出结果至少应覆盖以下部分：

1. `输入摘要`
2. `全局设计结构`
3. `设计 Token 归纳`
4. `亮色主题方案`
5. `暗色主题方案`
6. `组件拆解清单`
7. `页面实现骨架`
8. `高保真 / Flutter 化取舍说明`
9. `实现边界建议`
10. `可供 flutter-init 消费的规范摘要`
11. `风险与待确认项`

### 9.1 强制字段

对关键页面区块或组件，建议统一输出以下字段：

- `设计原意`
- `Flutter 落法`
- `是否高保真`
- `是否进入主题层`
- `是否抽成复用组件`
- `风险/备注`

这样后续 skill 可以直接消费这些结构化结论，而不必重新推断。

## 10. 硬规则

- 不把 `.pen` 的绝对位置和尺寸机械翻译成 Flutter 布局
- 不把每个视觉节点都抽成组件，组件化必须服务复用与维护
- 不把暗色主题理解成亮色主题的颜色反相
- 不默认照搬装饰性视觉效果，必须先判断其业务语义或品牌语义
- 不输出泛泛的审美建议，必须落到 Flutter 的主题、token、组件和页面架构
- 不直接生成代码；如果用户明确要代码，应交给后续实现型 skill
- 对每个关键视觉决策，都必须标明是：
  - `建议高保真还原`
  - `建议 Flutter 化重构`
  - `建议简化处理`

## 11. 与 flutter-init 的关系

`flutter-pen-to-architecture` 与 `flutter-init` 的职责边界如下：

- `flutter-pen-to-architecture` 负责把设计稿转成 Flutter 导向的实现架构方案
- `flutter-init` 负责基于这些方案继续生成约束规范 skill 或初始化规范能力

因此，本 skill 的输出中必须包含一段 `可供 flutter-init 消费的规范摘要`，至少覆盖：

- 主题约束
- token 约束
- 组件约束
- 页面骨架约束
- 高保真边界
- Flutter 化重构边界

## 12. 风险与对策

### 风险一：设计稿样式不一致，难以归纳 token

对策：优先输出“候选 token 组”和归并建议，而不是强行给出唯一答案。

### 风险二：暗色主题缺少明确线索

对策：明确标记哪些暗色 token 属于推断结果，并附上可读性与层级优先原则。

### 风险三：组件抽象过度

对策：要求每个抽象组件都必须说明复用场景、状态变化点和维护收益。

### 风险四：分析结果过于贴近设计工具结构

对策：在取舍规则中强制加入 Flutter 化重构说明，避免工具结构污染实现结构。

## 13. 验收标准

当用户提供一套中等复杂度以上的 `.pen` 设计稿和 `Pencil MCP` 结构化结果时，这个 skill 应能稳定输出：

- 覆盖全局、多页面视角的分析结果
- 同时包含亮色与暗色主题策略
- 可维护的 token 归纳与组件拆解
- 清晰的页面骨架与实现边界
- 明确的高保真 / Flutter 化 / 简化处理取舍
- 可供 `flutter-init` 继续消费的规范摘要

## 14. 实施阶段

### 阶段一：创建 skill 目录与元数据

- 初始化 `skills/flutter-pen-to-architecture/`
- 创建 `agents/openai.yaml`

### 阶段二：编写 `SKILL.md`

- 写入触发描述
- 固化主流程
- 固化输出契约与硬规则

### 阶段三：补齐参考文件

- 编写 7 份按职责拆分的参考文件
- 保持单文件单职责，避免主文件膨胀

### 阶段四：校验与微调

- 运行结构校验
- 检查 frontmatter、命名和引用关系
- 检查是否存在占位内容、歧义和职责重叠
