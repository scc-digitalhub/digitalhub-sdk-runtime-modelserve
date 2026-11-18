# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.builder import ModelBuilder
from digitalhub.entities.model._base.status import ModelStatus

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.model.huggingface.entity import ModelHuggingface
from digitalhub_runtime_modelserve.entities.model.huggingface.spec import (
    ModelSpecHuggingface,
)


class ModelHuggingfaceBuilder(ModelBuilder):
    """ModelHuggingface builder."""

    ENTITY_CLASS = ModelHuggingface
    ENTITY_SPEC_CLASS = ModelSpecHuggingface
    ENTITY_STATUS_CLASS = ModelStatus
    ENTITY_KIND = EntityKinds.MODEL_HUGGINGFACE.value
