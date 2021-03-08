import unittest

from src.state_machine.machine import StateMachine
from src.state_machine.state import SimpleState
from src.state_machine.transition import AnnouncerTransition

from tests.test_user_interface import helper_get_testable_user_interface


class MyTestCase(unittest.TestCase):
    def test_state_machine_finishes(self):
        states = [
            SimpleState("start"),
            SimpleState("right"),
            SimpleState("left"),
            SimpleState("end"),
        ]
        transitions = [
            AnnouncerTransition(states[0], states[1], "go right"),
            AnnouncerTransition(states[0], states[2], "go left"),
            AnnouncerTransition(states[1], states[3], "end"),
            AnnouncerTransition(states[2], states[3], "end"),
        ]
        interface = helper_get_testable_user_interface(["take a right", "go to end"])
        machine = StateMachine("test", states, transitions)
        machine.run(interface)

        self.assertEqual("right", interface._stdout.outputs[0])
        self.assertEqual("end", interface._stdout.outputs[1])


if __name__ == "__main__":
    unittest.main()
