# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import ExecutableBuildMixin

from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub.plugins import Status

    from digitalhub_runtime_modelserve.entities.function.modelserve.spec import FunctionSpecModelserve


class FunctionMlflowserve(ExecutableBuildMixin, FunctionModelserve):
    """
    FunctionMlflowserve class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecModelserve
        self.status: Status
