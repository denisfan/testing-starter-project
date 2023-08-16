import enum


class State(enum.Enum):
    empty = enum.auto()
    high = enum.auto()
    low = enum.auto()


state_high_trainsitions = {
    State.empty: State.high,
    State.high: State.empty,
    State.low: State.high,
}

state_low_transitions = {
    State.empty: State.low,
    State.high: State.low,
    State.low: State.empty,
}


def state_change_high(s: State) -> State:
    return state_high_trainsitions[s]


def state_change_low(s: State) -> State:
    return state_low_transitions[s]


def state_change_many(s: State, states: str) -> State:
    for c in states:
        c = c.lower()
        if c == 'h':
            s = state_change_high(s)
        elif c == 'l':
            s = state_change_low(s)
        else:
            raise ValueError('invalid slap')
    return s
