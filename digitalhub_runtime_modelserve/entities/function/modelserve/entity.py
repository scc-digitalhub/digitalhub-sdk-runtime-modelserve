# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.function._base.entity import Function

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.modelserve.spec import FunctionSpecModelserve
    from digitalhub_runtime_modelserve.entities.function.modelserve.status import FunctionStatusModelserve


class FunctionModelserve(Function):
    """
    FunctionModelserve class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecModelserve
        self.status: FunctionStatusModelserve
