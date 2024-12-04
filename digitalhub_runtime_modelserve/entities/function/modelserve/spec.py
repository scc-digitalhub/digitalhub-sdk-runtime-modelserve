from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecModelserve(FunctionSpec):
    """
    FunctionSpecModelserve specifications.
    """

    def __init__(
        self,
        path: str | None = None,
        model_name: str | None = None,
        image: str | None = None,
    ) -> None:
        super().__init__()
        self.path = path
        self.model_name = model_name
        self.image = image


class FunctionValidatorModelserve(FunctionValidator):
    """
    FunctionValidatorModelserve validator.
    """

    path: str = None
    "Path to the model files"

    model_name: str = None
    "Name of the model"

    image: str = None
    "Image where the function will be executed"
