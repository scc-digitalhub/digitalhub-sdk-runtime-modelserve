# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import FunctionBuilder, Status

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmserveSpeech
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.entity import FunctionVllmservespeech


class FunctionVllmservespeechBuilder(FunctionBuilder, RuntimeEntityBuilderVllmserveSpeech):
    """
    FunctionVllmservespeech builder.
    """

    ENTITY_CLASS = FunctionVllmservespeech
    ENTITY_SPEC_CLASS = FunctionSpecVllmserve
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.FUNCTION_VLLMSERVESPEECH.value
