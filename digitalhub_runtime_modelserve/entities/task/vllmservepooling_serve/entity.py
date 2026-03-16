# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.task.vllmserve_serve.entity import TaskVllmserveServe

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.spec import TaskSpecVllmservepoolingServe
    from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.status import (
        TaskStatusVllmservepoolingServe,
    )


class TaskVllmservepoolingServe(TaskVllmserveServe):
    """
    TaskVllmservepoolingServe class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecVllmservepoolingServe
        self.status: TaskStatusVllmservepoolingServe
