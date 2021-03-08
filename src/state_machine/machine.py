from typing import List

from src.state_machine.state import State
from src.interfaces.exceptions import Quit, Cancel
from src.interfaces.user_interface import UserInterface
from src.state_machine.transition import Transition


class StateMachine:
    """Can transition between states."""

    def __init__(self, name: str, states: List[State], transitions: List[Transition]):
        """
        Generate a state machine from states and transitions.

        Assumes first state is the start and last state is the end.

        :param name: Name of the state machine.
        :param states: States in the state machine.
        :param transitions: Transitions in the state machine.
        """

        assert len(states) > 0, "must have at least one state"

        self.name = name
        self.states = states
        self.transitions = transitions

        self.start_state = states[0]
        self.end_state = states[-1]

        self.current_state = self.start_state

        self.registers = dict()
        self.transitions_dict = {
            state: [transition for transition in transitions if transition.origin]
            for state in states
        }

    def run(self, interface: UserInterface):
        """Run the state machine until the end State is reached."""

        while self.current_state is not self.end_state:

            transition = self._get_transition(interface)

            try:
                transition.transition(self.registers, interface)
            except Cancel:
                interface.send_output(f"Cancelled {transition.name}")
            except Quit:
                interface.send_output(f"Quitting")
                return
            except Exception:
                interface.send_error(f"Failed {transition.name}")
            else:
                self.current_state = transition.destination

    def _get_transition(self, interface: UserInterface) -> Transition:
        """Get transition from user."""

        transition_options = self._get_transition_options_from_state()
        transition_option = interface.get_similar([list(transition_options.keys())])
        transition = transition_options[transition_option]

        return transition

    def _get_transition_options_from_state(self):
        """Get dictionary with all options from a state."""
        options = {
            transition.name: transition
            for transition in self.transitions_dict[self.current_state]
        }

        return options
