# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.builder import (
    FunctionKubeaiserveSpeechtotextBuilder,
)
from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.crud import (
    new_function_kubeaiservespeechtotext,
)
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.builder import FunctionKubeaiserveTextBuilder
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.crud import new_function_kubeaiservetext
from digitalhub_runtime_modelserve.entities.function.mlflowserve.builder import FunctionMlflowserveBuilder
from digitalhub_runtime_modelserve.entities.function.mlflowserve.crud import new_function_mlflowserve
from digitalhub_runtime_modelserve.entities.function.ollamaserve.builder import FunctionOllamaserveBuilder
from digitalhub_runtime_modelserve.entities.function.ollamaserve.crud import new_function_ollamaserve
from digitalhub_runtime_modelserve.entities.function.sglangserve.builder import FunctionSglangserveBuilder
from digitalhub_runtime_modelserve.entities.function.sglangserve.crud import new_function_sglangserve
from digitalhub_runtime_modelserve.entities.function.sklearnserve.builder import FunctionSklearnserveBuilder
from digitalhub_runtime_modelserve.entities.function.sklearnserve.crud import new_function_sklearnserve
from digitalhub_runtime_modelserve.entities.function.teiserve.builder import FunctionTeiserveBuilder
from digitalhub_runtime_modelserve.entities.function.teiserve.crud import new_function_teiserve
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.builder import FunctionVllmservepoolingBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.crud import new_function_vllmservepooling
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.builder import FunctionVllmservespeechBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.crud import new_function_vllmservespeech
from digitalhub_runtime_modelserve.entities.function.vllmservetext.builder import FunctionVllmservetextBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservetext.crud import new_function_vllmservetext
from digitalhub_runtime_modelserve.entities.model.huggingface.builder import ModelHuggingfaceBuilder
from digitalhub_runtime_modelserve.entities.model.huggingface.crud import register_huggingface
from digitalhub_runtime_modelserve.entities.model.mlflow.builder import ModelMlflowBuilder
from digitalhub_runtime_modelserve.entities.model.mlflow.crud import log_mlflow, register_mlflow
from digitalhub_runtime_modelserve.entities.model.ollama.builder import ModelOllamaBuilder
from digitalhub_runtime_modelserve.entities.model.ollama.crud import register_ollama
from digitalhub_runtime_modelserve.entities.model.sklearn.builder import ModelSklearnBuilder
from digitalhub_runtime_modelserve.entities.model.sklearn.crud import log_sklearn, register_sklearn
from digitalhub_runtime_modelserve.entities.run.kubeaiservespeechtotext_run.builder import (
    RunKubeaiserveSpeechtotextRunBuilder,
)
from digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.builder import RunKubeaiserveTextRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.builder import RunMlflowserveBuildRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.builder import RunMlflowserveServeRunBuilder
from digitalhub_runtime_modelserve.entities.run.ollamaserve_run.builder import RunOllamaserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.sglangserve_run.builder import RunSglangserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.builder import RunSklearnserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.teiserve_run.builder import RunTeiserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.builder import RunVllmservepoolingRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservespeech_run.builder import RunVllmservespeechRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservetext_run.builder import RunVllmservetextRunBuilder
from digitalhub_runtime_modelserve.entities.task.kubeaiservespeechtotext_serve.builder import (
    TaskKubeaiserveSpeechtotextServeBuilder,
)
from digitalhub_runtime_modelserve.entities.task.kubeaiservetext_serve.builder import TaskKubeaiserveTextServeBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.builder import TaskMlflowserveBuildBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_serve.builder import TaskMlflowserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.ollamaserve_serve.builder import TaskOllamaserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.sglangserve_serve.builder import TaskSglangserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.builder import TaskSklearnserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.teiserve_serve.builder import TaskTeiserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.builder import TaskVllmservepoolingServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservespeech_serve.builder import TaskVllmservespeechServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservetext_serve.builder import TaskVllmservetextServeBuilder

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_MODELSERVE_BUILDER = "digitalhub_runtime_modelserve.runtimes.builder:RuntimeModelserveBuilder"


def _function(builder, *shortcuts) -> EntityPlugin:
    return EntityPlugin(
        builder=builder,
        shortcuts=tuple(CrudPlugin(shortcut) for shortcut in shortcuts),
        runtime_builder=RUNTIME_MODELSERVE_BUILDER,
    )


def _executable(builder) -> EntityPlugin:
    return EntityPlugin(builder=builder, runtime_builder=RUNTIME_MODELSERVE_BUILDER)


def _model(builder, *shortcuts) -> EntityPlugin:
    return EntityPlugin(builder=builder, shortcuts=tuple(CrudPlugin(shortcut) for shortcut in shortcuts))


entity_plugins = (
    _model(ModelHuggingfaceBuilder, register_huggingface),
    _model(ModelMlflowBuilder, log_mlflow, register_mlflow),
    _model(ModelOllamaBuilder, register_ollama),
    _model(ModelSklearnBuilder, log_sklearn, register_sklearn),
    _function(FunctionKubeaiserveSpeechtotextBuilder, new_function_kubeaiservespeechtotext),
    _function(FunctionKubeaiserveTextBuilder, new_function_kubeaiservetext),
    _function(FunctionMlflowserveBuilder, new_function_mlflowserve),
    _function(FunctionOllamaserveBuilder, new_function_ollamaserve),
    _function(FunctionSglangserveBuilder, new_function_sglangserve),
    _function(FunctionSklearnserveBuilder, new_function_sklearnserve),
    _function(FunctionTeiserveBuilder, new_function_teiserve),
    _function(FunctionVllmservepoolingBuilder, new_function_vllmservepooling),
    _function(FunctionVllmservespeechBuilder, new_function_vllmservespeech),
    _function(FunctionVllmservetextBuilder, new_function_vllmservetext),
    _executable(TaskKubeaiserveSpeechtotextServeBuilder),
    _executable(TaskKubeaiserveTextServeBuilder),
    _executable(TaskMlflowserveBuildBuilder),
    _executable(TaskMlflowserveServeBuilder),
    _executable(TaskOllamaserveServeBuilder),
    _executable(TaskSglangserveServeBuilder),
    _executable(TaskSklearnserveServeBuilder),
    _executable(TaskTeiserveServeBuilder),
    _executable(TaskVllmservepoolingServeBuilder),
    _executable(TaskVllmservespeechServeBuilder),
    _executable(TaskVllmservetextServeBuilder),
    _executable(RunKubeaiserveSpeechtotextRunBuilder),
    _executable(RunKubeaiserveTextRunBuilder),
    _executable(RunMlflowserveBuildRunBuilder),
    _executable(RunMlflowserveServeRunBuilder),
    _executable(RunOllamaserveRunBuilder),
    _executable(RunSglangserveRunBuilder),
    _executable(RunSklearnserveRunBuilder),
    _executable(RunTeiserveRunBuilder),
    _executable(RunVllmservepoolingRunBuilder),
    _executable(RunVllmservespeechRunBuilder),
    _executable(RunVllmservetextRunBuilder),
)
