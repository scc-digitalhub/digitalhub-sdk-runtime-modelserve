from __future__ import annotations

from digitalhub_runtime_container.entities._base.runtime_entity.builder import RuntimeEntityBuilderContainer
from digitalhub_runtime_container.entities.task.container_job.entity import TaskContainerJob
from digitalhub_runtime_container.entities.task.container_job.spec import (
    TaskSpecContainerJob,
    TaskValidatorContainerJob,
)
from digitalhub_runtime_container.entities.task.container_job.status import TaskStatusContainerJob

from digitalhub.entities.task._base.builder import TaskBuilder


class TaskContainerJobBuilder(TaskBuilder, RuntimeEntityBuilderContainer):
    """
    TaskContainerJobBuilder jober.
    """

    ENTITY_CLASS = TaskContainerJob
    ENTITY_SPEC_CLASS = TaskSpecContainerJob
    ENTITY_SPEC_VALIDATOR = TaskValidatorContainerJob
    ENTITY_STATUS_CLASS = TaskStatusContainerJob
    ENTITY_KIND = "container+job"