# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpecFunction

from digitalhub_runtime_modelserve.entities._mixin.execution.spec import (
    HuggingfaceServeSpecMixin,
    ModelserveServeSpecMixin,
)


class RunSpecHuggingfaceserveRun(
    RunSpecFunction,
    ModelserveServeSpecMixin,
    HuggingfaceServeSpecMixin,
):
    """RunSpecHuggingfaceserveRun specifications."""

    path: str | None = None
    args: list[str] | None = None
