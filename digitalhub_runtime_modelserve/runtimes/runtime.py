from __future__ import annotations

from digitalhub.context.api import get_context
from digitalhub.runtimes._base import Runtime


class RuntimeModelserve(Runtime):
    """
    Runtime Model Serve base class.
    """

    def __init__(self, project: str) -> None:
        super().__init__(project)
        ctx = get_context(self.project)
        self.root = ctx.root

    def build(self, function: dict, task: dict, run: dict) -> dict:
        """
        Build run spec.

        Parameters
        ----------
        function : dict
            The function.
        task : dict
            The task.
        run : dict
            The run.

        Returns
        -------
        dict
            The run spec.
        """
        return {
            **function.get("spec", {}),
            **task.get("spec", {}),
            **run.get("spec", {}),
        }

    def run(self, run: dict) -> dict:
        """
        Run function.

        Returns
        -------
        dict
            Status of the executed run.
        """
        raise NotImplementedError("Local execution not implemented for Modelserve runtime.")
