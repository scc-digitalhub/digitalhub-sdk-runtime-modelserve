# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import ModelserveServeSpecMixin


class RunSpecSklearnserveRun(RunSpec, ModelserveServeSpecMixin):
    """RunSpecSklearnserveRun specifications."""

    path: str | None = None
