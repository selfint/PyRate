import libcst as cst


class Parser:
    def __init__(self):
        pass

    def parse(self, file_text: str) -> cst.CSTNode:
        """Generate a concrete syntax tree for the text in a file"""

        tree = cst.parse_module(file_text)

        return tree
