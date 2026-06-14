# Outline v4 - mirrored to the reordered deck, problem cluster trimmed

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot. ~38 min content + 10 min Q&A + 5 min host preamble.
**Slide count:** 16
**Last synced to `Running-AI-in-Production.pptx`:** 2026-06-14

**Structural shift from v3:** Three changes, driven by deck work on 2026-06-14.
(1) **Two architecture-primer slides split out** - the deck now teaches "System
anatomy" (model/harness/MCP, the same-channel fact) and "Autonomous agents" (who
drives the loop) as their own slides before the six-layer inventory, where v3
compressed them. (2) **The problem cluster is trimmed** - old deck slides 10
(infra exposed), 11 (agents act, you cannot stop them) and 12 (attacker moves
second / "a number is not a posture") were CUT to stop the problem half running
to seven consecutive stat-heavy slides; the problem half now ends on the supply
chain. (3) **The back half renumbered down** and the discipline slide retitled
"You're not inventing this alone anymore" and promoted to carry the problem ->
solution bridge straight off the supply-chain slide.

**Sourcing exceptions (pre-2026, retained by agreement):**
- **Anthropic 1%-ASR result (Nov 2025)** - slide-15 candour beat ("1% still
  represents meaningful risk"); PromptArmor (ICLR 2026) carries the 2026 on-slide
  defence cite alongside it.
- **The Attacker Moves Second (Oct 2025)** - no longer on a slide (its slide was
  cut) but retained in Q&A reserve; verified this session.

> Each slide carries its **Outline** (the content), **Narrative** (what it is
> doing and how it moves the story), and **References** (sources likely to be
> cited). Tags: (P) primary, (2) secondary/press, (chart) figure to screenshot at
> build time; **VERIFY** = still needs a primary-source check before going live.

### Slide 1 - Title and the promise  *(Open)*
**Outline:** Title slide. Non-product, 40/60. Bibliography by email. Part 1 was build-time; today is what you are defending once it ships - a system whose inputs come from anyone and whose output is non-deterministic.

**Narrative:** Opens the session and re-establishes the non-product compact that earned the room in Part 1. Positions Part 2 against Part 1 - build-time is behind us; this hour is about the AI you have already put into production - so the audience knows exactly what lens to bring. Heavy caveat up front: things move fast, no simple answers.

**References:** None (title slide).

### Slide 2 - It's already out there  *(Open)*
**Outline:** Hero: 99% of organisations already run autonomous AI agents in production (Palo Alto Networks 2026). 83% plan agentic AI; only 29% feel ready to secure it (Cisco 2026). 62% name security as the PRIMARY blocker to scaling agentic AI, ahead of technical limits (38%) - McKinsey via Stanford AI Index 2026. Live poll: has someone in your org shipped an AI feature you did not know about?

**Narrative:** Establishes that this is not hypothetical: agentic AI is deployed faster than it is secured, and the audience is sitting in that gap. The deployed/ready split and "security is the primary blocker" quietly frame security as the thing standing between the business and its roadmap - a thread the close pays off. The poll seeds the discovery spine that recurs on slides 5 and 9.

**References:**
- Palo Alto Networks 2026 Identity Security Landscape (run agents in production; 109:1) (P, **VERIFY** the on-slide 99% - v3 sourced 91% from this report): https://www.paloaltonetworks.com/idira/identity-security-landscape-report
- Cisco State of AI Security 2026 (83% plan / 29% ready) (P): https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report
- Stanford AI Index 2026 (62% security is primary blocker, Fig 3.3.10 / McKinsey) (P): https://hai.stanford.edu/ai-index/2026-ai-index-report ; PDF: https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf

### Slide 3 - System anatomy  *(Open)*
**Outline:** What an LLM actually is in operation: model (the reasoning core, hosted by a builder or hyperscaler), harness (Claude Code, ChatGPT web UI - holds chat history, makes the tool calls), MCP server (lets tool calls reach any other system). Key model facts: stateless, static, probabilistic; the whole context is re-sent every turn. CLOSES on the one fact: it all arrives down the same channel, so the model cannot tell a trusted instruction from data it was handed.

**Narrative:** The conceptual keystone of the talk. It demystifies the architecture so a CISO can reason about it, and plants the single idea - the same-channel problem - that almost every later breach reduces to. Introduced once here, then referenced (not re-explained) on slides 5, 6 and 8.

**References:**
- Anthropic, "Code execution with MCP" (architecture primer; on-slide ref) (P): https://www.anthropic.com/engineering/code-execution-with-mcp

### Slide 4 - Autonomous agents  *(Open)*
**Outline:** Same model underneath, stateless, text in / text out; what changes is who drives the loop. Chatbot/coding assistant: a human is in the loop every turn. An agent hands the "what's next" decision to the model and runs the loop itself - works out a step, calls a tool to actually do something, reads the result, goes again, no human between. That autonomy is the whole point of an agent and the whole risk.

**Narrative:** Builds directly on the same-channel fact: with a human in the loop a tricked model is caught before it acts; take the human out and the agent acts on its own judgement, turn after turn, building on any injected instruction. This is the shift that makes everything downstream dangerous - from a thing that answers to a thing that acts.

**References:**
- Google Cloud, "Choose a design pattern for your agentic AI system" (on-slide ref) (P): https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

### Slide 5 - What you actually deploy  *(S2)*
**Outline:** Anatomy of a production AI feature - six layers, one threat each: model (provenance, poisoned weights, malicious pickle files), prompt (injection, direct and indirect), tools/MCP/RAG (tool poisoning, over-broad scope), memory (poisoning and persistence), identity (sprawl, shared service accounts), data flow (exfiltration, logging gaps). Self-audit beat: most rooms lack visibility on three or more. "You cannot defend an inventory you do not have."

**Narrative:** Hands the audience the vocabulary for the rest of the talk by decomposing a production AI feature into six layers, each with one attached threat. Turns the vague "AI feature" into an inventory a CISO can reason about; the self-audit beat is the second hit of the discovery spine and earns attention for the breach run that follows.

**References:**
- OWASP LLM01:2025 Prompt Injection (P): https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; Top 10 2025: https://genai.owasp.org/llm-top-10/
- OWASP Top 10 for Agentic Applications 2026 (P): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- Saviynt 2026 CISO AI Risk Report (92% lack visibility into AI identities) (P): https://saviynt.com/ciso-ai-risk-report-2026

### Slide 6 - The attacker filled in a web form (ForcedLeak)  *(S2)*
**Outline:** Salesforce Agentforce "ForcedLeak" end to end: a company deploys a CRM agent; an attacker plants hidden instructions in the public Web-to-Lead form's Description field; when an employee later asks the agent to summarise that lead, it runs the payload with its own CRM permissions and exfiltrates pipeline data via an image call to a trusted domain - an expired-but-allowlisted Salesforce URL bought for $5. The attacker never spoke to the agent. (Noma Labs, CVSS 9.4, Sept 2025; researcher PoC, no named victim.) Label: the input is hostile.

**Narrative:** The first breach and the emotional hook: one named, concrete story of a deployed business AI turned into an exfiltration tool, walked through end to end. It makes the threat personal and is the first leg of the input/action/output triad. Lands on "new attack, old control" - good hygiene on the URL allow list would have stopped it.

**References:**
- ForcedLeak / Salesforce Agentforce (Noma Labs, CVSS 9.4, Sept 2025) (P): https://noma.security/blog/ (find ForcedLeak post; **VERIFY** exact URL)
- Historical anchor only, not on slide: EchoLeak / CVE-2025-32711 (P): https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711

### Slide 7 - Real incidents in real deployments  *(S2)*
**Outline:** Two named, real-world compromises of deployed AI - one in the wild, one found on the live system. Meta / Instagram (May 2026): attackers tricked Instagram's AI account-support agent into sending password-reset links to an address they controlled and hijacked 20,225 accounts (Meta's own breach notice), including the dormant @WhiteHouse handle and a US Space Force official - the action is unauthorized (over-permissioned agent acting on unverified instructions). Lenovo "Lena" (Aug 2025): a single ~400-char message made the public support chatbot emit attacker HTML (prompt injection + unsanitised output); when a human agent's console rendered the stored chat it stole their session cookies, opening Lenovo's support back-end - the output is hostile.

**Narrative:** Moves from anatomy to evidence: this is already happening to real, named deployments. Completes the input/action/output triad (input = slide 6, action = Meta, output = Lenovo), and each lands on a missing control that is not new - authorisation checks, output sanitisation. Sets up the question slide 8 answers: can't we just train the model to resist?

**References:**
- Meta / Instagram AI support assistant (May 2026) - 20,225 accounts; "prompt injection vs authorization bug" contested, name both: 404 Media (P) https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/ ; Silicon Republic (20,225 / Maine AG figure) (2) https://www.siliconrepublic.com/enterprise/hackers-stole-more-than-20000-instagram-accounts-using-meta-ai
- Lenovo "Lena" chatbot (Aug 2025) - prompt injection -> attacker HTML -> stolen session cookies; Cybernews, responsibly disclosed, fixed pre-publication (P): https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/ ; CSO Online (2): https://www.csoonline.com/article/4043005/lenovo-chatbot-breach-highlights-ai-security-blind-spots-in-customer-facing-systems.html

### Slide 8 - How about lab conditions?  *(S2)*
**Outline:** CHART: Gray Swan / NIST CAISI / UK AISI competition (arXiv:2603.15714, Q1 2026) - ASR-by-model bars (8.5% Gemini 2.5 Pro down to 0.5% Claude Opus 4.5) and the robustness-vs-capability scatter. 464 red-teamers, ~272K attack submissions, 8,648 successful breaks, at least one against every one of 13 frontier models. Pith: no model sits at zero; robustness does not track capability; per-attempt risk compounds across repeated tries. PIVOT line: stop asking the model to defend itself - build the defences around it. (The promise slide 10 pays off.)

**Narrative:** Shifts from individual incidents to systematic measurement - when every frontier model is stress-tested, all of them fall. Closes the "we'll just pick a safer model" escape route, and is the hinge of the deck: it forces the conclusion that the model's resistance is a layer, not a boundary, and that the rest of the session is about architecture.

**References:**
- Gray Swan / NIST CAISI / UK AISI competition paper (464 participants, ~272K submissions, 8,648 breaks; Figs 1, 7, 12) (P, chart): https://arxiv.org/abs/2603.15714
- NIST CAISI research blog (text only, no charts) (P): https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition
- Cisco audit (73.2% of production deployments carry injection weaknesses) (P): https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report

### Slide 9 - The supply chain into your agent  *(S2)*
**Outline:** The agentic supply chain - the unvetted distribution channel feeding code into your agents. ClawHub (Koi Security, "ClawHavoc", Jan-Feb 2026): 341 of 2,857 marketplace skills were outright malicious (~1 in 8), a real infostealer campaign - not a benchmark. Key point: a skill is content + scripts the agent executes with its own permissions, so a poisoned skill is code, not a vuln to exploit. And the registries don't vet - OX Security got a malicious package published by 9 of 11 AI-tool registries with zero review. Pith: you didn't write or vet most of your agent's attack surface; defending it starts with that inventory. (Last problem slide.)

**Narrative:** Turns from the model to the things you bolt onto it. The last and bleakest beat of the problem half: the marketplace you import from is mostly unvetted, you can't see what's plugged in, and "defending an agent has to start" with inventory and distrust. That lonely, overwhelming note is exactly what slide 10 pivots on.

**References:**
- ClawHub / "ClawHavoc" malicious skills (Koi Security, Feb 2026; 341 of 2,857 = ~12%, real infostealer campaign) (P): https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- OX Security - 9 of 11 AI-tool registries published a malicious package with zero review (benign PoC, ~Apr 2026) (P): https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/
- CVE-2026-25253 (OpenClaw one-click RCE, CVSS 8.8; supporting, the "skills are code" point) (P): https://nvd.nist.gov/vuln/detail/CVE-2026-25253
- Do-not-use: inflated follow-on counts (Antiy "1,184", "300k users"); OX "200k exposed servers" is an estimate - attribute only.

### Slide 10 - You're not inventing this alone anymore  *(S1)*  [bridge slide]
**Outline:** Six (VERIFY: Five Eyes is five nations) governments, one sentence: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment" (Five Eyes / UK NCSC, ~May 2026). Four bodies converged within a twelve-month window: Five Eyes "Careful Adoption of Agentic AI Services"; CoSAI agentic IAM + Agent Detection and Response (RSAC 2026); OWASP Agentic Top 10 + risk-tiering (Infosecurity Europe, June 2026); ISO/IEC 27090 at final draft. You are not inventing this alone any more - the floor is being poured around you.

**Narrative:** The bridge off slide 9. Slide 9 leaves the room feeling this is novel, overwhelming and lonely; slide 10 pivots on that feeling - you don't build the rest from scratch, because governments, industry and the standards bodies have converged on the same handful of ideas (know what you've got, give it an identity, be able to contain it) in twelve months. Emotional turn (alone -> supported) and logical turn (problem -> what to do). Speaker notes drafted; see speaker-notes-v4 DISPLAY 10.

**References** (each with a one-line description for the slide cards):
- **Five Eyes / UK NCSC - "Careful Adoption of Agentic AI Services"** (P): Joint guidance from the Five Eyes cyber-security agencies (the UK lead is NCSC) on deploying agentic AI with eyes open; it is the source of the headline go-live test that an agent you cannot understand, monitor or contain is not ready for deployment. https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFUL%20ADOPTION%20OF%20AGENTIC%20AI%20SERVICES_FINAL.PDF ; NCSC companion blog (the quote): https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai  **VERIFY** signatory count ("six governments" vs Five Eyes = five).
- **CoSAI (Coalition for Secure AI)** (P): An OASIS-hosted industry coalition that at RSAC 2026 published an agentic identity-and-access framework and an Agent Detection and Response (ADR) specification - effectively the industry's blueprint for giving every agent its own identity and a kill switch. https://www.oasis-open.org/2026/05/06/coalition-for-secure-ai-unveils-new-agentic-identity-and-security-research-following-high-profile-sessions-at-rsac-2026/
- **OWASP - Agentic Top 10 + risk-tiering** (2): OWASP, the body behind the web-app Top 10 every security team already knows, has done the same for agents - a ranked top-ten of agentic risks plus a scheme to risk-tier deployments, presented at Infosecurity Europe in June 2026. https://www.infosecurity-magazine.com/news/owasp-new-agentic-research-council/
- **ISO/IEC 27090** (P): The first international standard aimed squarely at AI security threats and how to address them, now at final-draft stage - the formal baseline organisations will eventually be audited against. https://www.iso.org/standard/56581.html

### Slide 11 - Tooling: discover what you have, then defend it  *(S3)*
**Outline:** Discover before you defend. Step zero is continuous discovery of what is actually running in production - deployed models and inference endpoints, MCP servers and tool registries, agent identities and service accounts, AI-adjacent services and data flows. You cannot defend an inventory you do not have (slide 5); discovery feeds the AI-BOM (slide 14). Then defence-in-depth, runtime edition: AI gateway with egress control (kills the zero-click exfil channel from ForcedLeak); layered injection defence - PromptArmor (ICLR 2026, <1% FP/FN) plus data-channel output filtering; OS-level agent sandboxing (Microsoft Execution Containers, 2026); log every prompt, tool call and memory write.

**Narrative:** Opens the response by making discovery the precondition - the payoff of slides 5 and 9 - then layers concrete, buyable-or-buildable controls around a model you must assume is fallible. Translates "defend with architecture" into specifics while honestly marking what reduces risk versus what eliminates it.

**References:**
- PromptArmor (ICLR 2026; <1% FP/FN) (P): https://arxiv.org/abs/2507.15219
- Anthropic prompt-injection defenses (1% ASR; "1% still represents meaningful risk") (P): https://www.anthropic.com/research/prompt-injection-defenses
- Microsoft Execution Containers / Build 2026 (P): https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/
- Orphaned-stat candidate to relocate here: 82% found agents security did not know about (CSA 2026) - opens the "discover" half. https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments
- Older defence literature for notes only: Spotlighting https://arxiv.org/abs/2403.14720 ; StruQ/SecAlign https://arxiv.org/abs/2402.06363 ; CaMeL https://arxiv.org/abs/2503.18813

### Slide 12 - Identity: agents are first-class identities  *(S3)*
**Outline:** Highest-leverage control. Every agent: a named human owner (no owner, no production), its own credential (no shared service accounts - per-agent attribution/revocation/audit, now a platform feature in Entra Agent ID), task-scoped JIT access (blast radius bounded by design), and a rehearsed kill switch - a control plane, not a button, tested quarterly (CoSAI blueprint). With machine/AI identities 109:1 (Palo Alto 2026), shared accounts are no longer acceptable; 60% cannot terminate a misbehaving agent today (Kiteworks).

**Narrative:** The single highest-leverage governance move a CISO can make this year: reframe agents from anonymous service accounts into named, owned, scoped, killable identities. NOTE: the on-slide line "the answer to 'you cannot stop them' is..." referenced the cut old-slide-11 - reword it, or carry the "agents act, you can't stop them" point briefly in the spoken notes so the callback still lands.

**References:**
- CoSAI "Agentic Identity and Access Management" (P): https://www.oasis-open.org/2026/05/06/coalition-for-secure-ai-unveils-new-agentic-identity-and-security-research-following-high-profile-sessions-at-rsac-2026/
- Microsoft Entra Agent ID (Ignite 2025) (P): https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025
- Kiteworks (60% cannot terminate) (P): https://www.kiteworks.com/sites/default/files/resources/kiteworks-report-2026-data-security-compliance-risk-forecast.pdf
- Palo Alto Networks 2026 (109:1) (P): https://www.paloaltonetworks.com/idira/identity-security-landscape-report

### Slide 13 - Process: red-team as launch criteria  *(S3)*
**Outline:** Adaptive evaluation before go-live and continuously after - static vendor numbers overstate protection. Two named, continuous practices: (1) red-team your own deployed models for prompt injection - run the attacks against your deployment, do not trust vendor ASR claims; (2) scan your MCP attack surface (slide 9) for tool poisoning, excessive scope and missing auth, on the same cadence. Garak / PyRIT / AgentDojo as the toolkit; red-teaming now runs at agent speed - 681 assessments in ~3 hours (Dreadnode, 2026). AI-aware IR playbooks; kill-switch tabletops quarterly.

**Narrative:** Moves from controls you deploy to the operating rhythm that keeps them honest - red-team as a launch gate, not an annual tick, plus AI-aware incident response. Makes evaluation a continuous, run-it-yourself discipline. NOTE: on-slide "as Slide 10 demonstrated" is now broken (it pointed at the cut infra slide) - re-point to slide 8 (Gray Swan) by name.

**References:**
- Garak (NVIDIA) (P): https://github.com/NVIDIA/garak ; https://arxiv.org/abs/2406.11036
- PyRIT (Microsoft) (P): https://github.com/Azure/PyRIT ; https://arxiv.org/abs/2410.02828
- AgentDojo benchmark (run it; leaderboard stale) (P): https://agentdojo.spylab.ai/
- Dreadnode "Redefining AI Red Teaming in the Agentic Era" (681 assessments in ~3 hrs) (P): https://arxiv.org/abs/2605.04019
- MITRE ATLAS v5.4 (P): https://atlas.mitre.org/

### Slide 14 - Governance: anchor, owner, measure  *(S3)*
**Outline:** Anchor: ISO/IEC 42001 + incoming 27090; EU AI Act - high-risk obligations land Dec 2027, but transparency obligations arrive Aug 2026 and Annex IV documentation maps to an AI-BOM (CycloneDX ML-BOM) - build it now. Owner: the agent inventory with a named human against every entry; no owner, no production. Measure: ASR per evaluation category, blast radius per agent, shadow-AI exposure (DBIR 2026: shadow AI tripled to 45% in a year). Translate metrics into pounds and owners.

**Narrative:** Lifts the response to board level - anchor to a standard, name an owner, measure what matters - with the regulatory clock as the forcing function. Gives the CISO the language to report control upward and turns the talk's advice into an accountable programme.

**References:**
- ISO/IEC 42001 (P): https://www.iso.org/standard/42001 ; ISO/IEC 27090: https://www.iso.org/standard/56581.html
- EU AI Act timeline (P/analysis): https://artificialintelligenceact.eu/implementation-timeline/
- CycloneDX ML-BOM / AI-BOM (ECMA-424) (P): https://cyclonedx.org/capabilities/mlbom/
- Verizon DBIR 2026 (shadow AI 15% -> 45%) (P): https://www.verizon.com/business/resources/reports/dbir/

### Slide 15 - On the other hand: the defences are arriving  *(Close)*
**Outline:** Steel-man for optimism: layered defence already reaches 1% ASR under adaptive attack (Anthropic); containment is becoming an OS primitive (Microsoft Execution Containers) and a product category (kill switches engineered, not improvised); the discipline consolidated within twelve months (Five Eyes, CoSAI, OWASP, ISO). Stanford reframe: security is the #1 blocker to scaling AI - which makes the CISO the enabler of the roadmap, not the brake.

**Narrative:** The steel-man close: honestly concedes the defences are arriving fast so the talk does not read as fear-mongering. Reframes the CISO as the enabler of the AI roadmap rather than its brake. NOTE: the "discipline consolidated" bullet duplicates slide 10 - decide whether to cut it here and keep this slide purely about defences/products working.

**References:** As cited on slides 8-12 (Anthropic 1% ASR; Microsoft Execution Containers; Five Eyes; CoSAI; Stanford 62%).

### Slide 16 - Questions / series close  *(Close)*
**Outline:** Bibliography by email. Series recap: Part 1 - the new SDLC (securing the AI that writes your code); Part 2 - what you are defending now. Monday-morning checklist: discover your AI estate; make every agent a named, scoped, killable identity; red-team your own models and MCP surface continuously; translate it for the board in pounds and owners.

**Narrative:** Closes the series, recaps the two-part arc (build-time, then run-time), and points the audience at the checklist and the emailed bibliography. Hands back to the host having given the room something concrete to do.

**References:** None (recap slide).

## Section breakdown

| Block | Slides |
|---|---|
| Open (incl. architecture primer) | 1 - 4 |
| Section 2 - The runtime risk pile (the problem) | 5 - 9 |
| Section 1 - The bridge | 10 |
| Section 3 - What to do (the response) | 11 - 14 |
| Close | 15 - 16 |
| **Total** | **16 slides** |

## Changes vs v3

| v3 slide | Disposition in v4 |
|---|---|
| Architecture (was folded into anatomy/inventory) | SPLIT OUT into two new deck slides: 3 System anatomy, 4 Autonomous agents. |
| v3 S2 You already shipped it | -> v4 S2 (hero figure now 99%, VERIFY vs v3's 91%). |
| v3 S3 ForcedLeak | -> v4 S6 (reordered after the anatomy primer + inventory). |
| v3 S4 What you actually deployed | -> v4 S5. |
| v3 S5 Real incidents | -> v4 S7. |
| v3 S6 Lab conditions | -> v4 S8. |
| v3 S7 Supply chain | -> v4 S9 (now the last problem slide). |
| v3 S8 Infrastructure exposed | **CUT.** |
| v3 S9 Agents act, cannot stop them | **CUT** (82%-unknown-agents and 60%-cannot-terminate stats relocate to v4 S11/S12). |
| v3 S10 The attacker moves second | **CUT** (verified, moved to Q&A reserve). |
| v3 S11 The discipline is being written now | -> v4 S10, retitled "You're not inventing this alone anymore," promoted to bridge. |
| v3 S12-17 | -> v4 S11-16 (renumbered down by one net of the cuts/splits). |

## Verified facts (this session, 2026-06-14)

- Gray Swan: 464 participants, ~272K submissions, 8,648 breaks, 13 models; ASR 0.5% (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro); no model at zero (arXiv:2603.15714).
- ClawHub / ClawHavoc: 341 of 2,857 skills malicious (~12%) (Koi Security, Feb 2026). OX Security: 9 of 11 registries published a malicious package with no review.
- The Attacker Moves Second (arXiv:2510.09023, OpenAI/Anthropic/DeepMind): 12 defences; Spotlighting 1% -> >95%, MetaSecAlign 2% -> 96%, Circuit Breakers -> 100%. (Slide cut; held for Q&A.)
- Qualys TRU "The Broken Physics of Remediation" (March 2026): 1bn+ CISA KEV records, 10,000+ orgs; critical vuln volume up 6.5x; time-to-exploit now negative. (Not on a slide; Q&A reserve / home-team reference.)

## Do-not-use (failed verification - kept out)

- "~50% injection success within 10 attempts" precise figure (International AI Safety Report 2026) - could not confirm the exact number; the report supports "within 10 attempts" qualitatively only.
- Inflated OpenClaw follow-on counts (Antiy "1,184", "300k users"); OX "200k exposed servers" is an estimate - attribute only.
- "98.2% memory poisoning"; "9-day agent-to-agent loop" - secondhand/unverified.

## Open items

1. **DISPLAY 10 notes** drafted, pending stat-verification (NCSC quote/date, Five Eyes signatory count, CoSAI ADR at RSAC, OWASP at Infosec Europe, ISO 27090 status) and copy-in to the deck.
2. **Slide 2** hero figure: deck says 99%, v3 sourced 91% from Palo Alto - reconcile.
3. **Slide 12** "the answer to 'you cannot stop them'" lost its setup (old slide 11 cut) - reword or carry in notes.
4. **Slide 13** "as Slide 10 demonstrated" mispointer - re-point to slide 8 (Gray Swan).
5. **Slide 15** "discipline consolidated" duplicates slide 10.

---

## Held in reserve / Q&A only (not on slides)
- OpenClaw "ClawJacked" full-takeover chain (Oasis Security, Feb 2026) + CVE-2026-25253 (1-click RCE) + the Qualys ETM OpenClaw case study - strong "is there Qualys work on this?" answer; note the Qualys piece is a product case study on a public CVE, not original TRU research.
- The Attacker Moves Second (arXiv:2510.09023) - "defences that test at 1% fail at >90% under an adaptive attacker"; the rebuttal to "just add a guardrail".
- Anthropic "Agentic Misalignment" (55.1% vs 6.5% - red-team scenario, easy to overclaim): https://www.anthropic.com/research/agentic-misalignment
