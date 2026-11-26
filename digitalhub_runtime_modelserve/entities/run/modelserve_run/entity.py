# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import time
import typing

import requests
from digitalhub.factory.entity import entity_factory
from digitalhub.plugins import EntityRef, Run, State
from digitalhub.utils.exceptions import EntityError
from digitalhub.utils.logger.logger import get_logger

from digitalhub_runtime_modelserve.entities._commons.enums import Actions

if typing.TYPE_CHECKING:
    from digitalhub_runtime_modelserve.entities.run.modelserve_run.spec import RunSpecModelserveRun
    from digitalhub_runtime_modelserve.entities.run.modelserve_run.status import RunStatusModelserveRun
logger = get_logger(__file__)


class RunModelserveRun(Run):
    """
    RunModelserveRun class.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.spec: RunSpecModelserveRun
        self.status: RunStatusModelserveRun

    def wait(
        self,
        log_info: bool = True,
        timeout: float | None = None,
        poll_interval: float = 5.0,
    ) -> Run:
        """
        Wait for run to finish.

        Parameters
        ----------
        log_info : bool
            If True, log information.
        timeout : float | None
            Maximum wait time in seconds.
        poll_interval : float
            Time between status checks in seconds.

        Returns
        -------
        Run
            Run object.
        """
        task_kind = EntityRef.parse(self.spec.task).kind
        action = entity_factory.get_action_from_task_kind(self.kind, task_kind)

        if action == Actions.SERVE.value:
            serve_timeout = 300
            start = time.time()

            while time.time() - start < serve_timeout:
                if log_info:
                    logger.info(f"Waiting for run {self.id} to deploy service.")

                self.refresh()
                if self.status.service is not None:
                    if log_info:
                        msg = f"Run {self.id} service deployed."
                        logger.info(msg)
                    return self

                elif self.status.state == State.ERROR.value:
                    if log_info:
                        msg = f"Run {self.id} serving failed."
                        logger.info(msg)
                    return self

                time.sleep(5)

            if log_info:
                msg = f"Waiting for run {self.id} service timed out. Check logs for more information."
                logger.info(msg)

            return self

        return super().wait(
            log_info=log_info,
            timeout=timeout,
            poll_interval=poll_interval,
        )

    def _check_service(self) -> None:
        """
        Check if the service is available.
        """
        if self.status.service is None:
            raise RuntimeError("Service is not available for this run.")

    def _get_base_url(self) -> str:
        """
        Get base URL from service.

        Returns
        -------
        str
            Base URL.
        """
        try:
            base_url: str = self.status.service.get("url")
            return self._strip_http(base_url)
        except AttributeError:
            raise EntityError(
                "Url not specified and service not found on run status."
                " If a service is deploying, use run.wait() or try again later."
            )

    def _eval_url(self, url: str, base_url: str) -> None:
        """
        Evaluate if URL starts with base URL.

        Parameters
        ----------
        url : str
            URL to evaluate.
        base_url : str
            Base URL.

        Raises
        ------
        EntityError
            If URL does not start with base URL.
        """
        stripped_url = self._strip_http(url)
        if not stripped_url.startswith(base_url):
            raise EntityError(f"Invalid URL: {stripped_url}. It must start with the service URL: {base_url}")

    @staticmethod
    def _strip_http(url: str) -> str:
        """
        Strip http:// or https:// from URL.

        Parameters
        ----------
        url : str
            URL to strip.

        Returns
        -------
        str
            Stripped URL.
        """
        return url.removeprefix("http://").removeprefix("https://")

    @staticmethod
    def _prepend_http(url: str) -> str:
        """
        Prepend http:// to URL if it does not start with http:// or https://.

        Parameters
        ----------
        url : str
            URL to prepend.

        Returns
        -------
        str
            URL with http:// prepended if it was not already present.
        """
        if not url.startswith("http://") and not url.startswith("https://"):
            return f"http://{url}"
        return url


class RunServiceUrlsRun(RunModelserveRun):
    """
    Serve run invoked through the URLs its service publishes.
    """

    def invoke(
        self,
        method: str = "POST",
        url: str | None = None,
        **kwargs,
    ) -> requests.Response:
        """
        Invoke served model.
        The method defaults to "POST" if data or json is provided in kwargs,
        otherwise it defaults to "GET". The function returns a requests.Response
        object.

        Parameters
        ----------
        method : str
            Method of the request (e.g., "GET", "POST").
        url : str
            URL to invoke. If specified, it must start with the service URL
            (http:// or https:// prefixes are required and stripped before comparison).
        **kwargs : dict
            Keyword arguments to pass to the request.

        Returns
        -------
        requests.Response
            Response from the request.
        """
        self._check_service()
        base_url: str = self._get_base_url()

        if url is None:
            url = self.status.service.get("urls")[0]
            url = self._prepend_http(url)
        else:
            self._eval_url(url, base_url)

        if "data" not in kwargs and "json" not in kwargs:
            method = "GET"

        return requests.request(method=method, url=url, **kwargs)

    def list_endpoints(self) -> list[str]:
        """
        List all available endpoints for the served model.

        Returns
        -------
        list[str]
            List of available endpoints.
        """
        self._check_service()
        urls = self.status.service.get("urls", [])
        return [self._prepend_http(url) for url in urls]
