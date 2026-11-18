# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderSklearnserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.modelserve.spec import FunctionSpecModelserve
from digitalhub_runtime_modelserve.entities.function.sklearnserve.entity import FunctionSklearnserve


class FunctionSklearnserveBuilder(FunctionBuilder, RuntimeEntityBuilderSklearnserve):
    """
    FunctionSklearnserve builder.
    """

    ENTITY_CLASS = FunctionSklearnserve
    ENTITY_SPEC_CLASS = FunctionSpecModelserve
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_SKLEARNSERVE.value
