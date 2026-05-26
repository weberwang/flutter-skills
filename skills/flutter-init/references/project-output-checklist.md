# Project Output Checklist

## 目录检查

- 存在 `pubspec.yaml`，且依赖与 guardrails 对齐
- 存在 `lib/app`
- 存在 `lib/core`
- 存在 `lib/shared`
- 存在 `lib/features`
- 存在项目内 `skills/flutter-dev`
- 首批业务 feature 都已按 DDD 分层建好目录

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
- `skills/flutter-dev/SKILL.md` 与所需 `references/` 已从模板回填完成

## 插件处理检查

- 如果未传 `--force` 且插件尚未配置，首次插件配置已执行
- 如果未传 `--force` 且已有插件配置，现有插件配置未被重复覆盖
- 如果传了 `--force`，当前 RD 范围内插件已重新配置
- 插件版本已优先选择为与当前 Flutter SDK 兼容的最新版
- 插件重配后，后续初始化步骤仍然继续执行，没有在插件步骤提前结束

## Feature 检查

每个首批 feature 至少满足：

- `domain` 不依赖 Flutter UI
- `application` 负责用例编排和 provider 暴露
- `infrastructure` 负责数据源、模型、仓储实现
- `presentation` 负责页面、组件、视图状态消费

## 验证检查

- `flutter pub get` 通过
- `dart run build_runner build --delete-conflicting-outputs` 通过
- `flutter analyze` 通过
- `flutter test` 通过，或至少有明确说明当前 smoke test 的覆盖边界
- 插件和依赖没有遗留 Flutter SDK 兼容性错误

## 交付说明检查

- 已说明新增依赖及其用途
- 已说明哪些 feature 只是骨架
- 已说明 `--force` 是否生效，或是否执行了首次插件配置，以及对插件配置造成了什么影响
- 已说明插件或依赖版本是否为与当前 Flutter SDK 兼容的最新版，以及修复了哪些不兼容问题
- 已说明项目内 `flutter-dev` 承接了哪些项目级约束
- 已列出仍待确认的 RD 缺口
- 已明确下一步优先实现顺序
