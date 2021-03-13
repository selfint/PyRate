from pathlib import Path

from src.editor.parser import Parser


class Buffer:
    def __init__(self, file_path: Path):
        self._file_path = file_path

        self._text = "" if not file_path.exists() else file_path.read_text()
        self._tree = Parser().parse(self._text)
