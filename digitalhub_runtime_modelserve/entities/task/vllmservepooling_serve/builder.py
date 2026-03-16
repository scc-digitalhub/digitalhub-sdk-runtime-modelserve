# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmservePooling
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.entity import TaskVllmservepoolingServe
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.spec import (
    TaskSpecVllmservepoolingServe,
    TaskValidatorVllmservepoolingServe,
)
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.status import TaskStatusVllmservepoolingServe


class TaskVllmservepoolingServeBuilder(TaskBuilder, RuntimeEntityBuilderVllmservePooling):
    """
    TaskVllmservepoolingServe builder.
    """

    ENTITY_CLASS = TaskVllmservepoolingServe
    ENTITY_SPEC_CLASS = TaskSpecVllmservepoolingServe
    ENTITY_SPEC_VALIDATOR = TaskValidatorVllmservepoolingServe
    ENTITY_STATUS_CLASS = TaskStatusVllmservepoolingServe
    ENTITY_KIND = EntityKinds.TASK_VLLMSERVEPOOLING_SERVE.value
