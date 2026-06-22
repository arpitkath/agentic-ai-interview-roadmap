"""A small retrieval evaluation harness using lexical overlap."""

from __future__ import annotations

import re
from typing import NamedTuple


class Document(NamedTuple):
    source_id: str
    text: str


class EvalCase(NamedTuple):
    query: str
    expected_source_ids: set[str]


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(query: str, documents: list[Document], k: int = 2) -> list[Document]:
    """Rank documents by shared query terms.

    Production retrieval normally uses embeddings, keyword indexes, rerankers,
    or a hybrid. Lexical overlap keeps this example dependency-free.
    """
    query_terms = tokenize(query)
    ranked = sorted(
        documents,
        key=lambda document: (
            len(query_terms & tokenize(document.text)),
            document.source_id,
        ),
        reverse=True,
    )
    return ranked[:k]


def recall_at_k(
    retrieved: list[Document],
    expected_source_ids: set[str],
) -> float:
    if not expected_source_ids:
        return 1.0
    retrieved_ids = {document.source_id for document in retrieved}
    return len(retrieved_ids & expected_source_ids) / len(expected_source_ids)


def is_grounded(
    *,
    cited_source_ids: set[str],
    retrieved_source_ids: set[str],
) -> bool:
    """A citation is grounded only if every cited source was retrieved."""
    return cited_source_ids <= retrieved_source_ids


def evaluate(
    cases: list[EvalCase],
    documents: list[Document],
    k: int = 2,
) -> float:
    scores = [
        recall_at_k(retrieve(case.query, documents, k), case.expected_source_ids)
        for case in cases
    ]
    return sum(scores) / len(scores) if scores else 0.0


def main() -> None:
    documents = [
        Document("loops", "Agent loops need stop conditions and step budgets."),
        Document("tools", "Tool calls need schemas, validation, and retry policy."),
        Document("rag", "RAG retrieves and reranks evidence before generation."),
    ]
    cases = [
        EvalCase("How do I stop an agent loop?", {"loops"}),
        EvalCase("How should tool arguments be checked?", {"tools"}),
        EvalCase("What happens before RAG generation?", {"rag"}),
    ]

    for case in cases:
        results = retrieve(case.query, documents, k=2)
        ids = [document.source_id for document in results]
        score = recall_at_k(results, case.expected_source_ids)
        print(f"{case.query} -> {ids} (recall@2={score:.1f})")

    print(f"Mean recall@2: {evaluate(cases, documents, k=2):.2f}")


if __name__ == "__main__":
    main()
