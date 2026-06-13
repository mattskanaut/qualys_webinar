# Slide Briefs v8 - punchier briefs, primer cut, problem-first

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Slide count:** 17

> Companion to `slide-plan-v8.md` - same 17 slides, leaner Gamma briefs. Detail, captions, and supporting prose live in slide-plan-v8.md speaker notes; this file is what to paste into gamma.app.

---

## Slide 1 - Title and the promise

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

## Slide 4 - The productivity paradox

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

## Slide 5 - Quality on security is materially worse

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

Visual: Banner thesis dominates the top third. Three argument bands beneath. CVE tile grid sits inside band three as evidence, not as the slide. Quiet supply-chain footer band beneath.
Tone: Sharp. The audience expects "tools have CVEs"; the slide tells them why this is not that.
```

---

## Slide 9 - Shadow AI - your developers will route around you

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

## Slide 10 - Secure SDLC is a profession

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

## Slide 12 - Tooling - what a confidently AI-enabled SDLC looks like

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

## Slide 16 - On the other hand - maybe this is transitional

```
Title: On the other hand
Subtitle: Maybe this is transitional

Setup line (top, italic): Maybe AI gets so good these concerns evaporate. Worth taking that seriously.

Five bullets (one line each):
- Aviation: ~70% of flight time is on autopilot; senior pilots trust it more than humans
- Boris Cherny ships 22 PRs/day, Claude writing 100%; Roon at OpenAI: "I don't write code anymore"
- GPT-3 -> 4 -> 5: the flat line could break
- Defensive tooling improves alongside (2026 IDE-boundary defences: PromptArmor >99% prevention, PromptGuard 67% reduction; AI-aware SAST shipping)
- We adapted to compilers, GC, high-level languages - maybe AI-as-author is just the next layer

Closing line (italic): Maybe. But you have to defend now, not in five years.

Visual: Five clean bullet rows. Subtle aviation imagery as a quiet background motif.
Tone: Even-handed. The deck is the rebuttal.
```

---

## Slide 17 - Q&A and Part 2 preview

```
Title: Q&A | Part 2 preview
Two columns:
  Questions: bibliography by email | Q&A
  Coming up: Part 2 - Running AI in Production - what you are actually defending now
Visual: Series wordmark. Two columns.
Tone: Open. End on the next thing.
```
