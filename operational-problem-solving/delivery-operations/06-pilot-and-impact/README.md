# 06 — Measure outcomes without overstating them

**Format:** worked learning case with exercises. All organisations, data, and examples are fictional.

## Carry forward

Freeze the rule version and document any usability revisions. Distinguish application correctness, successful user actions, and business outcomes.

## Worked output: pilot plan v1

- Obtain a real baseline using agreed definitions before setting a target.
- Start with a shadow review: compute recommendations without changing dispatch decisions.
- Check data quality and whether the recommendations are actionable.
- If justified, run a limited pilot with comparable shifts or a suitable assignment design. Record capacity, order mix, staffing, and rule changes.
- Measure time to prioritise, valid completed investigations, unnecessary escalations, and delivery outcomes.
- Pause when data cannot support decisions or workload exceeds the agreed capacity. Numeric stop thresholds must be chosen before the pilot, not invented after seeing results.

## Worked arithmetic: illustrative outcomes only

For a separate, made-up historical batch: 20 orders had valid promised timestamps and were due within the completed observation window. Eighteen were completed on time. The on-time rate is 18 / 20 = 90%.

This is not a pilot result and not an outcome for the six-row review snapshot. Open orders already past their promise at the window's cutoff count as not on time; cancellations and invalid promises must follow a documented eligibility rule. Report excluded records separately.

A later batch with 19 / 20 = 95% is 5 percentage points higher. That difference alone does not establish that the workflow caused an improvement; small samples and different order mixes matter.

## Results report structure

| Field | What to record |
| --- | --- |
| Population and window | Eligible orders, exclusions, and comparison design |
| Data quality | Missingness, freshness, join coverage |
| Workflow evidence | Task times, actions completed, user errors |
| Outcome evidence | Defined delivery metric with counts, not only percentages |
| Guardrails | Added workload and unnecessary escalation |
| Limitations | Confounders, sample size, missing observations |
| Decision | Continue, revise, stop, or gather more evidence |

Current case status: no pilot has been run. All real results remain unmeasured.

中文：能算指标不等于证明效果。模拟数字只用于练习，不是业务成果。

## Your task

Explain how excluding every late, unfinished order would bias the on-time rate. Propose one way to make a pilot comparison fairer.

## Gate to the next stage

Have a reproducible metric and an evaluation plan. AI is optional; a useful rules-based workflow is already a valid destination.

[Case overview](../README.md) · [Previous stage](../05-demo-and-adoption/README.md) · [Next stage](../07-ai-decision-and-handoff/README.md)
