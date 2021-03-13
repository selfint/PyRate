import unittest

from src.interfaces.exceptions import ExceptionsKeywordsDict
from tests.helpers.testable_user_interface import helper_get_testable_user_interface


class TestUserInterface(unittest.TestCase):
    def test_get_value_type_casting(self):
        interface = helper_get_testable_user_interface(["5", "hello world"])

        self.assertEqual(5, interface.get_value(int))
        self.assertEqual("hello world", interface.get_value(str))

    def test_get_value_invalid_value_error_response(self):
        interface = helper_get_testable_user_interface(["hello world", "5"])

        value = interface.get_value(int)

        # make sure that user interface generates the correct error message
        self.assertEqual("not a valid int value", interface._stderr.get_output())

        # and that it calls the get input again
        self.assertEqual(5, value)

    def test_get_similar(self):
        interface = helper_get_testable_user_interface(["sum variables"])
        self.assertEqual(
            "sum numbers", interface.get_similar([["subtract"], ["sum numbers"]])
        )

    def test_get_value_keyword_exceptions(self):
        for keyword, exception in ExceptionsKeywordsDict.items():
            interface = helper_get_testable_user_interface([keyword])
            with self.assertRaises(exception):
                interface.get_value(int)

    def test_get_similar_keyword_exceptions(self):
        for keyword, exception in ExceptionsKeywordsDict.items():
            interface = helper_get_testable_user_interface([keyword])
            with self.assertRaises(exception):
                interface.get_similar([["cancel"], ["test"], ["quit"]])


if __name__ == "__main__":
    unittest.main()
