# Flutter Release Checklist

## Verdict

- Ready / Not ready:
- Verification platform scope: `docs/architecture/verification-platforms.md`
- Build:

## App Identity

- App name:
- Bundle ID / application ID:
- Version and build number:
- Icons:
- Splash:

## Legal and Privacy

- Privacy policy:
- Terms:
- Consent:
- Data deletion:
- Account deletion:
- Tracking disclosure:
- App Store Privacy Nutrition Labels:
- Google Play Data Safety:
- Data collection disclosure matches SDK behavior:
- Export compliance / encryption declaration:
- iOS entitlements:
- Android permissions and manifest disclosures:

## Monetization

- Products configured:
- Purchase flow:
- Failure flow:
- Restore purchase:
- Receipt validation:
- Subscription status sync:

## Reliability

- Crash reporting:
- Analytics:
- Logging:
- Network failure handling:
- Offline behavior:
- Support channel:
- Alert owner:
- Rollback or hotfix plan:

## Store Assets

- Screenshots:
- Description:
- Keywords:
- Category:
- Age rating:
- Test account:

## CI and Supply Chain

- CI release workflow:
- Dependency license review:
- Signing key storage:
- Production secrets are not committed:

## Verification

- `fvm flutter analyze`:
- `fvm flutter test`:
- Integration tests:
- Required platform build and smoke evidence: `docs/architecture/verification-platforms.md`
- Final runtime validation: completed after all modules/pages and high-fidelity restoration; record platform evidence in `docs/architecture/verification-platforms.md`

## Blockers

| Blocker | Owner | Status |
|---|---|---|

## Non-Blocking Risks

| Risk | Mitigation |
|---|---|
