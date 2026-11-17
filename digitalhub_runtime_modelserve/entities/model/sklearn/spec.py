# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.spec import ModelSpec
from pydantic import Field


class ModelSpecSklearn(ModelSpec):
    """ModelSpecSklearn specifications."""

    parameters: dict | None = Field(default_factory=dict)
