# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.spec import (
        FunctionSpecKubeaiserveSpeechtotext,
    )
    from digitalhub_runtime_modelserve.entities.function.kubeaiservespeechtotext.status import (
        FunctionStatusKubeaiserveSpeechtotext,
    )


class FunctionKubeaiserveSpeechtotext(FunctionModelserve):
    """
    FunctionKubeaiserveSpeechtotext class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecKubeaiserveSpeechtotext
        self.status: FunctionStatusKubeaiserveSpeechtotext
