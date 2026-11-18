# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.models import CoreServiceType
from digitalhub.entities.task._base.spec import ServeSpecMixin, TaskSpecFunction


class ModelserveServeSpecMixin(ServeSpecMixin):
    service_type: CoreServiceType | None = CoreServiceType.CLUSTER_IP


class TaskSpecModelserveServe(TaskSpecFunction, ModelserveServeSpecMixin):
    """TaskSpecModelserveServe specifications."""
