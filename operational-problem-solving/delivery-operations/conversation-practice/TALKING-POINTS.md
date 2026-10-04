# Talking-point playbook

Use these prompts as flexible conversation aids, not a questionnaire to read mechanically. Follow relevant answers, let the person finish, and check your understanding before changing topics.

英文是可练习的话术；中文提示帮助理解目的。不是套话术操控对方，而是帮助双方把事情讲清楚。

## Discovery talking points

| Point | Key purpose | Suggested wording | Listen for / next move | Capture |
| --- | --- | --- | --- | --- |
| D1 — Agenda | Agree a useful outcome | “Let’s start with the decision you need to make, then look at a recent example. That will help us agree what is worth investigating.” | A different urgent priority: adjust the agenda | Meeting outcome |
| D2 — Incident | Move from general frustration to evidence | “Could you walk me through the last time that happened?” | Specific actor, event, time; if still broad, ask about one shift | Example and source |
| D3 — Decision | Identify an action and constraint | “What were you trying to decide, and what could you actually change?” | Authority, capacity, deadline | Decision statement |
| D4 — Cause | Separate explanation from observation | “What makes you think that is the cause? When does the pattern not hold?” | Supporting evidence and counterexamples | Hypotheses and gaps |
| D5 — Impact | Find measurable consequences | “What happens downstream when that decision is delayed?” | Rework, delay, risk; unknown numbers stay unknown | Candidate metrics |
| D6 — Evidence | Make a targeted data request | “Which record would let us check that example, and who can explain its meaning?” | Definition, ownership, access, timing | Data request and owner |
| D7 — Solution request | Connect a proposed tool to a task | “What would someone do differently if they had that?” | A decision, or a feature with no clear action yet | Need versus proposed approach |
| D8 — Scope | Agree a useful first boundary | “For the first iteration, I suggest X. Y would need a separate decision because Z. Would X still be useful?” | An essential dependency versus a future wish | In/out and revisit trigger |
| D9 — Playback | Invite correction | “Here is what I heard. What have I missed or misunderstood?” | New constraints or disagreement | Revised brief |
| D10 — Commitment | Make next steps concrete | “With these inputs, I can bring this artifact for this decision. Who owns the inputs, and when are they feasible?” | Missing dependencies or decision-maker | Owner, date to agree, deliverable |

## Turning complaints into investigable questions

Do not label the person as “complaining.” Treat the statement as a signal, acknowledge the difficulty, then ask for a concrete example without assuming its cause.

| What the client says | What it might mean—not a conclusion | Natural follow-up | Avoid |
| --- | --- | --- | --- |
| “The data is terrible.” | Missing, stale, inconsistent, inaccessible, or poorly understood data | “Which decision was affected most recently? Could we look at the record you could not rely on?” | “So you need a new data platform.” |
| “Nobody takes ownership.” | Unclear handoff, incentives, permissions, or capacity | “After an issue is flagged, who normally takes the next step? What happened in the last example?” | Blaming a named team |
| “The dashboard is useless.” | It may not support a decision or action | “What did you need to do that the dashboard could not help you do?” | Adding more charts immediately |
| “Everything is urgent.” | No shared prioritisation rule or insufficient capacity | “If only two investigations could happen today, how would you choose? What would be the consequence of waiting?” | Inventing priority weights without review |
| “We need real-time data.” | A decision may need fresher information | “How late can an update arrive before it changes the decision? Can you give an example?” | Promising live streaming before understanding need |
| “We need AI.” | A desired capability, an expectation, or an unclear problem | “Which judgement should improve, and how would we know it is better than today?” | Promising a model or dismissing the request |
| “Just automate it.” | Repetitive work, but perhaps exceptions or accountability matter | “Which steps are predictable, and which require someone to check or approve an exception?” | Automating external actions without scope |
| “We need it next week.” | A fixed event or negotiating anchor | “What must be possible by then? Could a sample analysis or prototype support that decision?” | Agreeing to a production deadline without dependencies |

## Follow-up branches

**If the answer is still vague:** “Could we pick one order or one shift and walk through it?”

**If they do not know:** “Let’s record that as an open question. Who is best placed to check?”

**If people disagree:** “It sounds like you are describing different parts of the process. Could we compare one example from each before choosing a definition?”

**If the conversation jumps to a solution:** “I’ll capture that option. Before evaluating it, can we finish identifying the action it needs to support?”

**If the complaint reveals an urgent issue outside scope:** “This sounds important and may need a different owner. Who should handle it now, and should we change today’s priorities?” Do not force the original agenda.

**If a new request changes the work:** “That changes the scope and dependencies. Let’s decide whether to replace something in this iteration or assess it separately.”

中文：不清楚就问具体例子；不知道就找信息负责人；意见不同先对齐定义；新增需求要重新评估范围。

## Transitions in natural business language

- **Problem → workflow:** “Now that we have the decision, could you show me how the team reaches it today?”
- **Workflow → data:** “To check where that breaks down, let’s look at what information is available at that moment.”
- **Data → rule:** “We have identified the records we can rely on. Let’s test a simple way to prioritise them and look for cases where it fails.”
- **Rule → workflow:** “A ranking is useful only if someone can act on it. Let’s walk through who does what next.”
- **Demo → adoption:** “Rather than explain every control, I’d like to see whether the task is clear enough to complete without help.”
- **Pilot → impact:** “Let’s separate what we observed from what we can reasonably attribute to the change.”
- **Impact → next scope:** “Based on that evidence, what is the smallest next investment we can justify?”

## Words to translate for a business audience

| Technical phrase | Plain alternative |
| --- | --- |
| Data quality | Can we rely on this information for this decision? |
| Latency / freshness | How old is the information when someone acts? |
| Entity model | Which things are we tracking, and how do they relate? |
| Idempotent assignment | Repeating the action should not create duplicate work. |
| Audit trail | Can we see who acted, why, and using which information? |
| Baseline | What happens today before the change? |
| Evaluation metric | What would we measure to decide whether this helps? |
| Scope | What this iteration includes, and what needs a separate decision |

## Meeting notes that accumulate

Use one case notebook. For each statement record **source, status, implication, and next check**.

| Entry type | Example from the fictional case | How to treat it |
| --- | --- | --- |
| Reported experience | “I spend the review checking messages.” | A person's account; observe or measure before quantifying |
| Supplied sample fact | A104 has no promised timestamp | True of the sample; do not generalise to the full operation |
| Hypothesis | Fragmented information delays prioritisation | Test against examples and counterexamples |
| Exercise assumption | Two investigation slots | Replace with validated capacity in a real setting |
| Decision | Keep unscorable records in a visible exception queue | Record owner, rationale, and scope |
| Open question | Does completion timestamp mean handover? | Assign an owner and follow-up |

## Closing recap to practise

“Today we focused on [decision] for [user]. We learned [supported finding], while [uncertainty] still needs checking. For the first iteration we agreed [scope]; [excluded item] needs a separate decision. [Owner] will confirm [input] by [agreed date]. With that input, I can bring [artifact] so we can decide [next decision]. If the input is delayed, I’ll explain the gaps and revised options. What should I correct before I send the recap?”

This is a rehearsal template; do not substitute invented dates, findings, or agreements into a real recap. No recap is sent by this repository.

## Practice and self-review

Take turns as facilitator and operator. Start with one complaint from the table, and improvise the answers instead of copying the transcript. Afterwards check:

- [ ] Did I acknowledge the experience without assuming a cause?
- [ ] Did I get a specific example and a concrete decision?
- [ ] Did I ask a counterexample or invite correction?
- [ ] Did I separate evidence from assumptions and proposed solutions?
- [ ] Did we agree useful scope, exclusions, and owners?
- [ ] Did I commit to a feasible artifact and next decision, rather than an unsupported result?

[Annotated transcript](TRANSCRIPT.md) · [Conversation map](README.md)
