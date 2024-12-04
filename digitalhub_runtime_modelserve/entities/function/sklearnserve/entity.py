from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_modelserve.entities.function.sklearnserve.spec import FunctionSpecSklearnserve
    from digitalhub_runtime_modelserve.entities.function.sklearnserve.status import FunctionStatusSklearnserve


class FunctionSklearnserve(FunctionModelserve):
    """
    FunctionSklearnserve class.
    """

    def __init__(
        self,
        project: str,
        name: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: FunctionSpecSklearnserve,
        status: FunctionStatusSklearnserve,
        user: str | None = None,
    ) -> None:
        super().__init__(project, name, uuid, kind, metadata, spec, status, user)

        self.spec: FunctionSpecSklearnserve
        self.status: FunctionStatusSklearnserve
