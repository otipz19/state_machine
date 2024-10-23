import time
from encodings.punycode import selective_find
from typing import Callable

from state import State

class StateMachine:
    def __init__(self):
        self.__states: [State] = []
        self.__current_state: State = None
        self.__last_transition_time_in_sec: float = time.perf_counter()

    def add_state(self, name: str, state_function: Callable[[], None]) -> None:
        self.__states.append(State(name, state_function))

    def run_current_state(self) -> None:
        if self.__current_state is not None:
            self.__current_state.run()

    def go_to_next_state(self) -> None:
        if self.__current_state is not None:
            self.__current_state = self.__get_state_by_name(self.__current_state.get_next_state_name())
        elif self.__states is not None and len(self.__states) > 0:
            self.__current_state = self.__states[0]
        self.__last_transition_time_in_sec = time.perf_counter()

    def __get_state_by_name(self, name: str) -> State:
        for state in self.__states:
            if state.get_name() == name:
                return state
        raise Exception(f'State with name {name} not found.')

    def add_transition(self, from_state: str, to_state: str, should_transition_function: Callable[[], bool]) -> None:
        if from_state == "*":
            self.__add_transition_to_all(to_state, should_transition_function)
        else:
            state = self.__get_state_by_name(from_state)
            state.add_transition(to_state, should_transition_function)

    def __add_transition_to_all(self, to_state: str, should_transition_function: Callable[[], bool]) -> None:
        for state in self.__states:
            # prevent transition loops
            if state.get_name() != to_state:
                state.add_transition(to_state, should_transition_function)

    def has_timeout_passed_since_last_transition(self, timeout: float) -> bool:
        return (time.perf_counter() - self.__last_transition_time_in_sec) >= timeout

