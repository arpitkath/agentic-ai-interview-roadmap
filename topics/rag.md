# Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) finds external evidence at query time and supplies it to a model. It can improve freshness and attribution, but only when retrieval and grounding are measured.

## What interviewers may test

- Chunking and indexing choices
- Keyword, vector, and hybrid retrieval
- Reranking and relevance thresholds
- Query rewriting and metadata filters
- Citation grounding and abstention
- Retrieval and answer evaluation

## Core concepts

- **Chunking:** split documents into useful retrieval units with metadata.
- **Candidate retrieval:** optimize recall using keyword, vector, or hybrid search.
- **Reranking:** apply a more precise scorer to a smaller candidate set.
- **Grounding:** require claims to be supported by retrieved evidence.
- **Abstention:** say there is insufficient evidence below a quality threshold.
- **Freshness:** version, timestamp, and invalidate indexed content.

## Common interview questions

### Why can RAG still hallucinate?

Retrieval may return irrelevant, conflicting, incomplete, or stale evidence. The model may also ignore the evidence or add unsupported claims. RAG changes the available context; it does not guarantee grounded generation.

### How do you debug irrelevant retrieval?

Inspect the query, filters, chunk boundaries, candidate scores, and reranker output. Measure recall at K on labeled queries before tuning generation prompts. Compare keyword, vector, and hybrid baselines.

### What metrics matter for RAG?

Measure retrieval recall, precision or relevance at K, ranking quality, citation correctness, grounded answer quality, abstention quality, latency, and cost. Segment results by query type and data source.

## Common failure modes

- Chunks split required context across boundaries
- Embedding search misses identifiers or exact phrases
- Too many chunks dilute relevant evidence
- Metadata filters exclude correct documents
- Retrieved text contains prompt injection
- Citations point to sources that do not support the claim
- The index serves deleted or outdated content

## Design checklist

- [ ] Preserve source, section, timestamp, and access metadata.
- [ ] Establish a simple lexical baseline.
- [ ] Evaluate candidate retrieval separately from generation.
- [ ] Add reranking only when metrics justify it.
- [ ] Enforce document-level authorization.
- [ ] Define relevance and abstention thresholds.
- [ ] Validate citations against retrieved sources.
- [ ] Monitor index freshness and ingestion failures.

## Related resources

- [RAG evaluation example](../examples/rag-eval-example.py)
- [Evals](evals.md)
- [Memory](memory.md)
- [Intermediate questions](../questions/intermediate.md)

For deeper learning and coding practice, see [RAG on AgenticPrep](https://www.agenticprep.io/curriculum/rag).
