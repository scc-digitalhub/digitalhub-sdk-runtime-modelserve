# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator

from digitalhub_runtime_modelserve.entities.function.kubeaiserve.models import KubeaiAdapter


class FunctionSpecKubeaiserve(FunctionSpec):
    """
    FunctionSpecKubeaiserve specifications.
    """

    def __init__(
        self,
        model_name: str | None = None,
        image: str | None = None,
        url: str | None = None,
        adapters: list[dict] | None = None,
        engine: str | None = None,
    ) -> None:
        super().__init__()
        self.model_name = model_name
        self.image = image
        self.url = url
        self.adapters = adapters
        self.engine = engine


class FunctionValidatorKubeaiserve(FunctionValidator):
    """
    FunctionValidatorKubeaiserve validator.
    """

    model_name: str | None = None
    "Name of the model to be served."

    url: str | None = None
    "URL of the model to be served."

    engine: str | None = None
    "Engine used for serving the model."

    image: str | None = None
    "Image where the function will be executed."

    adapters: list[KubeaiAdapter] | None = None
    "Adapters."
