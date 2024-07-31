from __future__ import annotations

from digitalhub_core.entities._base.status import Status


class ArtifactStatus(Status):
    """
    Status class for artifact entities.
    """

    def __init__(
        self,
        state: str,
        message: str | None = None,
        files: list[dict] | None = None,
        **kwargs,
    ) -> None:
        """
        Constructor.

        Parameters
        ----------
        **kwargs : dict
            Keywords arguments.
        """
        super().__init__(state, message)
        self.files = files

    def add_file(self, files: list) -> None:
        """
        Add a file to the status.

        Parameters
        ----------
        files : list
            Files to add.

        Returns
        -------
        None
        """

        # Add the file to the list
        if self.files is None:
            self.files = []

        for file in files:
            # Remove the file info if it already exists
            self.files = [f for f in self.files if (f["path"] != file["path"] or f["hash"] != file["hash"])]

            # Add the new file
            self.files.append(file)


class ArtifactStatusArtifact(ArtifactStatus):
    """
    Status class for artifact entities.
    """