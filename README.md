# Deployment Orchestrator

Artifact-driven CI/CD and promotion workflows with release evidence, verification gates and recovery planning.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A release-engineering project for building once and promoting the same immutable artifact across environments. It treats verification, deployment identity, approval, release traceability and rollback compatibility as first-class concerns.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Immutable build artifacts with traceable source and verification evidence.
- PR validation separated from privileged deployment workflows.
- Digest-based staging deployment and gated promotion.
- Scoped deployment identity, provenance and release metadata.
- Post-deployment health verification and compatibility-aware rollback planning.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Commit -> checks -> immutable image -> staging verification
                                            |
                                      approval -> promotion -> health gate
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

GitHub Actions · CI/CD · Docker · GitOps · Release engineering.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/deployment-orchestrator.git
cd deployment-orchestrator
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/deployment_orchestrator/interfaces.py`](src/deployment_orchestrator/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- Staging and release reference the same image digest.
- Untrusted PR code never receives deployment credentials.
- A failed health gate prevents successful release status.
- Rollback documentation separates reversible code changes from data changes.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/deployment_orchestrator/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://docs.github.com/en/actions/security-for-github-actions
- https://docs.docker.com/build/
