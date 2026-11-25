# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve


def new_function_teiserve(
    project: str,
    name: str,
    path: str | None = None,
    image: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionModelserve:
    """
    Create a Text Embeddings Inference serving function entity.

    Examples
    --------
    Create a serving function for a registered model:

    ```python
    import digitalhub as dh

    model = dh.register_huggingface(project="my-project", source="hf://BAAI/bge-small-en-v1.5")
    function = dh.new_function_teiserve(
        project="my-project",
        name="embedding-service",
        path=model.key,
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=EntityKinds.FUNCTION_TEISERVE.value,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        image=image,
    )
