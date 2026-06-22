# Agentic AI Interview Roadmap

Use this roadmap to move from basic agent control flow to production system design. Advance when you can explain a concept, implement a small version, and identify its failure modes.

## Level 1: Foundations

### Understand

- The boundary between an LLM and the application runtime
- The Thought → Action → Observation loop
- Tool calls as structured requests, not direct model execution
- Final-answer and maximum-step stop conditions
- Context-window limits
- Basic retrieve-then-generate RAG

### Practice

- Explain a ReAct loop without naming a framework.
- Run [`simple-agent-loop.py`](examples/simple-agent-loop.py).
- Add a second read-only tool.
- Explain why retrieved context can reduce but not eliminate hallucination.

### Ready to advance when

You can draw a minimal agent loop, identify who executes tools, and name at least three ways the loop can terminate.

Read: [Agent loops](topics/agent-loops.md), [Tool calling](topics/tool-calling.md), and [RAG](topics/rag.md).

## Level 2: Practical agent design

### Understand

- Clear tool names, descriptions, and JSON schemas
- Argument validation before execution
- Retryable versus permanent failures
- Idempotency for mutating operations
- Short-term context versus durable memory
- Chunking, hybrid retrieval, reranking, and relevance thresholds
- When an agent should ask for clarification

### Practice

- Run [`tool-retry-example.py`](examples/tool-retry-example.py).
- Design a `send_email` tool with a preview and idempotency key.
- Write a memory policy that separates session state from durable facts.
- Debug a RAG pipeline that retrieves plausible but irrelevant chunks.

### Ready to advance when

You can describe validation, retry, and fallback behavior for every external call and defend what your system stores as memory.

Read: [Tool calling](topics/tool-calling.md), [Memory](topics/memory.md), and [RAG](topics/rag.md).

## Level 3: Production readiness

### Understand

- Golden datasets and regression suites
- Final-answer, retrieval, and trajectory evaluation
- LLM-as-judge limitations and calibration
- Least-privilege tool access
- Prompt injection through retrieved or tool-returned content
- Human approval for consequential actions
- Structured logs, traces, replay, cost, and latency

### Practice

- Run [`rag-eval-example.py`](examples/rag-eval-example.py).
- Define success metrics for a customer-support agent.
- Add an approval boundary around a risky tool.
- Design a trace that explains every model and tool step.
- Create an incident checklist for an agent that took the wrong action.

### Ready to advance when

You can define offline and online measurements, show how unsafe actions are blocked, and explain how an engineer would debug a failed run.

Read: [Evals](topics/evals.md), [Guardrails](topics/guardrails.md), and [Observability](topics/observability.md).

## Level 4: System design and interview synthesis

### Understand

- When deterministic workflows are better than open-ended agents
- Single-agent versus multi-agent tradeoffs
- Synchronous versus asynchronous execution
- Model, retrieval, and tool fallback strategies
- Rollout, shadow testing, canaries, and rollback
- Cost, latency, reliability, and safety budgets

### Practice

Design one complete system, such as:

- A customer-support resolution agent
- A research assistant with cited sources
- A coding agent that can read and modify a repository
- A financial assistant that drafts but cannot execute transactions

For the design, specify:

1. Inputs, outputs, and success criteria
2. Components and trust boundaries
3. State and memory lifecycle
4. Tool permissions and approval points
5. Failure handling and fallbacks
6. Offline evals and online metrics
7. Logs and traces required for debugging
8. Cost and latency constraints

### Ready for interviews when

You can communicate a simple baseline first, add complexity only when justified, and connect every architectural choice to a measurable requirement or failure mode.

Test yourself with the [advanced question bank](questions/advanced.md).

## Suggested four-week sequence

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Agent loops and tool calling | Build and explain a bounded tool-using loop |
| 2 | Memory and RAG | Design context policy and evaluate retrieval |
| 3 | Evals, guardrails, observability | Create a production-readiness checklist |
| 4 | System design and mock interviews | Present two end-to-end architectures |

Adjust the pace to your background. The important part is producing evidence—code, diagrams, eval cases, and design explanations—not merely reading definitions.
