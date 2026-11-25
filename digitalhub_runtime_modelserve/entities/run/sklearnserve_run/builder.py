# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import RunBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderSklearnserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.entity import RunSklearnserveRun
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.spec import (
    RunSpecSklearnserveRun,
)


class RunSklearnserveRunBuilder(RunBuilder, RuntimeEntityBuilderSklearnserve):
    """
    RunSklearnserveRunBuilder runer.
    """

    ENTITY_CLASS = RunSklearnserveRun
    ENTITY_SPEC_CLASS = RunSpecSklearnserveRun
    ENTITY_STATUS_CLASS = RunStatusModelserveRun
    ENTITY_KIND = EntityKinds.RUN_SKLEARNSERVE_SERVE.value
