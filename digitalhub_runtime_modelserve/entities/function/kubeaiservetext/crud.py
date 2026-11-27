# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Function


def new_function_kubeaiservetext(
    project: str,
    name: str,
    model_name: str | None = None,
    image: str | None = None,
    url: str | None = None,
    adapters: list[dict] | None = None,
    engine: str | None = None,
    features: list[dict] | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> Function:
    """
    Create a KubeAI text function entity.

    Examples
    --------
    Create a text-generation function using KubeAI:

    ```python
    import digitalhub as dh

    function = dh.new_function_kubeaiservetext(
        project="my-project",
        name="text-generation",
        url="hf://microsoft/DialoGPT-medium",
        features=["TextGeneration"],
        engine="VLLM",
    )
    ```
    """
    return new_function(
        project=project,
        name=name,
        kind=EntityKinds.FUNCTION_KUBEAISERVETEXT.value,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        model_name=model_name,
        image=image,
        url=url,
        adapters=adapters,
        engine=engine,
        features=features,
    )
