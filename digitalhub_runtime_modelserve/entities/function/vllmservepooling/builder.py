# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmservePooling
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.entity import FunctionVllmservepooling
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.spec import (
    FunctionSpecVllmservepooling,
    FunctionValidatorVllmservepooling,
)
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.status import FunctionStatusVllmservepooling


class FunctionVllmservepoolingBuilder(FunctionBuilder, RuntimeEntityBuilderVllmservePooling):
    """
    FunctionVllmservepooling builder.
    """

    ENTITY_CLASS = FunctionVllmservepooling
    ENTITY_SPEC_CLASS = FunctionSpecVllmservepooling
    ENTITY_SPEC_VALIDATOR = FunctionValidatorVllmservepooling
    ENTITY_STATUS_CLASS = FunctionStatusVllmservepooling
    ENTITY_KIND = EntityKinds.FUNCTION_VLLMSERVEPOOLING.value
