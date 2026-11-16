# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec

from digitalhub_runtime_modelserve.entities.function.kubeaiserve.models import KubeaiAdapter


class FunctionSpecKubeaiserve(FunctionSpec):
    """
    FunctionSpecKubeaiserve specifications.
    """

    model_name: str | None = None
    image: str | None = None
    url: str | None = None
    adapters: list[KubeaiAdapter] | None = None
