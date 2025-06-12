# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.task.modelserve_serve.spec import (
    TaskSpecModelserveServe,
    TaskValidatorModelserveServe,
)


class TaskSpecMlflowserveServe(TaskSpecModelserveServe):
    """
    TaskSpecMlflowserveServe specifications.
    """


class TaskValidatorMlflowserveServe(TaskValidatorModelserveServe):
    """
    TaskValidatorMlflowserveServe validator.
    """
