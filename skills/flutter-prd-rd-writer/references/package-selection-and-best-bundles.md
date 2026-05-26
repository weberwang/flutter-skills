# Package Selection and Best Bundles

## Use This File For

- choosing Flutter package stacks from product requirements instead of personal taste
- explaining why certain packages work well together
- warning against overlapping abstractions and fragile mix-and-match choices

## Selection Principles

Prefer:

- stable and widely used ecosystems
- packages with clear maintenance signals
- combinations with low conceptual friction
- tooling that supports testability and long-term evolution

Do not default to the newest or most feature-rich option when it increases migration risk or team learning cost.

## Before Recommending Any Package

Check whether the package choice is sensitive to current ecosystem state. If yes, verify with official documentation or the current package homepage before finalizing the recommendation.

## Capability Domains

Always recommend by capability domain, not by scattered package names.

### 1. 状态管理与依赖组织

Recommended default for most modern teams:

- `flutter_riverpod`

Best bundles:

- `flutter_riverpod` + `riverpod_annotation` + `riverpod_generator`
- pair with `go_router` for route-aware auth flows
- pair with `dio` and repository abstractions for data orchestration

Alternatives:

- `bloc` / `flutter_bloc` for event-driven teams with stricter state flow discipline
- `provider` only for smaller, low-complexity apps

Avoid mixing:

- multiple app-wide state management systems in the same feature set
- `get_it` as hidden global state plus another full state framework unless responsibilities are explicit

### 2. 路由与页面守卫

Recommended default:

- `go_router`

Best bundles:

- `go_router` + `flutter_riverpod` for auth guards and redirect logic
- `go_router` + typed route wrappers when route complexity grows

Alternatives:

- `auto_route` when code generation and strongly structured route graphs are desired

Avoid mixing:

- more than one router abstraction
- ad hoc manual guards plus a router package without a single source of truth

### 3. 网络请求、模型序列化、错误映射

Recommended default:

- `dio` + `retrofit` + `json_serializable` + `freezed`

Best bundles:

- `dio` handles interceptors, retry hooks, and transport control
- `retrofit` keeps API declarations structured
- `freezed` + `json_serializable` keeps request/response models explicit

Alternatives:

- plain `dio` without `retrofit` for smaller teams that want less code generation
- `graphql_flutter` only when the backend contract is truly GraphQL-centered

Avoid mixing:

- multiple serialization approaches in the same model layer
- `http` and `dio` together for the same transport layer without a hard boundary

### 4. 本地存储、安全存储、缓存

Recommended default:

- `shared_preferences` for lightweight flags
- `flutter_secure_storage` for tokens and secrets
- `drift` for relational offline data or complex query needs

Best bundles:

- `flutter_secure_storage` + `shared_preferences` for session metadata split
- `drift` + repository cache policy for structured offline and sync behavior

Alternatives:

- `isar` for high-performance object storage when the team accepts a different data model
- avoid overusing key-value stores as pseudo-databases

Avoid mixing:

- multiple primary databases without a strong reason
- storing secrets in plain preferences

### 5. 登录态、鉴权、刷新与会话管理

Recommended pattern:

- `flutter_riverpod` or `bloc` for auth state
- `dio` interceptors for token attach and refresh flow
- `flutter_secure_storage` for sensitive credential storage

Best bundles:

- auth state + secure storage + transport interceptor kept in one clear ownership model

Avoid mixing:

- UI-triggered token refresh plus interceptor-triggered refresh at the same time
- duplicated auth state across cache, singleton, and provider layers

### 6. 图片、媒体、上传下载

Recommended defaults by need:

- `cached_network_image` for remote image rendering
- `image_picker` for simple media intake
- `dio` for uploads and downloads with progress handling

Alternatives:

- introduce specialized media libraries only when editing, compression, or background transfer requirements justify them

Avoid mixing:

- multiple image caching layers
- upload libraries that bypass the main network transport without a clear contract

### 7. 消息推送、实时通信、深链

Recommended defaults:

- `firebase_messaging` for push when Firebase fits the stack
- `websocket_channel` for lightweight WebSocket needs
- platform deep-link support layered behind one app entry abstraction

Alternatives:

- vendor-specific push or messaging stacks only when product or region requires them

Avoid mixing:

- multiple competing push stacks for the same notification responsibility
- deep-link parsing split across unrelated modules

### 8. 日志、崩溃、性能监控

Recommended defaults:

- `logger` or team-standard structured logging wrapper for local logs
- `firebase_crashlytics` or `sentry_flutter` for crash reporting and production diagnostics

Best bundles:

- crash reporting + structured log context + release metadata

Alternatives:

- use `sentry_flutter` when distributed tracing or broader backend observability alignment matters

Avoid mixing:

- multiple crash SDKs without a defined division of responsibility

### 9. 埋点、远程配置、AB、灰度能力

Recommended defaults:

- `firebase_analytics`
- `firebase_remote_config` when remote switches and staged rollout are needed

Alternatives:

- vendor analytics stacks when the organization already standardizes on them

Avoid mixing:

- duplicate event sources across analytics SDKs without a taxonomy owner
- remote config without a clear fallback and rollout policy

### 10. 测试、Mock、代码生成、Lint 与工程工具链

Recommended defaults:

- `flutter_test`
- `integration_test`
- `mocktail`
- `build_runner`
- `flutter_lints`

Helpful companions:

- `golden_toolkit` when visual regression has real product value
- `melos` when the workspace becomes multi-package or modular at scale

Avoid mixing:

- multiple mocking styles in the same team conventions
- code generation without CI validation for stale generated files

## Scenario Bundles

### 轻交付组合

Use when speed matters more than heavy infrastructure:

- `flutter_riverpod`
- `go_router`
- `dio`
- `freezed` + `json_serializable`
- `shared_preferences`
- `flutter_secure_storage`
- `mocktail`

### 增长型组合

Use when analytics, experiments, and release control matter:

- `flutter_riverpod`
- `go_router`
- `dio` + `retrofit`
- `freezed` + `json_serializable`
- `flutter_secure_storage`
- `firebase_analytics`
- `firebase_remote_config`
- `firebase_crashlytics`

### 企业型组合

Use when maintainability, observability, and domain complexity are higher:

- `flutter_riverpod` or `bloc` depending on team discipline
- `go_router` or `auto_route` with explicit route ownership
- `dio` + `retrofit`
- `freezed` + `json_serializable`
- `drift`
- `flutter_secure_storage`
- `sentry_flutter` or `firebase_crashlytics` based on observability stack

## Output Shape

When writing the final研发文档, keep every domain in this structure:

```text
能力域：
推荐主方案：
推荐理由：
最佳搭档：
备选方案：
避免混搭：
接入注意事项：
升级/维护风险：
```
