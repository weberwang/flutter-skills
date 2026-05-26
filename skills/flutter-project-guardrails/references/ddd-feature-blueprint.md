# DDD Feature Blueprint

## 用途

- 规定 Flutter 项目的默认目录结构
- 强制按业务边界拆 feature，而不是按页面、接口或临时需求堆文件
- 保证后续新增功能时仍然能沿着同一结构演进

## 顶层目录

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

## 顶层职责

### `app/`

- 负责应用启动、全局装配、路由树、入口配置
- 不承载具体业务规则

### `core/`

- 放跨 feature 基础设施
- 例如网络客户端、日志、配置、错误模型、存储基座
- 这里是可复用基础能力，不是所有杂项都往里丢

### `shared/`

- 只放真正跨 feature 复用且不属于某个单一业务域的内容
- 可包含共享展示组件和少量 shared kernel
- 如果一个东西只服务单 feature，就回到 feature 内部

### `features/`

- 每个一级目录都是一个清晰的 bounded context
- 不按页面数量拆，不按后端接口数量拆

## Feature 分层职责

### `domain/`

- 放实体、值对象、领域规则、仓储抽象
- 不依赖 Flutter UI
- 不直接依赖网络、数据库、平台插件

### `application/`

- 放 use case、应用服务、状态编排、provider 暴露
- 负责把领域能力组织成可调用的业务动作
- 可依赖 `domain`

### `infrastructure/`

- 放数据源、DTO、仓储实现、平台适配
- 负责和 `dio`、`retrofit`、存储插件、第三方 SDK 打交道
- 可依赖 `domain`

### `presentation/`

- 放页面、组件、页面级视图状态消费
- 只负责用户交互和显示，不承载数据访问细节

## 依赖方向

只能接受下面的方向：

- `presentation -> application -> domain`
- `infrastructure -> domain`
- `app -> features / core / shared`

禁止下面的方向：

- `domain -> infrastructure`
- `domain -> presentation`
- `presentation -> infrastructure` 直接跳过应用层
- feature A 直接引用 feature B 的内部实现细节

## Feature 模板

```text
features/
  auth/
    domain/
      entities/
      repositories/
      value_objects/
    application/
      providers/
      use_cases/
    infrastructure/
      datasources/
      models/
      repositories/
    presentation/
      pages/
      widgets/
```

## 命名与组织规则

- 一个 feature 下的文件名按职责命名，不用 `utils.dart`、`manager.dart`、`common.dart` 这类模糊名字
- 页面状态如果只服务当前页面，优先留在当前 feature 内部
- 跨 feature 复用要先证明真的跨 feature，再上提到 `shared`
- 新需求先判断是扩现有 feature 还是新建 bounded context，不要默认继续往老 feature 里塞
