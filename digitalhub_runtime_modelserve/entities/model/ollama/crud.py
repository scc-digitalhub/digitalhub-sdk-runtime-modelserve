# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.model._base.crud import register_base_model

from digitalhub_runtime_modelserve.entities._commons.enums import EntityKinds

if typing.TYPE_CHECKING:
    from digitalhub.entities.model.model.entity import ModelModel

OLLAMA_SCHEME = "ollama://"


def register_ollama(
    project: str,
    source: str,
    name: str | None = None,
    uuid: str | None = None,
    version: str | None = None,
    description: str | None = None,
    labels: list[str] | None = None,
    embedded: bool = False,
    extensions: list[dict] | None = None,
    framework: str | None = None,
    algorithm: str | None = None,
    parameters: dict | None = None,
    **kwargs,
) -> ModelModel:
    """
    Register an Ollama model entity for a model in the Ollama library.

    Parameters
    ----------
    project : str
        Project name.
    source : str
        Ollama URI of the model, such as ``ollama://llama3:latest``.
    name : str, optional
        Entity name. If omitted, it is the model name in ``source``
        (``llama3`` for ``ollama://library/llama3:latest``).
    uuid : str, optional
        Entity identifier.
    version : str, optional
        Entity version.
    description : str, optional
        Human-readable entity description.
    labels : list[str], optional
        Entity labels.
    embedded : bool, default=False
        Whether to embed the entity specification in the project specification.
    extensions : list[dict], optional
        Entity extensions.
    framework : str, optional
        Model framework.
    algorithm : str, optional
        Model algorithm.
    parameters : dict, optional
        Model parameters.
    **kwargs : dict
        Additional model specification parameters.

    Returns
    -------
    ModelModel
        Registered model entity.

    Examples
    --------
    ```python
    import digitalhub as dh

    model = dh.register_ollama(project="my-project", source="ollama://llama3:latest")
    ```
    """
    if not source.startswith(OLLAMA_SCHEME):
        raise ValueError("register_ollama requires an Ollama source URI (scheme 'ollama').")
    if name is None:
        name = _name_from_source(source)

    return register_base_model(
        project=project,
        source=source,
        entity_kind=EntityKinds.MODEL_OLLAMA.value,
        name=name,
        uuid=uuid,
        version=version,
        description=description,
        labels=labels,
        embedded=embedded,
        extensions=extensions,
        framework=framework,
        algorithm=algorithm,
        parameters=parameters,
        **kwargs,
    )


def _name_from_source(source: str) -> str:
    """Return the model name of an Ollama URI, without namespace and tag."""
    reference = source.removeprefix(OLLAMA_SCHEME)
    return reference.rsplit("/", 1)[-1].split(":", 1)[0]
