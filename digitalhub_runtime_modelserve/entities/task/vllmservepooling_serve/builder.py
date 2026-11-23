# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmservePooling
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.entity import TaskVllmservepoolingServe


class TaskVllmservepoolingServeBuilder(TaskBuilder, RuntimeEntityBuilderVllmservePooling):
    """
    TaskVllmservepoolingServe builder.
    """

    ENTITY_CLASS = TaskVllmservepoolingServe
    ENTITY_SPEC_CLASS = TaskSpecModelserveServe
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_VLLMSERVEPOOLING_SERVE.value
