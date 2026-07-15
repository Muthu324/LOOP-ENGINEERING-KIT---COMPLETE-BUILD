# Retry with Exponential Backoff

Retries transient failures with capped exponential delays and optional jitter. Use for timeouts, rate limits, and temporary outages; do not retry validation or authorization errors.

## Configuration

`RetryConfig(max_attempts=3, initial_delay=1, backoff_multiplier=2, max_delay=60, jitter=True)`

## Production checklist

- Define stopping and failure behavior.
- Log attempts, latency, quality, and estimated cost.
- Test success, retry/correction, and terminal failure.
- Avoid logging secrets or personal data.
