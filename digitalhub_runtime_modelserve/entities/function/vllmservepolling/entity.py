# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.vllmserve.entity import FunctionVllmserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.vllmservepolling.spec import FunctionSpecVllmservepolling
    from digitalhub_runtime_modelserve.entities.function.vllmservepolling.status import FunctionStatusVllmservepolling


class FunctionVllmservepolling(FunctionVllmserve):
    """
    FunctionVllmservepolling class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecVllmservepolling
        self.status: FunctionStatusVllmservepolling
