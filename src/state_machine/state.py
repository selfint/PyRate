from abc import ABC


class State(ABC):
    def __init__(self, name: str):
        self.name = name


class SimpleState(State):
    pass
