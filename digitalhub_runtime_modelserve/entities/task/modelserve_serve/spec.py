# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.models import CoreServiceType
from digitalhub.entities.task._base.spec import TaskSpecFunction
from pydantic import Field


class TaskSpecModelserveServe(TaskSpecFunction):
    """TaskSpecModelserveServe specifications."""

    replicas: int | None = Field(default=None, ge=1)
    service_type: CoreServiceType | None = None
    service_name: str | None = None
