# Outline v1 - Part 2, problem-first, mirrors Part 1 architecture

**Webinar:** Running AI in Production: What You Are Actually Defending Now
**Series:** The New Normal: Software, Security and the AI Stack - Part 2 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot. ~38 min content + 10 min Q&A + 5 min host preamble.
**Slide count:** 17

**Design notes:** Same architecture as Part 1 v8 - problem-first arc, 17 slides at ~2.6 min each. Open with adoption + a year of zero-click incidents, walk the full runtime risk pile (S2), pivot on the reframe ("the model will be bypassed - defend with architecture") and the discipline now being written (Five Eyes / CoSAI / OWASP), then the four-category response (S3: Tooling, Identity, Process, Governance - Identity replaces Part 1's Culture as the category the runtime data demands), steel-man close. Built from `part2-production-ai.md` (April research base) updated by `research-update-june2026.md` (June 10 sweep). Part 1 hand-offs honoured: runtime prompt injection (P1 slide 8 footer), EchoLeak hook, LiteLLM -> Mercor continuity.

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product, 40/60. Bibliography by email. Where Part 1 was build-time, today is what you are defending once it ships. |
| 2 | Open | You already shipped it | Hero: 83% of orgs plan agentic AI deployment; 29% feel ready to do so securely (Cisco 2026). 51% already run agents in production (Kiteworks 2026); Stanford AI Index 2026 - 62% say security is now the PRIMARY blocker to scaling AI, ahead of technical limits. Poll: has someone in your org shipped an AI feature you did not know about? |
| 3 | Open | A year of zero-click | Incident narrative: EchoLeak (June 2025, CVSS 9.3, first zero-click prompt injection in production) -> three more Critical M365 Copilot injection CVEs (May 2026), zero-auth, fixed server-side - you never saw a patch. The vulnerability class did not retire in a year of fixes. The slope is the story, again. |
| 4 | S2 | What you actually deployed | Anatomy of a production AI feature - six layers, one threat each: model (provenance), prompt (injection), tools/MCP, memory (poisoning), identity (sprawl), data flow (exfiltration). Self-audit beat: most rooms lack visibility on three or more. |
| 5 | S2 | Prompt injection is structural - and the filters will not save you | Foundational record: every evaluated LLM vulnerable to indirect injection (BIPIA, KDD 2025); Cisco audit - 73.2% of production AI deployments contain prompt-injection weaknesses. Copilot Studio ShareLeak: data exfiltrated even after the patch. Pith: output-layer safety filters are not an access-control boundary. |
| 6 | S2 | The attack arrives through channels the agent trusts | Fast incident rotation: ShadowLeak (service-side zero-click via Gmail connector), Microsoft AI Recommendation Poisoning (50 attempts, 31 companies, 60 days - persistent memory), image-scaling injection (Trail of Bits), Meta internal agent confused-deputy exposure. Takeaway: direct user prompts are the minority; retrieved content, email, images and memory writes are the attack surface. |
| 7 | S2 | Your AI infrastructure is already on the internet | Bleeding Llama (CVE-2026-7482): unauth memory dump from ~300K exposed Ollama servers in three API calls. 175K exposed Ollama hosts (SentinelLABS/Censys); vLLM pre-auth RCE CVSS 9.8; ~2,000 production MCP servers, none authenticated; NSA: MCP risks "cannot be patched at isolated endpoints." |
| 8 | S2 | Agents act - incidents at machine speed | Agents of Chaos live red-team (6 agents, real email/bash/cron): leaked SSNs, destroyed own mail server, 9-day agent-to-agent loop, no effective kill switch. Replit 2025: production database deleted in 9 seconds. CSA Apr 2026: 65% had an agent-related incident in 12 months; 53% saw agents exceed intended permissions. |
| 9 | S2 | The identity sprawl nobody governs | Machine identities outnumber humans 82:1 (CyberArk 2025); 82% of enterprises found AI agents security did not know about; 68% cannot distinguish human from agent activity; 92% lack visibility into AI identities (Saviynt). Containment gap: 60% cannot terminate a misbehaving agent (Kiteworks). Cues slide 13. |
| 10 | S1 | Assume the model will be bypassed | The reframe. Best-defended frontier models bypassed ~50% of the time within 10 attempts (International AI Safety Report 2026); NIST CAISI competition - 250K+ attacks, all 13 frontier models fell; "The Attacker Moves Second" (OpenAI+Anthropic+DeepMind) - adaptive attacks push most published defences above 90% ASR. Pith: the model's resistance is a layer, not a boundary - defend with architecture. |
| 11 | S1 | The discipline is being written now | Six governments, one sentence: "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment" (Five Eyes / NCSC, May 2026). CoSAI agentic IAM + Agent Detection and Response (RSAC 2026); OWASP Agentic Top 10 + risk-tiering (Infosecurity Europe, June 2026); ISO/IEC 27090 at FDIS. You are not inventing this alone any more - but the floor is being poured around you. |
| 12 | S3 | Tooling - defence in depth around the model | The yes-path gates, runtime edition: AI gateway with egress control (kills the EchoLeak exfil channel); layered injection defence - Spotlighting, CaMeL, PromptArmor (<1% FP/FN), Anthropic browser stack at 1% ASR under adaptive attack; OS-level agent sandboxing arriving as platform primitive (MS Execution Containers, Build 2026); log every prompt, tool call and memory write. |
| 13 | S3 | Identity - agents are first-class identities | Every agent: a named human owner, its own credential (no shared service accounts), task-scoped JIT access, and a rehearsed kill switch - a control plane, not a button (60% cannot terminate today). CoSAI agentic IAM; Entra Agent ID. Closes the slide 9 loop. |
| 14 | S3 | Process - red-team as launch criteria, not annual check | Adaptive evaluation before go-live and continuously after (static benchmark numbers overstate protection - Attacker Moves Second); Garak / PyRIT / AgentDojo; red-teaming itself now runs at agent speed (hours, not weeks - Dreadnode). AI-aware IR playbooks: memory poisoning, agent-gone-rogue, vendor AI compromise (Mercor: the LiteLLM victim). Kill-switch tabletops quarterly. |
| 15 | S3 | Governance - anchor, owner, measure | Anchor: ISO/IEC 42001 + incoming 27090; EU AI Act news - high-risk obligations delayed to Dec 2027, but transparency lands Aug 2026 and Annex IV documentation maps to an AI-BOM (CycloneDX ML-BOM) - build it now. Owner: agent inventory with named humans. Measure: ASR per evaluation category, blast radius per agent, shadow-AI exposure (DBIR: shadow AI tripled to 45% in one year). |
| 16 | Close | On the other hand - the defences are arriving | Steel-man: layered defence already reaches 1% ASR under adaptive attack (Anthropic); containment is becoming an OS primitive (MXC) and a product category (kill switches); the discipline consolidated in twelve months (Five Eyes, CoSAI, ISO). Stanford reframe: security is the #1 blocker to scaling - which makes the CISO the enabler of the roadmap, not the brake. |
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

17 slides at ~2.6 min each in a ~45-min content window. Same shape as Part 1 v8: 6 problem slides, 2 pivot slides, 4 response slides.

## Relationship to part2-production-ai.md (April design doc)

| April doc element | Disposition in v1 |
|---|---|
| EchoLeak opening hook | Kept, extended into "A year of zero-click" with the May 2026 M365 Copilot CVEs (slide 3) - stronger than a single 2025 incident. |
| Anatomy of a production AI feature (Segment 1) | Kept as slide 4, compressed from a 10-min segment to one slide; per-layer stats move to speaker notes. |
| Foundational prompt-injection literature list | Compressed into slide 5; full citation list lives in slide-plan sources, not on slides. |
| Incident rotation (Segment 2) | Split across slides 5-8 by argument (filters fail / trusted channels / exposed infrastructure / agents act) rather than presented as a list. |
| Agent identity (3.2) | Promoted: gets a problem slide (9) AND a response slide (13). The June data (containment gap, CSA incident rates) makes identity the strongest single thread in Part 2. |
| Technical controls (3.1) | Slide 12, updated with PromptArmor ICLR 2026, Anthropic 1% ASR, MXC. |
| Process (3.3) | Slide 14, updated with adaptive-evaluation caveat and Dreadnode agent-speed red-teaming. |
| Culture and organisation (3.4) | Folded into slides 13-15 (named owner, CISO-as-enabler close). No standalone culture slide - the runtime story is identity and containment, and Part 1 already made the culture argument. |
| Governance (3.5) | Slide 15 in Part 1's anchor/owner/measure shape; EU AI Act omnibus delay is new and audience-fresh. |
| Anthropic Agentic Misalignment 55.1% stat | Dropped from slides (red-team scenario, easy to overclaim - per the April doc's own rigor note); available in speaker notes for Q&A. |
| IBM Cost of a Data Breach 2025 metrics | Kept in slide 15 speaker notes; 2026 edition lands ~6 weeks after the webinar - say so. |
| "73.2% -> 8.7% defence framework" pairing | 73.2% audit stat kept (slide 5); the 8.7% reduction claim dropped - source quality failed verification. |
