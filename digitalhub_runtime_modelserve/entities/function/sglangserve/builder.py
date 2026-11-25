# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import FunctionBuilder, Status

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderSglangserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve
from digitalhub_runtime_modelserve.entities.function.sglangserve.spec import FunctionSpecSglangserve


class FunctionSglangserveBuilder(FunctionBuilder, RuntimeEntityBuilderSglangserve):
    """
    FunctionSglangserve builder.
    """

    ENTITY_CLASS = FunctionModelserve
    ENTITY_SPEC_CLASS = FunctionSpecSglangserve
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_SGLANGSERVE.value
