"""Bounded retry policy for tool calls, with deterministic demo output."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar


T = TypeVar("T")


class TransientToolError(RuntimeError):
    """A temporary failure such as a timeout or rate limit."""


class ValidationToolError(ValueError):
    """A permanent failure caused by invalid input."""


def call_with_retry(
    operation: Callable[[], T],
    *,
    max_attempts: int = 3,
    base_delay: float = 0.5,
    jitter: Callable[[float], float] = lambda delay: delay,
    on_retry: Callable[[float, Exception], None] | None = None,
) -> T:
    """Retry transient failures and immediately surface permanent failures.

    Only retry idempotent operations, or mutations protected by an idempotency
    key. This example reports delays through ``on_retry`` instead of sleeping.
    """
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except ValidationToolError:
            raise
        except TransientToolError as error:
            if attempt == max_attempts:
                raise
            delay = jitter(base_delay * (2 ** (attempt - 1)))
            if on_retry is not None:
                on_retry(delay, error)

    raise RuntimeError("unreachable")


def main() -> None:
    attempts = 0

    def flaky_weather_lookup() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise TransientToolError("weather API timed out")
        return "Weather lookup succeeded"

    result = call_with_retry(
        flaky_weather_lookup,
        on_retry=lambda delay, error: print(f"Retrying in {delay:.1f}s: {error}"),
    )
    print(result)
    print(f"Attempts: {attempts}")


if __name__ == "__main__":
    main()
