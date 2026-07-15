# Cost Optimization

Combines exact caching with complexity-based routing between inexpensive and capable model functions.

## Configuration

Replace the in-memory cache with a bounded, persistent cache in production.

## Production checklist

- Define stopping and failure behavior.
- Log attempts, latency, quality, and estimated cost.
- Test success, retry/correction, and terminal failure.
- Avoid logging secrets or personal data.
