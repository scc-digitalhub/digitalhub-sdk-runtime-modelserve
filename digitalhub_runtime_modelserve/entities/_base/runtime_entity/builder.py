# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._commons.utils import map_actions
from digitalhub.entities._mixin.runtime_entity.builder import RuntimeEntityBuilder

from digitalhub_runtime_modelserve.entities._commons.enums import Actions, EntityKinds


class RuntimeEntityBuilderMlflowserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_MLFLOWSERVE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_MLFLOWSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
            (
                EntityKinds.TASK_MLFLOWSERVE_BUILD.value,
                Actions.BUILD.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_MLFLOWSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
            (
                EntityKinds.RUN_MLFLOWSERVE_BUILD.value,
                Actions.BUILD.value,
            ),
        ]
    )


class RuntimeEntityBuilderVllmservePooling(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_VLLMSERVEPOOLING.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_VLLMSERVEPOOLING_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_VLLMSERVEPOOLING_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderVllmserveSpeech(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_VLLMSERVESPEECH.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_VLLMSERVESPEECH_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_VLLMSERVESPEECH_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderVllmserveText(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_VLLMSERVETEXT.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_VLLMSERVETEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_VLLMSERVETEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderKubeaiserveSpeechtotext(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_KUBEAISERVESPEECHTOTEXT.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_KUBEAISERVESPEECHTOTEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_KUBEAISERVESPEECHTOTEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderKubeaiserveText(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_KUBEAISERVETEXT.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_KUBEAISERVETEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_KUBEAISERVETEXT_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderSklearnserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_SKLEARNSERVE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_SKLEARNSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_SKLEARNSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderOllamaserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_OLLAMASERVE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_OLLAMASERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_OLLAMASERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderSglangserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_SGLANGSERVE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_SGLANGSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_SGLANGSERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )


class RuntimeEntityBuilderTeiserve(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_TEISERVE.value
    TASKS_KINDS = map_actions(
        [
            (
                EntityKinds.TASK_TEISERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
    RUN_KINDS = map_actions(
        [
            (
                EntityKinds.RUN_TEISERVE_SERVE.value,
                Actions.SERVE.value,
            ),
        ]
    )
