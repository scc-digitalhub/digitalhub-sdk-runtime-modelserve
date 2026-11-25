# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from unittest.mock import Mock

import pytest

import digitalhub_runtime_modelserve.entities.model.ollama.crud as ollama_crud


@pytest.mark.parametrize(
    ("source", "name"),
    [
        ("ollama://llama3", "llama3"),
        ("ollama://llama3:latest", "llama3"),
        ("ollama://library/llama3:8b", "llama3"),
    ],
)
def test_register_ollama_names_the_model_after_the_source(monkeypatch, source, name) -> None:
    register_base_model = Mock(return_value="model")
    monkeypatch.setattr(ollama_crud, "register_base_model", register_base_model)

    assert ollama_crud.register_ollama(project="my-project", source=source) == "model"

    kwargs = register_base_model.call_args.kwargs
    assert (kwargs["name"], kwargs["source"], kwargs["entity_kind"]) == (name, source, "ollama")


def test_register_ollama_keeps_an_explicit_name(monkeypatch) -> None:
    register_base_model = Mock()
    monkeypatch.setattr(ollama_crud, "register_base_model", register_base_model)

    ollama_crud.register_ollama(project="my-project", source="ollama://llama3:latest", name="assistant")

    assert register_base_model.call_args.kwargs["name"] == "assistant"


@pytest.mark.parametrize("source", ["hf://my-org/model", "store://my-project/model/ollama/model:1"])
def test_register_ollama_rejects_non_ollama_source(monkeypatch, source) -> None:
    register_base_model = Mock()
    monkeypatch.setattr(ollama_crud, "register_base_model", register_base_model)

    with pytest.raises(ValueError, match="Ollama source URI"):
        ollama_crud.register_ollama(project="my-project", source=source)

    register_base_model.assert_not_called()
