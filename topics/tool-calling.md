# Tool Calling

Tool calling allows a model to request external data or actions through a structured interface. The runtime validates the request, enforces permissions, executes the tool, and returns an observation.

## What interviewers may test

- How you design names, descriptions, and schemas
- Validation before execution
- Retry, timeout, and error-classification policy
- Idempotency for mutating calls
- Permissions and approval for consequential actions
- How the model chooses among similar tools

## Core concepts

- **Schema:** define typed parameters, required fields, constraints, and descriptions.
- **Dispatch:** map an allowed tool name to a known implementation.
- **Validation:** reject unknown fields, invalid types, and business-rule violations.
- **Idempotency:** make repeated mutations safe with request keys or deduplication.
- **Retry policy:** retry only transient failures and bound every attempt.
- **Result normalization:** give the model predictable success and error shapes.

## Common interview questions

### What makes a good tool schema?

Use a specific verb-noun name, explain when the tool should be called, constrain parameters, and distinguish required from optional fields. Descriptions should resolve ambiguity rather than restate parameter names.

### When should a failed tool call be retried?

Retry temporary failures such as timeouts, connection resets, and rate limits when the operation is safe to repeat. Do not retry invalid input, denied permissions, or business-rule errors without changing the request.

### How do you make a mutating tool safe?

Validate authorization and arguments, require confirmation for risky operations, use an idempotency key, record an audit event, and return the authoritative result. Never rely on the model to enforce those controls.

## Common failure modes

- Ambiguous or overlapping tool descriptions
- Schema accepts more input than the implementation
- Raw user input reaches SQL, shell, or file paths
- Blind retries duplicate a charge, message, or database write
- Tool timeout consumes the entire agent budget
- Sensitive tool output is copied into model context
- The agent can call tools outside the user's permissions

## Design checklist

- [ ] Use clear, non-overlapping tool descriptions.
- [ ] Validate schema and domain rules.
- [ ] Apply per-user authorization.
- [ ] Classify tools by risk.
- [ ] Define timeout and retry policy.
- [ ] Protect mutations with idempotency.
- [ ] Normalize errors without exposing secrets.
- [ ] Log tool name, arguments policy, result status, and duration.

## Related resources

- [Retry example](../examples/tool-retry-example.py)
- [Agent loops](agent-loops.md)
- [Guardrails](guardrails.md)
- [Intermediate questions](../questions/intermediate.md)

For deeper learning and coding practice, see [Tool creation on AgenticPrep](https://www.agenticprep.io/curriculum/tool-creation).
