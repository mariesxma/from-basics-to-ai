# Delivery Operations — one accumulating case

**Question:** which delivery orders should a dispatcher investigate first?

Work through one scenario from discovery to evaluation. Each stage carries forward the previous decisions and adds an output. These are learning stages, not unrelated mini-projects.

同一个配送场景，前一阶段的成果成为下一阶段的输入，逐步累积到完整方案。

**Available:** a fully written worked case, six synthetic records, exercises, and decision checks. **Not implemented:** a runnable application, data pipeline, real interviews, pilot, or AI model. The six records are provided as a readable table in stage 2.

## Follow the case

| Stage | What you have accumulated |
| --- | --- |
| [01 — Define the decision](01-problem-and-decision/README.md) | Problem brief |
| [02 — Inspect the evidence](02-data-and-quality/README.md) | Brief + data contract and quality report |
| [03 — Turn evidence into a decision rule](03-rules-and-priorities/README.md) | Previous outputs + ranked queue |
| [04 — Design the action workflow](04-workflow-and-prototype/README.md) | Previous outputs + workflow specification |
| [05 — Help a user complete the task](05-demo-and-adoption/README.md) | Previous outputs + demo and feedback plan |
| [06 — Measure outcomes without overstating them](06-pilot-and-impact/README.md) | Previous outputs + pilot and metric plan |
| [07 — Decide whether AI adds value](07-ai-decision-and-handoff/README.md) | Complete case + AI decision and handoff |

## How to study

1. Read the worked example and identify what was carried forward.
2. Complete the exercise in your own notes.
3. Check the completion gate before moving on.
4. If you change an assumption, revisit downstream calculations and recommendations.

Keep a single case notebook with sections matching these stages. Preserve earlier versions of your outputs so you can explain why a decision changed. Coding implementations can later live under `projects/delivery-operations/`; this entire learning case stays here.

## Shared assumptions

- Review time: 09:00 UTC, 5 October 2026.
- Operational capacity: two investigations; data-quality review has a separate owner.
- Snapshot freshness: at most 30 minutes for this exercise.
- Goals: support a useful decision, protect visibility of uncertainty, and measure outcomes honestly.

These are classroom assumptions, not facts from an actual organisation. The case contains no completed experiment or claim of business improvement.

[Start stage 1](01-problem-and-decision/README.md) · [Operational learning section](../README.md)
