# Self-Correction Loop

Generates an answer, validates it, carries structured feedback forward, and stops at a quality threshold or iteration limit.

## Configuration

Return `ValidationResponse` with a status, score, feedback, and optional errors.

## Production checklist

- Define stopping and failure behavior.
- Log attempts, latency, quality, and estimated cost.
- Test success, retry/correction, and terminal failure.
- Avoid logging secrets or personal data.
