"""Simple cache and complexity-based model routing pattern."""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class CostConfig:
    complexity_threshold: float = 0.5
    max_cache_entries: int = 1000

class CostOptimizedLoop:
    def __init__(self, cheap_model: Callable[[str], Any], capable_model: Callable[[str], Any],
                 estimate_complexity: Callable[[str], float], config: CostConfig | None = None):
        self.cheap_model, self.capable_model = cheap_model, capable_model
        self.estimate_complexity, self.config = estimate_complexity, config or CostConfig()
        self.cache: dict[str, Any] = {}
    def process(self, prompt: str) -> Any:
        if prompt in self.cache: return self.cache[prompt]
        model = self.capable_model if self.estimate_complexity(prompt) >= self.config.complexity_threshold else self.cheap_model
        result = model(prompt)
        if len(self.cache) >= self.config.max_cache_entries: self.cache.pop(next(iter(self.cache)))
        self.cache[prompt] = result
        return result
