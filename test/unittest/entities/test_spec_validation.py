# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from digitalhub.plugins import CoreServiceType, ModelSpec, build_spec
from pydantic import ValidationError

from digitalhub_runtime_modelserve.entities._commons.models import KubeaiFile, Scaling
from digitalhub_runtime_modelserve.entities.function.ollamaserve.spec import FunctionSpecOllamaserve
from digitalhub_runtime_modelserve.entities.function.sglangserve.spec import FunctionSpecSglangserve
from digitalhub_runtime_modelserve.entities.function.teiserve.spec import FunctionSpecTeiserve
from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter
from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
from digitalhub_runtime_modelserve.entities.model.mlflow.builder import ModelMlflowBuilder
from digitalhub_runtime_modelserve.entities.model.sklearn.spec import ModelSpecSklearn
from digitalhub_runtime_modelserve.entities.run.kubeaiservetext_run.builder import RunKubeaiserveTextRunBuilder
from digitalhub_runtime_modelserve.entities.run.mlflowserve_build_run.spec import RunSpecMlflowserveBuildRun
from digitalhub_runtime_modelserve.entities.run.ollamaserve_run.spec import RunSpecOllamaserveRun
from digitalhub_runtime_modelserve.entities.run.sglangserve_run.spec import RunSpecSglangserveRun
from digitalhub_runtime_modelserve.entities.run.teiserve_run.spec import RunSpecTeiserveRun
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.spec import RunSpecVllmserveRun
from digitalhub_runtime_modelserve.entities.task.kubeaiservetext_serve.builder import TaskKubeaiserveTextServeBuilder
from digitalhub_runtime_modelserve.entities.task.mlflowserve_build.spec import TaskSpecMlflowserveBuild
from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import TaskSpecModelserveServe
from digitalhub_runtime_modelserve.entities.task.sklearnserve_serve.builder import TaskSklearnserveServeBuilder


def test_function_spec_validates_nested_adapters() -> None:
    spec = build_spec(
        FunctionSpecVllmserve,
        url="store://models/model/huggingface/model",
        adapters=[{"name": "adapter", "url": "https://example.test"}],
    )

    assert isinstance(spec.adapters[0], VLLMAdapter)

    with pytest.raises(ValidationError):
        build_spec(
            FunctionSpecVllmserve,
            url="store://models/model/huggingface/model",
            adapters=["adapter"],
        )

    assert build_spec(FunctionSpecVllmserve, url="model").url == "model"


def test_task_spec_preserves_replica_constraint() -> None:
    builder = TaskSklearnserveServeBuilder()

    spec = builder.build_spec(function="function", replicas=0)
    assert spec.replicas == 0
    assert spec.service_type == CoreServiceType.CLUSTER_IP

    with pytest.raises(ValidationError):
        builder.build_spec(function="function", replicas=-1)


def test_mlflow_build_specs_do_not_inherit_serve_fields() -> None:
    task = build_spec(TaskSpecMlflowserveBuild, function="function", instructions=["pip install mlflow"])
    run = build_spec(
        RunSpecMlflowserveBuildRun,
        function="function",
        task="task",
        instructions=["pip install mlflow"],
    )

    assert task.instructions == ["pip install mlflow"]
    assert run.instructions == ["pip install mlflow"]

    with pytest.raises(TypeError, match="replicas"):
        build_spec(TaskSpecMlflowserveBuild, function="function", replicas=1)

    with pytest.raises(TypeError, match="replicas"):
        build_spec(RunSpecMlflowserveBuildRun, function="function", task="task", replicas=1)


def test_run_spec_merges_action_fields_and_preserves_run_fields() -> None:
    spec = build_spec(
        RunSpecVllmserveRun,
        function="function",
        task="task",
        url="store://models/model/huggingface/model",
        args=["--port", "8000"],
        replicas=2,
        service_type="ClusterIP",
    )

    assert spec.url == "store://models/model/huggingface/model"
    assert spec.args == ["--port", "8000"]
    assert spec.enable_telemetry is None
    assert spec.replicas == 2
    assert spec.service_type == "ClusterIP"

    with pytest.raises(TypeError, match="use_cpu_image"):
        build_spec(RunSpecVllmserveRun, function="function", task="task", use_cpu_image=True)


def test_kubeai_run_spec_preserves_constraint_and_nested_models() -> None:
    builder = RunKubeaiserveTextRunBuilder()
    spec = builder.build_spec(
        function="function",
        task="task",
        processors=2,
        files=[{"path": "model.bin"}],
        scaling={"replicas": 3},
        resources={"cpu": "1"},
    )

    assert isinstance(spec.files[0], KubeaiFile)
    assert isinstance(spec.scaling, Scaling)
    assert spec.resources.cpu == "1"

    with pytest.raises(ValidationError):
        builder.build_spec(function="function", task="task", processors=0)


def test_kubeai_task_spec_validates_runtime_and_service_fields() -> None:
    builder = TaskKubeaiserveTextServeBuilder()
    spec = builder.build_spec(
        function="function",
        args=["--model"],
        image="model-image",
        model_name="model",
        processors=1,
        files=[{"path": "model.bin"}],
        scaling={"replicas": 3},
        replicas=2,
        resources={"cpu": "1"},
    )

    assert isinstance(spec.files[0], KubeaiFile)
    assert isinstance(spec.scaling, Scaling)
    assert spec.replicas == 2
    assert spec.resources.cpu == "1"

    with pytest.raises(ValidationError):
        builder.build_spec(function="function", processors=0)


def test_mlflow_model_spec_uses_aliased_and_nested_fields() -> None:
    spec = ModelMlflowBuilder().build_spec(
        path="model",
        model_config={"artifact_path": "model"},
        input_datasets=[{"name": "training"}],
        signature={"inputs": "input"},
    )

    serialized = spec.to_dict()
    assert serialized["model_config"] == {"artifact_path": "model"}
    assert serialized["parameters"] == {}
    assert serialized["input_datasets"] == [{"name": "training"}]
    assert serialized["signature"]["inputs"] == "input"

    sklearn_spec = build_spec(ModelSpecSklearn, path="model.pkl")
    assert sklearn_spec.parameters == {}


def test_new_runtime_specs_match_modelserve_contracts() -> None:
    ollama_function = build_spec(
        FunctionSpecOllamaserve,
        path="store://models/model/ollama/1",
    )
    ollama_model = build_spec(ModelSpec, path="ollama://llama3:latest")
    ollama_task = build_spec(TaskSpecModelserveServe, function="function", replicas=0)
    ollama_run = build_spec(
        RunSpecOllamaserveRun,
        function="function",
        task="task",
        path="store://models/model/ollama/1",
    )

    assert ollama_function.path.endswith("/ollama/1")
    assert ollama_model.path == "ollama://llama3:latest"
    assert ollama_task.replicas == 0
    assert ollama_run.model_name is None

    sglang_function = build_spec(
        FunctionSpecSglangserve,
        path="store://models/model/huggingface/1",
        adapters=[{"name": "adapter", "url": "https://example.test"}],
    )
    sglang_task = build_spec(TaskSpecModelserveServe, function="function")
    sglang_run = build_spec(
        RunSpecSglangserveRun,
        function="function",
        task="task",
        path="store://models/model/huggingface/1",
    )
    tei_function = build_spec(FunctionSpecTeiserve, path="store://models/model/tei/1")
    tei_task = build_spec(TaskSpecModelserveServe, function="function")
    tei_run = build_spec(RunSpecTeiserveRun, function="function", task="task", path="store://models/model/tei/1")

    assert isinstance(sglang_function.adapters[0], VLLMAdapter)
    assert sglang_task.service_type == CoreServiceType.CLUSTER_IP
    assert sglang_run.model_name is None
    assert tei_function.path.endswith("/tei/1")
    assert tei_task.service_type == CoreServiceType.CLUSTER_IP
    assert tei_run.model_name is None

    assert build_spec(FunctionSpecTeiserve, path="huggingface://org/model").path == "huggingface://org/model"
