from unittest.mock import Mock

import pytest

import digitalhub_runtime_modelserve.entities.model.huggingface.crud as huggingface_crud


@pytest.mark.parametrize(
    "source",
    [
        "hf://my-org/text-classifier",
        "hf:my-org/text-classifier",
        "huggingface://my-org/text-classifier",
        ["hf://my-org/text-classifier"],
    ],
)
def test_register_huggingface_accepts_hugging_face_source(monkeypatch, source) -> None:
    register_base_model = Mock(return_value="model")
    monkeypatch.setattr(huggingface_crud, "register_base_model", register_base_model)

    result = huggingface_crud.register_huggingface(project="my-project", source=source, name="model")

    assert result == "model"
    register_base_model.assert_called_once()


@pytest.mark.parametrize("source", ["s3://my-bucket/models/model", "./models/model"])
def test_register_huggingface_rejects_non_hugging_face_source(monkeypatch, source) -> None:
    register_base_model = Mock()
    monkeypatch.setattr(huggingface_crud, "register_base_model", register_base_model)

    with pytest.raises(ValueError, match="Hugging Face source URI"):
        huggingface_crud.register_huggingface(project="my-project", source=source, name="model")

    register_base_model.assert_not_called()
