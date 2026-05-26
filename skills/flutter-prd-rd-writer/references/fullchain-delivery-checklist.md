# Fullchain Delivery Checklist

## Use This File For

- extending the研发文档 beyond Flutter client implementation
- making backend collaboration, operations, and release concerns explicit
- preventing “client-only”方案 from being mistaken for production-ready delivery

## Backend Collaboration

Call out:

- auth and permission model
- error response schema
- pagination conventions
- timestamp and timezone rules
- retry and idempotency expectations
- upload and download contracts
- signed URL or media processing assumptions
- real-time boundary: push, polling, WebSocket, or event stream

## Data and Security

Cover:

- sensitive local data handling
- token lifecycle and refresh boundaries
- privacy and log redaction
- minimal-permission principles
- anti-abuse or risk-control touchpoints
- audit or compliance expectations when relevant

## Analytics and Operations

Cover:

- event taxonomy by page, action, and business funnel
- key funnel metrics the app should support
- crash and performance monitoring expectations
- alert ownership and escalation assumptions
- remote config or feature flag needs
- A/B, gray rollout, staged release, or kill-switch requirements

## Release and Delivery

Call out:

- environment separation needs
- configuration management boundaries
- pre-release verification checkpoints
- app store or channel release risks
- rollback or disablement strategy

## Milestones and Cross-Team Dependencies

Encourage the研发文档 to name:

- which work can be parallelized
- which backend outputs are blockers
- which analytics or operations inputs are missing
- which risks could delay release even if Flutter implementation finishes

## Risk Prompts

Use these prompts when the PRD looks complete but delivery risk is still unclear:

- Does this feature require phased rollout or selective enablement?
- Is there any failure mode that needs business-visible fallback handling?
- Will operations need dashboards, alerts, or manual intervention playbooks?
- Are there security or compliance constraints that change local storage or logging?
- Does this release depend on backend sequencing, data migration, or vendor setup?
