from typing import Dict, Any

from src.interfaces.user_interface import UserInterface
from src.state_machine.state import State
from abc import ABC


class Transition(ABC):
    """A transition from a state to a state."""

    def __init__(self, origin: State, destination: State, name: str):
        self.origin = origin
        self.destination = destination
        self.name = name

    def transition(self, registers: Dict[str, Any], interface: UserInterface):
        """
        Make the transition.

        :param registers: Registers of a state machine to read/write from/to.
        :param interface: User interface to interact through.
        """

        raise NotImplementedError()


class AnnouncerTransition(Transition):
    """Announce the destination of the transition."""

    def transition(self, registers: Dict[str, Any], interface: UserInterface):
        interface.send_output(self.destination.name)
