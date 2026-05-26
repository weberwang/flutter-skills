# Project Output Checklist

## 目录检查

- 存在 `pubspec.yaml`，且依赖与 guardrails 对齐
- 存在 `lib/app`
- 存在 `lib/core`
- 存在 `lib/shared`
- 存在 `lib/modules`
- 存在项目内 `skills/flutter-dev`
- 首批业务模块都已按 DDD 分层建好目录

## 基础文件检查

- 启动入口已替换默认计数器示例
- 已有统一 app shell，如 `app.dart` / `bootstrap.dart`
- 已有 `go_router` 路由入口
- 已有 `dio` 基础客户端和拦截器入口
- 已有存储抽象与安全存储入口
- 已有统一错误模型或失败模型

## 代码生成检查

- Provider 至少已有一个 `@riverpod` 示例
- DTO / state 至少已有一个 `@freezed` / `@JsonSerializable` 示例
- 至少已有一个 `@RestApi` 接口定义或基础 API 模板
- `build_runner` 可成功生成 `.g.dart` / `.freezed.dart`
- `skills/flutter-dev/SKILL.md` 与 `agents/openai.yaml` 已从模板回填完成

## 模块检查

每个首批模块至少满足：

- `domain` 不依赖 Flutter UI
- `application` 负责用例编排和 provider 暴露
- `infrastructure` 负责数据源、模型、仓储实现
- `presentation` 负责页面、组件、视图状态消费

## 验证检查

- `flutter pub get` 通过
- `dart run build_runner build --delete-conflicting-outputs` 通过
- `flutter analyze` 通过
- `flutter test` 通过，或至少有明确说明当前 smoke test 的覆盖边界

## 交付说明检查

- 已说明新增依赖及其用途
- 已说明哪些模块只是骨架
- 已说明项目内 `flutter-dev` 承接了哪些项目级约束
- 已列出仍待确认的 RD 缺口
- 已明确下一步优先实现顺序
