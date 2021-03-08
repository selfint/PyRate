import unittest
from typing import List

from src.interfaces.user_interface import UserInterface
from src.interfaces.interface_device import InterfaceDevice


class TestableInterfaceDevice(InterfaceDevice):
    def __init__(self, inputs: List[str]):
        self.inputs = inputs
        self.index = 0
        self.outputs = []
        self.last_output = None

    def get_input(self):
        if self.index >= len(self.inputs):
            raise Exception("Test input index got out of range - test failed")

        value = self.inputs[self.index]
        self.index += 1
        return value

    def send_output(self, msg: str):
        self.outputs.append(msg)
        self.last_output = msg

    def get_output(self):
        return self.last_output


def helper_get_testable_user_interface(
    stdin: List[str] = [], stdout: List[str] = [], stderr: List[str] = []
):
    return UserInterface(
        TestableInterfaceDevice(stdin),
        TestableInterfaceDevice(stdout),
        TestableInterfaceDevice(stderr),
    )


class TestUserInterface(unittest.TestCase):
    def test_get_value_type_casting(self):
        interface = helper_get_testable_user_interface(["5", "hello world"])

        self.assertEqual(5, interface.get_value(int))
        self.assertEqual("hello world", interface.get_value(str))

    def test_get_value_exception(self):
        interface = helper_get_testable_user_interface(["hello world", "5"])

        value = interface.get_value(int)

        # make sure that user interface generates the correct error message
        self.assertEqual("not a valid int value", interface.stderr.get_output())

        # and that it calls the get input again
        self.assertEqual(5, value)

    def test_get_similar(self):
        interface = helper_get_testable_user_interface(["sum variables"])
        self.assertEqual(
            "sum numbers", interface.get_similar([["subtract"], ["sum numbers"]])
        )


if __name__ == "__main__":
    unittest.main()
