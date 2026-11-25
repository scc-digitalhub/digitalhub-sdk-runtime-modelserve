# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    MODEL_HUGGINGFACE = "huggingface"
    MODEL_MLFLOW = "mlflow"
    MODEL_OLLAMA = "ollama"
    MODEL_SKLEARN = "sklearn"

    FUNCTION_MLFLOWSERVE = "mlflowserve"
    TASK_MLFLOWSERVE_BUILD = "mlflowserve+build"
    RUN_MLFLOWSERVE_BUILD = "mlflowserve+build:run"
    TASK_MLFLOWSERVE_SERVE = "mlflowserve+serve"
    RUN_MLFLOWSERVE_SERVE = "mlflowserve+serve:run"

    FUNCTION_SKLEARNSERVE = "sklearnserve"
    TASK_SKLEARNSERVE_SERVE = "sklearnserve+serve"
    RUN_SKLEARNSERVE_SERVE = "sklearnserve+serve:run"

    FUNCTION_OLLAMASERVE = "ollamaserve"
    TASK_OLLAMASERVE_SERVE = "ollamaserve+serve"
    RUN_OLLAMASERVE_SERVE = "ollamaserve+serve:run"

    FUNCTION_SGLANGSERVE = "sglangserve"
    TASK_SGLANGSERVE_SERVE = "sglangserve+serve"
    RUN_SGLANGSERVE_SERVE = "sglangserve+serve:run"

    FUNCTION_TEISERVE = "teiserve"
    TASK_TEISERVE_SERVE = "teiserve+serve"
    RUN_TEISERVE_SERVE = "teiserve+serve:run"

    FUNCTION_KUBEAISERVETEXT = "kubeai-text"
    TASK_KUBEAISERVETEXT_SERVE = "kubeai-text+serve"
    RUN_KUBEAISERVETEXT_SERVE = "kubeai-text+serve:run"

    FUNCTION_KUBEAISERVESPEECHTOTEXT = "kubeai-speech"
    TASK_KUBEAISERVESPEECHTOTEXT_SERVE = "kubeai-speech+serve"
    RUN_KUBEAISERVESPEECHTOTEXT_SERVE = "kubeai-speech+serve:run"

    FUNCTION_VLLMSERVESPEECH = "vllmserve-speech"
    TASK_VLLMSERVESPEECH_SERVE = "vllmserve-speech+serve"
    RUN_VLLMSERVESPEECH_SERVE = "vllmserve-speech+serve:run"

    FUNCTION_VLLMSERVEPOOLING = "vllmserve-pooling"
    TASK_VLLMSERVEPOOLING_SERVE = "vllmserve-pooling+serve"
    RUN_VLLMSERVEPOOLING_SERVE = "vllmserve-pooling+serve:run"

    FUNCTION_VLLMSERVETEXT = "vllmserve-text"
    TASK_VLLMSERVETEXT_SERVE = "vllmserve-text+serve"
    RUN_VLLMSERVETEXT_SERVE = "vllmserve-text+serve:run"


class Actions(Enum):
    """
    Task actions.
    """

    SERVE = "serve"
    BUILD = "build"
