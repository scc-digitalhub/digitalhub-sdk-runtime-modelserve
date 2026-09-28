# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.builder import (
    FunctionKubeaiserveSpeechtotextBuilder,
)

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.entity import (
        FunctionKubeaiserveSpeechtotext,
    )


def new_function_kubeaiservespeechtotext(
    project: str,
    name: str,
    model_name: str | None = None,
    image: str | None = None,
    url: str | None = None,
    adapters: list[dict] | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
) -> FunctionKubeaiserveSpeechtotext:
    """Create a KubeAI speech-to-text function entity."""
    return new_function(
        project=project,
        name=name,
        kind=FunctionKubeaiserveSpeechtotextBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        model_name=model_name,
        image=image,
        url=url,
        adapters=adapters,
    )
