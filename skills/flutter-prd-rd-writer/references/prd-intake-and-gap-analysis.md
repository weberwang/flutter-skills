# PRD Intake and Gap Analysis

## Use This File For

- reading a PRD before proposing any Flutter技术方案
- identifying which missing details would materially change architecture, package selection, or delivery scope
- generating `假设前提` and `待确认项` instead of guessing

## Intake Order

Process the input in this order:

1. `产品目标`
2. `目标用户`
3. `核心场景`
4. `关键业务流程`
5. `范围内功能`
6. `明确不做`
7. `约束条件`
8. `外部依赖`

Do not jump to package recommendations before these are extracted.

## PRD Extraction Checklist

For each PRD, extract:

- the business outcome this feature or product is trying to create
- the primary and secondary user roles
- the main success path from entry to completion
- the main exception paths and failure states
- page or module scope implied by the requirement
- whether login, payment, upload, push, real-time, analytics, or approval flows are involved
- whether the request is MVP-oriented, growth-oriented, or enterprise-oriented

## Gap Analysis Rules

Flag a gap when any missing information would change:

- state management choice
- routing and guard design
- network, serialization, or caching strategy
- local storage or secure storage needs
- authentication or session refresh design
- analytics, monitoring, rollout, or release scope
- backend contract expectations

Do not treat minor copy, style, or static content uncertainty as architecture-blocking gaps.

## High-Impact Missing Information

Prioritize these questions when the PRD is incomplete:

- Is this an MVP, growth product, or complex enterprise product?
- Does the feature require login, multi-role access, or permission gating?
- Are there upload, download, media, push, deep link, or real-time capabilities?
- Is offline access or local-first behavior required?
- Does the product need analytics funnels, A/B support, remote config, or phased rollout?
- Are there security, privacy, audit, or compliance constraints?
- Are there backend constraints such as idempotency, pagination, retry rules, or signed URLs?

## Assumptions First

When key information is missing, output two sections before the main研发文档:

### 假设前提

List the assumptions you are making so the technical方案 can move forward.

Example shape:

```text
假设前提：
- 当前版本面向登录用户，不支持游客核心链路。
- 上传内容以图片和短视频为主，不要求离线编辑。
- 首期只支持单租户，不支持企业级多组织权限模型。
```

### 待确认项

List the questions that could materially change the plan.

Example shape:

```text
待确认项：
- 是否需要离线草稿和断点续传？
- 是否要求远程配置与灰度发布能力首期接入？
- 是否存在审计日志、风控规则或合规留痕要求？
```

## Output Discipline

- 如果信息不足，先明确说明“不足以直接拍板”的点。
- 如果某个待确认项不成立，要指出受影响的章节。
- 如果 PRD 同时混合多个独立子系统，先拆分范围，再写技术方案。
