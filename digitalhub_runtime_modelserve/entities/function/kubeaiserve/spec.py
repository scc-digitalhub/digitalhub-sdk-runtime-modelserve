# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.spec import Spec

from digitalhub_runtime_modelserve.entities.function.kubeaiserve.models import KubeaiAdapter


class FunctionSpecKubeaiserve(Spec):
    """
    FunctionSpecKubeaiserve specifications.
    """

    model_name: str | None = None
    image: str | None = None
    url: str | None = None
    adapters: list[KubeaiAdapter] | None = None
