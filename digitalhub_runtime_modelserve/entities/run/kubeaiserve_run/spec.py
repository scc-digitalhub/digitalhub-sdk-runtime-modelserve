# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec
from pydantic import Field

from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.models import KubeaiFile, Scaling


class RunSpecKubeaiserveRun(RunSpec):
    """RunSpecKubeaiserveRun specifications."""

    envs: dict | None = None
    image: str | None = None
    adapters: list[dict] | None = None
    url: str | None = None
    model_name: str | None = None
    processors: int | None = Field(default=None, ge=1)
    args: list[str] | None = None
    cache_profile: str | None = None
    files: list[KubeaiFile] | None = None
    scaling: Scaling | None = None
