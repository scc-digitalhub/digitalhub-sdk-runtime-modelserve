# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec


class FunctionSpecTeiserve(FunctionSpec):
    """FunctionSpecTeiserve specifications."""

    image: str | None = None
    path: str
