# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec


class FunctionSpecModelserve(FunctionSpec):
    """
    FunctionSpecModelserve specifications.
    """

    path: str | None = None
    model_name: str | None = None
    image: str | None = None
