import pytest
from state_change.change_that_state import State, state_change_many


def test_empty_state():
    assert state_change_many(State.empty, '') is State.empty


def test_single_state():
    assert state_change_many(State.empty, 'h') is State.high
    assert state_change_many(State.empty, 'l') is State.low


@pytest.mark.parametrize("test_input,expected", [
    ('hh', State.empty),
    ('ll', State.empty),
    ('hl', State.low),
    ('lh', State.high),
    ('hll', State.empty),
    ('hhll', State.empty),
    ('llh', State.high),
])
def test_multi_state_change(test_input, expected):
    assert state_change_many(State.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert state_change_many(State.empty, '[hl]*llh') is State.high


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(ValueError):
        state_change_many(State.empty, 'x')


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"

# def test_many_slaps():
#     assert slap_many(LikeState.empty, 'hh') is State.empty
#     assert slap_many(LikeState.empty, 'll') is State.empty
#     assert slap_many(LikeState.empty, 'hl') is State.low
#     assert slap_many(LikeState.empty, 'lh') is State.high
#     assert slap_many(LikeState.empty, 'hll') is State.empty
#     assert slap_many(LikeState.empty, 'hhll') is State.empty
#     assert slap_many(LikeState.empty, 'llh') is State.high
