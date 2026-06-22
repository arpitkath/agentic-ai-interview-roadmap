"""Behavior tests for the dependency-free roadmap examples."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


EXAMPLES_DIR = Path(__file__).parent


def load_module(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, EXAMPLES_DIR / filename)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AgentLoopTests(unittest.TestCase):
    def test_search_goal_uses_tool_and_returns_observation(self) -> None:
        module = load_module("simple-agent-loop.py", "simple_agent_loop")

        result = module.run_agent("Search for agent eval patterns")

        self.assertEqual(result.status, "completed")
        self.assertIn("Search result for: agent eval patterns", result.answer)
        self.assertEqual(result.steps[0].action, "search")

    def test_unknown_tool_is_recorded_without_execution(self) -> None:
        module = load_module("simple-agent-loop.py", "simple_agent_loop_unknown")

        result = module.run_agent("Use an unsupported tool")

        self.assertEqual(result.status, "stopped")
        self.assertIn("Unknown tool", result.steps[0].observation)


class RetryTests(unittest.TestCase):
    def test_transient_failures_retry_until_success(self) -> None:
        module = load_module("tool-retry-example.py", "tool_retry")
        attempts = 0
        delays: list[float] = []

        def flaky_operation() -> str:
            nonlocal attempts
            attempts += 1
            if attempts < 3:
                raise module.TransientToolError("temporary timeout")
            return "ok"

        result = module.call_with_retry(
            flaky_operation,
            max_attempts=3,
            on_retry=lambda delay, _error: delays.append(delay),
        )

        self.assertEqual(result, "ok")
        self.assertEqual(attempts, 3)
        self.assertEqual(delays, [0.5, 1.0])

    def test_validation_failure_is_not_retried(self) -> None:
        module = load_module("tool-retry-example.py", "tool_retry_validation")
        attempts = 0

        def invalid_operation() -> str:
            nonlocal attempts
            attempts += 1
            raise module.ValidationToolError("invalid city")

        with self.assertRaises(module.ValidationToolError):
            module.call_with_retry(invalid_operation, max_attempts=3)

        self.assertEqual(attempts, 1)

    def test_retry_delay_accepts_deterministic_jitter(self) -> None:
        module = load_module("tool-retry-example.py", "tool_retry_jitter")
        delays: list[float] = []

        def always_transient() -> str:
            raise module.TransientToolError("rate limited")

        with self.assertRaises(module.TransientToolError):
            module.call_with_retry(
                always_transient,
                max_attempts=2,
                jitter=lambda delay: delay + 0.25,
                on_retry=lambda delay, _error: delays.append(delay),
            )

        self.assertEqual(delays, [0.75])


class RagEvalTests(unittest.TestCase):
    def test_recall_at_k_rewards_retrieving_expected_source(self) -> None:
        module = load_module("rag-eval-example.py", "rag_eval")
        documents = [
            module.Document("loops", "Agent loops require explicit stop conditions."),
            module.Document("rag", "RAG retrieves relevant context before generation."),
        ]

        retrieved = module.retrieve("How does retrieval work in RAG?", documents, k=1)

        self.assertEqual(module.recall_at_k(retrieved, {"rag"}), 1.0)

    def test_grounding_check_rejects_unknown_source(self) -> None:
        module = load_module("rag-eval-example.py", "rag_eval_grounding")

        self.assertFalse(
            module.is_grounded(
                cited_source_ids={"rag", "missing"},
                retrieved_source_ids={"rag", "loops"},
            )
        )


if __name__ == "__main__":
    unittest.main()
