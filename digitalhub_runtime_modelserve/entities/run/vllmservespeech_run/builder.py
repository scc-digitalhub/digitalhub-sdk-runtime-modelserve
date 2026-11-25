# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmserveSpeech
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.spec import RunSpecVllmserveRun
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.status import RunStatusVllmserveRun
from digitalhub_runtime_modelserve.entities.run.vllmservespeech_run.entity import RunVllmservespeechRun


class RunVllmservespeechRunBuilder(RunBuilder, RuntimeEntityBuilderVllmserveSpeech):
    """
    RunVllmservespeechRunBuilder builder.
    """

    ENTITY_CLASS = RunVllmservespeechRun
    ENTITY_SPEC_CLASS = RunSpecVllmserveRun
    ENTITY_STATUS_CLASS = RunStatusVllmserveRun
    ENTITY_KIND = EntityKinds.RUN_VLLMSERVESPEECH_SERVE.value
