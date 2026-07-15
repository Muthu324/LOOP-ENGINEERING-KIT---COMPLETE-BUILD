# Contributing

1. Fork the repository and create a focused branch.
2. Install development dependencies with `pip install -e ".[dev]"`.
3. Add tests for behavioral changes.
4. Run `pytest` and `ruff check .`.
5. Open a pull request explaining the problem, approach, and trade-offs.

New patterns should include explicit stopping conditions, error behavior, a runnable example, tests, and notes about cost and observability. Never commit credentials or customer data.
