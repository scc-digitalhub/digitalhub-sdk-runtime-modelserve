# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunModelserveRun

if typing.TYPE_CHECKING:

    from digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.spec import RunSpecHuggingfaceserveRun
    from digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.status import RunStatusHuggingfaceserveRun


class RunHuggingfaceserveRun(RunModelserveRun):
    """
    RunHuggingfaceserveRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecHuggingfaceserveRun
        self.status: RunStatusHuggingfaceserveRun
