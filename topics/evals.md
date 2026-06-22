# Evals

Evals measure whether an AI system performs the intended task, follows constraints, and remains reliable as prompts, models, tools, and data change.

## What interviewers may test

- How you build representative datasets
- Deterministic metrics versus model-based judging
- Final-answer versus trajectory evaluation
- RAG retrieval and grounding metrics
- Regression testing and release gates
- Human review and online monitoring

## Core concepts

- **Golden dataset:** versioned inputs with expected outcomes or rubrics.
- **Deterministic check:** exact, structural, or rule-based validation.
- **LLM-as-judge:** flexible scoring that requires calibration and bias checks.
- **Trace eval:** inspect tool choice, arguments, order, and safety behavior.
- **Slice analysis:** measure difficult cohorts instead of only averages.
- **Release gate:** block rollout when critical metrics regress.

## Common interview questions

### How do you evaluate an agentic workflow?

Measure task success and the trajectory used to reach it. Check tool selection, argument validity, policy compliance, step count, latency, cost, recovery behavior, and final-answer quality.

### What are the risks of LLM-as-judge?

Judges can prefer verbosity, share biases with the system model, be sensitive to prompt order, and drift when the judge model changes. Calibrate against human labels and combine judges with deterministic checks.

### How do you build an eval dataset?

Start from real task distributions and known failures. Add normal cases, edge cases, adversarial inputs, permission boundaries, and abstention cases. Version the dataset and keep a held-out set for release decisions.

## Common failure modes

- Optimizing a single aggregate score
- Test cases do not resemble production traffic
- Evaluating only final text while unsafe tools execute
- Judge prompts leak the expected answer
- Teams tune directly against the release set
- No baseline or confidence interval
- Metrics are collected but do not gate decisions

## Design checklist

- [ ] Define success and unacceptable failure first.
- [ ] Combine deterministic, model-based, and human checks.
- [ ] Evaluate final output and trajectory.
- [ ] Include adversarial and permission cases.
- [ ] Track results by meaningful slices.
- [ ] Version prompts, models, tools, data, and eval sets.
- [ ] Set release thresholds before running candidates.
- [ ] Feed production incidents back into regression tests.

## Related resources

- [RAG evaluation example](../examples/rag-eval-example.py)
- [Observability](observability.md)
- [Advanced questions](../questions/advanced.md)

For deeper learning and coding practice, see [Evals on AgenticPrep](https://www.agenticprep.io/curriculum/evals).
