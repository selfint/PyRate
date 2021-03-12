from pathlib import Path


class Editor:
    def __init__(self):
        self._buffers = dict()

    def edit_file(self, file_path: Path) -> None:
        """Read file text into a buffer."""

        self._buffers[file_path] = file_path.read_text()
