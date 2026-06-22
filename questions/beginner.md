# Beginner Agentic AI Interview Questions

Use these questions to check definitions and basic control flow.

## 1. What is an agent loop?

**Answer:** An agent loop repeatedly asks a model for the next action, executes an allowed action in the application runtime, returns the observation to the model, and stops when a termination condition is met.

**What this tests:** Whether you understand that the runtime owns execution and control flow.

## 2. What is the ReAct pattern?

**Answer:** ReAct alternates reasoning and acting: the model evaluates the current state, selects an action, receives an observation, and repeats until it can answer.

**What this tests:** Familiarity with the basic reasoning-and-tool-use cycle.

## 3. Why do agents need stop conditions?

**Answer:** Without stop conditions, an agent may repeat actions, consume unbounded tokens, increase cost, or perform unnecessary operations. Use final-answer detection plus hard step, time, and cost limits.

**What this tests:** Awareness of bounded execution.

## 4. What is tool calling?

**Answer:** Tool calling is a structured request from a model to use an external function or service. The application validates and executes the request; the model does not execute it directly.

**What this tests:** The model-runtime boundary.

## 5. Why are tool schemas important?

**Answer:** Schemas describe available tools and constrain their arguments. They improve tool selection, enable validation, and create a stable contract between the model and runtime.

**What this tests:** Understanding of structured interfaces.

## 6. What is the difference between context and memory?

**Answer:** Context is the information sent to a model for one call. Memory is the system that decides what information to store, retrieve, summarize, update, and place into future context.

**What this tests:** Whether you avoid treating the context window as durable storage.

## 7. What is RAG?

**Answer:** Retrieval-augmented generation retrieves relevant external evidence at query time and includes it in model context before generation.

**What this tests:** The basic retrieval-then-generation pipeline.

## 8. Can RAG still hallucinate?

**Answer:** Yes. Retrieval can return weak or stale evidence, and the model can ignore or misinterpret good evidence. Grounding, citation checks, thresholds, and evals are still required.

**What this tests:** Whether you understand RAG's limits.

## 9. What is a golden eval dataset?

**Answer:** It is a versioned collection of representative inputs with expected outputs, labels, or scoring rubrics used to compare system versions.

**What this tests:** Basic evaluation vocabulary and regression thinking.

## 10. Why is observability important for agents?

**Answer:** Agent failures span models, retrieval, tools, and policies. Traces and metrics show which step failed, what context was used, how long it took, and what it cost.

**What this tests:** Production debugging awareness.

Next: [Intermediate questions](intermediate.md) or return to the [roadmap](../roadmap.md).
