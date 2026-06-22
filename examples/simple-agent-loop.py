"""A deterministic agent loop that demonstrates control flow without an SDK."""

from __future__ import annotations

from typing import Callable, NamedTuple


MAX_STEPS = 4


class Step(NamedTuple):
    action: str
    arguments: str
    observation: str


class AgentResult(NamedTuple):
    status: str
    answer: str
    steps: list[Step]


def search_tool(query: str) -> str:
    """Return a deterministic stand-in for an external search result."""
    return f"Search result for: {query}"


TOOLS: dict[str, Callable[[str], str]] = {"search": search_tool}


def decide_next_action(goal: str, steps: list[Step]) -> tuple[str, str]:
    """Stand in for a model choosing a tool or returning a final answer."""
    if steps:
        return "final", f"Answer based on: {steps[-1].observation}"
    if goal.lower().startswith("search for "):
        return "search", goal[len("search for ") :]
    if "unsupported tool" in goal.lower():
        return "unsupported", goal
    return "final", "No tool was needed for this goal."


def run_agent(goal: str, max_steps: int = MAX_STEPS) -> AgentResult:
    """Run until a final answer, unknown tool, or maximum-step boundary."""
    steps: list[Step] = []

    for _ in range(max_steps):
        action, arguments = decide_next_action(goal, steps)
        if action == "final":
            return AgentResult("completed", arguments, steps)

        tool = TOOLS.get(action)
        if tool is None:
            observation = f"Unknown tool: {action}"
            steps.append(Step(action, arguments, observation))
            return AgentResult("stopped", observation, steps)

        observation = tool(arguments)
        steps.append(Step(action, arguments, observation))

    return AgentResult(
        "stopped",
        f"Stopped after reaching the {max_steps}-step limit.",
        steps,
    )


def main() -> None:
    result = run_agent("Search for agentic AI interview questions")
    for index, step in enumerate(result.steps, start=1):
        print(f"Step {index}: {step.action}({step.arguments!r})")
        print(f"Observation: {step.observation}")
    print(f"Status: {result.status}")
    print(result.answer)


if __name__ == "__main__":
    main()
