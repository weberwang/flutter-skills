# Annotation Rules

## 用途

- 强制把可生成的样板代码交给注解与生成器
- 降低手写 provider、DTO、copyWith、API client 带来的漂移成本

## 必须使用注解的场景

### Provider

- 使用 `@riverpod`
- 不手写大量样板 provider 族和依赖装配
- Provider 命名与 use case / 状态语义保持一致

### 状态对象、DTO、值对象

- 优先使用 `@freezed`
- 需要 JSON 时，接 `fromJson` / `toJson`
- 联合状态、失败模型、筛选条件等都优先走 `freezed`

### JSON 序列化

- 使用 `@JsonSerializable` 或 `freezed` 配套生成
- 不要手写大段 `Map<String, dynamic>` 转换

### API 声明

- 使用 `@RestApi`
- 每个接口方法使用 `@GET`、`@POST`、`@PUT`、`@DELETE` 等注解
- 请求参数、分页参数、上传参数保持显式声明

## 生成命令

初始化或新增注解后至少运行一次：

```bash
dart run build_runner build --delete-conflicting-outputs
```

需要持续开发时可使用：

```bash
dart run build_runner watch --delete-conflicting-outputs
```

## 生成文件规则

- 不手改 `.g.dart`
- 不手改 `.freezed.dart`
- 生成失败先修源文件与依赖，再重跑生成
- 不允许把生成器依赖加进来却从不执行

## 反模式

- 手写 provider 样板，绕开 `@riverpod`
- 手写 `copyWith`、相等比较、联合状态，绕开 `@freezed`
- 手写 API client，绕开 `retrofit`
- 一部分模型走生成，一部分模型继续手写 JSON，导致同层风格分裂

## 输出检查

每次初始化或新增模块后，至少确认：

- provider 已成功生成
- DTO / state 已成功生成
- API client 已成功生成
- `flutter analyze` 和 `flutter test` 没有被生成代码破坏
