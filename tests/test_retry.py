import pytest
from loop_engineering_kit import RetryConfig, RetryLoop

def test_succeeds_after_retry():
    state={"n":0}
    def operation():
        state["n"] += 1
        if state["n"] < 3: raise TimeoutError
        return "ok"
    loop=RetryLoop(RetryConfig(max_attempts=3, initial_delay=0, jitter=False), sleep=lambda _: None)
    assert loop.execute(operation) == "ok"
    assert state["n"] == 3

def test_raises_after_limit():
    loop=RetryLoop(RetryConfig(max_attempts=2, initial_delay=0), sleep=lambda _: None)
    with pytest.raises(ValueError): loop.execute(lambda: (_ for _ in ()).throw(ValueError("bad")))
