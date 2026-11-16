# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pydantic import Field

from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.models import KubeaiFile, Scaling
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe


class TaskSpecKubeaiserveServe(TaskSpecModelserveServe):
    """
    TaskSpecKubeaiserveServe specifications.
    """

    envs: dict | None = None
    image: str | None = None
    model_name: str | None = None
    args: list[str] | None = None
    processors: int | None = Field(default=None, ge=1)
    files: list[KubeaiFile] | None = None
    scaling: Scaling | None = None
