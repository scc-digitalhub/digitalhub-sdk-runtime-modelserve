# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.model._base.builder import ModelBuilder

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds
from digitalhub_runtime_modelserve.entities.model.huggingface.entity import ModelHuggingface
from digitalhub_runtime_modelserve.entities.model.huggingface.spec import (
    ModelSpecHuggingface,
    ModelValidatorHuggingface,
)
from digitalhub_runtime_modelserve.entities.model.huggingface.status import ModelStatusHuggingface


class ModelHuggingfaceBuilder(ModelBuilder):
    """ModelHuggingface builder."""

    ENTITY_CLASS = ModelHuggingface
    ENTITY_SPEC_CLASS = ModelSpecHuggingface
    ENTITY_SPEC_VALIDATOR = ModelValidatorHuggingface
    ENTITY_STATUS_CLASS = ModelStatusHuggingface
    ENTITY_KIND = EntityKinds.MODEL_HUGGINGFACE.value
