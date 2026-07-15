# What Is Loop Engineering?

Loop Engineering is the practice of building systems that execute work, validate the result, incorporate feedback, and repeat under explicit limits.

```text
Input → Execute → Validate ── pass → Output
                    │
                    └─ fail → Correct → stopping check → Execute
```

## Core components

1. **State** — input, prior attempts, feedback, costs, and timing.
2. **Execution** — an LLM call, tool invocation, deterministic function, or workflow.
3. **Validation** — rules, tests, schemas, confidence estimates, or human review.
4. **Correction** — a revised prompt, alternative tool, fallback model, or escalation.
5. **Stopping conditions** — quality threshold, maximum attempts, timeout, and budget.
6. **Observability** — logs and metrics for decisions, latency, quality, and cost.

## Essential patterns

- **Retry:** recover from transient operational failures.
- **Self-correction:** improve output using validation feedback.
- **Human verification:** route uncertain or high-impact work to people.
- **Reflection:** critique a plan or answer before accepting it.
- **Cost optimization:** cache repeated work and route by complexity.

## Production guidance

Use deterministic checks where possible. Calibrate confidence thresholds on representative data. Keep generator and validator independent when correlated errors are risky. Apply least privilege to tools. Redact sensitive data from telemetry. Always test terminal failure and escalation paths.
