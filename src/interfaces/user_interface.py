from typing import TypeVar

from src.interfaces.interface_device import InterfaceDevice
from src.interfaces.exceptions import assert_not_exception_keyword


SupportedInputValueType = TypeVar("SupportedInputValueType", int, str)


class UserInterface:
    def __init__(
        self, stdin: InterfaceDevice, stdout: InterfaceDevice, stderr: InterfaceDevice
    ):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr

    def get_value(self, value_type: SupportedInputValueType) -> SupportedInputValueType:
        """
        Get a typed value from the user

        Raises KeywordException - if user utters an exception keyword
        """

        while True:
            value = self.stdin.get_input()
            assert_not_exception_keyword(value)

            try:
                typed_value: SupportedInputValueType = value_type(value)

                return typed_value
            except (TypeError, ValueError):
                self.stderr.send_output(f"got an invalid {value_type.__name__} value")
