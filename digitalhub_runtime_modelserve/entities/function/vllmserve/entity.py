# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.vllmserve.spec import FunctionSpecVllmserve
    from digitalhub_runtime_modelserve.entities.function.vllmserve.status import FunctionStatusVllmserve


class FunctionVllmserve(FunctionModelserve):
    """
    FunctionVllmserve class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecVllmserve
        self.status: FunctionStatusVllmserve
