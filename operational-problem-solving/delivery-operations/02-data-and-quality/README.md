# 02 — Inspect the evidence

**Format:** worked learning case with exercises. All organisations, data, and examples are fictional.

## Carry forward

Use problem brief v1: one 09:00 review, six orders, two investigation slots. We need information available **at that time**, not facts learned after delivery.

## Worked input: synthetic snapshot

All times below are UTC on 5 October 2026. Minutes remaining are measured from 09:00. `ready` means ready for dispatch, not already delivered.

| Order | Promised by | Minutes left | Ready | Carrier exception | Snapshot updated |
| --- | --- | --- | --- | --- | --- |
| A101 | 09:30 | 30 | No | No | 08:55 |
| A102 | 10:00 | 60 | Yes | Yes | 08:58 |
| A103 | 12:00 | 180 | Yes | No | 08:50 |
| A104 | Unknown | Unknown | No | No | 08:57 |
| A105 | 10:30 | 90 | No | No | 08:56 |
| A106 | 09:45 | 45 | Yes | No | 07:00 |

This table is the supplied classroom evidence. It is not a live feed or a statistically representative dataset.

## Worked output: data contract and quality report v1

- **Grain:** one row per order at the review snapshot. `order_id` must be unique.
- **Required fields:** ID, promised timestamp, readiness, exception flag, update timestamp. Boolean fields must be known or explicitly marked unknown.
- **Time rule:** use timezone-aware UTC timestamps. Future updates cannot be used in this snapshot.
- **Freshness rule:** for this exercise, an update older than 30 minutes is stale. This threshold needs operational validation.
- **A104:** missing promise; deadline urgency cannot be computed.
- **A106:** last updated 120 minutes ago; do not interpret its old “no exception” as current reassurance.
- **Result:** four orders have sufficient current data for operational ranking; two require data review.

In a larger implementation, inspect duplicate IDs, missing joins, conflicting statuses, and ingestion delay. When joining event history, select the latest event available by the review time for each order; a raw one-to-many join can duplicate orders and distort counts.

中文：A104 缺承诺时间，A106 数据过期。不能把未知当成正常，也不能用未来数据帮助过去的决策。

## Your task

Calculate each snapshot age. Explain why A103 is current enough under the exercise rule and A106 is not. Propose what should happen if an order has two conflicting latest events.

## Gate to the next stage

You can reproduce the four-versus-two quality split and explain every exclusion. Missing data remains visible.

[Case overview](../README.md) · [Previous stage](../01-problem-and-decision/README.md) · [Next stage](../03-rules-and-priorities/README.md)

## Conversation practice

See the [stage-to-conversation map](../conversation-practice/README.md) for dialogue, talking points, and the accumulated meeting outputs for this stage.
