# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import (
    RuntimeEntityBuilderKubeaiserveSpeechtotext,
)
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.kubeaiserve_serve.spec import TaskSpecKubeaiserveServe
from digitalhub_runtime_modelserve.entities.task.kubeaiservespeechtotext_serve.entity import (
    TaskKubeaiserveSpeechtotextServe,
)


class TaskKubeaiserveSpeechtotextServeBuilder(TaskBuilder, RuntimeEntityBuilderKubeaiserveSpeechtotext):
    """
    TaskKubeaiserveSpeechtotextServe builder.
    """

    ENTITY_CLASS = TaskKubeaiserveSpeechtotextServe
    ENTITY_SPEC_CLASS = TaskSpecKubeaiserveServe
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_KUBEAISERVESPEECHTOTEXT_SERVE.value
