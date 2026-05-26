# Mandatory Package Bundle

## 用途

- 规定 Flutter 项目的默认必选依赖
- 约束加了就必须用的包治理方式
- 防止同一职责里混入多套状态、路由、网络、序列化或存储方案

## 基础必选运行时依赖

以下包默认进入所有新项目基线：

- `flutter_riverpod`
- `riverpod_annotation`
- `go_router`
- `dio`
- `retrofit`
- `freezed_annotation`
- `json_annotation`
- `flutter_secure_storage`
- `shared_preferences`
- `logger`

## 基础必选开发依赖

- `build_runner`
- `riverpod_generator`
- `retrofit_generator`
- `freezed`
- `json_serializable`
- `custom_lint`
- `riverpod_lint`
- `flutter_lints`

## 按能力触发的附加依赖

### 离线关系型数据

当 RD 明确有复杂离线查询、同步、本地草稿或结构化缓存时，追加：

- `drift`
- `drift_dev`

### 埋点、远程配置、崩溃监控

当 RD 明确要求运营能力或生产监控时，追加：

- `firebase_analytics`
- `firebase_remote_config`
- `firebase_crashlytics`

### 图片与媒体输入

当 RD 明确需要媒体选择、远程图片缓存时，追加：

- `cached_network_image`
- `image_picker`

### 实时通信

当 RD 明确需要 WebSocket 或轻量实时通道时，追加：

- `websocket_channel`

## 包治理规则

- 新增包前，先说明它属于哪个能力域、由哪一层拥有、放在哪个模块使用。
- 包一旦进入 `pubspec.yaml`，必须在当前脚手架或当前需求里落到真实代码，不允许先占坑。
- 同一能力域只保留一套主方案，不做双轨并存。
- 如果能力不成立，就不要把对应包加进来。

## 强制搭配

### 状态与依赖组织

- 主方案：`flutter_riverpod` + `riverpod_annotation` + `riverpod_generator`
- 说明：既负责状态，也承担显式依赖组织；不要再叠加第二套全局状态框架

### 路由

- 主方案：`go_router`
- 说明：鉴权跳转、深链入口、页面守卫都围绕同一套路由树实现

### 网络与模型

- 主方案：`dio` + `retrofit` + `freezed_annotation` + `json_annotation`
- 说明：接口定义、错误拦截、DTO、状态对象和序列化统一走注解生成

### 存储

- 主方案：`flutter_secure_storage` + `shared_preferences`
- 说明：敏感数据与轻量偏好分层存储；不要把 token 落到普通偏好里

## 禁止混搭

- `flutter_riverpod` 与 `provider` / `bloc` 并存承担同一职责
- `dio` 与 `http` / `chopper` 在同一业务链路并存
- 手写 JSON mapping 与 `json_serializable` / `freezed` 并存
- `get_it` 作为隐藏全局容器，再叠加 Riverpod 管理同一批依赖
- 多个主存储方案同时承担同一离线职责

## 版本策略

- skill 中固定的是包名与职责，不是写死版本号
- 真正写入项目时，优先用当前稳定版本，并在需要时去官方文档或 pub.dev 核实
