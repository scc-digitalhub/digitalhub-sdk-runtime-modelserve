"""
Spec factory entity.
"""
from __future__ import annotations

import importlib
import typing

from pydantic import ValidationError

from sdk.entities.artifacts.spec import ArtifactParams, ArtifactSpec
from sdk.entities.dataitems.spec import DataitemParams, DataitemSpec
from sdk.entities.projects.spec import ProjectParams, ProjectSpec
from sdk.entities.runs.spec import RunParams, RunSpec
from sdk.entities.workflows.spec import WorkflowParams, WorkflowSpec
from sdk.utils.commons import ARTF, DTIT, PROJ, RUNS, WKFL
from sdk.utils.exceptions import EntityError
from sdk.utils.modules_utils import import_registry

if typing.TYPE_CHECKING:
    from sdk.entities._base.spec import Spec


REGISTRY = {
    "artifact": [ArtifactSpec, ArtifactParams],
    "dataitem": [DataitemSpec, DataitemParams],
    "project": [ProjectSpec, ProjectParams],
    "run": [RunSpec, RunParams],
    "workflow": [WorkflowSpec, WorkflowParams],
}


def build_spec(
    entity: str, kind: str, ignore_validation: bool = False, module_kind: str | None = None, **kwargs
) -> Spec:
    """
    Build runtimes.

    Parameters
    ----------
    entity : str
        Type of entity.
    kind : str
        The type of Spec to build.
    ignore_validation : bool
        Whether to ignore the validation of the parameters.
    module_kind : str, optional
        The module to import (for function and tasks).
    **kwargs
        Keyword arguments.


    Returns
    -------
    Spec
        A Spec object with the given parameters.
    """
    try:
        if module_kind is not None:
            # Import registry
            registry = import_registry(module_kind)

            # Get name of module and class
            obj = registry.get_spec(entity, kind)

            # Import spec and model
            module = importlib.import_module(obj.module)
            class_spec = getattr(module, obj.class_spec)
            class_params = getattr(module, obj.class_params)
        else:
            # Get spec and model
            class_spec, class_params = REGISTRY[kind]

        # Validate arguments
        if not ignore_validation:
            kwargs = class_params(**kwargs).model_dump()

        return class_spec(**kwargs)
    except (ModuleNotFoundError, ImportError):
        raise ValueError(f"Runtime {kind} not found")
    except KeyError:
        raise EntityError(f"Unsupported parameters kind {kind} for entity {entity}")
    except ValidationError as err:
        raise EntityError(f"Invalid parameters for kind {kind} for entity {entity}") from err