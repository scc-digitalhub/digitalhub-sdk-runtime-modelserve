# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.plugins import BuildSpecMixin, RunSpecFunction


class RunSpecMlflowserveBuildRun(RunSpecFunction, BuildSpecMixin):
    """RunSpecMlflowserveBuildRun specifications."""

    path: str | None = None
