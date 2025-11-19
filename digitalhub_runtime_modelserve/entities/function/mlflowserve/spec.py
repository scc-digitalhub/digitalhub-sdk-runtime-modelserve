# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional

from pydantic import Field

from digitalhub_runtime_modelserve.entities.function.modelserve.spec import (
    FunctionSpecModelserve,
    FunctionValidatorModelserve,
)

image_regex = r"^seldonio\/mlserver?:.*-mlflow$"


class FunctionSpecMlflowserve(FunctionSpecModelserve):
    """
    FunctionSpecMlflowserve specifications.
    """


class FunctionValidatorMlflowserve(FunctionValidatorModelserve):
    """
    FunctionValidatorMlflowserve validator.
    """

    image: Optional[str] = Field(default=None, pattern=image_regex)
    "Function image"
