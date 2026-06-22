# Observability

Observability makes an agent run explainable through structured events, traces, metrics, and replayable inputs. It is required to debug failures that cross model, retrieval, and tool boundaries.

## What interviewers may test

- What to record for each model and tool step
- Correlation IDs and distributed traces
- Cost, token, latency, and reliability metrics
- Privacy-aware logging
- Replay and incident debugging
- Turning production failures into eval cases

## Core concepts

- **Run trace:** a causally ordered record of decisions, calls, and results.
- **Structured event:** machine-queryable fields rather than unstructured text.
- **Correlation ID:** connect user request, model calls, retrieval, and tools.
- **Redaction:** remove secrets and sensitive data before storage.
- **Replay:** rerun captured inputs with controlled dependencies.
- **Operational metric:** aggregate success, error, latency, cost, and policy events.

## Common interview questions

### What should you log for a tool call?

Record run and step IDs, tool name, validated argument metadata, authorization decision, start and end time, status, normalized error class, retry count, and result size. Redact secrets and sensitive values.

### How would you debug a wrong agent action?

Start with the failed run trace. Check the context and tool catalog shown to the model, the selected action, validation and policy decisions, tool result, and subsequent state. Reproduce with a replay or mocked dependency.

### Which metrics belong on an agent dashboard?

Track task success, escalation and abstention, tool errors, invalid calls, policy blocks, step count, latency percentiles, tokens, cost, and model or retrieval fallbacks. Segment by workflow and version.

## Common failure modes

- Logging only the final answer
- No shared run ID across services
- Traces store credentials or personal data
- Model, prompt, tool, or index versions are missing
- Sampling removes rare safety failures
- Retries hide the original error
- Incidents are fixed without adding regression cases

## Design checklist

- [ ] Assign run and step identifiers.
- [ ] Capture model, prompt, tool, and data versions.
- [ ] Record validation and policy decisions.
- [ ] Track latency, tokens, cost, and retries.
- [ ] Redact or hash sensitive fields.
- [ ] Preserve high-severity safety events.
- [ ] Support controlled replay.
- [ ] Convert incidents into eval fixtures.

## Related resources

- [Agent loops](agent-loops.md)
- [Evals](evals.md)
- [Advanced questions](../questions/advanced.md)

For deeper learning and coding practice, see [Observability on AgenticPrep](https://www.agenticprep.io/curriculum/observability).
