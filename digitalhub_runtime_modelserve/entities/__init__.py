# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.factory.plugins import CrudPlugin, EntityPlugin

from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.builder import FunctionHuggingfaceserveBuilder
from digitalhub_runtime_modelserve.entities.function.huggingfaceserve.crud import new_function_huggingfaceserve
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
from digitalhub_runtime_modelserve.entities.function.sklearnserve.builder import FunctionSklearnserveBuilder
from digitalhub_runtime_modelserve.entities.function.sklearnserve.crud import new_function_sklearnserve
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.builder import FunctionVllmservepoolingBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.crud import new_function_vllmservepooling
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.builder import FunctionVllmservespeechBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.crud import new_function_vllmservespeech
from digitalhub_runtime_modelserve.entities.function.vllmservetext.builder import FunctionVllmservetextBuilder
from digitalhub_runtime_modelserve.entities.function.vllmservetext.crud import new_function_vllmservetext
from digitalhub_runtime_modelserve.entities.model.huggingface.builder import ModelHuggingfaceBuilder
from digitalhub_runtime_modelserve.entities.model.huggingface.crud import log_huggingface, register_huggingface
from digitalhub_runtime_modelserve.entities.model.mlflow.builder import ModelMlflowBuilder
from digitalhub_runtime_modelserve.entities.model.mlflow.crud import log_mlflow, register_mlflow
from digitalhub_runtime_modelserve.entities.model.sklearn.builder import ModelSklearnBuilder
from digitalhub_runtime_modelserve.entities.model.sklearn.crud import log_sklearn, register_sklearn
from digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.builder import RunHuggingfaceserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.kubeaiservespeechtotext_run.builder import (
    RunKubeaiserveSpeechtotextRunBuilder,
)
from digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.builder import RunKubeaiserveTextRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.builder import RunMlflowserveBuildRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.builder import RunMlflowserveServeRunBuilder
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.builder import RunSklearnserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservepooling_run.builder import RunVllmservepoolingRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservespeech_run.builder import RunVllmservespeechRunBuilder
from digitalhub_runtime_modelserve.entities.run.vllmservetext_run.builder import RunVllmservetextRunBuilder
from digitalhub_runtime_modelserve.entities.task.huggingfaceserve_serve.builder import TaskHuggingfaceserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.kubeaiservespeechtotext_serve.builder import (
    TaskKubeaiserveSpeechtotextServeBuilder,
)
from digitalhub_runtime_modelserve.entities.task.kubeaiservetext_serve.builder import TaskKubeaiserveTextServeBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.builder import TaskMlflowserveBuildBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_serve.builder import TaskMlflowserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.builder import TaskSklearnserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservepooling_serve.builder import TaskVllmservepoolingServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservespeech_serve.builder import TaskVllmservespeechServeBuilder
from digitalhub_runtime_modelserve.entities.task.vllmservetext_serve.builder import TaskVllmservetextServeBuilder

function_huggingfaceserve_plugin = EntityPlugin(
    builder=FunctionHuggingfaceserveBuilder,
    shortcuts=(CrudPlugin(new_function_huggingfaceserve),),
)
function_kubeaiserve_speech_plugin = EntityPlugin(
    builder=FunctionKubeaiserveSpeechtotextBuilder,
    shortcuts=(CrudPlugin(new_function_kubeaiservespeechtotext),),
)
function_kubeaiserve_text_plugin = EntityPlugin(
    builder=FunctionKubeaiserveTextBuilder,
    shortcuts=(CrudPlugin(new_function_kubeaiservetext),),
)
function_mlflowserve_plugin = EntityPlugin(
    builder=FunctionMlflowserveBuilder,
    shortcuts=(CrudPlugin(new_function_mlflowserve),),
)
function_sklearnserve_plugin = EntityPlugin(
    builder=FunctionSklearnserveBuilder,
    shortcuts=(CrudPlugin(new_function_sklearnserve),),
)
function_vllmserve_pooling_plugin = EntityPlugin(
    builder=FunctionVllmservepoolingBuilder,
    shortcuts=(CrudPlugin(new_function_vllmservepooling),),
)
function_vllmserve_speech_plugin = EntityPlugin(
    builder=FunctionVllmservespeechBuilder,
    shortcuts=(CrudPlugin(new_function_vllmservespeech),),
)
function_vllmserve_text_plugin = EntityPlugin(
    builder=FunctionVllmservetextBuilder,
    shortcuts=(CrudPlugin(new_function_vllmservetext),),
)
model_huggingface_plugin = EntityPlugin(
    builder=ModelHuggingfaceBuilder,
    shortcuts=(CrudPlugin(log_huggingface), CrudPlugin(register_huggingface)),
)
model_mlflow_plugin = EntityPlugin(
    builder=ModelMlflowBuilder,
    shortcuts=(CrudPlugin(log_mlflow), CrudPlugin(register_mlflow)),
)
model_sklearn_plugin = EntityPlugin(
    builder=ModelSklearnBuilder,
    shortcuts=(CrudPlugin(log_sklearn), CrudPlugin(register_sklearn)),
)

entity_plugins = (
    model_huggingface_plugin,
    model_mlflow_plugin,
    model_sklearn_plugin,
    function_huggingfaceserve_plugin,
    function_kubeaiserve_speech_plugin,
    function_kubeaiserve_text_plugin,
    function_mlflowserve_plugin,
    function_sklearnserve_plugin,
    function_vllmserve_pooling_plugin,
    function_vllmserve_speech_plugin,
    function_vllmserve_text_plugin,
    EntityPlugin(builder=TaskHuggingfaceserveServeBuilder),
    EntityPlugin(builder=TaskKubeaiserveSpeechtotextServeBuilder),
    EntityPlugin(builder=TaskKubeaiserveTextServeBuilder),
    EntityPlugin(builder=TaskMlflowserveBuildBuilder),
    EntityPlugin(builder=TaskMlflowserveServeBuilder),
    EntityPlugin(builder=TaskSklearnserveServeBuilder),
    EntityPlugin(builder=TaskVllmservepoolingServeBuilder),
    EntityPlugin(builder=TaskVllmservespeechServeBuilder),
    EntityPlugin(builder=TaskVllmservetextServeBuilder),
    EntityPlugin(builder=RunHuggingfaceserveRunBuilder),
    EntityPlugin(builder=RunKubeaiserveSpeechtotextRunBuilder),
    EntityPlugin(builder=RunKubeaiserveTextRunBuilder),
    EntityPlugin(builder=RunMlflowserveBuildRunBuilder),
    EntityPlugin(builder=RunMlflowserveServeRunBuilder),
    EntityPlugin(builder=RunSklearnserveRunBuilder),
    EntityPlugin(builder=RunVllmservepoolingRunBuilder),
    EntityPlugin(builder=RunVllmservespeechRunBuilder),
    EntityPlugin(builder=RunVllmservetextRunBuilder),
)
