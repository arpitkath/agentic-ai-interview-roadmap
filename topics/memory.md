# Memory and Context

Memory is the policy for retaining, retrieving, and expiring information across steps or sessions. A context window is model input; it is not automatically a reliable memory system.

## What interviewers may test

- Short-term context versus durable memory
- Token-budget and context-selection strategy
- Summarization and retrieval tradeoffs
- Memory write policy and user consent
- Staleness, provenance, deletion, and privacy
- How memory errors affect agent behavior

## Core concepts

- **Working memory:** current messages, scratchpad, and task state.
- **Long-term memory:** durable facts stored outside the model context.
- **Summarization:** compress older context while accepting information loss.
- **Retrieval:** select relevant past facts instead of loading everything.
- **Write policy:** decide what is worth storing and with what provenance.
- **TTL and invalidation:** expire or update stale facts.

## Common interview questions

### What is the difference between context and memory?

Context is the information sent to the model for one inference. Memory is the broader system that decides what to store, retrieve, summarize, update, and delete before constructing that context.

### What should an agent store as long-term memory?

Store durable, useful facts with a clear source and expected lifetime, such as an explicitly stated preference. Avoid storing temporary observations, inferred sensitive attributes, or unverified model output.

### How do you prevent memory pollution?

Use a write gate that validates provenance, confidence, scope, consent, and expiry. Separate user-provided facts from model inferences, support corrections, and evaluate retrieval for stale or contradictory memories.

## Common failure modes

- Treating the full conversation transcript as memory
- Persisting temporary or incorrect observations
- Retrieving semantically similar but irrelevant facts
- Summaries remove constraints or attribution
- Old preferences override newer instructions
- Cross-user memory leakage
- No deletion or correction path

## Design checklist

- [ ] Separate session state from durable storage.
- [ ] Define what may be written and by whom.
- [ ] Store source, timestamp, scope, and confidence.
- [ ] Set retention and deletion rules.
- [ ] Retrieve only task-relevant memories.
- [ ] Resolve contradictions predictably.
- [ ] Protect tenant and user boundaries.
- [ ] Evaluate both memory writes and retrievals.

## Related resources

- [RAG](rag.md)
- [Guardrails](guardrails.md)
- [Intermediate questions](../questions/intermediate.md)

For deeper learning and coding practice, see [Memory and context on AgenticPrep](https://www.agenticprep.io/curriculum/memory).
