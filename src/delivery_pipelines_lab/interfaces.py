"""Proposed application boundary for CI/CD & Deployment Pipelines Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class ReleaseGate:
    def evaluate(self, evidence: dict) -> dict:
        """Approve or reject promotion based on immutable artifact evidence."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def rollback_plan(self, release_id: str) -> dict:
        """Describe rollback limits including schema compatibility."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

