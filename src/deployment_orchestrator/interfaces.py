"""Initial application boundary for Deployment Orchestrator.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class ReleaseGate:
    def evaluate(self, evidence: dict) -> dict:
        """Approve or reject promotion based on immutable artifact evidence."""
        raise NotImplementedError("Runtime implementation is in development.")

    def rollback_plan(self, release_id: str) -> dict:
        """Describe rollback limits including schema compatibility."""
        raise NotImplementedError("Runtime implementation is in development.")
