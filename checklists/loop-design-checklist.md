# Production Loop Design Checklist

- [ ] Quality target is documented.
- [ ] Maximum iterations, timeout, and budget are enforced.
- [ ] Only transient failures are retried.
- [ ] Backoff is capped and uses jitter.
- [ ] Validation is deterministic where practical.
- [ ] Feedback is preserved between attempts.
- [ ] Non-improving loops terminate.
- [ ] A safe fallback or human escalation exists.
- [ ] Tool permissions follow least privilege.
- [ ] Secrets and personal data are excluded from logs.
- [ ] Quality, cost, latency, and iterations are monitored.
- [ ] Unit, integration, failure, and load tests pass.
- [ ] Operators can disable or roll back the loop.
