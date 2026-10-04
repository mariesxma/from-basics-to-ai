# 01 — Understand the problem

**Goal:** turn “deliveries are late” into a clear investigation and decision. No coding required.

目标：把模糊抱怨变成可调查的问题和明确决策。本练习不需要写代码。

## Scenario

A fictional dispatcher currently checks several spreadsheets and messages to decide which orders to investigate. The team reports late deliveries but has not supplied a reliable baseline, a consistent definition of “late,” or evidence about the causes.

Everything in this scenario is an exercise assumption. Do not invent interview findings or claim that a solution has already improved outcomes.

## 1. Identify the decision

Write one sentence in this form:

> [User] needs to decide [action] by [time] because [consequence], subject to [constraint].

Example hypothesis: “The dispatcher needs to choose which at-risk orders to investigate before dispatch closes, while respecting limited staff capacity.” Confirm the time window and capacity rather than inventing numeric limits.

先明确谁、什么时候、做什么决定、受什么限制。例句是假设，不是已经验证的事实。

## 2. Prepare discovery questions

- What counts as late: arrival, handover, or completed delivery? Which promised timestamp matters?
- Walk through the last late order: when was the problem noticed, and what happened next?
- Which decisions can the dispatcher actually make? Who can approve a change?
- What is the current workflow, including spreadsheets, messages, handoffs, and exceptions?
- Which delays are costly or urgent, and who defines those priorities?
- Which data sources exist, who owns them, and how quickly do they update?
- What would make a proposed tool unusable or untrustworthy?

If no interview partner is available, record these as unanswered questions. A simulated conversation is practice, not customer evidence.

## 3. Sketch the current workflow

Start with this tentative chain and mark gaps:

```text
Order accepted → warehouse preparation → dispatch → delivery → issue resolution
```

For each step, record the actor, input, action, output, and handoff. Place a question mark where ownership or data is unknown. Do not assume that every delay originates in the warehouse.

## 4. Define evidence to request

| Candidate source | Fields to investigate | Checks to plan |
| --- | --- | --- |
| Orders | Order ID, promised delivery time, status | Unique IDs, cancelled orders, timezone |
| Warehouse events | Order ID, event type, event time | Missing events, sequence, late-arriving records |
| Delivery records | Order ID, dispatch and completion timestamps | Multiple attempts, incomplete journeys, join coverage |
| Intervention log | Order ID, action, actor, time, outcome | Whether outcomes can be attributed to an intervention |

This is a proposed data request, not an existing schema. Confirm access and join keys with the data owner. Avoid collecting personal information that is unnecessary for the exercise.

## 5. Define success before building

Propose an on-time delivery rate with an explicit numerator, denominator, time window, and exclusions. Resolve how pending and cancelled orders should be treated before comparing rates.

Also consider time spent prioritising orders and a guardrail such as extra workload or unnecessary escalations. Do not claim that a changed rate proves the tool caused it: order mix, seasonality, and staffing may also change.

成功标准要先写清楚怎么算。效果变化不一定由工具造成，还要考虑订单结构、季节和人员变化。

## 6. Produce the one-page brief

Fill out these fields in your own notes:

| Field | Your answer should include |
| --- | --- |
| User and decision | Who acts, what they decide, and when |
| Current workflow | Steps, handoffs, and observed or suspected difficulty |
| Evidence | Known facts with sources; assumptions clearly labelled |
| Data needed | Candidate sources, owners, access and quality questions |
| Scope | One decision to support first and what is out of scope |
| Success | Metric definition, baseline to obtain, and guardrails |
| Next step | The smallest investigation that could confirm or reject the hypothesis |

## Completion checklist

- [ ] A reader can identify the user and the decision without seeing a proposed product.
- [ ] Facts, assumptions, and unanswered questions are distinct.
- [ ] Data requests relate directly to the decision.
- [ ] Success criteria include a definition, baseline requirement, and guardrail.
- [ ] The next step investigates the problem rather than committing to an untested solution.

Optional challenge: present the brief in three minutes to someone else. Ask them to explain back the problem and decision; revise any unclear parts.

Next planned stage: investigate synthetic data using SQL and Python. [Back to the learning roadmap](README.md).
