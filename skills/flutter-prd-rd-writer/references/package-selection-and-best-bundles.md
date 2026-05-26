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

## 通用基础组合

Use this section when the PRD does not require a special exception. This is the default “base stack” guidance for many Flutter projects before feature-specific packages are added.

### 国际化基础

Recommended default:

- `flutter_localizations` + `intl` + Flutter `gen_l10n`

Best bundles:

- `flutter_localizations` provides framework localization glue
- `intl` supports formatting for dates, numbers, currencies, and messages
- `gen_l10n` keeps the translation flow aligned with Flutter's built-in tooling

Alternatives:

- `slang` when the team wants stronger typed translation access, modular language packs, or a more package-driven i18n workflow

Avoid mixing:

- `gen_l10n` and another full translation runtime as co-primary systems
- manual string maps plus a generated i18n pipeline in the same app layer

When to recommend:

- recommend by default for any product that might expand beyond a single language region
- do not postpone i18n if copy volume, formatting rules, or regional rollout are already visible in the PRD

### 数据模型与不可变对象基础

Recommended default:

- `freezed` + `freezed_annotation` + `json_annotation` + `json_serializable` + `build_runner`

Best bundles:

- `freezed` for immutable models, unions, and explicit state shapes
- `json_serializable` for generated DTO parsing
- `build_runner` keeps code generation consistent across the project

Alternatives:

- `equatable` + hand-written classes for smaller apps with very few models
- plain Dart classes plus `json_serializable` when sealed unions are unnecessary

Avoid mixing:

- hand-written immutable patterns in some modules and `freezed` unions in others without a clear rule
- multiple model-generation styles in the same feature boundary

When to recommend:

- recommend this as the default base when the app has moderate or higher API and state complexity
- for very small MVPs, it is acceptable to simplify, but call out the future migration cost

### JSON 解析与映射基础

Recommended default:

- `json_annotation` + `json_serializable`

Best bundles:

- pair with `freezed` when request and response models also serve as immutable state or union types
- pair with `dio` or `retrofit` for a consistent transport-to-model pipeline

Alternatives:

- manual parsing only for trivial prototypes or one-off payloads

Avoid mixing:

- generated JSON in one repository layer and ad hoc `Map<String, dynamic>` traversal in another without a boundary
- leaking raw JSON maps into widget or state layers

When to recommend:

- recommend as the default for any project that values maintainability, testability, and DTO clarity

### 函数式错误与结果流基础

Recommended default:

- do not add `fpdart` by default for every project

Best bundles when needed:

- `fpdart` + `freezed` for typed result and failure modeling
- pair with repository and use-case layers when the team wants explicit success/failure pipelines
- fit best in enterprise or domain-heavy products where validation and branching logic grow quickly

Alternatives:

- `freezed`-based sealed failures without `fpdart`
- exception-based flows with strict boundary mapping in smaller teams or simpler apps

Avoid mixing:

- `fpdart`-style `Either` flows in one domain and uncontrolled exception-driven flows in the same path
- introducing `fpdart` only for stylistic reasons when the team is not prepared to use the pattern consistently

When to recommend:

- recommend only when the PRD implies complex validation chains, multi-step business rules, explicit domain failures, or high-value error recoverability
- for small and medium apps, call it out as an optional enhancement instead of a default dependency

## 默认通用基础栈

Use this as the baseline recommendation unless the PRD justifies a simpler or more specialized path:

- `flutter_localizations` + `intl` + `gen_l10n`
- `freezed` + `freezed_annotation`
- `json_annotation` + `json_serializable`
- `build_runner`
- add `fpdart` only when domain complexity and failure modeling requirements clearly justify it

When writing the final研发文档, explicitly say whether this baseline stack is adopted as-is, simplified, or replaced.

## Scenario Bundles

### 轻交付组合

Use when speed matters more than heavy infrastructure:

- `flutter_localizations` + `intl`
- `flutter_riverpod`
- `go_router`
- `dio`
- `freezed` + `json_serializable`
- `build_runner`
- `shared_preferences`
- `flutter_secure_storage`
- `mocktail`

### 增长型组合

Use when analytics, experiments, and release control matter:

- `flutter_localizations` + `intl`
- `flutter_riverpod`
- `go_router`
- `dio` + `retrofit`
- `freezed` + `json_serializable`
- `build_runner`
- `flutter_secure_storage`
- `firebase_analytics`
- `firebase_remote_config`
- `firebase_crashlytics`

### 企业型组合

Use when maintainability, observability, and domain complexity are higher:

- `flutter_localizations` + `intl`
- `flutter_riverpod` or `bloc` depending on team discipline
- `go_router` or `auto_route` with explicit route ownership
- `dio` + `retrofit`
- `freezed` + `json_serializable`
- `build_runner`
- `fpdart` when domain failures and validation pipelines are first-class concerns
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
