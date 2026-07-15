"""Generate, validate, and improve until quality or stopping criteria are met."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional

class ValidationResult(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    NEEDS_IMPROVEMENT = "needs_improvement"

@dataclass
class ValidationResponse:
    status: ValidationResult
    score: float
    feedback: str = ""
    errors: list[str] = field(default_factory=list)

@dataclass(frozen=True)
class SelfCorrectionConfig:
    max_iterations: int = 3
    min_quality_score: float = 0.85
    improvement_threshold: float = 0.0
    def __post_init__(self):
        if self.max_iterations < 1: raise ValueError("max_iterations must be at least 1")
        if not 0 <= self.min_quality_score <= 1: raise ValueError("min_quality_score must be in [0, 1]")

class SelfCorrectionLoop:
    def __init__(self, config: SelfCorrectionConfig | None = None):
        self.config = config or SelfCorrectionConfig()
        self.metrics = {"total_runs": 0, "successful_first_try": 0, "required_correction": 0,
                        "total_failures": 0, "iterations": []}

    def run(self, generator: Callable[[str, Optional[str]], str],
            validator: Callable[[str], ValidationResponse], initial_prompt: str,
            context: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        del context
        self.metrics["total_runs"] += 1
        correction_context = None
        previous_score = -1.0
        best_output, best_validation = "", ValidationResponse(ValidationResult.FAIL, 0.0)
        for iteration in range(1, self.config.max_iterations + 1):
            output = generator(initial_prompt, correction_context)
            validation = validator(output)
            if validation.score > best_validation.score:
                best_output, best_validation = output, validation
            if validation.status == ValidationResult.PASS and validation.score >= self.config.min_quality_score:
                self.metrics["successful_first_try" if iteration == 1 else "required_correction"] += 1
                self.metrics["iterations"].append(iteration)
                return {"output": output, "validation": validation, "iterations": iteration, "success": True}
            improvement = validation.score - previous_score
            if iteration > 1 and improvement < self.config.improvement_threshold: break
            correction_context = self._build_context(output, validation, iteration)
            previous_score = validation.score
        self.metrics["total_failures"] += 1
        self.metrics["iterations"].append(iteration)
        return {"output": best_output, "validation": best_validation, "iterations": iteration, "success": False}

    @staticmethod
    def _build_context(output: str, validation: ValidationResponse, iteration: int) -> str:
        errors = "; ".join(validation.errors) or "none"
        return (
            f"Previous attempt {iteration}:\n{output}\n"
            f"Score: {validation.score:.2f}\n"
            f"Feedback: {validation.feedback}\n"
            f"Errors: {errors}\n"
            "Improve the answer using this feedback."
        )

    def get_metrics(self) -> dict[str, Any]:
        successful = self.metrics["successful_first_try"] + self.metrics["required_correction"]
        iterations = self.metrics["iterations"]
        return {**self.metrics, "success_rate": successful / max(self.metrics["total_runs"], 1),
                "average_iterations": sum(iterations) / max(len(iterations), 1)}
