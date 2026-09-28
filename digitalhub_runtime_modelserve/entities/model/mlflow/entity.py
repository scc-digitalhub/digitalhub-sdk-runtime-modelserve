# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.model._base.entity import Model

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.model.mlflow.spec import ModelSpecMlflow
    from digitalhub_runtime_modelserve.entities.model.mlflow.status import ModelStatusMlflow


class ModelMlflow(Model):
    """ModelMlflow class."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: ModelSpecMlflow
        self.status: ModelStatusMlflow
