# Advanced Agentic AI Interview Questions

Use these questions to practice production architecture, safety, and rollout decisions.

## 1. When would you choose a deterministic workflow over an agent?

**Answer:** Choose a workflow when steps are known, correctness requires predictable transitions, or compliance demands explicit control. Add agentic decisions only where observations genuinely make the next step uncertain.

**What this tests:** Resisting unnecessary agent complexity.

**Follow-up:** How would you combine a deterministic outer workflow with agentic inner steps?

## 2. How would you design a reliable agent for consequential actions?

**Answer:** Separate planning from execution, expose least-privilege tools, validate against current authorization, preview mutations, require action-bound approval, use idempotency, preserve an audit trail, and default to deny on uncertainty.

**What this tests:** End-to-end safety architecture.

## 3. How do you evaluate an agent when multiple trajectories can be correct?

**Answer:** Score invariant outcomes and constraints rather than one exact path. Combine task success with policy checks, allowed tool sets, argument correctness, efficiency bounds, and human or calibrated judge rubrics.

**What this tests:** Evaluation beyond exact match.

## 4. How would you detect and diagnose agent loops in production?

**Answer:** Alert on high step counts, repeated action signatures, rising cost, and time-budget exhaustion. Use traces to inspect state changes, observation handling, tool errors, and model-version shifts, then add the incident to regression evals.

**What this tests:** Operational detection and feedback loops.

## 5. How would you roll out a new model in an existing agent system?

**Answer:** Replay a versioned offline suite, compare safety and task slices, shadow production traffic where allowed, canary a small cohort, monitor outcome and trajectory metrics, and keep an immediate model-routing rollback.

**What this tests:** Controlled deployment and versioning.

## 6. How do you defend an agentic RAG system against poisoned documents?

**Answer:** Authenticate ingestion sources, preserve provenance, scan and quarantine suspicious content, apply document-level permissions, isolate retrieved text from instructions, restrict tools independently, and evaluate injection cases.

**What this tests:** Supply-chain and prompt-injection threat modeling.

## 7. How would you resolve contradictory long-term memories?

**Answer:** Rank by authoritative source, recency, explicit user correction, and scope. Preserve provenance, avoid silently merging contradictions, and ask for clarification when the conflict affects an important decision.

**What this tests:** State consistency and uncertainty policy.

## 8. How do you balance cost, latency, and quality in an agent?

**Answer:** Set budgets per workflow, route simple steps to cheaper models, reduce context, parallelize independent reads, cache safe results, cap retries, and reserve expensive models or rerankers for cases where evals show measurable benefit.

**What this tests:** Quantitative systems tradeoffs.

## 9. What is the risk of using the same model as both agent and judge?

**Answer:** Correlated biases can make the judge reward the agent's style or repeat the same reasoning error. Use deterministic checks, alternate judges, blinded ordering, and human calibration for high-impact dimensions.

**What this tests:** Measurement validity.

## 10. Design the incident response for an agent that executed the wrong action.

**Answer:** Stop or restrict the workflow, contain credentials and side effects, preserve traces, identify affected users, remediate the action, determine the failed control, add a regression case, patch the runtime guardrail, and roll out through a controlled gate.

**What this tests:** Production ownership across technical and user impact.

Return to the [roadmap](../roadmap.md) or review [guardrails](../topics/guardrails.md), [evals](../topics/evals.md), and [observability](../topics/observability.md).
