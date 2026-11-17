# CI/CD & Deployment Pipelines Lab

**Release evidence, artifact identity and controlled rollback**

> Status: foundation only / implementation not started. Independent educational project by Abdelrahman Ahmed. This repository is not a reconstruction of employer systems, a production deployment or proof of completed work.

## The engineering challenge

Design delivery for WorkshopHub so the same tested artifact moves through staging and a lab production environment. A deployment is a traceable change with verification and recovery.

This is a capstone for an experienced engineer. The goal is to defend tradeoffs, investigate failure and produce reproducible evidence, not just get a happy-path demo running.

**Technical focus:** GitHub Actions · CI/CD · Docker · GitOps · Release engineering.

## What exists in this first commit

- A project-specific architecture brief and decision questions.
- Five implementation milestones with explicit review gates.
- Failure experiments and acceptance criteria.
- Typed Python interface scaffolds. Methods deliberately raise `NotImplementedError`.
- One synthetic scenario fixture; it is an input, not a successful output or benchmark.
- Evidence and journal templates, an issue template, and syntax/JSON foundation checks.

## What you will build

1. Define branch/release rules and separate PR validation from privileged deployment. Describe forked PR trust and required checks.
2. Add meaningful unit/integration tests and reproducible image builds. Record the digest, dependency inventory and provenance.
3. Deploy the exact digest to staging using short-lived identity. Run smoke tests and verify configuration without logging secrets.
4. Promote with an approval gate, health criteria and failure handling. Pin third-party actions to reviewed commits when introduced.
5. Practice rollback and forward-fix scenarios, including incompatible schema changes. Measure deployment duration and recovery time.

## Start here

1. Read [the architecture brief](docs/architecture.md) and record the first decision in [ADR 0001](docs/adr/0001-system-boundaries.md).
2. Inspect [the synthetic scenario](examples/scenario.json) and [the interface boundary](src/delivery_pipelines_lab/interfaces.py).
3. Run the foundation checks from the repository root:

   ```sh
   python3 tools/check_foundation.py
   ```

   Python 3.9+ is sufficient for these standard-library checks. They parse Python and JSON; they do **not** validate runtime behavior, deployment safety, protocol compliance or completion.
4. Create a feature branch, implement milestone 1 and add behavior tests before adapters.
5. Follow [the milestone backlog](docs/milestones.md). Select and pin implementation dependencies when you introduce them; none are installed by this scaffold.
6. Complete [the failure lab](docs/failure-lab.md), gather [evidence](docs/evidence/README.md) and review [acceptance criteria](docs/acceptance.md).

There is deliberately no `deploy`, `apply`, paid API call, installed cloud SDK or working runtime in this initial commit.

## Architecture at a glance

```text
Commit -> checks -> immutable image -> staging verification
                                            |
                                      approval -> promotion -> health gate
```

This is a proposed lab architecture. [The design brief](docs/architecture.md) identifies decisions still to make.

## Learning prerequisites

- `application-engineering-lab` (a suggested learning prerequisite; no runtime dependency is wired in)
- `kubernetes-addons-lab` (a suggested learning prerequisite; no runtime dependency is wired in)

Repositories are separate and can evolve independently. If you connect them later, exchange versioned fixtures or contracts; do not rely on sibling-relative imports. You can implement a standalone synthetic adapter first.

## What makes this substantial

- Push deployment versus GitOps promotion
- Artifact provenance and promotion gates
- Rollback versus forward fix

You must explain what happens on retries, partial failure, concurrent operations and recovery. Record what your test environment cannot prove. No result is accepted simply because a dashboard is green.

## Definition of done

- Staging and release reference the same image digest.
- Untrusted PR code never receives deployment credentials.
- A failed health gate prevents successful release status.
- Rollback documentation separates reversible code changes from data changes.

Also supply installation/reproduction instructions, dependency versions, meaningful behavior tests, cleanup instructions, an architecture decision log and evidence from a repeatable demonstration. A checklist or syntax check alone does not satisfy completion.

## Advanced extensions

- Canary rollout with a measurable abort rule
- SBOM and dependency policy gates
- Reusable workflows with least privilege
- Ephemeral integration environments

Extensions follow a working baseline; they are not requirements for the first milestone.

## Boundaries and costs

Use fictional services, synthetic inputs and a disposable sandbox. Do not copy employer repositories, runbooks, tickets, customer data, credentials or internal architecture. Real cloud/provider adapters are future work and may incur costs; [the operations plan](docs/operations.md) must identify account, region, budget, resource inventory and teardown before deployment. Budget alerts notify; they do not constitute a hard spending cap.

## Publishable evidence, when earned

A completed lab may support a portfolio case study labeled **independent project**. Share your original code, sanitized diagrams, measured results and a failure/recovery write-up. Employer experience and personal lab evidence remain separate. Never copy illustrative fixture values into a results claim.

## Primary references

- https://docs.github.com/en/actions/security-for-github-actions
- https://docs.docker.com/build/

Read current official documentation when selecting SDKs, images, tool versions and integrations. The scaffold intentionally does not guess compatible version combinations.

## Repository map

- `src/delivery_pipelines_lab/interfaces.py`
- `examples/scenario.json`
- `docs/architecture.md`
- `docs/milestones.md`
- `docs/failure-lab.md`
- `docs/acceptance.md`
- `docs/learning-journal.md`
- `docs/evidence/README.md`
- `docs/operations.md` — local/cloud boundaries and teardown plan.
- `docs/adr/` — decisions and alternatives.
- `tools/check_foundation.py` — syntax and fixture integrity only.

## Working agreement

Keep commits focused: `docs`, `feat`, `test`, `fix`, `ops`. Work on a feature branch and merge only after the milestone review. Consult [CONTRIBUTING.md](CONTRIBUTING.md). No open-source license has been chosen yet; see [NOTICE.md](NOTICE.md).
