"""Retry execution with capped exponential backoff and jitter."""
from __future__ import annotations
import logging, random, time
from dataclasses import dataclass
from typing import Any, Callable, Optional, Type

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class RetryConfig:
    max_attempts: int = 3
    initial_delay: float = 1.0
    backoff_multiplier: float = 2.0
    max_delay: float = 60.0
    jitter: bool = True

    def __post_init__(self) -> None:
        if self.max_attempts < 1: raise ValueError("max_attempts must be at least 1")
        if self.initial_delay < 0 or self.max_delay < 0: raise ValueError("delays cannot be negative")
        if self.backoff_multiplier < 1: raise ValueError("backoff_multiplier must be >= 1")

class RetryLoop:
    def __init__(self, config: RetryConfig | None = None, *, sleep: Callable[[float], None] = time.sleep):
        self.config = config or RetryConfig()
        self._sleep = sleep
        self.metrics = {"total_runs": 0, "total_attempts": 0, "successful_first_try": 0,
                        "required_retry": 0, "total_failures": 0}

    def calculate_delay(self, attempt: int) -> float:
        delay = min(self.config.initial_delay * self.config.backoff_multiplier ** (attempt - 1),
                    self.config.max_delay)
        return delay * random.uniform(0.5, 1.5) if self.config.jitter else delay

    def execute(self, func: Callable[[], Any], retry_on: tuple[Type[BaseException], ...] = (Exception,),
                on_retry: Optional[Callable[[BaseException, int], None]] = None) -> Any:
        self.metrics["total_runs"] += 1
        for attempt in range(1, self.config.max_attempts + 1):
            self.metrics["total_attempts"] += 1
            try:
                result = func()
                self.metrics["successful_first_try" if attempt == 1 else "required_retry"] += 1
                return result
            except retry_on as exc:
                logger.warning("Attempt %s/%s failed: %s", attempt, self.config.max_attempts, exc)
                if attempt == self.config.max_attempts:
                    self.metrics["total_failures"] += 1
                    raise
                if on_retry: on_retry(exc, attempt)
                self._sleep(self.calculate_delay(attempt))
        raise RuntimeError("unreachable")

    def get_metrics(self) -> dict[str, float | int]:
        successes = self.metrics["successful_first_try"] + self.metrics["required_retry"]
        return {**self.metrics, "success_rate": successes / max(self.metrics["total_runs"], 1)}
