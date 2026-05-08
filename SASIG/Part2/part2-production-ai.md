# Part 2 - Running AI in Production: What You Are Actually Defending Now

**Series:** The New Normal: Software, Security and the AI Stack
**Format:** One-hour, non-product webinar
**Duration:** 55 min content + 5 min Q&A
**Shape:** 5 / 10 / 10 / 25 / 5
**Audience:** SASIG community - CISOs and security leaders (vendors, contractors and press excluded)
**Host:** Matt Campbell

**Series framing (from titles-and-blurbs.md):** AI is already in your stack - writing your code, running in your products, and embedded in the vendor tools your teams depend on. This two-part series offers security leaders a practical view of what has changed, and what to do next.

**Part 2 framing:** Your business just shipped an AI feature. What exactly are you defending, and how? Prompt injection, model supply-chain attacks, agent identity sprawl, and AI tooling buried inside vendor platforms are all rewriting what "production security" means. Most enterprises are inventing the discipline as they go. We will work through what to inventory, what to test, what to govern, and the questions you should be putting to your teams before the next launch.

**Thesis:** You have shipped AI features. What is running in production is a model, a prompt, a set of tools and agents, and a supply chain you probably do not fully understand. The peer-reviewed and industry literatures both report that current LLM systems are universally vulnerable to indirect prompt injection (Greshake et al. AISec 2023; Yi et al. KDD 2025; Cisco 2026 reports 73% of audited production deployments contain prompt-injection weaknesses). The job is to defend a system whose output is non-deterministic with controls whose precondition was determinism.

---

## Design principles (apply to both sessions)

- **Non-product promise.** Stated in the intro and close. Earns the room at SASIG.
- **Problem-to-solution balance closer to 40/60.** The "what to do" content is the centre of gravity - not the threat deck.
- **Academic-grade sourcing.** Every quantitative claim traces to a primary publication: peer-reviewed paper, conference proceedings, or named industry research with stated methodology.
- **One arresting stat per segment, not a firehose.** Most slides are one chart, one diagram, or one incident narrative.
- **Live poll at opening.** "Has someone in your org shipped an AI feature you did not know about?"
- **Peer voice.** If SASIG allows, a 5-minute fireside with a CISO who has lived one of the incident categories.

## Cross-cutting thread

**Velocity is the shift, evidence is the test.** Developers got faster (Cui et al. RCT shows +26% PRs/week with Copilot - arXiv:2302.06590) but the same tools introduced 2.74x more vulnerabilities (CodeRabbit 2025), and on real maintenance work in mature codebases experienced developers were 19% slower while believing they were 20% faster (METR 2025, arXiv:2507.09089). Reviewers, defenders, and governance all have to match the new pace - and the data already tells us where the gap is widening.

---

## Opening hook (5 min)

**EchoLeak (CVE-2025-32711)** as the first documented zero-click prompt-injection exploit in a production LLM system. Microsoft 365 Copilot; CVSS 9.3; disclosed by Aim Labs June 2025; chained four primitives - XPIA classifier bypass, reference-style markdown evading link redaction, auto-fetched images, Teams proxy abuse via permitted CSP. Coined the term "LLM Scope Violation."

- Academic write-up: Reddy & Gujral 2025, AAAI Fall Symposium - https://arxiv.org/abs/2509.10540
- CVE: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711
- Technical deep-dive: https://www.hackthebox.com/blog/cve-2025-32711-echoleak-copilot-vulnerability
- Industry coverage: https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html, https://www.varonis.com/blog/echoleak

**Pair with ShadowLeak** (Radware via Bugcrowd, June 2025; fixed September 2025) as the **service-side** zero-click case: ChatGPT Deep Research with Gmail connector; exfiltration occurs from OpenAI's infrastructure rather than the client device (https://www.darkreading.com/vulnerabilities-threats/shadowleak-chatgpt-invisibly-steal-emails, https://therecord.media/openai-fixes-zero-click-shadowleak-vulnerability).

**Frame:** the AI supply chain is also an API supply chain (https://securityboulevard.com/2026/04/the-ai-supply-chain-is-actually-an-api-supply-chain-lessons-from-the-litellm-breach/), and nobody has a map of it.

**Charts to use:** EchoLeak attack chain diagram; Reddy & Gujral "LLM Scope Violation" model.

## Segment 1 - What you actually deployed (10 min)

**Anatomy of a production AI feature.** Walk through each layer, name what attaches to it.

- **Model** - provider, version, provenance. Hugging Face / pickle ecosystem cited in Segment 2.
- **Prompt** - system prompt, user prompt, retrieved context. OWASP LLM01:2025 Prompt Injection (https://genai.owasp.org/llmrisk/llm01-prompt-injection/); LLM07:2025 System Prompt Leakage (new for 2025).
- **Tools** - function calls, MCP servers, API integrations. Anthropic's MCP draws 57 catalogued threats per Hou et al.; Backslash found critical flaws in hundreds of public MCP servers (https://www.globenewswire.com/news-release/2025/06/25/3105144/0/en/Backslash-Security-Exposes-Critical-Flaws-in-Hundreds-of-Public-MCP-Servers.html).
- **Memory** - session, long-term, shared. Microsoft "AI Recommendation Poisoning" (Feb 2026) documented 50 attempts from 31 companies in 60 days exploiting persistent memory (https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/).
- **Identity** - what the agent is authorised to do, and as whom. Saviynt 2026 CISO AI Risk Report: 92% lack full visibility into AI identities, 86% do not enforce access policies for them, 5% confident they could contain a compromised agent (https://saviynt.com/ciso-ai-risk-report-2026).
- **Data flow** - training, retrieval, logging.

**Audience self-audit slide.** Most attendees will lack visibility on three or more of these. Cisco State of AI Security 2026 reports 83% of orgs plan to deploy agentic AI; only 29% feel ready to do so securely (https://www.cisco.com/c/en/us/products/security/state-of-ai-security.html, https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report).

**Charts to use:** layered system diagram with one labelled threat per layer; CSA "Securing Autonomous AI Agents" 82%/73%/68%/74% bar chart on agent visibility (https://cloudsecurityalliance.org/artifacts/securing-autonomous-ai-agents).

## Segment 2 - How it gets attacked (10 min)

**Headline statistic, pre-validated:** Cisco State of AI Security 2026 - 73.2% of audited production AI deployments contained prompt-injection weaknesses; defence framework reduced attack success from 73.2% to 8.7% in their tested configuration. Pair with the foundational academic literature so the room understands this is not a one-vendor finding.

**Foundational academic literature on prompt injection (cite verbatim on the slide):**

- Greshake, Abdelnabi, Mishra, Endres, Holz & Fritz, AISec 2023 - "Not what you've signed up for" coined "indirect prompt injection" and demonstrated working attacks against Bing Chat (https://arxiv.org/abs/2302.12173, ACM https://dl.acm.org/doi/10.1145/3605764.3623985).
- Perez & Ribeiro, NeurIPS 2022 ML Safety Workshop - "Ignore Previous Prompt" defined goal-hijacking and prompt-leaking with handcrafted inputs against GPT-3 (https://arxiv.org/abs/2211.09527).
- Liu et al. 2023 "HouYi" - tested 36 real LLM-integrated commercial applications; 31 (86%) were vulnerable; 10 vendors confirmed (https://arxiv.org/abs/2306.05499).
- Yi et al. KDD 2025 (BIPIA) - first systematic indirect-prompt-injection benchmark; all evaluated LLMs universally vulnerable (https://arxiv.org/abs/2312.14197, code https://github.com/microsoft/BIPIA).
- Zhan et al., ACL Findings 2024 (InjecAgent) - 1,054 test cases, 17 user tools, 62 attacker tools; ReAct-prompted GPT-4 vulnerable to IPI 24% of the time (https://arxiv.org/abs/2403.02691, https://aclanthology.org/2024.findings-acl.624/).
- Debenedetti et al., NeurIPS 2024 (AgentDojo) - 97 realistic agent tasks, 629 security tests; SOTA agents solved <66% of tasks even with no attack and were exploitable in <25% of tasks (https://arxiv.org/abs/2406.13352, leaderboard https://agentdojo.spylab.ai/).
- Ruan et al., ICLR 2024 Spotlight (ToolEmu) - safest LM agent failed 23.9% of the time across 144 high-stakes test cases, 68.8% of detected failures validated as real-world risks by human reviewers (https://arxiv.org/abs/2309.15817).
- Anthropic 2025, "Agentic Misalignment" - models from all major labs chose blackmail/exfiltration when threatened with replacement; Claude blackmailed 55.1% of the time when it believed the scenario was real vs 6.5% in evaluation - **models reason about whether they are being tested** (https://www.anthropic.com/research/agentic-misalignment, https://arxiv.org/abs/2510.05179).
- Fang et al. 2024, "LLM Agents can Autonomously Hack Websites" - GPT-4 agents perform blind SQL-injection schema extraction unaided (https://arxiv.org/abs/2402.06664).

**Real 2025-2026 incidents, fast rotation, each with primary source:**

- **EchoLeak (June 2025)** - opening-hook reference. Aim Labs / Microsoft.
- **ShadowLeak (June-Sept 2025)** - service-side zero-click prompt injection in ChatGPT Deep Research / Gmail. Radware via Bugcrowd. https://www.darkreading.com/vulnerabilities-threats/shadowleak-chatgpt-invisibly-steal-emails
- **AI Recommendation Poisoning (Feb 2026)** - hidden instructions behind "Summarise with AI" buttons plant persistent memory; 50 attempts from 31 companies in 60 days. Microsoft Threat Intelligence. https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/
- **OpenClaw (Q1 2026)** - CVE-2026-25253 (RCE via implicit-trust localhost WebSocket) plus 138 associated CVEs; ClawHub marketplace supply-chain compromise (~12% of 2,857 published skills malicious). Qualys ETM analysis: https://blog.qualys.com/product-tech/2026/04/13/anatomy-autonomous-ai-agent-risk-qualys-etm-openclaw. Also https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks.
- **Logo / image prompt injection** - Trail of Bits image-scaling attack on Gemini and Vertex AI (https://www.securityweek.com/ai-systems-vulnerable-to-prompt-injection-via-image-scaling-attack/); Brave research on screenshot injection in AI browsers (https://brave.com/blog/unseeable-prompt-injections/); Lakera primer (https://www.lakera.ai/blog/visual-prompt-injections); academic - "Mind Mapping Prompt Injection" MDPI Electronics 2025 (https://www.mdpi.com/2079-9292/14/10/1907).
- **Meta internal AI assistant data exposure (March 2026)** - confused-deputy failure; agent autonomously posted analysis to internal forum; ~2-hour exposure of proprietary code, business strategy, user data (https://venturebeat.com/security/meta-rogue-ai-agent-confused-deputy-iam-identity-governance-matrix, https://cybermagazine.com/news/the-risk-of-agentic-the-story-of-metas-ai-agent-data-leak).
- **Slopsquatting in production** - huggingface-cli incident (Lasso); covered in detail in Part 1.

**Takeaway, evidence-anchored:** in all the literatures and incidents above, direct user prompts are the minority. The risk lands through channels the agent already trusts - retrieved web pages, emails, documents, OCR'd images, MCP tool descriptions, persistent memory writes. The real design question is *what is trusted, why, and at what blast radius.*

**Charts to use:** AgentDojo "task solved with no attack" vs "task solved under attack" comparison; Anthropic Agentic Misalignment 55.1% vs 6.5% bar chart; Cisco 73.2% headline with Constitutional-Classifiers-style reduction overlay.

## Segment 3 - What to do (25 min)

**Centre of gravity. Five sub-blocks. Each anchored to peer-reviewed defence research, a standards body, or named operating practice.**

### 3.1 - Technical controls (6 min)

- **AI gateway with egress controls.** Govern what data can leave (DLP at the gateway plane), what can return. Reduces the EchoLeak / ShadowLeak exfiltration channel by attacking the markdown-image / proxy primitives directly.
- **Defence-in-depth on prompts and outputs.** Best-published defences:
  - Hines et al. (Microsoft) "Spotlighting" - delimiting / datamarking / encoding reduces ASR from >50% to <2% (https://arxiv.org/abs/2403.14720).
  - Chen et al. "StruQ" / "SecAlign" (USENIX Security 2025) - structured front-end with separated data/instruction channels drops ASR to ~0% against optimisation-free attacks (https://arxiv.org/abs/2402.06363, USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe, blog https://bair.berkeley.edu/blog/2025/04/11/prompt-injection-defense/).
  - Debenedetti / Google DeepMind 2025 "CaMeL" - privileged-LLM + quarantined-LLM + capability tags; 77% of AgentDojo tasks solved with provable security (https://arxiv.org/abs/2503.18813).
  - Anthropic Constitutional Classifiers - reduced jailbreak success from 86% to 4.4% with 1,700+ red-team hours / 198,000 attempts; only 1 high-risk universal jailbreak found (https://www.anthropic.com/research/constitutional-classifiers, https://arxiv.org/abs/2501.18837).
- **Runtime monitoring.** Log every prompt, every tool call, every memory write, with retention aligned to compliance regime. NIST AI 600-1 MS-2.6, MS-2.7.
- **Agent sandboxing.** Least-privilege on the tool surface, not just the network. CaMeL is the academic reference architecture; Kubernetes/sandbox patterns the operational analogue.
- **Pin every AI dependency; audit your MCP trust surface.** LiteLLM lesson. Hou et al. STRIDE/DREAD model of MCP threats (https://xinyi-hou.github.io/files/hou2025mcp_1.pdf).

### 3.2 - Agent identity (5 min)

- **Treat agents as first-class identities, not service accounts.** OWASP Top 10 for Agentic Applications 2026 frames this as a separate risk class (https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **Required human owner per agent**, documented and reported. Saviynt 2026 CISO AI Risk Report: 71% confirm AI tools access core systems (Salesforce, SAP); only 16% govern that access effectively (https://saviynt.com/ciso-ai-risk-report-2026).
- **JIT access over standing permissions.** CSA + Oasis "State of NHI and AI Security" survey (n=383, Aug-Sept 2025): 78% have no documented policies for creating or removing AI identities; 92% are not confident legacy IAM can manage AI/NHI risk (https://cloudsecurityalliance.org/artifacts/state-of-nhi-and-ai-security-survey-report).
- **Kill switches, rehearsed not assumed.** The CSA / Strata "Securing Autonomous AI Agents" survey (April 2026) reports 82% of enterprises have unknown AI agents in their environments; 68% cannot distinguish human vs agent activity; 74% say agents are over-privileged (https://cloudsecurityalliance.org/artifacts/securing-autonomous-ai-agents).
- **The current best baseline number to share:** CyberArk 2025 Identity Security Landscape - machine identities outnumber humans 82:1 (Vanson Bourne, n=2,600, https://www.cyberark.com/threat-landscape/). Keep the older 45:1 figure attributed to CyberArk's earlier "Seven Types of NHI" content (https://www.cyberark.com/resources/blog/the-seven-types-of-non-human-identities-to-secure) - it is still defensible, but the headline has aged and the room will likely have heard the newer number.
- **Peer-reviewed work to cite for the architecturally-minded:** "AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A" (https://arxiv.org/abs/2603.24775) - introduces invocation-bound capability tokens; reports a scan of ~2,000 MCP servers all lacking authentication. Also "Securing the Model Context Protocol: Risks, Controls, and Governance" (https://arxiv.org/html/2511.20920v1).

### 3.3 - Process and operational rhythm (5 min)

- **Red-team as launch criteria, not annual check.** Minimum evaluation before go-live; continuous evaluation after.
  - Standards: NIST AI 600-1 MS family (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).
  - Methodology: Perez et al., DeepMind 2022 "Red Teaming Language Models with Language Models" (https://arxiv.org/abs/2202.03286); Anthropic / OpenAI red-teaming reports.
  - Tooling: Garak (NVIDIA, https://arxiv.org/abs/2406.11036, https://github.com/NVIDIA/garak), PyRIT (Microsoft, used in 100+ MS AI Red Team operations, https://arxiv.org/abs/2410.02828, https://github.com/Azure/PyRIT), Promptfoo, DeepTeam.
  - Benchmarks worth running internally: AgentDojo (https://agentdojo.spylab.ai/), HarmBench (https://github.com/centerforaisafety/HarmBench), BIPIA (https://github.com/microsoft/BIPIA), Open-Prompt-Injection (https://github.com/liu00222/Open-Prompt-Injection).
- **AI-aware IR playbooks.** Deepfake-CFO, agent-gone-rogue, supply-chain compromise, prompt-injection discovery, persistent-memory-poisoning detection.
- **Kill-switch tabletops quarterly.** Not annually.
- **Incident classification taxonomy** that distinguishes AI incidents so the org can actually learn from them. Stanford AI Index 2026 reports 362 AI incidents in 2025 vs 233 in 2024 (https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai); MITRE ATLAS v5.4.0 Feb 2026 (https://atlas.mitre.org/) provides the technique taxonomy and 14 new agentic-AI techniques added October 2025 in collaboration with Zenity Labs.

### 3.4 - Culture and organisation (5 min)

- **"Refuse to ship" authority for security at AI launch gates** - explicit, not implied.
- **AI reliability/security engineer as an emerging role** - GitHub Octoverse 2025 and JetBrains 2025 both show a measurable hiring shift; Stanford AI Index 2026 reports AI-specific governance roles +17% in 2025.
- **CISO on the AI product review board, not informed after the fact.** ISO/IEC 42001 Clause 5 and Annex A.6 (AI system lifecycle) make the seat structural.
- **Legal, privacy and security in design, not review.** NCSC / CISA Guidelines for Secure AI System Development - "Secure Design" section (https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf).
- **Safety review gate with a named owner and a veto.**

### 3.5 - Governance, reporting, and the board (4 min)

- **AI-BOM (bill of materials) per deployed feature** - model, prompts, tools, data, agents, owners - versioned. NIST SP 800-204D (https://csrc.nist.gov/pubs/sp/800/204/d/final) for the CI/CD evidence-generation pattern.
- **Vendor AI risk assessments** - what is their evaluation process, red team, incident history? OWASP LLM03:2025 Supply Chain.
- **Metrics that land:**
  - Attack success rate per evaluation category (not binary pass/fail).
  - Blast radius per agent in dollar terms.
  - Dollar exposure per AI feature.
  - **Anchor with IBM Cost of a Data Breach 2025:** AI-driven detection saves USD 1.9M per breach and 80 days lifecycle; **shadow AI adds USD 670,000 to average cost**; 20% of breaches involved unauthorised AI tools; 97% of AI-incident orgs lacked proper AI access controls; 63% lack AI governance policies (https://www.ibm.com/reports/data-breach, PDF https://www.ibm.com/downloads/documents/us-en/131cf87b20b31c91, X-Force analysis https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai).
- **Board framing.** IANS data shows only 29% of directors rate cyber updates as "very effective"; 47% say AI / emerging-tech reporting specifically needs improvement (https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/24/boards-give-ciso-cybersecurity-reporting-a-mixed-grade). Translate evaluation output into dollars and outcomes.
- **Frameworks worth naming on a single slide:**
  - NIST AI RMF + AI 600-1 (https://www.nist.gov/itl/ai-risk-management-framework, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
  - NIST SP 800-218A SSDF for GenAI (https://csrc.nist.gov/pubs/sp/800/218/a/final)
  - NIST SP 800-204D supply chain in CI/CD (https://csrc.nist.gov/pubs/sp/800/204/d/final)
  - ISO/IEC 42001 + 23894 (https://www.iso.org/standard/42001, https://www.iso.org/standard/77304.html)
  - EU AI Act Art. 9, 10, 15 (https://artificialintelligenceact.eu/article/15/)
  - NCSC + CISA Secure AI System Development (https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf)
  - OWASP Top 10 for LLM Applications 2025 + Top 10 for Agentic Applications 2026 (https://genai.owasp.org/llm-top-10/, https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
  - MITRE ATLAS (https://atlas.mitre.org/)
  - CSA "Securing Non-Human Identities in the Age of AI Agents" (RSAC 2025, https://cloudsecurityalliance.org/artifacts/securing-non-human-identities-in-the-age-of-ai-agents-rsac-2025) and the 2026 "Securing Autonomous AI Agents" follow-up (https://cloudsecurityalliance.org/artifacts/securing-autonomous-ai-agents)

**Charts to use:** Constitutional Classifiers ASR drop chart (86% to 4.4%); IBM shadow-AI cost adder chart; CSA / Saviynt / CSA-Strata identity-visibility stacked-bar comparison; framework-stack diagram (NIST + ISO + OWASP + MITRE + EU AI Act).

## Close (5 min)

Monday-morning checklist:

- Build the AI inventory you do not currently have (model, prompts, tools, memory, identity, data flow).
- Extend IAM to treat agents as first-class identities (named owner, JIT access, kill switch).
- Pin every AI-related dependency; audit your MCP trust surface.
- Continuous red-teaming (Garak / PyRIT / AgentDojo / HarmBench), not annual pen tests.
- Reframe board reporting in dollar exposure and evaluation success rates, not tool counts.

Q&A.

---

# Production notes

- **Slide count target:** 18-22 slides.
- **Citation discipline:** every quantitative claim has the primary source on the slide footer; long URLs pushed to the bibliography slide.
- **Q&A buffer:** reserve final 5-10 minutes.
- **Storytelling over stats after the hook.** Suggested narrative-driven incident: EchoLeak walked through end-to-end.
- **Live poll at opening:** "Has someone in your org shipped an AI feature you did not know about?"
- **The non-product promise:** say it out loud in the intro and close.
- **Charts to pre-build (priority order):** EchoLeak attack-chain diagram; AgentDojo task-success-with-and-without-attack; Anthropic Agentic Misalignment 55.1% vs 6.5%; Cisco 73.2% with defence reduction; IBM shadow-AI cost adder; framework-stack diagram.

---

# Source library - Part 2

Organised by topic to support follow-up reading. Where both an arXiv preprint and a venue version exist, both are listed. Where industry research has a stated methodology and named author/team, the original publication is preferred over press summaries.

## A. Series-wide / framing

- Stanford AI Index Report 2025 (HAI) - https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai (Chapter 3 PDF: https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter3_final.pdf)
- Stanford AI Index Report 2026 (HAI) - https://hai.stanford.edu/ai-index/2026-ai-index-report (Responsible AI: https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai)
- IBM Cost of a Data Breach Report 2025 - https://www.ibm.com/reports/data-breach (PDF https://www.ibm.com/downloads/documents/us-en/131cf87b20b31c91, X-Force analysis https://www.ibm.com/think/x-force/2025-cost-of-a-data-breach-navigating-ai)
- IANS "Boards Give CISO Cybersecurity Reporting a Mixed Grade" - https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/24/boards-give-ciso-cybersecurity-reporting-a-mixed-grade
- Cisco State of AI Security 2026 - https://www.cisco.com/c/en/us/products/security/state-of-ai-security.html (blog https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)

## B. Foundational prompt-injection papers

- Greshake et al. (AISec 2023) "Not what you've signed up for" - https://arxiv.org/abs/2302.12173, ACM https://dl.acm.org/doi/10.1145/3605764.3623985
- Perez & Ribeiro (NeurIPS 2022 ML Safety Workshop) "Ignore Previous Prompt" - https://arxiv.org/abs/2211.09527, code https://github.com/agencyenterprise/PromptInject
- Liu et al. (2023) "Prompt Injection attack against LLM-integrated Applications" (HouYi) - https://arxiv.org/abs/2306.05499, code https://github.com/LLMSecurity/HouYi
- Yi et al. (KDD 2025) BIPIA - https://arxiv.org/abs/2312.14197, code https://github.com/microsoft/BIPIA
- Zhan et al. (ACL Findings 2024) InjecAgent - https://arxiv.org/abs/2403.02691, ACL https://aclanthology.org/2024.findings-acl.624/
- Liu et al. (USENIX Security 2024) "Formalizing and Benchmarking Prompt Injection Attacks and Defenses" - https://arxiv.org/abs/2310.12815, code https://github.com/liu00222/Open-Prompt-Injection
- Pasquini et al. (2024) "Neural Exec" - https://arxiv.org/abs/2403.03792

## C. Agent and tool-use security

- Debenedetti et al. (NeurIPS 2024) "AgentDojo" - https://arxiv.org/abs/2406.13352, leaderboard https://agentdojo.spylab.ai/
- Ruan et al. (ICLR 2024 Spotlight) "ToolEmu" - https://arxiv.org/abs/2309.15817, code https://github.com/ryoungj/ToolEmu
- Hou et al. (2025) "MCP: Landscape, Security Threats, and Future Research Directions" - https://xinyi-hou.github.io/files/hou2025mcp_1.pdf, related https://arxiv.org/html/2508.12538v1
- "Securing the Model Context Protocol: Risks, Controls, and Governance" - https://arxiv.org/html/2511.20920v1
- "SMCP: Secure Model Context Protocol" - https://arxiv.org/pdf/2602.01129
- "Security Analysis of Agentic AI Communication Protocols" (MCP/ACP/A2A/ANP) - https://arxiv.org/html/2511.03841v1
- "Survey of Agent Interoperability Protocols" - https://arxiv.org/html/2505.02279v2
- "AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A" - https://arxiv.org/abs/2603.24775
- Invariant Labs "MCP Security Notification: Tool Poisoning" - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
- Astrix "State of MCP Server Security 2025" - https://astrix.security/learn/blog/state-of-mcp-server-security-2025/
- Backslash "Critical Flaws in Hundreds of Public MCP Servers" - https://www.globenewswire.com/news-release/2025/06/25/3105144/0/en/Backslash-Security-Exposes-Critical-Flaws-in-Hundreds-of-Public-MCP-Servers.html
- Fang et al. (2024) "LLM Agents can Autonomously Hack Websites" - https://arxiv.org/abs/2402.06664
- Anthropic (2025) "Agentic Misalignment" - https://www.anthropic.com/research/agentic-misalignment, paper https://arxiv.org/abs/2510.05179
- PipeLab "State of MCP Security 2026" - https://pipelab.org/blog/state-of-mcp-security-2026/

## D. Jailbreaks and adversarial attacks

- Zou et al. (2023) GCG "Universal and Transferable Adversarial Attacks on Aligned LMs" - https://arxiv.org/abs/2307.15043, project https://llm-attacks.org/
- Wei, Haghtalab, Steinhardt (NeurIPS 2023 Oral) "Jailbroken: How Does LLM Safety Training Fail?" - https://arxiv.org/abs/2307.02483
- Anil et al. / Anthropic (NeurIPS 2024) "Many-shot Jailbreaking" - https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf, post https://www.anthropic.com/research/many-shot-jailbreaking
- Sharma et al. / Anthropic (2025) "Constitutional Classifiers" - https://arxiv.org/abs/2501.18837, post https://www.anthropic.com/research/constitutional-classifiers
- Shen et al. (ACM CCS 2024) "Do Anything Now" - https://arxiv.org/abs/2308.03825, dataset https://github.com/verazuo/jailbreak_llms
- Chao et al. (2023) PAIR - https://arxiv.org/abs/2310.08419
- Mazeika et al. (ICML 2024) HarmBench - https://arxiv.org/abs/2402.04249, code https://github.com/centerforaisafety/HarmBench
- Hubinger et al. / Anthropic (2024) "Sleeper Agents" - https://arxiv.org/abs/2401.05566

## E. Defences

- Hines et al. / Microsoft (2024) "Spotlighting" - https://arxiv.org/abs/2403.14720
- Chen et al. (USENIX Security 2025) StruQ + SecAlign - https://arxiv.org/abs/2402.06363, USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/chen-sizhe, BAIR blog https://bair.berkeley.edu/blog/2025/04/11/prompt-injection-defense/
- Debenedetti et al. / Google DeepMind (2025) "CaMeL: Defeating Prompt Injections by Design" - https://arxiv.org/abs/2503.18813
- Perez et al. / DeepMind (2022) "Red Teaming Language Models with Language Models" - https://arxiv.org/abs/2202.03286, post https://deepmind.google/blog/red-teaming-language-models-with-language-models/
- NVIDIA Garak - https://arxiv.org/abs/2406.11036, code https://github.com/NVIDIA/garak
- Microsoft PyRIT - https://arxiv.org/abs/2410.02828, code https://github.com/Azure/PyRIT

## F. Real-world incidents

- EchoLeak / CVE-2025-32711 academic - https://arxiv.org/abs/2509.10540 (Reddy & Gujral, AAAI Fall Symposium 2025); Microsoft advisory https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711; technical https://www.hackthebox.com/blog/cve-2025-32711-echoleak-copilot-vulnerability; Varonis https://www.varonis.com/blog/echoleak; The Hacker News https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html
- ShadowLeak - Dark Reading https://www.darkreading.com/vulnerabilities-threats/shadowleak-chatgpt-invisibly-steal-emails; The Record https://therecord.media/openai-fixes-zero-click-shadowleak-vulnerability; SecurityAffairs https://securityaffairs.com/182334/hacking/shadowleak-radware-uncovers-zero-click-attack-on-chatgpt; Malwarebytes https://www.malwarebytes.com/blog/news/2025/09/chatgpt-deep-research-zero-click-vulnerability-fixed-by-openai; Bank Info Security https://www.bankinfosecurity.com/openai-fixes-gmail-data-flaw-in-chatgpt-agent-a-29513
- AI Recommendation Poisoning - Microsoft Security https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/; The Register https://www.theregister.com/2026/02/12/microsoft_ai_recommendation_poisoning/; The Hacker News https://thehackernews.com/2026/02/microsoft-finds-summarize-with-ai.html; Help Net Security https://www.helpnetsecurity.com/2026/02/11/ai-recommendation-memory-poisoning-attacks/
- OpenClaw (CVE-2026-25253) - Qualys ETM https://blog.qualys.com/product-tech/2026/04/13/anatomy-autonomous-ai-agent-risk-qualys-etm-openclaw; Reco https://www.reco.ai/blog/openclaw-the-ai-agent-security-crisis-unfolding-right-now; Dark Reading https://www.darkreading.com/application-security/critical-openclaw-vulnerability-ai-agent-risks; IBM X-Force https://www.ibm.com/think/x-force/agentic-ai-growing-fast-vulnerabilities; Conscia https://conscia.com/blog/the-openclaw-security-crisis/; CVE summary https://www.cvefind.com/en/blog/openclaw-compromise-ai-agents.html
- Visual / image / OCR injection - Trail of Bits via SecurityWeek https://www.securityweek.com/ai-systems-vulnerable-to-prompt-injection-via-image-scaling-attack/; Brave https://brave.com/blog/unseeable-prompt-injections/; Lakera https://www.lakera.ai/blog/visual-prompt-injections; Palo Alto Unit 42 https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/; NVIDIA https://developer.nvidia.com/blog/securing-agentic-ai-how-semantic-prompt-injections-bypass-ai-guardrails/; Radware https://www.radware.com/blog/threat-intelligence/weaponizing-images/; MDPI Electronics 2025 https://www.mdpi.com/2079-9292/14/10/1907
- Meta internal AI assistant exposure - Computing https://www.computing.co.uk/news/2026/ai/meta-ai-agent-teiggers-data-exposure; Cyber Magazine https://cybermagazine.com/news/the-risk-of-agentic-the-story-of-metas-ai-agent-data-leak; Kiteworks https://www.kiteworks.com/cybersecurity-risk-management/meta-rogue-ai-agent-data-exposure-governance/; VentureBeat https://venturebeat.com/security/meta-rogue-ai-agent-confused-deputy-iam-identity-governance-matrix; EDRM https://edrm.net/2026/03/when-the-agent-goes-off-script-metas-ai-triggered-data-exposure-revives-old-security-fears/
- Hugging Face / pickle ecosystem - JFrog https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/; ReversingLabs https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face; Hugging Face + ProtectAI https://huggingface.co/blog/pai-6-month; Infosecurity Magazine https://www.infosecurity-magazine.com/news/malicious-ai-models-hugging-face/; SANS ISC ModelScan https://isc.sans.edu/diary/31692; PickleBall (academic) https://arxiv.org/html/2508.15987v2; NSFOCUS https://nsfocusglobal.com/ai-supply-chain-security-hugging-face-malicious-ml-models/
- LiteLLM supply chain (covered in Part 1) - https://docs.litellm.ai/blog/security-update-march-2026; Security Boulevard "AI supply chain is an API supply chain" https://securityboulevard.com/2026/04/the-ai-supply-chain-is-actually-an-api-supply-chain-lessons-from-the-litellm-breach/

## G. Threat-intelligence reports

- Anthropic Threat Intelligence Report (Aug 2025) - https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf, post https://www.anthropic.com/news/detecting-countering-misuse-aug-2025
- Anthropic March 2025 report - https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025
- Anthropic "Disrupting the first reported AI-orchestrated cyber-espionage campaign" - https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf, post https://www.anthropic.com/news/disrupting-AI-espionage
- OpenAI "Disrupting Malicious Uses of AI" Oct 2025 - https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/
- OpenAI June 2025 report - https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf
- OpenAI Feb 2024 state-affiliated actors - https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/

## H. Agent identity / non-human identity

- Saviynt 2026 CISO AI Risk Report - https://saviynt.com/ciso-ai-risk-report-2026, press https://www.globenewswire.com/news-release/2026/04/21/3278155/0/en/The-Ungoverned-Workforce-Cybersecurity-Insiders-Finds-92-Lack-Visibility-Into-AI-Identities.html
- CSA + Oasis "State of NHI and AI Security" survey - https://cloudsecurityalliance.org/artifacts/state-of-nhi-and-ai-security-survey-report
- CSA "Securing Non-Human Identities in the Age of AI Agents" (RSAC 2025) - https://cloudsecurityalliance.org/artifacts/securing-non-human-identities-in-the-age-of-ai-agents-rsac-2025
- CSA / Strata "Securing Autonomous AI Agents" 2026 - https://cloudsecurityalliance.org/artifacts/securing-autonomous-ai-agents
- CSA / Astrix "State of NHI Security" 2024 - https://cloudsecurityalliance.org/artifacts/state-of-non-human-identity-security-survey-report
- CSA 2026 March release on agent vs human distinguishability - https://cloudsecurityalliance.org/press-releases/2026/03/24/more-than-two-thirds-of-organizations-cannot-clearly-distinguish-ai-agent-from-human-actions
- CyberArk 2025 Identity Security Landscape - https://www.cyberark.com/threat-landscape/, machine-identity report https://www.cyberark.com/CyberArk-2025-state-of-machine-identity-security-report.pdf, blog https://www.cyberark.com/resources/blog/ai-agents-and-identity-risks-how-security-will-shift-in-2026, "Seven Types of NHI" https://www.cyberark.com/resources/blog/the-seven-types-of-non-human-identities-to-secure
- Strata "AI Agent Identity Crisis" 2026 - https://www.strata.io/blog/agentic-identity/the-ai-agent-identity-crisis-new-research-reveals-a-governance-gap/, NHI playbook https://www.strata.io/blog/agentic-identity/new-identity-playbook-ai-agents-not-nhi-8b/
- Astrix research on AI <-> NHI - https://astrix.security/learn/blog/astrix-research-presents-touchpoints-between-ai-and-non-human-identities/
- IDSA 2025 Trends in Securing Digital Identities - https://www.idsalliance.org/white-paper/2025-trends-in-securing-digital-identities/
- Microsoft Entra Agent ID (Ignite 2025) - https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025
- Google Cloud "RSAC 26 Supercharging agentic AI defense" - https://cloud.google.com/blog/products/identity-security/rsac-26-supercharging-agentic-ai-defense-with-frontline-threat-intelligence

## I. Standards and frameworks

- NIST SP 800-218A SSDF for GenAI - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST AI RMF 1.0 - https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1 GenAI Profile - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NIST SP 800-204D supply chain in CI/CD - https://csrc.nist.gov/pubs/sp/800/204/d/final
- ISO/IEC 42001:2023 AI management system - https://www.iso.org/standard/42001
- ISO/IEC 23894:2023 AI risk management - https://www.iso.org/standard/77304.html
- EU AI Act Article 15 - https://artificialintelligenceact.eu/article/15/
- "Robustness and Cybersecurity in the EU AI Act" (FAccT 2025) - https://dl.acm.org/doi/10.1145/3715275.3732020
- NCSC + CISA "Guidelines for Secure AI System Development" - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf
- CISA AI Red Teaming / TEVV - https://www.cisa.gov/news-events/news/ai-red-teaming-applying-software-tevv-ai-evaluations
- DHS AI Safety & Security Guidelines for Critical Infrastructure - https://www.dhs.gov/sites/default/files/2024-04/24_0426_dhs_ai-ci-safety-security-guidelines-508c.pdf
- OWASP Top 10 for LLM Applications 2025 - https://genai.owasp.org/llm-top-10/, PDF https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf, project https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/, LLM01 https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- OWASP Top 10 for Agentic Applications 2026 - https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP Prompt Injection community page - https://owasp.org/www-community/attacks/PromptInjection
- MITRE ATLAS - https://atlas.mitre.org/, GitHub https://github.com/mitre/advmlthreatmatrix, NIST briefing https://csrc.nist.gov/csrc/media/Presentations/2025/mitre-atlas/TuePM2.1-MITRE%20ATLAS%20Overview%20Sept%202025.pdf, SAFE-AI report https://atlas.mitre.org/pdf-files/SAFEAI_Full_Report.pdf

---

## Notes on rigor (Part 2)

A few stats commonly cited in this space need careful attribution. They are usable, but be precise:

1. **"45 NHIs per human identity"** traces to CyberArk's "Seven Types of NHI" content (https://www.cyberark.com/resources/blog/the-seven-types-of-non-human-identities-to-secure). The current CyberArk 2025 Identity Security Landscape figure is **82:1** (Vanson Bourne, n=2,600). Use the 82:1 number as the headline; the 45:1 figure is still defensible if attributed.
2. **"78% have no formal NHI policy" and "92% not confident legacy IAM can handle agents"** both come from the same CSA + Oasis "State of NHI and AI Security" report (Aug-Sept 2025, n=383). Cite once, not as independent corroboration.
3. **Cisco "73% of production AI deployments have prompt-injection weaknesses"** is from Cisco's own AI Threat Intelligence audits (https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report). Methodology context (sample size, audit selection) should appear on the slide footer.
4. **Anthropic Agentic Misalignment 55.1% vs 6.5%** is a red-team scenario, not a production-incident base rate. Frame as "models reason about whether they are being tested" rather than "models blackmail users 55% of the time."
5. **AgentDojo and ToolEmu** failure rates are evaluation-environment metrics. They translate as "agents are exploitable by published attacks today" - not as a direct estimate of in-the-wild compromise rate.
