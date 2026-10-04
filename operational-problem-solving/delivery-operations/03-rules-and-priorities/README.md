# 03 — Turn evidence into a decision rule

**Format:** worked learning case with exercises. All organisations, data, and examples are fictional.

## Carry forward

Keep the original decision and all six rows. Use the stage 2 quality gate before calculating priority.

## Worked output: decision rule v1

First send missing or stale records to a **data-review queue**. For eligible records, assign points:

- 2 points if the promise is at most 60 minutes away, including already-overdue orders.
- 1 point if the order is not ready.
- 2 points if a carrier exception is active.

Sort by score descending, then promised time ascending, then order ID ascending. These weights are transparent exercise choices, not a validated prediction model.

| Order | Quality gate | Calculation | Operational rank |
| --- | --- | --- | --- |
| A102 | Pass | 2 deadline + 0 readiness + 2 exception = 4 | 1 |
| A101 | Pass | 2 deadline + 1 readiness + 0 exception = 3 | 2 |
| A105 | Pass | 0 deadline + 1 readiness + 0 exception = 1 | 3 |
| A103 | Pass | 0 + 0 + 0 = 0 | 4 |
| A104 | Missing promise | No score | Data review |
| A106 | Stale snapshot | No score | Data review |

**Recommendation:** investigate A102 and A101. Separately ask the data owner to resolve A104 and A106; do not hide them below low-scoring orders. For the exercise, the data owner is separate from the two operational investigation slots. If the dispatcher owns both queues, revisit capacity before applying this rule.

## Model the relationships

```text
Order → many status events
Order → many investigation actions
Investigation action → one accountable owner
Review snapshot → the version of evidence used for a decision
```

Store an action's order ID, owner, reason, timestamp, and status. An alert is not the same as an action, and an action is not proof of a successful outcome.

中文：规则必须能解释。先查数据质量，再排序；“分数高”不是一定迟到，也不证明干预一定有效。

## Your task

Increase capacity to three and identify the additional order. Then remove the carrier-exception weight: does the first choice change? Explain what evidence would justify either weighting.

## Gate to the next stage

You can reproduce the ranking by hand and explain a tie, an overdue order, and an unscorable order.

[Case overview](../README.md) · [Previous stage](../02-data-and-quality/README.md) · [Next stage](../04-workflow-and-prototype/README.md)
