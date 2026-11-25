# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import FunctionBuilder, Status

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmserveText
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
from digitalhub_runtime_modelserve.entities.function.vllmservetext.entity import FunctionVllmservetext


class FunctionVllmservetextBuilder(FunctionBuilder, RuntimeEntityBuilderVllmserveText):
    """
    FunctionVllmservetext builder.
    """

    ENTITY_CLASS = FunctionVllmservetext
    ENTITY_SPEC_CLASS = FunctionSpecVllmserve
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_VLLMSERVETEXT.value
