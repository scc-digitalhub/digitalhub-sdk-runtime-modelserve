# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunSpecFunction

from digitalhub_runtime_modelserve.entities._mixin.execution.spec import KubeaiServeSpecMixin, ModelserveServeSpecMixin


class RunSpecKubeaiserveRun(RunSpecFunction, ModelserveServeSpecMixin, KubeaiServeSpecMixin):
    """RunSpecKubeaiserveRun specifications."""

    adapters: list[dict] | None = None
    url: str | None = None
    cache_profile: str | None = None
