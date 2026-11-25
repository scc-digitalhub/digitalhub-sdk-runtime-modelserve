# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderTeiserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunServiceUrlsRun
from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun
from digitalhub_runtime_modelserve.entities.run.teiserve_run.spec import RunSpecTeiserveRun


class RunTeiserveRunBuilder(RunBuilder, RuntimeEntityBuilderTeiserve):
    """
    RunTeiserveRun builder.
    """

    ENTITY_CLASS = RunServiceUrlsRun
    ENTITY_SPEC_CLASS = RunSpecTeiserveRun
    ENTITY_STATUS_CLASS = RunStatusModelserveRun
    ENTITY_KIND = EntityKinds.RUN_TEISERVE_SERVE.value
