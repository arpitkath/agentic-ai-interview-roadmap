# Contributing

Thanks for helping improve this roadmap.

## Good contributions

- New interview questions with concise answers
- Corrections or clearer explanations
- Real-world agent failure cases
- Small, dependency-free examples
- Practical diagrams
- Better evaluation or safety checklists

Do not copy content from books, paid courses, blogs, interview platforms, private interview loops, or other copyrighted sources.

## Adding a question

Include:

1. The question
2. A concise answer
3. **What this tests**
4. An optional follow-up when it adds a meaningful second layer

Place the question at the lowest difficulty that matches the reasoning required:

- Beginner: definitions and basic control flow
- Intermediate: implementation and failure handling
- Advanced: architecture, safety, operations, and tradeoffs

## Adding an example

Examples should:

- Run on Python 3.10 or newer
- Use the standard library unless a dependency is essential to the lesson
- Be deterministic and safe to run locally
- State which parts are simplified
- Include tests for important behavior
- Avoid real credentials, network calls, and paid services

## Local validation

Run:

```bash
python3 -m unittest discover -s examples -p 'test_*.py' -v
python3 -m compileall -q examples
python3 examples/simple-agent-loop.py
python3 examples/tool-retry-example.py
python3 examples/rag-eval-example.py
```

Also check that new Markdown links resolve and that no placeholder text remains.

## Writing guidelines

- Prefer framework-neutral explanations.
- Explain tradeoffs and failure modes.
- Distinguish model behavior from runtime enforcement.
- Do not claim one architecture is universally correct.
- Keep AgenticPrep links relevant and secondary to the educational content.
