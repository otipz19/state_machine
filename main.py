import time

from state_machine import StateMachine

if __name__ == '__main__':
    should_go_to_retreat: bool = False
    should_go_to_attack: bool = False
    should_go_to_search: bool = False

    logs: [str] = []

    state_machine = StateMachine()
    state_machine.add_state("search", lambda: logs.append("search"))
    state_machine.add_state("attack", lambda: logs.append("attack"))
    state_machine.add_state("retreat", lambda: logs.append("retreat"))

    state_machine.add_transition("*", "retreat", lambda: should_go_to_retreat)
    state_machine.add_transition("search", "attack", lambda: should_go_to_attack)
    state_machine.add_transition("attack", "search", lambda: should_go_to_search)
    state_machine.add_transition("retreat", "search", lambda: state_machine.has_timeout_passed_since_last_transition(0.5))

    state_machine.go_to_next_state()
    state_machine.run_current_state()

    should_go_to_retreat = True

    state_machine.go_to_next_state()
    state_machine.run_current_state()

    time.sleep(0.5)

    state_machine.go_to_next_state()
    state_machine.run_current_state()

    should_go_to_retreat = False
    should_go_to_attack = True

    state_machine.go_to_next_state()
    state_machine.run_current_state()

    should_go_to_search = True

    state_machine.go_to_next_state()
    state_machine.run_current_state()

    print(logs)