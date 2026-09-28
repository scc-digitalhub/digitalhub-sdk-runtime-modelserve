# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function.crud import new_function

from digitalhub_runtime_modelserve.entities.function.sklearnserve.builder import FunctionSklearnserveBuilder

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.sklearnserve.entity import FunctionSklearnserve


def new_function_sklearnserve(
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
) -> FunctionSklearnserve:
    """Create a scikit-learn serving function entity."""
    return new_function(
        project=project,
        name=name,
        kind=FunctionSklearnserveBuilder.ENTITY_KIND,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        path=path,
        model_name=model_name,
        image=image,
    )
