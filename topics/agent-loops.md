# Agent Loops

An agent loop lets a model repeatedly choose an action, observe the result, update its state, and decide what to do next. The application—not the model—owns this control flow.

## What interviewers may test

- Whether you can separate model decisions from runtime execution
- How you represent state and observations
- Which stop conditions prevent runaway execution
- How the loop recovers from malformed actions or failed tools
- When a deterministic workflow is safer than an open-ended agent

## Core concepts

- **ReAct:** alternate reasoning, action, and observation.
- **State:** retain the goal, messages, tool results, budgets, and approvals needed for the next decision.
- **Termination:** stop on a valid final answer, maximum steps, time or cost budget, cancellation, or unrecoverable failure.
- **Repeated-action detection:** catch identical tool calls that indicate the agent is stuck.
- **Fallback:** return a bounded failure, ask a clarifying question, or escalate to a human.

## Common interview questions

### How do you prevent an agent from running forever?

Use layered termination: a model-selected final answer plus hard runtime limits for steps, wall-clock time, tokens, and cost. Detect repeated actions and support external cancellation. Return a clear stopped state instead of silently truncating the run.

### What should happen after a malformed model action?

Validate the action against the allowed response schema. Return a structured observation that explains the validation error and allow a small correction budget. Stop or fall back after repeated invalid responses.

### When should you avoid an agent loop?

Prefer a deterministic workflow when the steps are known, compliance requires predictable execution, or model flexibility adds little value. Agents are useful when the next action genuinely depends on intermediate observations.

## Common failure modes

- No hard stop condition
- Tool result is not appended to state
- Same action repeats without progress
- Unknown tools execute through unsafe dynamic dispatch
- Errors are converted into misleading success messages
- Context grows without token budgeting
- A user cancellation request is ignored

## Design checklist

- [ ] Define the state and its owner.
- [ ] Validate every model action.
- [ ] Allowlist available tools.
- [ ] Set step, time, token, and cost budgets.
- [ ] Detect repeated actions.
- [ ] Record a trace for each step.
- [ ] Specify cancellation and human-escalation behavior.
- [ ] Evaluate both final answers and trajectories.

## Related resources

- [Simple agent loop example](../examples/simple-agent-loop.py)
- [Beginner questions](../questions/beginner.md)
- [Tool calling](tool-calling.md)
- [Observability](observability.md)

For deeper learning and coding practice, see [Agent loops on AgenticPrep](https://www.agenticprep.io/curriculum/agent-loop).
