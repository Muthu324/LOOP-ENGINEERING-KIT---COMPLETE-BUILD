from loop_engineering_kit.retry import RetryConfig, RetryLoop

if __name__ == "__main__":
    attempts = 0
    def flaky():
        global attempts
        attempts += 1
        if attempts < 3: raise TimeoutError("temporary failure")
        return "success"
    print(RetryLoop(RetryConfig(jitter=False)).execute(flaky))
