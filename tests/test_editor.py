import unittest

from src.editor.editor import Editor

from pathlib import Path


TEST_TEMP_FILE = Path("test_temp_file.py")


class TestEditor(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TEMP_FILE.touch(exist_ok=True)

    def tearDown(self) -> None:
        TEST_TEMP_FILE.unlink(missing_ok=True)

    def test_editor_can_edit_files(self):
        e = Editor()
        e.edit_file(TEST_TEMP_FILE)


if __name__ == "__main__":
    unittest.main()
