# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A release-engineering project for building once and promoting the same immutable artifact across environments. It treats verification, deployment identity, approval, release traceability and rollback compatibility as first-class concerns.

## Component view
```text
Commit -> checks -> immutable image -> staging verification
                                            |
                                      approval -> promotion -> health gate
```

## Design decisions
- Push deployment versus GitOps promotion
- Artifact provenance and promotion gates
- Rollback versus forward fix

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/deployment_orchestrator/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.
