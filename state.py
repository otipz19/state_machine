from typing import Callable

from transition import Transition

class State:
    def __init__(self, name: str, state_function: Callable[[], None]):
        self.__name = name
        self.__state_function = state_function
        self.__transitions: [Transition] = []

    def add_transition(self, to_state: str, should_transition_function: Callable[[], bool]) -> None:
        self.__transitions.append(Transition(to_state, should_transition_function))

    def remove_transitions_to_state(self, to_state: str) -> None:
        self.__transitions = [transition for transition in self.__transitions if transition.to_state != to_state]

    def remove_all_transitions(self) -> None:
        self.__transitions = []

    def get_next_state_name(self) -> str:
        for transition in self.__transitions:
            if transition.should_transition():
                return transition.get_to_state_name()

        return self.__name

    def run(self) -> None:
        self.__state_function()

    def equals(self, name: str) -> bool:
        return name == self.__name

    def get_name(self) -> str:
        return self.__name