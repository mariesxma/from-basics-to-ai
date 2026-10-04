# 07 — Decide whether AI adds value

**Format:** worked learning case with exercises. All organisations, data, and examples are fictional.

## Carry forward

Keep the rules-based queue as the baseline and fallback. The six synthetic rows are not enough to train or validate a useful model.

## Worked output: AI proposal, not an implementation

**Candidate task:** rank eligible orders by risk of missing their promise, for the same two investigation slots.

**Data needed:** historical snapshots captured at review time, later outcomes, intervention records, and enough representative examples. Do not include delivery-completion timestamps or future status updates as prediction inputs.

**Baseline:** stage 3's explicit rule. Compare both methods on the same eligible population and held-out time period, then inspect performance by warehouse or other relevant operational group.

**Measures:** precision among the two selected orders per review, missed late orders, quality exclusions, runtime, and operator usefulness. High lateness risk is not necessarily high benefit from intervention; the most likely late order may already be impossible to rescue.

**Operational behavior:** the model proposes a ranking; a person decides and records the reason. When the model or its input is unavailable, use the agreed rule or a visible data-review path. Do not silently treat an unavailable prediction as low risk.

**Promotion decision:** adopt only if it improves a pre-agreed objective without unacceptable workload, reliability, or subgroup failures. Thresholds require evidence and stakeholder agreement. With the current case data, the decision is **do not deploy an AI model yet**.

中文：先问 AI 是否比简单规则更有用。预测会迟到，不等于干预能挽救；当前六条样例不足以训练和验证模型。

## Final handoff package

The accumulated case now contains:

1. A scoped decision and explicit assumptions.
2. A synthetic snapshot and quality report.
3. A reproducible ranking rule and exception queue.
4. A prototype workflow and implementation acceptance checks.
5. A demonstration and usability-test plan.
6. A pilot plan and metric definitions.
7. An AI evaluation proposal with a clear no-deployment decision for now.

The runnable application, user observations, pilot results, and trained model are still absent. These are separate future deliverables, not implied by finishing the written case.

## Your task

Write a five-sentence handoff: problem, evidence, proposed action, uncertainty, and next decision. Recommend the smallest next step rather than promising an end-to-end production system.

## Completion gate

You can trace a proposed action back to the original problem and evidence, distinguish plans from results, and explain why stopping at a non-AI solution can be appropriate.

[Case overview](../README.md) · [Previous stage](../06-pilot-and-impact/README.md)
