# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderOllamaserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.entity import TaskModelserveServe
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe


class TaskOllamaserveServeBuilder(TaskBuilder, RuntimeEntityBuilderOllamaserve):
    """
    TaskOllamaserveServe builder.
    """

    ENTITY_CLASS = TaskModelserveServe
    ENTITY_SPEC_CLASS = TaskSpecModelserveServe
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_OLLAMASERVE_SERVE.value
