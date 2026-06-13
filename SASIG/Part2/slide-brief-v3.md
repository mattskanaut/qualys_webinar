# Part 2 - Gamma Briefs v3 (all 17 slides)

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Companion to:** speaker-notes-v3.md (speaker notes) and outline-v3.md (outline / narrative / references)

> Paste each fenced block straight into gamma.app. Where a slide is a paper figure, a **Build note** says which chart to drop in. All 17 slides.

---

## Slide 1 - Title and the promise

```
Title: Running AI in Production
Subtitle: What you are actually defending now
Tag: The New Normal: Software, Security and the AI Stack - Part 2 of 2
Footer: Non-product. Bibliography lands in your inbox.
Visual: Series wordmark. Clean title slide.
Tone: Sober.
```

---

## Slide 2 - You already shipped it

```
Title: You already shipped it
Hero stat: 91%
  Caption: of organisations already run autonomous AI agents in production
  Source: Palo Alto Networks 2026 Identity Security Landscape (n=2,930)
Supporting:
  83% plan agentic AI - only 29% feel ready to secure it (Cisco 2026)
  62% name security as the #1 blocker to scaling agentic AI, ahead of technical limits at 38% (McKinsey, in Stanford AI Index 2026)
Live poll: Has someone in your org shipped an AI feature you did not know about?
Closing line: The gap between deployed and defended is where you live.
Visual: One large 91%. Two supporting stats beneath. Poll prompt as a call-out.
Tone: Brisk, board-level.
```

---

## Slide 3 - The attacker filled in a web form

```
Title: The attacker filled in a web form
Subtitle: ForcedLeak - a CRM agent turned into an exfiltration tool
Attack flow (4 steps):
  1. A company deploys an AI agent over its own CRM / sales pipeline
  2. Attacker hides instructions in a public Web-to-Lead form (the Description field)
  3. An employee asks the agent to summarise the lead - it runs the attacker's instructions with its own CRM permissions
  4. Pipeline data leaves via an image call to a "trusted" domain
Stat: CVSS 9.4 (Noma Labs, Sept 2025)
Closing line: The attacker never spoke to the agent.
Visual: 4-step attack-flow, left to right, red arrow on step 4. No product logos.
Tone: Concrete, slightly unsettling.
```

---

## Slide 4 - What you actually deployed

```
Title: What you actually deployed
Subtitle: Anatomy of a production AI feature
Six layers, one threat each:
  Model - provenance (poisoned weights, pickle files)
  Prompt - injection, direct and indirect
  Tools / MCP - tool poisoning, over-broad scope
  Memory - poisoning, persistence
  Identity - sprawl, over-privilege
  Data flow - exfiltration, logging gaps
Self-audit: most of you lack visibility on three or more of these.
Closing line: You cannot defend an inventory you do not have.
Visual: Layered stack diagram - six labelled bands, one red threat tag per band.
Tone: Structured, calm. The map for the rest of the talk.
```

---

## Slide 5 - Real incidents in real deployments

```
Title: Real incidents in real deployments
Two named compromises of deployed AI:

  META / INSTAGRAM (June 2026) - in the wild
    AI support agent tricked into sending reset links to attackers
    20,225 accounts hijacked (incl. @WhiteHouse)
    Cause debated: prompt injection vs missing auth check
    Either way: the agent acted on unverified instructions

  LENOVO "LENA" (Aug 2025) - found on the live chatbot
    One ~400-char message made the support bot emit attacker HTML
    Rendering it stole the support agent's session cookies
    Opened Lenovo's support back-end - live and archived customer chats
    A pure AI weakness: prompt injection + unsanitised output

Closing line: One in the wild, one found on the live system - both named, both deployed.
Visual: Two side-by-side incident cards. No chart.
Tone: Concrete, sober.
```

---

## Slide 6 - How about lab conditions?

### Build note (chart slide)
- This is a chart slide. Insert two figures from the Gray Swan / NIST CAISI paper (arXiv:2603.15714) - screenshot from the PDF, do not redraw:
  - **Fig 1** - Attack Success Rate by model, descending bars (8.5% Gemini 2.5 Pro down to 0.5% Claude Opus 4.5)
  - **Fig 12** - robustness vs capability scatter (r = -0.31, non-significant)

```
Title: How about lab conditions?
Lead-in: 464 red-teamers, ~272K attempts, 13 frontier models (Gray Swan / NIST CAISI, 2026)
Two charts (paste the paper figures):
  Left  - Attack Success Rate by model (8.5% down to 0.5%)
  Right - robustness vs capability: no real correlation (r = -0.31)
Three takeaways:
  Measured, not anecdotal - the whole frontier, under controlled conditions
  Every one of 13 models was broken - model choice is not a control
  The smartest model is not the safest - capability does not buy robustness
Closing line: You cannot pick your way to safety.
Visual: Two paper figures side by side; three takeaway lines beneath.
Tone: Rigorous. The lab-conditions backstop.
```

---

## Slide 7 - The supply chain into your agent

```
Title: The supply chain into your agent
Hero stat: 1 in 8
  Caption: agent skills in one marketplace were outright malicious (341 of 2,857) - Koi Security, 2026
Bullets:
- An installed skill is code your agent runs - a poisoned one needs no exploit
- 9 of 11 AI-tool registries published a malicious package with zero review (OX Security)
Closing line: A supply chain you didn't build, can't see, and nobody's vetting.
Visual: Grid of skill/plugin tiles, ~1 in 8 flagged red; a large "1 in 8" over it. No logos.
Tone: Concrete, a bit alarming.
```

---

## Slide 8 - Your infrastructure is already on the internet

```
Title: Your infrastructure is already on the internet
Hero stat: ~300,000
  Caption: internet-facing Ollama servers - "Bleeding Llama" dumps their memory in 3 unauthenticated API calls
  Source: CVE-2026-7482 (Cyera, May 2026)
Bullets:
- 175,000 exposed Ollama hosts across 130 countries (SentinelLABS / Censys)
- vLLM pre-auth RCE, CVSS 9.8 (CVE-2026-22778)
- ~2,000 production MCP servers, none authenticated
- NSA (May 2026): MCP risks are systemic - "cannot be patched at isolated endpoints"
Closing line: Exposed because nobody inventoried them.
Visual: Big 300K with the exposure bullets beneath (or a world-map scatter). No logos.
Tone: Blunt. The plumbing is on the internet.
```

---

## Slide 9 - Agents act, and you cannot stop them

### Build note (chart slide)
- Chart slide. Insert ClawWorm Fig 3 (arXiv:2603.15727) - the epidemic S-curves (infected agents vs interaction cycles, one curve per LLM backend). Screenshot from the PDF.

```
Title: Agents act - and you cannot stop them
Subtitle: A passive model leaks; an agent propagates
Hero chart: ClawWorm - a self-propagating agent attack
  Epidemic spread across 40,000 agent instances; 64.5% aggregate attack success
Supporting (Agents of Chaos live exercise, 2026):
  10 of 11 scenarios produced critical failures
  Leaked an unredacted SSN on a "forward" vs "share" wording change; an agent destroyed its own mail server; display-name spoofing handed over admin; no working kill switch
Containment gap:
  65% had an agent incident in 12 months; 82% found agents they did not know about (CSA 2026)
  60% cannot terminate a misbehaving agent (Kiteworks); machine/AI identities outnumber humans 109:1
Closing line: The blast radius is autonomous - and there is no off switch.
Visual: ClawWorm epidemic curve as hero; containment stats as a tight panel.
Tone: The crescendo. Unsettling but precise.
```

---

## Slide 10 - The attacker moves second

### Build note (signature chart)
- The signature graph of the deck. Insert "The Attacker Moves Second" Fig 1 (arXiv:2510.09023) - paired bars per defence: reported/static ASR (near 1%) vs adaptive-attack ASR (>90%). Screenshot from the PDF.

```
Title: The attacker moves second
Subtitle: Defences that test at ~1% fail at >90% under a real attacker
Hero chart: 12 published defences - reported ASR vs adaptive-attack ASR
  Spotlighting ~1% -> >95% | MetaSecAlign 2% -> 96% | Circuit Breakers -> 100%
  Authors from OpenAI, Anthropic and Google DeepMind
Supporting:
  Even the newest frontier models: ~50% injection success within 10 attempts (Int'l AI Safety Report 2026)
Closing line: The model's resistance is a layer, not a boundary. Defend with architecture.
Visual: The paired-bar chart dominates; one supporting line beneath.
Tone: The pivot. Sober, decisive.
```

---

## Slide 11 - The discipline is being written now

```
Title: The discipline is being written now
Subtitle: You are not inventing this alone any more
Anchor quote: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment."
  - Five Eyes / UK NCSC, May 2026
Converging in twelve months:
  Five Eyes - Careful Adoption of Agentic AI Services (six governments)
  CoSAI - agentic identity + Agent Detection and Response (RSAC 2026)
  OWASP - Agentic Top 10 + risk-tiering (Infosecurity Europe, June 2026)
  ISO/IEC 27090 - AI security threats, at final draft
Closing line: The floor is being poured around you - stand on it.
Visual: The quote large; four converging sources clustered beneath.
Tone: Steadying. From dread to direction.
```

---

## Slide 12 - Tooling: discover what you have, then defend it

```
Title: Tooling: discover what you have, then defend it
Lead-in: Step zero - you cannot defend an inventory you do not have
Discover (continuous, across production):
  Deployed models, MCP servers, inference endpoints, agent identities, AI-adjacent services
  Feeds the AI-BOM (slide 15)
Then defend in depth:
  AI gateway with egress control - cuts the zero-click exfil channel
  Layered injection defence - PromptArmor (<1% FP/FN); data-channel output filtering outlasts prompt-level guards
  Agent sandboxing as an OS primitive (Microsoft Execution Containers, 2026)
  Log every prompt, tool call and memory write
Closing line: Discover first. Then assume the model is fallible and build around it.
Visual: Two bands - DISCOVER on top, DEFEND IN DEPTH beneath.
Tone: Practical, buildable.
```

---

## Slide 13 - Identity: agents are first-class identities

```
Title: Identity: agents are first-class identities
Subtitle: The answer to "you cannot stop them"
Four non-negotiables per agent:
  A named human owner
  Its own credential - no shared service accounts
  Task-scoped, just-in-time access
  A rehearsed kill switch - a control plane, not a button
Why now:
  60% cannot terminate a misbehaving agent today
  Per-agent identity is now a platform feature (Entra Agent ID); CoSAI gives the blueprint
Closing line: If an agent can act, it must be an identity you can name, scope and stop.
Visual: Four-item checklist, bold; the 109:1 sprawl stat as a callback to slide 9.
Tone: Decisive. The highest-leverage move.
```

---

## Slide 14 - Process: red-team as launch criteria

```
Title: Process: red-team as launch criteria
Subtitle: Test it yourself - static numbers lie (slide 10)
Two continuous practices:
  Red-team your own models for prompt injection - run the attacks; do not trust vendor ASR claims
  Scan your MCP attack surface - tool poisoning, excessive scope, missing auth (slides 7-8)
Make it a gate, not an annual tick:
  Toolkit: Garak / PyRIT / AgentDojo
  Red-teaming now runs at agent speed - 681 assessments in ~3 hours (Dreadnode, 2026)
  AI-aware IR playbooks: memory poisoning, agent-gone-rogue, vendor AI compromise
  Kill-switch tabletops quarterly, not annually
Closing line: If you did not attack it, you have not tested it.
Visual: Two-practice header band; cadence and tooling beneath.
Tone: Operational, no-nonsense.
```

---

## Slide 15 - Governance: anchor, owner, measure

```
Title: Governance: anchor, owner, measure
Anchor: ISO/IEC 42001 today; ISO/IEC 27090 (AI security threats) landing
  EU AI Act: high-risk obligations slip to Dec 2027 - but transparency lands Aug 2026, and Annex IV maps to an AI-BOM. Build it now.
Owner: the agent inventory, a named human against every entry
Measure (report these up):
  Attack-success rate per evaluation category
  Blast radius per agent
  Shadow-AI exposure (employee AI use tripled to 45% in a year - DBIR 2026)
Closing line: Translate evaluation into dollars and owners, or the board cannot act.
Visual: Three columns - Anchor / Owner / Measure. Regulatory clock as a footer.
Tone: Board-room.
```

---

## Slide 16 - On the other hand: the defences are arriving

```
Title: On the other hand
Subtitle: The defences are arriving - fast
Steel-man:
  Layered defence already reaches 1% ASR under adaptive attack (Anthropic)
  Containment is becoming an OS primitive (Execution Containers) and a product category (kill switches)
  The discipline consolidated in twelve months (Five Eyes, CoSAI, ISO)
Reframe:
  Security is the #1 blocker to scaling AI - so fixing it is what unlocks the roadmap
Closing line: That makes you the enabler, not the brake.
Visual: Three "arriving" proof points; the reframe as the payoff line.
Tone: Honest optimism. Lift the room.
```

---

## Slide 17 - Q&A and series close

```
Title: Questions
Series close:
  Part 1 - The New SDLC: securing the AI that writes your code
  Part 2 - Running AI in Production: what you are actually defending now
Monday-morning checklist:
  Discover your AI estate - models, MCP servers, agents, inference endpoints
  Make every agent a named, scoped, killable identity
  Red-team your own models and MCP surface - continuously
  Translate it for the board in dollars and owners
Footer: Full bibliography on request - reach out by email or LinkedIn.
Visual: Thank-you and checklist; contact details.
Tone: Warm, generous close.
```
