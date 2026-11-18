# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.builder import ModelBuilder
from digitalhub.entities.model._base.status import ModelStatus

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.model.sklearn.entity import ModelSklearn
from digitalhub_runtime_modelserve.entities.model.sklearn.spec import ModelSpecSklearn


class ModelSklearnBuilder(ModelBuilder):
    """ModelSklearn builder."""

    ENTITY_CLASS = ModelSklearn
    ENTITY_SPEC_CLASS = ModelSpecSklearn
    ENTITY_STATUS_CLASS = ModelStatus
    ENTITY_KIND = EntityKinds.MODEL_SKLEARN.value
