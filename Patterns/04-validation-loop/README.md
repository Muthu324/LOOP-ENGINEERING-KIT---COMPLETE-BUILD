# Validation Loop

A provider-neutral generate/validate/correct cycle for structured or unstructured values.

## Configuration

Validators return `(score, feedback)`; correctors receive the value and feedback.

## Production checklist

- Define stopping and failure behavior.
- Log attempts, latency, quality, and estimated cost.
- Test success, retry/correction, and terminal failure.
- Avoid logging secrets or personal data.
