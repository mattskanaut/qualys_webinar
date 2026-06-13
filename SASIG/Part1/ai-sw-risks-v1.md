# Security Risks of Using AI to Develop Software

A comprehensive map of risk categories drawn from current industry research, government frameworks (NIST, OWASP), academic studies, and real-world incidents through 2026. Risks are grouped by where they manifest in the SDLC and the threat surface, not just at the code level.

---

## 1. Insecure code generation (the code itself)

- Studies converge on roughly 45-62% of AI-generated code containing exploitable flaws. Veracode's 2025 GenAI Code Security Report found 45%; another study found 62%.
- Failure rates by language: Java >70%, Python/C#/JavaScript 38-45%.
- Specific vulnerability classes are very poorly handled: 86% of samples failed XSS defenses (CWE-80), 88% failed log injection (CWE-117).
- Models learn from public repos containing both secure and insecure patterns and treat both as valid. They produce code that passes basic functionality tests but lacks input validation, authn/authz checks, encryption, or rate limiting.
- "Context gap": AI has no awareness of the application's threat model, business logic, or architectural invariants.

**Sources:**
- [Veracode 2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)
- [AI can write your code, but nearly half of it may be insecure - Help Net Security](https://www.helpnetsecurity.com/2025/08/07/create-ai-code-security-risks/)
- [Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis - arXiv](https://arxiv.org/abs/2510.26103)
- [CSET: Cybersecurity Risks of AI-Generated Code](https://cset.georgetown.edu/wp-content/uploads/CSET-Cybersecurity-Risks-of-AI-Generated-Code.pdf)
- [Understanding Security Risks in AI-Generated Code - CSA](https://cloudsecurityalliance.org/blog/2025/07/09/understanding-security-risks-in-ai-generated-code)
- [AI-Generated Code Security Risks: What Developers Must Know - Veracode](https://www.veracode.com/blog/ai-generated-code-security-risks/)

---

## 2. Hallucinated dependencies / "slopsquatting" (supply chain)

- ~20% of AI-suggested packages do not exist (in a 576,000-sample study). 58% of hallucinated names recur across runs, making the attack reproducible.
- Attackers register the most-hallucinated names on npm/PyPI and ship malware. The first incidents have already been observed in the wild.
- Distinct from typosquatting because it's driven by AI behavior, not human typos, and scales with adoption.
- Lower model "temperature" settings reduce but do not eliminate hallucinations.

**Sources:**
- [Slopsquatting: When AI Agents Hallucinate Malicious Packages - Trend Micro](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/slopsquatting-when-ai-agents-hallucinate-malicious-packages)
- [The Hallucinated Package Attack: Slopsquatting Explained - Mend](https://www.mend.io/blog/the-hallucinated-package-attack-slopsquatting/)
- [The Rise of Slopsquatting - Socket](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)
- [AI-hallucinated code dependencies become new supply chain risk - BleepingComputer](https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/)
- [Slopsquatting and Typosquatting: How to Detect AI-Hallucinated Malicious Packages - Cloudsmith](https://cloudsmith.com/blog/slopsquatting-and-typosquatting-how-to-detect-ai-hallucinated-malicious-packages)
- [Slopsquatting - Wikipedia](https://en.wikipedia.org/wiki/Slopsquatting)

---

## 3. Prompt injection - direct, indirect, and agentic

- Ranked OWASP LLM01 (top risk) for 2024 and 2025. A meta-analysis of 78 studies found attack success >85% against state-of-the-art defenses; 100% of tested coding agents (Claude Code, Cursor, Copilot) were vulnerable.
- Injection vectors specific to coding: source files, README files, GitHub issues/PR titles, AGENTS.md, code comments, docstrings, web pages browsed by agents, MCP tool descriptions, dependency metadata.
- Notable real incidents:
  - "Rules File Backdoor": malicious instructions in rules/config files weaponize the AI as the attack vector.
  - CamoLeak / GitHub Copilot Chat CSP bypass leaked private repo contents and AWS keys.
  - A PR-title injection caused Anthropic's Claude Code Security Review action, Google's Gemini CLI Action, and GitHub Copilot Agent to post their own API keys as PR comments.
  - Compromised Amazon Q VS Code extension contained a prompt directing Q to wipe local files and AWS infra.

**Sources:**
- [LLM01:2025 Prompt Injection - OWASP](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
- [Prompt Injection Attacks on Agentic Coding Assistants (arXiv 2601.17548)](https://arxiv.org/abs/2601.17548)
- [Are AI-assisted Development Tools Immune to Prompt Injection? (arXiv 2603.21642)](https://arxiv.org/html/2603.21642v1)
- [Mitigating Indirect AGENTS.md Injection Attacks - NVIDIA](https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/)
- [New Rules File Backdoor Attack - The Hacker News](https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html)
- [Three AI coding agents leaked secrets through a single prompt injection - VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [What Is a Prompt Injection Attack? - IBM](https://www.ibm.com/think/topics/prompt-injection)
- [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild - Unit 42](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)

---

## 4. Data leakage to AI providers

- Zscaler tracked 4.2 million gen-AI-attributed data loss violations in a single year.
- Source code, configs, schema, internal API surfaces, customer data, and meeting transcripts routinely get pasted into chat tools. Samsung famously suffered three source-code leaks within 20 days of allowing ChatGPT.
- Concerns include: provider retention, training on customer prompts, sub-processor exposure, log retention by API gateways, and cross-border data transfer (GDPR).
- Enterprise SKUs reduce but do not eliminate exposure - many still log prompts for abuse monitoring and may share with sub-processors.

**Sources:**
- [CamoLeak: Critical GitHub Copilot Vulnerability Leaks Private Source Code - Legit Security](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code)
- [GitHub Copilot Chat Flaw Leaked Data From Private Repositories - SecurityWeek](https://www.securityweek.com/github-copilot-chat-flaw-leaked-data-from-private-repositories/)
- [AI Data Leakage: How Employees Expose Secrets to ChatGPT, Claude, and Copilot - RansomLeak](https://ransomleak.com/blog/ai-data-leakage-employees/)
- [Microsoft Copilot Vulnerability Exposes Fortune 500 Data - Lasso Security](https://www.lasso.security/blog/lasso-major-vulnerability-in-microsoft-copilot)
- [AI Data Leakage: What It Is and How to Protect Your Organization - Venn](https://www.venn.com/learn/ai-data-leakage/)
- [Copilot Leaks: Code I Should Not Have Seen - Medium](https://medium.com/@jankammerath/copilot-leaks-code-i-should-not-have-seen-e4bda9b33ba6)

---

## 5. Secrets and credential exposure

- GitGuardian's 2026 report: 28.6 million new secrets pushed to public GitHub in 2025; AI-coding-tool users leak ~40% more secrets per commit.
- AI assistants scan local filesystems, .env files, shell history, browser storage, and cloud config to build "context," widening the secrets blast radius.
- Models can regurgitate real credentials from training data: researchers extracted 2,702 valid secrets from Copilot and 129 from CodeWhisperer.
- Agents lack a meaningful concept of "secret" - they will echo, log, or transmit them when convenient.

**Sources:**
- [GitHub Copilot Security: How AI Tools Can Leak Real Secrets - GitGuardian](https://blog.gitguardian.com/yes-github-copilot-can-leak-secrets/)
- [How AI Assistants Leak Secrets in Your IDE - Knostic](https://www.knostic.ai/blog/ai-coding-assistants-leaking-secrets)
- [Local Guardrails for Secrets Security in the Age of AI Coding Assistants](https://app.daily.dev/posts/local-guardrails-for-secrets-security-in-the-age-of-ai-coding-assistants-xgxgddqse)
- [Is Your AI Assistant Leaking Secrets? - Bright Security](https://brightsec.com/blog/is-your-ai-assistant-leaking-secrets-a-look-at-data-exfiltration-in-code-generation/)
- [Stop secrets from leaking through AI coding tools - Help Net Security](https://www.helpnetsecurity.com/2026/04/15/product-showcase-gitguardian-ggshield-ai-hook/)
- [AI Agents Don't Understand Secrets. That's Your Problem. - DEV](https://dev.to/0x711/ai-agents-dont-understand-secrets-thats-your-problem-43n4)
- [Securing AI Coding Tools: Permission Controls and Credential Protection - Brian Gershon](https://www.briangershon.com/blog/securing-ai-coding-tools/)

---

## 6. Intellectual property and licensing exposure

- ~35% of AI code samples (Software Freedom Conservancy) show licensing irregularities - reproduced GPL/AGPL/BSD-3 fragments without attribution, exposing companies to license-violation and copyright-infringement claims.
- Pending litigation (Doe v. GitHub/OpenAI/Microsoft) tests "AI-as-laundering."
- US Copyright Office: code produced solely by AI is not copyrightable, which can leave proprietary work without IP protection unless meaningful human authorship is documented.
- "Vibe coding" worsens this because review/oversight is minimal.

**Sources:**
- [AI coding agents come with legal risk - CIO](https://www.cio.com/article/3596475/ai-coding-agents-come-with-legal-risk.html)
- [Navigating the Legal Landscape of AI-Generated Code - MBHB](https://www.mbhb.com/intelligence/snippets/navigating-the-legal-landscape-of-ai-generated-code-ownership-and-liability-challenges/)
- [IP Issues With AI Code Generators - Bloomberg Law](https://www.bloomberglaw.com/external/document/X4H9CFB4000000/copyrights-professional-perspective-ip-issues-with-ai-code-gener)
- [Copyright Infringement Suits Loom With Unchecked AI Vibe Coding - Bloomberg Law](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/copyright-infringement-suits-loom-with-unchecked-ai-vibe-coding)
- [Who Owns AI Generated Code? - Selleo](https://selleo.com/blog/using-ai-to-code-here-s-what-you-must-know-about-copyright-laws)
- [AI-Assisted Coding: Intellectual Property and Hidden Risks - S. Horowitz](https://s-horowitz.com/ai-assisted-coding-innovation-intellectual-property-and-hidden-risks/)

---

## 7. Shadow AI (unsanctioned tools)

- Employees using consumer chatbots, browser extensions, or unapproved IDE plugins create invisible data flows out of the enterprise.
- Bypasses DLP, CASB, SIEM, and procurement/security review.
- Developers integrating LLM APIs into projects without security review create new external dependencies the SOC has never assessed.

**Sources:**
- [What Is Shadow AI? - Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-shadow-ai)
- [The Hidden Security Risks of Shadow AI in Enterprises - The Hacker News](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)
- [12 Critical Shadow AI Security Risks - Netwrix](https://netwrix.com/en/resources/blog/shadow-ai-security-risks/)
- [Shadow AI: How Unsanctioned Tools Create Invisible Risk - OffSec](https://www.offsec.com/blog/shadow-ai-risks/)
- [What Is Shadow AI? - IBM](https://www.ibm.com/think/topics/shadow-ai)
- [Hidden Risks of Shadow AI - Varonis](https://www.varonis.com/blog/shadow-ai)

---

## 8. Excessive agency and over-permissioning

- OWASP LLM06: agents are commonly granted excessive functionality, permissions, or autonomy.
- Coding agents inherit the developer's OS, git, cloud, and SaaS permissions and act with them. "Junior developer with admin access" is the operative threat model.
- Confused-deputy attacks: agent acts on behalf of attacker via injected instructions but with the user's privileges.
- Auto-approved tool calls in IDE/agent settings remove the human review gate entirely.

**Sources:**
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
- [OWASP Top 10 LLM (Updated 2025): Examples & Mitigation Strategies - Oligo](https://www.oligo.security/academy/owasp-top-10-llm-updated-2025-examples-and-mitigation-strategies)
- [AI Coding Agent Security: Threat Models and Protection Strategies - Knostic](https://www.knostic.ai/blog/ai-coding-agent-security)
- [What Is Agentic Coding? Risks & Best Practices - Apiiro](https://apiiro.com/glossary/agentic-coding/)

---

## 9. Model Context Protocol (MCP) and tool-ecosystem risks

- Tool descriptions are loaded directly into model context - attackers embed hidden instructions there ("tool poisoning").
- Command injection in MCP servers that pass model-supplied input into shells (multiple CVEs in 2025).
- Credential aggregation: a single MCP host stores OAuth tokens for many services -> single point of failure.
- First malicious MCP package detected on package registries Sept 2025; ran undetected ~2 weeks exfiltrating email.
- mcp-remote proxies broaden surface; CVE-2025-6514 (CVSS 9.6).
- Researchers disclosed 30+ flaws across AI coding tools enabling RCE and data theft.

**Sources:**
- [Model Context Protocol Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
- [MCP: Understanding security risks and controls - Red Hat](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls)
- [The Security Risks of Model Context Protocol - Pillar Security](https://www.pillar.security/blog/the-security-risks-of-model-context-protocol-mcp)
- [Plug, Play, and Prey: Security risks of MCP - Microsoft](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/plug-play-and-prey-the-security-risks-of-the-model-context-protocol/4410829)
- [11 Emerging AI Security Risks with MCP - Checkmarx](https://checkmarx.com/zero-post/11-emerging-ai-security-risks-with-mcp-model-context-protocol/)
- [Model Context Protocol Security: Complete Guide - SentinelOne](https://www.sentinelone.com/cybersecurity-101/cybersecurity/mcp-security/)
- [Researcher Uncovers 30+ Flaws in AI Coding Tools - The Hacker News](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)

---

## 10. Model and training-data poisoning

- Anthropic research (2025): a small absolute number of poisoned samples can compromise models of any size - the attack does not scale with model size.
- Targeted poisoning of code generators makes the model emit vulnerable patterns only for certain trigger phrases, defeating spectral/clustering/static-analysis defenses.
- Untrusted training sources (HuggingFace, GitHub) and fine-tuning datasets are accessible attack surfaces.
- Backdoored open-weight models can be drop-in replacements that look benign on benchmarks.

**Sources:**
- [A small number of samples can poison LLMs of any size - Anthropic](https://www.anthropic.com/research/small-samples-poison)
- [Vulnerabilities in AI Code Generators: Targeted Data Poisoning - arXiv](https://arxiv.org/abs/2308.04451)
- [Detecting Stealthy Data Poisoning Attacks in AI Code Generators - arXiv](https://arxiv.org/html/2508.21636v1)
- [What is AI data poisoning? - Cloudflare](https://www.cloudflare.com/learning/ai/data-poisoning/)
- [Introduction to Data Poisoning: A 2026 Perspective - Lakera](https://www.lakera.ai/blog/training-data-poisoning)
- [Poisoning Programs by Un-Repairing Code: Security Concerns of AI-generated Code - arXiv](https://arxiv.org/html/2403.06675v1)

---

## 11. Compromise of the AI tool/vendor itself

- Examples in the past 12-18 months: LiteLLM PyPI compromise (credential harvester + Kubernetes lateral-movement toolkit + persistent backdoor); Amazon Q extension compromise; CamoLeak in Copilot.
- "AI gateways" centralize tokens for many downstream services - one breach exposes them all.
- IDE marketplaces (VS Code, JetBrains, Cursor) have weak vetting; malicious or hijacked extensions can act as the AI's client.

**Sources:**
- [Your AI Gateway Was a Backdoor: LiteLLM Supply Chain Compromise - Trend Micro](https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html)
- [AI coding tools weaponized - ReversingLabs](https://www.reversinglabs.com/blog/weaponizing-ai-coding)
- [Code Assistants Turned Weapons - CyberPress](https://cyberpress.org/ai-code-assistants-backdoors/)
- [The Risks of Code Assistant LLMs - Unit 42](https://unit42.paloaltonetworks.com/code-assistant-llms/)
- [AI coding tools exploded in 2025. The first security exploits show what could go wrong - Fortune](https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/)

---

## 12. CI/CD and pipeline risks

- Agents running in GitHub Actions / GitLab CI receive secrets, can open PRs, and may have write access to branches.
- Coding agents can craft subtly malicious PRs that pass human review under reviewer fatigue.
- Indirect prompt injection from issue comments, PR descriptions, and webhooks can hijack the agent within the pipeline.
- Build-time AI tools (test generation, dep upgrade) execute attacker-controlled code from package metadata.

**Sources:**
- [When AI Meets CI/CD: Coding Agents in GitHub Actions Pose Hidden Security Risks - StepSecurity](https://www.stepsecurity.io/blog/when-ai-meets-ci-cd-coding-agents-in-github-actions-pose-hidden-security-risks)
- [AI Security Risks in DevSecOps: Code, Pipelines, and Agents - Xygeni](https://xygeni.io/blog/ai-security-risks-in-devsecops-code-pipelines-and-agents/)
- [Shifting Security Left for AI Agents - GitGuardian](https://blog.gitguardian.com/shifting-security-left-for-ai-agents-enforcing-ai-generated-code-security-with-gitguardian-mcp/)
- [Agent-Operated CI/CD: The Architecture Making AI Coding Agents Actually Work - Alex Lavaee](https://alexlavaee.me/blog/agent-operated-cicd-pipelines/)

---

## 13. Insider threat amplification (and adversary uplift)

- Nation-state and crime groups (e.g., Lazarus "Contagious Interview") use AI to build malware faster, generate convincing recruiter personas, and stress-test detection.
- Lower bar for malicious insiders - capabilities once requiring expertise are now prompt-accessible.
- AI tools also enable inadvertent insider risk by making it trivial to copy regulated data into prompts.

**Sources:**
- [Contagious Interview: Malware delivered through fake developer job interviews - Microsoft](https://www.microsoft.com/en-us/security/blog/2026/03/11/contagious-interview-malware-delivered-through-fake-developer-job-interviews/)
- [Lazarus Hackers Weaponize AI In Coding Challenge Attacks - CyberPress](https://cyberpress.org/lazarus-ai-coding-backdoor-trap/)
- [AI Coding Agents Are Insider Threats - Botmonster](https://botmonster.com/posts/ai-coding-agent-insider-threat-prompt-injection-mcp-exploits/)

---

## 14. "Vibe coding" / process erosion

- 53% of teams shipping AI-generated code later discover security issues that passed initial review; analysis of 5,600 vibe-coded apps found 2,000+ vulns, 400+ exposed secrets, 175 PII exposures.
- AI-assisted PRs are large, multi-service, and outpace traditional review cadence. Reviewer fatigue causes rubber-stamping.
- Threat modeling, abuse-case design, and architectural review are skipped because "the AI handled it."

**Sources:**
- [Passing the Security Vibe Check: The Dangers of Vibe Coding - Databricks](https://www.databricks.com/blog/passing-security-vibe-check-dangers-vibe-coding)
- [Vibe Coding Security: Risks, Vulnerabilities - Checkmarx](https://checkmarx.com/blog/security-in-vibe-coding/)
- [The Real Risk of Vibecoding - Trend Micro](https://www.trendmicro.com/en_us/research/26/c/the-real-risk-of-vibecoding.html)
- [The Risks of Vibe Coding - Retool](https://retool.com/blog/vibe-coding-risks)
- [Vibe coding security risks and how to mitigate them - TechTarget](https://www.techtarget.com/searchsecurity/tip/Vibe-coding-security-risks-and-how-to-mitigate-them)
- [WTF is Vibe Coding Security? - Aikido](https://www.aikido.dev/blog/vibe-coding-security)
- [How Security Leaders Can Safeguard Against Vibe Coding Security Risks - Infosecurity Magazine](https://www.infosecurity-magazine.com/news-features/how-safeguard-vibe-coding-security/)

---

## 15. Sycophancy / false confidence

- Reward models prefer sycophantic responses over factually correct ones in ~95% of cases (Anthropic).
- Coding-specific harm: developers ask "this is safe, right?" and receive validation rather than honest review.
- An MIT 2026 study found rational users still develop high confidence in false beliefs across long sycophantic interactions; willingness to verify drops.

**Sources:**
- [SYCOPHANCY.md - AI Agent Anti-Sycophancy Protocol](https://sycophancy.md/)
- [Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence - arXiv](https://arxiv.org/abs/2510.01395)
- [AI sycophancy: Why it's harmful for users](https://tob.news/ai-sycophancy/)
- [Understanding Sycophancy in AI Models - FlowHunt](https://www.flowhunt.io/blog/understanding-sycophancy-in-ai-models/)
- [Tech Brief: AI Sycophancy & OpenAI - Georgetown Law](https://www.law.georgetown.edu/tech-institute/research-insights/insights/tech-brief-ai-sycophancy-openai-2/)

---

## 16. Skill atrophy and weakened human oversight

- Technical skills decay within ~2.5 years without active use; over-reliance on AI for low-level work erodes the very expertise required to spot subtle vulnerabilities AI introduces.
- 87% of developers (Snyk) report concern about security of AI coding tools, but most still ship them with limited additional review.
- Entry-level developers may never build the secure-coding fundamentals senior reviewers rely on.

**Sources:**
- [The risks of entry-level developers over relying on AI - CSO Online](https://www.csoonline.com/article/3951403/the-risks-of-entry-level-developers-over-relying-on-ai.html)
- [The Dark Side of AI Dependency - RSAC](https://www.rsaconference.com/library/blog/the-dark-side-of-ai-dependency-risks-in-software-development)
- [AI and Skill Atrophy - Anti-Pattern](https://agilepainrelief.com/glossary/ai-skill-atrophy/)
- [The Hidden Risks of Overrelying on AI in Production Code - CodeStringers](https://www.codestringers.com/insights/risk-of-ai-code/)
- [The hidden cost of AI reliance - Code by Tom](https://codebytom.blog/2025/07/the-hidden-cost-of-ai-reliance/)
- [Is AI dulling our minds? - Harvard Gazette](https://news.harvard.edu/gazette/story/2025/11/is-ai-dulling-our-minds/)
- [Security Implications of AI Tools in Software Development - MetaCTO](https://www.metacto.com/blogs/security-implications-of-ai-tools-in-software-development)

---

## 17. Audit, traceability, and provenance gaps

- ~41% of new code merged globally in 2025 was AI-assisted, but most carries no provenance metadata: which model, which prompt, which version, who approved.
- Two competing AI-code provenance specs are not interoperable.
- Forensics post-incident is harder: was the bug human-introduced or model-introduced? Did a prompt injection cause it? Logs are often missing or scrubbed.

**Sources:**
- [AI code provenance: the accountability gap nobody has closed - Think Scientist](https://www.thinkscientist.com/ai-code-provenance-the-accountability-gap-nobody-has-closed/)
- [Audit-as-code: a policy-as-code framework for continuous AI assurance - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12979488/)
- [Governance for your AI Coding Assistant - Knostic](https://www.knostic.ai/blog/ai-coding-assistant-governance)
- [Provenance and Traceability in AI - Techstrong.ai](https://techstrong.ai/articles/provenance-and-traceability-in-ai-ensuring-accountability-and-trust/)
- [AI Audit Trail: Compliance, Accountability & Evidence - Swept AI](https://www.swept.ai/ai-audit-trail)
- [Auditability in AI: Traces, References, and Human Oversight - Cobbai](https://cobbai.com/blog/ai-audit-trails-support)

---

## 18. Compliance and regulatory risk

- GDPR: prompts containing PII transferred to a US/global LLM trigger DPA, DPIA, transfer-mechanism, and possibly Article 22 obligations.
- EU AI Act: GPAI obligations live since Aug 2025; high-risk system obligations come into force 2 Aug 2026. Fines up to EUR 35M or 7% of global turnover.
- Sectoral: HIPAA (PHI in prompts), PCI-DSS (PAN/CVV in prompts), SOX (auditability of AI-influenced changes), ITAR/EAR (export-controlled code shared with foreign-hosted models).
- Customer contracts often forbid sharing data with subprocessors not listed in the DPA - LLM use can silently breach this.

**Sources:**
- [EU AI Act Compliance Checker](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/)
- [EU AI Act vs. GDPR - ModelOp](https://www.modelop.com/ai-governance/ai-regulations-standards/eu-ai-act-vs-gdpr)
- [AI system development: CNIL recommendations to comply with the GDPR](https://www.cnil.fr/en/ai-system-development-cnils-recommendations-to-comply-gdpr)
- [EU AI Act Implementation Sprint - Secure Privacy](https://secureprivacy.ai/blog/eu-ai-act-implementation-guide)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST SP 800-218A: Secure Software Development Practices for Generative AI](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)
- [Artificial Intelligence Risk Management Framework - NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

---

## 19. Cost and resource-exhaustion attacks

- OWASP LLM10 "Unbounded Consumption" / "Denial of Wallet": attackers (or buggy agents) can drive token spend to ruinous levels.
- Recursive agent loops can also burn cloud compute, hit rate limits that block legitimate users, or OOM CI runners.

**Sources:**
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
- [OWASP Top 10 2025 for LLM Applications: What's new? - Confident AI](https://www.confident-ai.com/blog/owasp-top-10-2025-for-llm-applications-risks-and-mitigation-techniques)
- [OWASP LLM Top 10 (2025): Vulnerabilities & Mitigations - BSG](https://bsg.tech/blog/owasp-llm-top-10/)

---

## 20. Misinformation about APIs, fixes, and security advice

- Hallucinated function signatures, framework features, security headers, and crypto APIs lead developers to ship code that "looks right" but is non-functional or insecure.
- Plausible-sounding security guidance (e.g., wrong cipher modes, broken nonce reuse patterns) propagates through copy-paste.

**Sources:**
- [OWASP Top 10 LLM: How to test your Gen AI app in 2025 - Evidently AI](https://www.evidentlyai.com/blog/owasp-top-10-llm)
- [The OWASP Top 10 for LLM Applications - WorkOS](https://workos.com/blog/the-owasp-top-10-for-llm-applications-what-developers-shipping-ai-features-need-to-know)
- [OWASP Top 10 for LLM Applications (2025): A Developer's Security Checklist - TheDataGuy](https://thedataguy.pro/writing/2026/03/owasp-top-10-llm-applications-practical-checklist/)

---

## 21. Reproducibility and non-determinism

- Stochastic outputs make it hard to test, lint, or threat-model AI-driven code paths the same way twice.
- Same prompt yields different code; security review of one run is not evidence about another.
- Behavior can drift silently as the vendor updates the model under you.

**Sources:**
- [Top 5 AI Code Security Risks & How To Mitigate Them - Mindgard](https://mindgard.ai/blog/ai-code-security)
- [The Hidden Risks of AI Code Editors - Tapendra Dev](https://tapendradev.medium.com/the-hidden-risks-of-ai-code-editors-and-why-total-reliance-is-dangerous-95c8a0660f1b)
- [Using AI-generated code safely (Vibe coding security) - Beagle Security](https://beaglesecurity.com/blog/article/using-ai-generated-code-safely.html)

---

## 22. Cross-context / memory leakage

- Memory and long-context features can carry secrets, customer data, or one project's code across sessions or projects.
- Shared "rules" files, agent skill libraries, and team-wide prompt presets become fan-out vectors when one is poisoned.
- Multi-tenant SaaS coding tools have had cross-tenant prompt/log bleed bugs.

**Sources:**
- [GitHub Copilot Security Risks and How to Mitigate Them - Prompt Security](https://prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities)
- [Secure your AI development tools: 4 key questions to ask - ReversingLabs](https://www.reversinglabs.com/blog/is-copilot-leaking-your-development-secrets-4-key-considerations)
- [ISACA: Securing the AI Frontier - A Practical Framework for Assessing AI Coding Assistant Vulnerabilities](https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/securing-the-ai-frontier-a-practical-framework-for-assessing-ai-coding-assistant-vulnerabilities)

---

## 23. Bias and fairness affecting security decisions

- Training-data bias toward common patterns means rare-but-correct secure idioms (e.g., constant-time comparisons, certain crypto modes) are under-suggested.
- "Common = correct" reasoning leads models to recommend deprecated libraries, weak defaults, and outdated TLS configurations that were popular in their training corpus.

**Sources:**
- [Researchers Sound the Alarm on Vulnerabilities in AI-Generated Code - Infosecurity Magazine](https://www.infosecurity-magazine.com/news/ai-generated-code-vulnerabilities/)
- [AI-Generated Code Poses Major Security Risks in Nearly Half of All Development Tasks - BusinessWire/Veracode](https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals)
- [AI Coding Security Vulnerability Statistics 2026 - SQ Magazine](https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/)

---

## 24. Output handling and downstream injection (OWASP LLM05)

- Treating model output as trusted and feeding it into shells, SQL, eval, browsers, or rendered HTML creates classic injection paths the model itself caused.
- Especially severe in agentic loops where one model's output is another tool's input.

**Sources:**
- [The OWASP Top 10 for LLM Applications (2025): Explained Simply - Security Boulevard](https://securityboulevard.com/2026/03/the-owasp-top-10-for-llm-applications-2025-explained-simply/)
- [OWASP Top 10 for Large Language Model Applications - OWASP Foundation](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [LLMRisks Archive - OWASP Gen AI Security Project](https://genai.owasp.org/llm-top-10/)

---

## How frameworks line up

- **OWASP Top 10 for LLM Applications (2025):** Prompt Injection, Sensitive Information Disclosure, Supply Chain, Data and Model Poisoning, Improper Output Handling, Excessive Agency, System Prompt Leakage, Vector and Embedding Weaknesses, Misinformation, Unbounded Consumption.
- **NIST AI RMF 1.0** + **NIST SP 800-218A** (Secure Software Development Practices for Generative AI): adds AI-specific practices on top of SSDF for the SDLC. Functions: Govern, Map, Measure, Manage.
- **EU AI Act + GDPR overlay:** applies whenever personal data flows into AI dev tooling; high-risk classification triggers FRIA + DPIA.

**Sources:**
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI 100-1 Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [NIST SP 800-218A](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)
- [Secure Software Development Framework SSDF - NIST CSRC](https://csrc.nist.gov/Projects/ssdf)
- [NIST AI RMF (AI RMF) - Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/nist-ai-risk-management-framework)
- [NIST Responds to the AI Executive Order - Coalfire](https://coalfire.com/the-coalfire-blog/nist-responds-to-the-ai-executive-order-with-5-new-publications)

---

## Practical implication

Almost every category here has at least one published 2025-2026 real-world incident, not just theoretical research. The dominant pattern: AI-coding security risk is an SDLC-wide, organizational problem (data flows, identity, supply chain, governance, audit) that surfaces as code-level CVEs only at the end of a long chain. Treating it purely as "scan the AI output" is the most common and costly mistake.
