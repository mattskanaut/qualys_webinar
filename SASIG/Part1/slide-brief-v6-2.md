# Slide Briefs v6.2 - punchier briefs

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Slide count:** 19

> Companion to `slide-plan-v6.md` - same 19 slides, leaner Gamma briefs. Detail, captions, and supporting prose live in slide-plan-v6.md speaker notes; this file is what to paste into gamma.app.

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

## Slide 2 - Real CVEs in real repos

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

## Slide 3 - Secure SDLC is a defined discipline

```
Title: Secure SDLC is a defined discipline
Cards (4):
- Microsoft SDL (2004)
- NIST SSDF (2022)
- OWASP SAMM
- BSIMM 15
Footer band: EU CRA | UK PSTI | EU AI Act
Visual: 4-card grid above a regulation band. No logos.
Tone: Authoritative.
```

---

## Slide 4 - Secure SDLC is a profession

```
Title: Secure SDLC is a profession
Banner quote: "Buildings don't fall down because of monitoring. They don't fall down because designers and builders behaved professionally."
Two-panel comparison:
  Buildings: designer | builder
  Software: developer | reviewer | maintainer | operator
Common base: frameworks - standards - regulation
Visual: Architectural line-art left, code-repo schematic right.
Tone: Reflective.
```

---

## Slide 5 - The four assumptions every secure SDLC rests on

```
Title: The four assumptions every secure SDLC rests on
2x2 quadrant:
  W - The developer wrote it
  R - The reviewer read it
  D - The dependencies were vetted
  T - The tools were deterministic
Footer (italic): "With AI in the loop, what does the developer actually know about what was just written?"
Visual: Four bold W/R/D/T glyphs. Concept slide - icons appear here only, not pinned in later slides.
Tone: Definitive.
```

---

## Slide 6 - Where CI/CD fits

```
Title: SDLC defines, pipelines enforce
Two-tier diagram:
  Top tier - SDLC practices (the human-judgment layer): Writer, Reviewer, Dependency
  Bottom tier - CI/CD pipeline (build - test - package - deploy): Tool
Divider citation (italic): NIST SP 800-204D Appendix B
Side caption: "Three of four assumptions live above the pipeline."
Visual: Two stacked bands. SLSA badge on the build box.
Tone: Definitive.
```

---

## Slide 7 - From tool to author

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

Closing line: The slope is the story.

Visual: 75% dominates the slide. Trajectory beneath it. Adoption headcount stats stay in speaker notes.
Tone: Crisp, audited.
```

---

## Slide 8 - The four moving parts of AI dev tooling

```
Title: The four moving parts of AI dev tooling
Four boxes left-to-right:
  LLM - the brain
  Harness - turns prediction into action
  MCP server - talks to your systems
  RAG - pulls in your data
Footer: Today: build-time AI. Runtime is Part 2.
Visual: Architecture diagram. Dotted line separates "what the developer sees" from "what runs against your systems."
Tone: Educational, fast.
```

---

## Slide 9 - The productivity paradox

```
Title: The productivity paradox
Two panels:
  Productivity: +26% PRs/week (Cui RCT, n=4,867)
  Review cost: +441% review time | PR size +51% (DORA 2025)
Closing line: The reviewer is now the load-bearing role.
Visual: Two-panel comparison. The +441% bar dominates.
Tone: Data-driven.
```

---

## Slide 10 - Quality on security is materially worse

```
Title: Quality on security - and not improving
Three-bar chart:
  2022: 40% (Pearce IEEE S&P)
  2025: 45% (Veracode Spring 2026)
  2026: 55.8% (Broken-by-Default, Z3-proven)
Supporting line: 6 SAST tools combined miss 97.8%
Visual: Three bars showing a flat line across four years and a generation of LLMs.
Tone: Sobering.
```

---

## Slide 11 - Insecure-by-default at scale

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

## Slide 12 - Hallucinated dependencies and slopsquatting

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

## Slide 13 - The AI toolchain is itself an attack surface

```
Title: The AI toolchain is itself an attack surface
Lead incident: LiteLLM (Mar 2026)
  3.4M daily downloads | 40k+ in the exposure window
CVE tile grid (2026):
  Cursor RCE
  Copilot Reprompt
  Claude Code CLI RCE
  Windsurf MCP zero-interaction
Bullet: ~2,000 production MCP servers, none authenticated (Prakash AIP)
Closing line: The pipeline runs AI tools that run AI tools.
Visual: Pipeline-attack-flow left. CVE tile grid right.
Tone: Names, dates, CVEs.
```

---

## Slide 14 - Tooling

```
Title: Tooling - the pipeline-enforceable controls
Pipeline diagram with four gates:
  1. AI-asset & MCP inventory
  2. IDE boundary
  3. PR gate (fail-closed)
  4. Build gate (pin versions)
Closing line: Inventory first, then gates.
Visual: Linear horizontal pipeline with four vertical gate bars.
Tone: Operational.
```

---

## Slide 15 - Process

```
Title: Process - the human-judgment restorations
PR mockup with two new fields highlighted:
  AI-assisted? (yes / no / which tool)
  AI-BOM attached?
Bullets:
- AI-usage disclosure at PR level
- AI-BOM (extends SBOM)
- Third-party AI-tool intake review
- AI branch in IR playbook
Closing line: Disclosure first. Provenance second.
Visual: GitHub-style PR mockup left. Bullets right.
Tone: Practical.
```

---

## Slide 16 - Culture and Organisation

```
Title: Culture and Organisation
Two columns:
  Culture:
    No merge until reviewed by someone who didn't write the prompt
    Pair-review: one used AI, one didn't
    Ownership is human
    Reward catches, not velocity
  Organisation:
    Joint AppSec + engineering owner (not product)
    Weekly governance cadence
    Seniors review more, write less
    Hire for the review reflex
Closing line: Review capacity is the new bottleneck.
Visual: Two equal columns. Subtle "two devs reviewing" line illustration as a divider.
Tone: Cultural and structural.
```

---

## Slide 17 - Governance and metrics

```
Title: Governance and metrics
Framework stack (bottom to top):
  NIST SP 800-218A
  NIST AI 600-1
  NCSC + CISA
  OWASP LLM Top 10
Metrics:
  AI-assisted PR rate
  Vuln rate: AI vs human
  Secret exposures from AI
  MTTR for AI-introduced vulns
Closing line: Endpoint + exposure + identity.
Visual: Stacked framework layers left. Metrics list right.
Tone: Audit-grade.
```

---

## Slide 18 - On the other hand - maybe this is transitional

```
Title: On the other hand
Subtitle: Maybe this is transitional

Five bullets (one line each):
- Aviation: ~70% of flight time is on autopilot
- Boris Cherny ships 22 PRs/day, Claude writing 100%
- GPT-3 -> 4 -> 5: the flat line could break
- Defensive tooling improves alongside (Spotlighting: 50% -> 2% ASR)
- We adapted to compilers, GC, high-level languages

Closing line (italic): Maybe. But you have to defend now, not in five years.

Visual: Five clean bullet rows. Subtle aviation imagery as a quiet background motif.
Tone: Even-handed. The deck is the rebuttal.
```

---

## Slide 19 - Q&A and Part 2

```
Title: Q&A | Part 2 preview
Two columns:
  Questions: bibliography by email | Q&A
  Coming up: Part 2 - Running AI in Production
Visual: Series wordmark. Two columns.
Tone: Open. End on the next thing.
```
