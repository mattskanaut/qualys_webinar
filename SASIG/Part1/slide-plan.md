# Part 1 - Slide Plan

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Target:** ~20 slides, 55 min content + 5 min Q&A
**Style:** brief, high-level. Speaker carries the content; slides anchor.

---

## Slide 1 - Title

- The New SDLC: Security When Every Developer Writes With AI
- The New Normal: Software, Security and the AI Stack - Part 1 of 2
- Matt Campbell, SASIG

**Graphic:** Series wordmark. No image.

**Speaker notes:** Welcome, set the room, name SASIG. Two-part series. Today is the writer's side; Part 2 is what runs in production.

---

## Slide 2 - The promise of this hour

- Non-product. No vendor pitch.
- 40% problem, 60% what to do.
- Every stat sourced. Bibliography at the end.

**Graphic:** Three-icon strip: shield (non-product), clock (40/60), book (sources).

**Speaker notes:** Earn the room. Say the non-product promise out loud. Tell them slides will look light because I plan to talk - the citations live in the footer and the bibliography lands in their inbox.

---

## Slide 3 - Live poll

- Do you have an AI inventory?
- Yes / Partial / No / Not sure

**Graphic:** Poll widget placeholder.

**Speaker notes:** Use the poll result later in Segment 3. Most rooms answer "partial" or "no" - which is exactly the launching point.

---

## Slide 4 - Hook 1: AI-written code is shipping CVEs into enterprise and OSS

- Georgia Tech "Vibe Security Radar" (April 2026): traces CVE fixing-commits back through git history. 6 AI-attributed CVEs in Jan 2026, 15 in Feb, 35 in March - near 6x growth in two months. 74 lifetime confirmed; researchers estimate true count is 5-10x detected
- Endor Labs / CMU Agent Security League (April 2026): top agent on 200 real OSS tasks scores 84.4% functional but only 17.3% on security - over 80% of outputs vulnerable
- Fu et al., ACM TOSEM 2025: 29.5% of Python and 24.2% of JavaScript Copilot-attributed snippets in real GitHub projects contained at least one CWE

**Graphic:** Vibe Security Radar monthly CVE-attribution chart (or stylised reproduction of the live dashboard); the trajectory is the story.

**Speaker notes:** Reframe before the breach narrative. This is real CVEs in real repos, not benchmarks. The Georgia Tech work is the most direct evidence - they look at fixing-commits, walk the git history back, and identify when the original vulnerable code was written by an AI tool. 27 of the 74 traced are attributable to Claude Code because of its commit-message signature. The Endor Labs leaderboard tells you the same story from the other side - even the best AI agent fails security on 80% of real OSS tasks. This is what is shipping into enterprise stacks while we are in this room.

**Sources:**
- Georgia Tech "Bad Vibes: AI-Generated Code is Vulnerable" (April 13, 2026) - https://news.research.gatech.edu/2026/04/13/bad-vibes-ai-generated-code-vulnerable-researchers-warn (live dataset https://vibe-radar-ten.vercel.app/)
- Endor Labs / CMU Agentic Code Security Benchmark + Agent Security League (April 15, 2026) - https://www.endorlabs.com/research/ai-code-security-benchmark
- Fu et al., ACM TOSEM 2025 - https://dl.acm.org/doi/10.1145/3716848 (preprint https://arxiv.org/abs/2310.02059)
- MITRE CWE Top 25 - https://cwe.mitre.org/top25/

---

## Slide 5 - Hook 2: the enterprise version - Vercel / Context AI

- Lumma Stealer infects Context.ai employee
- Pivots: Context -> Google Workspace -> Vercel environment
- OAuth tokens for AI Office Suite users exfiltrated, sold for USD 2M

**Graphic:** Three-step attack-flow arrow diagram.

**Speaker notes:** April 2026, fresh. The point is not "this vendor was bad" - it is that the AI tooling your build pipeline trusts is now an attack surface. Every CISO in the room has a Context-AI-shaped supplier somewhere.

**Sources:**
- Vercel security bulletin - https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
- TechCrunch - https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/
- Trend Micro analysis - https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html

---

## Slide 6 - Adoption is near-universal in the enterprise

- Microsoft FY26 Q2 earnings (Jan 28, 2026): 4.7M paid GitHub Copilot subscribers, +75% YoY; ~90% of the Fortune 100 use Copilot
- DORA 2025 State of AI-Assisted Software Development (Sept 2025, n~5,000): 90% of devs use AI at work; 65% rely on it heavily
- McKinsey 2026 Developer Survey (Feb 2026, 4,500 devs / 150 enterprises): 90%+ of software teams use AI; ~6 hours/week saved per developer on average

**Graphic:** Three-column number card (4.7M / 90% / 90%+) with logos.

**Speaker notes:** Skip past the "AI is coming" framing. Three independent 2026 data points - one from Microsoft's audited revenue, one from a 5,000-developer survey, one from McKinsey across 150 enterprises - all converge on near-universal in the enterprise. Microsoft's separate disclosure that 20-30% of code in their own repos is AI-generated (Nadella, April 2025) is the directional anchor for "this is already in your stack." The interesting question is what changes downstream.

**Sources:**
- Microsoft FY26 Q2 earnings call (Jan 28, 2026), reported across financial press; GitHub Copilot 4.7M paid subs, ~90% Fortune 100
- DORA 2025 State of AI-Assisted Software Development - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (announcement https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report, full report https://dora.dev/dora-report-2025/)
- McKinsey "Unlocking the value of AI in software development" (Feb 2026) - https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development
- Stanford HAI 2026 AI Index (April 2026): 88% of organizations adopted AI; 70% use generative AI in at least one business function - https://hai.stanford.edu/ai-index/2026-ai-index-report
- Microsoft 20-30% AI-written code (Nadella, LlamaCon April 2025) - https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/

---

## Slide 7 - The productivity paradox

- Cui et al. RCT (n=4,867): +26% PRs/week with Copilot
- METR Feb 2026 update: original 19% slowdown finding moderates to -4% in re-run (CI -15% to +9%); selection bias was significant. Productivity gains "likely" - but METR explicitly does NOT retract the security/quality concerns
- DORA 2025: 90% of devs use AI; ~33% explicitly distrust AI-generated code; PR review time up 441%; PR size up 51.3%

**Graphic:** Two-panel chart - left: Cui +26% / METR Feb 2026 -4% (with original July 2025 -19% greyed out for context); right: DORA 2025 PR-size and PR-review-time deltas.

**Speaker notes:** Important nuance. METR walked back the headline -19% number in February 2026 - the new study shows roughly flat. But the security side has not moved: the same paper that walked back the time-loss explicitly preserves the quality and review-burden concerns. DORA 2025 makes the review-burden quantitative: PRs are bigger and take 5x longer to review. The reviewer is still the load-bearing role.

**Sources:**
- Cui, Demirer, Jaffe, Musolff, Peng, Salz (2024) "The Effects of Generative AI on High-Skilled Work" - https://arxiv.org/abs/2302.06590
- METR (2025) original study - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (paper https://arxiv.org/abs/2507.09089)
- METR Feb 24, 2026 follow-up "We Are Changing Our Developer Productivity Experiment Design" - https://metr.org/blog/2026-02-24-uplift-update/
- Google DORA 2025 State of AI-Assisted Software Development - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (announcement https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)

---

## Slide 8 - Quality on security is materially worse - and not improving

- Veracode Spring 2026 (rerun of 2025 harness, 100+ LLMs): 45% of AI code still has an OWASP Top 10 vuln; Java still 72%; newer/"more hyped" models show no measurable improvement
- "Broken by Default" arXiv:2604.05292 (April 2026): 3,500 artifacts across 7 LLMs; 55.8% formally proven vulnerable by Z3; 6 commercial SAST tools combined miss 97.8% of Z3-proven findings
- Pearce et al., IEEE S&P 2022: ~40% of Copilot completions had a CWE-Top-25 flaw - the 2022 baseline is essentially unchanged in 2026

**Graphic:** Three-bar comparison (2022 / 2025 / Spring 2026) showing the line is flat.

**Speaker notes:** Two messages on this slide. First: across four years and a generation of frontier models, the failure rate has not moved. The Veracode Spring 2026 rerun is the headline - same harness, newer models, same 45%. Second: the formal-verification work in "Broken by Default" closes the methodology critique. These are not heuristics flagging false positives - they are Z3-proven vulnerabilities, and the SAST tools you are buying right now miss 97.8% of them.

**Sources:**
- Veracode Spring 2026 GenAI Code Security Update - https://www.veracode.com/blog/spring-2026-genai-code-security/
- "Broken by Default: A Formal Verification Study of Security Vulnerabilities in AI-Generated Code" - https://arxiv.org/abs/2604.05292
- Pearce, Ahmad, Tan, Dolan-Gavitt, Karri (IEEE S&P 2022) "Asleep at the Keyboard?" - https://arxiv.org/abs/2108.09293 (IEEE Xplore https://ieeexplore.ieee.org/document/9833571)
- Veracode 2025 baseline (for the longitudinal comparison) - https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/

---

## Slide 9 - Insecure-by-default at scale (Apiiro)

- One Fortune-50 deployment: 7,000 devs, 62,000 repos
- 10,000+ new security findings per month by June 2025 - 10x in 6 months
- +322% privilege escalation paths; +153% architectural flaws; +40% secret exposures

**Graphic:** Apiiro hockey-stick of monthly findings.

**Speaker notes:** "Shallow up, deep down" - syntax errors fell, architectural and identity flaws exploded. Note the directional caveat - this is one big customer, not a population estimate. But the trend is the story.

**Sources:**
- Apiiro "4x Velocity, 10x Vulnerabilities" - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
- Companion: Apiiro "Faster Code, Greater Risks" - https://apiiro.com/blog/faster-code-greater-risks-the-security-trade-off-of-ai-driven-development/

---

## Slide 10 - Hallucinated dependencies (slopsquatting)

- Spracklen et al., USENIX Security 2025: 576,000 samples, 16 LLMs
- Commercial models: >=5.2% hallucination rate. Open-source: >=21.7%
- 43% of hallucinations recur across 10 prompt repeats - perfect repeatability for an attacker

**Graphic:** Per-model hallucination rate chart from the paper.

**Speaker notes:** Lasso registered the hallucinated `huggingface-cli` as an empty PyPI package - 30,000 downloads in 3 months, including a reference in Alibaba's docs. This is the next typosquatting and it does not need any user error to land.

**Sources:**
- Spracklen et al. (USENIX Security 2025) "We Have a Package for You!" - https://arxiv.org/abs/2406.10279 (USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen, data https://github.com/Spracks/PackageHallucination)
- Lasso Security / Bar Lanyado huggingface-cli demo - https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks
- Socket "Rise of Slopsquatting" - https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks

---

## Slide 11 - The toolchain is itself an attack surface

- LiteLLM, March 24 2026 - backdoored 1.82.7/1.82.8 via Trivy in CI
- 3.4M daily downloads; ~40,000 in the exposure window
- Payload: SSH keys, cloud creds, K8s configs, shell history, crypto wallets

**Graphic:** Attack-flow: Trivy unpinned -> CI compromise -> PYPI_PUBLISH token -> backdoored package -> developer machines.

**Speaker notes:** The pipeline runs AI tools that run AI tools. Pinning is not paranoia, it is the policy.

**Sources:**
- LiteLLM advisory - https://docs.litellm.ai/blog/security-update-march-2026
- Microsoft Security blog on Trivy/LiteLLM - https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
- Snyk analysis - https://snyk.io/blog/poisoned-security-scanner-backdooring-litellm/
- Trend Micro analysis - https://www.trendmicro.com/en_us/research/26/c/inside-litellm-supply-chain-compromise.html

---

## Slide 12 - The trust gap is widening, and so is the confidence gap

- Perry et al., ACM CCS 2023: AI-assisted users wrote less secure code on 4 of 5 tasks - and were more likely to believe it was secure
- Stack Overflow Feb 2026 follow-up: 84% use AI but only 29% trust it (down 11pts YoY); 81% concerned about security/data privacy; 66% cite "almost right but not quite" as their #1 frustration
- Snyk RSAC 2026: 48% of AI-generated code contains vulnerabilities; per-developer vuln rate up 2-10x YoY

**Graphic:** Two-line chart - usage rising, trust falling - over 2023 to 2026.

**Speaker notes:** Two trends on the same axis. Use is up, trust is down, security concern is highest among any AI worry. This is the cultural slide. The reviewer reflex is the whole game - and your developers, by survey, already know the tool is unreliable. The job is to make the review structure match the survey instinct.

**Sources:**
- Perry, Srivastava, Kumar, Boneh (ACM CCS 2023) "Do Users Write More Insecure Code with AI Assistants?" - https://arxiv.org/abs/2211.03622 (ACM https://dl.acm.org/doi/10.1145/3576915.3623157)
- Stack Overflow blog "Closing the Developer AI Trust Gap" (Feb 18, 2026) - https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
- Snyk RSAC 2026 / Manoj Nair interview - https://expertinsights.com/industry-perspectives/rsac-2026-manoj-nair-snyk
- Snyk "Secure Adoption in the GenAI Era" - https://snyk.io/reports/secure-adoption-in-the-genai-era/

---

## Slide 13 - What to do - the 40/60 frame

- Tooling, Process, Culture, Organisation, Governance
- 25 minutes - 5 each
- Each grounded in either peer-reviewed defence, a standards body, or named enterprise practice

**Graphic:** Five-pillar diagram with section icons.

**Speaker notes:** Transition slide. The remaining 25 minutes are the centre of gravity. I will move quickly.

---

## Slide 14 - Tooling

- IDE-boundary controls: inspect prompts, block secrets, govern context
- PR gates fail-closed: SAST, secret scan, SCA on every AI-assisted PR
- Block hallucinated imports at CI - allowlist against a known-good registry
- Pin AI tool versions; treat MCP servers as third-party dependencies

**Graphic:** Pipeline diagram with three gates: IDE boundary, PR gate, build gate.

**Speaker notes:** Spotlighting paper (Hines et al.) takes prompt-injection ASR from >50% to <2% with delimiting/encoding. That is the academic anchor for IDE controls.

**Sources:**
- Hines et al. / Microsoft (2024) "Defending Against Indirect Prompt Injection Attacks With Spotlighting" - https://arxiv.org/abs/2403.14720
- Hou et al. (2025) "Model Context Protocol: Landscape, Security Threats, and Future Research Directions" - https://xinyi-hou.github.io/files/hou2025mcp_1.pdf
- Invariant Labs "MCP Security Notification: Tool Poisoning" - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks

---

## Slide 15 - Process

- Mandatory AI-usage disclosure at PR level
- Third-party AI tool intake review - the Context AI question
- AI-specific branch in IR playbook
- Dependency pinning as policy, not guidance

**Graphic:** PR template mock-up with an "AI used? yes/no/which tool" field highlighted.

**Speaker notes:** You cannot improve what you cannot see. The PR field is the most cost-effective lever in the whole programme. Pair with NIST SP 800-218A practice PO.1.

**Sources:**
- NIST SP 800-218A (SSDF community profile for Generative AI) - https://csrc.nist.gov/pubs/sp/800/218/a/final

---

## Slide 16 - Culture

- No merge until reviewed by someone who did not write the prompt
- Pair-review: one used AI, one did not
- Ownership is human, regardless of what wrote it
- Reward catches, not velocity

**Graphic:** Two-developer review pattern.

**Speaker notes:** This is where most programmes will stall. The metrics have to follow - if the pipeline rewards merge-rate and ignores caught-flaw-rate, you are training the wrong reflex.

**Sources:**
- Sandoval, Pearce, Nys, Karri, Garg, Dolan-Gavitt (USENIX Security 2023) "Lost at C" - https://arxiv.org/abs/2208.09727 (USENIX https://www.usenix.org/conference/usenixsecurity23/presentation/sandoval)

---

## Slide 17 - Organisational

- Name an owner: AppSec + engineering lead, not product
- Joint governance body that meets weekly, not quarterly
- Redistribute review workload: seniors review more, write less
- Hiring: interview for the review reflex, not the typing reflex

**Graphic:** Org-chart fragment with the AppSec/engineering joint owner highlighted.

**Speaker notes:** GitLab 2025 found 49% of orgs run 5+ AI tools - quarterly cadence cannot keep up. ISO 42001 Clause 5 makes leadership accountability explicit.

**Sources:**
- GitLab Global DevSecOps Report 2025 - https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/
- ISO/IEC 42001:2023 (AI Management System) - https://www.iso.org/standard/42001

---

## Slide 18 - Governance: anchor on NIST SP 800-218A

- NIST SP 800-218A - SSDF for GenAI - is your spine
- Layer NIST AI 600-1 for risk taxonomy; ISO/IEC 42001 for management system
- NCSC + CISA Secure AI System Development for lifecycle hooks
- Metrics: AI-assisted PR rate, vuln rate AI vs human, secret exposures from AI, MTTR for AI-introduced vulns

**Graphic:** Framework-stack diagram (NIST + ISO + NCSC/CISA + OWASP).

**Speaker notes:** If the room takes one URL home, this is it: https://csrc.nist.gov/pubs/sp/800/218/a/final. Audit-ready. Unambiguous. Free.

**Sources:**
- NIST SP 800-218A SSDF for GenAI - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST AI 600-1 GenAI Profile - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- ISO/IEC 42001:2023 - https://www.iso.org/standard/42001
- NCSC + CISA "Guidelines for Secure AI System Development" - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf
- OWASP Top 10 for LLM Applications 2025 - https://genai.owasp.org/llm-top-10/

---

## Slide 19 - Monday morning

- Inventory AI coding tools in use, including unsanctioned
- Require SAST + secret scanning on AI-assisted PRs
- Acceptable-use policy anchored to NIST SP 800-218A
- Audit what AI tools your build pipeline trusts (the Context AI question)
- Name the owner; stand up the governance body

**Graphic:** Five-checkbox card.

**Speaker notes:** These are five things a CISO can start before the next standup. None of them require new spend.

---

## Slide 20 - Q&A and tease Part 2

- Questions
- Bibliography sent with the recording
- Part 2: Running AI in Production - what you are actually defending now

**Graphic:** Series wordmark with Part 2 title and date.

**Speaker notes:** Once the code ships, it is someone else's attack surface. That is Part 2. Take questions.
