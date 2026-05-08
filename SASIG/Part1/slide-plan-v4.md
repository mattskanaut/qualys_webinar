# Part 1 - Slide Plan (v4, profession-anchored)

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders (vendors, contractors and press excluded)
**Format:** 60-min slot. ~34 min content + 10 min Q&A + 5 min host preamble.
**Style:** Brief, high-level. Speaker carries the content; slides anchor.

> **Gamma briefs:** Each slide section below ends with a `### Gamma brief` fenced code block. Paste that block directly into gamma.app to generate the slide. The full bullets, speaker notes, and sources stay outside the brief - they're for the speaker, not the tool.

---

## The argument

1. Secure software development is a mature, 30-year-old discipline with broad consensus, **and now codified in product law - EU CRA (in force Dec 2024), UK PSTI Act (full enforcement Apr 2024), EU AI Act (staged from Aug 2024)**. The 30-year consensus has just become a regulatory floor.
2. Its controls quietly depend on humans doing the work - defining requirements, threat-modelling, reviewing designs, choosing libraries, reading code. **NIST itself draws this line: SP 800-204D Appendix B carves PW.1 - PW.4 and PW.7 out of CI/CD pipeline scope on the grounds that they "pertain to secure software design, review of the design, and software reuse." Read plainly, that is the human-judgment layer of the SSDF.**
3. AI now sits inside every human-judgment control and compresses or removes it. Four assumptions break:
   - **The developer wrote it** (W)
   - **The reviewer read it** (R)
   - **The dependencies were vetted** (D)
   - **The tools were deterministic** (T)
4. The response is mostly not more pipeline tooling. **Pipelines can encode codifiable judgment - version pinning, policy-as-code, threat-model templates, allowlists - but cannot exercise the residual judgment AI is compressing: was the design fit for purpose, is this AI-suggested library actually maintained, did the reviewer understand what they approved.** That residual layer - W, R, and D - is restored through process, organisation, and governance. **Pipelines reinforce T.**

---

## Structural rebuild from v3

Three changes from v3 drove this rebuild:

1. **Three competing taxonomies collapsed into one.** v3 had PO/PS/PW/RV (slide P1.2), six build-time controls (P1.3), and the four assumptions (Section 2 framing slide). Audience cognitive load was 18 items across four taxonomies. v4 makes the four assumptions the *only* talk-level taxonomy, introduced once in Part 1, used everywhere afterwards. Framework citations move to inline references under each assumption.
2. **Profession-framing surfaced.** v3 implicitly assumed the audience would intuit that secure SDLC rests on professional trust. v4 names it explicitly with a dedicated slide (the buildings analogy) so the four assumptions land as *professional* assumptions, not technical controls.
3. **Section 3 expanded back to v2's depth.** v3 compressed Culture, Organisation, and Governance into two slides for time. With a 60-min slot (not the 30-min I'd been targeting), the three response categories get full slides each.

The four-assumption spine (W/R/D/T) survives unchanged. v3's Section 2 framing slide is dropped because the spine is now established in Part 1.

---

## How CI/CD fits (framing for Part 1)

CI/CD is the operational *enactment* of the SDLC. The SDLC defines what good development practices are; CI/CD pipelines are where those practices become automated, enforceable gates rather than aspirational policy. The bridge is explicit in the literature:

- **NIST SP 800-218 (SSDF)** defines the practices (the *what*).
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) - *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines* - is the companion publication that maps SSDF practices onto CI/CD pipeline stages: **build, test, package, deployment** (the *how*, in CI/CD terms). NIST itself draws the line: Appendix B carves SSDF practices PW.1 - PW.4 and PW.7 out of CI/CD scope on the grounds that they "pertain to secure software design, review of the design, and software reuse."
- **SLSA v1.2** defines build-platform integrity levels (L0 - L3) so "we built it on a trusted system" is provable rather than asserted.
- **DevSecOps** is the cultural framing: every CI/CD stage is also a security stage; shift-left because a CWE caught in a PR is roughly two orders of magnitude cheaper than one caught in production.

This is also the right place to land the build-time framing - this talk owns the build-time / artefact layer, distinct from the workforce and runtime layers in adjacent SASIG sessions.

---

# Section 1 - Secure SDLC concepts

## Slide P1.1 - Secure SDLC is a defined discipline, not a buzzword

- **Microsoft SDL** (origin: Bill Gates Trustworthy Computing memo, January 2002; first published SDL ~2004): five phases - Requirements, Design, Implementation, Verification, Release - plus 10 practices including threat modelling, secure engineering environment, supply-chain security, security testing, monitoring and response.
- **NIST SP 800-218 (SSDF v1.1)**, Feb 2022; **v1.2 in public comment** (Dec 2025 - Jan 2026). Four practice groups: PO (Prepare the Organization), PS (Protect the Software), PW (Produce Well-Secured Software), RV (Respond to Vulnerabilities). The U.S. federal baseline.
- **OWASP SAMM v2** - open-source maturity model. Five business functions, 15 security practices, three maturity levels.
- **BSIMM 15** (Black Duck / Synopsys, 2024) - the *measured* practice across 121 firms. 12 practices in 4 domains.
- **Now codified in product law:** EU CRA (in force Dec 2024, full obligations Dec 2027), UK PSTI Act (full enforcement Apr 2024), EU AI Act (staged from Aug 2024). The 30-year consensus has just become a regulatory floor.

**Graphic:** Four-logo / four-card lineup with year established and one-line "what it is." A separate footer band shows the three regulations with their in-force dates.

**Speaker notes:** Three decades, four mature frameworks, one clear consensus - secure software development has a defined shape. Microsoft SDL is the grandfather; NIST SSDF is the U.S. federal baseline; SAMM is the open-source maturity model; BSIMM is the *empirical* model - what firms actually do, measured. Take the convergence as established and move on.

The new line worth landing for this audience: as of late 2024 / early 2025 this is no longer just industry consensus - it's a regulatory floor in your home jurisdictions. EU CRA covers any product with digital elements sold into the EU. UK PSTI is in full force. The EU AI Act applies on top where AI components are involved. Your customers' regulators now require what these frameworks recommend.

**Sources:**
- Microsoft SDL practices - https://www.microsoft.com/en-us/securityengineering/sdl/practices
- NIST SSDF (project page) - https://csrc.nist.gov/projects/ssdf
- NIST SP 800-218 v1.1 - https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF v1.2 public comment notice - https://www.nist.gov/news-events/news/2025/12/secure-software-development-framework-ssdf-version-12-available-public
- OWASP SAMM - https://owaspsamm.org/model/
- BSIMM 15 datasheet - https://www.blackduck.com/content/dam/black-duck/en-us/datasheets/bsimm-datasheet.pdf
- EU Cyber Resilience Act - https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- UK PSTI Act - https://www.gov.uk/government/collections/the-product-security-and-telecommunications-infrastructure-psti-act
- EU AI Act - https://artificialintelligenceact.eu/
- NCSC + CISA Guidelines for Secure AI System Development - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf

### Gamma brief

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

## Slide P1.2 - Secure SDLC is a profession

**Top thesis (banner):** *"Secure-SDLC frameworks codify a profession. Like every profession, they rest on assumptions about how trusted humans behave."*

- Buildings don't fall down *only* because of monitoring by building control or planning departments. They don't fall down because the designer and the builder behaved professionally.
- A profession is the mechanism by which society delegates trust. We delegate to humans we believe to be competent - they execute their work to the standards we lay out, and we don't have to inspect every weld.
- Secure software development works the same way. We don't audit every line - we trust the developer. We don't review every dependency manually - we trust the maintainer chose it knowingly. We don't decompile every tool - we trust the operator wields it deterministically.
- Without that delegation, every line, every dep, every tool would need exhaustive verification. It doesn't scale.
- The four assumptions on the next slide are how that delegation manifests in code.

**Graphic:** Two-panel diagram. Left: a building under construction, with arrows from "designer" and "builder" labelled "professional practice." Right: a code repo, with arrows from "developer," "reviewer," "maintainer," "operator" labelled "professional practice." Underneath both: the same supporting layers - "frameworks, standards, regulation."

**Speaker notes:** Take a step back. Secure software development is not first a tooling stack - it's a profession. The frameworks on the previous slide are how the profession codifies its standards.

The buildings analogy is the cleanest way I know to land this. Buildings don't fall down because the planning department audits every weld. They don't fall down because there's a regulator at the foundation pour. They don't fall down because the designer and the builder behaved professionally - they applied their training, they followed the standards, they took responsibility for what they signed off on. Monitoring matters; it's a backstop. But the primary mechanism by which buildings stay up is the professional practice of the people who designed and built them.

Software security has worked this way for thirty years. We don't audit every line of code in production. We don't manually review every package in our SBOM. We don't decompile every binary in our toolchain. We *trust* - we trust the developer wrote it knowingly, we trust the reviewer read it carefully, we trust the maintainer chose dependencies that were real and maintained, we trust the operator wielded the tools deterministically. That trust is the assumption stack the rest of the discipline sits on top of.

The reason this matters now: AI sits inside every one of those trust delegations. With AI in the loop, what does the developer actually know about what was just written?

**Sources:** Frameworks already cited on Slide P1.1.

### Gamma brief

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

## Slide P1.3 - The four assumptions every secure SDLC rests on

Each assumption named, with the frameworks that codify it in tiny type underneath.

| Icon | Assumption | What humans used to do | Codified in |
|---|---|---|---|
| **W** | The developer wrote it | A human composed the line, knowing what it did | SSDF PW.5 *Create Source Code by Adhering to Secure Coding Practices*; SDL secure coding (practice 6); SAMM Secure Build |
| **R** | The reviewer read it | A second human read the change before merge | SSDF PW.2.1 ("a qualified person not involved with the design"); SSDF PW.7 *Review and/or Analyze Human-Readable Code*; SDL Verification ("manual review by a reviewer who isn't the engineer that developed the code"); SAMM Architecture Assessment + Security Testing |
| **D** | The dependencies were vetted | A human knew the package existed, was maintained, and was fit for use | SSDF PS.3.2 *Collect, safeguard, maintain, and share provenance data ... in a software bill of materials*; SSDF PW.4.4 third-party component verification through life cycle; SLSA v1.2 build-track provenance; SAMM Software Dependencies |
| **T** | The tools were deterministic | The operator invoked tools that ran what they were told, predictably | SSDF PO.3 *Implement Supporting Toolchains*; SSDF PO.5 *Implement and Maintain Secure Environments*; SDL secure engineering environment + supply-chain (practice 5) |

*Closing italicised line at bottom of slide:* **"With AI in the loop, what does the developer actually know about what was just written? How secure are we?"**

**Graphic:** Four-quadrant card. Each quadrant has the icon (W / R / D / T), the one-sentence assumption, and the framework citations beneath in smaller type. **This is the icon legend** - the same four icons appear in the bottom-right of every Section 2 and Section 3 slide, with the relevant icon highlighted.

**Speaker notes:** This is the spine of the whole talk. Walk the four quadrants slowly.

For each, name what the human used to do and what framework practice encodes it. Keep emphasising: these are *professional* assumptions, not technical controls. They name what every secure-SDLC programme implicitly trusts humans to do. The frameworks underneath are how the profession codified each delegation.

Honest framing for a senior audience: this four-assumption packaging is my synthesis for this conversation - the individual claims trace to NIST SSDF, SDL, SAMM, SLSA and the empirical literature; the four-quadrant frame is mine. I'm not claiming NIST or anyone else has named it this way. I'm claiming this is the cleanest way to see what AI just changed.

Pause on the closing line. Don't answer it - the answer is the rest of the talk.

**Sources:**
- NIST SP 800-218 (SSDF v1.1) - verbatim practice titles, https://csrc.nist.gov/pubs/sp/800/218/final
- Microsoft SDL practices - https://www.microsoft.com/en-us/securityengineering/sdl/practices
- OWASP SAMM model - https://owaspsamm.org/model/
- SLSA v1.2 - https://slsa.dev/spec/v1.2/

### Gamma brief

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

## Slide P1.4 - Where CI/CD fits - SDLC defines, pipelines enforce

- **SDLC = practices** (NIST SSDF, Microsoft SDL, OWASP SAMM, BSIMM). **CI/CD = enforcement** - where the practices become automated gates or get bypassed.
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) - *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines* - is the explicit bridge. Pipeline stages: **build, test, package, deployment**. Two stated security goals (Sec. 4.1): (1) actively defend the CI/CD pipeline and build processes; (2) ensure the integrity of upstream sources and artifacts.
- **NIST itself draws the line.** Appendix B carves SSDF practices **PW.1 - PW.4 and PW.7** out of CI/CD pipeline scope on the grounds that they "pertain to secure software design, review of the design, and software reuse." Read plainly: that is the human-judgment layer of the SSDF. Appendix B similarly carves **RV.1 - RV.3** as "at the organization policy level and not specific to CI/CD pipelines."
- Mapped against the four assumptions: **W, R, D live above the pipeline.** Only **T (deterministic tools)** rides on it.
- **SLSA v1.2 build levels (L0 - L3)** turn build-platform integrity from assertion into evidence (L1 = provenance exists; L2 = hosted, signing platform; L3 = platform isolation and confidentiality).
- **DevSecOps** is the cultural frame; **shift-left** is the operational principle.
- **CISA Secure by Design** (2023, refreshed 2024 RSAC pledge - 100+ signatories) is the policy backdrop: manufacturers own the outcome.

**Graphic:** Two-tier diagram. Top tier: "SDLC practices (the human-judgment layer)" with the W / R / D icons inside. Bottom tier: "CI/CD pipeline (build, test, package, deploy)" with the T icon inside. NIST's Appendix B citation is the dividing line. SLSA badge on the build-platform box.

**Speaker notes:** The question this slide answers is "but our developers already do CI/CD - isn't that enough?" The pipeline is the *runway* for the SDLC. Without an SDLC defining what the gates need to enforce, you have a fast deployment pipeline that ships insecure code faster.

The point worth landing slowly is the carve-out. NIST 800-204D is one of the few places where a standards body is candid about what the pipeline *can't* do. Read their words carefully: practices PW.1 through PW.4 and PW.7 - secure design, threat modelling, software-reuse decisions, code review - "pertain to secure software design, review of the design, and software reuse." That's NIST's wording. The pipeline can't enact those activities; never could. Appendix B similarly carves out vulnerability response (RV.1 - RV.3) as "at the organization policy level."

Map this to our four assumptions: three of the four (Writer, Reviewer, Dependency) live in the carved-out human-judgment layer above the pipeline. Only the fourth (Tool determinism) rides on the pipeline itself - and even there, the pipeline only enforces *codifiable* aspects of tool integrity (version pinning, allowlists, signing). Residual judgment isn't pipeline material.

In Section 2 we'll see that AI compresses or removes exactly the W / R / D residual judgment that the pipeline was never going to do. That's why "more pipeline tooling" alone won't save you. The pipeline reinforces T - which it can - but the rest is restored elsewhere.

**Sources:**
- NIST SP 800-204D (Chandramouli, Kautz, Torres-Arias, Feb 2024), DOI https://doi.org/10.6028/NIST.SP.800-204D - landing page https://csrc.nist.gov/pubs/sp/800/204/d/final - PDF https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf
- SLSA v1.2 spec - https://slsa.dev/spec/v1.2/
- OWASP DevSecOps Guideline - https://owasp.org/www-project-devsecops-guideline/
- CISA Secure by Design - https://www.cisa.gov/securebydesign
- CISA Secure by Design pledge - https://www.cisa.gov/securebydesign/pledge

### Gamma brief

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

# Section 2 - How AI is breaking the SDLC

## Slide P2.1 (running-order #7) - From tool to author

- **"Vibe coding" - coined Feb 2025** by Andrej Karpathy: "fully give in to the vibes... forget that the code even exists"
- **Collins Dictionary Word of the Year 2025** (Nov 6, 2025): "the use of artificial intelligence prompted by natural language to assist with the writing of computer code"
- **Google, Q1 2026 earnings call**: **75%** of new code is AI-generated and engineer-approved - up from 50% in fall 2025 and 25% in 2024
- **Frontier labs sit higher**: Anthropic ~70-90% company-wide (per spokesperson, Jan 2026); senior engineers report personal workflows at ~100%
- *Floor: Microsoft repos at 20-30% AI-written (Nadella, Apr 2025) - already a year stale*

**Graphic:** A single trajectory line: 25% (2024) -> 50% (fall 2025) -> 75% (Q1 2026) at Google, with a shaded "frontier labs" band sitting above at ~70-100%. Karpathy quote pulled to the top-left; "Collins Word of the Year 2025" tag top-right. The Microsoft 30% sits as a small caption near the 2024 point - the historical floor.

**Speaker notes:** Twelve months ago "vibe coding" was a Karpathy tweet. By November it was the Collins Word of the Year. By Q1 2026, on an audited earnings call, Sundar Pichai said 75% of all new code at Google is AI-generated. That figure was 25% in 2024 and 50% in fall 2025. The slope is the story: 25 -> 50 -> 75 in two product cycles.

One nuance worth naming explicitly so nobody catches it as a gotcha: Google's 75% is AI-generated *and engineer-approved*. So the human is still in the loop - on paper. Hold that thought, because the assumption that the reviewer actually read the code is exactly one of the four assumptions we're about to take apart.

The frontier-lab numbers are softer-source - Boris Cherny on X, an Anthropic spokesperson clarifying 70-90% company-wide. Don't overclaim them. Use them as leading indicators: the people building the models run their workflows at the high end, and the rest of the industry is moving toward where they already are.

The takeaway is not the headline number. It's the trajectory and what it implies. Whatever your build pipeline looks like today, in twelve months it will look more like Google's than like the 2024 baseline. The assumptions we walk through next - writer, reviewer, dependencies, tools - were designed for a world where humans wrote the code. That world is being phased out, fast.

**Sources:**
- Karpathy origin / vibe coding overview - https://en.wikipedia.org/wiki/Vibe_coding
- Collins Word of the Year 2025 - https://www.collinsdictionary.com/woty
- Collins definition - https://www.collinsdictionary.com/dictionary/english/vibe-coding
- Pichai, Alphabet Q1 2026 earnings - https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2026/
- Pichai, Cloud Next 2026 - https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
- Anthropic / OpenAI frontier-lab figures (Cherny, Roon via Fortune, Jan 2026) - https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
- Nadella 30% - https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/

### Gamma brief

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

## Slide P2.2 (running-order #8) - What's actually in your build pipeline now

- **LLM** - a stateless next-token predictor (the brain). Each call is independent; statefulness is faked by replaying history. Output is sampled, so the same input can produce different outputs.
- **Harness** - the wrapper that turns prediction into action. Reads model output, executes tools, feeds results back. Cursor, Copilot, Claude Code, Cline.
- **MCP server** - how harnesses talk to your systems. Open standard for tool calls into GitHub, Slack, Postgres, JIRA. Tool descriptions are an executable surface (Hou et al. 2025).
- **RAG** - how AI features pull in your private data. Embedding model + vector DB lookup + LLM call in a single pass. Retrieved content lands in the same context window as your system prompt - no privilege separation.
- *Scoping note: today is build-time AI. Runtime AI is Part 2 of the series.*

**Graphic:** Four labelled boxes flowing left-to-right with arrows showing data flow. A subtle dotted boundary line shows "what the developer sees" (LLM + Harness) vs "what gets executed against your systems" (MCP + RAG).

**Speaker notes:** One slide covers what could fill an hour. The point is not to explain LLMs in depth - it's to give the audience a shared mental model so the rest of Section 2 lands concretely.

Four moving parts. The LLM is just a statistical next-token predictor - it doesn't reason, doesn't know facts, samples from a probability distribution. Each API call is independent; statefulness is faked by replaying the whole conversation back. Critical security point: there is no privilege separation between instructions and data inside the context window. They are the same string of text. That single fact is the root of half the threats we'll see in this talk and the next.

The harness is what turns prediction into action. It reads the model's output and decides whether to call your filesystem, your build tool, your shell. The harness has the privileges, not the model. There are coding harnesses - Cursor, Copilot, Claude Code, Cline - and agentic harnesses that run open-ended loops on developer machines. Each has its own trust-decision profile, and those decisions determine the blast radius.

MCP - Model Context Protocol - is the open standard for connecting harnesses to tools. Three years ago this category did not exist; today every coding harness ships with MCP integrations. The CISO-relevant single insight from Hou et al.'s threat model: LLMs treat tool descriptions as authoritative instructions, which means the metadata in an MCP server is an executable surface, not just documentation.

RAG - Retrieval-Augmented Generation - is how every "chat with your data" feature works. The user query goes to an embedding model and a vector DB lookup *first*, then the LLM sees query plus retrieved docs together in a single call. Anything an attacker can plant in your indexable corpus - an email, a wiki page, a public webpage your retriever crawls - lands inside the same context window as your system prompt.

These four are what's actually inside the AI dev tooling your engineers are using. Each is a separate attack surface. Specific incidents on each follow.

**Sources:**
- Hou, X., Zhao, Y., Wang, S., & Wang, H. (2025). *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions.* arXiv:2503.23278v3 - https://arxiv.org/abs/2503.23278
- Greshake et al. AISec 2023 (foundational on indirect prompt injection via retrieved content) - https://arxiv.org/abs/2302.12173
- Reddy & Gujral 2025, EchoLeak / CVE-2025-32711 - https://arxiv.org/abs/2509.10540

### Gamma brief

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

## Slide P2.3 (running-order #9) - Writer - the developer wrote it

- **Apiiro telemetry** (Fortune-50, 7,000+ devs, 62,000 repos): **10,000+ new findings/month** from AI-generated code by mid-2025; **10x in six months**
- **+322% privilege-escalation paths**; +153% architectural flaws; +40% secret exposures
- **41% of AI-generated backend code** ships with default-admin permissions when prompted naively (Backslash 2025)
- **Perry et al., ACM CCS 2023:** AI-assisted developers wrote less secure code on 4 of 5 tasks - **and were more likely to believe it was secure**
- *Pattern: shallow up, deep down - trivial errors fell, architectural and identity flaws exploded*

**Icon (bottom-right):** [**W**] R D T

**Graphic:** Hockey-stick chart of monthly findings (Dec 2024 - mid 2025) on the left. Bullets on the right. Apiiro source attribution.

**Speaker notes:** This is what happens when Assumption W breaks - the developer didn't really write it, didn't really read it, didn't really know what it does.

Apiiro's Fortune-50 telemetry is the cleanest enterprise signal we have. One Fortune-50 customer, 7,000 developers, 62,000 repositories - 10,000-plus new security findings per month from AI-generated code by mid-2025. Up 10x in six months. The directional caveat: this is one big data point, not a population estimate. The trend is the story.

The category breakdown matters more than the headline. Privilege-escalation paths up 322 percent. Architectural flaws up 153 percent. Secret exposures up 40 percent. Notice what *fell* - trivial syntax errors, missing semicolons, basic null checks. Those went down 76 percent. What rose was the deep stuff - the IAM scope decisions, the attack-path geometry, the credentials-in-the-wrong-place mistakes. Apiiro called this pattern "shallow up, deep down" and it's exactly right. AI fixes the surface; the depths go untended.

Default permissions matter too - Backslash showed 41 percent of naively-prompted backend code ships with default-admin permissions. The prompt is the control plane now. Your developers' prompt habits shape the vulnerability profile of what gets shipped. Backslash also showed Claude 3.7 went from 6/10 to 10/10 on secure-code generation when given security-focused prompts - the swing on prompt quality is enormous.

The Perry CCS 2023 finding is the one I most want this audience to internalise. AI-assisted developers wrote *less* secure code on four of five tasks - and were *more* likely to believe their code was secure. This isn't laziness. It's that LLM output reads as if a competent person wrote it. Reviewer instincts that work for human-written code don't transfer.

We're going to see this pattern recur through the next three slides. Each broken assumption combines a measurable degradation with a confidence gap.

**Sources:**
- Apiiro - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
- Apiiro companion - https://apiiro.com/blog/faster-code-greater-risks-the-security-trade-off-of-ai-driven-development/
- Backslash 2025 - https://www.backslash.security/press-releases/backslash-security-reveals-in-new-research-that-gpt-4-1-other-popular-llms-generate-insecure-code-unless-explicitly-prompted
- Perry et al., ACM CCS 2023 - https://arxiv.org/abs/2211.03622 (ACM https://dl.acm.org/doi/10.1145/3576915.3623157)

### Gamma brief

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

## Slide P2.4 (running-order #10) - Reviewer - the reviewer read it

- **DORA 2025** (n~5,000): PR size **+51.3%**; PR review time **+441%**
- 30% of developers distrust AI-generated code - but still merge it
- **Stack Overflow Feb 2026:** 84% use AI; only **29% trust it** (-11 pts YoY); 81% concerned about security
- Reviewer can't see the model, the prompt, the RAG context, or the tool calls the AI had access to
- *The bottleneck has moved - the reviewer is now the load-bearing role*

**Icon (bottom-right):** W [**R**] D T

**Graphic:** Side-by-side bar chart of PR-size and review-time deltas (the +441% bar drawn to scale - it dominates). Context bullets underneath.

**Speaker notes:** Assumption R - the reviewer read it - is the second to break, and it breaks because of mathematics, not negligence.

DORA 2025 is the load-bearing source. Roughly 5,000 developers across multiple organisations. Two numbers on the slide: PRs are 51 percent bigger and review time has stretched 441 percent. That is not a typo - it is five-and-a-half times as long to review a PR than the same team took before AI tools arrived. Productivity gains on the writing side are real - Cui et al. RCT shows +26% PRs per week with Copilot - but the cost has just shifted from authorship to review.

When PRs are bigger, more frequent, and structurally harder to read - because LLM-generated code reads as if a competent person wrote it but contains the architectural flaws Apiiro just showed us - reviewers do what humans always do under pressure. They rubber-stamp. The 30 percent of developers who self-report distrusting AI code still merge it. The trust gap doesn't translate into rejection because the rejection mechanism is review, and review capacity has not scaled with PR volume.

Stack Overflow's Feb 2026 survey is the supporting signal: 84 percent of developers use AI; only 29 percent trust it - down 11 points year over year. 81 percent are concerned about security. Use is up, trust is down. Your developers already know the tool is unreliable. The job is to make the review structure match the survey instinct - they don't need convincing, they need scaffolding.

The deeper problem is what reviewers can't see. They don't see the model that produced the code. They don't see the prompt the developer used. They don't see what the AI's RAG retrieved. They don't see which tool calls the agent made. They see a diff. We restore this in Section 3 - this is what AI-BOM is for.

**Sources:**
- DORA 2025 - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- Stack Overflow Feb 2026 - https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
- Cui et al. RCT (productivity context) - https://arxiv.org/abs/2302.06590
- METR Feb 2026 follow-up - https://metr.org/blog/2026-02-24-uplift-update/

### Gamma brief

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

## Slide P2.5 (running-order #11) - Dependency - the dependencies were vetted

- **Spracklen et al., USENIX Security 2025** - 576,000 samples, 16 LLMs studied
- Commercial LLMs **>=5.2%** hallucination rate; open-source **>=21.7%**; **205,474 unique fabricated package names**
- **43% of hallucinations recur across 10 prompt repeats** - perfect repeatability for an attacker
- **Lasso registered the hallucinated `huggingface-cli`** as an empty PyPI package: 30,000+ downloads in 3 months, including in Alibaba's GraphTranslator README
- *"Slopsquatting" coined by Seth Larson, Python Software Foundation*

**Icon (bottom-right):** W R [**D**] T

**Graphic:** Per-LLM hallucination-rate bar chart on the left. Three-step attack-flow diagram on the right (LLM hallucinates name -> attacker registers it on PyPI/npm -> developer's AI-suggested import installs malware). Use red arrows for the attack path.

**Speaker notes:** Assumption D - the dependencies were vetted - is the narrowest slot in the four-assumption frame, but uniquely AI-native. The threat didn't exist before LLMs.

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

## Slide P2.6 (running-order #12) - Tool - the tools were deterministic

- **LiteLLM** (Mar 24, 2026): backdoored 1.82.7 / 1.82.8 via Trivy in CI - **3.4M daily downloads**, 40,000+ in the exposure window
- 2026 CVEs in the AI tools themselves: **Cursor RCE** (CVE-2026-26268), **Copilot Reprompt** (CVE-2026-21516), **Claude Code CLI RCE** (CVE-2026-35021), **Windsurf MCP zero-interaction** (CVE-2026-30615)
- **Hou et al. 2025:** 16 MCP threat scenarios spanning the lifecycle (creation, deployment, operation, maintenance)
- **Prakash 2026 (AIP):** ~2,000 production MCP servers scanned, **all lacked authentication**
- **Vercel / Context AI** (Apr 20, 2026): AI-vendor breach pivots into customer environment

**Icon (bottom-right):** W R D [**T**]

**Graphic:** 8-tile incident grid, most recent on top. Each tile has a date stamp, vendor logo (where appropriate), and one-line consequence. Use a consistent severity colour scheme.

**Speaker notes:** Assumption T - the tools were deterministic - is the heaviest slot. Ten-plus distinct risk categories. I will walk the most important.

LiteLLM is the reference incident. March 24, 2026. The litellm package on PyPI - 3.4 million daily downloads - had two backdoored releases (1.82.7 and 1.82.8) published after the Trivy GitHub Action was unpinned in LiteLLM's CI. Forty thousand-plus downloads landed during the five-hour exposure window. The payload harvested SSH keys, cloud credentials, Kubernetes configs, shell history, and crypto wallets. This is the canonical AI-tool supply-chain attack and it's why dependency pinning is policy now, not guidance.

The CVE tile grid lists 2026 vulnerabilities in the AI dev tools themselves. Cursor RCE, Copilot Reprompt, Claude Code CLI RCE, Windsurf MCP zero-interaction. These are not theoretical. The pipeline runs AI tools that run AI tools - and those AI tools have remote code execution flaws. The blast radius is the developer endpoint with all its credentials.

Hou et al. 2025 is the most-cited threat-model work on MCP. They catalogue 16 attacker patterns across the full server lifecycle - tool poisoning, rug pulls, namespace typosquatting, cross-server shadowing, indirect prompt injection through retrieved data. The CISO-relevant single insight: tool descriptions are natural-language metadata that LLMs treat as authoritative, which means an attacker who controls a tool description can steer behaviour without touching the code.

Prakash's AIP paper scanned approximately 2,000 production MCP servers. None used authentication. Treat that as a directional signal - the methodology is sparse - but it lines up with what every practitioner finds when they look. This is developer-side shadow IT, mostly uninstrumented, and that is the gap.

Vercel and Context AI from April 2026 is the AI-vendor angle. A Lumma Stealer infection on a Context.ai employee was pivoted to a Google Workspace account, then into Vercel's environment. Customer environment variables and AI Office Suite OAuth tokens were exfiltrated and offered for USD 2M on BreachForums. The lesson: the AI tooling your build pipeline trusts is now an attack surface your supply-chain controls have to cover.

This layer was largely uninstrumented two years ago. We are catching up.

**Sources:**
- LiteLLM advisory - https://docs.litellm.ai/blog/security-update-march-2026
- Microsoft Security on Trivy/LiteLLM - https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
- Cursor CVE-2026-26268 - https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- Copilot Reprompt CVE-2026-21516 - https://www.paperclipped.de/en/blog/github-copilot-cve-2026-21516-reprompt-attack/
- Claude Code CLI CVE-2026-35021 - https://www.sentinelone.com/vulnerability-database/cve-2026-35021/
- "MCP by Design" supply-chain advisory - https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/
- Hou et al. 2025 - https://arxiv.org/abs/2503.23278
- AIP MCP scan paper (Prakash 2026) - https://arxiv.org/abs/2603.24775
- Vercel security bulletin - https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
- TechCrunch on Vercel/Context AI - https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/

### Gamma brief

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

# Section 3 - What to do

## Slide P3.1 (running-order #13) - Tooling - PR gates, AI-asset inventory, IDE boundary

- **AI-asset & MCP-server inventory** as the precondition for every other control - you cannot scan what you cannot see (the new shadow-IT discovery problem)
- **IDE-boundary controls** - inspect prompts, block secrets, govern context, allowlist tool calls. Hines et al. *Spotlighting* reduces prompt-injection ASR from >50% to <2%
- **PR gates fail-closed** - SAST + secret scanning + SCA on every AI-assisted PR; **block hallucinated imports** against a known-good registry allowlist
- **Pin AI tool versions**; treat MCP servers as third-party dependencies subject to existing controls
- *This is where pipelines reinforce T.*

**Icon (bottom-right):** W R D [**T**]

**Graphic:** Linear horizontal pipeline diagram with four labelled gates (asset inventory -> IDE boundary -> PR gate -> build gate). Use the same accent colour throughout to signal "pipeline-enforceable."

**Speaker notes:** Section 3 walks the four restorations starting with the one pipelines can do - tooling. This is the assumption pipelines were built for, and it's where the cleanest wins live.

Asset inventory first. You cannot scan what you cannot see. AI-asset and MCP-server discovery is the new shadow-IT discovery problem - the same 2010s-era playbook applies, just on new asset types. Every harness, every MCP server, every model endpoint, every coding assistant has to be inventoried before any other control matters.

IDE-boundary controls. Prompts leaving the developer endpoint should be inspectable; secrets in those prompts should be blocked; file context should be governed; tool calls should be allowlisted. Hines et al.'s Spotlighting paper is the academic anchor here - they reduce prompt-injection attack-success rate from over 50 percent to under 2 percent through delimiting, datamarking, and encoding. Applicable directly to prompt validation in the IDE plane.

PR gates. SAST, secret scanning, SCA on every AI-assisted PR - mandatory, fail-closed. Block hallucinated imports at CI by allowlisting against a known-good package registry. Veracode and Apiiro both report that the same controls applied universally reduce AI-introduced risk to roughly the human-only baseline. This isn't new tooling - it's the existing tooling applied without exception.

Pin AI coding tool versions. Treat MCP servers as third-party dependencies subject to your existing controls. Hou et al. catalogue 57 MCP-specific threats in their full work, and Invariant Labs has demonstrated rug-pull tool poisoning where benign tool descriptions silently mutate on second launch. Real attacks, fixable with version pinning and intake review.

Crucially, this slide is short for a reason. Pipelines reinforce T. They cannot restore W, R, or D. The next four slides are what actually restores those.

**Sources:**
- Hines et al. Spotlighting - https://arxiv.org/abs/2403.14720
- Hou et al. MCP Landscape - https://xinyi-hou.github.io/files/hou2025mcp_1.pdf
- Invariant Labs MCP tool-poisoning / rug-pull - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks

### Gamma brief

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

## Slide P3.2 (running-order #14) - Process - the human-judgment restorations

- **Mandatory AI-usage disclosure at PR level** - the cheapest, highest-leverage control in the talk
- **AI-BOM at PR level** - which model, which tools, which prompts, which packages. Extends SBOM to model and tool provenance
- **Third-party AI-tool intake review** before granting Workspace / Slack / GitHub access (the Context AI question)
- **AI-specific branch in IR playbook** - what happens when an AI-generated PR introduces a CVE; when an upstream AI tool is compromised; when a model provider rotates a key
- *Aligns with NIST SP 800-218A practice PO.1 and NIST AI 600-1 MS-2.6, MG-3.1/3.2*

**Icon (bottom-right):** [**W**] [**R**] [**D**] T

**Graphic:** Realistic mockup of a PR description in GitHub or GitLab style, with the two new fields highlighted (AI-assisted? / AI-BOM attached?). Process changes as a side panel.

**Speaker notes:** Process is where W, R, and D restoration starts. None of these requires new spend. They require new policy and new discipline.

Mandatory AI-usage disclosure at PR level is the single highest-leverage control in this talk. You cannot improve what you cannot see. Adding two fields to your PR template - "AI-assisted? yes/no/which tool" and "AI-BOM attached?" - costs nothing and changes everything downstream. Reviewers know what they're reading. Metrics become possible. Audit trails extend to authorship. This aligns with NIST SP 800-218A practice PO.1 - define security requirements - and was recommended in NIST AI 600-1 MG-3.1/3.2.

AI-BOM is the natural extension of SBOM. Your SBOM tells you which packages shipped. Your AI-BOM tells you which model wrote each PR, which version, with what system prompt, what tool calls, what RAG sources. The spec is maturing through OWASP and Linux Foundation work - it's not yet locked, but the categories are stable enough to start collecting now.

Third-party AI-tool intake review is the Context AI question. Before anyone grants Workspace, Slack, or GitHub access to a new AI tool, that tool gets reviewed - vendor security posture, data-handling commitments, breach history, OAuth-scope justification. Vercel/Context AI is the canonical case study. Every CISO has a Context-AI-shaped supplier in their build pipeline.

AI-specific branch in your IR playbook. What happens when an AI-generated PR introduces a CVE? When an upstream AI tool is compromised - LiteLLM-style? When a model provider rotates a key? These are different from your existing playbook because the actor on the other side might be a model, not a person. The playbook needs an AI section.

These are the cheap controls. Disclosure first. Provenance second.

**Sources:**
- NIST SP 800-218A - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST AI 600-1 - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NIST SP 800-204D - https://csrc.nist.gov/pubs/sp/800/204/d/final
- SLSA v1.2 - https://slsa.dev/spec/v1.2/

### Gamma brief

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

## Slide P3.3 (running-order #15) - Culture

- **No merge until reviewed by someone who did not write the prompt**
- **Pair-review for AI-generated code** - one used AI, one did not
- **Ownership is human**, regardless of what wrote it. The name on the PR owns the artefact.
- **Reward catches, not velocity.** A caught hallucination is the same artefact as a caught bug.
- *Sandoval et al., USENIX Security 2023, "Lost at C": review interaction is the primary moderator of LLM-assisted bug rate*

**Icon (bottom-right):** W [**R**] D T

**Graphic:** Four rule-cards stacked vertically. Subtle "two developers reviewing together" line illustration on the right.

**Speaker notes:** Culture is where R - the reviewer reflex - gets restored. This isn't new tooling either. It's how your team behaves around AI-generated code.

The first rule is simple. No merge until reviewed by someone who did not write the prompt. If the developer who wrote the prompt is also the only person who reads the PR, the review collapses into self-review. The reviewer has to be somebody else. This sounds obvious; it's not happening in most orgs today.

Pair-review for AI-generated code goes one step further. One developer who used AI plus one who did not. The non-AI reviewer brings the unmodified instinct of "wait, why is this here?" - which is exactly what gets eroded when both sides of the PR are LLM-mediated.

Ownership is human, regardless of what wrote it. The name on the PR owns what it does, full stop. AI is not an excuse, not a co-author for liability purposes, not a reason to disclaim a vulnerability. If your name is on the merge, you signed off.

Reward catches, not velocity. A caught hallucination, a caught architectural flaw, a caught secret leak - those are the same artefact as a caught bug. Your performance metrics, your team-level dashboards, your engineering-leadership reviews - if they reward merge rate without rewarding catch rate, you're training the wrong reflex.

The academic anchor is Sandoval et al., USENIX Security 2023, "Lost at C". They demonstrate that review interaction - the actual back-and-forth between author and reviewer - is the primary moderator of LLM-assisted bug rate. More interaction, fewer bugs. Less interaction, more bugs. Culture is what determines how much interaction happens.

**Sources:**
- Sandoval et al., "Lost at C", USENIX Security 2023 - https://arxiv.org/abs/2208.09727

### Gamma brief

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

## Slide P3.4 (running-order #16) - Organisation

- **Name an owner**: AppSec + engineering lead, **not product**
- **Joint governance body, weekly cadence** - 49% of orgs run 5+ AI tools; quarterly cannot keep up
- **Redistribute review workload** - seniors review more, write less. Review capacity is the new bottleneck.
- **Hire and grade for the review reflex**, not the typing reflex

**Icon (bottom-right):** W [**R**] D T

**Graphic:** Simplified org-chart fragment with the joint AppSec + engineering owner highlighted. Bullets to the right.

**Speaker notes:** Organisation is where R gets restored structurally. This is the engineering-org slide, not the GRC slide.

First, name an owner. AppSec plus engineering, jointly. Not product. Product owners optimise for shipping; security and engineering optimise for sustainable delivery. The joint owner has the authority to set policy, gate merges, and reshape review workflows. Without a named owner, AI-tooling decisions get made by whoever installed the latest tool.

A joint governance body running on a weekly cadence. GitLab's DevSecOps 2025 survey found 49 percent of organisations run five or more AI tools. The tooling landscape changes faster than that. Quarterly governance bodies cannot keep up. Weekly might still be too slow but it's the floor.

Redistribute the review workload. This is the structural change most engineering orgs haven't internalised yet. AI compresses authorship time. It does not compress review time - in fact it expands it (DORA's +441%). So your senior engineers, who used to spend most of their time writing, now need to spend most of their time reviewing. Seniors review more, write less. Junior and mid-level engineers do more authorship - with AI assistance - and seniors apply the residual judgment AI cannot do.

This has implications for hiring and grading. The performance criteria that mattered most for senior engineers two years ago - architecture, system design, deep technical writing - still matter, but they get exercised increasingly through review rather than authorship. Hire for the review reflex. Grade for it. Promote on it.

ISACA and ISO 42001 are the GRC framing - those are covered in adjacent webinars. What gets undercovered is exactly this: the engineering-org change. Review capacity is now the bottleneck, and that affects hiring, headcount mix, and how you grade seniority.

**Sources:**
- GitLab DevSecOps 2025 - https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/
- ISO/IEC 42001:2023 - https://www.iso.org/standard/42001

### Gamma brief

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

## Slide P3.5 (running-order #17) - Governance

- **Anchor on NIST SP 800-218A** - the SDLC-specific GenAI profile. The spine.
- Layer **NIST AI 600-1** for risk taxonomy; **NCSC + CISA Secure AI Development** for lifecycle hooks; **OWASP Top 10 for LLM Applications**
- **Metrics that matter:** AI-assisted PR rate; vuln rate AI vs human; secret exposures from AI; MTTR for AI-introduced vulns
- **Multi-signal correlation** - endpoint + exposure + identity - to detect rogue dev-side AI agents

**Icon (bottom-right):** [**W**] [**R**] [**D**] [**T**]

**Graphic:** Stacked framework layers on the left (SSDF GenAI profile at the base, then AI 600-1, then NCSC/CISA, then OWASP). Metrics as a clean bullet list on the right.

**Speaker notes:** Governance is the audit-layer restoration. This is the slide that covers all four assumptions at once - because governance is where you measure whether the other three slides actually happened.

The anchor is NIST SP 800-218A - the SDLC-specific GenAI profile. This is the only framework that maps cleanly onto the build pipeline with AI in mind. It extends SP 800-218 (the SSDF) with GenAI-specific practices. If you are building a new AI-security programme today, this is your spine.

The AI Risk Management Framework - NIST AI 600-1 - layers above for the risk taxonomy. NCSC and CISA's joint Guidelines for Secure AI System Development covers the lifecycle hooks. OWASP's Top 10 for LLM Applications gives you the threat catalogue at the application layer. These four together are the regulatory and standards stack a UK or EU CISO will be expected to demonstrate alignment with.

The metrics matter. The four on the slide - AI-assisted PR rate, vuln rate AI vs human, secret exposures from AI, MTTR for AI-introduced vulnerabilities - are the minimum viable dashboard. They tell you whether your disclosure policy is working (AI-PR rate growing), whether AI-generated code is materially worse (vuln rate AI vs human), whether the prompt-engineering controls are working (secret exposures), and whether your IR is keeping up (MTTR). Without these you cannot manage the programme.

Multi-signal correlation. Endpoint signals plus exposure signals plus identity signals. Pure runtime detection misses build-time precursors - by the time the AI-introduced vuln shows up at runtime, it's already in production. Correlating endpoint events (developer machine, IDE state) with exposure events (PR-level findings) with identity events (who has access to which tooling) is how you see a rogue AI agent in the build pipeline before it hits production.

This is the slide that gets reported to the board.

**Sources:**
- NIST SP 800-218A - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST AI 600-1 - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NCSC + CISA Secure AI Development - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf
- OWASP Top 10 for LLM Applications - https://genai.owasp.org/llm-top-10/

### Gamma brief

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

## Slide P3.6 (running-order #18) - Restoring the four

Four-row restoration table - one row per broken assumption.

| Icon | Assumption broke | The restoration |
|---|---|---|
| **W** | The developer wrote it | AI-usage disclosure at PR level + AI-BOM (model, tools, prompts, packages) |
| **R** | The reviewer read it | Pair review on AI-assisted PRs; redistribute review capacity (seniors review more, write less) |
| **D** | The dependencies were vetted | Allowlist your package registry at CI; block hallucinated imports; pin and verify |
| **T** | The tools were deterministic | Inventory AI assets and MCP servers; pin AI-tool versions; intake-review every new AI tool |

Cross-cutting move: anchor the programme to **NIST SP 800-218A** and report the four restorations as the metrics that matter.

*Closing aphorism (full-width, italic):* **"Aviation didn't get safe by trusting one agent. It got safe by trusting a system. These four restorations are software's equivalent."**

**Icon (bottom-right):** [**W**] [**R**] [**D**] [**T**]

**Graphic:** Clean four-row table with the W/R/D/T icons on the left. Use the same icon design as Slide P1.3 - this is the bookend. Closing aphorism in italic across the bottom.

**Speaker notes:** This is the close. Each row pairs a broken assumption from Slide P1.3 with one restoration that starts to fix it. None of these requires new spend. They require new policy and new attention.

Walk the rows briefly:
- **W:** Disclosure plus AI-BOM. You cannot improve what you cannot see.
- **R:** Pair review plus capacity redistribution. The reviewer is the load-bearing role; staff it like one.
- **D:** Allowlist plus pin plus verify. Slopsquatting is the most fixable problem in the talk.
- **T:** Inventory, pin, intake-review. The pipeline-enforceable assumption gets pipeline controls.

The cross-cutting move is to anchor your AI-security programme to NIST SP 800-218A and report these four as your top-line metrics. That gives you a defensible audit story and aligns you with the regulatory floor we named in Slide P1.1.

**Speaker beat at the close - the transitional counter-argument:**

> Honest counter-argument worth naming: maybe this is transitional. Maybe AI gets so good these concerns evaporate. The aviation analogy is real - modern airliners fly under heavy autopilot, and senior pilots will tell you they trust the autopilot more than they trust most humans. Boris Cherny, who created Claude Code, runs hundreds of agents full-time with no human in the loop. Maybe that's where software lands.
>
> Three reasons I don't bank on it:
>
> 1. **That's the frontier, not the median.** Boris Cherny is one of a handful of people in the world running a fleet of agents safely. Your developers are not Boris. The median enterprise has to defend with the median competence available now.
> 2. **You have to defend now, not in five years.** Even if AI is autonomous-grade by 2030, the breaches between now and then are real and your name is on them.
> 3. **Aviation didn't get safe by trusting one agent.** Autopilots fly safely inside a *system* - checklists, redundancy, air-traffic control, regulatory certification, mandatory incident reporting. The system doesn't trust any single agent, including the human pilot. The four restorations on this slide are software's equivalent of that system. They will outlast whatever the model does next.

**Sources:**
- NIST SP 800-218A - https://csrc.nist.gov/pubs/sp/800/218/a/final
- All restoration sources cited on the relevant Section 3 slides above.

### Gamma brief

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

## Slide P-Close (running-order #19) - Q&A and Part 2

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
