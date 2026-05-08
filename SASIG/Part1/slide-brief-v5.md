# Slide Briefs v5 - all Gamma briefs in one place

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Slide count:** 21

> Each block below is a Gamma brief for a single slide, in running order. Paste the fenced code block into gamma.app to generate the slide. Full bullets, speaker notes and sources live in `slide-plan-v5.md` - they are for the speaker, not the tool.

---

## Slide 1 (P1.1) - Secure SDLC is a defined discipline, not a buzzword

```
Title: Secure SDLC is a defined discipline
Subtitle: Three decades, four frameworks, now a regulatory floor
Layout: 4-card grid above a footer band
Cards:
- Microsoft SDL (2004) - 5 phases, 10 practices; the grandfather
- NIST SSDF v1.1 (2022) - PO/PS/PW/RV; US federal baseline
- OWASP SAMM v2 - 5 business functions, 15 practices; open-source
- BSIMM 15 (2024) - measured practice across 121 firms
Footer band: EU CRA (Dec 2024) | UK PSTI (Apr 2024) | EU AI Act (Aug 2024)
Visual: Clean 4-card grid with year badges. Muted accent colour for the regulation footer band. No vendor logos.
Tone: Sober, authoritative, non-product. Establishes credibility.
```

---

## Slide 2 (P1.2) - Secure SDLC is a profession

```
Title: Secure SDLC is a profession
Banner quote: "Secure-SDLC frameworks codify a profession. Like every profession, they rest on assumptions about how trusted humans behave."
Layout: Two-panel comparison
Left panel - "Buildings":
- Designer
- Builder
- Label underneath: "professional practice"
Right panel - "Software":
- Developer
- Reviewer
- Maintainer
- Operator
- Label underneath: "professional practice"
Common base under both panels: "frameworks - standards - regulation"
Closing line: "Buildings don't fall down only because of monitoring. They don't fall down because designers and builders behaved professionally."
Visual: Architectural line-art for the building panel; minimal code-repo schematic for the software panel. Restrained, monochrome with one accent colour.
Tone: Reflective, sets up the four assumptions. Not technical.
```

---

## Slide 3 (P1.3) - The four assumptions every secure SDLC rests on

```
Title: The four assumptions every secure SDLC rests on
Layout: 2x2 quadrant card. Each cell has a single bold icon, the assumption sentence, and framework citations in smaller type.
Quadrant 1 - W: The developer wrote it
  Codified in: SSDF PW.5 | SDL secure coding | SAMM Secure Build
Quadrant 2 - R: The reviewer read it
  Codified in: SSDF PW.2.1, PW.7 | SDL Verification | SAMM Architecture Assessment
Quadrant 3 - D: The dependencies were vetted
  Codified in: SSDF PS.3.2, PW.4.4 | SLSA v1.2 | SAMM Software Dependencies
Quadrant 4 - T: The tools were deterministic
  Codified in: SSDF PO.3, PO.5 | SDL secure engineering environment
Footer (italic, full width): "With AI in the loop, what does the developer actually know about what was just written? How secure are we?"
Visual: Four large quadrant cells, each dominated by a bold W/R/D/T glyph. This is the icon legend that recurs through the rest of the deck - keep the icon design distinctive and consistent.
Tone: Definitive. The talk's spine.
```

---

## Slide 4 (P1.4) - Where CI/CD fits - SDLC defines, pipelines enforce

```
Title: Where CI/CD fits - SDLC defines, pipelines enforce
Layout: Two horizontal tiers, top stacked above bottom, with a labelled divider line between them
Top tier - "SDLC practices: the human-judgment layer"
  Contains: W, R, D icons
  Caption: NIST SP 800-204D Appendix B - PW.1-PW.4 and PW.7 "pertain to secure software design, review of the design, and software reuse"
Bottom tier - "CI/CD pipeline (build - test - package - deploy)"
  Contains: T icon
  Badge: SLSA v1.2 (L0-L3) on the build-platform box
Side caption: "Three of four assumptions live above the pipeline. Only T rides on it."
Visual: Two horizontal bands stacked. The dividing line carries the NIST citation in italics. Icons for W/R/D in the top band, T alone in the bottom. SLSA badge as a small overlay.
Tone: Definitive. Closes Section 1 and sets up Section 2.
```

---

## Slide 5 (P2.1) - From tool to author

```
Title: From tool to author
Subtitle: "Vibe coding" - Collins Dictionary Word of the Year 2025

Layout: One hero stat, supporting trajectory beneath it, pull quote and footer captions below. No charts. No clip art.

Hero stat (dominant visual, center, very large):
  Number: 75%
  Caption directly under the number: of new code at Google is now AI-generated and engineer-approved
  Source line, smaller: Sundar Pichai, Alphabet Q1 2026 earnings call

Trajectory row (three small data points, side by side, below the hero):
  Heading: The climb
  Point 1: 2024 - 25%
  Point 2: Fall 2025 - 50%
  Point 3: Q1 2026 - 75%
  Sub-caption: 25 -> 50 -> 75 in two years

Pull quote (below the trajectory row, italics):
  "fully give in to the vibes... forget that the code even exists"
  Attribution: Andrej Karpathy, Feb 2025 - the tweet that coined "vibe coding"

Footer captions (small type, two short lines at the bottom):
  Line 1: Frontier labs sit higher - Anthropic 70-90% company-wide; senior engineers report ~100% personal workflows (Fortune, Jan 2026)
  Line 2: Historical floor - Microsoft repos at 20-30% AI-written (Nadella, Apr 2025)

Closing line (bottom, set off):
  The slope is the story.

Style: The 75% must be the dominant element on the slide - bigger than anything else by a wide margin. Everything else is supporting context. Sober, factual layout. No icons, no clip art, no decorative graphics, no charts.
Tone: Crisp, factual, no hype. Cultural framing in the subtitle, audited number as the hero.
```

---

## Slide 6 (P2.2) - Four moving parts that didn't exist 18 months ago

```
Title: What's actually in your build pipeline now
Subtitle: One-slide AI primer
Layout: Four labelled boxes connected with arrows, left to right
Box 1: LLM
  Caption: stateless next-token predictor (the brain)
Box 2: Harness
  Caption: wrapper that turns prediction into action
  Examples: Cursor, Copilot, Claude Code, Cline
Box 3: MCP server
  Caption: how harnesses talk to your systems
  Examples: GitHub, Slack, Postgres, JIRA
Box 4: RAG
  Caption: how AI features pull in your private data
Footer: "Today: build-time AI. Runtime AI is Part 2 of the series."
Visual: Architecture diagram. Boxes flow left-to-right with arrows showing data flow. A subtle dotted boundary line shows "what the developer sees" (LLM + Harness) vs "what gets executed against your systems" (MCP + RAG).
Tone: Educational, fast. Skim-readable.
```

---

## Slide 7 (P2.3) - Adoption is near-universal in the enterprise

```
Title: Adoption is near-universal in the enterprise
Subtitle: Three independent 2025-2026 sources converge
Layout: Three-column number card with logos
Stat 1: 4.7M
  Caption: paid Copilot subscribers (Microsoft FY26 Q2, Jan 28 2026)
  Sub-caption: +75% YoY; ~90% of Fortune 100
Stat 2: 90%
  Caption: of devs use AI at work (DORA 2025, n~5,000)
  Sub-caption: 65% rely on it heavily
Stat 3: 90%+
  Caption: of software teams use AI (McKinsey Feb 2026, 4,500 devs / 150 enterprises)
  Sub-caption: ~6 hrs/week saved per developer
Footer caption: Microsoft (Nadella, Apr 2025) - 20-30% of code in Microsoft repos is now AI-written
Closing line: Take "AI is in your stack" as established.
Visual: Three big-number cards in a row with vendor logos. Source attribution in small type underneath each.
Tone: Crisp, factual, no hype.
```

---

## Slide 8 (P2.4) - The productivity paradox

```
Title: The productivity paradox
Subtitle: Productivity gains are real - the bottleneck has just moved
Layout: Two-panel chart side by side
Left panel - Productivity:
  - Cui et al. RCT (n=4,867): +26% PRs/week with Copilot
  - METR Feb 2026 walkback: original -19% slowdown moderates to -4% (CI -15% to +9%)
  - Note: METR explicitly does NOT retract the security/quality concerns
Right panel - Review cost:
  - DORA 2025: PR review time +441%
  - PR size +51.3%
  - 30% of devs distrust AI code (but still merge it)
Closing line: The reviewer is now the load-bearing role.
Visual: Two-panel chart - left: Cui +26% / METR -4% (with original -19% greyed out); right: DORA PR-size and review-time deltas drawn to scale.
Tone: Data-driven. The trade-off is the story.
```

---

## Slide 9 (P2.5) - Quality on security is materially worse - and not improving

```
Title: Quality on security is materially worse - and not improving
Subtitle: Four years, no movement on the failure rate
Layout: Three-bar comparison + supporting bullet
Bars (year on x-axis, % vulnerable on y-axis):
  - Pearce et al. IEEE S&P 2022: 40% baseline
  - Veracode Spring 2026 (100+ LLMs): 45% still vulnerable; Java 72%
  - "Broken by Default" (arXiv:2604.05292, Apr 2026): 55.8% formally Z3-proven vulnerable
Supporting bullet:
  - 6 commercial SAST tools combined miss 97.8% of these flaws
Closing line: This is a build-pipeline gap, not a runtime adversarial-testing gap.
Visual: Three-bar comparison (2022 / 2025 / Spring 2026) showing flat trajectory. Supporting bullet underneath.
Tone: Sobering, evidence-led. The flat line is the headline.
```

---

## Slide 10 (P2.6) - Insecure-by-default at scale

```
Title: Insecure-by-default at scale
Icon highlighted (bottom-right): W
Layout: Hockey-stick chart + supporting bullets
Headline stat: 10x new findings/month from AI-generated code
  Source: Apiiro Fortune-50 telemetry, mid-2025 (7,000+ devs, 62,000 repos)
Supporting bullets:
- +322% privilege escalation paths
- +153% architectural flaws
- +40% secret exposures
- Trivial errors fell; deep flaws exploded
Closing line: "Shallow up, deep down."
Visual: Apiiro hockey-stick of monthly findings (Dec 2024 - mid 2025). Bullets to the right.
Tone: Evidence-driven. Let the slope speak.
```

---

## Slide 11 (P2.7) - Hallucinated dependencies and slopsquatting

```
Title: Hallucinated dependencies and slopsquatting
Icon highlighted (bottom-right): D
Layout: Per-model hallucination chart + attack-flow diagram
Headline stat: 43% of LLM-hallucinated package names recur across 10 prompt repeats
  Source: Spracklen et al., USENIX Security 2025 (576,000 samples, 16 LLMs)
Supporting bullets:
- Commercial LLMs >=5.2% hallucination rate; open-source >=21.7%
- 205,474 unique fabricated package names catalogued
- Lasso registered hallucinated `huggingface-cli` -> 30,000+ downloads in 3 months
- Hallucinated names landed in vendor docs (Alibaba GraphTranslator README)
Closing line: Perfect repeatability for an attacker. CI allowlist is the highest-leverage control.
Visual: Per-model hallucination-rate bar chart on the left. Three-step attack-flow on the right (LLM hallucinates -> attacker registers on PyPI -> developer's AI-suggested import installs malware). Red arrows for the attack path.
Tone: Concrete, actionable.
```

---

## Slide 12 (P2.8) - Secrets exposure and overly broad permissions

```
Title: Secrets exposure and overly broad permissions
Icons highlighted (bottom-right): W, R
Layout: Bar chart + supporting bullets
Headline stat: 41% of AI-generated backend code ships with default-admin permissions when prompted naively
  Source: Backslash 2025
Supporting bullets:
- AI-assisted projects: ~2x rate of cloud-credential exposure vs non-AI baselines (GitGuardian / Snyk via Apiiro)
- GPT-4.1 with naive prompts: 1.5/10 secure-code score
- Claude 3.7: 6/10 -> 10/10 with security-focused prompts
Closing line: The prompt is the control plane now.
Visual: Secure-code-score bar chart - naive prompt vs security-focused prompt. Show the 6/10 -> 10/10 swing prominently.
Tone: Concrete, leverage-led.
```

---

## Slide 13 (P2.9) - Developer confidence is anti-correlated with secure outcomes

```
Title: Developer confidence is anti-correlated with secure outcomes
Icon highlighted (bottom-right): W
Layout: Two-line chart + supporting bullets
Chart (2023 to 2026):
  - Line 1: AI usage rising (84% by Feb 2026)
  - Line 2: Developer trust falling (29% by Feb 2026, -11pts YoY)
Supporting bullets:
- Perry et al. ACM CCS 2023: AI-assisted devs wrote less secure code on 4 of 5 tasks - and were more likely to believe it was secure
- Snyk RSAC 2026: 48% of AI-generated code contains vulnerabilities; per-developer vuln rate up 2-10x YoY
- Stack Overflow Feb 2026: 81% concerned about AI code security
Closing line: Devs already know the tool is unreliable. The job is scaffolding, not convincing.
Visual: Two-line chart showing diverging usage and trust lines, 2023 to 2026.
Tone: Evidence-led, slightly counter-intuitive. The confidence gap is the story.
```

---

## Slide 14 (P2.10) - The toolchain is itself an AI attack surface

```
Title: The toolchain is itself an AI attack surface
Icon highlighted (bottom-right): T
Layout: Pipeline-attack-flow + CVE tile grid
Lead incident:
  - LiteLLM (Mar 24, 2026): backdoored 1.82.7 / 1.82.8 via Trivy in CI
  - 3.4M daily downloads; 40,000+ in the exposure window
CVE tile grid (2026):
  - Cursor RCE - CVE-2026-26268
  - Copilot Reprompt - CVE-2026-21516
  - Claude Code CLI RCE - CVE-2026-35021
  - Windsurf MCP zero-interaction - CVE-2026-30615
Supporting bullet:
  - MCP servers: developer-side shadow IT; ~2,000 production servers scanned, none authenticated (Prakash AIP 2026)
Closing line: The pipeline runs AI tools that run AI tools. Pinning is policy.
Visual: Pipeline-attack-flow on the left (LiteLLM as the canonical example). Small CVE tile grid on the right with date stamps and one-line consequences.
Tone: Specifics. Names, dates, CVEs.
```

---

## Slide 15 (P3.1) - Tooling - PR gates, AI-asset inventory, IDE boundary

```
Title: Tooling - PR gates, AI-asset inventory, IDE boundary
Icon highlighted (bottom-right): T
Layout: Pipeline diagram with four labelled gates
Gate 1: AI-asset & MCP-server inventory
  Caption: the new shadow IT
Gate 2: IDE boundary
  Caption: Hines et al. Spotlighting reduces prompt-injection ASR from >50% to <2%
Gate 3: PR gate (fail-closed)
  Caption: SAST + secrets + SCA on AI-assisted PRs; block hallucinated imports
Gate 4: Build gate
  Caption: pin AI tool versions; treat MCP servers as third-party deps
Closing line: "Pipelines reinforce T. Inventory first, then gates."
Visual: Linear horizontal pipeline diagram. Each gate is a vertical bar across the pipeline, annotated with the control it enforces. Use the same accent colour throughout to signal "pipeline-enforceable."
Tone: Operational, prescriptive. The "what to actually configure" slide.
```

---

## Slide 16 (P3.2) - Process - the human-judgment restorations

```
Title: Process - the human-judgment restorations
Icons highlighted (bottom-right): W, R, D
Layout: PR template mockup + side panel of process changes
PR mockup highlights:
- Field: AI-assisted? (yes / no / which tool)
- Field: AI-BOM attached? (model, tools, prompts, packages)
Side panel - process changes:
- Mandatory AI-usage disclosure at PR level (cheapest, highest-leverage control)
- AI-BOM at PR level - extends SBOM to model and tool provenance
- Third-party AI-tool intake review (the Context AI question)
- AI-specific branch in IR playbook
Closing line: "Disclosure first. Provenance second."
Visual: Realistic mockup of a PR description in GitHub or GitLab style, with the two new fields highlighted. Process changes as a side panel.
Tone: Practical, specific. These are concrete process changes to implement Monday-after-next.
```

---

## Slide 17 (P3.3) - Culture

```
Title: Culture
Icon highlighted (bottom-right): R
Layout: Four rule-cards stacked + research footer
Rule 1: No merge until reviewed by someone who did not write the prompt
Rule 2: Pair-review for AI-generated code - one used AI, one did not
Rule 3: Ownership is human, regardless of what wrote it
Rule 4: Reward catches, not velocity
Footer (italic): Sandoval et al. (USENIX Security 2023, "Lost at C") - review interaction is the primary moderator of LLM-assisted bug rate
Visual: Four rule-cards stacked vertically. Subtle "two developers reviewing together" line illustration on the right.
Tone: Cultural, value-led. The "what kind of team are we" slide.
```

---

## Slide 18 (P3.4) - Organisation

```
Title: Organisation
Icon highlighted (bottom-right): R
Layout: Org-chart fragment on the left + four bullets on the right
Org-chart fragment:
- Highlight a joint "AppSec + Engineering" owner
- Weekly governance body
Bullets:
- Name an owner: AppSec + engineering lead - not product
- Joint governance body, weekly cadence (49% of orgs run 5+ AI tools)
- Redistribute the review workload - seniors review more, write less
- Hire and grade for the review reflex, not the typing reflex
Closing line: "Review capacity is now the engineering org's bottleneck."
Visual: Simplified org-chart fragment with the joint AppSec+engineering owner highlighted. Bullets to the right.
Tone: Structural, decisive. Engineering-org change, not GRC change.
```

---

## Slide 19 (P3.5) - Governance

```
Title: Governance
Icons highlighted (bottom-right): W, R, D, T (all four)
Layout: Layered framework stack on the left + metrics list on the right
Framework stack (bottom to top):
- NIST SP 800-218A (SSDF GenAI profile) - the spine
- NIST AI 600-1 (risk taxonomy)
- NCSC + CISA Guidelines for Secure AI System Development (lifecycle hooks)
- OWASP Top 10 for LLM Applications
Metrics:
- AI-assisted PR rate
- Vuln rate: AI vs human
- Secret exposures from AI
- MTTR for AI-introduced vulnerabilities
Closing line: "Multi-signal correlation - endpoint + exposure + identity - is how you actually see a rogue AI agent."
Visual: Stacked framework layers on the left (each layer labelled, the SSDF GenAI profile at the base). Metrics as a clean bullet list on the right.
Tone: Audit-grade, regulatory-aware. The "what gets reported to the board" slide.
```

---

## Slide 20 (P3.6) - Restoring the four

```
Title: Restoring the four
Icons highlighted (bottom-right): W, R, D, T (all four)
Layout: Four-row restoration table + closing aphorism band
Table (one row per broken assumption):
- W | The developer wrote it | AI-usage disclosure at PR level + AI-BOM
- R | The reviewer read it | Pair review on AI-assisted PRs; redistribute review capacity (seniors review more, write less)
- D | The dependencies were vetted | Allowlist your package registry at CI; block hallucinated imports; pin and verify
- T | The tools were deterministic | Inventory AI assets and MCP servers; pin AI-tool versions; intake-review every new AI tool
Cross-cutting move (footer): Anchor the programme to NIST SP 800-218A. Report the four restorations as the metrics that matter.
Closing aphorism band (full-width, italic): "Aviation didn't get safe by trusting one agent. It got safe by trusting a system. These four restorations are software's equivalent."
Visual: Clean four-row table with the W/R/D/T icons on the left. Use the same icon design as Slide 3 (P1.3) - this is the bookend. Closing aphorism in italic across the bottom.
Tone: Conclusive. The talk's punchline.
```

---

## Slide 21 (P-Close) - Q&A and Part 2

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
