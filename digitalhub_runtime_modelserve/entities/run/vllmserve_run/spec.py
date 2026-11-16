# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.run.modelserve_run.spec import (
    RunSpecModelserveRun,
)
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import ModelserveServeSpecMixin


class RunSpecVllmserveRun(RunSpecModelserveRun, ModelserveServeSpecMixin):
    """RunSpecVllmserveRun specifications."""

    url: str | None = None
    adapters: list[dict] | None = None
    args: list[str] | None = None
    enable_telemetry: bool = True
    use_cpu_image: bool = True
    storage_space: str | None = None
