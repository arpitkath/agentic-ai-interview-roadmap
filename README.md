# Agentic AI Interview Roadmap

A practical, framework-neutral roadmap for preparing for agentic AI engineering interviews.

AI engineering interviews increasingly test more than model APIs and prompt writing. You may be asked to design an agent loop, define safe tool boundaries, debug weak retrieval, decide what belongs in memory, build an evaluation strategy, defend against prompt injection, or explain how you would investigate a failed production run.

This repository organizes those topics into a study path with:

- A staged [interview roadmap](roadmap.md)
- Seven focused [topic guides](#topic-guides)
- [30 answered interview questions](#interview-question-banks)
- Three [dependency-free Python examples](#runnable-python-examples)
- Checklists for [system design](#production-readiness-checklist) and interview answers

The goal is not to memorize one framework. It is to understand the engineering decisions that remain relevant across models, libraries, and agent platforms.

## Table of contents

- [What agentic AI interviews evaluate](#what-agentic-ai-interviews-evaluate)
- [Who this repository is for](#who-this-repository-is-for)
- [How to use this repository](#how-to-use-this-repository)
- [Repository map](#repository-map)
- [Topic guides](#topic-guides)
- [Interview question banks](#interview-question-banks)
- [Runnable Python examples](#runnable-python-examples)
- [Four-week study plan](#four-week-study-plan)
- [How to answer system-design questions](#how-to-answer-agentic-ai-system-design-questions)
- [Production-readiness checklist](#production-readiness-checklist)
- [Common interview mistakes](#common-interview-mistakes)
- [FAQ](#faq)
- [Hands-on practice](#hands-on-practice)
- [Contributing](#contributing)

## What agentic AI interviews evaluate

An agentic system gives a model some ability to decide what happens next. That flexibility creates engineering problems that do not appear in a single prompt-and-response call.

Interviewers often want to know whether you can reason about:

1. **Control flow:** Who owns the loop? How does the system stop? What happens when the model returns an invalid action?
2. **External actions:** How are tools described, validated, authorized, retried, and audited?
3. **State:** What information stays in the current context, what becomes durable memory, and what must expire?
4. **Retrieval:** How does the system find relevant evidence, reject weak evidence, and keep citations grounded?
5. **Measurement:** How do you evaluate outputs, trajectories, safety behavior, latency, and cost?
6. **Safety:** Which controls belong in deterministic runtime code instead of prompts?
7. **Operations:** How do you trace, replay, debug, and improve a failed run?

A strong answer does not assume the model behaves perfectly. It makes boundaries, validation, failure handling, and measurement explicit.

## Who this repository is for

This resource is useful if you are:

- Preparing for AI engineer, LLM engineer, applied AI, or agentic AI interviews
- Moving from backend, infrastructure, platform, data, or full-stack engineering into AI
- Building systems that combine models with APIs, databases, search, files, or code execution
- Comfortable with basic LLM concepts but unsure what production interview questions look like
- Looking for a structured alternative to collecting disconnected articles and framework tutorials

You do not need prior experience with LangChain, LlamaIndex, CrewAI, or another agent framework. The material focuses on the underlying system behavior.

## How to use this repository

Choose the path that matches your current preparation.

### If you are new to agentic systems

1. Read the [roadmap](roadmap.md).
2. Start with [agent loops](topics/agent-loops.md) and [tool calling](topics/tool-calling.md).
3. Run [`simple-agent-loop.py`](examples/simple-agent-loop.py).
4. Answer the [beginner questions](questions/beginner.md) without notes.
5. Move to memory, RAG, evals, guardrails, and observability.

### If you already build LLM applications

1. Review the [production-readiness checklist](#production-readiness-checklist).
2. Use the [intermediate](questions/intermediate.md) and [advanced](questions/advanced.md) question banks as a diagnostic.
3. Study the topic guides for areas where your answers are vague.
4. Practice one complete system-design problem from requirements through rollout.

### If your interview is soon

Focus on these high-signal areas:

- Agent termination and failure recovery
- Tool validation, permissions, retries, and idempotency
- RAG retrieval metrics and hallucination failure modes
- Final-answer versus trajectory evaluation
- Prompt injection and human approval boundaries
- Tracing, cost, latency, and incident debugging

Do not try to memorize every framework API. Practice explaining tradeoffs with a simple architecture first.

## Repository map

```text
agentic-ai-interview-roadmap/
├── README.md                         # Overview and practical study guide
├── roadmap.md                        # Four learning levels and study sequence
├── topics/
│   ├── agent-loops.md                # Control flow, state, and termination
│   ├── tool-calling.md               # Schemas, validation, retries, permissions
│   ├── memory.md                     # Context, durable memory, TTL, pollution
│   ├── rag.md                        # Retrieval, reranking, grounding, citations
│   ├── evals.md                      # Datasets, metrics, judges, regression tests
│   ├── guardrails.md                 # Least privilege, injection, approvals
│   └── observability.md              # Logs, traces, replay, cost, latency
├── questions/
│   ├── beginner.md                   # Definitions and basic control flow
│   ├── intermediate.md               # Implementation and failure handling
│   └── advanced.md                   # Production architecture and tradeoffs
└── examples/
    ├── simple-agent-loop.py          # Bounded loop and tool dispatch
    ├── tool-retry-example.py         # Error classification and backoff
    ├── rag-eval-example.py           # Retrieval and grounding evaluation
    └── test_examples.py              # Behavior tests for all examples
```

## Topic guides

### 1. Agent loops

An agent loop repeatedly asks a model what to do next, executes an allowed action in the application runtime, appends the observation, and continues until a stop condition is reached.

Study:

- ReAct and other reason-act-observe patterns
- Explicit state and scratchpads
- Final-answer, step, time, token, and cost limits
- Repeated-action detection
- Invalid action recovery
- Cancellation and human fallback
- Deterministic workflow versus open-ended agent tradeoffs

Representative interview questions:

- How do you prevent an agent from running forever?
- What should happen when the model requests an unknown tool?
- When is a deterministic state machine better than an agent loop?
- How would you debug an agent that repeatedly takes the same action?

Read the [agent loops guide](topics/agent-loops.md).

### 2. Tool calling

A tool call is a structured request. The model proposes it, but the runtime remains responsible for validation, authorization, execution, and error handling.

Study:

- Tool names, descriptions, and schemas
- Argument and business-rule validation
- Allowlisted dispatch
- Timeout and retry policy
- Retryable versus permanent failures
- Idempotency for side effects
- Permission checks and approval gates
- Normalized tool results

Representative interview questions:

- What makes a tool schema easy for a model to use correctly?
- When should a failed tool call be retried?
- How do you prevent duplicate payments or messages during retries?
- How would you safely expose a `send_email` tool?

Read the [tool calling guide](topics/tool-calling.md).

### 3. Memory and context

The context window is only the input to one model call. A memory system decides what to retain, retrieve, summarize, update, and delete across calls or sessions.

Study:

- Working memory versus long-term memory
- Context-window budgeting
- Sliding windows and summarization
- Semantic memory retrieval
- Memory write policies
- Provenance, timestamps, confidence, and scope
- TTL, invalidation, corrections, and deletion
- Memory pollution and cross-user leakage

Representative interview questions:

- What is the difference between context and memory?
- Which facts should be stored as durable memory?
- How do you resolve contradictory memories?
- How do you prevent temporary observations from becoming permanent facts?

Read the [memory guide](topics/memory.md).

### 4. Retrieval-augmented generation

RAG retrieves external evidence and places it into model context before generation. It can improve freshness and attribution, but it does not guarantee a correct or grounded answer.

Study:

- Chunking and metadata
- Keyword, vector, and hybrid retrieval
- Query rewriting
- Candidate retrieval versus reranking
- Relevance thresholds and abstention
- Grounded generation and citation validation
- Document permissions and freshness
- Retrieval evaluation

Representative interview questions:

- Why can RAG still hallucinate?
- How do you debug irrelevant retrieved chunks?
- When should you add a reranker?
- What metrics would you use to compare two retrieval pipelines?

Read the [RAG guide](topics/rag.md).

### 5. Evals

Evals measure whether the system completes the intended task, follows constraints, and remains reliable when models, prompts, tools, or data change.

Study:

- Golden datasets and held-out cases
- Deterministic checks
- Rubric scoring
- LLM-as-judge and calibration
- Final-answer and trajectory evaluation
- Safety and adversarial cases
- Slice analysis
- Regression suites and release gates

Representative interview questions:

- How would you evaluate an agentic workflow?
- When is exact match useful, and when is it misleading?
- What are the risks of using the same model as agent and judge?
- How do production incidents become regression tests?

Read the [evals guide](topics/evals.md).

### 6. Guardrails

Guardrails are deterministic controls around model inputs, outputs, data, and actions. Important authorization and safety decisions must not depend on the model voluntarily following a prompt.

Study:

- Least-privilege access
- User and tenant authorization
- Tool risk classification
- Human approval for consequential actions
- Prompt injection through retrieved content
- Sensitive-data handling
- Safe defaults and fail-closed behavior
- Audit trails and safety evals

Representative interview questions:

- How do you stop an agent from sending an email without approval?
- How do you handle prompt injection inside retrieved documents?
- Which controls belong in prompts, and which belong in runtime code?
- How should an approval be bound to the exact action being executed?

Read the [guardrails guide](topics/guardrails.md).

### 7. Observability

Observability creates an explainable record of each run across model calls, retrieval, tools, policies, retries, and final output.

Study:

- Run IDs and step IDs
- Structured model and tool events
- Prompt, model, tool, and index versioning
- Token, cost, latency, and reliability metrics
- Privacy-aware logging and redaction
- Trace replay
- Alerts for loops, failures, and policy events
- Incident-to-eval feedback loops

Representative interview questions:

- What should you record for every tool call?
- How would you debug a wrong action taken by an agent?
- Which metrics belong on an agent operations dashboard?
- How can you replay a production failure safely?

Read the [observability guide](topics/observability.md).

## Interview question banks

The repository contains 30 answered questions across three levels.

| Level | Focus | Use it when |
|---|---|---|
| [Beginner](questions/beginner.md) | Definitions, boundaries, and basic control flow | You are building foundational vocabulary |
| [Intermediate](questions/intermediate.md) | Validation, retries, memory, retrieval, safety, and tracing | You need to explain implementation decisions |
| [Advanced](questions/advanced.md) | Architecture, rollout, incident response, and cross-system tradeoffs | You are preparing for senior or system-design interviews |

Each question contains:

- A direct answer
- The underlying signal the interviewer is testing
- A follow-up question when a second layer of reasoning is useful

For practice, answer aloud before reading the provided response. Then improve your answer by adding one failure mode, one tradeoff, and one measurable success criterion.

## Runnable Python examples

The examples require Python 3.10 or newer and use only the standard library.

```bash
python3 examples/simple-agent-loop.py
python3 examples/tool-retry-example.py
python3 examples/rag-eval-example.py
python3 -m unittest discover -s examples -p 'test_*.py' -v
```

### Simple agent loop

[`simple-agent-loop.py`](examples/simple-agent-loop.py) demonstrates:

- Explicit agent state
- Deterministic tool selection as a stand-in for a model
- Allowlisted tool dispatch
- Observation recording
- Final-answer termination
- Maximum-step termination
- Unknown-tool handling

The important lesson is the control flow. A production system would replace the deterministic decision function with a model call while keeping runtime enforcement outside the model.

### Tool retry policy

[`tool-retry-example.py`](examples/tool-retry-example.py) demonstrates:

- Transient versus permanent error classes
- Bounded attempts
- Exponential backoff
- Deterministic jitter injection
- Immediate failure for invalid input
- A callback for retry reporting

The example intentionally does not sleep. This keeps tests fast and separates retry policy from scheduling.

### RAG evaluation

[`rag-eval-example.py`](examples/rag-eval-example.py) demonstrates:

- A small in-memory document collection
- Dependency-free lexical retrieval
- Recall at K
- Source-level grounding checks
- A compact evaluation dataset
- Aggregate metric reporting

Lexical overlap is not presented as production retrieval. It makes the evaluation structure visible without requiring an embedding service or vector database.

## Four-week study plan

### Week 1: Agent loops and tools

Learn:

- Model-runtime boundaries
- ReAct control flow
- Stop conditions
- Tool schemas and validation
- Retry and idempotency policy

Build:

- A loop with two read-only tools
- A maximum-step limit
- Structured errors for invalid actions
- A trace of every step

Interview outcome:

You should be able to draw the loop and explain who validates and executes each action.

### Week 2: Memory and RAG

Learn:

- Context budgeting
- Memory write and retrieval policy
- Chunking and metadata
- Keyword, vector, and hybrid retrieval
- Reranking and abstention

Build:

- A small document retrieval pipeline
- A labeled query set
- Recall-at-K measurement
- A memory policy with provenance and expiry

Interview outcome:

You should be able to diagnose whether a bad answer came from retrieval, context construction, or generation.

### Week 3: Evals, guardrails, and observability

Learn:

- Final-answer and trajectory evals
- Deterministic checks and model judges
- Prompt injection defenses
- Approval boundaries
- Structured traces and operational metrics

Build:

- A regression suite with normal, edge, and adversarial cases
- A human-approval flow for one risky action
- A trace that records model, tool, policy, cost, and timing data

Interview outcome:

You should be able to define how the system is measured, constrained, and debugged.

### Week 4: System design and mock interviews

Design two complete systems, such as:

- A customer-support resolution agent
- A research assistant with citations
- A coding agent with repository tools
- A financial assistant that drafts but cannot execute transactions

For each system, cover:

- User goal and success criteria
- Components and trust boundaries
- State and memory lifecycle
- Tools and permissions
- Failure handling
- Evals and release gates
- Observability
- Cost and latency
- Rollout and rollback

Interview outcome:

You should be able to start with a simple baseline, identify its weaknesses, and add complexity only when a requirement justifies it.

For a more detailed progression, follow the full [roadmap](roadmap.md).

## How to answer agentic AI system-design questions

Use this sequence to keep your answer structured.

### 1. Clarify the task

Define:

- Who the user is
- What outcome they need
- What data and tools are available
- Which actions are consequential
- What correctness, latency, and cost mean for this workflow

### 2. Start with the simplest architecture

Do not begin with multiple agents, long-term memory, and a complex vector stack. Start with a deterministic workflow or one bounded agent and explain why additional autonomy is needed.

### 3. Draw the trust boundaries

Separate:

- User input
- Trusted system instructions
- Untrusted retrieved content
- Model decisions
- Runtime validation
- Tool execution
- Durable storage
- Human approval

### 4. Explain the control loop

Describe:

- State passed to the model
- Available actions
- Action validation
- Tool observations
- Stop conditions
- Retry and fallback behavior

### 5. Cover failure modes

Discuss concrete failures:

- Invalid or hallucinated tools
- Repeated actions
- Partial or stale retrieval
- Prompt injection
- Tool timeout
- Duplicate side effects
- Permission denial
- Context overflow
- Unsupported final claims

### 6. Define evaluation

Include:

- Offline dataset
- Task-success metrics
- Tool and trajectory checks
- Safety cases
- Latency and cost budgets
- Human review
- Release criteria

### 7. Explain operations and rollout

Specify:

- Trace fields
- Dashboards and alerts
- Replay strategy
- Shadow testing or canaries
- Versioning
- Rollback
- How incidents become new eval cases

This sequence demonstrates that you can build, measure, and operate the system—not just draw boxes around an LLM.

## Production-readiness checklist

Use this checklist when reviewing an agent design.

### Control flow

- [ ] The runtime owns the loop.
- [ ] Model outputs are parsed and validated.
- [ ] Step, time, token, and cost limits exist.
- [ ] Repeated actions are detected.
- [ ] Cancellation and fallback behavior are defined.

### Tools and actions

- [ ] Only allowlisted tools can execute.
- [ ] Arguments pass schema and business validation.
- [ ] Authorization is checked immediately before execution.
- [ ] Timeouts and retryable failures are classified.
- [ ] Mutations use idempotency protection.
- [ ] Consequential actions require bound approval.

### Context and memory

- [ ] Context is selected within a token budget.
- [ ] Durable memory has a write policy.
- [ ] Stored facts include provenance and timestamps.
- [ ] Stale or contradictory memory can be corrected.
- [ ] User and tenant boundaries are enforced.

### RAG

- [ ] Retrieval is evaluated separately from generation.
- [ ] Document permissions apply during retrieval.
- [ ] Relevance thresholds and abstention are defined.
- [ ] Citations are checked against retrieved evidence.
- [ ] Index freshness and ingestion failures are monitored.

### Evals and safety

- [ ] The eval set represents real usage and known failures.
- [ ] Final answers and trajectories are both tested.
- [ ] Prompt injection and permission cases are included.
- [ ] Model judges are calibrated against human labels.
- [ ] Critical regressions block release.

### Observability

- [ ] Runs and steps have correlation IDs.
- [ ] Model, prompt, tool, and data versions are recorded.
- [ ] Tool status, retries, latency, tokens, and cost are measurable.
- [ ] Secrets and sensitive data are redacted.
- [ ] Failed runs can be replayed safely.

## Common interview mistakes

### Treating the model as the runtime

Saying “the model calls the API” hides the actual architecture. The model requests an action; application code validates and executes it.

### Using prompts as the only guardrail

Prompts cannot enforce authorization, transaction limits, tenant boundaries, or approval requirements. Those controls belong in deterministic code.

### Retrying every failure

Invalid input and denied permissions do not become valid through repetition. Retry only errors that are temporary and safe to repeat.

### Saying RAG prevents hallucination

RAG supplies evidence. It does not guarantee that evidence is relevant, complete, fresh, or correctly used.

### Calling the full transcript “memory”

A growing transcript is context accumulation. A memory system needs retention, retrieval, update, expiry, and deletion policies.

### Evaluating only the final answer

An agent may produce a correct answer after taking an unsafe or expensive path. Evaluate tool calls, arguments, policy decisions, retries, and step count.

### Adding multi-agent architecture too early

Multiple agents add coordination, shared-state, evaluation, latency, and debugging complexity. Use them only when role separation creates measurable value.

### Ignoring operations

Production answers should explain how failures are traced, replayed, alerted on, and converted into regression tests.

## FAQ

### Do I need to know a specific agent framework?

No. Framework familiarity can help with implementation, but interviews usually reveal whether you understand control flow, validation, retrieval, evaluation, and safety beneath the abstraction.

### Is data structures and algorithms preparation still useful?

Yes. Many companies still evaluate conventional coding and system design. This repository covers the additional agentic AI layer rather than replacing general engineering preparation.

### Should I memorize model-provider APIs?

Know the common concepts—messages, structured outputs, tool schemas, streaming, token limits, and retries—but prioritize transferable design reasoning over one provider's current method names.

### How much Python do I need?

You should be comfortable writing clear functions, data structures, error handling, tests, and simple asynchronous or API-oriented code. The examples here intentionally use basic Python.

### What is the best project to discuss in an interview?

Use a project where you can explain a concrete user goal, architecture, failure you observed, metric you improved, and tradeoff you made. A small measured system is stronger than a large demo you cannot evaluate.

### How do I know I am ready?

You are ready when you can:

- Explain every topic without framework jargon
- Implement a bounded tool-using loop
- Diagnose a RAG failure using retrieval metrics
- Define offline and online evals
- Draw safety and permission boundaries
- Walk through a failed run using traces
- Design a complete system and defend its tradeoffs

## Hands-on practice

This repository provides the roadmap, explanations, questions, and small examples. For LeetCode-style coding problems around agent loops, tool calling, memory, RAG, evals, guardrails, and observability, continue with [AgenticPrep](https://www.agenticprep.io/).

## Contributing

Corrections, additional questions, real-world failure cases, diagrams, and small examples are welcome.

Before contributing:

- Read [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep explanations framework-neutral where possible.
- Include failure modes and tradeoffs.
- Add tests for executable examples.
- Do not copy material from paid courses, books, blogs, or interview platforms.

## License

Licensed under the [MIT License](LICENSE).
