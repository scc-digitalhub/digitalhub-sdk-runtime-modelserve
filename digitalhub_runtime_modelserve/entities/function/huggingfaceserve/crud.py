# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.builder import FunctionHuggingfaceserveBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.entity import FunctionHuggingfaceserve


def new_function_huggingfaceserve(
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
) -> FunctionHuggingfaceserve:
    """
    Create a Hugging Face serving function entity.

    Examples
    --------
    Create a serving function for a stored Hugging Face model:

    ```python
    import digitalhub as dh

    function = dh.new_function_huggingfaceserve(
        project="my-project",
        name="huggingface-service",
        path="store://my-project/model/huggingface/text-classifier:123e4567-e89b-42d3-a456-426614174000",
        model_name="text-classifier",
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=FunctionHuggingfaceserveBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        model_name=model_name,
        image=image,
    )
