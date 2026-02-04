# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunModelserveRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.spec import RunSpecMlflowserveBuildRun
    from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.status import RunStatusMlflowserveBuildRun


class RunMlflowserveBuildRun(RunModelserveRun):
    """
    RunMlflowserveBuildRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecMlflowserveBuildRun
        self.status: RunStatusMlflowserveBuildRun
