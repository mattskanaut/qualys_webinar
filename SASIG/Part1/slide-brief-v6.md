# Slide Briefs v6 - all Gamma briefs in one place

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Slide count:** 19

> Each block below is a Gamma brief for a single slide, in running order. Paste the fenced code block into gamma.app to generate the slide.

---

## Slide 1 - Title and the promise

```
Title: The New SDLC: Security When Every Developer Writes With AI
Subtitle: When the four assumptions of secure development all break at once
Series tag: The New Normal: Software, Security and the AI Stack - Part 1 of 2
Layout: Title slide
Promise (small text below subtitle): Non-product. 40% problem, 60% what to do. Every stat sourced.
Footer: Bibliography lands in your inbox.
Visual: Series wordmark across the top. Subtitle in smaller type below the main title. Three-icon strip (shield / clock / book) as a quiet bottom motif.
Tone: Sober, intentional. Earn the room.
```

---

## Slide 2 - Real CVEs in real repos

```
Title: Real CVEs in real repos
Subtitle: AI-attributed vulnerabilities are showing up at scale, in production
Layout: Trajectory chart + supporting stats panel
Headline chart - Georgia Tech Vibe Security Radar (Apr 2026):
  - Jan 2026: 6 AI-attributed CVEs
  - Feb 2026: 15
  - Mar 2026: 35
  Annotation: Lifetime 74; 27 traceable to Claude Code
Supporting bullets (right panel):
- Endor Labs / CMU Agent Security League (Apr 2026): 200 real OSS tasks; top agent 84.4% functional, 17.3% security pass
- Fu et al., ACM TOSEM 2025: 29.5% of Python and 24.2% of JS Copilot snippets in real GitHub projects had at least one CWE
Closing line: The slope is the story. These are real CVEs, not benchmarks.
Visual: Monthly bar chart on the left showing the 6 / 15 / 35 trajectory. Supporting stats as small caption rows on the right.
Tone: Concrete, unmistakable. Ground the rest of the talk in "this is happening now."
```

---

## Slide 3 - Secure SDLC is a defined discipline

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

## Slide 4 - Secure SDLC is a profession

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
Tone: Reflective. Sets up the four assumptions. Not technical.
```

---

## Slide 5 - The four assumptions every secure SDLC rests on

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
Visual: Four large quadrant cells, each dominated by a bold W/R/D/T glyph. This is a concept slide, not a recurring icon system - the deck does not pin these icons in slide corners.
Tone: Definitive. The talk's conceptual anchor.
```

---

## Slide 6 - Where CI/CD fits - SDLC defines, pipelines enforce

```
Title: Where CI/CD fits - SDLC defines, pipelines enforce
Layout: Two horizontal tiers, top stacked above bottom, with a labelled divider line between them
Top tier - "SDLC practices: the human-judgment layer"
  Label: Writer, Reviewer, Dependency assumptions live here
  Caption: NIST SP 800-204D Appendix B - PW.1-PW.4 and PW.7 "pertain to secure software design, review of the design, and software reuse"
Bottom tier - "CI/CD pipeline (build - test - package - deploy)"
  Label: Tool assumption rides here
  Badge: SLSA v1.2 (L0-L3) on the build-platform box
Side caption: "Three of four assumptions live above the pipeline. Only the tool assumption rides on it. More pipeline tooling alone won't save you."
Visual: Two horizontal bands stacked. The dividing line carries the NIST citation in italics. SLSA badge as a small overlay.
Tone: Definitive. Closes Section 1 and sets up Section 2.
```

---

## Slide 7 - From tool to author

```
Title: From tool to author
Subtitle: "Vibe coding" - Collins Dictionary Word of the Year 2025

Layout: One hero stat dominating. Trajectory row beneath. Pull quote and adoption-stats footer band below.

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

Pull quote (italics, below the trajectory row):
  "fully give in to the vibes... forget that the code even exists"
  Attribution: Andrej Karpathy, Feb 2025 - the tweet that coined "vibe coding"

Adoption footer band (small type, two lines):
  Line 1: 4.7M paid Copilot subs (~90% of Fortune 100, Microsoft FY26 Q2) | 90% of devs use AI at work (DORA 2025) | 90%+ of software teams (McKinsey Feb 2026)
  Line 2: Frontier labs sit higher - Anthropic 70-90% company-wide; senior engineers ~100% personal workflows (Fortune Jan 2026)

Closing line (set off, bottom): The slope is the story.

Style: 75% must dominate. Adoption stats are footer-only, not equal-weighted with the hero. Sober, factual layout. No charts, no clip art.
Tone: Crisp, factual, no hype. Cultural framing in the subtitle, audited number as the hero.
```

---

## Slide 8 - The four moving parts of AI dev tooling

```
Title: The four moving parts of AI dev tooling
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
Visual: Architecture diagram. Boxes flow left-to-right with arrows showing data flow. A subtle dotted boundary line separates "what the developer sees" (LLM + Harness) from "what gets executed against your systems" (MCP + RAG).
Tone: Educational, fast. Skim-readable.
```

---

## Slide 9 - The productivity paradox

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
Visual: Two-panel chart - left: Cui +26% / METR -4% (with original -19% greyed out); right: DORA PR-size and review-time deltas drawn to scale (the +441% bar dominates).
Tone: Data-driven. The trade-off is the story.
```

---

## Slide 10 - Quality on security is materially worse - and not improving

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
Visual: Three-bar comparison (2022 / 2025 / Spring 2026) showing flat trajectory across generational LLM upgrades. Supporting bullet underneath.
Tone: Sobering, evidence-led. The flat line is the headline.
```

---

## Slide 11 - Insecure-by-default at scale

```
Title: Insecure-by-default at scale
Layout: Hockey-stick chart + supporting bullets
Headline stat: 10x new findings/month from AI-generated code
  Source: Apiiro Fortune-50 telemetry, mid-2025 (7,000+ devs, 62,000 repos)
Supporting bullets:
- +322% privilege escalation paths
- +153% architectural flaws
- +40% secret exposures
- 41% of AI-generated backend code ships with default-admin permissions when prompted naively (Backslash 2025)
- Trivial errors fell; deep flaws exploded
Closing line: "Shallow up, deep down." The prompt is part of the security perimeter now.
Visual: Apiiro hockey-stick of monthly findings (Dec 2024 - mid 2025). Bullets to the right. The default-admin-perms stat sits as a separate callout to flag prompt engineering as a control plane.
Tone: Evidence-driven. Let the slope speak.
```

---

## Slide 12 - Hallucinated dependencies and slopsquatting

```
Title: Hallucinated dependencies and slopsquatting
Layout: Per-model hallucination chart + attack-flow diagram
Headline stat: 43% of LLM-hallucinated package names recur across 10 prompt repeats
  Source: Spracklen et al., USENIX Security 2025 (576,000 samples, 16 LLMs)
Supporting bullets:
- Commercial LLMs >=5.2% hallucination rate; open-source >=21.7%
- 205,474 unique fabricated package names catalogued
- Lasso registered hallucinated `huggingface-cli` -> 30,000+ downloads in 3 months
- Hallucinated names landed in vendor docs (Alibaba GraphTranslator README)
Closing line: Perfect repeatability for an attacker. CI allowlist is the highest-leverage control in this whole talk.
Visual: Per-model hallucination-rate bar chart on the left. Three-step attack-flow on the right (LLM hallucinates -> attacker registers on PyPI -> developer's AI-suggested import installs malware). Red arrows for the attack path.
Tone: Concrete, actionable.
```

---

## Slide 13 - The AI toolchain is itself an attack surface

```
Title: The AI toolchain is itself an attack surface
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

## Slide 14 - Tooling - PR gates, AI-asset inventory, IDE boundary

```
Title: Tooling - PR gates, AI-asset inventory, IDE boundary
Layout: Pipeline diagram with four labelled gates
Gate 1: AI-asset & MCP-server inventory
  Caption: the new shadow IT
Gate 2: IDE boundary
  Caption: Hines et al. Spotlighting reduces prompt-injection ASR from >50% to <2%
Gate 3: PR gate (fail-closed)
  Caption: SAST + secrets + SCA on AI-assisted PRs; block hallucinated imports
Gate 4: Build gate
  Caption: pin AI tool versions; treat MCP servers as third-party deps
Closing line: "Inventory first, then gates."
Visual: Linear horizontal pipeline diagram. Each gate is a vertical bar across the pipeline, annotated with the control it enforces. Use the same accent colour throughout to signal "pipeline-enforceable."
Tone: Operational, prescriptive. The "what to actually configure" slide.
```

---

## Slide 15 - Process - the human-judgment restorations

```
Title: Process - the human-judgment restorations
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

## Slide 16 - Culture and Organisation

```
Title: Culture and Organisation
Subtitle: The team and the org are the same change in two registers
Layout: Two-column - Culture rules on the left, Organisational moves on the right
Left column - Culture rules:
- No merge until reviewed by someone who did not write the prompt
- Pair-review for AI-generated code - one used AI, one did not
- Ownership is human, regardless of what wrote it
- Reward catches, not velocity
Right column - Organisational moves:
- Name an owner: AppSec + engineering lead (not product)
- Joint governance body, weekly cadence (49% of orgs run 5+ AI tools)
- Redistribute review workload - seniors review more, write less
- Hire and grade for the review reflex, not the typing reflex
Footer (italic): Sandoval et al. (USENIX Security 2023, "Lost at C") - review interaction is the primary moderator of LLM-assisted bug rate
Closing line: "Review capacity is now the engineering org's bottleneck."
Visual: Two columns of equal weight. Subtle "two developers reviewing together" line illustration as a divider or background motif. Restrained design.
Tone: Cultural and structural. The "what kind of team are we, and how is it staffed" slide.
```

---

## Slide 17 - Governance and metrics

```
Title: Governance and metrics
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

## Slide 18 - On the other hand - maybe this is transitional

```
Title: On the other hand - maybe this is transitional
Subtitle: The honest counter-argument

Layout: Steel-man only. Five clean bullet rows. No rebuttal on the slide - the rest of the deck is the rebuttal.

Setup line (top of slide, italic):
  "Maybe AI gets so good these concerns evaporate. Worth taking that seriously."

Five steel-man bullets (each one or two lines, equal weight):
- Aviation analogy. ~70% of commercial flight time is on autopilot. Senior pilots will tell you they trust the autopilot more than they trust most humans. The "pilot is god" model died in the 1970s.
- Frontier-lab evidence. Boris Cherny (Claude Code) ships 22 PRs/day with Claude writing 100%. Roon at OpenAI: "I don't write code anymore." Real people, real work, end-to-end.
- Generational trajectory. GPT-3.5 -> 4 -> 5 showed huge reasoning gains. Veracode's 45% vulnerability rate today might be 20% next year. The flat line could finally break.
- Defensive tooling improves alongside. AI-aware SAST, prompt-injection defenses (Spotlighting: 50% -> 2% ASR), AI-BOM specs maturing. Models are getting better; the perimeter around them is too.
- Historical analogy. We used to read assembly to verify compilers. We used to manage memory by hand. Each abstraction layer was scary at the time and we adapted. Maybe AI-as-author is just the next layer.

Closing line (italic, set off at bottom):
  "Maybe. But you have to defend now, not in five years."

Visual: Five clean bullet rows, equal spacing, no charts. Subtle aviation imagery (cockpit silhouette or autopilot indicator) as a quiet side panel or background motif.
Tone: Intellectually honest, even-handed. The talk's most generous moment to the counter-argument. The audience does the rebuttal work because they just sat through it.
```

---

## Slide 19 - Q&A and Part 2 preview

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
