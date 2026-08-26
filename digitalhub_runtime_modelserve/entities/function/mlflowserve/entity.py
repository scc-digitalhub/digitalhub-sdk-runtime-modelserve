# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub_runtime_modelserve.entities._commons.enums import Actions
from digitalhub_runtime_modelserve.entities.function.modelserve.entity import FunctionModelserve

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.function.mlflowserve.spec import FunctionSpecMlflowserve
    from digitalhub_runtime_modelserve.entities.function.mlflowserve.status import FunctionStatusMlflowserve


class FunctionMlflowserve(FunctionModelserve):
    """
    FunctionMlflowserve class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: FunctionSpecMlflowserve
        self.status: FunctionStatusMlflowserve

    def build(
        self,
        wait: bool = True,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        **kwargs,
    ):
        """Build the function using the build action."""
        return super().run(
            Actions.BUILD.value,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )

    def run(
        self,
        action: str,
        wait: bool = False,
        log_info: bool = True,
        extensions: list[dict] | None = None,
        auto_build: bool = True,
        **kwargs,
    ):
        """Run the function, building it when no image is available."""
        if auto_build and self.spec.image is None:
            self.build(wait=True, log_info=log_info)

        return super().run(
            action,
            wait=wait,
            log_info=log_info,
            extensions=extensions,
            **kwargs,
        )
