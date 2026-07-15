# Case Study: Customer Support Automation

> The figures below are an illustrative scenario, not audited benchmark claims.

## Challenge

A support team handles 10,000 monthly tickets. A one-shot chatbot automates 40%, while agents review uncertain responses and repeatedly correct the same failure modes.

## Three-loop architecture

1. **Generation:** retrieve approved policy context and generate with retry protection.
2. **Validation:** check grounding, policy, tone, and completeness; regenerate with feedback up to three times.
3. **Human review:** auto-send calibrated high-confidence answers, review medium-confidence drafts, and escalate low-confidence or high-risk cases.

## Controls

- three validation attempts
- per-ticket timeout and cost limit
- mandatory review for refunds, cancellations, and policy exceptions
- versioned policy sources and citation logging
- redaction of sensitive customer data in telemetry

## Illustrative outcome

A pilot might target 78% automation, lower handling cost, and faster resolution while maintaining satisfaction. Real outcomes require an A/B test and manual quality audit.

## Lessons

Confidence must be calibrated rather than guessed. Medium-confidence drafts can save substantial agent time. Agent edits are useful feedback but require privacy controls. Maximum iterations prevent runaway costs and make failure predictable.
