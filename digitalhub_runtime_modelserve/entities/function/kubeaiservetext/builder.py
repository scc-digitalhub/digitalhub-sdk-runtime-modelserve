# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import FunctionBuilder, Status

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderKubeaiserveText
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.entity import FunctionKubeaiserveText
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.spec import (
    FunctionSpecKubeaiserveText,
)


class FunctionKubeaiserveTextBuilder(FunctionBuilder, RuntimeEntityBuilderKubeaiserveText):
    """
    FunctionKubeaiserveText builder.
    """

    ENTITY_CLASS = FunctionKubeaiserveText
    ENTITY_SPEC_CLASS = FunctionSpecKubeaiserveText
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_KUBEAISERVETEXT.value
