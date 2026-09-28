# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_modelserve.entities import entity_plugins
from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds

entity_builders = tuple((plugin.kind, plugin.builder) for plugin in entity_plugins)

try:
    from digitalhub_runtime_modelserve.runtimes.builder import RuntimeModelserveBuilder

    runtime_kinds = (
        EntityKinds.FUNCTION_HUGGINGFACESERVE,
        EntityKinds.TASK_HUGGINGFACESERVE_SERVE,
        EntityKinds.RUN_HUGGINGFACESERVE_SERVE,
        EntityKinds.FUNCTION_MLFLOWSERVE,
        EntityKinds.TASK_MLFLOWSERVE_BUILD,
        EntityKinds.RUN_MLFLOWSERVE_BUILD,
        EntityKinds.TASK_MLFLOWSERVE_SERVE,
        EntityKinds.RUN_MLFLOWSERVE_SERVE,
        EntityKinds.FUNCTION_SKLEARNSERVE,
        EntityKinds.TASK_SKLEARNSERVE_SERVE,
        EntityKinds.RUN_SKLEARNSERVE_SERVE,
        EntityKinds.FUNCTION_KUBEAISERVE,
        EntityKinds.TASK_KUBEAISERVE_SERVE,
        EntityKinds.RUN_KUBEAISERVE_SERVE,
        EntityKinds.FUNCTION_KUBEAISERVETEXT,
        EntityKinds.TASK_KUBEAISERVETEXT_SERVE,
        EntityKinds.RUN_KUBEAISERVETEXT_SERVE,
        EntityKinds.FUNCTION_KUBEAISERVESPEECHTOTEXT,
        EntityKinds.TASK_KUBEAISERVESPEECHTOTEXT_SERVE,
        EntityKinds.RUN_KUBEAISERVESPEECHTOTEXT_SERVE,
        EntityKinds.FUNCTION_VLLMSERVE,
        EntityKinds.TASK_VLLMSERVE_SERVE,
        EntityKinds.RUN_VLLMSERVE_SERVE,
        EntityKinds.FUNCTION_VLLMSERVESPEECH,
        EntityKinds.TASK_VLLMSERVESPEECH_SERVE,
        EntityKinds.RUN_VLLMSERVESPEECH_SERVE,
        EntityKinds.FUNCTION_VLLMSERVEPOOLING,
        EntityKinds.TASK_VLLMSERVEPOOLING_SERVE,
        EntityKinds.RUN_VLLMSERVEPOOLING_SERVE,
        EntityKinds.FUNCTION_VLLMSERVETEXT,
        EntityKinds.TASK_VLLMSERVETEXT_SERVE,
        EntityKinds.RUN_VLLMSERVETEXT_SERVE,
    )
    runtime_builders = ((kind.value, RuntimeModelserveBuilder) for kind in runtime_kinds)
except ImportError as e:
    from digitalhub.utils.logger.logger import get_logger

    logger = get_logger(__name__)
    logger.debug(f"Error importing runtime builders: {e}")
    runtime_builders = ()
