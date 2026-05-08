# Part 1 - The New Software Development Lifecycle: Security When Every Developer Writes With AI

**Series:** The New Normal: Software, Security and the AI Stack
**Format:** One-hour, non-product webinar
**Duration:** 55 min content + 5 min Q&A
**Shape:** 5 / 10 / 10 / 25 / 5
**Audience:** SASIG community - CISOs and security leaders (vendors, contractors and press excluded)
**Host:** Matt Campbell

**Series framing (from titles-and-blurbs.md):** AI is already in your stack - writing your code, running in your products, and embedded in the vendor tools your teams depend on. This two-part series offers security leaders a practical view of what has changed, and what to do next.

**Part 1 framing:** We are in the midst of the biggest shift in software development since the invention of the compiler. Developers at Anthropic and OpenAI have not written a line of code by hand for months. Your organisation will use AI development tools, or be left far behind in the feature race. Is your secure-by-design development process ready for this shift?

**Thesis:** The software your organisation ships is increasingly written by AI, reviewed by humans who did not write it, and assembled from toolchains that themselves embed AI. Three independent literatures - peer-reviewed code-security studies, large-scale enterprise telemetry, and adversarial-supply-chain disclosures - converge on the same conclusion: the writer bar dropped, the reviewer bar must rise, and the governance bar must rise faster than either.

---

## Design principles (apply to both sessions)

- **Non-product promise.** Stated in the intro and close. Earns the room at SASIG.
- **Problem-to-solution balance closer to 40/60.** The "what to do" content is the centre of gravity - not the threat deck.
- **Academic-grade sourcing.** Every quantitative claim traces to a primary publication: peer-reviewed paper, conference proceedings, or named industry research with stated methodology.
- **One arresting stat per segment, not a firehose.** Most slides are one chart, one diagram, or one incident narrative.
- **Live poll at opening.** "Do you have an AI inventory?"
- **Peer voice.** If SASIG allows, a 5-minute fireside with a CISO who has lived one of the incident categories.

## Cross-cutting thread

**Velocity is the shift, evidence is the test.** Developers got faster (Cui et al. RCT shows +26% PRs/week with Copilot - arXiv:2302.06590) but the same tools introduced 2.74x more vulnerabilities (CodeRabbit 2025), and on real maintenance work in mature codebases experienced developers were 19% slower while believing they were 20% faster (METR 2025, arXiv:2507.09089). Reviewers, defenders, and governance all have to match the new pace - and the data already tells us where the gap is widening.

---

## Opening hook (5 min)

**Frame:** Not hypothetical, already shipped, already breached.

Two paired exhibits, one slide each:

1. **Lovable / vibe-coding platforms** as the consumer-grade leading indicator. Wiz Research found ~20% of vibe-coded apps had at least one systematic security risk (https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps); Escape's scan of 5,600+ public apps built on Lovable, Base44, Bolt.new and Vibe Studio found 2,038 high-impact vulnerabilities, 400+ leaked secrets, 175 PII exposures (https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/). Lovable's CVE-2025-48757 (CVSS 9.3 row-level security bypass) and the February-April 2026 Wiz/Escape disclosures (https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/) demonstrate the failure mode in production.
2. **Vercel / Context AI breach (April 2026)** as the enterprise-grade leading indicator. A Lumma Stealer infection on a Context.ai employee was pivoted to a Vercel Google Workspace account, then into Vercel's environment; non-sensitive customer environment variables and AI Office Suite OAuth tokens were exfiltrated and offered for USD 2M on BreachForums (https://vercel.com/kb/bulletin/vercel-april-2026-security-incident, https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/, https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html).

**Charts to consider:** Escape vulnerability-by-platform bar chart; Vercel/Context AI attack-flow diagram showing the pivot Context -> Workspace -> Vercel.

## Segment 1 - What has changed (10 min)

**Goal:** Establish the scale shift with primary sources, then name the central paradox.

**Adoption is now near-universal.**
- GitHub Octoverse 2025: ~80% of new GitHub developers use Copilot within their first week; 1.1M public repos importing LLM SDKs (+178% YoY); 4.3M AI projects (https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/).
- Stack Overflow Developer Survey 2025: 84% of professional developers using or planning to use AI tools; 51% use AI daily; ChatGPT 81.7%, Copilot 67.9% market share (https://survey.stackoverflow.co/2025/ai).
- JetBrains State of Developer Ecosystem 2025: 85% regularly use AI tools, 62% use at least one AI coding assistant, 15% non-adopters (n=24,534 across 194 countries) (https://devecosystem-2025.jetbrains.com/artificial-intelligence).

**Productivity gains are real but narrower than the discourse suggests.**
- Cui, Demirer, Jaffe et al. (Microsoft / MIT / Princeton / Wharton, 2024): three RCTs, 4,867 developers; +26.08% pull requests per week with Copilot, larger gains for junior developers (https://arxiv.org/abs/2302.06590, https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/).
- METR 2025: in mature open-source repos (avg 22k stars, 1M+ LOC) with experienced maintainers, AI access produced a **19% slowdown**, while developers forecast a 24% speedup and post-hoc still believed they were 20% faster (n=16, 246 tasks) (https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/, paper https://arxiv.org/abs/2507.09089).
- DORA 2024: per +25% AI-adoption, +2.1% individual productivity, +2.6% job satisfaction, **-1.5% delivery throughput, -7.2% delivery stability** (https://dora.dev/research/2024/dora-report/, PDF https://services.google.com/fh/files/misc/dora-impact-of-generative-ai-in-software-development.pdf).

**Quality is materially worse on the security axis.**
- Pearce et al., IEEE S&P 2022, "Asleep at the Keyboard?": ~40% of 1,689 Copilot completions across 89 scenarios contained CWE-Top-25 vulnerabilities (https://arxiv.org/abs/2108.09293, IEEE https://ieeexplore.ieee.org/document/9833571, CACM https://dl.acm.org/doi/10.1145/3610721).
- Veracode 2025 GenAI Code Security Report: 80 tasks x 100+ LLMs across 4 languages; 45% of AI-generated code contained an OWASP Top-10 vulnerability; Java 72%, CWE-80 (XSS) failure 86%, CWE-117 (log injection) 88%; **larger LLMs do not perform measurably better** (https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/).
- CodeRabbit 2025 "State of AI vs Human Code Generation": 470 PRs analysed; AI code 1.7x more total issues, 2.74x more XSS, ~40% more critical security issues per 100 PRs (https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report).
- CodeQL large-scale GitHub analysis 2025: 7,703 AI-attributed files (ChatGPT 91.5%, Copilot 7.5%); 4,241 CWE instances across 77 distinct types (https://arxiv.org/abs/2510.26103).

**The cultural shift in one line:** the writer bar dropped (Cui et al. RCT, METR), so the reviewer bar must rise (Veracode, CodeRabbit, Apiiro telemetry below).

**Charts to use:** METR forecast-vs-observed slowdown bar chart (signature visual); DORA "throughput-down paradox" effect-size chart; Veracode per-language and per-CWE failure heatmaps; Octoverse 2025 LLM-SDK-importing repos (+178% YoY).

## Segment 2 - Where the risk is piling up (10 min)

Five concrete categories, each with a primary source, named methodology, and a single number.

### 2.1 - Insecure-by-default code at scale
- **Apiiro telemetry, Fortune-50, 7,000+ developers, 62,000 repos:** 10,000+ new security findings per month from AI-generated code by June 2025; 10x increase vs December 2024; +322% privilege-escalation paths; +153% architectural design flaws; +40% secret exposures (https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/, companion: https://apiiro.com/blog/faster-code-greater-risks-the-security-trade-off-of-ai-driven-development/). Pattern: trivial syntax errors fell 76%, logic bugs >60%, but architectural and identity flaws exploded - "shallow up, deep down."
- **Fu et al., TOSEM 2025:** 733 Copilot snippets from real GitHub projects; 29.5% of Python and 24.2% of JavaScript snippets had at least one CWE; 43 CWEs spanned, 8 in CWE Top-25 (https://arxiv.org/abs/2310.02059, https://dl.acm.org/doi/10.1145/3716848).

### 2.2 - Hallucinated dependencies and slopsquatting
- **Spracklen et al., USENIX Security 2025, "We Have a Package for You!":** 576,000 code samples across 16 LLMs; >=5.2% hallucination rate on commercial LLMs, >=21.7% on open-source; 205,474 unique fabricated package names; **43% of hallucinations recur across 10 prompt repetitions** - ideal repeatability for an attacker (https://arxiv.org/abs/2406.10279, USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen, data https://github.com/Spracks/PackageHallucination).
- **Lasso Security in-the-wild demonstration (Lanyado):** registered hallucinated `huggingface-cli` empty package on PyPI; 30,000+ downloads in 3 months, including documentation reference by Alibaba's GraphTranslator README (https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks).
- **Term provenance:** "slopsquatting" coined by Seth Larson, Python Software Foundation. Industry summary: https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks.

### 2.3 - Secret exposure and overly broad permissions
- **GitGuardian and Snyk telemetry triangulated through Apiiro:** AI-assisted projects show ~2x rate of cloud-credential exposure compared to non-AI baselines; 41% of AI-generated backend code ships with default-admin permissions when prompted naively.
- **Backslash Security 2025 prompt-sensitivity study:** GPT-4.1 with naive prompts scored 1.5/10 on secure-code generation; Claude 3.7 Sonnet went from 6/10 (naive) to 10/10 (security-focused) - the prompt is the control plane (https://www.backslash.security/press-releases/backslash-security-reveals-in-new-research-that-gpt-4-1-other-popular-llms-generate-insecure-code-unless-explicitly-prompted).

### 2.4 - User confidence is anti-correlated with secure outcomes
- **Perry, Srivastava, Kumar & Boneh, ACM CCS 2023, "Do Users Write More Insecure Code with AI Assistants?":** 47 Stanford participants, 5 security-relevant tasks across Python/JS/C; AI-assisted users wrote significantly less secure code on 4 of 5 questions - and were **more likely to believe their code was secure** than the control group (https://arxiv.org/abs/2211.03622, ACM https://dl.acm.org/doi/10.1145/3576915.3623157, replication data https://github.com/NeilAPerry/Do-Users-Write-More-Insecure-Code-with-AI-Assistants).
- **Snyk 2023/2024 AI Code Security Report:** ~80% of developers admit bypassing AI security policies; only 10% scan the majority of AI-generated code; <25% use SCA on AI suggestions (https://go.snyk.io/2023-ai-code-security-report.html).

### 2.5 - The toolchain is itself an AI attack surface
- **Vercel / Context AI (April 20, 2026, opening hook):** an internal AI-tooling employee compromise pivoted into customer-affecting OAuth-token theft. Sources above.
- **LiteLLM supply chain compromise (March 24, 2026):** litellm 1.82.7/1.82.8 published as backdoored PyPI packages after the Trivy GitHub Action was unpinned in LiteLLM's CI; ~3.4M daily downloads, 40,000+ in the 5+ hour exposure window; payload harvested SSH keys, cloud creds, K8s configs, shell history, crypto wallets (https://docs.litellm.ai/blog/security-update-march-2026, Microsoft Security https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/, Snyk https://snyk.io/blog/poisoned-security-scanner-backdooring-litellm/, Trend Micro https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html).
- **Hugging Face / pickle ecosystem:** ProtectAI Guardian + Hugging Face partnership scanned 4.47M model versions and surfaced 352K unsafe issues across ~51,700 models; ReversingLabs "nullifAI" found broken-pickle evasion of Picklescan (https://huggingface.co/blog/pai-6-month, https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face).

**Charts to use:** Apiiro hockey-stick of monthly findings (Dec 2024 - June 2025); Spracklen per-model hallucination rates and 43%-recurrence histogram; LiteLLM attack-flow diagram (Trivy -> CI -> PyPI publish token -> backdoored package -> developer machines).

## Segment 3 - What to do (25 min)

**The centre of gravity. Five sub-blocks, five minutes each. Each anchored to either a peer-reviewed defence, a standards body, or named enterprise practice.**

### 3.1 - Tooling (5 min)

- **IDE-boundary controls.** Inspect prompts before they leave the endpoint, block secrets in transit, govern file context, enforce tool-call allowlists. Cycode and similar guardrail vendors codify these patterns; the academic frame is Hines et al. "Spotlighting" (Microsoft, arXiv:2403.14720) which reduces injection ASR from >50% to <2% via delimiting / datamarking / encoding - applicable to prompt validation in the IDE plane (https://arxiv.org/abs/2403.14720).
- **PR gates that fail-closed.** SAST, secret scanning and SCA mandatory on AI-assisted PRs; block hallucinated imports at CI by allowlisting against a known-good package registry. Veracode and Apiiro both report that the same controls applied universally reduce AI-introduced risk to roughly the human-only baseline.
- **SBOM extended to model and tool provenance.** SLSA v1.2 (https://slsa.dev/spec/v1.2/) for build integrity; NIST SP 800-204D (https://csrc.nist.gov/pubs/sp/800/204/d/final) for CI/CD supply-chain integration; AI-BOM concept maturing through OWASP and Linux Foundation work.
- **Pin AI coding tool versions.** Treat MCP servers as third-party dependencies subject to your existing controls. Hou et al. 2025 catalogue 57 MCP-specific threats using STRIDE/DREAD (https://xinyi-hou.github.io/files/hou2025mcp_1.pdf); Invariant Labs demonstrates "rug-pull" tool poisoning where benign-looking tool descriptions silently mutate on second launch (https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

### 3.2 - Process (5 min)

- **Mandatory AI-usage disclosure at the PR level.** You cannot improve what you cannot see. Aligns with NIST SP 800-218A practice PO.1 (https://csrc.nist.gov/pubs/sp/800/218/a/final).
- **Third-party AI tool intake review** before anyone grants Google Drive / Slack / GitHub access to a new AI tool. The Vercel / Context AI breach is the canonical case study.
- **AI-specific branch in IR playbook.** What happens when an AI-generated PR introduces a CVE? When an upstream AI tool is compromised? When a model provider rotates a key? NIST AI 600-1 MS-2.6 and MG-3.1/3.2 (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) provide the structure.
- **Dependency pinning as policy, not guidance.** LiteLLM is the reference incident.

### 3.3 - Culture (5 min)

- **Trust-but-verify with teeth.** No merge until reviewed by someone who did not write the prompt. Sandoval et al. (USENIX Security 2023, "Lost at C") show review interaction is the primary moderator of LLM-assisted bug rate (https://arxiv.org/abs/2208.09727).
- **Pair-review for AI-generated code.** One developer who used AI plus one who did not.
- **Ownership is human, not the model.** The name on the PR owns what it does, regardless of what wrote it.
- **Reward catches, not velocity.** A caught hallucination is the same artefact as a caught bug; the metric should reflect that.

### 3.4 - Organisational (5 min)

- **Name an owner for AI-in-SDLC.** Usually AppSec plus an engineering lead, not product. ISO/IEC 42001:2023 Clause 5 (https://www.iso.org/standard/42001) makes leadership accountability explicit.
- **Joint governance body that meets weekly, not quarterly.** GitLab 2025 DevSecOps Report finds 49% of orgs use 5+ AI tools; tool sprawl outpaces quarterly cadences (https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/).
- **Redistribute the review workload.** Apiiro telemetry: AI users commit 3-4x more often, larger PRs - seniors must spend more time reviewing, less time writing.
- **Update hiring.** If juniors are using AI, what does "senior" actually mean, and how do you interview for the review reflex rather than the typing reflex?

### 3.5 - Governance and reporting (5 min)

- **Anchor your programme to NIST SP 800-218A** (https://csrc.nist.gov/pubs/sp/800/218/a/final). It extends NIST SSDF v1.1 (https://csrc.nist.gov/pubs/sp/800/218/final) with PS.1/2 (protect all forms of code, including weights/data/prompts), PW.4 (model and dataset due diligence), RV.1/RV.2 (model evaluation, prompt-injection response). Audit-ready and unambiguous.
- **Layer NIST AI 600-1** (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) for the GenAI risk taxonomy, ISO/IEC 42001 for management-system certification, and CISA / NCSC Guidelines for Secure AI System Development (https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf) for the lifecycle hooks.
- **Metrics worth reporting:** proportion of PRs AI-assisted, vulnerability rate AI-assisted vs human-only, secret exposures traced to AI contexts, MTTR for AI-introduced vulnerabilities tracked separately. Apiiro telemetry shows these segregated metrics reveal patterns invisible at the aggregate level.
- **Board-level answer ready:** "what proportion of our production code is now AI-authored, and how does its vulnerability rate compare to our human-only baseline?"

**Charts to use:** NIST SSDF mapping diagram (PO/PS/PW/RV with AI-specific extensions); a single CISO-board-pack metrics card showing the segregated metrics; Constitutional Classifiers ASR-reduction chart from Anthropic 2025 as a teaser for Part 2.

## Close (5 min)

Monday-morning checklist:

- Inventory AI coding tools in use (including unsanctioned).
- Require SAST and secret scanning on AI-assisted PRs.
- Write an acceptable-use policy anchored to NIST SP 800-218A.
- Audit what third-party AI tools your build pipeline trusts (the Context AI question).
- Name the owner and stand up the governance body.

Tease Part 2: once it ships, it is someone else's attack surface.

---

# Production notes

- **Slide count target:** 18-22 slides.
- **Citation discipline:** every quantitative claim has the primary source on the slide footer; long URLs pushed to the bibliography slide.
- **Q&A buffer:** reserve final 5-10 minutes.
- **Storytelling over stats after the hook.** Suggested narrative-driven incident: Vercel / Context AI walked through end-to-end.
- **Live poll at opening:** "Do you have an AI inventory?"
- **The non-product promise:** say it out loud in the intro and close.
- **Charts to pre-build (priority order):** METR forecast-vs-observed slowdown; Veracode per-CWE failure heatmap; Apiiro hockey-stick of AI-introduced findings; DORA throughput-down paradox; LiteLLM attack-flow.

---

# Source library - Part 1

Organised by topic to support follow-up reading. Where both an arXiv preprint and a venue version exist, both are listed. Where industry research has a stated methodology and named author/team, the original publication is preferred over press summaries.

## A. Series-wide / framing

- Stanford AI Index Report 2025 (HAI) - https://hai.stanford.edu/ai-index/2025-ai-index-report/responsible-ai (Chapter 3 PDF: https://hai.stanford.edu/assets/files/hai_ai-index-report-2025_chapter3_final.pdf)
- Stanford AI Index Report 2026 (HAI) - https://hai.stanford.edu/ai-index/2026-ai-index-report
- IBM Cost of a Data Breach Report 2025 - https://www.ibm.com/reports/data-breach (PDF https://www.ibm.com/downloads/documents/us-en/131cf87b20b31c91)
- IANS "Boards Give CISO Cybersecurity Reporting a Mixed Grade" - https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/03/24/boards-give-ciso-cybersecurity-reporting-a-mixed-grade

## B0. 2026 updates (post-Feb 2026 - newest material)

- Georgia Tech Vibe Security Radar (April 13, 2026) - traces CVE fixing-commits through git history to attribute to AI tools; 6 / 15 / 35 AI-attributed CVEs in Jan/Feb/Mar 2026; 74 lifetime; 27 to Claude Code - https://news.research.gatech.edu/2026/04/13/bad-vibes-ai-generated-code-vulnerable-researchers-warn (live dataset https://vibe-radar-ten.vercel.app/)
- Endor Labs / Carnegie Mellon "Agentic Code Security Benchmark" + Agent Security League (April 15, 2026) - 200 OSS tasks, 108 projects, 77 CWEs; top agent 84.4% functional / 17.3% security - https://www.endorlabs.com/research/ai-code-security-benchmark
- Zhao et al. "Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks" (SUSVIBES) - https://arxiv.org/abs/2512.03262
- "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code" (April 2026) - https://arxiv.org/abs/2604.05292
- Weissberg et al. "LLM-based Vulnerability Discovery through the Lens of Code Metrics" (ICSE 2026) - https://www.mlsec.org/docs/2026-icse.pdf
- Dai et al. "Rethinking the Evaluation of Secure Code Generation" (ICSE 2026) - https://arxiv.org/abs/2503.15554
- "LLM-based Vulnerability Detection at Project Scale: An Empirical Study" (Jan 27, 2026) - https://arxiv.org/abs/2601.19239
- METR Feb 24, 2026 update "We Are Changing Our Developer Productivity Experiment Design" - https://metr.org/blog/2026-02-24-uplift-update/
- Veracode Spring 2026 GenAI Code Security Update - https://www.veracode.com/blog/spring-2026-genai-code-security/
- Snyk RSAC 2026 / Manoj Nair interview - https://expertinsights.com/industry-perspectives/rsac-2026-manoj-nair-snyk; "Secure Adoption in the GenAI Era" - https://snyk.io/reports/secure-adoption-in-the-genai-era/
- Apiiro AI Threat Modeling launch (March 23, 2026) - https://www.helpnetsecurity.com/2026/03/23/apiiro-ai-threat-modeling/; Guardian Agent (Jan 28, 2026) - https://www.globenewswire.com/news-release/2026/01/28/3227686/0/en/Apiiro-Launches-Guardian-Agent-to-Enable-Zero-Vulnerabilities-in-AI-Generated-Code.html
- Stanford HAI 2026 AI Index Report - https://hai.stanford.edu/ai-index/2026-ai-index-report (PDF https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)
- Stack Overflow "Closing the Developer AI Trust Gap" (Feb 18, 2026) - https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
- DORA 2025 State of AI-Assisted Software Development - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (announcement https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report, full report https://dora.dev/dora-report-2025/) - 90% of devs use AI at work, 65% heavy reliance, 30% distrust AI-generated code, ~5,000 respondents
- McKinsey "Unlocking the value of AI in software development" (Feb 2026, n=4,500 devs / 150 enterprises) - https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development - 90%+ teams use AI, ~6 hrs/week saved, 46% routine-coding-time reduction
- Atlassian State of Teams 2026 - https://www.atlassian.com/blog/state-of-teams-2026 - 85% of knowledge workers use AI; only 29% have embedded it in workflows
- Atlassian State of Developer Experience 2025 - https://www.atlassian.com/teams/software-development/state-of-developer-experience-2025 - 99% report time savings; 68% save more than 10 hours/week
- Anthropic Economic Index Jan 2026 - https://www.anthropic.com/research/anthropic-economic-index-january-2026-report; March 2026 update - https://www.anthropic.com/research/economic-index-march-2026-report - 35% of Claude.ai conversations / 44% of API traffic are computer/mathematical occupations; 79% of Claude Code conversations involve automation
- Microsoft FY26 Q2 earnings (Jan 28, 2026) - 4.7M paid GitHub Copilot subscribers (+75% YoY); ~90% of Fortune 100 use Copilot
- Microsoft 20-30% AI-written code in its own repos (Nadella, LlamaCon April 2025) - https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/ (CNBC https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html)
- Gartner: 40% of enterprise apps will feature task-specific AI agents by 2026 - https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- CSA + SANS + OWASP GenAI "AI Vulnerability Storm: Building a Mythos-Ready Security Program" (April 2026) - https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/mythosreadyv92.pdf
- OWASP GenAI "Exploit Round-up Report Q1 2026" (April 14, 2026) - https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
- CWE Top 25 (2026 list, released January 29, 2026) - https://cwe.mitre.org/top25/

### AI-tool CVEs (2026, additions for the toolchain narrative)

- CVE-2026-26268 - Cursor IDE arbitrary code execution via git hook (Feb 2026) - https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- CVE-2026-21516 - GitHub Copilot "Reprompt Attack" (patched in Copilot 1.5.63, Feb 10, 2026) - https://www.paperclipped.de/en/blog/github-copilot-cve-2026-21516-reprompt-attack/
- CVE-2026-35021 - Claude Code CLI OS command injection RCE - https://www.sentinelone.com/vulnerability-database/cve-2026-35021/
- CVE-2026-30615 / CVE-2025-54135 / CVE-2025-54136 - "MCP by Design" supply-chain RCE pattern (Cursor, Windsurf) - https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/
- SecurityWeek "Claude Code, Gemini CLI, GitHub Copilot Agents Vulnerable to Prompt Injection via Comments" - https://www.securityweek.com/claude-code-gemini-cli-github-copilot-agents-vulnerable-to-prompt-injection-via-comments/

## B. Peer-reviewed papers on AI-generated code security

- Pearce, Ahmad, Tan, Dolan-Gavitt, Karri (IEEE S&P 2022) "Asleep at the Keyboard?" - https://arxiv.org/abs/2108.09293, IEEE Xplore https://ieeexplore.ieee.org/document/9833571, CACM https://dl.acm.org/doi/10.1145/3610721
- Sandoval, Pearce, Nys, Karri, Garg, Dolan-Gavitt (USENIX Security 2023) "Lost at C" - https://arxiv.org/abs/2208.09727, USENIX https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval, PDF https://www.usenix.org/system/files/usenixsecurity23-sandoval.pdf
- Perry, Srivastava, Kumar, Boneh (ACM CCS 2023) "Do Users Write More Insecure Code with AI Assistants?" - https://arxiv.org/abs/2211.03622, ACM https://dl.acm.org/doi/10.1145/3576915.3623157, replication https://github.com/NeilAPerry/Do-Users-Write-More-Insecure-Code-with-AI-Assistants
- Khoury, Avila, Brunelle, Camara (IEEE SMC 2023) "How Secure is Code Generated by ChatGPT?" - https://arxiv.org/abs/2304.09655
- Fu et al. (ACM TOSEM 2025) "Security Weaknesses of Copilot-Generated Code in GitHub Projects" - https://arxiv.org/abs/2310.02059, https://dl.acm.org/doi/10.1145/3716848
- Hamer, d'Aragona, Bavota (2024) "Just Another Copy and Paste? ChatGPT vs StackOverflow" - https://arxiv.org/abs/2403.15600
- Basic et al. (2024) "LLMs and Code Security: A Systematic Literature Review" - https://arxiv.org/abs/2412.15004
- "A Systematic Literature Review on Detecting Software Vulnerabilities with LLMs" (2025) - https://arxiv.org/abs/2507.22659
- "Security Vulnerabilities in AI-Generated Code: A Large-Scale Analysis of Public GitHub Repositories" (2025) - https://arxiv.org/abs/2510.26103
- Benchmarks: CWEval https://arxiv.org/abs/2501.08200, SecRepoBench https://arxiv.org/abs/2504.21205

## C. Productivity vs quality

- Cui, Demirer, Jaffe, Musolff, Peng, Salz (2024) "The Effects of Generative AI on High-Skilled Work" (3 RCTs, 4,867 devs) - https://arxiv.org/abs/2302.06590, https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf, https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/
- METR (2025) "Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity" - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/, paper https://arxiv.org/abs/2507.09089, follow-up https://metr.org/blog/2026-02-24-uplift-update/
- Google DORA 2024 "Accelerate State of DevOps - Impact of AI" - https://dora.dev/research/2024/dora-report/, PDF https://services.google.com/fh/files/misc/dora-impact-of-generative-ai-in-software-development.pdf
- Google DORA 2025 "State of AI-Assisted Software Development" - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- GitHub Octoverse 2024 - https://github.blog/news-insights/octoverse/octoverse-2024/
- GitHub Octoverse 2025 - https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Stack Overflow Developer Survey 2024 AI - https://survey.stackoverflow.co/2024/ai
- Stack Overflow Developer Survey 2025 AI - https://survey.stackoverflow.co/2025/ai (press https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)
- JetBrains State of Developer Ecosystem 2025 - https://devecosystem-2025.jetbrains.com/, AI section https://devecosystem-2025.jetbrains.com/artificial-intelligence
- GitLab Global DevSecOps Report 2025 - https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/
- GitClear "Coding on Copilot" (2024) - https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality
- GitClear "AI Copilot Code Quality 2025: 4x Growth in Code Clones" - https://www.gitclear.com/ai_assistant_code_quality_2025_research, PDF https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf

## D. Industry telemetry on AI vulnerabilities

- Veracode "2025 GenAI Code Security Report" - https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/, blog https://www.veracode.com/blog/genai-code-security-report/
- Apiiro "4x Velocity, 10x Vulnerabilities" - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/, companion https://apiiro.com/blog/faster-code-greater-risks-the-security-trade-off-of-ai-driven-development/
- CodeRabbit "State of AI vs Human Code Generation 2025" - https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
- Snyk 2023 AI Code Security Report - https://go.snyk.io/2023-ai-code-security-report.html
- Snyk 2024 Open Source Security Report - https://snyk.io/lp/state-of-open-source-2024/, blog https://snyk.io/blog/2024-open-source-security-report-slowing-progress-and-new-challenges-for/
- Backslash Security GPT-4.1 secure-code research - https://www.backslash.security/press-releases/backslash-security-reveals-in-new-research-that-gpt-4-1-other-popular-llms-generate-insecure-code-unless-explicitly-prompted
- Kusari "AI Coding Assistants 4x Faster 10x Riskier" - https://www.kusari.dev/blog/ai-coding-assistants-in-2026-4x-faster-10x-riskier-the-hidden-security-cost
- The Register - https://www.theregister.com/2026/03/26/ai_coding_assistant_not_more_secure/

## E. Hallucinated packages / slopsquatting

- Spracklen et al. (USENIX Security 2025) "We Have a Package for You!" - https://arxiv.org/abs/2406.10279, USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen, data https://github.com/Spracks/PackageHallucination
- Lasso Security / Bar Lanyado huggingface-cli demo - https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks
- Socket "Rise of Slopsquatting" - https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks
- CSO Online - https://www.csoonline.com/article/3961304/ai-hallucinations-lead-to-new-cyber-threat-slopsquatting.html
- BleepingComputer - https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/
- Snyk mitigation - https://snyk.io/articles/slopsquatting-mitigation-strategies/

## F. Vibe-coding platform security

- Wiz "Common Security Risks in Vibe-Coded Apps" - https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps
- Wiz "Critical Vulnerability Base44" - https://www.wiz.io/blog/critical-vulnerability-base44
- Escape "Methodology - 2k+ vulnerabilities in vibe-coded apps" - https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/
- The Register on Lovable - https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities/, follow-up https://www.theregister.com/2026/04/20/lovable_denies_data_leak/
- Superblocks "How 170+ Lovable apps were exposed" - https://www.superblocks.com/blog/lovable-vulnerabilities
- TheNextWeb - https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed
- CSA "Vibe Coding's Security Debt" - https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/
- Backslash on vibe-coding security - https://www.backslash.security/vibe-coding-ai-security
- SQ Magazine "AI Coding Security Vulnerability Statistics 2026" - https://sqmagazine.co.uk/ai-coding-security-vulnerability-statistics/
- LeadDev - https://leaddev.com/ai/ai-assisted-coding-and-unsanctioned-tools-headline-2026s-biggest-security-risks
- ISACA "Securing the AI Frontier" - https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/securing-the-ai-frontier-a-practical-framework-for-assessing-ai-coding-assistant-vulnerabilities
- SoftwareSeni - https://www.softwareseni.com/ai-generated-code-security-risks-why-vulnerabilities-increase-2-74x-and-how-to-prevent-them/

## G. AI-tool-supply-chain incidents

- Vercel security bulletin (April 2026) - https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
- TechCrunch - https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/
- Trend Micro Vercel/Context.ai analysis - https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html
- The Hacker News - https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html
- CyberScoop - https://cyberscoop.com/vercel-security-breach-third-party-attack-context-ai-lumma-stealer/
- BleepingComputer - https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/
- LiteLLM advisory - https://docs.litellm.ai/blog/security-update-march-2026
- Microsoft Security on Trivy/LiteLLM - https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
- Snyk on LiteLLM - https://snyk.io/blog/poisoned-security-scanner-backdooring-litellm/
- Trend Micro on LiteLLM - https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html
- Cycode "AI Guardrails for IDE security" - https://cycode.com/blog/ai-guardrails-real-time-ide-security/

## H. Standards and frameworks

- NIST SP 800-218A SSDF for GenAI - https://csrc.nist.gov/pubs/sp/800/218/a/final, PDF https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf
- NIST SP 800-218 base SSDF v1.1 - https://csrc.nist.gov/pubs/sp/800/218/final, draft v1.2 https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
- NIST AI RMF 1.0 - https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1 GenAI Profile - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NIST SP 800-204D supply chain in CI/CD - https://csrc.nist.gov/pubs/sp/800/204/d/final
- SLSA framework - https://slsa.dev/, levels https://slsa.dev/spec/v1.0/levels, current spec https://slsa.dev/spec/v1.2/
- ISO/IEC 42001:2023 AI management system - https://www.iso.org/standard/42001
- ISO/IEC 23894:2023 AI risk management - https://www.iso.org/standard/77304.html
- EU AI Act Article 15 - https://artificialintelligenceact.eu/article/15/, EC service desk https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15
- NCSC + CISA "Guidelines for Secure AI System Development" - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf, announcement https://www.cisa.gov/news-events/alerts/2023/11/26/cisa-and-uk-ncsc-unveil-joint-guidelines-secure-ai-system-development
- CISA Secure by Design - https://www.cisa.gov/securebydesign, pledge https://www.cisa.gov/securebydesign/pledge
- OWASP Top 10 for LLM Applications 2025 - https://genai.owasp.org/llm-top-10/

---

## Notes on rigor (Part 1)

A few stats commonly cited in this space need careful attribution. They are usable, but be precise:

1. **METR "19% slowdown" and Cui et al. "+26% PRs/week"** are not in conflict. They sample different populations (mature OSS maintainers vs. Microsoft / Accenture / Fortune-100 enterprise developers) and different task types (issue resolution in mature 1M+ LOC repos vs. shorter-cycle enterprise work). Present them as such on the same slide - the reconciliation is what makes the point.
2. **Veracode 45% / CodeRabbit 2.74x / Apiiro 10x / Pearce 40%** are different methodologies (curated benchmark, real-world PR analysis, enterprise telemetry, hand-crafted scenarios respectively). They are independent, mutually corroborating, and should be presented together on a "convergent evidence" slide rather than chained.
3. **Apiiro telemetry is one Fortune-50 deployment** (7,000+ developers, 62,000 repos). Powerful directional signal, not a population estimate.
4. **Spracklen et al. hallucination rates** are model-specific; the 5.2% / 21.7% figures are minimums across the commercial / open-source classes - cite the model alongside the rate where space permits.
