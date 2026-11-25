# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import CoreServiceType, ServeSpecMixin, Spec
from pydantic import Field

from digitalhub_runtime_modelserve.entities._commons.models import KubeaiFile, Scaling


class ModelserveServeSpecMixin(ServeSpecMixin):
    """Specification fields shared by ModelServe tasks and runs."""

    service_type: CoreServiceType | None = CoreServiceType.CLUSTER_IP


class KubeaiServeSpecMixin(Spec):
    """KubeAI serving fields shared by its tasks and runs."""

    envs: dict | None = None
    image: str | None = None
    model_name: str | None = None
    args: list[str] | None = None
    processors: int | None = Field(default=None, ge=1)
    files: list[KubeaiFile] | None = None
    scaling: Scaling | None = None
