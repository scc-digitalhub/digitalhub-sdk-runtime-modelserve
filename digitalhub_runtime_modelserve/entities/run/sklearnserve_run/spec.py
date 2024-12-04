from __future__ import annotations

from digitalhub_runtime_modelserve.entities.run.modelserve_run.spec import (
    RunSpecModelserveRun,
    RunValidatorModelserveRun,
)


class RunSpecSklearnserveRun(RunSpecModelserveRun):
    """RunSpecSklearnserveRun specifications."""


class RunValidatorSklearnserveRun(RunValidatorModelserveRun):
    """RunValidatorSklearnserveRun validator."""
