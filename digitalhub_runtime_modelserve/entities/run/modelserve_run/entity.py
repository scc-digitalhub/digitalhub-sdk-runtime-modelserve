# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.plugins import Run, ServeRunMixin

if typing.TYPE_CHECKING:
    from requests import Response


class RunModelserveRun(ServeRunMixin, Run):
    """
    Serve run of a model.
    """


class RunModelserveV2Run(RunModelserveRun):
    """
    Serve run of a model exposed with the V2 inference protocol.
    """

    def invoke(
        self,
        method: str | None = None,
        path: str | None = None,
        model_name: str | None = None,
        **kwargs,
    ) -> Response:
        """
        Call the service of the run, by default at the V2 inference endpoint
        of the model (``/v2/models/{model_name}/infer``).

        Parameters
        ----------
        method : str | None
            HTTP method. Defaults to POST when ``data`` or ``json`` is given,
            otherwise to GET.
        path : str | None
            Path on the service. Overrides the default path.
        model_name : str | None
            Model of the default path. Defaults to ``model``.
        **kwargs : dict
            Keyword arguments of ``requests.request()``.

        Returns
        -------
        Response
            Response of the service.
        """
        if path is None:
            path = f"/v2/models/{model_name or 'model'}/infer"
        return super().invoke(method=method, path=path, **kwargs)
