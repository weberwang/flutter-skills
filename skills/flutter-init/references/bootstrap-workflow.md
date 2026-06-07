# Flutter Bootstrap Workflow

## 用途

- 给 `flutter-init` 提供固定的初始化顺序
- 保证先锁结构、再加依赖、再落 feature，而不是从某个页面开始随手堆代码

## 初始化顺序

### 1. 创建工程

1. 使用 `flutter create` 创建干净项目
2. 删除默认 demo 页面、计数器逻辑和无关示例代码
3. 保留必要平台目录与基础工程配置

### 2. 锁定依赖

1. 读取 `flutter-project-guardrails`
2. 先添加基础必选包，并优先选择与当前 Flutter SDK 兼容的最新版
3. 再按 RD 能力补充场景型包，同样优先选择与当前 Flutter SDK 兼容的最新版
4. 任何新增包都必须立刻有落点，不允许先加着以后再用

### 3. 处理插件重配开关

1. 检查请求里是否显式包含 `--force`
2. 如果包含：
   - 重新执行当前 RD 范围内的插件配置
   - 插件版本优先选择与当前 Flutter SDK 兼容的最新版
   - 覆盖或刷新已有插件接入产物
   - 然后继续后续初始化步骤
3. 如果不包含：
   - 先检查当前 RD 范围内所需插件是否已经配置
   - 如果还没配置，执行首次插件配置，并优先选择与当前 Flutter SDK 兼容的最新版
   - 如果已经配置，保留现有插件配置，不重复覆盖
   - 然后继续后续初始化步骤

### 4. 建立顶层目录

默认顶层结构：

```text
lib/
  app/
    bootstrap/
    router/
    startup/
  core/
    config/
    error/
    logging/
    network/
    storage/
  shared/
    kernel/
    presentation/
  features/
    <feature>/
      domain/
      application/
      infrastructure/
      presentation/
```

### 5. 建目录级占位与最小基线

- 只创建后续 bootstrap 阶段会用到的目录与最小占位
- 可以预留 `app/bootstrap`、`app/router`、`app/startup`、`core/network`、`core/storage`、`core/logging`、`core/error`
- 这里不落真实启动入口、不落 `ProviderScope`、不落路由树、不落全局 wiring
- 如果需要占位文件，只允许放不会形成真实运行链路的占位声明、空壳契约或说明性 stub
- 如果某个目录当前 RD 明确不需要，可以不建；但不要为了后续方便直接写入 bootstrap 代码

### 6. 搭 feature 骨架

每个首批 feature 至少生成：

- `domain/entities`
- `domain/repositories`
- `application/use_cases`
- `application/providers`
- `infrastructure/datasources`
- `infrastructure/models`
- `infrastructure/repositories`
- `presentation/pages`
- `presentation/widgets`
- `presentation/providers` 或仅保留应用层 provider 入口

### 7. 接入注解与代码生成准备

- Provider 使用 `@riverpod`
- DTO / 状态 / 值对象优先使用 `@freezed`
- JSON 序列化使用 `@JsonSerializable` 或 `freezed` 配套 `fromJson`
- API 接口使用 `@RestApi`、`@GET`、`@POST` 等
- 只有当当前占位已经需要验证生成链路时，才跑一次 `dart run build_runner build --delete-conflicting-outputs`

### 8. 生成项目内 `flutter-dev`

1. 从 `assets/flutter-dev-template/` 复制出 `skills/flutter-dev/`
2. 回填项目名、feature 清单、环境信息、核心命令、集成能力、决策日志
3. 明确声明它继承 `flutter-project-guardrails`
4. 不要保留模板占位符到最终项目里

### 9. 初始化验证

至少执行：

```bash
flutter pub get
dart run build_runner build --delete-conflicting-outputs
flutter analyze
flutter test
```

如果依赖解析、插件接入、代码生成或分析阶段出现 Flutter SDK 兼容问题，先调整到与当前 Flutter SDK 兼容的最新版组合，再继续验证。

如果当前脚手架还没有测试用例，可以先不补业务 smoke test；但要明确记录这是目录初始化阶段，真实启动链路留给 bootstrap code 阶段。

## 输出要求

初始化完成后，必须说明：

- 已创建哪些 feature
- 已接入哪些强制依赖
- 是否触发了 `--force` 插件重配，或是否执行了首次插件配置
- 本次处理了哪些插件，哪些插件保持不变
- 本次依赖和插件使用了哪些与当前 Flutter SDK 兼容的最新版
- 遇到了哪些兼容性问题，以及如何修复
- 已生成哪些 `flutter-dev` 项目约束内容
- 哪些内容只是目录、占位或契约，尚未形成真实运行代码
- 哪些 bootstrap 代码仍明确留在后续 `bootstrap code` 阶段
- 哪些能力只是预留扩展点，还没写业务实现
- 哪些 RD 缺口仍然阻塞后续开发
