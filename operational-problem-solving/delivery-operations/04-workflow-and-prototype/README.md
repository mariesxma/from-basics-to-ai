# 04 — Design the action workflow

**Format:** worked learning case with exercises. All organisations, data, and examples are fictional.

## Carry forward

The prototype must implement the data-quality gate and ranking from stage 3, not invent a different score in the interface.

## Worked output: prototype specification v1

This is a text prototype and acceptance specification. A runnable application is not implemented yet.

```text
Dispatch review — 09:00 UTC — rule v1
Investigation capacity: 2

RECOMMENDED
A102 | score 4 | due in 60m | carrier exception | [Assign]
A101 | score 3 | due in 30m | not ready         | [Assign]

OTHER ELIGIBLE ORDERS
A105 | score 1 | not ready
A103 | score 0 | no rule flags

DATA REVIEW — 2 unresolved
A104 | missing promise | request correction
A106 | stale snapshot | request refresh
```

## Walk through one action

1. Dispatcher opens A102 and inspects the timestamp and scoring reasons.
2. They assign an investigation to the carrier coordinator, with a reason and follow-up time.
3. The system records the action and uses one available investigation slot.
4. Repeated clicking must not create duplicate open investigations for that order.
5. The coordinator records an update. Resolving the investigation does not automatically mark the delivery on time.
6. If evidence changes before assignment, show the new evidence and require review again.

For A101, the proposed owner is the warehouse lead. Names here are fictional functional roles, not real recipients. No messages are sent by this exercise.

## Acceptance checks for the future app

- [ ] The six-row fixture produces exactly the stage 3 ranking and two quality exceptions.
- [ ] Two different orders can be assigned; a third requires an explicit capacity decision.
- [ ] A duplicate assignment does not consume another slot.
- [ ] Missing/stale evidence cannot receive a reassuring score of zero.
- [ ] Each action preserves its actor, evidence version, rule version, and reason.
- [ ] A user can correct or cancel an action with a recorded explanation.

中文：页面要支持行动，不只是展示数字。每次分配都要能追溯当时的数据和理由。

## Your task

Sketch what a user sees when A102's exception clears just before they press Assign. Decide how a changed recommendation should be communicated.

## Gate to the next stage

A reader can act on a recommendation, handle a data exception, and understand what is recorded. Do not label the application complete until implementation and checks exist.

[Case overview](../README.md) · [Previous stage](../03-rules-and-priorities/README.md) · [Next stage](../05-demo-and-adoption/README.md)
