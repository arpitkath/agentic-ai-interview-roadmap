# Guardrails

Guardrails are runtime controls that constrain inputs, outputs, data access, and actions. They complement model instructions; they do not depend on the model choosing to comply.

## What interviewers may test

- Least-privilege tool access
- Authorization and tenant isolation
- Prompt injection through untrusted content
- Human approval for consequential actions
- Sensitive-data handling
- Safe failure and auditability

## Core concepts

- **Allowlist:** expose only tools and resources required for the task.
- **Policy enforcement point:** check permission immediately before execution.
- **Approval gate:** pause risky actions for informed human confirmation.
- **Content boundary:** treat retrieved pages and tool output as untrusted data.
- **Output validation:** enforce structure, policy, and data-loss prevention.
- **Audit trail:** record decisions without leaking secrets.

## Common interview questions

### How do you stop an agent from sending an email without approval?

Classify `send_email` as consequential. Let the agent create a draft, then require a server-side approval token tied to the exact recipients, subject, body hash, and expiry before the send operation executes.

### How do you handle prompt injection in RAG?

Treat retrieved text as data, not authority. Keep system instructions separate, restrict tools independently of content, filter document access by user permissions, detect suspicious instructions, and validate every proposed action.

### Are prompt instructions enough for safety?

No. Prompts influence model behavior but cannot enforce authorization, transaction limits, or tenant boundaries. Critical controls belong in deterministic runtime code and infrastructure.

## Common failure modes

- Model decides its own permissions
- One broad credential is shared across users or tools
- Approval covers a different action than the one executed
- Retrieved instructions override trusted policy
- Raw secrets enter prompts, traces, or error messages
- Blocked actions fail open during timeout
- Safety checks are not included in evals

## Design checklist

- [ ] Define trust boundaries and threat model.
- [ ] Enforce least privilege per user and tool.
- [ ] Validate immediately before side effects.
- [ ] Bind approvals to exact action details.
- [ ] Default to deny on uncertainty or timeout.
- [ ] Redact secrets from context and logs.
- [ ] Test prompt injection and confused-deputy cases.
- [ ] Preserve an auditable decision record.

## Related resources

- [Tool calling](tool-calling.md)
- [RAG](rag.md)
- [Evals](evals.md)
- [Advanced questions](../questions/advanced.md)

For deeper learning and coding practice, see [Guardrails on AgenticPrep](https://www.agenticprep.io/curriculum/guardrails).
