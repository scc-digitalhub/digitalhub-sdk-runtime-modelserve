# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecModelserve(FunctionSpec):
    """
    FunctionSpecModelserve specifications.
    """

    def __init__(
        self,
        path: str | None = None,
        model_name: str | None = None,
        image: str | None = None,
    ) -> None:
        super().__init__()
        self.path = path
        self.model_name = model_name
        self.image = image


class FunctionValidatorModelserve(FunctionValidator):
    """
    FunctionValidatorModelserve validator.
    """

    image: str | None = None
    "Image where the function will be executed"

    model_name: str | None = None
    "Name of the model to be served"

    path: str | None = None
    "Path to the model to be served"
