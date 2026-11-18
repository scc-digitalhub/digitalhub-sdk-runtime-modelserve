# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.entity import RunKubeaiserveRun

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.spec import RunSpecKubeaiserveTextRun
    from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun


class RunKubeaiserveTextRun(RunKubeaiserveRun):
    """
    RunKubeaiserveTextRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecKubeaiserveTextRun
        self.status: RunStatusModelserveRun
