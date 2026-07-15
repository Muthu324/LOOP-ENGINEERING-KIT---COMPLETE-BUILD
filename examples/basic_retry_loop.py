from loop_engineering_kit import RetryConfig, RetryLoop

attempts = 0
def unstable_operation():
    global attempts
    attempts += 1
    if attempts < 2: raise ConnectionError("temporary network issue")
    return {"ok": True, "attempts": attempts}

if __name__ == "__main__":
    loop = RetryLoop(RetryConfig(max_attempts=3, initial_delay=0.1, jitter=False))
    print(loop.execute(unstable_operation))
    print(loop.get_metrics())
