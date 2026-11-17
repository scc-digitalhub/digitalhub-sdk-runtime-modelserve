# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec
from digitalhub.entities.task._base.spec import BuildSpecMixin


class RunSpecMlflowserveBuildRun(RunSpec, BuildSpecMixin):
    """RunSpecMlflowserveBuildRun specifications."""

    path: str | None = None
