# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Spec
from pydantic import Field

from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter


class FunctionSpecVllmserve(Spec):
    """
    FunctionSpecVllmserve specifications.
    """

    url: str
    model_name: str | None = Field(default=None, json_schema_extra={"default": "model"})
    adapters: list[VLLMAdapter] | None = None
    image: str | None = None
    use_cpu_image: bool | None = None
