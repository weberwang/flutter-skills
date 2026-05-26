# Flutter Technical Solution Template

## Use This File For

- building the main body of the Flutter研发文档
- keeping the document complete enough for design review and development kickoff
- forcing every critical section to include recommendation, alternatives, and trade-offs

## Default Document Skeleton

Use this chapter order unless the request clearly needs a smaller subset:

0. 文档信息
1. PRD 需求理解
2. 假设前提与待确认项
3. 业务流程与页面范围
4. 总体技术架构
5. Flutter 客户端详细技术方案
6. 第三方包选型与最佳搭档
7. 后端协作与接口契约要求
8. 数据与安全方案
9. 埋点、监控与运营支持
10. 测试与质量保障
11. 实施计划与里程碑
12. 风险清单与替代方案
13. 最终结论

## Chapter Writing Rules

For every critical chapter, include:

- `推荐方案`
- `备选方案`
- `取舍理由`

This is required for architecture, state management, routing, networking, storage, authentication, analytics, monitoring, and rollout decisions.

## Section Guidance

### 1. PRD 需求理解

Summarize:

- product goal
- target users
- main scenarios
- in-scope functions
- explicit non-goals

### 2. 假设前提与待确认项

Use this section whenever missing information would change the plan. Do not bury assumptions later in the document.

### 3. 业务流程与页面范围

Cover:

- main user journey
- exception flows
- page list or module list
- navigation relations
- key state transitions

### 4. 总体技术架构

Explain:

- why the proposed layering fits this product
- how modules should be bounded
- how Flutter client, backend, third-party services, analytics, and monitoring connect

### 5. Flutter 客户端详细技术方案

Cover at least:

- project structure
- state management
- routing and guards
- network layer
- model serialization
- local storage and secure storage
- login state and session refresh
- error handling and fallback strategy
- configuration, theme, i18n, and permissions
- media, upload/download, push, deep links, real-time if needed
- performance and testability

### 6. 第三方包选型与最佳搭档

Do not write a package dump. Use capability domains and package stacks.

### 7. 后端协作与接口契约要求

Call out:

- auth model
- error schema
- pagination rules
- timestamp and timezone conventions
- retry and idempotency expectations
- upload/download conventions
- real-time contract boundaries

### 8. 数据与安全方案

Cover:

- sensitive data handling
- token storage principles
- local data retention
- privacy and logging redaction
- risk control boundaries

### 9. 埋点、监控与运营支持

Cover:

- event taxonomy
- funnel suggestions
- crash and performance monitoring
- alerting expectations
- remote config, A/B, gray rollout, if relevant

### 10. 测试与质量保障

Cover:

- unit tests
- widget or integration tests
- contract and joint-debug checks
- regression focus areas
- pre-release checks

### 11. 实施计划与里程碑

Break the work into execution phases and call out parallelizable streams and blockers.

### 12. 风险清单与替代方案

Make risks concrete:

- technical risk
- collaboration risk
- performance risk
- release risk

### 13. 最终结论

Close with:

- recommended main plan
- why this is the recommended path
- top 3-5 questions to confirm next

## Writing Tone

- Write like a lead engineer preparing a reviewable design doc.
- Prefer direct statements over brainstorming language.
- Keep advice specific to the PRD, not generic to all Flutter apps.
