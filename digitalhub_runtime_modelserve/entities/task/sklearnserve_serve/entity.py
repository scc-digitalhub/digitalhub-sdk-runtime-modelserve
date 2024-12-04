from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.entity import TaskModelserveServe

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.spec import TaskSpecSklearnserveServe
    from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.status import TaskStatusSklearnserveServe


class TaskSklearnserveServe(TaskModelserveServe):
    """
    TaskSklearnserveServe class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: TaskSpecSklearnserveServe,
        status: TaskStatusSklearnserveServe,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: TaskSpecSklearnserveServe
        self.status: TaskStatusSklearnserveServe
