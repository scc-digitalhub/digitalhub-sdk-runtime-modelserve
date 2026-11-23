# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.status import Status
from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderKubeaiserveText
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.kubeaiserve_serve.spec import TaskSpecKubeaiserveServe
from digitalhub_runtime_modelserve.entities.task.kubeaiservetext_serve.entity import TaskKubeaiserveTextServe


class TaskKubeaiserveTextServeBuilder(TaskBuilder, RuntimeEntityBuilderKubeaiserveText):
    """
    TaskKubeaiserveTextServe builder.
    """

    ENTITY_CLASS = TaskKubeaiserveTextServe
    ENTITY_SPEC_CLASS = TaskSpecKubeaiserveServe
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_KUBEAISERVETEXT_SERVE.value
