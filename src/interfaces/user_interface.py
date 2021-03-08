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
        Get a typed value from the user, loops unitl a valid input is given.

        :param value_type: Type of value to get
        :raises KeywordException - if user utters an exception keyword
        :return: Typed value
        """

        while True:
            value = self.stdin.get_input()
            assert_not_exception_keyword(value)

            try:
                return value_type(value)
            except (TypeError, ValueError):
                self.stderr.send_output(f"got an invalid {value_type.__name__} value")
