from pathlib import Path

from src.editor.buffer import Buffer


class Editor:
    def __init__(self, working_directory: Path):
        self._working_directory = working_directory.resolve()
        self._buffers = dict()

    def edit_file(self, file_path: Path) -> None:
        """Open a new buffer for file, if one doesn't already exist"""

        local_file_path = self._get_local_file_path(file_path)

        if local_file_path not in self._buffers:
            self._buffers[local_file_path] = Buffer(local_file_path)

    def _get_local_file_path(self, file_path: Path) -> Path:
        """
        Get path of file relative to working directory.

        :raises FileNotFoundError: if file couldn't be found in working directory.
        """

        # check if file is not already relative to working directory
        if self._working_directory not in file_path.parents:

            # generate local file path if it exists
            if not (local_file_path := self._working_directory / file_path).exists():
                raise FileNotFoundError(
                    f"couldn't find file {self._working_directory / file_path}"
                )
        else:
            local_file_path = file_path
        return local_file_path
