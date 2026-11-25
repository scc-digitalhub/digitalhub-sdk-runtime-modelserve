# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Spec

from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter


class FunctionSpecSglangserve(Spec):
    """FunctionSpecSglangserve specifications."""

    image: str | None = None
    path: str
    adapters: list[VLLMAdapter] | None = None
