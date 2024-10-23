from typing import Callable

class Transition:
    def __init__(self, to_state_name: str, should_transition_function: Callable[[], bool]):
        self.__to_state_name = to_state_name
        self.__should_transition_function = should_transition_function

    def should_transition(self) -> bool:
        return self.__should_transition_function()

    def get_to_state_name(self) -> str:
        return self.__to_state_name