# Part 2 - Research update, June 10 2026

Supplements `part2-production-ai.md` (which is current to ~mid-April 2026). Two web sweeps run June 10 2026: (a) attacks/incidents on production AI, (b) defences, standards and survey data. Verification status noted per item. Items marked VERIFY need a primary-source check before they go on a slide.

---

## A. New incidents and attacks (April 15 - June 10, 2026)

### A1. Google GTIG: first AI-developed zero-day seen in the wild
- Date: May 11, 2026. Google Threat Intelligence Group.
- A threat actor used a zero-day exploit GTIG assesses "with high confidence" was developed with AI assistance - a 2FA bypass against a popular open-source web-based sysadmin tool. Tell-tale LLM artifacts: educational docstrings, a hallucinated CVSS score, textbook Pythonic structure.
- Also catalogues operational AI-enabled malware (PROMPTSPY, PROMPTFLUX, HONESTCUE, LONGSTREAM) that call LLMs at runtime to generate/obfuscate code. PROMPTSPY uses Gemini-2.5-flash-lite to autonomously navigate Android UI and can capture/replay biometric data.
- https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access

### A2. Three Critical M365 Copilot information-disclosure CVEs
- Date: May 7, 2026. CVE-2026-26129 (Business Chat), CVE-2026-26164 (command injection), CVE-2026-33111 (Copilot Chat in Edge).
- Injection-class (CWE-74/77), network-exploitable, no auth, at least one zero-interaction. Fixed server-side - enterprises never saw a patch or alert.
- Pairs with EchoLeak (June 2025): a year on, same product class, same vulnerability class. "The slope is the story" beat for Part 2.
- VERIFY: cite MSRC advisory pages by CVE number; agent verified via press only (cybersecuritynews.com/microsoft-365-copilot-vulnerabilities-data/).

### A3. "Bleeding Llama" - CVE-2026-7482, Ollama unauth memory leak
- Date: May 7, 2026. Disclosed by Cyera. CVSS 9.1.
- Unauthenticated attacker dumps raw process memory from an exposed Ollama server with three API calls (crafted GGUF tensor-size out-of-bounds read). Leaked memory: prompts, system instructions, API keys, env vars. ~300,000 internet-facing Ollama servers. Fixed in 0.17.1.
- Primary: Cyera research blog (cite that, not the press mirror).

### A4. Copilot Studio "ShareLeak" - patched, but the data exfiltrated anyway
- Analysis ~April 15, 2026 (Capsule Security / VentureBeat). Underlying CVE-2026-21520 patched Jan 15, 2026.
- Fake system-role message injected via a public SharePoint form field; agent emailed customer data out via Outlook. After the patch, output safety filters fired on some outputs but data still exfiltrated.
- PITH: output-layer safety filters are not an access-control boundary. You need pre-execution governance.
- VERIFY date on live VentureBeat page: venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook

### A5. Mercor breach - the downstream victim of LiteLLM
- Date: April 2, 2026 (Fortune). Mercor (~$10B AI training-data startup) compromised via the LiteLLM supply-chain attack Part 1 covered at the library level. Customer datasets, secret customer AI project info, Slack/ticketing, source code exposed. Lapsus$ later claimed ~4TB.
- Continuity story: Part 1 showed the compromise; Part 2 shows the victim.
- https://fortune.com/2026/04/02/mercor-ai-startup-security-incident-10-billion/

### A6. NSA MCP guidance
- Date: May 20-21, 2026. "Security Design Considerations for AI-Driven Automation Leveraging the Model Context Protocol" (17-page CSI).
- MCP "was released with a flexible and underspecified design"; serialization risks, unclear trust boundaries, dynamic tool invocation flagged as SYSTEMIC risks that "cannot be patched at isolated endpoints."
- https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/ (PDF 403s to fetch - screenshot or re-host for reference)

### A7. Mass exposure of AI infrastructure
- SentinelLABS + Censys (Jan 2026): 175,000 unique Ollama hosts exposed across 130 countries.
- THN "We Scanned 1 Million Exposed AI Services" (May 2026): 518 servers wrapping paid frontier models with no auth; 90+ exposed instances in government and finance. VERIFY figures on live page (403 to fetch).
- vLLM pre-auth RCE CVE-2026-22778, CVSS 9.8 (Feb 2026, pre-window): malicious video URL to multimodal API -> system(). vLLM 3M+ downloads/month. ox.security / orca.security writeups.

### A8. Pre-window items possibly missed
- "Chat & Ask AI" leak (Feb 2026): ~300M messages / ~25M users via Firebase misconfig; 103 of 200 iOS apps scanned had the same misconfig - systemic LLM-wrapper pattern. (malwarebytes.com)
- Anthropic AI-orchestrated espionage campaign (Nov 2025): already in base - do not double count.

---

## B. New defence, standards and survey material

### B1. Five Eyes joint guidance: "Careful Adoption of Agentic AI Services"
- CISA, NSA, UK NCSC, ASD, CCCS, NZ NCSC. April 30 / May 1, 2026; NCSC companion blog May 15, 2026.
- Prescriptions: least privilege for agents, scope limits, no long-lived credentials, bounded pilots, continuous behaviour monitoring.
- NCSC quote (verified): "If you cannot understand, monitor or contain an agent's actions, it is not ready for deployment."
- Strong UK anchor. https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai

### B2. CoSAI papers (RSAC 2026)
- Coalition for Secure AI / OASIS (40+ orgs incl. Google, Microsoft, Anthropic, OpenAI). May 6, 2026 press release (verified).
- "Agentic Identity and Access Management" (Apr 2026) + "The Future of Agentic Security" (Mar 2026). Unique credentials per agent, task-scoped access, ephemeral environments, intent-based authorization, and a new category: Agent Detection and Response (ADR).

### B3. EU AI Act - Digital Omnibus delay agreed May 2026
- Political agreement May 6, Council confirmed May 13, 2026. Stand-alone high-risk (Annex III) obligations postponed Aug 2 2026 -> Dec 2 2027; embedded (Annex I) -> Aug 2 2028. BUT Article 50 transparency obligations still land Aug 2, 2026, and Omnibus only becomes law on OJ publication.
- Audience-fresh news. Message: 16 months breathing room on high-risk, but transparency lands in 8 weeks; Annex IV documentation maps to AI-BOM - build now.
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

### B4. OWASP at Infosecurity Europe (London, June 2-4, 2026)
- New Agentic Research Council announced June 4 (led by John Sotiropoulos). "State of Agentic AI and Governance" (June 3, 2026) includes a practical maturity and risk-tiering scheme.
- Event research: 64% of UK cybersecurity leaders say agentic AI will have the biggest impact on cyber defence over the next three years (52% across Europe).

### B5. Containment gap, quantified (Kiteworks 2026 Forecast; n=225 - state methodology)
- 100% have agentic AI on roadmap; 51% in production. 60% cannot terminate a misbehaving agent; 63% cannot enforce purpose limitations; 55% cannot prevent lateral movement. Monitoring investment outruns containment by 15-20 points.
- PITH: a kill switch is a control plane, not a button.

### B6. Platform containment arriving
- Microsoft Build 2026 (June 2-3): Microsoft Execution Containers (MXC) - OS-enforced agent sandboxing; per-agent Entra identity; session isolation; Agent 365 policy management.
- ServiceNow AI Control Tower kill switches (May 5-6, 2026): immediate stop with state capture, audit trail. Fortune framing anecdote: 2025 Replit incident - agent deleted a production database in 9 seconds.

### B7. "Agents of Chaos" live red-team study (Feb 2026)
- ~20 researchers (Northeastern, Stanford, Harvard, MIT, CMU et al.); 6 autonomous agents with real email, filesystems, bash, cron; two-week live exercise. PII disclosure (leaked SSNs because attacker said "forward" instead of "share"), one agent destroyed its own mail server, a 9-day agent-to-agent infinite loop, takeover via display-name impersonation. No effective kill switch.
- VERIFY specifics against the arXiv paper before quoting.

### B8. Defence efficacy - the honest picture
- Anthropic (Nov 24, 2025, verified): Claude Opus 4.5 browser use with safeguards: 1% ASR against an adaptive best-of-N attacker with 100 attempts. Anthropic's own caveat: "1% still represents meaningful risk."
- PromptArmor (ICLR 2026, arXiv 2507.15219): off-the-shelf LLM strips injected content; <1% FPR and FNR on AgentDojo; post-removal ASR <1%. Deployable-today baseline.
- "The Attacker Moves Second" (Nasr, Carlini et al.; OpenAI+Anthropic+DeepMind; arXiv 2510.09023): 12 published defences subjected to adaptive attacks - ASR pushed above 90% for most defences that claimed near-zero on static benchmarks. ESSENTIAL CAVEAT SLIDE.
- International AI Safety Report 2026 (Bengio-chaired, Feb 2026): sophisticated attackers bypass even best-defended frontier models ~50% of the time within 10 attempts.
- NIST CAISI / Gray Swan / UK AISI red-team competition (Mar 23, 2026, verified): 400+ competitors, 250,000+ attack submissions vs 13 frontier models; at least one successful attack against EVERY model; robustness did NOT correlate with capability; attacks transfer.
- Synthesis: assume the model layer will be bypassed; prefer architectural controls (CaMeL-style isolation, sandboxing, least privilege) that do not depend on the model resisting.

### B9. Fresh survey ammunition
- Verizon DBIR 2026 (May 19, 2026, verified on newsroom): vulnerability exploitation now #1 breach entry point at 31% - first time in 19 years it beats stolen credentials; AI compressed exploit windows "from months to mere hours". Shadow AI tripled 15% -> 45% in one year - now #3 non-malicious data-leakage action. Third-party involvement 48% of breaches.
- CSA "Autonomous but not Controlled" (Apr 21, 2026; Token Security; n=418): 65% had an AI-agent-related security incident in the past 12 months (61% data exposure, 43% operational disruption, 35% financial loss). Same survey as the existing "82% unknown agents" stat - cite once.
- CSA / Zenity (Apr 16, 2026; n=445, verified): 53% experienced agent scope violations; 47% agent-involved incidents; 16% high confidence detecting agent threats; 31% have formal agent policies.
- Stanford AI Index 2026: 62% cite security/risk as the PRIMARY blocker to scaling agentic AI (ahead of technical limits 38%). Incidents up 55% YoY (233 -> 362). VERIFY 62% in the PDF.
- Cisco State of AI Security 2026 (verified): 83% plan agentic deployment; 29% feel ready to do so securely.
- IBM X-Force 2026 (Feb 25): 44% surge in attacks starting at public-facing apps; 300,000+ ChatGPT credentials for sale on dark web.

### B10. Tooling / AI-BOM / standards status
- Dreadnode "Redefining AI Red Teaming in the Agentic Era" (arXiv 2605.04019, May 5, 2026, verified): agentic harness ran 681 assessments / 7,727 trials across 68 goals in ~3 hours vs weeks. Red-teaming is being automated to agent speed.
- PyRIT moved to microsoft/PyRIT (Azure repo archived Mar 2026). Garak mature (19+ probe families).
- CycloneDX ML-BOM (ECMA-424) becoming the de facto AI-BOM format; EU AI Act Annex IV maps onto it.
- ISO/IEC 27090 (AI security threats): FDIS Mar 12, 2026, publication expected later 2026.
- NIST COSAiS (800-53 overlays for AI): agent overlays still in development.
- MITRE ATLAS still v5.4.0 (16 tactics / 84 techniques / 32 mitigations); no newer version as of June 10.
- IBM Cost of a Data Breach 2026: NOT yet released (expect late July 2026). Use 2025 edition, say so.

---

## C. Do not use without a primary source (failed verification)

- "88% of orgs with AI agents had a confirmed/suspected incident" - content-farm only; no named survey found. (Use CSA 65% instead.)
- A2A "single poisoned agent corrupted 87% of downstream decisions within 4 hours" - blog-only, no primary research.
- MCP STDIO "200,000 servers at risk" / nginx-ui CVE-2026-33032 - aggregator-only; check NVD first.
- Promptfoo acquired by OpenAI (~$86M) - single low-quality source.
- VentureBeat's "31.5% pre-safeguard" Anthropic browser ASR - not on Anthropic's page; use Anthropic's verified 1%-with-safeguards number.
- "73.2% -> 8.7% defence framework" (arXiv 2511.15759) - paper of uncertain quality; skip. (The Cisco 73.2% audit stat itself remains fine, separately sourced.)
- "74% of agents over-privileged" - could not trace to a primary source; the 68% human-vs-agent stat is CSA/Aembit (Mar 24, 2026).
- AgentPoison / MINJA memory-poisoning rates - real papers but lab results, pre-2026; frame as "research shows", not incidents.
