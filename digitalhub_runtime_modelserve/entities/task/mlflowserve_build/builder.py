# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import Status, TaskBuilder

from digitalhub_runtime_modelserve.entities._base.runtime_entity.builder import RuntimeEntityBuilderMlflowserve
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.entity import TaskMlflowserveBuild
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.spec import (
    TaskSpecMlflowserveBuild,
)


class TaskMlflowserveBuildBuilder(TaskBuilder, RuntimeEntityBuilderMlflowserve):
    """
    TaskMlflowserveBuild builder.
    """

    ENTITY_CLASS = TaskMlflowserveBuild
    ENTITY_SPEC_CLASS = TaskSpecMlflowserveBuild
    ENTITY_STATUS_CLASS = Status
    ENTITY_KIND = EntityKinds.TASK_MLFLOWSERVE_BUILD.value
