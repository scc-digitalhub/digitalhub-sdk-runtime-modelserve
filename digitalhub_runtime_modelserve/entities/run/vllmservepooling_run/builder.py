# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmservePooling
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.entity import RunVllmservepoolingRun
from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.spec import (
    RunSpecVllmservepoolingRun,
    RunValidatorVllmservepoolingRun,
)
from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.status import RunStatusVllmservepoolingRun


class RunVllmservepoolingRunBuilder(RunBuilder, RuntimeEntityBuilderVllmservePooling):
    """
    RunVllmservepoolingRunBuilder builder.
    """

    ENTITY_CLASS = RunVllmservepoolingRun
    ENTITY_SPEC_CLASS = RunSpecVllmservepoolingRun
    ENTITY_SPEC_VALIDATOR = RunValidatorVllmservepoolingRun
    ENTITY_STATUS_CLASS = RunStatusVllmservepoolingRun
    ENTITY_KIND = EntityKinds.RUN_VLLMSERVEPOOLING_SERVE.value
