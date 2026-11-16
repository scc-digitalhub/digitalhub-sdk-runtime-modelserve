# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.spec import ModelSpec
from pydantic import Field

from digitalhub_runtime_modelserve.entities.model.mlflow.models import Dataset, Signature


class ModelSpecMlflow(ModelSpec):
    """ModelSpecMlflow specifications."""

    flavor: str | None = None
    placeholder_cfg_: dict = Field(default=None, alias="model_config")
    input_datasets: list[Dataset] | None = None
    signature: Signature | None = None
