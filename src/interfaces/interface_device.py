from abc import ABC


class InterfaceDevice(ABC):
    def get_input(self) -> str:
        """Get input from user"""

    def send_output(self, msg: str):
        """Send message to user"""
