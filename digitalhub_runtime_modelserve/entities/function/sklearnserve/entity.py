# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.sklearnserve.spec import FunctionSpecSklearnserve
    from digitalhub_runtime_modelserve.entities.function.sklearnserve.status import FunctionStatusSklearnserve


class FunctionSklearnserve(FunctionModelserve):
    """
    FunctionSklearnserve class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecSklearnserve
        self.status: FunctionStatusSklearnserve
