# Annotation Rules

## 用途

- 强制把可生成的样板代码交给注解与生成器
- 降低手写 provider、DTO、copyWith、API client 带来的漂移成本
- 规定“能用注解时必须用注解”，而不是把注解当成风格偏好

## 必须使用注解的场景

### Provider

- 使用 `@riverpod`
- 只要当前 provider 形态能被 `@riverpod` 表达，就必须使用 `@riverpod`
- 不手写大量样板 provider 族和依赖装配
- Provider 命名与 use case / 状态语义保持一致

### 状态对象、DTO、值对象

- 优先使用 `@freezed`
- 只要当前对象需要不可变状态、联合类型、copyWith、相等比较或可预测构造，就必须优先落到 `@freezed`
- 需要 JSON 时，接 `fromJson` / `toJson`
- 联合状态、失败模型、筛选条件等都优先走 `freezed`

### JSON 序列化

- 使用 `@JsonSerializable` 或 `freezed` 配套生成
- 只要模型需要稳定的 JSON 映射且现有注解链能覆盖，就禁止继续手写 `Map<String, dynamic>` 转换
- 不要手写大段 `Map<String, dynamic>` 转换

### API 声明

- 使用 `@RestApi`
- 只要接口仍属于当前 `dio` + `retrofit` 主链路，就必须使用 `@RestApi` 与方法注解声明
- 每个接口方法使用 `@GET`、`@POST`、`@PUT`、`@DELETE` 等注解
- 请求参数、分页参数、上传参数保持显式声明

## 强制判定原则

- 判断标准不是“手写也能做”，而是“现有批准的注解链是否已经能表达”
- 只要 `@riverpod`、`@freezed`、`@JsonSerializable`、`@RestApi` 中任一组合能覆盖当前契约，就必须走注解生成
- 只有在注解链无法表达目标结构，或会直接破坏当前项目约束时，才允许显式说明原因后走手写实现
- 这种例外必须被视为偏离基线，而不是默认选项

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
- 能走 `json_serializable` / `freezed` 却继续手写 `fromJson` / `toJson`
- 手写 API client，绕开 `retrofit`
- 一部分模型走生成，一部分模型继续手写 JSON，导致同层风格分裂

## 输出检查

每次初始化或新增 feature 后，至少确认：

- provider 已成功生成
- DTO / state 已成功生成
- API client 已成功生成
- `flutter analyze` 和 `flutter test` 没有被生成代码破坏
