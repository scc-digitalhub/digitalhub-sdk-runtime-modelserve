# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pydantic import Field

from digitalhub_runtime_modelserve.entities.function.modelserve.spec import (
    FunctionSpecModelserve,
    FunctionValidatorModelserve,
)

image_regex = r"^seldonio\/mlserver?:.*-sklearn$"


class FunctionSpecSklearnserve(FunctionSpecModelserve):
    """
    FunctionSpecSklearnserve specifications.
    """


class FunctionValidatorSklearnserve(FunctionValidatorModelserve):
    """
    FunctionValidatorSklearnserve validator.
    """

    image: str | None = Field(default=None, pattern=image_regex)
    "Function image"
