# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.vllmserve.entity import FunctionVllmserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.vllmservepooling.spec import FunctionSpecVllmservepooling
    from digitalhub_runtime_modelserve.entities.function.vllmservepooling.status import FunctionStatusVllmservepooling


class FunctionVllmservepooling(FunctionVllmserve):
    """
    FunctionVllmservepooling class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecVllmservepooling
        self.status: FunctionStatusVllmservepooling
