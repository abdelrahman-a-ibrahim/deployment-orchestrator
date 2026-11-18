# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Fail staging verification after an image is published.
- Attempt promotion with a digest that lacks test evidence.
- Revoke deployment identity during a release.
- Roll back an application after an irreversible schema change and explain the limit.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- Staging and release reference the same image digest.
- Untrusted PR code never receives deployment credentials.
- A failed health gate prevents successful release status.
- Rollback documentation separates reversible code changes from data changes.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.
