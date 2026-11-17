# ADR 0001: System boundaries and implementation approach

Status: proposed / decision not yet made.

## Context
Design delivery for WorkshopHub so the same tested artifact moves through staging and a lab production environment. A deployment is a traceable change with verification and recovery.

## Decision questions
- Push deployment versus GitOps promotion
- Artifact provenance and promotion gates
- Rollback versus forward fix

## Options
1. Small local implementation with synthetic adapters.
2. Integrated lab with real dependencies in a disposable environment.
3. A justified alternative to be supplied during design.

## Decision
Pending. Start by evaluating the smallest approach that can demonstrate the core invariant.

## Consequences to assess
Correctness, complexity, cost, recovery, trust boundaries, portability and maintenance burden.

## Evidence needed
A failure experiment, a working implementation slice and a comparison of the alternatives.

## Revisit when
Document a concrete load, team, correctness or operational constraint that invalidates the selected approach.
