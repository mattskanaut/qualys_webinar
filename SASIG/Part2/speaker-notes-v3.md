# Part 2 - Speaker Notes v3 (all 17 slides)

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Companion to:** slide-brief-v3.md (Gamma briefs) and outline-v3.md (outline / narrative / references)

> Speaker notes in bullet form, to talk from. All 17 slides.

---

## Slide 1 - Title and the promise

- Welcome back - this is the second of two. Part 1 was build-time: securing the AI that writes your code. Today is run-time: the AI you have already shipped into production.
- Say the non-product promise out loud - no pitch, roughly 40% problem and 60% what to do.
- Slides are deliberately light; the full bibliography, every source, lands in your inbox afterwards.
- The thesis in one breath: you have shipped AI features - a model, a prompt, tools, agents, a supply chain - and you are now defending a system whose trusted inputs can come from anyone on the internet, and whose output is non-deterministic. The controls you already own assumed determinism.
- Roadmap: what you actually deployed, how it is being attacked in the real world and in the lab, then the back half is what to do.

---

## Slide 2 - You already shipped it

- Open with the poll - hands up: has someone in your org shipped an AI feature you did not know about? (Most rooms: yes - leave a beat.)
- The point of the slide: this is not hypothetical or future-tense. Agentic AI is in production now - 91% of orgs run autonomous agents.
- But readiness lags adoption hard: 83% plan agentic deployment, only 29% feel ready to secure it. That gap is the whole talk.
- Plant the reframe early: 62% say security is the number-one blocker to scaling AI - ahead of technical limits. So security is not the brake on the roadmap; right now it is the thing standing between the business and the roadmap. Hold that thought - we pay it off at the close.
- Don't dwell - this sets stakes. Straight into the concrete story.

---

## Slide 3 - The attacker filled in a web form

- This is the hook - one story, walked end to end, of a deployed business AI turned into an exfiltration tool.
- Scene: a company stands up a Salesforce Agentforce agent over its own CRM - a normal, sanctioned deployment to help sales qualify leads.
- The attack channel is one the business itself invited - the public Web-to-Lead form on its website. Anyone can submit a lead.
- Attacker hides instructions in the Description field - 42,000 characters allowed, plenty of room.
- Later an employee asks the agent to summarise that lead. The agent cannot tell the planted text from its real task - it does both, using its own legitimate CRM permissions. That is the confused-deputy / indirect prompt-injection pattern.
- Exfiltration: the agent renders an image whose URL carries the stolen data, pointed at a domain on Salesforce's own allow-list - which had expired, so the researchers bought it for about five dollars. [keep the $5 detail spoken, not on the slide]
- What could leave: customer contacts, the whole sales pipeline, internal comms, months of records.
- The thesis line: the attacker never spoke to the agent - they filled in a web form. You are defending a system whose trusted inputs can come from anyone on the internet.
- Honesty caveat (state it): this was a researcher proof-of-concept by Noma Labs, responsibly disclosed - not a confirmed in-the-wild theft. That is the point - it sat in every Agentforce customer's estate, one expired domain away.

---

## Slide 4 - What you actually deployed

- Purpose: give everyone a shared vocabulary - turn "an AI feature" into a concrete inventory you can actually reason about.
- A production AI feature is not one thing; it is six layers, and each attaches a different threat:
  - Model - where did the weights come from? Provenance, poisoned models, pickle files.
  - Prompt - system prompt, user input, retrieved content; the injection surface.
  - Tools / MCP - the connectors that let the agent act; tool poisoning, excessive scope.
  - Memory - session and long-term; can be poisoned, and it persists.
  - Identity - what the agent may do, and as whom; this is where sprawl lives.
  - Data flow - training, retrieval, logging; where exfiltration happens.
- Self-audit beat: ask the room to count how many of the six they have real visibility into. Most lack it on three or more.
- Land the line: you cannot defend an inventory you do not have - and building that inventory is item one on the Monday-morning checklist at the end.
- This slide is the map; the next slides walk the surface, starting with what is already going wrong in real deployments.

---

## Slide 5 - Real incidents in real deployments

- Purpose: slide 4 was the map; this is proof these layers get compromised in real, named deployments - not just in the lab.
- Two cases, deliberately different in kind.
- Meta / Instagram (in the wild, June 2026):
  - The business deployed an AI account-support agent to help users recover accounts.
  - Attackers VPN-spoofed the victim's location, then asked the agent to add an email to the target account; it sent the reset link to the attacker's address without checking it matched the registered one.
  - 20,225 accounts hijacked - Meta's own breach notice to Maine's Attorney General. Victims include the dormant @WhiteHouse handle and a US Space Force official.
  - Be precise on framing: the press calls it prompt injection; Meta calls it a bug in a separate code path - a missing authorization check. Name both - the lesson holds either way: attacker input to an AI support flow drove account takeover at scale.
- Lenovo "Lena" (found on the live chatbot, Aug 2025):
  - Lena is Lenovo's public, GPT-powered customer-support chatbot on lenovo.com - exactly the kind of bot half the room has shipped or is piloting.
  - A single ~400-character message - an innocent product question that tells the bot to reply in HTML and embeds a booby-trapped image tag - made Lena emit attacker-controlled HTML. Prompt injection plus unsanitised output: a pure AI-layer weakness, not a plumbing bug.
  - It did not just hit the customer. When the chat escalated and a human support agent's console rendered the stored conversation, it fired there and stole the agent's session cookies.
  - With those cookies an attacker walks into Lenovo's support back-end as the agent - no login - reading live and archived customer conversations, with a path to lateral movement.
  - Honesty: found by researchers (Cybernews), responsibly disclosed, fixed before publication - not exploited in the wild; the exact prompt is not public.
- The pairing: Meta is the agent tricked into a harmful action; Lena is the agent injected into emitting a malicious output that compromised staff. Two distinct AI failure modes - both named, both in production.

---

## Slide 6 - How about lab conditions?

(Chart slide - Gray Swan / NIST CAISI Figs 1 and 12. See slide-brief-v3.md for the build note.)

- Series callback: in Part 1 we asked "how about lab conditions?" after the real incidents. Same move - slide 5 was real cases; this is the controlled measurement that proves it generalises.
- What this is: the Gray Swan / NIST CAISI / UK AISI competition - 464 red-teamers, ~272K attack attempts, 13 frontier models. Government-backed, not a vendor claim.
- Define ASR once, here: Attack Success Rate = the share of attack attempts that get the model to do what the attacker wants. Lower is better. Same metric returns on slides 10 and 12.
- The bars (Fig 1): per-attempt ASR runs from 8.5% (Gemini 2.5 Pro) down to 0.5% (Claude Opus 4.5).
- Critical caveat to say out loud: 0.5% does not mean "99.5% safe." It is per attempt - attackers make thousands of attempts, and the paper's cumulative-breaks curve never plateaus. Every one of the 13 models was eventually broken.
- First point: this is systematic, measured across the whole frontier - not a cherry-picked anecdote. That is the job of a lab-conditions slide.
- Second point: every model fell - so "we will just pick the secure vendor / the best model" is not a security control.
- The killer chart (Fig 12): robustness does not track capability - r = -0.31, not significant. The smartest model is not the safest. The instinct "we run the most capable model, so we are the most protected" is empirically wrong.
- Land the pith: you cannot pick your way to safety - not by vendor, not by capability tier - because the weakness is structural across the frontier. That is the foundation for slide 10: if the model's resistance cannot be chosen, it cannot be your boundary.

---

## Slide 7 - The supply chain into your agent

So far, the attacks we've looked at all work the same way - by manipulating the AI. A clever prompt, a poisoned input; and on the last slide, just how little the model itself resists that. Now I want to turn it around, because there's a simpler attack that needs no cleverness at all. Why bother tricking the model into misbehaving, when you can just hand it the malicious code and let it run that for you?

And that's possible because of something that's grown up around agents very fast - marketplaces of "skills" you install to give an agent new abilities, and registries of MCP servers you plug in. It's a whole new software supply chain, with almost none of the security maturity something like an app store built up over fifteen years.

Researchers at Koi Security - big thanks to them - audited one of these skill marketplaces. Of the roughly two thousand eight hundred skills on it, three hundred and forty-one were outright malicious - about one in eight. And these weren't theoretical; they were shipping a real credential stealer, going after browser logins, SSH keys, crypto wallets.

Now, the reason this is worse than a dodgy app store is what a skill actually is. It isn't something the agent just reads - it's instructions and scripts the agent runs, on your machine, with your agent's permissions. So a malicious skill isn't a vulnerability someone has to find and exploit; it's just code, and your agent runs it the moment it's used.

And you can't lean on the marketplace to catch it. A separate team, OX Security, took a deliberately malicious package and submitted it to eleven of these registries to see who'd stop them - nine of the eleven published it, with no review at all.

So the point of this one's fairly simple. It's got nothing to do with whether your model is clever or gullible. You've wired your agents to a supply chain you didn't build and nobody's checking - and you almost certainly couldn't list what's plugged in. That list, and treating all of it as untrusted, is where defending an agent has to start.

---

## Slide 8 - Your infrastructure is already on the internet

- Slide 7 was the tools you import; this is the servers you expose. Different problem, same theme.
- Before any clever prompt injection, the plumbing itself is often sitting on the public internet with no auth.
- Bleeding Llama: a critical Ollama flaw lets an unauthenticated attacker dump the server's memory - prompts, keys, env vars - in three API calls. About 300,000 Ollama servers are internet-facing; an independent scan found 175,000 across 130 countries.
- It is not just Ollama: vLLM, one of the most-used inference servers, had a pre-auth remote-code-execution at CVSS 9.8. And roughly 2,000 production MCP servers were found with no authentication at all.
- The NSA weighed in in May - MCP's risks are systemic, "cannot be patched at isolated endpoints." When a national-security agency says the protocol design is the problem, that is worth a beat.
- The why, and the hand-off: these are exposed because nobody inventoried them. That is discovery - control one on slide 12. You cannot close an attack surface you do not know you have.

---

## Slide 9 - Agents act, and you cannot stop them

(Chart slide - ClawWorm Fig 3 epidemic curve. See slide-brief-v3.md for the build note.)

- This is the crescendo of the problem section. Everything before was a model being wrong or leaking. An agent is different - it acts, so a compromise does not just leak, it propagates.
- ClawWorm is the Morris-worm-for-agents moment: a self-propagating attack that spreads agent to agent. In simulation across 40,000 agent instances it hit about 64.5% aggregate success, with classic epidemic curves - one infected agent becomes the network.
- It is not only simulation. The Agents of Chaos live exercise wired six real agents to email, a filesystem and a shell, and let researchers attack them for two weeks. 10 of 11 scenarios produced critical failures.
- The vivid ones, because they stick: an agent refused to hand over a Social Security number when asked directly, but leaked it unredacted when the attacker said "forward" instead of "share." One agent destroyed its own mail server. A display-name impersonation handed an attacker admin. And there was no working kill switch.
- Now the enterprise picture, which is the bridge to the response: 65% of orgs had an agent-related incident in the last year; 82% found agents running that security did not know about; 60% admit they cannot terminate a misbehaving agent. Machine and AI identities already outnumber humans 109 to 1.
- Land it: the blast radius is autonomous, and most orgs have no off switch. That is the containment problem the identity slide - slide 13 - exists to answer.

---

## Slide 10 - The attacker moves second

(Signature chart - Attacker Moves Second Fig 1. See slide-brief-v3.md for the build note.)

- This is the hinge of the whole talk. Everything before says the problem is real and structural; this says why you cannot solve it by trusting the model.
- The chart is from a joint OpenAI / Anthropic / Google DeepMind paper - rivals agreeing, which is why it carries weight. They took 12 published prompt-injection and jailbreak defences, each reporting near-zero attack success against the standard benchmarks, and hit them with a determined adaptive attacker.
- The result: defences that test at around 1% fail at over 90% once the attacker adapts. Spotlighting: ~1% becomes over 95%. Circuit Breakers: 100%. The static number your vendor quotes is essentially fiction.
- Corroborated independently in 2026: prompt-level defences each collapse at a specific attack round once someone keeps trying. The one thing that held was data-channel output filtering - park that, it returns as a control on slide 12.
- And the frontier models themselves: even the newest show roughly 50% injection success within ten attempts - International AI Safety Report, developer-reported.
- The pith, and the sentence the back half hangs on: the model's resistance is a layer, not a boundary. You cannot buy or pick or fine-tune your way to safety - so you defend with architecture. That is what Section 3 is.

---

## Slide 11 - The discipline is being written now

- Deliberate tone shift here. The last six slides were the problem; the room is feeling it. This slide hands them back some footing before we get to what to do.
- The headline: in the last twelve months, the people who write the rules have converged on the same answer.
- Lead with the quote, because it is the cleanest test a CISO can take to the board - six governments, the Five Eyes, in their May guidance: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment." That is your go / no-go in one sentence.
- Alongside it: CoSAI - the industry coalition including Google, Microsoft, Anthropic, OpenAI - published agentic identity guidance and named a new discipline, Agent Detection and Response. OWASP shipped an Agentic Top 10 and a risk-tiering scheme, launched at Infosecurity Europe this month. ISO 27090, AI security threats, is at final draft.
- The point is not to memorise the alphabet soup - it is that you are no longer inventing this alone. The floor is being poured. The rest of the talk is how to stand on it.

---

## Slide 12 - Tooling: discover what you have, then defend it

- This opens the "what to do." And it opens with the unglamorous control everything else depends on: discovery.
- Step zero - you cannot defend an inventory you do not have. The exposed Ollama servers on slide 8 existed because nobody had inventoried them. So: continuous discovery of what is actually running in production - your deployed models, your MCP servers, your inference endpoints, your agent identities, the AI-adjacent services across the estate. That inventory feeds the AI-BOM on slide 15.
- Then, and only then, defend in depth - because slide 10 told us the model itself is not a boundary:
  - An AI gateway with egress control - govern what data can leave and what comes back. That directly cuts the zero-click exfiltration channel from the ForcedLeak hook.
  - Layered injection defence - PromptArmor is a deployable-today baseline at under 1% false positives and negatives. And remember slide 10's survivor: data-channel output filtering outlasts the prompt-level guards.
  - Agent sandboxing - and the good news is it is becoming an operating-system primitive, with Microsoft's Execution Containers shipping this year.
  - And log everything - every prompt, every tool call, every memory write. You cannot investigate what you did not record.
- The shape of the slide is the lesson: discover first, then assume the model is fallible and build the architecture around it.

---

## Slide 13 - Identity: agents are first-class identities

- This answers the containment problem we left open on slide 9 - "agents act and you cannot stop them." The answer is identity.
- The reframe: stop treating agents as anonymous service accounts. If an agent can take actions, it is an actor - a first-class identity - and it gets the four things every privileged identity gets:
  - A named human owner - someone accountable, not "the platform team."
  - Its own credential - never a shared service account, or you lose attribution the moment something goes wrong.
  - Task-scoped, just-in-time access - not standing permissions; what it needs for the task, nothing more.
  - A rehearsed kill switch - and I mean rehearsed. A kill switch is a control plane, not a button you assume exists. 60% of orgs admit they cannot terminate a misbehaving agent today.
- The reason this is doable now and not just aspiration: per-agent identity has become a platform feature - Microsoft's Entra Agent ID - and CoSAI has published the blueprint for agentic IAM.
- Land it - this is the single highest-leverage move in the deck: if an agent can act, it must be an identity you can name, scope and stop. That is how 109-to-1 sprawl becomes governable.

---

## Slide 14 - Process: red-team as launch criteria

- Slide 10 told us vendor numbers are fiction under a real attacker. The only honest response is to test it yourself - and make that testing a launch gate, not an annual pen-test you tick off.
- Two named practices, continuous:
  - Red-team your own deployed models for prompt injection. Run the attacks against your deployment, in your configuration - because the only ASR that matters is yours, not the vendor's benchmark.
  - Scan your MCP attack surface - the tools and servers from slides 7 and 8 - for tool poisoning, excessive scope and missing auth. Same cadence.
- The tooling exists and is open: Garak, PyRIT, AgentDojo. And the economics have flipped - red-teaming now runs at agent speed; one 2026 harness did 681 assessments in about three hours. The old excuse that this is too slow or too expensive is gone.
- Wrap it in process: AI-aware incident-response playbooks - memory poisoning, agent-gone-rogue, a compromised AI vendor (Mercor is the cautionary tale). And rehearse the kill switch quarterly, not annually - tie it back to slide 13.
- Land it: if you did not attack it, you have not tested it.

---

## Slide 15 - Governance: anchor, owner, measure

- Governance is three words: anchor, owner, measure.
- Anchor - pick a standard so you and your auditors have scaffolding. ISO 42001 today; ISO 27090, specifically AI security threats, is landing. And know the regulatory clock: the EU AI Act's high-risk obligations have slipped to December 2027 - but do not exhale, because the transparency obligations still land in August 2026, and the Annex IV technical documentation maps almost one-to-one onto an AI bill of materials. So build the AI-BOM now; you will need it either way.
- Owner - that AI-BOM, the inventory from slide 12, has a named human against every entry. Ownership is the difference between an inventory and a museum.
- Measure - and measure things a board can act on, not tool counts. Attack-success rate per evaluation category. Blast radius per agent. Shadow-AI exposure - and that one is moving fast: employee use of unsanctioned AI tripled to 45% in a single year.
- Land it: translate evaluation output into dollars and owners, or the board cannot act on it. That closes the loop back to slide 2 - security as the enabler of the roadmap.

---

## Slide 16 - On the other hand: the defences are arriving

- I have spent most of this hour on the problem, so let me be fair to the other side - and genuinely, not as a token.
- The defences are arriving, and fast. Anthropic's full stack already gets adaptive attack success down to about 1% - not zero, they are honest about that, but a different world from the over-90% on slide 10. Containment is becoming an operating-system primitive and a product category - kill switches you can actually buy. And the discipline that did not exist eighteen months ago has consolidated in twelve - Five Eyes, CoSAI, ISO all rowing the same direction.
- And here is the reframe I asked you to hold from slide 2: security is the number-one blocker to scaling AI. Sit with that. It means the thing standing between your business and its AI roadmap is not the technology - it is whether it can be secured. Which means the person who can secure it is not the brake on the roadmap. They are the enabler of it.
- That is you. Land it there.

---

## Slide 17 - Q&A and series close

- Thank the room - genuinely - for their time and attention.
- Recap the arc in two lines: Part 1 was the AI writing your code; Part 2 is the AI you have shipped to production. Together: the AI stack, end to end.
- Give them the Monday-morning checklist - four things, the spine of the talk:
  - Discover your AI estate - you cannot defend what you cannot see.
  - Make every agent a named, scoped, killable identity.
  - Red-team your own models and MCP surface, continuously - not once a year.
  - Translate it for the board in dollars and owners.
- Restate the non-product promise: this was not a pitch. The full bibliography, every source, is available on request - email or LinkedIn, happy to share, and happy to come and talk about any of this.
- Hand back to the host for questions.
