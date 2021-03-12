import unittest

from src.editor.parser import Parser


class TestParser(unittest.TestCase):
    def test_parse_file_is_lossless(self):
        file_text = """
class Foo:
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y
        
    def bar(self) -> int:
        '''add x and y'''
        
        return self.x + int(self.y)
    """

        p = Parser()

        tree = p.parse(file_text)

        self.assertEqual(file_text, tree.code)


if __name__ == "__main__":
    unittest.main()
