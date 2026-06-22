# Intermediate Agentic AI Interview Questions

Use these questions to practice implementation decisions and failure handling.

## 1. How should an agent handle invalid tool arguments?

**Answer:** Validate arguments before execution and return a structured error identifying correctable fields. Give the agent a small correction budget, but stop repeated invalid calls and never bypass runtime validation.

**What this tests:** Schema enforcement and bounded recovery.

**Follow-up:** Which validation belongs in JSON Schema, and which belongs in business logic?

## 2. When should a tool call be retried?

**Answer:** Retry transient errors such as timeouts or rate limits when the operation is safe to repeat. Do not retry invalid input, permission denial, or permanent business errors without changing the request.

**What this tests:** Error classification and idempotency.

## 3. How do you prevent duplicate side effects during retries?

**Answer:** Use idempotency keys, deduplication records, or transactional uniqueness constraints. Bind the key to the intended operation and return the original result for repeated requests.

**What this tests:** Safe mutation design.

## 4. When should an agent ask the user for clarification?

**Answer:** Ask when required information is missing and guessing would materially change correctness, cost, or safety. Do not ask when a safe default is explicit or the missing value can be retrieved reliably.

**What this tests:** Product judgment and uncertainty handling.

## 5. How would you design a memory write policy?

**Answer:** Store only durable, useful information with source, scope, timestamp, consent, and expiry. Separate user statements from model inference and provide correction and deletion paths.

**What this tests:** Memory quality, privacy, and lifecycle design.

## 6. How do you debug a RAG system returning irrelevant chunks?

**Answer:** Inspect query rewriting, filters, chunk boundaries, candidate scores, and reranker output. Measure retrieval recall and relevance on labeled queries before changing the generation prompt.

**What this tests:** Pipeline decomposition and metric-driven debugging.

## 7. When is hybrid retrieval useful?

**Answer:** Combine lexical and vector retrieval when queries include both exact identifiers and semantic intent. Hybrid search often improves recall across mixed query types, but it should be justified by eval results.

**What this tests:** Retrieval tradeoffs rather than blind use of embeddings.

## 8. How would you evaluate a customer-support agent?

**Answer:** Measure resolution correctness, policy compliance, required tool use, escalation quality, unsupported claims, latency, cost, and customer outcomes. Evaluate both the final response and action trace.

**What this tests:** Multi-dimensional evaluation design.

## 9. How do you protect a tool-using agent from prompt injection?

**Answer:** Treat external content as untrusted data, enforce tool permissions independently of prompts, validate every action, isolate credentials, and require approval for consequential operations.

**What this tests:** Defense in depth and trust boundaries.

## 10. What belongs in an agent trace?

**Answer:** Record run and step IDs, versioned model and prompt, selected action, validated arguments, authorization decision, tool result or error, retries, tokens, cost, and timing—with sensitive data redacted.

**What this tests:** Debuggability and privacy-aware observability.

Next: [Advanced questions](advanced.md) or review the [topic guides](../README.md#topic-guides).
