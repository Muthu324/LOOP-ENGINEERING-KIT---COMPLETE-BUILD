"""Confidence-based human review and escalation."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class HumanVerificationConfig:
    auto_approve_threshold: float = 0.90
    review_threshold: float = 0.70

class HumanVerificationLoop:
    def __init__(self, config: HumanVerificationConfig | None = None):
        self.config = config or HumanVerificationConfig()
        if self.config.review_threshold > self.config.auto_approve_threshold:
            raise ValueError("review_threshold cannot exceed auto_approve_threshold")

    def execute(self, task: Any, processor: Callable[[Any], Any], confidence: Callable[[Any], float],
                request_review: Callable[[Any, Any], Any], escalate: Callable[[Any, Any], Any]) -> dict:
        output = processor(task)
        score = confidence(output)
        if score >= self.config.auto_approve_threshold:
            return {"status": "auto_approved", "output": output, "confidence": score}
        if score >= self.config.review_threshold:
            return {"status": "reviewed", "output": request_review(task, output), "confidence": score}
        return {"status": "escalated", "output": escalate(task, output), "confidence": score}
