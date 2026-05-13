# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub_runtime_modelserve.entities.run.kubeaiserve_run.spec import (
    RunSpecKubeaiserveRun,
    RunValidatorKubeaiserveRun,
)


class RunSpecKubeaiserveTextRun(RunSpecKubeaiserveRun):
    """RunSpecKubeaiserveTextRun specifications."""

    def __init__(
        self,
        task: str,
        function: str | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        model_name: str | None = None,
        url: str | None = None,
        image: str | None = None,
        adapters: list[dict] | None = None,
        processors: int | None = None,
        env: dict | None = None,
        args: list[str] | None = None,
        cache_profile: str | None = None,
        scaling: dict | None = None,
        files: list[dict] | None = None,
        features: list[str] | None = None,
        engine: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            task=task,
            function=function,
            envs=envs,
            secrets=secrets,
            profile=profile,
            model_name=model_name,
            url=url,
            image=image,
            adapters=adapters,
            processors=processors,
            env=env,
            args=args,
            cache_profile=cache_profile,
            scaling=scaling,
            files=files,
            **kwargs,
        )
        self.features = features
        self.engine = engine


class RunValidatorKubeaiserveTextRun(RunValidatorKubeaiserveRun):
    """RunValidatorKubeaiserveTextRun validator."""

    features: list[str] | None = None
    engine: str | None = None
