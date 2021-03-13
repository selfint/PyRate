import unittest

from src.editor.editor import Editor

from pathlib import Path


TEST_WORKING_DIRECTORY = Path("./test_temp_wd")
TEST_TEMP_FILE = Path("test_editor_temp_file.py")


class TestEditor(unittest.TestCase):
    def setUp(self) -> None:
        TEST_WORKING_DIRECTORY.mkdir(parents=True, exist_ok=True)
        (TEST_WORKING_DIRECTORY / TEST_TEMP_FILE).touch(exist_ok=True)

    def tearDown(self) -> None:
        (TEST_WORKING_DIRECTORY / TEST_TEMP_FILE).unlink(missing_ok=True)
        TEST_WORKING_DIRECTORY.rmdir()

    def test_editor_can_edit_files(self):
        e = Editor(TEST_WORKING_DIRECTORY)
        e.edit_file(TEST_TEMP_FILE)


if __name__ == "__main__":
    unittest.main()
