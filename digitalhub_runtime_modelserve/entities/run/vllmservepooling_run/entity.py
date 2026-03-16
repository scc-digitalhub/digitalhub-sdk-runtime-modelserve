# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.vllmserve_run.entity import RunVllmserveRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.spec import RunSpecVllmservepoolingRun
    from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.status import RunStatusVllmservepoolingRun


class RunVllmservepoolingRun(RunVllmserveRun):
    """
    RunVllmservepoolingRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecVllmservepoolingRun
        self.status: RunStatusVllmservepoolingRun
