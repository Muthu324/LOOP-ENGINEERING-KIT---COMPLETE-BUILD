# Testing Guide

Test loops as state machines, not only as happy-path functions.

## Required cases

- Success on the first attempt
- Success after retries or corrections
- Exhausted attempts
- Validator exception
- Timeout and budget exhaustion
- Non-improving correction
- Human review and escalation
- Cache hit, miss, and eviction

Use fake model functions and injected sleep functions so tests remain deterministic and fast. Assert the result, iteration count, callbacks, and metrics. Keep real-provider integration tests separate and protect them with spending caps.
