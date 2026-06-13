# Part 1 - Slide Plan (v8, problem-first, slimmed, primer cut)

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders (vendors, contractors and press excluded)
**Format:** 60-min slot. ~38 min content + 10 min Q&A + 5 min host preamble.
**Style:** Brief, high-level. Speaker carries the content; slides anchor.
**Slide count:** 17

> **Gamma briefs:** Each slide section below ends with a `### Gamma brief` fenced code block. Paste that block directly into gamma.app to generate the slide. The full bullets, speaker notes, and sources stay outside the brief - they're for the speaker, not the tool. A consolidated copy of the briefs lives in `slide-brief-v8.md`.

---

## The argument

1. The biggest shift in software development since the compiler is already underway. Adoption is universal in the enterprise; AI now writes 75% of new code at Google. The CISO question is no longer "will we use AI?" - it is "what is breaking, and what do we do about it?"
2. The breakage is real, measurable, and at scale. AI-attributed CVEs are showing up in production; review time is up 441%; security failure rates have not moved in four years across a generation of LLM upgrades; insecure-by-default code is shipping at 10x the human baseline; supply-chain attacks against AI tooling itself have arrived; and your developers are already routing prompts that contain proprietary code and credentials to vendor LLMs without DLP coverage.
3. Secure software development is a 30-year-old discipline with broad consensus, **and now codified in product law - EU CRA (in force Dec 2024), UK PSTI Act (full enforcement Apr 2024), EU AI Act (staged from Aug 2024)**. The 30-year consensus has just become a regulatory floor. That discipline is fundamentally a profession - it works because trusted humans (developer, reviewer, maintainer, operator) execute their work to professional standards. AI now sits inside every one of those trust delegations.
4. **NIST itself draws the line: SP 800-204D Appendix B carves PW.1 - PW.4 and PW.7 out of CI/CD pipeline scope on the grounds that they "pertain to secure software design, review of the design, and software reuse."** The judgment layer of the SDLC lives above the pipeline. You cannot fix what AI is breaking with more pipeline tooling alone.
5. The response is four practical categories - tooling, process, culture-and-organisation, governance - delivered as a "yes path" for confident AI adoption rather than a list of brakes. The cultural posture matters: developers will use whatever makes them effective, so the org that says yes to sanctioned tools fast beats the one that says no slowly.
6. The deck closes on the most generous version of the counter-argument - "maybe this all gets better when the models do" - and lets the rest of the talk do the rebutting.

---

## Structural shift from v7

Three changes from v7 drove this rebuild:

1. **Problem-first arc.** Open with adoption + real CVEs, walk the audience through the full risk pile (S2), name the discipline that should have prevented it (S1), prescribe the response (S3). Audience feels the damage before they hear the discipline that was supposed to prevent it. The buildings analogy on Slide 10 lands as moral indictment, not throat-clearing.
2. **S1 slimmed to two slides.** v6's "Defined discipline" name-check is absorbed into the Profession slide footer band; the regulatory floor (EU CRA, UK PSTI, EU AI Act) moves to the CI/CD-fits slide footer band. The standalone credibility slide didn't earn its place once the audience already cared.
3. **The W/R/D/T four-assumption frame is gone, the AI primer is cut.** v6's quadrant was scaffolding to fit a four-letter mnemonic; T (tools were deterministic) didn't map cleanly to anything codified. The deck makes its argument from data rather than a manufactured frame. The four-moving-parts AI primer is cut entirely - inline glosses on Slides 8, 12, and 13 cover MCP, harness, and RAG for a CISO audience.

Four content additions from a 24-risk coverage assessment (against `ai-sw-risks-v1.md`) are baked in:
- **Prompt injection of coding agents** on Slide 8 (the biggest gap - OWASP LLM01, 100% of tested coding agents vulnerable; build-time only, runtime version is Part 2).
- **Sycophancy** and **reproducibility** beats on Slide 5 (explain *why* the quality line is flat).
- **Skill atrophy** beat on Slide 14 (anchors "hire for the review reflex").

---

## How CI/CD fits (framing for Part 1)

CI/CD is the operational *enactment* of the SDLC. The SDLC defines what good development practices are; CI/CD pipelines are where those practices become automated, enforceable gates rather than aspirational policy. The bridge is explicit in the literature:

- **NIST SP 800-218 (SSDF)** defines the practices (the *what*).
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) - *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines* - is the companion publication that maps SSDF practices onto CI/CD pipeline stages: **build, test, package, deployment** (the *how*, in CI/CD terms). NIST itself draws the line: Appendix B carves SSDF practices PW.1 - PW.4 and PW.7 out of CI/CD scope on the grounds that they "pertain to secure software design, review of the design, and software reuse."
- **SLSA v1.2** defines build-platform integrity levels (L0 - L3) so "we built it on a trusted system" is provable rather than asserted.
- **DevSecOps** is the cultural framing: every CI/CD stage is also a security stage; shift-left because a CWE caught in a PR is roughly two orders of magnitude cheaper than one caught in production.

This is also the right place to land the build-time framing - this talk owns the build-time / artefact layer, distinct from the workforce and runtime layers in adjacent SASIG sessions. **Runtime concerns - production prompt injection, model supply-chain attacks, agent identity sprawl, AI-in-vendor-platforms - are explicitly Part 2 of the series.**

---

# Open

## Slide 1 - Title and the promise

- The New SDLC: Security When Every Developer Writes With AI
- The New Normal: Software, Security and the AI Stack - Part 1 of 2
- Non-product. 40% problem, 60% what to do. Every stat sourced.

**Graphic:** Series wordmark across the top. Title and subtitle centred. Restrained, sober.

**Speaker notes:** Welcome. Earn the room - say the non-product promise out loud. Tell them slides are deliberately light; the bibliography lands in their inbox after the session. The argument: the biggest shift in software development since the compiler is already in production, and the discipline that has made software secure for thirty years rests on assumptions that AI quietly removes. We will walk what is breaking, name the discipline AI is breaking, finish with what to do.

### Gamma brief

```
Title: The New SDLC
Subtitle: Security when every developer writes with AI
Tag: The New Normal: Software, Security and the AI Stack - Part 1 of 2
Footer: Bibliography lands in your inbox.
Visual: Series wordmark. Title slide.
Tone: Sober.
```

---

## Slide 2 - From tool to author

- **"Vibe coding" - coined Feb 2025** by Andrej Karpathy: "fully give in to the vibes... forget that the code even exists"
- **Collins Dictionary Word of the Year 2025** (Nov 6, 2025): "the use of artificial intelligence prompted by natural language to assist with the writing of computer code"
- **Google, Q1 2026 earnings call**: **75%** of new code is AI-generated and engineer-approved - up from 50% in fall 2025 and 25% in 2024
- **Adoption is not in dispute** (footer-only): Microsoft FY26 Q2 - 4.7M paid Copilot subscribers (~90% of Fortune 100); DORA 2025 (n~5,000) - 90% of devs use AI at work; McKinsey Feb 2026 - 90%+ of software teams use AI
- **Frontier labs sit higher**: Anthropic ~70-90% company-wide; senior engineers report personal workflows at ~100%
- **The board-level "why now"**: AI-centric organisations report **20-40% opex reductions** and **12-14pp EBITDA margin gains** (CIO May 2026)

**Graphic:** A single hero stat - 75% - dominates the centre. Below it, three small data points form the trajectory row (2024 / Fall 2025 / Q1 2026 = 25% / 50% / 75%). Karpathy pull quote sits below the trajectory. The board-level "why now" line sits as a quiet beat beneath the pull quote.

**Speaker notes:** Open with scale. Twelve months ago "vibe coding" was a Karpathy tweet. By November 2025 it was the Collins Word of the Year. By Q1 2026, on an audited earnings call, Sundar Pichai said 75% of all new code at Google is AI-generated. That figure was 25% in 2024 and 50% in fall 2025. The slope is the story: 25 -> 50 -> 75 in two product cycles.

One nuance worth naming explicitly so nobody catches it as a gotcha: Google's 75% is AI-generated *and engineer-approved*. So the human is still in the loop - on paper. Hold that thought, because the productivity-paradox slide in two slides' time will show that "engineer-approved" is doing a lot of work it can't actually do at scale.

Adoption is not the story we are spending time on. Three independent 2025-2026 sources (Microsoft, DORA, McKinsey) all converge on near-universal in the enterprise. That is footer-band material. The actual story is the trajectory of *how much code is being written by AI*, which is a different and more security-relevant question.

The frontier-lab numbers are softer-source - Boris Cherny on X, an Anthropic spokesperson clarifying 70-90% company-wide. Don't overclaim them. Use them as leading indicators: the people building the models run their workflows at the high end, and the rest of the industry is moving toward where they already are.

The board-level beat at the bottom is the "why now" your CISO audience needs to be able to recite back to their board. AI-centric organisations are reporting 20-40% operating-cost reductions and 12-14 percentage-point EBITDA margin improvements. That is the number that closes the conversation about whether AI development tools get adopted - they already are being adopted, and the financial pressure to keep adopting is structural. The blurb's "or be left far behind in the feature race" is what this number underwrites. Land it briefly - it's not the focus of the slide, but it earns the audience's attention for the security argument that follows.

The takeaway is not the headline number. It is the trajectory and what it implies. Whatever your build pipeline looks like today, in twelve months it will look more like Google's than like the 2024 baseline. The next six slides walk what is already breaking at scale.

**Sources:**
- Karpathy origin / vibe coding overview - https://en.wikipedia.org/wiki/Vibe_coding
- Collins Word of the Year 2025 - https://www.collinsdictionary.com/woty
- Collins definition - https://www.collinsdictionary.com/dictionary/english/vibe-coding
- Pichai, Alphabet Q1 2026 earnings - https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/
- Pichai, Cloud Next 2026 - https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
- DORA 2025 - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- McKinsey - https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development
- Microsoft FY26 Q2 earnings - https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q2/press-release-webcast
- Anthropic / OpenAI frontier-lab figures (Cherny, Roon via Fortune, Jan 2026) - https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
- AI-centric business outcomes (20-40% opex / 12-14pp EBITDA) - CIO, May 2026 - https://www.cio.com/article/4134741/how-agentic-ai-will-reshape-engineering-workflows-in-2026.html

### Gamma brief

```
Title: From tool to author
Subtitle: "Vibe coding" - Collins Word of the Year 2025

Hero stat: 75%
  Caption: of new code at Google is AI-generated and engineer-approved
  Source: Pichai, Alphabet Q1 2026 earnings

Trajectory row:
  2024: 25%
  Fall 2025: 50%
  Q1 2026: 75%

Pull quote (italic):
  "fully give in to the vibes... forget that the code even exists"
  - Andrej Karpathy, Feb 2025

Why now (board-level line, smaller type beneath the trajectory):
  AI-centric orgs report 20-40% opex reductions and 12-14pp EBITDA gains (CIO May 2026)

Closing line: The slope is the story.

Visual: 75% dominates the slide. Trajectory beneath it. Why-now line as a quiet board-level beat. Adoption headcount stats stay in speaker notes.
Tone: Crisp, audited. The "why now" the board hears.
```

---

## Slide 3 - Real CVEs in real repos

- **Georgia Tech Vibe Security Radar** (Apr 2026): 6 / 15 / 35 AI-attributed CVEs in Jan / Feb / Mar 2026; 74 lifetime; 27 traceable to Claude Code
- **Endor Labs / CMU Agent Security League** (Apr 2026): 200 real OSS tasks, top agent 84.4% functional but only **17.3%** security pass
- **Fu et al., ACM TOSEM 2025**: 29.5% of Python and 24.2% of JS Copilot snippets in real GitHub projects had at least one CWE
- *Real repos, real vulnerabilities, real CVEs - not benchmark data*

**Graphic:** Monthly bar chart on the left showing the 6 / 15 / 35 trajectory from Vibe Security Radar. Supporting stats as small caption rows on the right.

**Speaker notes:** Now drop the audience into the consequences. The Georgia Tech Vibe Security Radar is the cleanest signal we have. Their team walks fixing-commits back through git history and identifies when an AI tool wrote the original vulnerable code. Six AI-attributed CVEs in January, fifteen in February, thirty-five in March. Seventy-four lifetime so far. Twenty-seven of those traceable to a single tool, Claude Code. The slope is the story.

The Endor Labs / CMU benchmark is the agent-side signal. Two hundred real open-source tasks. The top performer hits 84% functional pass rate - so the agents work - but only 17% security pass. There is no version of "AI is too unreliable to use" that survives this data; equally, there is no version of "AI is good enough to trust" that survives it either. Both things are true at once.

The Fu et al. paper is the longitudinal signal. Roughly 30% of Python and 24% of JavaScript Copilot snippets in real GitHub projects ship with at least one CWE. This is not a controlled experiment - it's what is actually being merged.

The point of opening here is to ground the rest of the talk in the empirical record. We are not arguing about whether something is happening; we are talking about what to do given that it is. The next six slides walk the categories of damage the audience needs to see before we name the discipline AI is breaking.

**Sources:**
- Georgia Tech Vibe Security Radar - https://news.research.gatech.edu/2026/04/13/bad-vibes-ai-generated-code-vulnerable-researchers-warn (live https://vibe-radar-ten.vercel.app/)
- Endor Labs / CMU Agent Security League - https://www.endorlabs.com/research/ai-code-security-benchmark
- Fu et al., ACM TOSEM 2025 - https://dl.acm.org/doi/10.1145/3716848 (preprint https://arxiv.org/abs/2310.02059)

### Gamma brief

```
Title: Real CVEs in real repos
Hero chart: Georgia Tech Vibe Security Radar
  Jan 2026: 6
  Feb 2026: 15
  Mar 2026: 35
  Annotation: 27 traceable to Claude Code
Supporting bullets:
- 17.3% security pass on 200 OSS tasks (Endor / CMU, Apr 2026)
- 29.5% of Copilot Python snippets carry a CWE (Fu et al. 2025)
Visual: Monthly bar chart. Stats panel right.
Tone: Concrete. Not benchmarks - real CVEs.
```

---

# Section 2 - Where the risk is piling up

## Slide 4 - The productivity paradox

- DORA 2025 (~5,000 devs): **+21% tasks completed; +98% PRs merged** for individual developers using AI assistants
- METR Feb 2026 walkback: original -19% slowdown moderates to -4% (CI -15% to +9%); productivity gains "likely" - but METR explicitly does NOT retract the security/quality concerns
- BNY Mellon Feb 2026 (n=2,989): perceived productivity diverges from measured productivity - devs feel faster than the commit data shows
- DORA 2025 cost side: **PR review time +441%; PR size +51.3%; 30% distrust AI-generated code** but still merge it
- *The bottleneck has moved - the reviewer is now the load-bearing role*

**Graphic:** Two-panel chart - left: DORA +21% tasks / +98% PRs merged; METR -4% (with original -19% greyed out); right: DORA PR-size and review-time deltas drawn to scale (the +441% bar dominates).

**Speaker notes:** Productivity gains are real on developer-facing tasks. DORA 2025 - the largest survey of its kind, roughly 5,000 developers across thousands of organisations - measures a 21% increase in tasks completed and a 98% increase in pull requests merged for individual developers using AI assistants. METR's February 2026 walkback says their original -19% slowdown finding moderates to -4% with confidence interval -15% to +9% - so productivity gains are "likely." Worth noting METR explicitly did *not* retract the security and quality concerns alongside that walkback.

Worth one beat of caution on the headline numbers. A February 2026 BNY Mellon study - 2,989 developers surveyed at one of the largest enterprise dev orgs in the world - found that perceived productivity gains diverge meaningfully from what shows up in commit-based metrics. Developers feel faster. The measured signal is more cautious. Take the productivity numbers seriously, but do not assume measured throughput and felt productivity are the same thing.

Either way, the cost has shifted. The same DORA 2025 dataset shows PRs are 51% bigger and review time has stretched 441%. That is not a typo - it is five-and-a-half times as long to review a PR than the same team took before AI tools arrived.

When PRs are bigger, more frequent, and structurally harder to read - because LLM-generated code reads as if a competent person wrote it but contains the architectural flaws we'll see in the next three slides - reviewers do what humans always do under pressure. They rubber-stamp. The 30% of developers who self-report distrusting AI code still merge it. The trust gap doesn't translate into rejection because the rejection mechanism is review, and review capacity has not scaled with PR volume.

Worth absorbing the trust-gap signal here because it does not get its own slide: Stack Overflow's February 2026 survey of 84% of developers using AI but only 29% trusting it - an 11-point year-over-year drop in trust - is the same story. Your developers already know the tool is unreliable. Use is up; trust is down. The job is not to convince them; it is to build a review structure that matches what their instinct is already telling them.

This is why the rest of the talk is about review and governance, not speed.

**Sources:**
- DORA 2025 - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- METR Feb 2026 follow-up - https://metr.org/blog/2026-02-24-uplift-update/
- BNY Mellon "Beyond the Commit" Feb 2026 - https://arxiv.org/abs/2602.03593
- Stack Overflow Feb 2026 - https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/

### Gamma brief

```
Title: The productivity paradox
Two panels:
  Productivity: +21% tasks completed | +98% PRs merged (DORA 2025, ~5,000 devs)
  Review cost: +441% review time | PR size +51% (DORA 2025)
Closing line: The reviewer is now the load-bearing role.
Visual: Two-panel comparison. The +441% bar dominates.
Tone: Data-driven.
```

---

## Slide 5 - Quality on security is materially worse - and not improving

- Veracode Oct 2025 GenAI report (100+ LLMs across Java/JS/Python/C#): **45% of AI-generated code introduced risky security flaws**
- Veracode Spring 2026 rerun (100+ LLMs): **45% still vulnerable**; Java still 72%; newer models show no improvement
- "Broken by Default" arXiv:2604.05292 (Apr 2026): **55.8% of artifacts formally Z3-proven vulnerable**; **6 commercial SAST tools combined miss 97.8%**
- Two Veracode reruns six months apart plus formal verification all converge near 50% - **the line is flat across an LLM generation**
- **Sycophancy** explains *why* the line stays flat. SycEval (Feb 2025) measured **58% sycophantic responses** when LLMs were challenged; ELEPHANT (ICLR 2026) found LLMs affirm whichever side the user adopts in **48% of moral-conflict queries**. Devs ask "this is safe, right?" and get validation, not review.
- **Reproducibility** compounds it. Same prompt yields different code - security review of one run is not evidence about another.

**Graphic:** Three-bar comparison (Veracode Oct 2025 / Veracode Spring 2026 / Broken-by-Default Apr 2026) showing flat trajectory across two consecutive measurements. Two short rows beneath naming why the line stays flat (sycophancy + reproducibility). Supporting bullet on SAST miss rate.

**Speaker notes:** Two messages. One: across two consecutive Veracode reruns six months apart - October 2025 and Spring 2026 - the failure rate has not moved. Both measured 45% of AI-generated code introduces a risky security flaw, across 100+ models including the latest frontier ones. The "Broken by Default" formal-verification work in April 2026 measures 55.8% Z3-proven vulnerable - independent methodology, same neighbourhood of the answer. The line is flat across an LLM generation cycle.

Two: this is not heuristic noise - the formal-verification work proves it. And the SAST tools you bought to catch this miss 97.8% of these flaws *combined*. Your existing perimeter is not catching this category.

The interesting question is *why* the line stays flat when the models get better. Two reasons worth landing.

The first is sycophancy. The SycEval benchmark - February 2025, AAAI/AIES - measured 58% sycophantic responses across frontier models when their initial answer was challenged; ELEPHANT, accepted to ICLR 2026, showed LLMs affirm whichever side the user adopts in 48% of moral-conflict queries. The coding-specific harm is the conversation that goes "this is safe, right?" and gets back "yes, this looks correct." That is not review. That is validation - and an MIT 2026 study showed rational users still develop high confidence in false beliefs across long sycophantic interactions; willingness to verify drops. Your developer's instinct to push back is being trained out of them by the tool that was supposed to be helping them.

The second is reproducibility. LLM output is stochastic. The same prompt yields different code. A security review of one run is not evidence about another run, and behaviour can drift silently as the vendor updates the model under you. This is why traditional regression testing of generated code does not work the way it does for human-written code.

To be precise about scope: this is a build-pipeline gap, not a runtime adversarial-testing gap. New tooling categories are needed at the build-time perimeter, before code ever reaches a deployed environment that could be pen-tested. We come back to this in Section 3 when we discuss tooling.

**Sources:**
- Veracode Oct 2025 GenAI Code Security Report - https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
- Veracode Spring 2026 - https://www.veracode.com/blog/spring-2026-genai-code-security/
- Broken by Default - https://arxiv.org/abs/2604.05292
- SycEval (Feb 2025, AAAI/AIES) - https://arxiv.org/abs/2502.08177
- ELEPHANT (ICLR 2026) - https://arxiv.org/abs/2505.13995
- MIT 2026 study on user confidence under sycophantic interactions - https://arxiv.org/abs/2510.01395
- Reproducibility / non-determinism in AI code editors - https://mindgard.ai/blog/ai-code-security

### Gamma brief

```
Title: Quality on security - and not improving
Three-bar chart:
  Veracode Oct 2025: 45% (100+ LLMs)
  Veracode Spring 2026: 45% (rerun, 100+ LLMs)
  Broken-by-Default Apr 2026: 55.8% (Z3-proven)
Supporting line: 6 SAST tools combined miss 97.8%
Why the line is flat (two beats beneath the chart):
  Sycophancy: 58% sycophantic responses when challenged (SycEval Feb 2025); 48% affirmation rate in moral-conflict queries (ELEPHANT, ICLR 2026). Devs ask "this is safe, right?" and get validation, not review.
  Reproducibility: same prompt yields different code - security review of one run is not evidence about another.
Visual: Three bars showing a flat line across two consecutive Veracode reruns plus a formal-verification cross-check. Two short rows beneath naming why the line stays flat.
Tone: Sobering. The flat line is the headline; sycophancy and reproducibility are why it stays flat.
```

---

## Slide 6 - Insecure-by-default at scale

- **Apiiro Fortune-50 telemetry** (7,000+ devs, 62,000 repos): **10,000+ new findings/month** from AI-generated code by mid-2025; **10x in six months**
- **+322% privilege-escalation paths**; +153% architectural flaws; +40% secret exposures
- **41% of AI-generated backend code** ships with default-admin permissions when prompted naively (Backslash 2025); GPT-4.1 with naive prompts scored 1.5/10 on secure code; Claude 3.7 went from 6/10 to 10/10 with security-focused prompts
- AI-assisted projects show roughly **2x rate of cloud-credential exposure** vs non-AI baselines (GitGuardian 2026 / Snyk RSAC 2026 via Apiiro)
- **Snyk RSAC 2026 (Manoj Nair):** per-developer vulnerability rate **up 2-10x year-over-year** since AI-coding tools landed - the "shallow up, deep down" pattern at scale
- *Pattern: shallow up, deep down - trivial errors fell, architectural and identity flaws exploded*

**Graphic:** Apiiro hockey-stick of monthly findings on the left. Bullets on the right. The 41% default-admin-perms stat sits as a separate callout to make prompt engineering visible as a control plane.

**Speaker notes:** This is the largest single risk slide and it earns the space. The Apiiro telemetry is the cleanest enterprise signal we have. One Fortune-50 customer, 7,000 developers, 62,000 repositories - 10,000-plus new security findings per month from AI-generated code by mid-2025. Up 10x in six months. The directional caveat: this is one big data point, not a population estimate. The trend is the story.

The category breakdown matters more than the headline. Privilege-escalation paths up 322 percent. Architectural flaws up 153 percent. Secret exposures up 40 percent. Notice what *fell* - trivial syntax errors, missing semicolons, basic null checks. Those went down 76 percent. What rose was the deep stuff - the IAM scope decisions, the attack-path geometry, the credentials-in-the-wrong-place mistakes. Apiiro called this pattern "shallow up, deep down" and it's exactly right. AI fixes the surface; the depths go untended.

Default permissions are a related leverage point. Backslash showed 41 percent of naively-prompted backend code ships with default-admin permissions. The prompt is the control plane now. Your developers' prompt habits shape the vulnerability profile of what gets shipped. Backslash also showed Claude 3.7 went from 6/10 to 10/10 on secure-code generation when given security-focused prompts - the swing on prompt quality is enormous. Prompt engineering for security is a real discipline.

Snyk's RSAC 2026 keynote put the per-developer vulnerability rate up 2-10x year-over-year since AI-coding tools landed. That is not a benchmark - that is what their customers are seeing in production. This isn't laziness. It's that LLM output reads as if a competent person wrote it. Reviewer instincts that work for human-written code don't transfer. This is the operational manifestation of the sycophancy data on the previous slide.

This is what happens when the developer isn't really writing it, isn't really reading it, doesn't really know what it does. Specific risk categories follow.

**Sources:**
- Apiiro - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
- Apiiro companion - https://apiiro.com/blog/faster-code-greater-risks-the-security-trade-off-of-ai-driven-development/
- Backslash 2025 - https://www.backslash.security/press-releases/backslash-security-reveals-in-new-research-that-gpt-4-1-other-popular-llms-generate-insecure-code-unless-explicitly-prompted
- Snyk RSAC 2026 (per-developer vuln rate up 2-10x YoY) - https://expertinsights.com/industry-perspectives/rsac-2026-manoj-nair-snyk
- GitGuardian 2026 (~40% more secrets per commit for AI-tool users) - https://blog.gitguardian.com/yes-github-copilot-can-leak-secrets/

### Gamma brief

```
Title: Insecure-by-default at scale
Hero stat: 10x findings/month
  Caption: from AI-generated code (Apiiro Fortune-50, mid-2025)
Bullets:
- +322% privilege escalation paths
- +153% architectural flaws
- 41% ships with default-admin perms (Backslash)
Closing line: Shallow up, deep down.
Visual: Apiiro hockey-stick chart. Bullets right.
Tone: Let the slope speak.
```

---

## Slide 7 - Hallucinated dependencies and slopsquatting

- **Spracklen et al., USENIX Security 2025** - 576,000 samples, 16 LLMs studied
- Commercial LLMs **>=5.2%** hallucination rate; open-source **>=21.7%**; **205,474 unique fabricated package names**
- **43% of hallucinations recur across 10 prompt repeats** - perfect repeatability for an attacker
- **Lasso registered the hallucinated `huggingface-cli`** as an empty PyPI package: 30,000+ downloads in 3 months, including in Alibaba's GraphTranslator README
- *"Slopsquatting" coined by Seth Larson, Python Software Foundation*

**Graphic:** Per-LLM hallucination-rate bar chart on the left. Three-step attack-flow diagram on the right (LLM hallucinates name -> attacker registers it on PyPI/npm -> developer's AI-suggested import installs malware). Use red arrows for the attack path.

**Speaker notes:** This is the narrowest risk category in the talk but uniquely AI-native. The threat didn't exist before LLMs.

Spracklen et al. is the canonical work. 576,000 code-generation samples across 16 LLMs - commercial and open-source. They counted how often the LLM generated an `import` statement referring to a package that doesn't exist on PyPI or npm. Commercial LLMs hallucinate at a 5.2 percent rate or higher. Open-source models hallucinate at 21.7 percent or higher. Across the corpus they catalogued 205,474 unique fabricated package names.

The 43 percent number is the one that turns this from a curiosity into an attack. Forty-three percent of the hallucinated names recur across 10 prompt repeats. That is perfect repeatability for an attacker. They run the same prompt against the same model, watch which hallucinated package names come back consistently, register those names on PyPI or npm with malicious payloads, and wait. The next developer who runs the same prompt installs the attacker's package.

Lasso Security's huggingface-cli demo proves the attack works in the wild. They registered an empty package under that hallucinated name. Thirty thousand downloads in three months. Alibaba's GraphTranslator README documented an install command pointing to it. This is happening now.

The term "slopsquatting" was coined by Seth Larson at the Python Software Foundation. It's the next typosquatting and it does not need any user error to land - the LLM does the typo for you.

The CI gate to allowlist against a known-good registry is one of the highest-leverage controls in this whole talk. We come back to it in Section 3.

**Sources:**
- Spracklen et al., USENIX Security 2025 - https://arxiv.org/abs/2406.10279 (USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)
- Lasso huggingface-cli demo - https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks
- Slopsquatting term provenance (Seth Larson) - https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks

### Gamma brief

```
Title: Hallucinated dependencies and slopsquatting
Hero stat: 43%
  Caption: of LLM-hallucinated package names recur across 10 prompt repeats (Spracklen et al., USENIX 2025)
Bullets:
- 205,474 fabricated package names catalogued
- Lasso huggingface-cli: 30,000+ downloads in 3 months
- Reached vendor docs (Alibaba GraphTranslator)
Attack flow (3 steps): LLM hallucinates -> attacker registers on PyPI -> developer installs malware
Closing line: Perfect repeatability for an attacker.
Visual: Hallucination chart left. 3-step attack flow right with red arrows.
Tone: Concrete.
```

---

## Slide 8 - This is not "tools have CVEs"

**Top thesis (banner):** *Your CVE patching cadence is the wrong instrument for this.*

- **Prompt injection is a vulnerability *class*, not a CVE.** OWASP LLM01. 100% of tested coding agents (Claude Code, Cursor, Copilot) vulnerable. The state-of-the-art defences (PromptArmor, PromptGuard) reduce, they do not eliminate. You cannot patch your way out of a structural property of how LLMs read input.
- **The attack surface is content, not the network.** Any README, PR title, issue comment, retrieved doc, or rules file is potential attacker code that the agent reads as instruction. Real 2025-26 incidents:
  - **CamoLeak** - markdown image link in a public issue exfiltrated private repos and AWS keys via Copilot Chat
  - **Rules File Backdoor** - malicious instructions in `.cursor/rules` / `AGENTS.md` weaponise the AI against the developer
  - One **PR-title injection** made Claude Code Security Review, Gemini CLI Action, and GitHub Copilot Agent each post their own API keys
- **Agents act, so the blast radius is autonomous action - not passive theft.** An RCE in VS Code is credential theft. An RCE in an autonomous coding agent is the attacker pushing code, opening PRs, exfiltrating via commit, pivoting through MCP servers. 2026 CVEs to land: **Cursor RCE** (CVE-2026-26268), **Copilot Reprompt** (CVE-2026-21516), **Claude Code CLI RCE** (CVE-2026-35021), **Windsurf MCP zero-interaction** (CVE-2026-30615).
- **The perimeter does not exist yet.** **MCP servers** (the connectors that let AI tools talk to your systems): ~2,000 production servers scanned, **none authenticated** (Prakash AIP 2026). LiteLLM (Mar 2026) - 3.4M daily downloads, 40,000+ in the exposure window - is what supply-chain compromise looks like in this layer. Vercel / Context AI (Apr 2026) is what vendor breach pivots look like.
- *Hand-off: runtime prompt injection of your production AI features is Part 2*

**Graphic:** Top banner thesis dominates. Three argument bands beneath it: (1) "structural class" with the LLM01 / 100% of agents stat; (2) "content is attack surface" with the three injection incidents; (3) "agents act" with the CVE tile grid - the CVEs sit *inside* the third argument as evidence, not as the slide. Single quiet footer band names the supply-chain layer (LiteLLM, Vercel/Context AI, MCP no-auth) as evidence the perimeter is missing.

**Speaker notes:** This is the heaviest slot in S2. The audience walks in expecting "yes of course tools have CVEs - everything has CVEs." Land the pith fast: this is not that.

Three things make this layer structurally different from any tool category your CVE programme already covers.

**One: prompt injection is a vulnerability class, not a CVE.** OWASP LLM01. A buffer overflow gets patched and goes away. Prompt injection is structural - the model treats all input text as instruction-eligible because there is no syntactic boundary between the system prompt and the content the model reads. 100% of tested coding agents - Claude Code, Cursor, Copilot - are vulnerable. The 2026 academic state-of-the-art (PromptArmor, PromptGuard) cuts attack-success rates by 67 to 99 percent depending on technique - reduction, not elimination. You cannot patch your way out of how LLMs read input. This is the most important sentence in the slide: **your existing patch cadence does not retire this class of risk.**

**Two: the attack surface is content, not the network.** Your existing perimeter assumes attackers come through traffic, packets, malformed files. In this category, any README, any PR title, any issue comment, any retrieved doc, any rules file is potential attacker code that the agent treats as instruction.

CamoLeak: a markdown image link in a public GitHub issue. The Copilot Chat CSP bypass parsed the link as instruction and exfiltrated private repo contents, customer AWS keys, and source code. The "exploit" was a markdown image.

Rules File Backdoor: malicious instructions hidden in `.cursor/rules`, `AGENTS.md`, or similar config files. The agent reads them as system instructions. The AI is weaponised against the developer who is using it.

The cleanest one: a single PR-title injection made three different coding agents - Anthropic's Claude Code Security Review, Google's Gemini CLI Action, and GitHub Copilot Agent - each post their own API keys as PR comments. One attack. Three vendors. Same vulnerability class. Read by the title of a pull request.

Your TLS, your WAF, your SAST, your DLP - none of them defend the input channel that actually got exploited in any of these incidents.

**Three: agents act. The blast radius is what an autonomous agent can do, not what an attacker can read.** This is where the CVE list earns its place on the slide. An RCE in VS Code is a credential-theft incident - bad, manageable. An RCE in Claude Code with shell access and OAuth scopes is the attacker getting to push code, open PRs, exfiltrate via commit, and pivot through MCP servers - autonomously, on the developer's behalf. The CVE numbers - Cursor RCE, Copilot Reprompt, Claude Code CLI RCE, Windsurf MCP zero-interaction - look familiar in form. The *consequence* of the CVE is categorically different.

The supply-chain layer beneath all of this is the evidence that the perimeter has not been built yet. MCP - the Model Context Protocol - did not exist three years ago; today every coding harness ships with MCP integrations and Prakash's AIP 2026 paper scanned approximately 2,000 production MCP servers, none of them authenticated. LiteLLM in March 2026 - 3.4 million daily downloads, two backdoored releases, 40,000-plus downloads during the five-hour exposure window - is what supply-chain compromise looks like at this layer. Vercel and Context AI in April 2026 is what vendor breach pivots look like - a Lumma Stealer infection on a Context.ai employee pivoted to Workspace, then into Vercel's environment, customer environment variables and OAuth tokens offered for USD 2M on BreachForums.

The takeaway is not "patch your AI tools." The takeaway is: **your CVE patching cadence is the wrong instrument for the structural class.** Build-time defences against this are on Slide 12.

The hand-off line is deliberate. Runtime prompt injection of your production AI features - the LLM01 risk in your customer-facing product - is Part 2. Today is build-time only.

**Sources:**
- LiteLLM advisory - https://docs.litellm.ai/blog/security-update-march-2026
- Microsoft Security on Trivy/LiteLLM - https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
- Cursor CVE-2026-26268 - https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- Copilot Reprompt CVE-2026-21516 - https://www.paperclipped.de/en/blog/github-copilot-cve-2026-21516-reprompt-attack/
- Claude Code CLI CVE-2026-35021 - https://www.sentinelone.com/vulnerability-database/cve-2026-35021/
- "MCP by Design" supply-chain advisory - https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/
- Hou et al. 2025 (MCP threat model) - https://arxiv.org/abs/2503.23278
- AIP MCP scan paper (Prakash 2026) - https://arxiv.org/abs/2603.24775
- Vercel security bulletin - https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
- TechCrunch on Vercel/Context AI - https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/
- OWASP LLM01 (Prompt Injection) - https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- Prompt injection on agentic coding assistants (arXiv 2601.17548) - https://arxiv.org/abs/2601.17548
- Three coding agents leaked secrets through one PR-title injection (VentureBeat, 2026) - https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026
- New Rules File Backdoor Attack - The Hacker News - https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html
- CamoLeak / GitHub Copilot Chat - Legit Security - https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code

### Gamma brief

```
Title: This is not "tools have CVEs"
Banner (top, large): Your CVE patching cadence is the wrong instrument for this.

Three argument bands:

  1. A vulnerability class, not a CVE
     Prompt injection (OWASP LLM01) is structural - LLMs treat all input as instruction-eligible
     100% of tested coding agents (Claude Code, Cursor, Copilot) vulnerable
     2026 defences (PromptArmor, PromptGuard) reduce ASR by 67-99% - reduction, not elimination

  2. The attack surface is content, not the network
     CamoLeak - markdown image link in a public issue exfiltrated private repos and AWS keys (Copilot Chat)
     Rules File Backdoor - malicious instructions in .cursor/rules or AGENTS.md weaponise the AI
     One PR-title injection made Claude Code Security Review, Gemini CLI Action, and Copilot Agent post their own keys
     Your TLS / WAF / SAST / DLP do not defend this channel

  3. Agents act - blast radius is autonomous action, not passive theft
     CVE tile grid (2026): Cursor RCE | Copilot Reprompt | Claude Code CLI RCE | Windsurf MCP zero-interaction
     RCE in an autonomous agent = the attacker pushing code, opening PRs, pivoting through MCP - autonomously

Footer band (the perimeter does not exist yet):
  ~2,000 production MCP servers, none authenticated (Prakash AIP 2026)
  LiteLLM Mar 2026: 3.4M daily downloads, 40k+ in the exposure window
  Vercel / Context AI Apr 2026: AI-vendor breach pivots into customer environment

Hand-off line (italic, smaller): Runtime prompt injection of your production AI features is Part 2.

Visual: Banner thesis dominates the top third. Three argument bands beneath. CVE tile grid sits inside band three as evidence, not as the slide. Quiet supply-chain footer band beneath. No more "list of CVEs" - the slide makes a structural argument.
Tone: Sharp. The audience expects "tools have CVEs"; the slide tells them why this is not that.
```

---

## Slide 9 - Shadow AI - your developers will route around you

**Hero line (large, set off):** *Developers will use whatever makes them effective. If security is too slow, they choose for you.*

- **3 of 4 CISOs** find unsanctioned coding tools already running in their estate (Aikido 2026)
- **75%+ of knowledge workers** use GenAI at work; substantial fractions admit to risky data-handling (Sysdig 2026)
- **Consequence: prompts routinely include proprietary source code, credentials, customer data, strategic context** - sent to vendor LLMs with no DLP coverage of that channel
- **Zscaler tracked 4.2M gen-AI-attributed data-loss violations in a single year** (the channel volume the perimeter currently does not see)
- Shadow-AI incidents reportedly cost ~**$650K above the breach baseline**
- *Cues Slide 14: the org that says yes to a sanctioned tool fast beats the one that says no slowly*

**Graphic:** Hero line dominates the top half. Supporting bullets as a quiet right-side panel with the data points. Subtle "developer routing around a blocked door" motif as background, restrained.

**Speaker notes:** This is the people problem behind the data. The previous five slides documented what AI is doing to your code. This slide is about what your *developers* are doing in response to AI - and what your security organisation looks like from their side of the desk.

Lead with the bind. Developers will use whatever makes them effective. If they cannot get sanctioned access to AI tools through procurement and security, they will use unsanctioned access - personal accounts, browser extensions, IDE plugins their company never reviewed. This is not new; it is the consumerisation-of-IT story from fifteen years ago, replayed at higher stakes.

The numbers. Three of four CISOs surveyed find unsanctioned coding tools already running in their estate - Aikido's State of AI 2026 report. Across the broader knowledge-worker population, Sysdig and others put usage at 75%+. Zscaler's data-loss telemetry tracked 4.2 million gen-AI-attributed data-loss violations in a single year - that is the volume of the channel your perimeter currently does not see.

The consequence is not abstract. Every prompt your developers send to a non-sanctioned LLM may include proprietary source code, customer data, strategic context, or credentials. Samsung had three source-code leaks within twenty days of allowing ChatGPT internally. The financial impact reporting suggests shadow-AI incidents land roughly $650K above your standard breach baseline - GitGuardian and others put AI-coding-tool users at ~40% more secrets per commit than non-AI users.

The IP-leakage angle is what to land for a SASIG audience. This is happening now, in your organisation, today. You can pretend it isn't and absorb the surprise when it shows up in a breach disclosure - or you can build the response on Slide 14, which is fundamentally about not being the team that says no slowly.

This slide cues the culture and organisation slide directly. The mitigation is not to ban shadow AI - that is structurally impossible. The mitigation is to be the org that says yes to a sanctioned tool fast enough that there is no demand for shadow AI.

**Sources:**
- Aikido - State of AI in Security & Development 2026 - https://www.aikido.dev/state-of-ai-security-development-2026
- Sysdig - "Real risks live at runtime: Why CISOs must care about deep telemetry in 2026" (3-of-4 unsanctioned GenAI stat) - https://webflow.sysdig.com/blog/real-risks-live-at-runtime-why-cisos-must-care-about-deep-telemetry-in-2026
- Zscaler 4.2M GenAI data-loss violations - https://www.zscaler.com/press/zscaler-threatlabz-2025-ai-security-report
- Netwrix - 12 Critical Shadow AI Security Risks 2026 - https://netwrix.com/en/resources/blog/shadow-ai-security-risks/
- Palo Alto Networks - What Is Shadow AI? - https://www.paloaltonetworks.com/cyberpedia/what-is-shadow-ai
- The Hacker News - The Hidden Security Risks of Shadow AI - https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html
- GitGuardian 2026 (AI-coding-tool users leak ~40% more secrets per commit) - https://blog.gitguardian.com/yes-github-copilot-can-leak-secrets/
- Samsung ChatGPT source-code leak history - https://ransomleak.com/blog/ai-data-leakage-employees/

### Gamma brief

```
Title: Shadow AI - your developers will route around you
Subtitle: The cost of being too slow

Hero line (large, set off):
  Developers will use whatever makes them effective. If security is too slow, they choose for you.

Supporting bullets:
- 3 of 4 CISOs find unsanctioned coding tools already running in their estate (Aikido 2026)
- 75%+ of knowledge workers use GenAI at work (Sysdig 2026)
- Consequence: prompts routinely include proprietary code and credentials sent to vendor LLMs without DLP coverage

Closing line: The org that says yes to a sanctioned tool fast beats the one that says no slowly.

Visual: Hero line dominates. Supporting bullets as a quiet right-side panel. Subtle "developer route around blocked door" motif as background, restrained.
Tone: Direct. The people problem behind the data. Cues Slide 14 (Culture and Organisation).
```

---

# Section 1 - The discipline that should have prevented this

## Slide 10 - Secure SDLC is a profession

**Top thesis (banner):** *"Buildings don't fall down only because of monitoring. They don't fall down because designers and builders behaved professionally."*

- A profession is the mechanism by which society delegates trust. We delegate to humans we believe to be competent - they execute their work to the standards we lay out, and we don't have to inspect every weld.
- Secure software development works the same way. We don't audit every line - we trust the developer. We don't review every dependency manually - we trust the maintainer chose it knowingly. We don't decompile every tool - we trust the operator wields it deterministically.
- Without that delegation, every line, every dep, every tool would need exhaustive verification. It doesn't scale.
- **The profession's codifications:** Microsoft SDL (2004) | NIST SSDF v1.1 (2022) | OWASP SAMM v2 | BSIMM 15 - 30 years of consensus.
- AI now sits inside every one of those trust delegations. *That is what you just watched break in Section 2.*

**Graphic:** Two-panel diagram. Left: building under construction with arrows from "designer" and "builder" labelled "professional practice." Right: code repo with arrows from "developer," "reviewer," "maintainer," "operator" labelled "professional practice." Footer band names the four frameworks (SDL, SSDF, SAMM, BSIMM 15) in muted type.

**Speaker notes:** Step back. Secure software development is not first a tooling stack - it's a profession. After Section 2's six slides of damage, this slide is where the audience hears why those incidents happened in language that names the loss.

The buildings analogy is the cleanest way to land it. Buildings don't fall down because the planning department audits every weld. They don't fall down because there's a regulator at the foundation pour. They don't fall down because the designer and the builder behaved professionally - they applied their training, they followed the standards, they took responsibility for what they signed off on. Monitoring matters; it's a backstop. But the primary mechanism by which buildings stay up is the professional practice of the people who designed and built them.

Software security has worked this way for thirty years. We don't audit every line of code in production. We don't manually review every package in our SBOM. We don't decompile every binary in our toolchain. We trust - we trust the developer wrote it knowingly, we trust the reviewer read it carefully, we trust the maintainer chose dependencies that were real and maintained, we trust the operator wielded the tools deterministically. That trust is the assumption stack the rest of the discipline sits on top of.

The profession has codified itself. Microsoft SDL is the grandfather, originating in the 2002 Trustworthy Computing memo and published as SDL around 2004 - five phases, ten practices including threat modelling and supply-chain security. NIST SSDF v1.1 (Feb 2022) is the U.S. federal baseline - PO, PS, PW, RV practice groups; v1.2 is in public comment now. OWASP SAMM v2 is the open-source maturity model. BSIMM 15 (2024) is the empirical model - what 121 firms actually do, measured. Take the convergence as established.

The reason this matters now: AI sits inside every one of those trust delegations. With AI in the loop, what does the developer actually know about what was just written? That is what you watched break across Section 2 - the productivity paradox showed reviewer attention collapsing under PR volume; the quality slide showed sycophancy training the developer's instinct out of them; the dependency slide showed package-name trust being weaponised; the toolchain slide showed the tools themselves being compromised; the shadow-AI slide showed developers routing around the controls entirely.

This is moral indictment, not framework throat-clearing. The audience just sat through the consequences. Now they hear the discipline they were supposed to be exercising.

**Sources:**
- Microsoft SDL practices - https://www.microsoft.com/en-us/securityengineering/sdl/practices
- NIST SSDF (project page) - https://csrc.nist.gov/projects/ssdf
- NIST SP 800-218 v1.1 - https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF v1.2 public comment notice - https://www.nist.gov/news-events/news/2025/12/secure-software-development-framework-ssdf-version-12-available-public
- OWASP SAMM - https://owaspsamm.org/model/
- BSIMM 15 datasheet - https://www.blackduck.com/content/dam/black-duck/en-us/datasheets/bsimm-datasheet.pdf

### Gamma brief

```
Title: Secure SDLC is a profession
Banner quote: "Buildings don't fall down because of monitoring. They don't fall down because designers and builders behaved professionally."
Two-panel comparison:
  Buildings: designer | builder
  Software: developer | reviewer | maintainer | operator
Common base: the profession's codifications - SDL (2004), SSDF (2022), SAMM, BSIMM 15
Closing line: Trust delegated to humans we believed competent. AI just sat down inside that delegation.
Visual: Architectural line-art left, code-repo schematic right. Footer band lists the four frameworks in muted type.
Tone: Reflective. After Section 2, this lands as moral indictment.
```

---

## Slide 11 - SDLC defines, pipelines enforce

- **SDLC = practices** (NIST SSDF, Microsoft SDL, OWASP SAMM, BSIMM). **CI/CD = enforcement** - where the practices become automated gates or get bypassed.
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) is the explicit bridge. Pipeline stages: **build, test, package, deployment**.
- **NIST itself draws the line.** Appendix B carves SSDF practices **PW.1 - PW.4 and PW.7** out of CI/CD pipeline scope on the grounds that they "pertain to secure software design, review of the design, and software reuse." Read plainly: that is the human-judgment layer of the SSDF.
- The judgment layer (Writer, Reviewer, Dependency) lives **above** the pipeline. Tool integrity rides on it.
- **SLSA v1.2 build levels (L0 - L3)** turn build-platform integrity from assertion into evidence.
- *Now codified in product law (footer band):* **EU CRA (Dec 2024) | UK PSTI Act (Apr 2024) | EU AI Act (Aug 2024)**
- *Closing line:* **You cannot fix what you just saw with more pipeline tooling alone.**

**Graphic:** Two-tier diagram. Top tier: "SDLC practices (the human-judgment layer)" labelled with Writer / Reviewer / Dependency. Bottom tier: "CI/CD pipeline (build, test, package, deploy)" labelled with Tool. NIST's Appendix B citation is the dividing line. SLSA badge on the build-platform box. Regulation footer band beneath the diagram in a muted accent colour.

**Speaker notes:** This slide is the bridge from "here is the damage" to "here is what to actually do." Walk it slowly.

The question this slide answers is "but our developers already do CI/CD - isn't that enough?" The pipeline is the *runway* for the SDLC. Without an SDLC defining what the gates need to enforce, you have a fast deployment pipeline that ships insecure code faster.

The point worth landing slowly is the carve-out. NIST 800-204D is one of the few places where a standards body is candid about what the pipeline *can't* do. Read their words carefully: practices PW.1 through PW.4 and PW.7 - secure design, threat modelling, software-reuse decisions, code review - "pertain to secure software design, review of the design, and software reuse." That's NIST's wording. The pipeline can't enact those activities; never could. Appendix B similarly carves out vulnerability response (RV.1 - RV.3) as "at the organization policy level."

The human-judgment layer of the SDLC - Writer, Reviewer, Dependency - lives above the pipeline. Tool integrity rides on the pipeline itself, and even there the pipeline only enforces *codifiable* aspects of tool integrity (version pinning, allowlists, signing). Residual judgment isn't pipeline material.

In Section 2 you watched AI compress or remove exactly the human-judgment layer that the pipeline was never going to do. That is why "more pipeline tooling" alone won't save you. The pipeline reinforces tool integrity - which it can - but the rest is restored elsewhere. Section 3, in three slides' time, is what the rest looks like.

The footer band on regulation matters for a CISO audience. As of late 2024 / early 2025 this is no longer just industry consensus - it is a regulatory floor in your home jurisdictions. EU CRA covers any product with digital elements sold into the EU. UK PSTI is in full force. The EU AI Act applies on top where AI components are involved. Your customers' regulators now require what these frameworks recommend. So the discipline being broken on Section 2's slides isn't just a craft loss - it's a compliance liability.

The closing line is the bridge. "You cannot fix what you just saw with more pipeline tooling alone." Land it cleanly and pivot to Section 3.

**Sources:**
- NIST SP 800-204D (Chandramouli, Kautz, Torres-Arias, Feb 2024), DOI https://doi.org/10.6028/NIST.SP.800-204D - landing page https://csrc.nist.gov/pubs/sp/800/204/d/final
- SLSA v1.2 spec - https://slsa.dev/spec/v1.2/
- OWASP DevSecOps Guideline - https://owasp.org/www-project-devsecops-guideline/
- CISA Secure by Design - https://www.cisa.gov/securebydesign
- EU Cyber Resilience Act - https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- UK PSTI Act - https://www.gov.uk/government/collections/the-product-security-and-telecommunications-infrastructure-psti-act
- EU AI Act - https://artificialintelligenceact.eu/

### Gamma brief

```
Title: SDLC defines, pipelines enforce
Two-tier diagram:
  Top tier - SDLC practices (the human-judgment layer): Writer, Reviewer, Dependency
  Bottom tier - CI/CD pipeline (build - test - package - deploy): Tool
Divider citation (italic): NIST SP 800-204D Appendix B - "pertain to secure software design, review of the design, and software reuse"
Side caption: The judgment layer lives above the pipeline.
Footer band (now codified in product law): EU CRA (Dec 2024) | UK PSTI (Apr 2024) | EU AI Act (Aug 2024)
Closing line: You cannot fix what you just saw with more pipeline tooling alone.
Visual: Two stacked bands. SLSA badge on the build box. Regulation footer band in muted accent colour.
Tone: Definitive. The bridge from "here is the damage" to "here is what to actually do."
```

---

# Section 3 - What to do

## Slide 12 - Tooling - what a confidently AI-enabled SDLC looks like

*Section opener. Reframe: the four gates are the **means** of confident AI adoption, not the destination. Section 3 is the "yes path" - here is what good looks like.*

- **AI-asset & MCP-server inventory** as the precondition for every other control - you cannot scan what you cannot see (the new shadow-IT discovery problem)
- **IDE-boundary controls** - inspect prompts, block secrets, govern context, allowlist tool calls. 2026 prompt-injection defences (PromptArmor, PromptGuard) cut attack-success rates by **67-99%** depending on technique
- **PR gates fail-closed** - SAST + secret scanning + SCA on every AI-assisted PR; **block hallucinated imports** against a known-good registry allowlist
- **Pin AI tool versions** (Cursor, Copilot, Claude Code, Cline - the harness layer); **treat MCP servers as third-party dependencies** subject to existing controls
- *Pipeline-enforceable. Inventory first, then gates.*

*Footer band:* **And the defenders are evolving too** - AI-aware SAST is the new perimeter category (Snyk DeepCode, Datadog OSS AI-native SAST, DryRun, Endor Labs, Semgrep, GitHub CodeQL). Multi-agent reasoning detects business-logic and AI-specific flaws (incl. prompt injection) that pattern-based SAST misses. Fight AI with AI.

**Graphic:** Linear horizontal pipeline diagram with four labelled gates (asset inventory -> IDE boundary -> PR gate -> build gate). Single quiet footer band beneath the pipeline names the AI-aware SAST category.

**Speaker notes:** Section 3 is the "yes path." This is what a confidently AI-enabled SDLC looks like in operation - the four gates here, the human-judgment restorations on the next two slides, governance on the slide after that. The frame for this section is not "how do we slow AI down"; it is "how do we let our developers move fast safely." The four gates are the means. The destination is a build pipeline that lets your developers use whatever AI tools they need without asking permission, because the controls are in the pipeline rather than in the gating committee.

Tooling is the cleanest-wins category and it earns being first. Start with the one pipelines can do.

Asset inventory first. You cannot scan what you cannot see. AI-asset and MCP-server discovery is the new shadow-IT discovery problem - the same 2010s-era playbook applies, just on new asset types. Every harness, every MCP server, every model endpoint, every coding assistant has to be inventoried before any other control matters. This is also where the shadow-AI conversation from Slide 9 comes to ground - you cannot govern prompt content, IP-leakage, or credential exposure on tools you do not know exist.

IDE-boundary controls. Prompts leaving the developer endpoint should be inspectable; secrets in those prompts should be blocked; file context should be governed; tool calls should be allowlisted. The 2026 defence stack is real: PromptArmor uses an LLM-as-filter approach measuring over 99% attack prevention on AgentDojo with sub-1% false positive and false negative rates; PromptGuard's four-layer framework cuts injection success by 67% across PromptBench and InjectBench. Multi-model voting and behavioural monitoring of tool calls add layered reductions on top. None of these is a silver bullet; the 2026 consensus is layered defence at the IDE boundary, and that is the build-time response to the prompt-injection attacks named on Slide 8.

PR gates. SAST, secret scanning, SCA on every AI-assisted PR - mandatory, fail-closed. Block hallucinated imports at CI by allowlisting against a known-good package registry. Veracode and Apiiro both report that the same controls applied universally reduce AI-introduced risk to roughly the human-only baseline. This isn't new tooling - it's the existing tooling applied without exception.

Pin AI coding tool versions. The "harness" layer - Cursor, Copilot, Claude Code, Cline - these are the wrappers that turn LLM prediction into action on the developer's machine; treat them as third-party software with version pinning, not as continuously updating SaaS. Treat MCP servers as third-party dependencies subject to your existing controls. Hou et al. catalogue 16-plus MCP-specific threats in their full work, and Invariant Labs has demonstrated rug-pull tool poisoning where benign tool descriptions silently mutate on second launch. Real attacks, fixable with version pinning and intake review.

The footer band is the move I want to land for an "enable" framing. The defence is evolving alongside the offence. The category to track is AI-aware SAST - multi-agent reasoning systems (DryRun, Snyk DeepCode, Datadog's open-source AI-native SAST, Endor Labs, Semgrep, GitHub CodeQL) that detect business-logic and AI-specific flaws including prompt injection. Pattern-based SAST is structurally insufficient against LLM-generated code; the new category exists for exactly that reason. Mention briefly - the audience hears "you can fight AI with AI."

Crucially, this slide is short for a reason. Pipelines reinforce the tool layer. They cannot restore writer judgment, reviewer attention, or dependency provenance. The next two slides are what actually restores those.

**Sources:**
- Prompt Injection Defense 2026 - 8 techniques ranked (TokenMix) - https://tokenmix.ai/blog/prompt-injection-defense-techniques-2026
- Hou et al. MCP Landscape (2025) - https://arxiv.org/abs/2503.23278
- Invariant Labs MCP tool-poisoning / rug-pull - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
- DryRun - "Top 10 AI SAST Tools for 2026" - https://www.dryrun.security/blog/top-ai-sast-tools-2026
- Snyk DeepCode AI - https://snyk.io/platform/deepcode-ai/
- Datadog open-source AI-native SAST - https://www.datadoghq.com/blog/open-source-ai-sast/
- Endor Labs - AI Risk Reduction guide 2026 - https://www.endorlabs.com/learn/ai-risk-reduction-complete-guide-to-mitigation-strategies-for-2026

### Gamma brief

```
Title: Tooling - what a confidently AI-enabled SDLC looks like
Subtitle: The yes path - four gates, then AI-aware defence in parallel
Pipeline diagram with four gates:
  1. AI-asset & MCP inventory
       Caption: the new shadow IT - cannot govern what you cannot see
  2. IDE boundary
       Caption: 2026 defences (PromptArmor, PromptGuard) cut prompt-injection ASR by 67-99%
  3. PR gate (fail-closed)
       Caption: SAST + secrets + SCA on AI-assisted PRs; block hallucinated imports
  4. Build gate
       Caption: pin AI tool versions (Cursor, Copilot, Claude Code, Cline - the harness layer); treat MCP servers as third-party deps
Closing line: Inventory first, then gates - so your developers can move fast safely.
Footer band (single quiet line beneath the pipeline):
  And the defenders are evolving too - AI-aware SAST is the new perimeter category (Snyk DeepCode, Datadog OSS, DryRun, Endor, Semgrep, GitHub CodeQL). Fight AI with AI.
Visual: Linear horizontal pipeline with four vertical gate bars. Single muted footer band beneath the pipeline carries the AI-aware-SAST line - supporting context, not a fifth gate.
Tone: Operational and enabling. The "what good looks like" opener for Section 3.
```

---

## Slide 13 - Process - the human-judgment restorations

*Lead-in (italic, top of slide):* **Tooling enforces policy. It does not write policy. Six rules you cannot skip.**

- **Acceptable Use Policy for AI coding tools** - Standing rules: which tools are sanctioned, which actions are prohibited (no production secrets in prompts, no personal accounts, no consumer-tier LLMs against proprietary code), what counts as an override and who can authorise it. Stack Overflow 2025: 84% of devs use AI tools, only **28% of organisations have a formal AI policy**. The cheapest standing document with the broadest enforcement reach - templates from ISACA, WWT, Lattice, Adelia. *Anchors:* ISO/IEC 42001 A.3.2 (Policies related to AI); ETSI TS 104 223 Principle 1.
- **Data classification policy for prompts and context** - Tiered classification (public / internal / sensitive / prohibited) mapped to which AI tools are allowed for which tier. UK GDPR, HIPAA, PCI-DSS, ITAR/EAR already require classification of regulated data; AI tools are simply another egress channel that needs the same tier mapping. Without this, the AI-aware DLP on Slide 12 Gate 2 has no policy to enforce. *Anchors:* ISO/IEC 27001:2022 A.5.12 (Classification), A.5.13 (Labelling), A.8.12 (DLP); ISO/IEC 42001 A.7 (Data for AI systems); **ICO Guidance on AI and Data Protection**.
- **DPIA and privacy assessment policy** - Decide a default position: which AI coding tools, contexts, and data flows trigger a Data Protection Impact Assessment under **UK GDPR Article 35** before rollout, and which do not. The ICO's published view is that AI processing "in the vast majority of cases" triggers a DPIA - silence is not a policy. Different decision-owner (DPO / Privacy lead) than data classification (AppSec). *Anchors:* UK GDPR Art. 35; **ICO AI and Data Protection Risk Toolkit**; ISO/IEC 42001 A.6.1.4 (AI system impact assessment); ETSI TS 104 223 Principle 3.
- **Threat-modelling discipline** - Required at design time for any feature with an LLM call, a coding agent, or an MCP integration. Map the new failure modes onto familiar categories - prompt injection -> Tampering, excessive agency -> Elevation of Privilege, tool poisoning -> Spoofing, unbounded compute -> Denial of Service. The CISO decision is when it is required, what method, who reviews, what gates the merge. *Anchors:* **MITRE ATLAS v5.1** (Nov 2025, the canonical adversarial-AI knowledge base); **OWASP Multi-Agentic System Threat Modeling Guide v1.0** + OWASP *Agentic AI - Threats and Mitigations* (Apr 2025); **STRIDE-AI** (Mauri & Damiani, IEEE 2021); ETSI TS 104 223 Principle 3.
- **Tool, model, and MCP intake** - Criteria for sanctioning anything that touches the developer environment. Standing requirements: enterprise contract terms (**no-train-on-data, zero data retention, data residency, sub-processor controls, breach notification, model-change notice**), adversarial red-team results, an integration threat model, refresh cadence. The intake *decision* is the policy; the approved list is the artefact Slide 12 Gate 4 enforces cryptographically. *Anchors:* ISO/IEC 42001 A.10.3 (Suppliers); ISO/IEC 27001:2022 A.5.19-A.5.23 (supplier-relationship controls); ETSI TS 104 223 Principle 6.
- **AI-specific incident-response policy** - Pre-decided scenarios with named playbook entries: AI-introduced CVE in a merged commit; upstream AI-tool compromise (LiteLLM, March 2026); model-provider key rotation; a poisoned MCP server disclosed weeks after being sanctioned (Slide 12 Gate 3 commit trailers are the query surface for "find every commit that touched it"); vendor breach with credential pivot (Vercel / Context AI, April 2026). *Anchors:* **Five Eyes - Careful Adoption of Agentic AI Services** (May 2026); ISO/IEC 27001:2022 A.5.24-A.5.28 (incident management); ISO/IEC 42001 A.6.2.8 (AI system event logging); NCSC-UK incident-management guidance.

**Graphic:** Six labelled blocks across the top - AUP / Data classification / DPIA / Threat model / Intake / IR - with arrows fanning down to "Slide 12 enforces" on one side and "Slide 14 lives" on the other. Makes the upstream/downstream relationship visible without a frame or acronym.

**Speaker notes:** **The argument:** the gates on Slide 12 can only enforce rules that exist. Someone has to write the rules down first. Six rules you cannot skip.

The pipeline cannot decide whether your developers are allowed to paste customer data into ChatGPT - that is a policy call. It cannot decide whether using AI to help write code triggers a GDPR DPIA - that is a privacy-and-legal call. It cannot decide what contract terms you require from a vendor before letting Cursor or Copilot near your codebase - that is a procurement call. None of those have right answers that pop out of a tool. A human has to make each call, write it down, and own it.

Six bullets on the slide, each one a question of that kind:

- **AUP** - are people allowed to use this tool, and for what?
- **Data classification** - what data is allowed in a prompt?
- **DPIA** - does using this tool trigger UK GDPR Article 35?
- **Threat model** - when we build something with AI, what could go wrong?
- **Intake** - what hoops does a vendor jump through before we let their tool near our code?
- **IR** - what do we do when one of these tools gets compromised?

Two practical beats worth saying aloud. First, most of this is template selection, not original work - ISACA AUP templates, ISO/IEC 42001 Annex A, ETSI TS 104 223, and the ICO Risk Toolkit all do the heavy lifting. Pick and adopt. Second, the decision-owners differ - AUP and intake are AppSec calls, DPIA is the DPO or Privacy lead, threat models live with engineering. The slide is policy-level so each owner picks their piece up.

**Take-away: process decides; tooling enforces.** Slide 12's gates can only run against rules that exist. This slide is where the rules get written.

**Sources:**
- ISACA AI Acceptable Use Policy Template - https://www.isaca.org/resources/artificial-intelligence-acceptable-use-policy-template
- Stack Overflow Developer Survey 2025 - https://survey.stackoverflow.co/2025
- ISO/IEC 42001:2023 (A.3.2 Policies, A.6.1.4 Impact assessment, A.6.2.8 Event logging, A.7 Data, A.10.3 Suppliers) - https://www.iso.org/standard/42001
- ISO/IEC 27001:2022 (A.5.12 Classification, A.5.13 Labelling, A.5.19-A.5.23 Supplier controls, A.5.24-A.5.28 Incident management, A.8.12 DLP) - https://www.iso.org/standard/27001
- UK AI Cyber Security Code of Practice (DSIT, Jan 2025) / ETSI TS 104 223 (Apr 2025) - https://www.etsi.org/deliver/etsi_TS/104200_104299/104223/01.01.01_60/ts_104223v010101p.pdf
- ICO Guidance on AI and Data Protection - https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
- ICO AI and Data Protection Risk Toolkit - https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/ai-and-data-protection-risk-toolkit/
- UK GDPR Article 35 (DPIA) - ICO guidance - https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/
- MITRE ATLAS v5.1 (Nov 2025) - https://atlas.mitre.org/
- OWASP Multi-Agentic System Threat Modeling Guide v1.0 - https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/
- OWASP Agentic AI - Threats and Mitigations (Apr 2025) - https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- STRIDE-AI (Mauri & Damiani, IEEE 2021) - https://ieeexplore.ieee.org/document/9527917
- Five Eyes - Careful Adoption of Agentic AI Services (May 2026) - https://www.cisa.gov/resources-tools/resources/careful-adoption-agentic-ai-services

### Gamma brief

```
Title: Process - the human-judgment restorations
Lead-in (italic, top): Tooling enforces policy. It does not write policy. Six rules you cannot skip.

Six policy bullets:
  1. Acceptable Use Policy for AI coding tools
       Caption: 84% of devs use AI; only 28% of orgs have a formal policy (Stack Overflow 2025) - ISO 42001 A.3.2; ETSI 104 223 P1
  2. Data classification policy for prompts and context
       Caption: tiered (public / internal / sensitive / prohibited) mapped to model class - the policy AI-aware DLP enforces - ISO 27001 A.5.12 / A.5.13 / A.8.12; ICO AI guidance
  3. DPIA and privacy assessment policy
       Caption: UK GDPR Article 35 - ICO says AI processing usually triggers DPIA; silence is not a policy - ICO Risk Toolkit; ISO 42001 A.6.1.4
  4. Threat-modelling discipline
       Caption: MITRE ATLAS v5.1, OWASP Multi-Agentic TM Guide, STRIDE-AI - prompt injection -> Tampering, excessive agency -> EoP, tool poisoning -> Spoofing
  5. Tool, model, and MCP intake
       Caption: contract terms (no-train, ZDR, residency, sub-processors, breach notification, model-change notice), red-team, threat model, refresh - ISO 42001 A.10.3
  6. AI-specific incident-response policy
       Caption: pre-decided scenarios - AI-introduced CVE, tool compromise, model-key rotation, poisoned MCP, vendor breach pivot - Five Eyes May 2026; ISO 27001 A.5.24-A.5.28

Closing line: Process decides; tooling enforces.
Visual: Six labelled blocks across the top - AUP / Data classification / DPIA / Threat model / Intake / IR - with arrows fanning down to "Slide 12 enforces" and "Slide 14 lives" on either side.
Tone: Policy-level, CISO-grade. The standing decisions humans still have to make.
```

---

## Slide 14 - Culture and Organisation - not the department of no

**Hero line (large, top of slide):** *The org that says yes to a sanctioned tool fast beats the one that says no slowly.*

*Lead-in (italic, beneath the hero):* **Slide 13 sets the policy. Here is how the team operationalises it - and how it closes the shadow-AI loop from Slide 9.**

**Sanctioned-tooling pathway (Slide 13's intake policy in operation):**
- Sanctioned tooling pathway with **weekly intake cadence** - 49% of orgs run 5+ AI tools (GitLab DevSecOps 2025); quarterly cannot keep up
- **Default-allow with guardrails**, not default-block
- **Visible "tools approved this week" feed** for engineering - the marketing of yes
- **Tools that fail intake** get a clear "here is what would need to change" - not a cold rejection (turns the gate into a roadmap)

**Culture rules (supporting):**
- No merge until reviewed by someone who did not write the prompt
- Pair-review for AI-generated code - one used AI, one did not
- Ownership is human, regardless of what wrote it
- Reward catches, not velocity

**Organisation (supporting):**
- Joint AppSec + engineering owner of the AI-tooling programme - **not product**
- Seniors review more, write less - review capacity is the new bottleneck
- **Hire and grade for the review reflex - and the skill atrophy behind it is real.** Technical skills decay within ~2.5 years without active use; 87% of devs are concerned about the security of AI coding tools (Snyk). Entry-level devs may never build the secure-coding fundamentals senior reviewers rely on.

*"Rethinking Code Review Workflows with LLM Assistance" (arXiv 2505.16339, May 2025): reviewer familiarity and PR severity moderate where AI-led review helps - human-in-the-loop is the load-bearing variable*

**Graphic:** Hero line dominates the top third. Sanctioned-tooling beat as a horizontal three-card row beneath. Two-column culture / organisation grid in the lower half. Subtle "two developers reviewing together" line illustration as a divider.

**Speaker notes:** This slide hangs off the agility hero - "the org that says yes to a sanctioned tool fast beats the one that says no slowly." Everything else on the slide is how you operationalise that.

Open by closing the shadow-AI loop from Slide 9. The CISO's instinct on shadow AI is to ban what they find. That instinct fails because developers will use whatever makes them effective; the alternative they choose if you say no is unsanctioned and uninstrumented. So the security team's primary cultural posture has to shift. You are not the department of no - you are the department of *yes, fast, with guardrails*.

That posture has three structural commitments. First, a sanctioned tooling pathway with a weekly intake cadence. GitLab's DevSecOps 2025 survey found 49 percent of organisations run five or more AI tools. The tooling landscape changes faster than that. Quarterly governance bodies cannot keep up. Weekly might still be too slow but it's the floor.

Second, default-allow with guardrails, not default-block. The shadow-AI bind exists because the easy path inside the company is "no" and the easy path around the company is "yes." Flip that. Tools that pass intake review are immediately available to engineering. Tools that fail get a clear "here is what you'd need to fix to make this work" response, not a cold rejection.

Third, market the yes. A visible "tools approved this week" feed for engineering does more for shadow-AI reduction than any DLP rule, because it removes the *reason* shadow AI is the easy path.

The culture-rules half supports the response. No merge until reviewed by someone who did not write the prompt - if the developer who wrote the prompt is also the only person who reads the PR, the review collapses into self-review. Pair-review for AI-generated code goes one step further - one developer who used AI plus one who did not, because the non-AI reviewer brings the unmodified instinct of "wait, why is this here?" Ownership is human - the name on the merge owns the artefact. Reward catches not velocity - your performance metrics, your team-level dashboards, your engineering-leadership reviews, if they reward merge rate without rewarding catch rate, you're training the wrong reflex.

The org-moves half is the structural change most engineering orgs haven't internalised. AI compresses authorship time. It does not compress review time - in fact it expands it (DORA's +441%). So your senior engineers, who used to spend most of their time writing, now need to spend most of their time reviewing. Seniors review more, write less. Junior and mid-level engineers do more authorship - with AI assistance - and seniors apply the residual judgment AI cannot do.

Hire for the review reflex. The skill atrophy data is the trend behind that prescription. Technical skills decay within 2.5 years without active use; 87 percent of developers (Snyk) report concern about the security of AI coding tools - they know what's happening. Entry-level developers using AI from day one may never build the secure-coding fundamentals senior reviewers rely on. Every CISO needs to look at their hiring pipeline and ask whether the next generation of seniors will have the substrate to do the residual-judgment work AI cannot do. If they don't, you have a five-year problem you need to start solving now.

The 2025 academic anchor for the whole slide is "Rethinking Code Review Workflows with LLM Assistance" (arXiv 2505.16339, May 2025). They show that AI-led code review is preferred *only* conditional on reviewer familiarity with the codebase and PR severity. The variable that determines whether AI review helps or hurts is the human in the loop - their context, their capacity, and the organisational discipline around when AI-led review gets the final say versus a senior signing the merge. Culture determines how much human review happens; organisational structure determines whether the team has capacity for it.

Review capacity is the new bottleneck. Saying yes fast is the new perimeter.

**Sources:**
- "Rethinking Code Review Workflows with LLM Assistance" (arXiv 2505.16339, May 2025) - https://arxiv.org/abs/2505.16339
- GitLab DevSecOps 2025 - https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/
- ISO/IEC 42001:2023 - https://www.iso.org/standard/42001
- The risks of entry-level developers over-relying on AI - CSO Online - https://www.csoonline.com/article/3951403/the-risks-of-entry-level-developers-over-relying-on-ai.html
- Skill atrophy / AI dependency - RSAC blog - https://www.rsaconference.com/library/blog/the-dark-side-of-ai-dependency-risks-in-software-development
- Snyk RSAC 2026 (87% dev concern; per-developer vuln rate up 2-10x YoY) - https://expertinsights.com/industry-perspectives/rsac-2026-manoj-nair-snyk

### Gamma brief

```
Title: Culture and Organisation - not the department of no
Subtitle: Closing the shadow-AI loop

Hero line (large, top):
  The org that says yes to a sanctioned tool fast beats the one that says no slowly.

Lead-in (italic, beneath hero):
  Slide 13 sets the policy. Here is how the team operationalises it - and closes the shadow-AI loop from Slide 9.

Sanctioned-tooling beat (four rows under the hero):
  - Weekly intake cadence (49% of orgs run 5+ AI tools - GitLab DevSecOps 2025)
  - Default-allow with guardrails, not default-block
  - Visible "tools approved this week" feed for engineering
  - Tools that fail intake get "here is what would need to change" - not cold rejection

Two columns beneath:
  Culture rules:
    No merge until reviewed by someone who didn't write the prompt
    Pair-review: one used AI, one didn't
    Ownership is human
    Reward catches, not velocity
  Organisation:
    Joint AppSec + engineering owner of the AI-tooling programme (not product)
    Seniors review more, write less
    Hire for the review reflex - skill decay 2.5 years; 87% of devs concerned about AI-tool security (Snyk)

Footer (italic): "Rethinking Code Review Workflows with LLM Assistance" (May 2025) - reviewer familiarity and PR severity moderate where AI-led review helps; the human-in-the-loop is the load-bearing variable
Closing line: Review capacity is the new bottleneck. Saying yes fast is the new perimeter.

Visual: Hero line dominates the top third. Sanctioned-tooling beat as a horizontal four-card row beneath. Two-column culture / organisation grid in the lower half. Restrained, no clip art.
Tone: The slide hangs off the agility hero, not on culture rules. Culture and org are how you operationalise saying yes fast.
```

---

## Slide 15 - Governance - anchor, owner, measure

**Hero (large, top of slide):** *Anchor. Owner. Measure.*

- **Anchor.** Pick a framework so the auditor has something to map to. **ISO/IEC 42001** if you want certifiable; the **UK AI Cyber Security Code of Practice / ETSI TS 104 223** if you want UK-government-aligned. The fit is by analogy - no standard is purpose-built for AI-assisted SDLC yet, and that is fine. Pick one and align to it.
- **Owner.** Name a single accountable owner. Joint AppSec + engineering, accountable to the board, reviewed quarterly. Not product. Not procurement. Not the CISO in name only. Without a named owner, governance is fiction.
- **Measure.** Four metrics, all derivable from the commit-trailer schema on Slide 12 Gate 3:
  - **AI-assisted PR rate** - is adoption growing, and where?
  - **Vulnerability rate: AI-touched vs human-touched code** - are the gates closing the gap?
  - **Secret exposures from AI-assisted commits** - are prompt and DLP controls working?
  - **MTTR for AI-introduced vulns** - is IR keeping up?

*Closing line (italic, bottom):* **Standards lag the practice. Measure first; let the framework alignment catch up.**

**Graphic:** Three large words across the top - **ANCHOR / OWNER / MEASURE**. Three short supporting bullets beneath, then the four metrics in a clean column or row. Quiet honest-beat closing line at the bottom. No framework-stack diagram, no clause numbers - the standards live in speaker notes.

**Speaker notes:** This is the slide that gets reported to the board. Three words to walk away with: anchor, owner, measure.

Anchor. Pick a framework so when your auditor asks what you are aligned to, you have an answer. The two strongest for a UK audience are ISO/IEC 42001 - the certifiable AI management-system standard, ISMS-shaped so it folds into your existing 27001 work - and the UK AI Cyber Security Code of Practice, published by DSIT on 31 January 2025 and adopted internationally as ETSI TS 104 223 in April 2025. Either one will hold up in a board room. The honest framing: no standard is purpose-built for using AI in your SDLC yet, so both apply by analogy. Pick one, document the analogy, and move on.

Owner. The decisions on Slide 13 - AUP, data classification, DPIA, threat modelling, intake, IR - all need a named human accountable. The strongest pattern is a joint AppSec-plus-engineering owner of the AI-tooling programme, accountable to the board, reviewed quarterly. Not product, because product owns features. Not procurement, because procurement signs contracts but does not run the programme. Not the CISO in name only, because that diffuses accountability. One name, one programme.

Measure. Four metrics, all derivable from the commit-trailer schema on Slide 12 Gate 3. **AI-assisted PR rate** tells you whether adoption is growing and which teams are leading. **Vulnerability rate AI-touched versus human-touched** tells you whether the gates are closing the gap. **Secret exposures from AI-assisted commits** tells you whether the prompt-engineering and DLP controls are actually working. **MTTR for AI-introduced vulnerabilities** tells you whether IR is keeping up. Without these four numbers reported monthly, you do not have a programme - you have a hope.

The closing line is the honest beat. Standards lag the practice. The frameworks were not written for vibe coding; they were written for AI systems being built and operated. They will catch up. Measure first; document the analogy to your chosen anchor; let alignment catch up.

If anyone in Q&A asks for the specific clause references: ISO/IEC 42001 Annex A.9 (Use of AI systems) and A.10 (Third-party and customer relationships) are the two that map most directly. The UK Code's load-bearing principles for SDLC use are P5 (identify, track and protect assets), P7 (secure your supply chain), P8 (document data, models and prompts), and P9 (testing and evaluation). The NIST SSDF GenAI Profile, NIST AI 600-1, NCSC+CISA Guidelines, and OWASP LLM Top 10 all apply to AI features you *build into products* - that is Part 2 of this series.

**Sources:**
- ISO/IEC 42001:2023 - https://www.iso.org/standard/42001
- UK AI Cyber Security Code of Practice (DSIT, 31 Jan 2025) - https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice/code-of-practice-for-the-cyber-security-of-ai
- ETSI TS 104 223 V1.1.1 (Apr 2025) - https://www.etsi.org/deliver/etsi_TS/104200_104299/104223/01.01.01_60/ts_104223v010101p.pdf
- *Cross-reference (Part 2 stack):* NIST SP 800-218A, NIST AI 600-1, NCSC + CISA Guidelines for Secure AI System Development, OWASP Top 10 for LLM Applications

### Gamma brief

```
Title: Governance - anchor, owner, measure

Hero (large, top): Anchor. Owner. Measure.

Three bullets (each starting with the verb):
  Anchor - Pick a framework: ISO/IEC 42001 (certifiable AIMS) or UK AI Cyber Security Code of Practice / ETSI TS 104 223. Fit by analogy; no standard is purpose-built for AI-assisted SDLC yet.
  Owner - Name a single accountable owner. Joint AppSec + engineering, board-accountable, quarterly reviewed. Not product. Not procurement. Not the CISO in name only.
  Measure - Four metrics, all from the Slide 12 Gate 3 commit-trailer schema:
    - AI-assisted PR rate
    - Vulnerability rate: AI-touched vs human-touched
    - Secret exposures from AI-assisted commits
    - MTTR for AI-introduced vulns

Closing line (italic, bottom): Standards lag the practice. Measure first; let the framework alignment catch up.

Visual: Three large words across the top - ANCHOR / OWNER / MEASURE. Three short supporting bullets beneath, then the four metrics in a clean column or row. Quiet honest-beat closing line at the bottom. No framework-stack diagram, no clause numbers.
Tone: Memorable, actionable. The "what gets reported to the board" slide.
```

---

# Close

## Slide 16 - On the other hand - maybe this is transitional

*Setup line (top of slide, italic):* **"Maybe AI gets so good these concerns evaporate. Worth taking that seriously."**

- **Aviation analogy.** ~70% of commercial flight time is on autopilot. Senior pilots will tell you they trust the autopilot more than they trust most humans. The "pilot is god" model died in the 1970s.
- **Frontier-lab evidence.** Boris Cherny (Claude Code) ships 22 PRs/day with Claude writing 100%. Roon at OpenAI: "I don't write code anymore." Real people, real work, end-to-end.
- **Generational trajectory.** GPT-3.5 -> 4 -> 5 showed huge reasoning gains. Veracode's 45% vulnerability rate today might be 20% next year. The flat line could finally break.
- **Defensive tooling improves alongside.** AI-aware SAST, 2026 prompt-injection defences (PromptArmor >99% prevention; PromptGuard 67% reduction), AI-BOM specs maturing. Models are getting better; the perimeter around them is too.
- **Historical analogy.** We used to read assembly to verify compilers. We used to manage memory by hand. Each abstraction layer was scary at the time and we adapted. Maybe AI-as-author is just the next layer.

*Closing line (italic, set off at bottom):* **"Maybe. But you have to defend now, not in five years."**

**Graphic:** Five clean bullet rows, equal spacing, no charts. Subtle aviation imagery (cockpit silhouette or autopilot indicator) as a quiet side panel or background motif.

**Speaker notes:** End on the most generous version of the counter-argument. There is no rebuttal on the slide because the rebuttal is the previous fifteen slides. The audience just sat through the data; they will do the work themselves.

Walk the steel-man slowly. Modern airliners fly under heavy autopilot, and senior pilots will tell you they trust the autopilot more than they trust most humans. The "pilot is god" model died in the 1970s. Boris Cherny, who created Claude Code, runs hundreds of agents full-time with no human in the loop. Roon at OpenAI says he doesn't write code anymore. The frontier labs have arrived at the destination.

The trajectory is real. GPT-3.5 to GPT-4 to GPT-5 showed enormous reasoning gains. The Veracode 45% vulnerability rate could break the flat line. The defensive perimeter is improving in parallel - 2026 prompt-injection defences are real (PromptArmor cleared 99% prevention on AgentDojo, PromptGuard 67% reduction), AI-BOM specs are maturing, AI-aware SAST is shipping. We have been here before with compilers, with garbage collection, with high-level languages. Each abstraction was scary when we adopted it and we adapted.

Pause briefly on the closing line. *"Maybe. But you have to defend now, not in five years."* That is the only thing the slide says explicitly that pushes back. Everything else in the deck has done the rebuttal already.

If you want to add a verbal beat at the close - and this is optional - the cleanest counter is the system frame. *"Aviation didn't get safe by trusting one agent. Autopilots fly safely inside a system - checklists, redundancy, air-traffic control, regulatory certification, mandatory incident reporting. The system doesn't trust any single agent, including the human pilot. The four responses on the previous slides are software's equivalent of that system. They will outlast whatever the model does next."* But that is speaker-only - keep the slide steel-man-only.

**Sources:**
- Cherny on personal workflow / frontier-lab figures - https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
- Prompt Injection Defense 2026 (TokenMix) - https://tokenmix.ai/blog/prompt-injection-defense-techniques-2026
- Veracode Spring 2026 (referenced) - https://www.veracode.com/blog/spring-2026-genai-code-security/

### Gamma brief

```
Title: On the other hand
Subtitle: Maybe this is transitional

Setup line (top, italic): Maybe AI gets so good these concerns evaporate. Worth taking that seriously.

Five bullets (one line each):
- Aviation: ~70% of flight time is on autopilot; senior pilots trust it more than humans
- Boris Cherny ships 22 PRs/day, Claude writing 100%; Roon at OpenAI: "I don't write code anymore"
- GPT-3 -> 4 -> 5: the flat line could break
- Defensive tooling improves alongside (2026 IDE-boundary defences PromptArmor >99% prevention, PromptGuard 67% reduction; AI-aware SAST shipping)
- We adapted to compilers, GC, high-level languages - maybe AI-as-author is just the next layer

Closing line (italic): Maybe. But you have to defend now, not in five years.

Visual: Five clean bullet rows. Subtle aviation imagery as a quiet background motif.
Tone: Even-handed. The deck is the rebuttal.
```

---

## Slide 17 - Q&A and Part 2 preview

- Questions
- Bibliography lands in your inbox
- Part 2: *Running AI in Production* - what you are actually defending now

**Speaker notes:** Once it ships, it is someone else's attack surface. That is Part 2. Take questions.

### Gamma brief

```
Title: Q&A | Part 2 preview
Layout: Two-column
Left column - Questions:
- Bibliography lands in your inbox after the session
- Q&A
Right column - Coming up:
- Series: The New Normal: Software, Security and the AI Stack
- Part 2: Running AI in Production - what you are actually defending now
- [date placeholder]
Visual: Series wordmark across the top. Two columns underneath. Restrained, signposting design - this is a wrap, not a content slide.
Tone: Open, inviting. End on the next thing, not on the last thing.
```
