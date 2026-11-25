# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.sglangserve.builder import FunctionSglangserveBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve


def new_function_sglangserve(
    project: str,
    name: str,
    path: str | None = None,
    image: str | None = None,
    adapters: list[dict] | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionModelserve:
    """
    Create a SGLang serving function entity.

    Examples
    --------
    Create a serving function for a registered model:

    ```python
    import digitalhub as dh

    model = dh.register_huggingface(project="my-project", source="hf://Qwen/Qwen2.5-0.5B-Instruct")
    function = dh.new_function_sglangserve(
        project="my-project",
        name="qwen-service",
        path=model.key,
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=FunctionSglangserveBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        image=image,
        adapters=adapters,
    )
