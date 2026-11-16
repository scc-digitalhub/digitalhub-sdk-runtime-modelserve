# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.task.huggingfaceserve_serve.models import Backend, Dtype, HuggingfaceTask
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import (
    TaskSpecModelserveServe,
)


class TaskSpecHuggingfaceserveServe(TaskSpecModelserveServe):
    """
    TaskSpecHuggingfaceserveServe specifications.
    """

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
