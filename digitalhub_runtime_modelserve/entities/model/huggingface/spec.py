# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.spec import ModelSpec
from pydantic import Field


class ModelSpecHuggingface(ModelSpec):
    """ModelSpecHuggingface specifications."""

    base_model: str | None = None
    placeholder_model_id: str | None = Field(default=None, alias="model_id")
    placeholder_model_revision: str | None = Field(default=None, alias="model_revision")
