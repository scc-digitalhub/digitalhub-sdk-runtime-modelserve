# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpecFunction
from pydantic import Field

from digitalhub_runtime_modelserve.entities._mixin.execution.spec import ModelserveServeSpecMixin


class RunSpecTeiserveRun(RunSpecFunction, ModelserveServeSpecMixin):
    """RunSpecTeiserveRun specifications."""

    path: str | None = None
    model_name: str | None = Field(default=None, json_schema_extra={"default": ""})
