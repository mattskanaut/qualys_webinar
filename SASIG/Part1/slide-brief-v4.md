# Slide briefs v4 (for gamma.app)

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2

Each section below is a self-contained brief for one slide. Copy the fenced block straight into gamma.app.

Slides 1 and 2 (Title and Opening hook) live in `outline-v4.md` only - briefs for those to follow if needed.

---

## P1.1 (running-order #3) - Secure SDLC is a defined discipline

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

## P1.2 (running-order #4) - Secure SDLC is a profession

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

## P1.3 (running-order #5) - The four assumptions every secure SDLC rests on

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

## P1.4 (running-order #6) - Where CI/CD fits

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

## P2.1 (running-order #7) - AI is now in every developer's hands

```
Title: AI is now in every developer's hands
Layout: Three-stat headline grid (big numbers, small captions)
Stat 1: 4.7M
  Caption: paid Copilot subscribers (Microsoft FY26 Q2, Jan 2026)
  Sub-caption: ~90% of Fortune 100
Stat 2: 90%
  Caption: of devs use AI at work (DORA 2025)
  Sub-caption: 65% rely on it heavily
Stat 3: 90%+
  Caption: of software teams use AI (McKinsey 2026)
Closing line: "Take 'AI is in your stack' as established."
Visual: Three big-number cards in a row. Source attribution in small type underneath each. No clip art. Sober design.
Tone: Crisp, factual, no hype.
```

---

## P2.2 (running-order #8) - What's actually in your build pipeline now

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

## P2.3 (running-order #9) - Writer - the developer wrote it

```
Title: Writer - the developer wrote it
Icon highlighted (bottom-right): W
Layout: Headline stat + supporting bullets
Headline: 10x new findings/month from AI-generated code
  Source: Apiiro Fortune-50 telemetry, mid-2025 (7,000+ devs, 62,000 repos)
Supporting bullets:
- +322% privilege-escalation paths
- +153% architectural flaws
- +40% secret exposures
- 41% of AI-generated backend code ships with default-admin perms when prompted naively (Backslash 2025)
- AI-assisted devs wrote less secure code on 4 of 5 tasks AND were more likely to believe it was secure (Perry et al., ACM CCS 2023)
Closing line: "Shallow up, deep down - trivial errors fell, architectural and identity flaws exploded."
Visual: Hockey-stick chart of monthly findings (Dec 2024 - mid 2025) on the left. Bullets on the right. Apiiro source attribution.
Tone: Data-driven. Let the numbers do the work.
```

---

## P2.4 (running-order #10) - Reviewer - the reviewer read it

```
Title: Reviewer - the reviewer read it
Icon highlighted (bottom-right): R
Layout: Two-stat headline + context bullets
Stat 1: PR size +51%
Stat 2: PR review time +441%
  Source for both: DORA 2025 (n~5,000 developers)
Supporting bullets:
- 84% of devs use AI but only 29% trust it (Stack Overflow Feb 2026)
- Developer trust at -11 points YoY
- 81% concerned about AI-generated code security
- Reviewer can't see model, prompt, or RAG context the AI had
Closing line: "The reviewer is now the load-bearing role - and the bottleneck."
Visual: Side-by-side bar chart of PR-size and review-time deltas (with the +441% bar drawn to scale - it dominates). Context bullets underneath.
Tone: Direct. The bottleneck has moved.
```

---

## P2.5 (running-order #11) - Dependency - the dependencies were vetted

```
Title: Dependency - the dependencies were vetted
Icon highlighted (bottom-right): D
Layout: Headline stat + attack-flow diagram
Headline: 43% of LLM-hallucinated package names recur across 10 prompt repeats
  Source: Spracklen et al., USENIX Security 2025 (576,000 samples, 16 LLMs)
Supporting bullets:
- Commercial LLMs >=5.2% hallucination rate; open-source >=21.7%
- 205,474 unique fabricated package names catalogued
- Lasso registered hallucinated `huggingface-cli` -> 30,000+ downloads in 3 months
- Hallucinated package names landed in vendor docs (Alibaba GraphTranslator README)
Attack flow (3-step diagram): LLM hallucinates name -> attacker registers it on PyPI -> developer's AI-suggested import installs malware
Closing line: "Perfect repeatability for an attacker. The CI allowlist is the highest-leverage control in this whole talk."
Visual: Per-LLM hallucination-rate bar chart on the left. Three-step attack-flow diagram on the right. Use red arrows for the attack path.
Tone: Concrete, actionable. Slopsquatting is a real and fixable threat.
```

---

## P2.6 (running-order #12) - Tool - the tools were deterministic

```
Title: Tool - the tools were deterministic
Icon highlighted (bottom-right): T
Layout: Incident-tile grid + scoping caption
Incident tiles (each with date and one-line summary):
- LiteLLM (24 Mar 2026): backdoored 1.82.7/1.82.8 via Trivy in CI; 3.4M daily downloads; 40k in exposure window
- Cursor RCE - CVE-2026-26268
- Copilot Reprompt - CVE-2026-21516
- Claude Code CLI RCE - CVE-2026-35021
- Windsurf MCP zero-interaction - CVE-2026-30615
- Hou et al. 2025: 16 MCP threat scenarios across the lifecycle
- Prakash AIP 2026: ~2,000 MCP servers scanned, none authenticated
- Vercel / Context AI (20 Apr 2026): AI-vendor as supply-chain pivot
Closing line: "The pipeline runs AI tools that run AI tools. This is the new attack surface."
Visual: 8-tile incident grid, most recent on top. Each tile has a date stamp, vendor logo (where appropriate), and one-line consequence. Use a consistent severity colour scheme.
Tone: Specifics. Names, dates, CVEs.
```

---

## P3.1 (running-order #13) - Tooling - PR gates, AI-asset inventory, IDE boundary

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

## P3.2 (running-order #14) - Process - the human-judgment restorations

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

## P3.3 (running-order #15) - Culture

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

## P3.4 (running-order #16) - Organisation

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

## P3.5 (running-order #17) - Governance

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

## P3.6 (running-order #18) - Restoring the four

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
Visual: Clean four-row table with the W/R/D/T icons on the left. Use the same icon design as Slide P1.3 - this is the bookend. Closing aphorism in italic across the bottom.
Tone: Conclusive. The talk's punchline.
```

---

## P-Close (running-order #19) - Q&A and Part 2

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
