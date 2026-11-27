# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from digitalhub.entities.model.model.entity import ModelModel
from digitalhub.plugins import (
    Action,
    BuilderDef,
    CrudPlugin,
    ExecFamily,
    ExecutableActions,
    FunctionBuilder,
    ModelBuilder,
    ModelSpec,
    ModelStatus,
    RunBuilder,
    Status,
    Task,
    TaskBuilder,
)

from digitalhub_runtime_modelserve.entities._commons.enums import Actions, EntityKinds
from digitalhub_runtime_modelserve.entities.function.kubeaiserve.spec import FunctionSpecKubeaiserve
from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.crud import (
    new_function_kubeaiservespeechtotext,
)
from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.entity import (
    FunctionKubeaiserveSpeechtotext,
)
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.crud import new_function_kubeaiservetext
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.entity import FunctionKubeaiserveText
from digitalhub_runtime_modelserve.entities.function.kubeaiservetext.spec import FunctionSpecKubeaiserveText
from digitalhub_runtime_modelserve.entities.function.mlflowserve.crud import new_function_mlflowserve
from digitalhub_runtime_modelserve.entities.function.mlflowserve.entity import FunctionMlflowserve
from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve
from digitalhub_runtime_modelserve.entities.function.modelserve.spec import FunctionSpecModelserve
from digitalhub_runtime_modelserve.entities.function.ollamaserve.crud import new_function_ollamaserve
from digitalhub_runtime_modelserve.entities.function.ollamaserve.spec import FunctionSpecOllamaserve
from digitalhub_runtime_modelserve.entities.function.sglangserve.crud import new_function_sglangserve
from digitalhub_runtime_modelserve.entities.function.sglangserve.spec import FunctionSpecSglangserve
from digitalhub_runtime_modelserve.entities.function.sklearnserve.crud import new_function_sklearnserve
from digitalhub_runtime_modelserve.entities.function.sklearnserve.entity import FunctionSklearnserve
from digitalhub_runtime_modelserve.entities.function.teiserve.crud import new_function_teiserve
from digitalhub_runtime_modelserve.entities.function.teiserve.spec import FunctionSpecTeiserve
from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.crud import new_function_vllmservepooling
from digitalhub_runtime_modelserve.entities.function.vllmservepooling.entity import FunctionVllmservepooling
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.crud import new_function_vllmservespeech
from digitalhub_runtime_modelserve.entities.function.vllmservespeech.entity import FunctionVllmservespeech
from digitalhub_runtime_modelserve.entities.function.vllmservetext.crud import new_function_vllmservetext
from digitalhub_runtime_modelserve.entities.function.vllmservetext.entity import FunctionVllmservetext
from digitalhub_runtime_modelserve.entities.model.huggingface.crud import register_huggingface
from digitalhub_runtime_modelserve.entities.model.huggingface.entity import ModelHuggingface
from digitalhub_runtime_modelserve.entities.model.huggingface.spec import ModelSpecHuggingface
from digitalhub_runtime_modelserve.entities.model.mlflow.crud import log_mlflow, register_mlflow
from digitalhub_runtime_modelserve.entities.model.mlflow.entity import ModelMlflow
from digitalhub_runtime_modelserve.entities.model.mlflow.spec import ModelSpecMlflow
from digitalhub_runtime_modelserve.entities.model.ollama.crud import register_ollama
from digitalhub_runtime_modelserve.entities.model.sklearn.crud import log_sklearn, register_sklearn
from digitalhub_runtime_modelserve.entities.model.sklearn.entity import ModelSklearn
from digitalhub_runtime_modelserve.entities.model.sklearn.spec import ModelSpecSklearn
from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.entity import RunKubeaiserveRun
from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.spec import RunSpecKubeaiserveRun
from digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.spec import RunSpecKubeaiserveTextRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.entity import RunMlflowserveBuildRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.spec import RunSpecMlflowserveBuildRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.status import RunStatusMlflowserveBuildRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.entity import RunMlflowserveServeRun
from digitalhub_runtime_modelserve.entities.run.mlflowserve_serve_run.spec import RunSpecMlflowserveServeRun
from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunServiceUrlsRun
from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun
from digitalhub_runtime_modelserve.entities.run.ollamaserve_run.spec import RunSpecOllamaserveRun
from digitalhub_runtime_modelserve.entities.run.sglangserve_run.spec import RunSpecSglangserveRun
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.entity import RunSklearnserveRun
from digitalhub_runtime_modelserve.entities.run.sklearnserve_run.spec import RunSpecSklearnserveRun
from digitalhub_runtime_modelserve.entities.run.teiserve_run.spec import RunSpecTeiserveRun
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.spec import RunSpecVllmserveRun
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.status import RunStatusVllmserveRun
from digitalhub_runtime_modelserve.entities.task.kubeaiserve_serve.spec import TaskSpecKubeaiserveServe
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.spec import TaskSpecMlflowserveBuild
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe

# Imported on first use: the entities register even when the runtime cannot be
# imported, and the import error is reported when a run executes locally.
RUNTIME_MODELSERVE_BUILDER = "digitalhub_runtime_modelserve.runtimes.builder:RuntimeModelserveBuilder"

kubeai_speech = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_KUBEAISERVESPEECHTOTEXT,
        FunctionKubeaiserveSpeechtotext,
        FunctionSpecKubeaiserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_kubeaiservespeechtotext),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_KUBEAISERVESPEECHTOTEXT_SERVE,
                Task,
                TaskSpecKubeaiserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_KUBEAISERVESPEECHTOTEXT_SERVE,
                RunKubeaiserveRun,
                RunSpecKubeaiserveRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

kubeai_text = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_KUBEAISERVETEXT,
        FunctionKubeaiserveText,
        FunctionSpecKubeaiserveText,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_kubeaiservetext),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_KUBEAISERVETEXT_SERVE,
                Task,
                TaskSpecKubeaiserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_KUBEAISERVETEXT_SERVE,
                RunKubeaiserveRun,
                RunSpecKubeaiserveTextRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

mlflowserve = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_MLFLOWSERVE,
        FunctionMlflowserve,
        FunctionSpecModelserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_mlflowserve),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_MLFLOWSERVE_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_MLFLOWSERVE_SERVE,
                RunMlflowserveServeRun,
                RunSpecMlflowserveServeRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
        ExecutableActions.BUILD: Action(
            task=BuilderDef(
                EntityKinds.TASK_MLFLOWSERVE_BUILD,
                Task,
                TaskSpecMlflowserveBuild,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_MLFLOWSERVE_BUILD,
                RunMlflowserveBuildRun,
                RunSpecMlflowserveBuildRun,
                RunStatusMlflowserveBuildRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

ollamaserve = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_OLLAMASERVE,
        FunctionModelserve,
        FunctionSpecOllamaserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_ollamaserve),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_OLLAMASERVE_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_OLLAMASERVE_SERVE,
                RunServiceUrlsRun,
                RunSpecOllamaserveRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

sglangserve = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_SGLANGSERVE,
        FunctionModelserve,
        FunctionSpecSglangserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_sglangserve),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_SGLANGSERVE_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_SGLANGSERVE_SERVE,
                RunServiceUrlsRun,
                RunSpecSglangserveRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

sklearnserve = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_SKLEARNSERVE,
        FunctionSklearnserve,
        FunctionSpecModelserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_sklearnserve),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_SKLEARNSERVE_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_SKLEARNSERVE_SERVE,
                RunSklearnserveRun,
                RunSpecSklearnserveRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

teiserve = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_TEISERVE,
        FunctionModelserve,
        FunctionSpecTeiserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_teiserve),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(EntityKinds.TASK_TEISERVE_SERVE, Task, TaskSpecModelserveServe, Status, base=TaskBuilder),
            run=BuilderDef(
                EntityKinds.RUN_TEISERVE_SERVE,
                RunServiceUrlsRun,
                RunSpecTeiserveRun,
                RunStatusModelserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

vllmserve_pooling = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_VLLMSERVEPOOLING,
        FunctionVllmservepooling,
        FunctionSpecVllmserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_vllmservepooling),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_VLLMSERVEPOOLING_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_VLLMSERVEPOOLING_SERVE,
                RunServiceUrlsRun,
                RunSpecVllmserveRun,
                RunStatusVllmserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

vllmserve_speech = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_VLLMSERVESPEECH,
        FunctionVllmservespeech,
        FunctionSpecVllmserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_vllmservespeech),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_VLLMSERVESPEECH_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_VLLMSERVESPEECH_SERVE,
                RunServiceUrlsRun,
                RunSpecVllmserveRun,
                RunStatusVllmserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

vllmserve_text = ExecFamily(
    executable=BuilderDef(
        EntityKinds.FUNCTION_VLLMSERVETEXT,
        FunctionVllmservetext,
        FunctionSpecVllmserve,
        Status,
        base=FunctionBuilder,
        shortcuts=(CrudPlugin(new_function_vllmservetext),),
    ),
    actions={
        Actions.SERVE: Action(
            task=BuilderDef(
                EntityKinds.TASK_VLLMSERVETEXT_SERVE,
                Task,
                TaskSpecModelserveServe,
                Status,
                base=TaskBuilder,
            ),
            run=BuilderDef(
                EntityKinds.RUN_VLLMSERVETEXT_SERVE,
                RunServiceUrlsRun,
                RunSpecVllmserveRun,
                RunStatusVllmserveRun,
                base=RunBuilder,
            ),
        ),
    },
    runtime_builder=RUNTIME_MODELSERVE_BUILDER,
)

_models = (
    BuilderDef(
        EntityKinds.MODEL_HUGGINGFACE,
        ModelHuggingface,
        ModelSpecHuggingface,
        ModelStatus,
        base=ModelBuilder,
        shortcuts=(CrudPlugin(register_huggingface),),
    ),
    BuilderDef(
        EntityKinds.MODEL_MLFLOW,
        ModelMlflow,
        ModelSpecMlflow,
        ModelStatus,
        base=ModelBuilder,
        shortcuts=(
            CrudPlugin(log_mlflow),
            CrudPlugin(register_mlflow),
        ),
    ),
    BuilderDef(
        EntityKinds.MODEL_OLLAMA,
        ModelModel,
        ModelSpec,
        ModelStatus,
        base=ModelBuilder,
        shortcuts=(CrudPlugin(register_ollama),),
    ),
    BuilderDef(
        EntityKinds.MODEL_SKLEARN,
        ModelSklearn,
        ModelSpecSklearn,
        ModelStatus,
        base=ModelBuilder,
        shortcuts=(
            CrudPlugin(log_sklearn),
            CrudPlugin(register_sklearn),
        ),
    ),
)

entity_plugins = (
    *(definition.plugin() for definition in _models),
    *kubeai_speech.plugins(),
    *kubeai_text.plugins(),
    *mlflowserve.plugins(),
    *ollamaserve.plugins(),
    *sglangserve.plugins(),
    *sklearnserve.plugins(),
    *teiserve.plugins(),
    *vllmserve_pooling.plugins(),
    *vllmserve_speech.plugins(),
    *vllmserve_text.plugins(),
)
