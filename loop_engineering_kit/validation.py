"""Generic validation loop independent of any LLM provider."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ValidationLoopConfig:
    max_iterations: int = 3
    quality_threshold: float = 0.85

class ValidationLoop:
    def __init__(self, config: ValidationLoopConfig | None = None): self.config = config or ValidationLoopConfig()
    def run(self, value: Any, validate: Callable[[Any], tuple[float, str]],
            correct: Callable[[Any, str], Any]) -> dict:
        best, best_score = value, -1.0
        for iteration in range(1, self.config.max_iterations + 1):
            score, feedback = validate(value)
            if score > best_score: best, best_score = value, score
            if score >= self.config.quality_threshold:
                return {"value": value, "score": score, "iterations": iteration, "success": True}
            value = correct(value, feedback)
        return {"value": best, "score": best_score, "iterations": self.config.max_iterations, "success": False}
