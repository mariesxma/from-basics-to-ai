# Annotated conversation transcript

**Fictional rehearsal script. No meetings, commitments, customer findings, or measured results below actually occurred.** Numbers and records come from the synthetic learning case. English dialogue is followed by coaching notes in plain English and Chinese.

## 1. Discovery meeting

**Purpose:** understand one operational decision before proposing a solution. Suggested rehearsal: 30 minutes. Talking points D1–D10 also appear in the [playbook](TALKING-POINTS.md).

### D1 — Open with a shared purpose

**Facilitator:** “Thanks for making time. I’d like to start with what happens during a morning dispatch review, then walk through a recent example and look at the information you use. That will help me identify where support could be useful, and help you decide whether this is worth pursuing. By the end, I’d like us to agree on one problem to investigate, what we still need to verify, and what I should bring back next time. Is there something more urgent we should cover first?”

**Maya:** “That works. We mainly want fewer late deliveries.”

**Coaching:** Offer an agenda with a benefit for both sides, then invite correction. The outcome is a useful investigation, not a commitment to build a tool.

中文：先讲今天聊什么、为什么聊、结束时拿到什么，再让对方调整议程。

### D2 — Acknowledge a complaint and ask for an incident

**Maya:** “Dispatch is chaos. The spreadsheets are useless and nobody knows what’s going on.”

**Facilitator:** “It sounds like the team is spending a lot of effort getting a reliable picture. Could you walk me through the most recent review where that made a decision difficult?”

**Leo:** “We had an order waiting on the warehouse and another with a carrier issue. I spent the review checking messages instead of deciding who to call.”

**Facilitator:** “Let’s stay with that example. What were you trying to decide when the review started?”

**Coaching:** The complaint is meaningful, but its cause is not established. Acknowledge the burden without endorsing the claim that spreadsheets are the cause. Ask for a specific event, then the blocked decision.

中文：不反驳抱怨，也不直接认定工具有问题。先问最近一次具体发生了什么，再找被卡住的决定。

### D3 — Make the decision and capacity concrete

**Leo:** “Which orders to chase first. We can’t chase everything.”

**Facilitator:** “What does ‘chase’ mean in practice—contact someone, change a route, or something else?”

**Leo:** “Usually ask the warehouse lead or carrier coordinator to investigate.”

**Facilitator:** “How much investigation capacity is normally available at that point?”

**Maya:** “For our practice scenario, assume two investigations and ten minutes before the 09:00 review.”

**Facilitator:** “So the immediate decision is which two orders to investigate, and who should own each action. That is narrower than preventing every late delivery. Does that describe the first decision accurately?”

**Leo:** “Yes. We can request an investigation, but we can’t create extra vehicles.”

**Coaching:** Clarify the verb, time, capacity, and authority. The two-slot limit is a supplied classroom assumption; in a real meeting it would require validation across normal and exceptional days.

### D4 — Separate symptoms from possible causes

**Facilitator:** “When you say an order was late, which event are you measuring against which promise?”

**Leo:** “I mean the customer received it after the promised delivery time.”

**Sam:** “Our source records completion, but we need to check whether that always means handover.”

**Facilitator:** “I’ll record that as an unresolved definition. What happens between accepting an order and recording completion, and where did the last example get stuck?”

**Leo:** “Order accepted, warehouse preparation, dispatch, then delivery. That example seemed to be waiting for preparation, but I’d need the event history to confirm.”

**Facilitator:** “What examples don’t fit that explanation? Have ready orders also arrived late?”

**Leo:** “Yes, carrier issues can still delay them.”

**Coaching:** Ask for disconfirming examples before settling on a cause. Record “seemed to be waiting” as a hypothesis, not a verified root cause.

中文：现象、解释、证据分开记。问反例，是为了避免只收集支持自己猜测的信息。

### D5 — Understand impact without inventing a number

**Facilitator:** “When the decision is delayed, what changes for the team or customer?”

**Maya:** “More follow-up calls, and sometimes we miss a chance to intervene.”

**Facilitator:** “Which of those effects could we measure with information you already collect? And which would need observation?”

**Maya:** “We should observe time spent in the review. I don’t have a reliable number today.”

**Facilitator:** “That’s fine. I’ll leave the baseline as unknown rather than estimate it from this conversation. We should also track unnecessary escalations so a faster review doesn’t simply create more work elsewhere.”

**Coaching:** Turn “it costs a lot” into a measurement question. Avoid demanding a fabricated business case during discovery.

### D6 — Ask for evidence with a purpose

**Facilitator:** “To check whether the information can support this decision, could we look at a small approved sample of orders, promised times, warehouse events, and delivery records? I’d also like to know when each update became available. That helps us avoid using information the dispatcher could not have known at 09:00.”

**Sam:** “We can start with the six synthetic records in the case. I would need to confirm definitions and access before any real extract.”

**Facilitator:** “Good. Who can confirm the meaning of each timestamp and the order identifier used to connect those records?”

**Sam:** “I can coordinate that with the source owners.”

**Coaching:** Explain why each data request matters. Access, meaning, and freshness are separate questions. No real data sharing has been authorised by this fictional exchange.

### D7 — Handle a proposed solution without dismissing it

**Maya:** “Can we just use AI to tell us which orders will be late?”

**Facilitator:** “We can evaluate that option. Before choosing the method, I’d like to establish a simple baseline and see whether the available information supports an actionable decision. If a clear rule already helps, it gives us something concrete to compare a model against. What would the team do differently with a prediction?”

**Leo:** “We’d still need to know who to contact and whether they can do anything.”

**Coaching:** Treat the suggestion as a candidate approach. Bring the conversation back to an action and evidence; do not promise AI or reject it as unnecessary before investigation.

### D8 — Agree boundaries and park larger requests

**Maya:** “Eventually we need route planning across every warehouse.”

**Facilitator:** “I’ll capture that as a future possibility. For the first iteration, I propose one review workflow: identify two investigations, show the reasons, and record an owner and follow-up. Automatic rerouting, changing customer promises, and a company-wide rollout would be outside that first scope. This lets us test the decision without taking on changes we cannot yet validate. Would that still be useful?”

**Maya:** “Yes, as long as the larger need stays visible.”

**Facilitator:** “Let’s put it in a future-work list with the evidence we would need to revisit it.”

**Coaching:** Explain the value of the boundary and ask whether the reduced scope is still worth doing. Parking a request is not silently accepting it for later delivery.

中文：范围外不是冷冰冰地拒绝；说明为什么先做这一步，并约定什么条件下重新讨论。

### D9 — Reflect back and invite correction

**Facilitator:** “Let me check my understanding. The immediate issue is choosing and assigning two investigations with limited time. We suspect fragmented or stale information contributes, but we have not established how much it explains late delivery. We need to verify the completion definition and source update times. Have I missed anything, or put too much emphasis on the data?”

**Leo:** “Ownership matters too. Sometimes everyone assumes someone else is following up.”

**Facilitator:** “That changes the brief: we need a visible owner and follow-up state as well as a ranking. I’ll add that, rather than treating this as only a reporting problem.”

**Coaching:** A summary is a test of understanding. Let it change your proposal. Do not ask “we agree, right?” after a long sales pitch.

### D10 — Close with a conditional, concrete commitment

**Facilitator:** “For our next session, I can bring a one-page problem brief, a map of the current workflow, and a quality review of the agreed sample. Sam, could you confirm the field definitions and access constraints before we schedule that review? Leo, could you review whether the workflow reflects a typical morning? If the inputs are available, we can use the next meeting to decide whether a small prioritisation prototype is justified. If they are not, I’ll bring the gaps and options instead. I’m not committing to a production tool at that meeting.”

**Maya:** “That gives us something useful to review.”

**Facilitator:** “Who should join to make that decision, and when can we reasonably have the inputs?”

**Coaching:** Name the artifact, input owner, dependency, and next decision. Agree the actual date together; “next time” alone is not a deadline.

**Accumulated output:** draft brief, unresolved definitions, tentative workflow, scope boundary, and action owners. Everything remains fictional rehearsal material here.

## 2. Evidence review

**Purpose:** agree what the data can and cannot support. Use the six records in [stage 2](../02-data-and-quality/README.md).

**Facilitator:** “Today I’d like to check the field meanings first, then the two quality exceptions. That should let us decide which records are ready for prioritisation and what needs correction.”

**Sam:** “A104 has no promised time. A106 was last updated at 07:00.”

**Facilitator:** “At our 09:00 review, that makes A106 two hours old. For the exercise we are using a 30-minute freshness limit. Is that appropriate to the decision, or would a real operation need a different limit?”

**Sam:** “We would have to verify it against source update frequency.”

**Maya:** “Could we fill in the missing time with an average so everything has a score?”

**Facilitator:** “That would create an estimate, not recover the customer's promise. For this version, I propose keeping A104 visible as a data exception. Sam can investigate the missing promise while we rank the four sufficiently current records. Does the team have separate capacity for that data review?”

**Maya:** “For this exercise, yes.”

**Facilitator:** “I’ll document that assumption. If the same dispatcher must handle both queues, we need to revisit the two-investigation limit.”

**Coaching:** Do not hide unknowns to make a dashboard look complete. Negotiate how quality exceptions affect work and capacity.

**Accumulated output:** brief + agreed data definitions to verify + four eligible records + two visible exceptions. Next deliverable: a provisional rule applied to that same snapshot.

## 3. Rule workshop

**Purpose:** test whether an explainable rule produces useful actions; see [stage 3](../03-rules-and-priorities/README.md).

**Facilitator:** “Let’s examine the reasoning before we discuss the interface. In this exercise, we give two points for a promise within 60 minutes, one for not being ready, and two for a carrier exception. These are proposed weights, not a proven predictor.”

**Leo:** “That puts A102 above A101?”

**Facilitator:** “Yes: four points versus three. With two slots we would investigate both. What would make that the wrong choice operationally?”

**Leo:** “A carrier exception could already be resolved even if the feed hasn’t caught up.”

**Facilitator:** “Then the interface needs the evidence time and a way to review changed information before assigning work. We should also test cases where the rule ranks a problem that no one can influence.”

**Maya:** “Can we call the score a likelihood of lateness?”

**Facilitator:** “Not from this rule. It is an investigation priority, not a probability. I’ll label it accordingly and show the reasons.”

**Coaching:** Invite counterexamples. Distinguish a priority score from a calibrated probability and from the benefit of intervention.

**Accumulated output:** prior evidence + ranked queue + caveats + a change to the prototype requirements. Next deliverable: a walkthrough of assigning the two investigations.

## 4. Workflow walkthrough

**Purpose:** turn recommendations into accountable actions; see [stage 4](../04-workflow-and-prototype/README.md).

**Facilitator:** “This is a text prototype, not working software yet. Let’s follow one order from recommendation to follow-up so we can identify missing steps before implementation.”

**Leo:** “I select A102, check the carrier issue, and assign it to the coordinator.”

**Facilitator:** “What must you record so the next shift can understand the action?”

**Leo:** “Owner, reason, and when to follow up.”

**Facilitator:** “And what should happen if someone else assigns the same order at the same time?”

**Leo:** “We shouldn’t create two investigations.”

**Facilitator:** “I’ll add that to the acceptance checks. We also need to recheck the evidence before saving if it changed after you opened the order.”

**Maya:** “Could Assign automatically message the carrier?”

**Facilitator:** “That would add an external action and a new approval process. For this first workflow, Assign records the investigation. We can assess messaging separately once we know who may send what and how mistakes would be corrected.”

**Coaching:** Ask about handoffs, concurrency, and changed information using everyday language. Translate answers into checks that an engineer can implement.

**Accumulated output:** earlier artifacts + action fields + duplicate/stale-data checks + explicit messaging boundary.

## 5. Adoption conversation

**Purpose:** find out whether someone can use the proposed workflow; see [stage 5](../05-demo-and-adoption/README.md).

**Facilitator:** “I’d like you to try choosing two investigations without me guiding each step. We’re testing whether the design is clear, not testing you. Please say what you’re looking for as you go.”

**Leo:** “I don’t see a score for A104. Does that mean it’s fine?”

**Facilitator:** “What on the page gave you that impression?”

**Leo:** “The scored orders look like the important ones.”

**Facilitator:** “That suggests the exception section needs to be more prominent. I’ll record the confusion and revise the wording, then repeat this task rather than assume the explanation fixed the design.”

**Maya:** “Could training solve it?”

**Facilitator:** “Training may help, but a missing promise should not look safe by default. Let’s improve the design and then see what training is still needed.”

**Coaching:** Avoid teaching the user the answer before observing the problem. This dialogue illustrates a possible observation; it is not a recorded test result.

**Accumulated output:** in a real session, an observed task log and a revision with a reason. In this repository, those remain a practice script and planned exercise.

## 6. Pilot review

**Purpose:** agree what evidence would support continued investment; see [stage 6](../06-pilot-and-impact/README.md).

**Maya:** “If on-time delivery goes from 90% to 95%, can we say the workflow improved it?”

**Facilitator:** “That is a five-percentage-point change, but we would need the counts, comparable periods, and context before attributing it to the workflow. Did staffing, order mix, or capacity change? In our case those percentages are only illustrative arithmetic, not measured pilot results.”

**Maya:** “What can we reasonably test first?”

**Facilitator:** “First, whether users choose and assign valid investigations faster without increasing unnecessary escalations. We can run a shadow review before changing operations, then agree a limited pilot if the recommendations are actionable. We should define the baseline, observation period, and stop criteria before we see the results.”

**Leo:** “We could finish the review faster but overwhelm the carrier coordinator.”

**Facilitator:** “Exactly. Added workload belongs alongside speed as a guardrail. Who can help define an acceptable limit?”

**Coaching:** Translate “prove impact” into a design for measuring it. Faster activity is not automatically a better operational outcome.

**Accumulated output:** pilot plan, metric definitions, unresolved thresholds, and owners. No actual impact claim.

## 7. AI and handoff

**Purpose:** decide the next investment using the accumulated evidence; see [stage 7](../07-ai-decision-and-handoff/README.md).

**Maya:** “When do we add a model?”

**Facilitator:** “When we have enough historical snapshots and outcomes to evaluate whether it improves this decision beyond the rule. These six examples let us discuss the workflow; they are not enough to validate a model. We also need to distinguish orders likely to be late from orders where investigation can actually help.”

**Sam:** “What should we prepare next?”

**Facilitator:** “A data-availability assessment: which review-time features and later outcomes exist, whether timestamps are reliable, and how interventions are recorded. In parallel, we can finish the non-AI prototype acceptance checks. At the next decision point, I can bring feasibility findings and an evaluation proposal—not promise a trained model.”

**Maya:** “So what do we have at the end of this case?”

**Facilitator:** “A scoped decision, sample-data findings, a transparent rule, a workflow specification, and plans for adoption and evaluation. We have not yet built the application or run a pilot. My recommendation is to validate the workflow and data before committing to AI.”

**Coaching:** Close with a recommendation, its evidence, its limitations, and a concrete next deliverable. A useful next decision matters more than an impressive-sounding feature promise.

[Conversation map](README.md) · [Talking-point playbook](TALKING-POINTS.md)
