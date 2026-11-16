# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.function.modelserve.spec import (
    FunctionSpecModelserve,
)
from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter


class FunctionSpecVllmserve(FunctionSpecModelserve):
    """
    FunctionSpecVllmserve specifications.
    """

    adapters: list[VLLMAdapter] | None = None
    url: str | None = None
    use_cpu_image: bool | None = None
