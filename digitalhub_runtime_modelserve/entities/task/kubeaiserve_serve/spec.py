# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.models import Env
from digitalhub.entities.task._base.spec import TaskSpec, TaskValidator


class TaskSpecKubeaiserveServe(TaskSpec):
    """
    TaskSpecKubeaiserveServe specifications.
    """

    def __init__(
        self,
        function: str,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        **kwargs,
    ) -> None:
        self.function = function
        self.envs = envs
        self.secrets = secrets


class TaskValidatorKubeaiserveServe(TaskValidator):
    """
    TaskValidatorKubeaiserveServe validator.
    """

    function: str
    """The function string."""

    envs: list[Env] | None
    """The envs list of Env."""

    secrets: list[str] | None
    """The secrets list of string."""
