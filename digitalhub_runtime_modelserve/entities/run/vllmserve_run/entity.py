# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunServiceUrlsRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.vllmserve_run.spec import RunSpecVllmserveRun
    from digitalhub_runtime_modelserve.entities.run.vllmserve_run.status import RunStatusVllmserveRun


class RunVllmserveRun(RunServiceUrlsRun):
    """
    RunVllmserveRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecVllmserveRun
        self.status: RunStatusVllmserveRun
