# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.entity.spec import Spec
from digitalhub.entities._frameworks.k8s.models import CoreServiceType
from digitalhub.entities._mixin.execution.spec import ServeSpecMixin
from pydantic import Field

from digitalhub_runtime_modelserve.entities._commons.models import KubeaiFile, Scaling
from digitalhub_runtime_modelserve.entities.task.huggingfaceserve_serve.models import Backend, Dtype, HuggingfaceTask


class ModelserveServeSpecMixin(ServeSpecMixin):
    """Specification fields shared by ModelServe tasks and runs."""

    service_type: CoreServiceType | None = CoreServiceType.CLUSTER_IP


class HuggingfaceServeSpecMixin(Spec):
    """Hugging Face serving fields shared by its task and run."""

    huggingface_task: HuggingfaceTask | None = None
    backend: Backend | None = None
    tokenizer_revision: str | None = None
    max_length: int | None = None
    disable_lower_case: bool | None = None
    disable_special_tokens: bool | None = None
    dtype: Dtype | None = None
    trust_remote_code: bool | None = None
    tensor_input_names: list[str] | None = None
    return_token_type_ids: bool | None = None
    return_probabilities: bool | None = None
    disable_log_requests: bool | None = None
    max_log_len: int | None = None


class KubeaiServeSpecMixin(Spec):
    """KubeAI serving fields shared by its tasks and runs."""

    envs: dict | None = None
    image: str | None = None
    model_name: str | None = None
    args: list[str] | None = None
    processors: int | None = Field(default=None, ge=1)
    files: list[KubeaiFile] | None = None
    scaling: Scaling | None = None
