# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import ModelSpec
from pydantic import Field

from digitalhub_runtime_modelserve.entities.model.mlflow.models import Dataset, Signature


class ModelSpecMlflow(ModelSpec):
    """ModelSpecMlflow specifications."""

    parameters: dict | None = Field(default_factory=dict)
    flavor: str | None = None
    placeholder_cfg_: dict[str, str] | None = Field(default=None, alias="model_config")
    input_datasets: list[Dataset] | None = None
    signature: Signature | None = None
