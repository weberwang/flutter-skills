# Flutter Bootstrap Workflow

## 用途

- 给 `flutter-init` 提供固定的初始化顺序
- 保证先锁结构、再加依赖、再落模块，而不是从某个页面开始随手堆代码

## 初始化顺序

### 1. 创建工程

1. 使用 `flutter create` 创建干净项目
2. 删除默认 demo 页面、计数器逻辑和无关示例代码
3. 保留必要平台目录与基础工程配置

### 2. 锁定依赖

1. 读取 `flutter-project-guardrails`
2. 先添加基础必选包
3. 再按 RD 能力补充场景型包
4. 任何新增包都必须立刻有落点，不允许先加着以后再用

### 3. 建立顶层目录

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
  modules/
    <module>/
      domain/
      application/
      infrastructure/
      presentation/
```

### 4. 搭基础设施

- `app/bootstrap`: 启动入口、ProviderScope、全局初始化
- `app/router`: `go_router` 路由树与守卫
- `core/network`: `dio`、拦截器、错误映射、`retrofit` 基座
- `core/storage`: 安全存储、轻量偏好、可选离线数据库入口
- `core/logging`: 统一日志封装
- `core/error`: 通用失败模型、异常映射、用户可见错误翻译

### 5. 搭模块骨架

每个首批模块至少生成：

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

### 6. 接入注解与代码生成

- Provider 使用 `@riverpod`
- DTO / 状态 / 值对象优先使用 `@freezed`
- JSON 序列化使用 `@JsonSerializable` 或 `freezed` 配套 `fromJson`
- API 接口使用 `@RestApi`、`@GET`、`@POST` 等
- 跑一次 `dart run build_runner build --delete-conflicting-outputs`

### 7. 生成项目内 `flutter-dev`

1. 从 `assets/flutter-dev-template/` 复制出 `skills/flutter-dev/`
2. 回填项目名、模块清单、环境信息、核心命令、集成能力、决策日志
3. 明确声明它继承 `flutter-project-guardrails`
4. 不要保留模板占位符到最终项目里

### 8. 初始化验证

至少执行：

```bash
flutter pub get
dart run build_runner build --delete-conflicting-outputs
flutter analyze
flutter test
```

如果当前脚手架还没有测试用例，至少补最小 smoke test，确保初始化结果不是能编目录但不能跑。

## 输出要求

初始化完成后，必须说明：

- 已创建哪些模块
- 已接入哪些强制依赖
- 已生成哪些 `flutter-dev` 项目约束内容
- 哪些能力只是预留扩展点，还没写业务实现
- 哪些 RD 缺口仍然阻塞后续开发
