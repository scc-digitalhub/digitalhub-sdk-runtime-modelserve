# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.entity import TaskModelserveServe

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.spec import TaskSpecMlflowserveBuild
    from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.status import TaskStatusMlflowserveBuild


class TaskMlflowserveBuild(TaskModelserveServe):
    """
    TaskMlflowserveBuild class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: TaskSpecMlflowserveBuild
        self.status: TaskStatusMlflowserveBuild
