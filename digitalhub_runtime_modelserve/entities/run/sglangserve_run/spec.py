# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec
from pydantic import Field

from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import ModelserveServeSpecMixin


class RunSpecSglangserveRun(RunSpec, ModelserveServeSpecMixin):
    """RunSpecSglangserveRun specifications."""

    path: str | None = None
    model_name: str | None = Field(default=None, json_schema_extra={"default": ""})
    adapters: list[VLLMAdapter] | None = None
