# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import (
    TaskSpecModelserveServe,
    TaskValidatorModelserveServe,
)


class TaskSpecMlflowserveBuild(TaskSpecModelserveServe):
    """
    TaskSpecMlflowserveBuild specifications.
    """

    def __init__(
        self,
        function: str,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        replicas: int | None = None,
        service_type: str | None = None,
        service_name: str | None = None,
        instructions: list[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            function=function,
            volumes=volumes,
            resources=resources,
            envs=envs,
            secrets=secrets,
            profile=profile,
            replicas=replicas,
            service_type=service_type,
            service_name=service_name,
            **kwargs,
        )
        self.instructions = instructions


class TaskValidatorMlflowserveBuild(TaskValidatorModelserveServe):
    """
    TaskValidatorMlflowserveBuild validator.
    """

    instructions: list[str] | None = None
    """Instructions for the MLflow model serving build task."""
