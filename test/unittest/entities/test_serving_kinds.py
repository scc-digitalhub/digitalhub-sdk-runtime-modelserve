# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from unittest.mock import Mock

import pytest
from digitalhub.factory.entity import entity_factory
from digitalhub.factory.registry import registry

import digitalhub_runtime_modelserve.entities.run.modelserve_run.entity as run_entity_module
from digitalhub_runtime_modelserve.entities.run.modelserve_run.entity import RunServiceUrlsRun

SERVING_KINDS = ("ollamaserve", "sglangserve", "teiserve")


def _entity(kind: str, spec: dict, status: dict | None = None) -> dict:
    return {
        "project": "my-project",
        "name": "service",
        "id": "1",
        "kind": kind,
        "metadata": {},
        "spec": spec,
        "status": status or {"state": "CREATED"},
    }


@pytest.mark.parametrize("kind", SERVING_KINDS)
def test_serving_kind_has_a_complete_family(kind) -> None:
    function = entity_factory.build_entity_from_dict(
        _entity(kind, {"path": "store://my-project/model/ollama/llama3:1"})
    )
    task = entity_factory.build_entity_from_dict(
        _entity(f"{kind}+serve", {"function": f"{kind}://my-project/service:1"})
    )
    run = entity_factory.build_entity_from_dict(
        _entity(f"{kind}+serve:run", {"function": f"{kind}://my-project/service:1", "task": "task"})
    )

    assert function.spec.path == "store://my-project/model/ollama/llama3:1"
    assert task.kind == f"{kind}+serve"
    assert isinstance(run, RunServiceUrlsRun)
    assert entity_factory.get_action_from_task_kind(kind, f"{kind}+serve") == "serve"
    assert registry.get_shortcut(f"new_function_{kind}").__name__ == f"new_function_{kind}"


@pytest.mark.parametrize("kind", SERVING_KINDS)
def test_serving_run_invokes_the_first_service_url(monkeypatch, kind) -> None:
    run = entity_factory.build_entity_from_dict(
        _entity(
            f"{kind}+serve:run",
            {"function": f"{kind}://my-project/service:1", "task": "task"},
            {"state": "RUNNING", "service": {"url": "service:8080", "urls": ["service:8080/v1/chat"]}},
        )
    )
    request = Mock(return_value="response")
    monkeypatch.setattr(run_entity_module.requests, "request", request)

    assert run.invoke(json={"prompt": "hello"}) == "response"
    assert run.list_endpoints() == ["http://service:8080/v1/chat"]
    request.assert_called_once_with(method="POST", url="http://service:8080/v1/chat", json={"prompt": "hello"})


def test_huggingfaceserve_is_no_longer_registered() -> None:
    assert "new_function_huggingfaceserve" not in registry.get_shortcut_names()
    assert registry.get_shortcut("register_huggingface").__name__ == "register_huggingface"
