# Outline v3 - verified 2026 figures, chart-anchored S2

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot. ~38 min content + 10 min Q&A + 5 min host preamble.
**Slide count:** 17

**Structural shift from v2:** Driven by the June 10 figure verification pass. Three changes. (1) **AgentDojo dropped as a live chart** - its public leaderboard has not been updated since Feb 2025, so it cannot anchor a "current lab conditions" slide. (2) **v2 slides 6 and 7 merge** - the Gray Swan / NIST CAISI competition paper (arXiv:2603.15714) carries BOTH the "lab conditions" message and the "every model fell" message in one source (ASR-by-model bars + the robustness-vs-capability scatter), so they collapse into a single slide. (3) The freed slot becomes a dedicated **agentic supply-chain** slide (slide 7), anchored on real 2026 incidents - the ClawHub malicious-skill marketplace (Koi Security) and OX Security's registry test. Net deck stays at 17.

**Sourcing exceptions (pre-2026, retained by agreement):**
- **EchoLeak (June 2025)** - the historical anchor of the slide-3 "year of zero-click" hook; the whole point is that it is a year old.
- **The Attacker Moves Second (Oct 2025)** - slide-10 signature chart. Joint OpenAI + Anthropic + DeepMind authorship, the definitive statement of the point, and now *corroborated* by a 2026 paper (arXiv:2604.23887) - the replication strengthens the exception.
- **Anthropic 1%-ASR result (Nov 2025)** - slide-12 candour beat ("1% still represents meaningful risk"); PromptArmor (ICLR 2026) carries the 2026 on-slide defence cite alongside it.

> Each slide carries its **Outline** (the content), **Narrative** (what it is doing and how it moves the story), and **References** (sources likely to be cited). Tags: (P) primary, (2) secondary/press, (chart) figure to screenshot at build time; **VERIFY** = still needs a primary-source check before going live.

### Slide 1 - Title and the promise  *(Open)*
**Outline:** Title slide. Non-product, 40/60. Bibliography by email. Part 1 was build-time; today is what you are defending once it ships.

**Narrative:** Opens the session and re-establishes the non-product compact that earned the room in Part 1. It positions Part 2 against Part 1 - build-time is behind us; this hour is about the AI you have already put into production - so the audience knows exactly what lens to bring.

**References:** None (title slide).

### Slide 2 - You already shipped it  *(Open)*
**Outline:** Hero: 83% of orgs plan agentic AI deployment; only 29% feel ready to do so securely (Cisco 2026). 91% already run autonomous agents in production (Palo Alto Networks 2026, n=2,930). Stanford AI Index 2026: 62% name security/risk as the PRIMARY blocker to scaling agentic AI, ahead of technical limits (38%) - McKinsey survey in the Index. Poll: has someone in your org shipped an AI feature you did not know about?

**Narrative:** Establishes that this is not hypothetical: agentic AI is deployed faster than it is secured, and the audience is sitting in that gap. The 83%/29% readiness split and "62% say security is the primary blocker to scaling" set the stakes and quietly frame security as the thing standing between the business and its roadmap - a thread the close pays off.

**References:**
- Cisco State of AI Security 2026 (83% plan / 29% ready) (P): https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report
- Palo Alto Networks 2026 Identity Security Landscape (91% run agents in production; 109:1) (P): https://www.paloaltonetworks.com/idira/identity-security-landscape-report ; press: https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-introduces-idira--the-next-generation-identity-security-platform-built-for-the-ai-enterprise
- Stanford AI Index 2026 (62% security is primary blocker, Fig 3.3.10 / McKinsey) (P): https://hai.stanford.edu/ai-index/2026-ai-index-report ; report PDF: https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Kiteworks 2026 Data Security & Compliance Risk Forecast (51% in production; n=225) (P): https://www.kiteworks.com/sites/default/files/resources/kiteworks-report-2026-data-security-compliance-risk-forecast.pdf

### Slide 3 - The attacker filled in a web form  *(Open)*
**Outline:** Salesforce Agentforce "ForcedLeak" walked through end to end: a company deploys a CRM agent over its own sales pipeline; an attacker plants hidden instructions in the public Web-to-Lead form's Description field; when an employee later asks the agent to summarise that lead, it runs the attacker's payload with its own CRM permissions and exfiltrates pipeline data via an image call to a CSP-trusted domain. The attacker never spoke to the agent. (Noma Labs, CVSS 9.4, Sept 2025; researcher PoC, no named victim.)

**Narrative:** The emotional hook: one named, concrete story of a deployed business AI turned into an exfiltration tool, walked through end to end. It makes the threat personal ("that is the agent my team just shipped") and plants the thesis in a single line - the attacker never spoke to the agent, they filled in a web form; you are defending a system whose trusted inputs come from anyone on the internet.

**References:** *(still list EchoLeak from before the slide-3 rework - left unchanged pending your direction)*
- EchoLeak / CVE-2025-32711 (P): https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711 ; academic write-up (Reddy & Gujral, AAAI 2025): https://arxiv.org/abs/2509.10540 ; technical: https://www.hackthebox.com/blog/cve-2025-32711-echoleak-copilot-vulnerability ; https://www.varonis.com/blog/echoleak
- M365 Copilot May 2026 CVEs - CVE-2026-26129, CVE-2026-26164, CVE-2026-33111 - cite by number on MSRC (P, **VERIFY** MSRC pages); press: https://cybersecuritynews.com/microsoft-365-copilot-vulnerabilities-data/

### Slide 4 - What you actually deployed  *(S2)*
**Outline:** Anatomy of a production AI feature - six layers, one threat each: model (provenance), prompt (injection), tools/MCP, memory (poisoning), identity (sprawl), data flow (exfiltration). Self-audit beat: most rooms lack visibility on three or more. Sets the inventory vocabulary for everything that follows.

**Narrative:** Hands the audience the vocabulary for the rest of the talk by decomposing a production AI feature into six layers, each with one attached threat. It turns the vague "AI feature" into an inventory a CISO can reason about, and the self-audit beat ("most of you lack visibility on three of these") earns attention for the problem run that follows.

**References:**
- OWASP LLM01:2025 Prompt Injection (P): https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; LLM Top 10 2025: https://genai.owasp.org/llm-top-10/
- OWASP Top 10 for Agentic Applications 2026 (P): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- Saviynt 2026 CISO AI Risk Report (92% lack visibility into AI identities) (P): https://saviynt.com/ciso-ai-risk-report-2026

### Slide 5 - Real incidents in real deployments  *(S2)*
**Outline:** Two named, real-world compromises of deployed AI - one in the wild, one found on the live system. Meta / Instagram (June 2026): attackers tricked Instagram's AI account-support agent into sending password-reset links to an address they controlled and hijacked 20,225 accounts (Meta's own breach notice to Maine's AG), including the dormant @WhiteHouse handle and a US Space Force official; whether the root cause is "prompt injection" or "a missing authorization check" is contested - name both. Lenovo "Lena" (Aug 2025): a single ~400-character message made Lenovo's public customer-support chatbot emit attacker-controlled HTML (prompt injection + unsanitised output); when a human support agent's console rendered the stored chat it stole the agent's session cookies, opening Lenovo's support back-end - live and archived customer conversations - with a path to lateral movement. A pure AI-layer weakness, not a plumbing bug.

**Narrative:** Moves from anatomy to evidence: this is already happening to real, named deployments, not just in the lab. It grounds the abstract layers of slide 4 in concrete compromise before we widen out to the measured, lab-scale picture in the next slides.

**References:**
- Meta / Instagram AI support assistant (June 2026) - 20,225 accounts hijacked; "prompt injection vs authorization bug" framing is contested, name both: 404 Media (P) https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/ ; TechCrunch (2) https://techcrunch.com/2026/06/01/hackers-hijacked-instagram-accounts-by-tricking-meta-ai-support-chatbot-into-granting-access/ ; Silicon Republic - the 20,225 / Maine AG figure (2) https://www.siliconrepublic.com/enterprise/hackers-stole-more-than-20000-instagram-accounts-using-meta-ai
- Lenovo "Lena" customer-support chatbot (Aug 2025) - prompt injection -> attacker-controlled HTML -> stolen support-agent session cookies -> entry to the support back-end; researcher finding (Cybernews), responsibly disclosed, fixed pre-publication, no in-the-wild abuse; exact prompt not public: Cybernews, primary (P) https://cybernews.com/security/lenovo-chatbot-lena-plagued-by-critical-vulnerabilities/ ; CSO Online (2) https://www.csoonline.com/article/4043005/lenovo-chatbot-breach-highlights-ai-security-blind-spots-in-customer-facing-systems.html ; IT Pro (2) https://www.itpro.com/security/flaw-in-lenovos-customer-service-ai-chatbot-could-let-hackers-run-malicious-code-breach-networks

### Slide 6 - How about lab conditions?  *(S2)*
**Outline:** CHART: Gray Swan / NIST CAISI / UK AISI competition (arXiv:2603.15714, Mar 2026) - ASR-by-model bars (8.5% Gemini 2.5 Pro down to 0.5% Claude Opus 4.5) and the robustness-vs-capability scatter (r=-0.31, non-significant). 464 red-teamers, ~272K attack submissions, 8,648 successful breaks, at least one against every one of 13 frontier models; attacks transfer across models. Cisco audit (73.2% of production deployments carry injection weaknesses) as supporting. Pith: model choice is a security decision; capability is not immunity. Series-callback title, deliberate.

**Narrative:** Shifts from individual incidents to systematic measurement - when every frontier model is stress-tested under controlled conditions, all of them fall. It closes the "we will just pick a safer model" escape route by showing robustness does not track capability, making the case that this is structural rather than a one-vendor problem.

**References:**
- Gray Swan / NIST CAISI / UK AISI competition paper (464 participants, 272K submissions, 8,648 breaks; Figs 1, 7, 12) (P, chart): https://arxiv.org/abs/2603.15714
- NIST CAISI research blog (text only, no charts) (P): https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition
- Cisco audit (73.2% of production deployments carry injection weaknesses) (P): https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report

### Slide 7 - The supply chain into your agent  *(S2)*
**Outline:** The agentic supply chain - the unvetted distribution channel feeding code into your agents. ClawHub (Koi Security, Feb 2026): 341 of 2,857 agent-marketplace skills were outright malicious (~1 in 8), a real infostealer campaign - not a benchmark. Key point: a skill is markdown + scripts the agent executes, so a poisoned skill is code, not a vuln to exploit. And the registries don't vet - OX Security got a malicious package published by 9 of 11 AI-tool registries with zero review. Pith: you didn't write or vet most of your agent's attack surface.

**Narrative:** Turns from the model to the things you bolt onto it - the tools, skills and MCP servers your agent trusts. It shows the marketplace you are importing from is mostly unvetted, so the attack surface is not just the model's reasoning but everything you have connected to it.

**References:**
- ClawHub / "ClawHavoc" malicious skills (Koi Security, Feb 2026; 341 of 2,857 = ~12%, real infostealer campaign) (P): https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting ; corroboration: https://www.scworld.com/news/openclaw-agents-targeted-with-341-malicious-clawhub-skills
- OX Security - 9 of 11 AI-tool registries published a malicious package with zero review (benign PoC, ~Apr 2026) (P): https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/
- "Markdown is an installer" pull-quote (1Password, via Immersive Labs - verify exact wording): https://www.immersivelabs.com/resources/c7-blog/openclaw-hunting-season-is-open
- CVE-2026-25253 (OpenClaw one-click RCE, CVSS 8.8) (P): https://nvd.nist.gov/vuln/detail/CVE-2026-25253
- Do-not-use: inflated follow-on counts (Antiy "1,184", "300k users"); OX "200k exposed servers" is an estimate - attribute only.

### Slide 8 - Your infrastructure is already on the internet  *(S2)*
**Outline:** Bleeding Llama (CVE-2026-7482, CVSS 9.1, May 2026): unauthenticated memory dump from exposed Ollama servers in three API calls; ~300K internet-facing. 175K exposed Ollama hosts across 130 countries (SentinelLABS/Censys); vLLM pre-auth RCE CVSS 9.8; ~2,000 production MCP servers, none authenticated. NSA (May 2026): MCP risks are systemic and "cannot be patched at isolated endpoints." Distinct from slide 7: this is the servers you expose, not the tools you import. Exposed because nobody inventoried them - which is why discovery is control one (slide 12).

**Narrative:** Drops from the agent's logical layers to the physical reality that the servers running your models often sit unauthenticated on the public internet. It is the "and it is worse than you think" beat - before any clever prompt injection, the plumbing itself is exposed.

**References:**
- Bleeding Llama / CVE-2026-7482 (Cyera) (P, **VERIFY** Cyera blog URL): press https://cybersecuritynews.com/ollama-vulnerability-exposes-servers/
- 175K exposed Ollama hosts (SentinelLABS/Censys) (2): https://thehackernews.com/2026/01/researchers-find-175000-publicly.html
- "We Scanned 1 Million Exposed AI Services" (518 no-auth frontier wrappers) (2, **VERIFY** figures on live page): https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html
- vLLM pre-auth RCE / CVE-2026-22778 (P): https://www.ox.security/blog/cve-2026-22778-vllm-rce-vulnerability/ ; https://orca.security/resources/blog/cve-2026-22778-vllm-rce-vulnerability/
- NSA MCP guidance (May 2026) (P, PDF 403s - screenshot/re-host): https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/
- ~2,000 unauthenticated MCP servers (AIP, Prakash 2026) (P): https://arxiv.org/abs/2603.24775

### Slide 9 - Agents act, and you cannot stop them  *(S2)*
**Outline:** CHART: ClawWorm self-propagating agent attack - epidemic S-curves across 40,000 agent instances, 64.5% aggregate ASR (arXiv:2603.15727, Mar 2026). The Morris-worm-for-agents visual. Supporting: Agents of Chaos live exercise (Feb 2026) - 10 of 11 scenarios produced critical failures; leaked an unredacted SSN over a "forward" vs "share" wording change, an agent destroyed its own mail server, display-name impersonation handed over admin, no working kill switch. Survey bars: CSA Apr 2026 - 65% had an agent-related incident in 12 months, 53% saw agents exceed intended permissions, 82% found agents security did not know about; 60% cannot terminate a misbehaving agent (Kiteworks); machine/AI identities outnumber humans 109:1 (Palo Alto Networks 2026). Cues slide 13.

**Narrative:** The crescendo of the problem section: unlike a passive model, an agent takes autonomous action, so compromise becomes propagation and there is no kill switch. It establishes the blast-radius and containment problem that the identity and response slides in Section 3 exist to answer.

**References:**
- ClawWorm (64.5% ASR; SI curves over 40,000 instances; Fig 3) (P, chart): https://arxiv.org/abs/2603.15727
- Agents of Chaos (10/11 scenarios critical; loop ~1 hour) (P): https://arxiv.org/abs/2602.20021 ; full report: https://agentsofchaos.baulab.info/report.html
- CSA "Autonomous but not Controlled" / Token Security (65% had an agent incident; 82% unknown agents) (P): https://cloudsecurityalliance.org/press-releases/2026/04/21/new-cloud-security-alliance-survey-reveals-82-of-enterprises-have-unknown-ai-agents-in-their-environments
- CSA / Zenity (53% scope violations; 47% agent incidents) (P): https://cloudsecurityalliance.org/press-releases/2026/04/16/more-than-half-of-organizations-experience-ai-agent-scope-violations-cloud-security-alliance-study-finds
- Kiteworks (60% cannot terminate a misbehaving agent) (P): https://www.kiteworks.com/sites/default/files/resources/kiteworks-report-2026-data-security-compliance-risk-forecast.pdf
- Palo Alto Networks 2026 (109:1; 90% had identity breach) (P): https://www.paloaltonetworks.com/idira/identity-security-landscape-report
- Replit "deleted prod DB in 9 seconds" framing anecdote (2): https://fortune.com/2026/05/06/servicenow-kill-switch-ai-agents-bill-mcdermott/

### Slide 10 - The attacker moves second  *(S1)*
**Outline:** SIGNATURE CHART: Nasr, Carlini et al. (OpenAI + Anthropic + DeepMind), arXiv:2510.09023 - paired bars across 12 published defences, reported ASR near 1% vs adaptive-attack ASR above 90% (Spotlighting ~1% -> >95%; MetaSecAlign 2% -> 96%; Circuit Breakers -> 100%). Corroborated 2026: prompt-level defences each collapse at a named attack round while data-channel output filtering held across 15,000 attacks (arXiv:2604.23887, Apr 2026) - feeds slide 12. Supporting: ~50% injection success within 10 attempts even for the newest frontier models (Int'l AI Safety Report 2026, Fig 3.9, developer-reported). Pith: static benchmark numbers are fiction; the model's resistance is a layer, not a boundary. Defend with architecture.

**Narrative:** The pivot of the whole deck. It delivers the uncomfortable truth that the defences vendors quote near-zero numbers for collapse under a determined adaptive attacker - so the model's resistance can never be your boundary. This forces the conclusion that drives Section 3: defend with architecture, not with the model's good behaviour.

**References:**
- The Attacker Moves Second (Nasr, Carlini et al.; Fig 1 paired bars) (P, chart): https://arxiv.org/abs/2510.09023
- Evaluation of Prompt Injection Defenses (collapse-by-round; output filtering held; Fig 6) (P): https://arxiv.org/abs/2604.23887
- International AI Safety Report 2026 (~50% within 10 attempts, Fig 3.9) (P): https://arxiv.org/abs/2602.21012 ; publication page: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026

### Slide 11 - The discipline is being written now  *(S1)*
**Outline:** Six governments, one sentence: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment" (Five Eyes / NCSC, May 2026). CoSAI agentic IAM + Agent Detection and Response (RSAC 2026); OWASP Agentic Top 10 + risk-tiering scheme (Infosecurity Europe, June 2026); ISO/IEC 27090 at FDIS. You are not inventing this alone any more - but the floor is being poured around you.

**Narrative:** Pulls the audience back from despair by showing they are not alone - six governments, OWASP, CoSAI and ISO have converged on the same controls within twelve months. It hands the room an external mandate and a shared vocabulary, bridging from "the problem is structural" to "here is the emerging consensus on what to do."

**References:**
- Five Eyes "Careful Adoption of Agentic AI Services" (P): https://media.defense.gov/2026/Apr/30/2003922823/-1/-1/0/CAREFUL%20ADOPTION%20OF%20AGENTIC%20AI%20SERVICES_FINAL.PDF ; NCSC companion blog (the "if you cannot understand, monitor or contain" quote): https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai
- CoSAI agentic identity + ADR (RSAC 2026) (P): https://www.oasis-open.org/2026/05/06/coalition-for-secure-ai-unveils-new-agentic-identity-and-security-research-following-high-profile-sessions-at-rsac-2026/
- OWASP Agentic Research Council / Infosecurity Europe June 2026 (2): https://www.infosecurity-magazine.com/news/owasp-new-agentic-research-council/ ; 64% UK leaders stat: https://www.globalbankingandfinance.com/infosecurity-europe-highlights-surge-in-agentic-ai-as-64-of-uk-cybersecurity-leaders-say-it-will-have-the-biggest-impact-on-cyber-defence-over-the-coming-years/
- ISO/IEC 27090 (FDIS) (P): https://www.iso.org/standard/56581.html

### Slide 12 - Tooling: discover what you have, then defend it  *(S3)*
**Outline:** Discover before you defend. Step zero is continuous discovery of what is actually running in production - deployed models, MCP servers, inference endpoints (the exposed Ollama/vLLM from slide 8), agent identities, and AI-adjacent services across the estate. You cannot defend an inventory you do not have (slide 4); discovery is the precondition for every control here and it feeds the AI-BOM on slide 15. Then the defence-in-depth gates, runtime edition: AI gateway with egress control (kills the zero-click exfil channel); layered injection defence - PromptArmor (ICLR 2026, <1% FP/FN) as the deployable baseline, plus the slide-10 lesson that data-channel output filtering outlasts prompt-level guards; Anthropic's full stack at 1% ASR under adaptive attack (their own caveat: 1% is still meaningful risk); OS-level agent sandboxing arriving as a platform primitive (Microsoft Execution Containers, Build 2026); log every prompt, tool call and memory write. Older defence literature (Spotlighting, StruQ, CaMeL) in notes.

**Narrative:** Opens the response by making discovery the precondition - you cannot defend what you have not inventoried (the payoff of slide 4 and the exposed infrastructure on slide 8) - then layers the technical controls around a model you must assume is fallible: gateway, injection defences, sandboxing, logging. It translates slide 10's "defend with architecture" into concrete, buyable-or-buildable controls, while honestly marking what reduces risk versus what eliminates it.

**References:**
- PromptArmor (ICLR 2026; <1% FP/FN) (P): https://arxiv.org/abs/2507.15219
- Anthropic prompt-injection defenses (1% ASR; "1% still represents meaningful risk") (P): https://www.anthropic.com/research/prompt-injection-defenses
- Evaluation of Prompt Injection Defenses (data-channel output filtering outlasts prompt-level guards) (P): https://arxiv.org/abs/2604.23887
- Microsoft Execution Containers / Build 2026 (P): https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/ ; https://www.microsoft.com/en-us/security/blog/2026/06/02/microsoft-build-2026-securing-code-agents-and-models-across-the-development-lifecycle/
- Older defence literature for speaker notes only: Spotlighting https://arxiv.org/abs/2403.14720 ; StruQ/SecAlign https://arxiv.org/abs/2402.06363 ; CaMeL https://arxiv.org/abs/2503.18813

### Slide 13 - Identity: agents are first-class identities  *(S3)*
**Outline:** Every agent: a named human owner, its own credential (no shared service accounts), task-scoped JIT access, and a rehearsed kill switch - a control plane, not a button (60% cannot terminate today). CoSAI agentic IAM blueprint; per-agent identity now a platform feature (Entra Agent ID). Lands the 109:1 / unknown-agents sprawl from slide 9.

**Narrative:** Answers the containment gap from slide 9 directly: if an agent can act, it must be a named, owned, scoped, killable identity. It reframes agents from anonymous service accounts into first-class identities - the single highest-leverage governance move a CISO can make this year.

**References:**
- CoSAI "Agentic Identity and Access Management" (P): https://www.oasis-open.org/2026/05/06/coalition-for-secure-ai-unveils-new-agentic-identity-and-security-research-following-high-profile-sessions-at-rsac-2026/
- Microsoft Entra Agent ID (Ignite 2025) (P): https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025
- ServiceNow AI Control Tower kill switches (2): https://www.theregister.com/software/2026/05/05/servicenow-adds-agent-kill-switches-to-ai-control-tower/
- Kiteworks (60% cannot terminate) and Palo Alto (109:1) - as Slide 9

### Slide 14 - Process: red-team as launch criteria  *(S3)*
**Outline:** Adaptive evaluation before go-live and continuously after - static numbers overstate protection (slide 10's lesson). Two named, continuous practices: (1) red-team your own deployed models for prompt injection - run the attacks against your deployment, do not trust vendor ASR claims (slide 10); (2) scan your MCP attack surface (slides 7-8) for tool poisoning, excessive scope and missing auth, on the same cadence. Garak / PyRIT / AgentDojo as the toolkit (run the benchmark, do not trust the leaderboard); red-teaming itself now runs at agent speed - 681 assessments in ~3 hours (Dreadnode, May 2026). AI-aware IR playbooks: memory poisoning, agent-gone-rogue, vendor AI compromise (Mercor - the LiteLLM victim, Apr 2026). Kill-switch tabletops quarterly.

**Narrative:** Moves from controls you deploy to the operating rhythm that keeps them honest - red-team your own models and MCP surface as a launch gate, not an annual tick, plus AI-aware incident response. It operationalises slide 10's lesson that static test numbers lie, and makes evaluation a continuous, run-it-yourself discipline.

**References:**
- Garak (NVIDIA) (P): https://github.com/NVIDIA/garak ; https://arxiv.org/abs/2406.11036
- PyRIT (Microsoft; now microsoft/PyRIT) (P): https://github.com/Azure/PyRIT ; https://arxiv.org/abs/2410.02828
- AgentDojo benchmark (run it; leaderboard stale) (P): https://agentdojo.spylab.ai/
- Dreadnode "Redefining AI Red Teaming in the Agentic Era" (681 assessments in ~3 hrs) (P): https://arxiv.org/abs/2605.04019
- Mercor breach (LiteLLM downstream victim) (2): https://fortune.com/2026/04/02/mercor-ai-startup-security-incident-10-billion/
- MITRE ATLAS v5.4 (P): https://atlas.mitre.org/

### Slide 15 - Governance: anchor, owner, measure  *(S3)*
**Outline:** Anchor: ISO/IEC 42001 + incoming 27090; EU AI Act news the room will not all know - high-risk obligations delayed to Dec 2027, but transparency lands Aug 2026 and Annex IV documentation maps to an AI-BOM (CycloneDX ML-BOM) - build it now. Owner: the agent inventory with named humans. Measure: ASR per evaluation category, blast radius per agent, shadow-AI exposure (DBIR 2026: shadow AI tripled to 45% in one year).

**Narrative:** Lifts the response to board level - anchor to a standard, name an owner, measure what matters - with the regulatory clock (EU AI Act, AI-BOM) as the forcing function. It gives the CISO the language to report control upward and turns the talk's advice into an accountable programme.

**References:**
- ISO/IEC 42001 (P): https://www.iso.org/standard/42001 ; ISO/IEC 27090: https://www.iso.org/standard/56581.html
- EU AI Act Digital Omnibus delay (P/analysis): https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ ; implementation timeline: https://artificialintelligenceact.eu/implementation-timeline/
- CycloneDX ML-BOM / AI-BOM (ECMA-424) (P): https://cyclonedx.org/capabilities/mlbom/
- Verizon DBIR 2026 (shadow AI 15% -> 45%) (P): https://www.verizon.com/about/news/breach-industry-wide-dbir-finds ; report: https://www.verizon.com/business/resources/reports/dbir/
- NIST AI 600-1 (logging/measurement practices, speaker notes) (P): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

### Slide 16 - On the other hand: the defences are arriving  *(Close)*
**Outline:** Steel-man: layered defence already reaches 1% ASR under adaptive attack; containment is becoming an OS primitive (MXC) and a product category (kill switches); the discipline consolidated within twelve months (Five Eyes, CoSAI, ISO). Stanford reframe: security is the #1 blocker to scaling - which makes the CISO the enabler of the roadmap, not the brake.

**Narrative:** The steel-man close: it honestly concedes the defences are arriving fast (1% ASR, OS-level containment, a consolidating discipline) so the talk does not read as fear-mongering. It reframes the CISO as the enabler of the AI roadmap rather than its brake, landing the empowering note.

**References:** As cited on slides 10-13 (Anthropic 1% ASR; MXC / Build 2026; ServiceNow kill switches; Five Eyes; CoSAI; Stanford 62%).

### Slide 17 - Q&A and series close  *(Close)*
**Outline:** Bibliography by email. Series recap: Part 1 - the new SDLC; Part 2 - what you are defending now. Monday-morning checklist callback.

**Narrative:** Closes the series, recaps the two-part arc (build-time, then run-time), and points the audience at the Monday-morning checklist and the emailed bibliography. It hands back to the host having given the room something concrete to do.

**References:** None (recap slide).

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 3 |
| Section 2 - The runtime risk pile (the problem) | 4 - 9 |
| Section 1 - The reframe and the discipline | 10 - 11 |
| Section 3 - What to do (the response) | 12 - 15 |
| Close | 16 - 17 |
| **Total** | **17 slides** |

17 slides at ~2.6 min each in a ~45-min content window. Six S2 slides (4 anatomy + 5 chart-anchored problem slides), two pivot slides, four response slides.

## Changes vs v2

| v2 slide | Disposition | Reason |
|---|---|---|
| v2 Slide 5 (Real incidents - Stanford chart) | Re-anchored | Rebuilt around two named real-world compromises of deployed AI - Meta/Instagram (in the wild, 20,225 accounts) and Lenovo Lena (prompt injection on the live customer chatbot). Incident-led, not chart-led; the Stanford incident count and resume-screening trend are both dropped. Retitled "Real incidents in real deployments." |
| v2 Slide 6 (AgentDojo live leaderboard) | Cut | Leaderboard stale since Feb 2025; cannot anchor a "current lab conditions" slide. |
| v2 Slide 7 (All thirteen models fell) | Becomes Slide 6 | Gray Swan paper carries both the "lab conditions" and "every model fell" messages; absorbs the cut AgentDojo slot and keeps the series-callback title. |
| NEW Slide 7 (Supply chain into your agent) | Added, then re-anchored | The freed slot. Dropped the academic benchmarks (SkillProbe/MCPTox/MCP First Glance) - too in-the-weeds and too close to the injection theme. Re-anchored on real 2026 incidents: ClawHub's malicious-skill marketplace (~1 in 8 skills malicious, Koi Security) + OX Security's registry test (9 of 11 publish with no review). Distinct from the injection slides - this is the third-party code you imported, not the model being tricked. |
| v2 Slide 8 (Infrastructure exposed) | Kept | Content unchanged; now explicitly contrasted with slide 7 (servers you expose vs tools you import) to police overlap. |
| v2 Slide 9 (Agents act) | Re-anchored | ClawWorm epidemic curve becomes the hero chart; Agents of Chaos provides the corrected stories (loop ~1 hour, not 9 days). Identity ratio updated 82:1 -> 109:1 (Palo Alto Networks 2026). |
| v2 Slide 10 (Attacker moves second) | Kept as signature | Attacker Moves Second retained per decision; 2026 collapse-by-round paper added as corroboration and as a feed into slide 12. IAISI line reworded to match Fig 3.9 (developer-reported). |
| v2 Slides 11-17 | Kept, light edits | Slide 12 gains the "output filtering outlasts prompt-level guards" point; slide 14 notes the AgentDojo benchmark/leaderboard distinction; 109:1 lands on slide 13. |

## Verified facts and corrections baked into v3

- Gray Swan: 464 participants, ~272K submissions, 8,648 breaks, 13 models, Fig 1 / Fig 7 / Fig 12 (arXiv:2603.15714, verified). Blog has no charts - cite the paper.
- ClawHub / ClawHavoc: 341 of 2,857 marketplace skills malicious (~12%), real infostealer campaign (Koi Security, Feb 2026, verified). OX Security: 9 of 11 AI-tool registries published a malicious package with no review (~Apr 2026; vendor benign PoC). [SkillProbe/MCPTox/MCP-First-Glance dropped from slide 7 - SkillProbe's "90% fail" was an overstatement: ~70% were Approved, ~0% rejected.]
- ClawWorm: 64.5% aggregate ASR, SI curves over 40,000 instances (arXiv:2603.15727, verified).
- Agents of Chaos: loop ran ~1 hour (NOT 9 days); 10/11 scenarios critical; 38 authors / 20 red-team participants (arXiv:2602.20021, verified).
- Attacker Moves Second: Fig 1 paired bars, named per-defence numbers (arXiv:2510.09023, verified).
- Stanford AI Index 2026: 362 vs 233 incidents (Fig 3.2.1); 62% security-is-primary-blocker (Fig 3.3.10, McKinsey survey) - both verified in the report PDF.
- IAISI 2026: ~50% within 10 attempts is a read-off of Fig 3.9 (developer-reported), not a verbatim quote - reworded.
- Identity ratio: 109:1 (Palo Alto Networks 2026 Identity Security Landscape, n=2,930); 91% run agents in production; 90% had an identity-related breach in 12 months. Supersedes CyberArk 82:1 (2025). The "79 of 109 are AI agents" split is secondary-source only - excluded.

## Do-not-use (failed verification - kept out)

- "98.2% memory poisoning across 74,636 production interactions" - NOT in the USENIX SoK it is attributed to; secondhand only.
- "9-day agent-to-agent loop" - secondary coverage only; primary report says ~1 hour.
- No clean 2026 memory-poisoning dose-response curve exists; the canonical one is AgentPoison 2024 (<0.1% poison -> ~80% ASR) - cite only with a 2024 flag if a dose-response visual is wanted.
- Promptfoo/OpenAI acquisition, "73.2% -> 8.7% defence framework," "74% of agents over-privileged" - all failed verification (see research-update-june2026.md section C).

## Open items for slide-plan stage

1. Charts to screenshot from primary PDFs at build time: Gray Swan Fig 1 + Fig 12; ClawWorm Fig 3; Attacker Moves Second Fig 1; IAISI Fig 3.9. (Slide 7 is now incident-led, not a paper chart - its visual is a Gamma-built "1 in 8" graphic.)
2. Confirm the Palo Alto 2026 identity report fieldwork firm before quoting n=2,930 methodology on a slide.

---

## Held in reserve / Q&A only (not on slides)
- IBM Cost of a Data Breach 2025 (shadow AI adds $670K; 2026 edition due ~late July) (P): https://www.ibm.com/reports/data-breach
- Anthropic "Agentic Misalignment" (55.1% vs 6.5% - red-team scenario, easy to overclaim) (P): https://www.anthropic.com/research/agentic-misalignment
- Foundational injection literature (notes only): Greshake et al. AISec 2023 https://arxiv.org/abs/2302.12173 ; BIPIA / Yi et al. KDD 2025 https://arxiv.org/abs/2312.14197 ; ShadowLeak (2025) https://www.darkreading.com/vulnerabilities-threats/shadowleak-chatgpt-invisibly-steal-emails
