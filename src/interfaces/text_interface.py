from src.interfaces.interface_device import InterfaceDevice


class TextIO(InterfaceDevice):
    """Get commands through the CLI"""

    def get_input(self) -> str:
        return input("> ").lower().strip()

    def send_output(self, msg: str):
        print(msg)
