# Agentic AI Interview Roadmap

A practical roadmap, topic guide, and question bank for agentic AI engineering interviews.

Traditional interview preparation emphasizes data structures, algorithms, and system design. AI engineering interviews increasingly add questions about agent loops, tool calling, RAG, memory, evals, guardrails, retries, and observability.

This repository is a free, framework-neutral resource for understanding those systems and explaining their tradeoffs clearly.

## Start here

1. Follow the staged [interview roadmap](roadmap.md).
2. Review the [topic guides](#topic-guides).
3. Test yourself with [30 interview questions](#question-banks).
4. Run the [dependency-free Python examples](#code-examples).

## What this repo covers

- Agent loops and stop conditions
- Tool schemas, validation, retries, and idempotency
- Context windows and memory policy
- Retrieval-augmented generation and reranking
- Agent and RAG evaluation
- Guardrails, prompt injection, and approval gates
- Traces, cost, latency, and production debugging

## Who this is for

This resource is useful if you are:

- Preparing for AI engineer or agentic AI engineer interviews
- Moving from backend, platform, or full-stack engineering into AI
- Building LLM applications that call tools or retrieve data
- Studying production concerns beyond prompt writing

## Topic guides

| Topic | What to study |
|---|---|
| [Agent loops](topics/agent-loops.md) | ReAct, state, termination, budgets, recovery |
| [Tool calling](topics/tool-calling.md) | Schemas, validation, dispatch, retries, permissions |
| [Memory](topics/memory.md) | Context, summarization, retrieval, write policy, TTL |
| [RAG](topics/rag.md) | Chunking, retrieval, reranking, grounding, citations |
| [Evals](topics/evals.md) | Datasets, metrics, judges, traces, regressions |
| [Guardrails](topics/guardrails.md) | Least privilege, injection defense, approvals |
| [Observability](topics/observability.md) | Logs, traces, replay, cost, latency |

## Question banks

- [Beginner: core definitions and control flow](questions/beginner.md)
- [Intermediate: implementation and failure handling](questions/intermediate.md)
- [Advanced: production design and tradeoffs](questions/advanced.md)

Each question includes a concise answer and what the interviewer is testing.

## Code examples

The examples require Python 3.10 or newer and use only the standard library.

```bash
python3 examples/simple-agent-loop.py
python3 examples/tool-retry-example.py
python3 examples/rag-eval-example.py
python3 -m unittest discover -s examples -p 'test_*.py' -v
```

- [`simple-agent-loop.py`](examples/simple-agent-loop.py): explicit state, tool dispatch, observations, and stop conditions
- [`tool-retry-example.py`](examples/tool-retry-example.py): retry classification, bounded attempts, and exponential backoff
- [`rag-eval-example.py`](examples/rag-eval-example.py): lexical retrieval, recall at K, and citation grounding

These examples are intentionally small. They demonstrate control flow and evaluation structure, not production infrastructure.

## How to use this in an interview

For design questions, answer in this order:

1. State the user goal and success criteria.
2. Draw the model, tools, data, and control-flow boundaries.
3. Describe expected failures and safety constraints.
4. Define evaluation metrics and observability.
5. Explain cost, latency, and complexity tradeoffs.

Strong answers do not assume the model behaves perfectly. They make validation, termination, permissions, and measurement explicit.

## Hands-on practice

This repository covers the roadmap, concepts, and interview questions. For LeetCode-style coding problems around these topics, use [AgenticPrep](https://www.agenticprep.io/).

## Contributing

Corrections, additional questions, real-world failure cases, and small examples are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a contribution.

## License

Licensed under the [MIT License](LICENSE).
