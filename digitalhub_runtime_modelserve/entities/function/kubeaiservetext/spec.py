# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.function.kubeaiserve.spec import (
    FunctionSpecKubeaiserve,
)
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.enums import KubeaiEngine, KubeaiFeature


class FunctionSpecKubeaiserveText(FunctionSpecKubeaiserve):
    """
    FunctionSpecKubeaiserveText specifications.
    """

    features: list[KubeaiFeature] | None = None
    engine: KubeaiEngine | None = None
