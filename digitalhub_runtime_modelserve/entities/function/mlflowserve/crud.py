# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.mlflowserve.builder import FunctionMlflowserveBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.mlflowserve.entity import FunctionMlflowserve


def new_function_mlflowserve(
    project: str,
    name: str,
    path: str | None = None,
    model_name: str | None = None,
    image: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionMlflowserve:
    """
    Create an MLflow serving function entity.

    Examples
    --------
    Create a serving function for an MLflow model:

    ```python
    import digitalhub as dh

    function = dh.new_function_mlflowserve(
        project="my-project",
        name="fraud-detector-service",
        path="store://my-project/model/mlflow/fraud-detector:123e4567-e89b-42d3-a456-426614174000",
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=FunctionMlflowserveBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        model_name=model_name,
        image=image,
    )
