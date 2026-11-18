# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import (
    RuntimeEntityBuilderKubeaiserveSpeechtotext,
)
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.kubeaiserve.spec import FunctionSpecKubeaiserve
from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.entity import (
    FunctionKubeaiserveSpeechtotext,
)


class FunctionKubeaiserveSpeechtotextBuilder(FunctionBuilder, RuntimeEntityBuilderKubeaiserveSpeechtotext):
    """
    FunctionKubeaiserveSpeechtotext builder.
    """

    ENTITY_CLASS = FunctionKubeaiserveSpeechtotext
    ENTITY_SPEC_CLASS = FunctionSpecKubeaiserve
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_KUBEAISERVESPEECHTOTEXT.value
