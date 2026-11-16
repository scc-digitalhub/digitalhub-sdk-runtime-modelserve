# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from digitalhub.entities._constructors.spec import build_spec
from pydantic import ValidationError

from digitalhub_runtime_modelserve.entities.function.vllmserve.models import VLLMAdapter
from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
from digitalhub_runtime_modelserve.entities.model.mlflow.builder import ModelMlflowBuilder
from digitalhub_runtime_modelserve.entities.run.huggingfaceserve_run.spec import RunSpecHuggingfaceserveRun
from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.builder import RunKubeaiserveRunBuilder
from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.models import KubeaiFile, Scaling
from digitalhub_runtime_modelserve.entities.run.vllmserve_run.spec import RunSpecVllmserveRun
from digitalhub_runtime_modelserve.entities.task.huggingfaceserve_serve.builder import TaskHuggingfaceserveServeBuilder
from digitalhub_runtime_modelserve.entities.task.kubeaiservetext_serve.builder import TaskKubeaiserveTextServeBuilder


def test_function_spec_validates_nested_adapters() -> None:
    spec = build_spec(FunctionSpecVllmserve, adapters=[{"name": "adapter", "url": "https://example.test"}])

    assert isinstance(spec.adapters[0], VLLMAdapter)

    with pytest.raises(ValidationError):
        build_spec(FunctionSpecVllmserve, adapters=["adapter"])


def test_task_spec_preserves_replica_constraint() -> None:
    builder = TaskHuggingfaceserveServeBuilder()

    spec = builder.build_spec(function="function", huggingface_task="text_generation")
    assert spec.huggingface_task == "text_generation"

    with pytest.raises(ValidationError):
        builder.build_spec(function="function", replicas=0)


def test_run_spec_rejects_task_service_fields_and_preserves_run_fields() -> None:
    spec = build_spec(RunSpecVllmserveRun, task="task", path="model", args=["--port", "8000"])

    assert spec.path == "model"
    assert spec.args == ["--port", "8000"]
    assert spec.enable_telemetry is True
    assert spec.use_cpu_image is True

    with pytest.raises(TypeError, match="replicas"):
        build_spec(RunSpecVllmserveRun, task="task", replicas=1)

    with pytest.raises(TypeError, match="service_type"):
        build_spec(RunSpecVllmserveRun, task="task", service_type="ClusterIP")

    with pytest.raises(TypeError, match="huggingface_task"):
        build_spec(RunSpecHuggingfaceserveRun, task="task", huggingface_task="text_generation")


def test_kubeai_run_spec_preserves_constraint_and_nested_models() -> None:
    builder = RunKubeaiserveRunBuilder()
    spec = builder.build_spec(
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
        builder.build_spec(task="task", processors=0)


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
    assert serialized["input_datasets"] == [{"name": "training"}]
    assert serialized["signature"]["inputs"] == "input"
