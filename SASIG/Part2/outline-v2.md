# Outline v2 - chart-first S2, 2026-only sourcing

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot. ~38 min content + 10 min Q&A + 5 min host preamble.
**Slide count:** 17

**Structural shift from v1:** Two changes drove this rebuild. (1) **Chart-first S2.** Part 1's middle run worked because each slide was one graph from one named study; v1 was survey-heavy and incident-heavy by comparison. S2 is rebuilt so slides 5-9 each anchor on a single chartable result, mirroring Part 1 slides 3-7 (real-world signal -> lab conditions -> replication -> agentic-makes-it-worse -> the instrumented study). Survey numbers compress into supporting bullets and footers - seasoning, not the meal. (2) **2026-only sourcing rule.** No pre-2026 references unless very compelling. Three exceptions retained by agreement: EchoLeak (June 2025) as the historical anchor of the "year of zero-click" hook; "The Attacker Moves Second" (Oct 2025, OpenAI + Anthropic + DeepMind joint - the deck's signature graph); Anthropic's 1%-ASR-under-adaptive-attack result (Nov 2025) as the best defence-efficacy number that survives the adaptive critique. Demoted to speaker notes: foundational injection literature (Greshake, BIPIA), ShadowLeak, Spotlighting/StruQ/CaMeL as headline cites, IBM CoDB 2025 (2026 edition lands ~6 weeks post-webinar - say so). CyberArk 82:1 (2025) used only if the figure-hunt finds no 2026 refresh, and date-flagged on the slide if so.

**Figure status:** Slides 5, 6, 7, 9, 10 are chart-anchored. Charts on 6, 7, 10 are verified in principle (AgentDojo leaderboard, NIST CAISI post, Attacker Moves Second); exact figures on 5 and 9 (Stanford incident chart, Agents of Chaos) pending the June 10 figure-hunt pass, with fallbacks noted per slide.

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product, 40/60. Bibliography by email. Part 1 was build-time; today is what you are defending once it ships. |
| 2 | Open | You already shipped it | Hero: 83% of orgs plan agentic AI deployment; only 29% feel ready to do so securely (Cisco 2026). 51% already run agents in production (Kiteworks 2026). Stanford AI Index 2026: 62% say security is now the PRIMARY blocker to scaling - ahead of technical limits. Poll: has someone in your org shipped an AI feature you did not know about? |
| 3 | Open | A year of zero-click | Incident narrative: EchoLeak (June 2025, CVSS 9.3, first zero-click prompt injection in a production LLM system) -> three more Critical M365 Copilot injection CVEs (May 2026), zero-auth, fixed server-side - you never saw a patch. One year of fixes did not retire the class. The slope is the story, again. |
| 4 | S2 | What you actually deployed | Anatomy of a production AI feature - six layers, one threat each: model (provenance), prompt (injection), tools/MCP, memory (poisoning), identity (sprawl), data flow (exfiltration). Self-audit beat: most rooms lack visibility on three or more. Sets the inventory vocabulary for everything that follows. |
| 5 | S2 | Real incidents in real deployments | CHART: Stanford AI Index 2026 - documented AI incidents 233 (2024) -> 362 (2025), +55% YoY (pending figure verification; fallback: 2026 incident timeline built from the verified record). Supporting rotation, all 2026: Recommendation Poisoning (50 attempts, 31 companies, 60 days), Copilot Studio ShareLeak (data exfiltrated even after the patch), Meta internal agent exposure. Pith: the attack arrives through channels the agent trusts - and output filters are not an access-control boundary. |
| 6 | S2 | How about lab conditions? | CHART: AgentDojo live leaderboard, current 2026 state - task success with vs without attack, the same ongoing-public-benchmark format as Part 1's Endor slide. Even frontier agents remain exploitable by published attacks while solving most tasks. Series callback title, deliberate. |
| 7 | S2 | All thirteen models fell | CHART: NIST CAISI / Gray Swan / UK AISI competition (Mar 2026) - 400+ red-teamers, 250,000+ attack submissions, at least one successful attack against EVERY frontier model; robustness does NOT correlate with capability; attacks transfer across models. Supporting: Cisco audit - 73.2% of production AI deployments contain prompt-injection weaknesses. Model choice is a security decision; no choice is immunity. |
| 8 | S2 | Your AI infrastructure is already on the internet | Bleeding Llama (CVE-2026-7482, CVSS 9.1): unauthenticated memory dump from exposed Ollama servers in three API calls; ~300K internet-facing. 175K exposed Ollama hosts across 130 countries (SentinelLABS/Censys); vLLM pre-auth RCE CVSS 9.8; ~2,000 production MCP servers, none authenticated. NSA (May 2026): MCP risks are systemic and "cannot be patched at isolated endpoints." |
| 9 | S2 | Agents act - and you cannot stop them | CHART: Agents of Chaos live red-team (Feb 2026, 6 instrumented agents with real email/bash/cron) - vulnerability-class matrix pending figure verification. Leaked SSNs over a wording change, destroyed its own mail server, 9-day agent-to-agent loop, no effective kill switch. CSA Apr 2026: 65% had an agent-related incident in 12 months; 53% saw agents exceed intended permissions; 82% found agents security did not know about; 60% cannot terminate a misbehaving agent (Kiteworks). Cues slide 13. |
| 10 | S1 | The attacker moves second | SIGNATURE CHART: Nasr, Carlini et al. (OpenAI + Anthropic + DeepMind) - 12 published defences, reported near-zero ASR vs adaptive-attack ASR pushed above 90%. Supporting: International AI Safety Report 2026 - best-defended frontier models bypassed ~50% of the time within 10 attempts. Pith: static benchmark numbers are fiction; the model's resistance is a layer, not a boundary. Defend with architecture. |
| 11 | S1 | The discipline is being written now | Six governments, one sentence: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment" (Five Eyes / NCSC, May 2026). CoSAI agentic IAM + Agent Detection and Response (RSAC 2026); OWASP Agentic Top 10 + risk-tiering scheme (Infosecurity Europe, June 2026); ISO/IEC 27090 at FDIS. You are not inventing this alone any more - but the floor is being poured around you. |
| 12 | S3 | Tooling - defence in depth around the model | The yes-path gates, runtime edition: AI gateway with egress control (kills the zero-click exfil channel); layered injection defence - PromptArmor (ICLR 2026, <1% FP/FN) as the deployable baseline, Anthropic's full stack at 1% ASR under adaptive attack (their own caveat: 1% is still meaningful risk); OS-level agent sandboxing arriving as a platform primitive (Microsoft Execution Containers, Build 2026); log every prompt, tool call and memory write. Older defence literature in notes. |
| 13 | S3 | Identity - agents are first-class identities | Every agent: a named human owner, its own credential (no shared service accounts), task-scoped JIT access, and a rehearsed kill switch - a control plane, not a button (60% cannot terminate today). CoSAI agentic IAM blueprint; per-agent identity now a platform feature (Entra Agent ID). Identity-sprawl numbers from slide 9 land their response here. |
| 14 | S3 | Process - red-team as launch criteria | Adaptive evaluation before go-live and continuously after - static numbers overstate protection (slide 10's lesson); Garak / PyRIT / AgentDojo as the toolkit; red-teaming itself now runs at agent speed (681 assessments in ~3 hours - Dreadnode, May 2026). AI-aware IR playbooks: memory poisoning, agent-gone-rogue, vendor AI compromise (Mercor - the LiteLLM victim, Apr 2026). Kill-switch tabletops quarterly. |
| 15 | S3 | Governance - anchor, owner, measure | Anchor: ISO/IEC 42001 + incoming 27090; EU AI Act news the room will not all know - high-risk obligations delayed to Dec 2027, but transparency lands Aug 2026 and Annex IV documentation maps to an AI-BOM (CycloneDX ML-BOM) - build it now. Owner: the agent inventory with named humans. Measure: ASR per evaluation category, blast radius per agent, shadow-AI exposure (DBIR 2026: shadow AI tripled to 45% in one year). |
| 16 | Close | On the other hand - the defences are arriving | Steel-man: layered defence already reaches 1% ASR under adaptive attack; containment is becoming an OS primitive (MXC) and a product category (kill switches); the discipline consolidated within twelve months (Five Eyes, CoSAI, ISO). Stanford reframe: security is the #1 blocker to scaling - which makes the CISO the enabler of the roadmap, not the brake. |
| 17 | Close | Q&A and series close | Bibliography by email. Series recap: Part 1 - the new SDLC; Part 2 - what you are defending now. Monday-morning checklist callback. |

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 3 |
| Section 2 - The runtime risk pile (the problem) | 4 - 9 |
| Section 1 - The reframe and the discipline | 10 - 11 |
| Section 3 - What to do (the response) | 12 - 15 |
| Close | 16 - 17 |
| **Total** | **17 slides** |

17 slides at ~2.6 min each in a ~45-min content window. Same shape as Part 1 v8 and Part 2 v1: 6 problem slides, 2 pivot slides, 4 response slides.

## Changes vs v1

| v1 slide | Disposition | Reason |
|---|---|---|
| v1 Slide 5 (Prompt injection is structural) | Split | The foundational-literature half (Greshake, BIPIA) demoted to speaker notes under the 2026 rule; the Cisco 73.2% audit stat moves to Slide 7 as supporting evidence; the ShareLeak "filters are not a boundary" pith moves to Slide 5's incident rotation. No standalone structural-argument slide - Part 1 slide 8 already made it, and slide 10 now makes it with better data. |
| v1 Slide 6 (Trusted channels rotation) | Re-anchored as Slide 5 | Incident rotation kept but now hangs off a chart (Stanford incident count) instead of a list. ShadowLeak (2025) dropped from the rotation; 2026 incidents fill it. Trusted-channels takeaway becomes the slide's pith. |
| v1 Slide 7 (Infrastructure exposed) | Kept as Slide 8 | Content unchanged; moved one slot later so the lab-conditions pair (6-7) sits together, mirroring Part 1's double "lab conditions" beat. |
| v1 Slides 8 + 9 (Agents act / Identity sprawl) | Merged into Slide 9 | One story: you cannot name them, distinguish them, or kill them. Agents of Chaos becomes the chart anchor; the survey bars (65%, 53%, 82%, 60%) compress to supporting bullets. Identity stats that served slide 13's setup still cue it; 82:1 and 92% visibility move to slide 13 speaker notes (82:1 pending 2026 refresh). |
| v1 Slide 10 (Assume the model will be bypassed) | Re-heroed as Slide 10 | Same argument, now anchored on the Attacker Moves Second chart as the deck's signature graph; retitled to match. NIST CAISI material moves forward to Slide 7 (it is a lab result, not a reframe), leaving slide 10 cleaner: one chart, one number, one pith. |
| New Slide 6 (How about lab conditions?) | Added | AgentDojo live leaderboard - the Part 2 analogue of Part 1's Endor ongoing-benchmark slide, including the series-callback title. Slot created by the 8+9 merge. |
| v1 Slides 11-17 | Kept, light edits | Slide 12 defence cites updated (PromptArmor headline, older papers to notes); slide 13 absorbs identity-response stats; wording aligned to the chart-first S2. |

## Open items (pending figure hunt, June 10)

1. **Slide 5 chart:** verify the Stanford AI Index 2026 incident figure (233 -> 362) and whether the published chart is usable; fallback is a self-built 2026 incident timeline.
2. **Slide 9 chart:** locate the Agents of Chaos arXiv paper, verify the anecdotes, and confirm there is a usable figure; fallback is the CSA survey bars promoted to the anchor.
3. **Slide 6/7 specifics:** pull current AgentDojo leaderboard rows and the exact NIST CAISI post charts.
4. **Slide 10:** exact figure number and per-defence numbers from Attacker Moves Second.
5. **82:1 identity ratio:** check for a CyberArk 2026 refresh; if none, date-flag or drop to notes.
6. **Hunt:** 2026 successor to HouYi (vulnerability rate across real deployed apps) and any 2026 memory-poisoning dose-response figure - either could displace a weaker chart if found.
