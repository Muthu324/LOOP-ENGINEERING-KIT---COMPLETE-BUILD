# Human Verification

Routes high-confidence output automatically, medium-confidence output to quick review, and low-confidence output to expert escalation.

## Configuration

Configure `auto_approve_threshold` and `review_threshold` from measured calibration data.

## Production checklist

- Define stopping and failure behavior.
- Log attempts, latency, quality, and estimated cost.
- Test success, retry/correction, and terminal failure.
- Avoid logging secrets or personal data.
