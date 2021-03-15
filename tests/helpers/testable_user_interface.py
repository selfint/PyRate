from typing import List

from src.interfaces.interface_device import InterfaceDevice
from src.interfaces.user_interface import UserInterface


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
) -> UserInterface:
    return UserInterface(
        TestableInterfaceDevice(stdin),
        TestableInterfaceDevice(stdout),
        TestableInterfaceDevice(stderr),
    )
