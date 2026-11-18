# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.spec import Spec


class FunctionSpecModelserve(Spec):
    """
    FunctionSpecModelserve specifications.
    """

    path: str | None = None
    model_name: str | None = None
    image: str | None = None
