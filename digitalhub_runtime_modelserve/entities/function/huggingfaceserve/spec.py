# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.function.modelserve.spec import (
    FunctionSpecModelserve,
    FunctionValidatorModelserve,
)


class FunctionSpecHuggingfaceserve(FunctionSpecModelserve):
    """
    FunctionSpecHuggingfaceserve specifications.
    """


class FunctionValidatorHuggingfaceserve(FunctionValidatorModelserve):
    """
    FunctionValidatorHuggingfaceserve validator.
    """
