# Project Output Checklist

## 目录检查

- 存在 `pubspec.yaml`，且依赖与 guardrails 对齐
- 存在 `lib/app`
- 存在 `lib/core`
- 存在 `lib/shared`
- 存在 `lib/features`
- 存在与 `flutter-init` 同级的 `skills/flutter-dev`
- 首批业务 feature 都已按 DDD 分层建好目录

## 基础文件检查

- 如果项目原本不是仓库，`git init` 已执行
- 根目录存在 `.gitignore`
- `.gitignore` 已覆盖 `.dart_tool/`、`.packages`、`build/`、`.fvm/`、`.idea/`、`.vscode/`、`*.iml`、`.DS_Store`、`Thumbs.db`、`*.log`、`.agents`、`.claude`
- 默认 demo 已移除或已明确留待后续 `bootstrap code` 阶段替换
- 已清楚区分“目录初始化”与“bootstrap code”阶段
- 未在初始化阶段偷跑真实 app shell、启动入口、路由树或共享 wiring

## 代码生成检查

- 如果初始化阶段已经放入注解占位，相关 `@riverpod` / `@freezed` / `@JsonSerializable` / `@RestApi` 示例至少有一个可验证
- 如果当前阶段只做到目录占位，也允许暂不跑生成，但必须在交付说明里写明原因
- `skills/flutter-dev/SKILL.md` 与所需 `references/` 已在同级目录下从模板回填完成

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
- 如果当前占位已需要代码生成，`dart run build_runner build --delete-conflicting-outputs` 通过
- `flutter analyze` 通过，或至少明确说明因只完成目录初始化暂未引入可分析源码的边界
- `flutter test` 通过，或明确说明当前阶段尚未进入 bootstrap/业务代码，不以测试通过作为 `project_initialized` 前置条件
- 插件和依赖没有遗留 Flutter SDK 兼容性错误

## 交付说明检查

- 已说明新增依赖及其用途
- 已说明哪些 feature 只是骨架
- 已说明哪些文件只是目录占位、契约占位或非运行时 stub
- 已说明是否执行了 `git init`
- 已说明 `.gitignore` 是新建还是增量补齐
- 已说明新增了哪些常见忽略项与中间产物规则，例如 `.agents`、`.claude`、`.dart_tool/`、`build/`
- 已说明 `--force` 是否生效，或是否执行了首次插件配置，以及对插件配置造成了什么影响
- 已说明插件或依赖版本是否为与当前 Flutter SDK 兼容的最新版，以及修复了哪些不兼容问题
- 已说明同级 `flutter-dev` 承接了哪些项目级约束
- 已说明哪些内容被明确留给 `bootstrap code` 阶段
- 已列出仍待确认的 RD 缺口
- 已明确下一步优先实现顺序
