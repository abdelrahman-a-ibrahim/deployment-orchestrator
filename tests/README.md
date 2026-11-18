# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- Staging and release reference the same image digest.
- Untrusted PR code never receives deployment credentials.
- A failed health gate prevents successful release status.
- Rollback documentation separates reversible code changes from data changes.

## Failure coverage
- Fail staging verification after an image is published.
- Attempt promotion with a digest that lacks test evidence.
- Revoke deployment identity during a release.
- Roll back an application after an irreversible schema change and explain the limit.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.
