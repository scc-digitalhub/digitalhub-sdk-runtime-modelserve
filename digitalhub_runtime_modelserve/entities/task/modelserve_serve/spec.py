# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import TaskSpecFunction

from digitalhub_runtime_modelserve.entities._mixin.execution.spec import ModelserveServeSpecMixin


class TaskSpecModelserveServe(TaskSpecFunction, ModelserveServeSpecMixin):
    """TaskSpecModelserveServe specifications."""
