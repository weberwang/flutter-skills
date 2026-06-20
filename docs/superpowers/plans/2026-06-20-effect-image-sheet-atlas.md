# Effect Image Sheet Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在现有 Flutter 工作流文档与测试中加入“生成效果图时同步生成透明背景、仅含 UI 层、可切割的 sheet atlas”的明确规则，并同时覆盖全局阶段与模块阶段。

**Architecture:** 不新增工作流阶段，只在现有效果图生成节点补充强制伴生产物契约。通过更新 orchestrator 主文档、路由/状态/硬规则/asset-atlas 参考文档，以及规则回归测试，保证 atlas 是 UI-only、透明背景、附带 manifest、且不替代逐资源独立生成主流程。

**Tech Stack:** Markdown 文档、Python `unittest`

---

### Task 1: 更新主流程文档与总技能约束

**Files:**
- Modify: `D:\Git\flutter-skills\README.md`
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\SKILL.md`

- [ ] **Step 1: 写出 README 与总技能文档中的目标断言**

需要明确补入这些约束：

```text
效果图生成时必须同步生成 UI-only sheet atlas
sheet atlas 必须是 transparent background
sheet atlas 必须附带 cut-ready manifest
全局阶段与模块阶段都要执行
atlas 是伴生产物，不替代逐资源独立生成
```

- [ ] **Step 2: 修改 README**

在共享效果图、模块效果图、资源生成规则附近补入：

```text
共享阶段：代表页最终效果图和范围内页面效果图生成时，同步生成透明背景的 UI-only sheet atlas 与 manifest
模块阶段：实现期模块效果图生成时，同步生成透明背景的 UI-only sheet atlas 与 manifest
atlas 只保留 UI 层，不含数据层，后续独立 bitmap 资源仍按逐资源流程确认与生成
```

- [ ] **Step 3: 修改 orchestrator 主技能文档**

在 `Asset Resource Boundary`、shared/global flow、module implementation flow 等位置补入：

```text
atlas 只保留 UI shell / stable visual regions
runtime data regions must stay placeholder_only or data_excluded_placeholder
atlas main sheet must use transparent background
each atlas must ship with a cut-ready manifest
do not treat atlas as final runtime asset pack
```

- [ ] **Step 4: 运行目标测试确认当前文档改动未引入现有规则回退**

Run: `rtk python -m unittest tests.test_commercial_product_ui_constraints tests.test_human_final_app_acceptance -v`
Expected: 现有两组测试继续通过

### Task 2: 更新路由、状态、硬规则与 atlas 参考契约

**Files:**
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\references\asset-atlas-flow.md`
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\references\routing-rules.md`
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\references\workflow-states.md`
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\references\hard-rules.md`
- Modify: `D:\Git\flutter-skills\skills\flutter-workflow-orchestrator\references\global-asset-catalog-contract.md`

- [ ] **Step 1: 先补 asset-atlas-flow 契约**

必须加入：

```text
shared/module effect-image generation also creates a UI-only transparent sheet atlas
exclude runtime-data regions from atlas
atlas must include slice manifest with bounds/background_mode/slice_type/cut_safe
atlas is a slicing baseline, not the final asset pack
```

- [ ] **Step 2: 修改 routing-rules**

在 shared 与 module 的 effect-image / asset-resource 路由位置补入：

```text
生成效果图时同步生成 atlas
若 atlas 或 manifest 缺失，不能声明对应效果图证据完整
atlas background must remain transparent
```

- [ ] **Step 3: 修改 workflow-states**

在 `global_effect_images_ready` 与 `implementing` 等状态说明中补入：

```text
effect-image evidence now includes matching UI-only transparent atlas artifacts
```

- [ ] **Step 4: 修改 hard-rules 与 catalog contract**

硬规则至少补入：

```text
Do not treat a page effect-image generation step as complete before its matching UI-only transparent atlas and manifest exist.
Do not bake runtime data layers into the atlas.
Do not use a non-transparent atlas background.
```

catalog contract 至少补入 atlas 记录说明或字段约束，使 manifest / atlas 路径能被稳定记录。

- [ ] **Step 5: 运行新增目标测试前的关键回归**

Run: `rtk python -m unittest tests.test_commercial_product_ui_constraints tests.test_human_final_app_acceptance -v`
Expected: 继续通过

### Task 3: 增加 atlas 规则回归测试

**Files:**
- Create: `D:\Git\flutter-skills\tests\test_effect_image_sheet_atlas_rules.py`

- [ ] **Step 1: 先写失败测试**

```python
"""验证效果图伴生 UI-only 透明 atlas 规则不会从工作流文档中丢失。"""

from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
ORCHESTRATOR = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "SKILL.md"
ROUTING_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "routing-rules.md"
HARD_RULES = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "hard-rules.md"
ASSET_ATLAS_FLOW = REPO_ROOT / "skills" / "flutter-workflow-orchestrator" / "references" / "asset-atlas-flow.md"


class EffectImageSheetAtlasRulesTest(unittest.TestCase):
    """验证效果图伴生 atlas 的范围、透明背景和可切割约束。"""

    def test_readme_mentions_shared_and_module_sheet_atlas(self) -> None:
        content = README.read_text(encoding="utf-8")
        self.assertIn("sheet atlas", content)
        self.assertIn("透明背景", content)

    def test_orchestrator_mentions_ui_only_transparent_atlas(self) -> None:
        content = ORCHESTRATOR.read_text(encoding="utf-8")
        self.assertIn("UI-only", content)
        self.assertIn("transparent background", content)

    def test_routing_rules_require_atlas_with_effect_images(self) -> None:
        content = ROUTING_RULES.read_text(encoding="utf-8")
        self.assertIn("matching UI-only transparent atlas", content)

    def test_hard_rules_block_missing_or_opaque_atlas(self) -> None:
        content = HARD_RULES.read_text(encoding="utf-8")
        self.assertIn("non-transparent atlas background", content)

    def test_asset_atlas_flow_mentions_manifest_and_data_exclusion(self) -> None:
        content = ASSET_ATLAS_FLOW.read_text(encoding="utf-8")
        self.assertIn("runtime-data", content)
        self.assertIn("cut-ready manifest", content)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: 运行失败测试确认断言真的能抓住缺失**

Run: `rtk python -m unittest tests.test_effect_image_sheet_atlas_rules -v`
Expected: FAIL，因为对应文档片段尚未全部落入

- [ ] **Step 3: 只写最小实现让测试通过**

实现方式：仅修改本计划前两项中的文档，不新增多余测试帮助层，不改无关测试。

- [ ] **Step 4: 再跑 atlas 测试确认通过**

Run: `rtk python -m unittest tests.test_effect_image_sheet_atlas_rules -v`
Expected: PASS

### Task 4: 完整验证

**Files:**
- Test: `D:\Git\flutter-skills\tests\test_effect_image_sheet_atlas_rules.py`
- Test: `D:\Git\flutter-skills\tests\test_commercial_product_ui_constraints.py`
- Test: `D:\Git\flutter-skills\tests\test_human_final_app_acceptance.py`

- [ ] **Step 1: 运行本次相关测试全集**

Run: `rtk python -m unittest tests.test_effect_image_sheet_atlas_rules tests.test_commercial_product_ui_constraints tests.test_human_final_app_acceptance -v`
Expected: 全部通过

- [ ] **Step 2: 检查 diff 只覆盖本次需求**

Run: `rtk git diff -- README.md skills/flutter-workflow-orchestrator tests`
Expected: 只出现 atlas 规则与测试改动

- [ ] **Step 3: 总结结果并等待提交决策**

输出：

```text
已完成文档契约与测试回归。
如工作区存在可提交改动，再提醒用户选择：
1：仅提交
2：提交并推送
3：忽略
```
