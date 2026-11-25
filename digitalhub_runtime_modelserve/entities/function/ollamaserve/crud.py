# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.ollamaserve.builder import FunctionOllamaserveBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve


def new_function_ollamaserve(
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
    Create a Ollama serving function entity.

    Examples
    --------
    Create a serving function for a registered model:

    ```python
    import digitalhub as dh

    model = dh.register_ollama(project="my-project", source="ollama://llama3:latest")
    function = dh.new_function_ollamaserve(
        project="my-project",
        name="llama-service",
        path=model.key,
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=FunctionOllamaserveBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        image=image,
    )
