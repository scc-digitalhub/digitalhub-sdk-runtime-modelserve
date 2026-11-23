# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderVllmserveText
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe
from digitalhub_runtime_modelserve.entities.task.vllmservetext_serve.entity import TaskVllmservetextServe


class TaskVllmservetextServeBuilder(TaskBuilder, RuntimeEntityBuilderVllmserveText):
    """
    TaskVllmservetextServe builder.
    """

    ENTITY_CLASS = TaskVllmservetextServe
    ENTITY_SPEC_CLASS = TaskSpecModelserveServe
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_VLLMSERVETEXT_SERVE.value
