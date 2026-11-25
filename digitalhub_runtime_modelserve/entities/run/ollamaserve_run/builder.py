# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderOllamaserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunServiceUrlsRun
from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun
from digitalhub_runtime_modelserve.entities.run.ollamaserve_run.spec import RunSpecOllamaserveRun


class RunOllamaserveRunBuilder(RunBuilder, RuntimeEntityBuilderOllamaserve):
    """
    RunOllamaserveRun builder.
    """

    ENTITY_CLASS = RunServiceUrlsRun
    ENTITY_SPEC_CLASS = RunSpecOllamaserveRun
    ENTITY_STATUS_CLASS = RunStatusModelserveRun
    ENTITY_KIND = EntityKinds.RUN_OLLAMASERVE_SERVE.value
