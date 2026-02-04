# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunModelserveRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.spec import RunSpecMlflowserveServeRun
    from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.status import RunStatusMlflowserveServeRun


class RunMlflowserveServeRun(RunModelserveRun):
    """
    RunMlflowserveServeRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecMlflowserveServeRun
        self.status: RunStatusMlflowserveServeRun
