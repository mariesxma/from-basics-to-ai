# Operational problem solving

Learn to turn an unclear real-world problem into a useful, data-informed workflow, then explain and evaluate its impact.

学习把模糊的业务问题变成明确的问题、可信的数据分析和能实际使用的工作流，再验证它有没有帮助。

**Available now:** learning roadmap and a first discovery exercise. **Planned:** a runnable delivery-operations project with synthetic data, Python, SQL, and a user interface. No dataset or application for that project is included yet.

## The shared scenario

A fictional delivery team says: “Too many deliveries arrive late, and we do not know which orders to prioritise.” A dispatcher needs to decide what to investigate and act on before the next delivery window.

Use this scenario throughout the track. Its starting statement is a hypothesis to investigate, not proof that prioritisation is the solution. No real customer data is needed.

虚构配送团队说：订单总迟到，不知道优先处理哪些。先调查问题，不预设一定要做一个排序工具。

## Learn step by step

| Stage | Questions to answer | Skills | Deliverable | Status |
| --- | --- | --- | --- | --- |
| 01 — Understand the problem | Who makes which decision? What goes wrong today? | Discovery, stakeholder interviews, scoping, success criteria | One-page problem brief and current workflow | [Exercise available](01-problem-discovery.md) |
| 02 — Investigate the data | Which records answer the question, and can we trust them? | SQL joins, Python analysis, missing values, duplicates, timestamps, provenance | Data dictionary, quality report, and reproducible analysis | Planned |
| 03 — Model the operation | How do orders, warehouses, deliveries, people, and actions connect? | Entity relationships, identifiers, business rules, event timelines | Relationship diagram and decision rules | Planned |
| 04 — Build a useful workflow | What should a dispatcher see and do? | Prioritisation, interface design, validation, collaboration with engineers | Complete local application with a transparent priority rule | Planned |
| 05 — Help people use it | Can a new user complete a real task? | Demonstrations, training, feedback, adapting explanations to the audience | Demo, quick-start guide, and observed usability exercise | Planned |
| 06 — Measure and improve | Did decisions or outcomes improve? What else could explain the change? | Baselines, metrics, pilots, tradeoffs, communicating uncertainty | Pilot plan, results report, and recommendation | Planned |
| 07 — Add AI where justified | Does a model improve on the simple rule? | Evaluation, human review, failure analysis, cost and latency | Optional evaluated AI version with a non-AI fallback | Planned |

Stages are learning milestones. The runnable project will live under `projects/delivery-operations/` when implemented, with complete versions preserved as it grows. This section holds the explanations and exercises.

每阶段有可检查的产出；以后完整应用放在 projects 下，本节保留思路与练习。先建立可解释的简单方法，再判断是否需要 AI。

## What good work looks like

- **Specific:** identify the user, decision, time window, and constraint before choosing a tool.
- **Evidence-based:** separate observed facts, assumptions, and questions. Trace a conclusion back to data.
- **Usable:** support an action, not just a chart. Explain what happens when data is missing or stale.
- **Collaborative:** document questions for operators, data owners, and engineers rather than guessing their answers.
- **Measurable:** define a baseline and success criteria; record negative effects as well as improvements.
- **Honest:** synthetic data can demonstrate a method, but cannot establish real-world business impact.

## Connections to the rest of the repo

| Section | How it supports this track |
| --- | --- |
| [Programming projects](../projects/README.md) | Build the technical foundations, then implement working tools |
| [Mathematics](../mathematics/README.md) | Understand rates, distributions, uncertainty, and comparisons as content is added |
| [Algorithms](../algorithms/README.md) | Explore ranking and allocation methods as content is added |
| [System design](../system-design/README.md) | Reason about storage, APIs, reliability, and deployment |
| [AI concepts](../ai-concepts/README.md) | Learn model behavior and evaluation as content is added |

You can begin discovery now while continuing Python. Finish basic functions and collections before the future data-analysis exercises; learn SQL when it becomes useful. Completing every game stage is not a prerequisite.

[Start the discovery exercise](01-problem-discovery.md) · [Main roadmap](../README.md)
