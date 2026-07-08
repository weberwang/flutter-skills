# Fixed Plugin Stack

Use this stack by default for every initialized Flutter app.

## Runtime Dependencies

| Package | Role | Required use |
|---|---|---|
| `flutter_riverpod` | Provider runtime | App-wide dependency injection and state containers |
| `hooks_riverpod` | HookConsumer widgets | UI that needs both hooks and providers |
| `flutter_hooks` | Local widget lifecycle | Controllers, focus nodes, animation controllers, local ephemeral state |
| `freezed_annotation` | Generated immutable APIs | Models, state objects, unions, failures |
| `json_annotation` | Serialization annotations | API DTOs and persisted JSON |
| `fpdart` | Typed functional flows | `Either`, `TaskEither`, `Option` for domain and repository failures |
| `flutter_screenutil` | Responsive sizing | App-level scale helpers and token mapping |

## Dev Dependencies

| Package | Role |
|---|---|
| `build_runner` | Code generation runner |
| `freezed` | Freezed generator |
| `json_serializable` | JSON generator |
| `riverpod_lint` | Riverpod rules |
| `custom_lint` | Lint runner |

## Commands

```bash
flutter pub add flutter_riverpod hooks_riverpod flutter_hooks freezed_annotation json_annotation fpdart flutter_screenutil
flutter pub add --dev build_runner freezed json_serializable riverpod_lint custom_lint
dart run build_runner build --delete-conflicting-outputs
flutter analyze
flutter test
```

## Package Selection Rules

- Do not add another state management package.
- Do not add another result or Either package.
- Do not handwrite JSON serialization for generated DTOs.
- Do not handwrite copy, equality, union, or immutable state boilerplate that Freezed can generate.
- Use annotations and `build_runner` for models, DTOs, unions, state objects, failures, and JSON serialization.
- Do not create custom responsive scaling when ScreenUtil and design tokens cover the need.
- Before adding any package, check whether the fixed stack or existing project packages already solve it.
