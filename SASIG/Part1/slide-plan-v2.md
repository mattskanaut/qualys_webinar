# Part 1 - Slide Plan (v2, structure-aligned)

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Target:** 25 slides, 55 min content + 5 min Q&A
**Style:** brief, high-level. Speaker carries the content; slides anchor.
**Structure:** mirrors `part1-sdlc.md` section-by-section. One or two slides per sub-segment.

**Spine (named on Slide 10, recurring icons throughout):** AI broke the four assumptions that secure software development was built on - the developer wrote it (W), the reviewer read it (R), dependencies were real (D), and the tools were inspectable (T). Segment 2 walks through how each assumption breaks in the data; Segment 3 walks through how to restore each one. Slide 24 closes with a four-row restoration map.

**Operational through-line (close):** *You cannot govern what you cannot inventory.* Inventory is how you restore provenance to the four assumptions. This is also the differentiator from the adjacent SASIG webinars - Redflags own the human layer, Wavestone owns the runtime-agent layer, this talk owns the build-time / artefact layer. Qualys's TotalAI / MCP-discovery / AI-BOM / TruRisk positioning lines up with this thread organically.

**Icon convention:** four small icons (W / R / D / T) appear in the bottom-right of every Segment 2 and Segment 3 slide, with the relevant icon(s) highlighted. Introduced on Slide 10. Designer note: pick one consistent icon style (e.g. line-art glyph) and one highlight treatment (e.g. brand colour fill vs greyed outline).

---

## Slide 1 - Title and the promise

- The New SDLC: Security When Every Developer Writes With AI
- *Subtitle: When the four assumptions of secure development all break at once*
- The New Normal: Software, Security and the AI Stack - Part 1 of 2
- Non-product. 40% problem, 60% what to do. Every stat sourced.

**Graphic:** Series wordmark, three-icon strip (shield/clock/book). Subtitle in smaller type below the main title.

**Speaker notes:** Welcome. Earn the room - say the non-product promise out loud. Tell them slides are deliberately light; the bibliography lands in their inbox. The subtitle is the spine: four assumptions broke; we name them, walk the data, and finish with how to restore them.

---

## Slide 2 - Where this talk sits

- Build-time AI risk: code, prompts, packages, models, IDEs, CI/CD, MCP servers
- Runtime AI risk: prompt injection, agent identity, runaway autonomy
- Workforce AI risk: shadow ChatGPT, data leakage, behaviour change
- Today: build-time. Part 2: runtime.

**Graphic:** Three-layer diagram - Workforce / Build-time / Runtime - with this talk highlighted on Build-time.

**Speaker notes:** Position the talk between the two adjacent SASIG sessions on AI - one on workforce behaviour, one on agent identity and runtime - without naming them. Build-time is the layer between, where AI is now writing the code that runs the rest. This is where most of your risk now compounds, and where the data is freshest.

---

## Slide 3 - Opening hook - real CVEs in real repos

- Georgia Tech Vibe Security Radar (Apr 2026): 6 / 15 / 35 AI-attributed CVEs in Jan / Feb / Mar 2026; 74 lifetime; 27 traceable to Claude Code
- Endor Labs / CMU Agent Security League (Apr 2026): 200 real OSS tasks, top agent 84.4% functional but only 17.3% security pass
- Fu et al., ACM TOSEM 2025: 29.5% of Python and 24.2% of JS Copilot snippets in real GitHub projects had at least one CWE

**Graphic:** Vibe Security Radar monthly CVE-attribution chart.

**Speaker notes:** Real CVEs in real repos, not benchmarks. The Georgia Tech work walks fixing-commits back through git history and identifies when an AI tool wrote the original vulnerable code. The slope is the story. **Now you're probably wondering how this is even possible. The next four slides give you the mental model - what an LLM actually is, what a harness is, what an MCP server is, and how RAG works. Then we come back to one more recent incident and walk the data.**

**Sources:**
- Georgia Tech Vibe Security Radar - https://news.research.gatech.edu/2026/04/13/bad-vibes-ai-generated-code-vulnerable-researchers-warn (live https://vibe-radar-ten.vercel.app/)
- Endor Labs / CMU Agent Security League - https://www.endorlabs.com/research/ai-code-security-benchmark
- Fu et al., ACM TOSEM 2025 - https://dl.acm.org/doi/10.1145/3716848 (preprint https://arxiv.org/abs/2310.02059)

---

## Slide 4 - What an LLM actually is

- A statistical next-token predictor trained on internet-scale text - not a knowledge base, not a reasoning engine
- Stateless: each API call is independent; statefulness is faked by replaying the whole conversation back in the next call
- The "context window" is the input - system prompt + user prompt + retrieved data + tool outputs + history all share the same channel
- Output is sampled from a probability distribution, so the same input can produce different outputs
- Security implication: there is no privilege separation between instructions and data inside the context window - that is why prompt injection works at all

**Graphic:** Diagram showing context-window contents (System / User / Retrieved / Tools / History) flowing into a single LLM box, single arrow out.

**Speaker notes:** Most CISOs think "the AI" is one thing. It is actually four things stacked: a stateless predictor, a wrapper that simulates state, a tool-using harness on top, and a retrieval system feeding it private data. Today we name all four. Crucially: there is no OS-level privilege separation between instructions and data inside the context window - they are the same string of text. That single fact is the root of half the threats we will see in this talk and the next.

---

## Slide 5 - Harnesses: the wrapper that turns prediction into action

- A harness wraps the model with scaffolding: prompts, tool calls, memory, control flow, retry logic
- Developer / coding harnesses: GitHub Copilot, Cursor, Claude Code, Cline, Aider, Windsurf
- Agentic harnesses (autonomous loops): Devin, Manus, Claude Computer Use, OpenAI Operator / ChatGPT Agent
- Agent frameworks (build-your-own): LangGraph, Microsoft AutoGen, CrewAI, LlamaIndex, Anthropic Agent SDK
- An agentic harness runs a loop: read model output -> execute tools -> feed results back -> repeat. The harness has the privileges, not the model
- Security implication: the harness is your new attack surface - 2026 has already seen RCEs in Cursor, Copilot, Claude Code, and Windsurf

**Graphic:** Stacked-layer diagram - Model -> Harness (with tools, memory, loop) -> Tools -> Filesystem / Network. Trust boundaries marked. Side panel: three harness families (coding / autonomous / framework).

**Speaker notes:** Harnesses are why you can no longer say "the AI generated the code." The model emits tokens; the harness reads those tokens and decides whether to call your filesystem, your build tool, your shell. There are three families to keep separate in your head: coding harnesses live in the developer's IDE; autonomous agentic harnesses run open-ended loops on a developer machine or VM; agent frameworks let your engineers build your own. Each family has its own trust-decision profile, and those decisions determine the blast radius. We return to specific harness CVEs later in the deck.

---

## Slide 6 - MCP servers: how harnesses talk to systems

- Model Context Protocol - Anthropic-led, broadly adopted by 2026 - the open standard for connecting harnesses to tools, data, and services
- Architecture: harness (client) -> MCP server (process) -> external system (GitHub, Slack, Postgres, JIRA, internal API). Three primitives: tools (actions), resources (read-only data), prompts (templates)
- Hou et al. 2025: 16 MCP threat scenarios across 4 attacker types and the full server lifecycle - creation, deployment, operation, maintenance. Named attacks include tool poisoning, rug pulls, namespace typosquatting, cross-server shadowing, installer spoofing, indirect prompt injection
- Distribution is fragmented: no official marketplace; 26 third-party directories catalogued; in a 300-server sample from MCP.so, ~16% were false positives or abandoned (Hou et al. 2025)
- Prakash 2026 (AIP paper): a scan of approximately 2,000 production MCP servers found all lacked authentication
- Security implication: LLMs treat tool descriptions as authoritative instructions, so the metadata in an MCP server is an executable surface - not just documentation

**Graphic:** Flow diagram - Cursor / Claude Code (harness) -> MCP server (process) -> GitHub / Slack / Postgres.

**Strapline (inset on the slide):** *Tool descriptions are an executable surface (Hou et al. 2025). ~2,000 production MCP servers scanned: none authenticated (Prakash 2026).*

**Speaker notes:** Three years ago this category did not exist. Today every coding harness ships with MCP integrations. Hou et al. is the most-cited threat-model work on MCP - the CISO-relevant insight is that the threat surface spans the whole lifecycle: malicious creation (poisoned tool descriptions, namespace typosquatting), compromised deployment (installer spoofing), operational attacks (cross-server shadowing, tool-chaining abuse, indirect prompt injection through retrieved data), and maintenance failures (privilege persistence, configuration drift). The most CISO-relevant single finding: tool descriptions are natural-language metadata that LLMs treat as authoritative, which means an attacker who controls a tool description can steer behaviour without touching the code. A separate paper - Prakash's AIP work - scanned ~2,000 production MCP servers and found none used authentication; treat that as a directional signal (the methodology is sparse) but it lines up with what every practitioner finds when they look. **Scoping note for the room:** today we are talking about developer-side MCP - tool discovery and inventory inside the build pipeline. The runtime IAM angle for autonomous agents is a separate session's territory.

**Sources:**
- Hou, X., Zhao, Y., Wang, S., & Wang, H. (2025). *Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions.* arXiv:2503.23278v3. https://arxiv.org/abs/2503.23278
- Prakash, S. (2026). *AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A.* arXiv:2603.24775. https://arxiv.org/abs/2603.24775 (~2,000 MCP servers scanned, all lacked authentication)
- Invariant Labs MCP tool-poisoning / rug-pull demos - https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks

---

## Slide 7 - RAG: how AI features pull in your data

- Retrieval-Augmented Generation - the standard pattern for getting your private data into an AI feature without retraining the model
- The user query does NOT go to the main LLM first - it goes to a retriever, then the LLM sees query + docs together in a single call
- Already pervasive in dev tooling: codebase search in IDEs, doc-question agents, internal-API copilots
- Security implication: retrieved content is untrusted input but lands in the same context window as your system prompt and user query - the LLM cannot tell trusted from untrusted

### How the flow actually works (canonical RAG)

1. **User submits query** -> handed to the RAG orchestrator, not to the LLM
2. **Query is embedded** by a small embedding model (different from the main LLM - much cheaper, just turns text into a vector)
3. **Vector DB search** finds the top-K documents whose embeddings are closest to the query embedding (pure similarity search, no LLM involved)
4. **Top-K docs come back** to the orchestrator
5. **Assembly:** orchestrator concatenates `[system prompt] + [retrieved docs] + [user query]` into a single string
6. **Single LLM call** with that combined string as input - the LLM sees everything at once and generates the answer

The LLM is invoked **once**, after retrieval has happened. It never sees the query in isolation.

**Graphic:** Two-column layout.

- **Left column - data plane (build-time):** documents -> embedding model -> vector DB. Label: "you build this once, then keep it updated."
- **Right column - query plane (runtime):** user query -> embedding model -> vector DB lookup -> top-K docs.
- **Centre / bottom:** the assembled LLM context window box, with three colour-coded inputs (green system prompt, yellow user query, red retrieved docs) all flowing into one LLM, one answer out.
- **Annotation arrow:** "No channel separation - red, yellow, green all arrive as one string."

ASCII reference (for the designer):

```
                                                  +------------------+
[User query] ----+---->  [Embedding model] ---->  |  Vector DB       |
                 |                                |  (your private   |
                 |                                |   corpus,        |
                 |                                |   pre-embedded)  |
                 |                                +--------+---------+
                 |                                         |
                 |                          top-K matching documents
                 |                                         |
                 v                                         v
              +----------------------------------------------------+
              |        Single LLM input (the "context window")     |
              |                                                    |
              |   [System prompt]                                  |
              |   [Retrieved doc 1]  <-- attacker-controllable     |
              |   [Retrieved doc 2]  <-- attacker-controllable     |
              |   [Retrieved doc K]  <-- attacker-controllable     |
              |   [User query]                                     |
              +-------------------------+--------------------------+
                                        |
                                        v
                                    [LLM] ---> [Answer]
```

**Speaker notes:** RAG is how every "chat with your data" feature works under the hood. The flow is often misunderstood: the user query does not go to the main LLM first - it goes to an embedding model, then a vector DB lookup, and only then does the main LLM see anything, in a single call that already contains the retrieved docs alongside the query. That single-call assembly is the security crux. Everything inside the dotted "context window" box arrives at the LLM as one undifferentiated string. The LLM has no mechanism to tell which lines are trusted system instructions, which are semi-trusted user input, and which are untrusted retrieved content. Anything an attacker can plant in your indexable corpus - an email, a wiki page, a document, a public webpage your retriever crawls - can land inside the same box as your system prompt. This is exactly how zero-click attacks like EchoLeak (Microsoft 365 Copilot, June 2025) work. RAG is a build-time concern (you build the retriever and the index) and a runtime concern (queries go in, attacker text comes back). We will return to it in Part 2.

**Sources:**
- Greshake et al. AISec 2023 (foundational on indirect prompt injection via retrieved content) - https://arxiv.org/abs/2302.12173
- Reddy & Gujral 2025, EchoLeak / CVE-2025-32711 (real-world zero-click via RAG) - https://arxiv.org/abs/2509.10540

---

## Slide 8 - Live poll

- Do you have an inventory of AI assets in your build pipeline?
- Tools, models, MCP servers, AI-attributed PRs - yes / partial / no / not sure

**Graphic:** Poll widget placeholder.

**Speaker notes:** Most rooms answer "partial" or "no." That answer is the launching point for the rest of the hour - and the through-line: you cannot govern what you cannot inventory. Now you have the mental model for what the inventory has to cover.

---

## Slide 9 - Reality check - the AI tooling supply chain

- Vercel / Context AI (April 20, 2026): Lumma Stealer on a Context.ai employee, pivot Context -> Google Workspace -> Vercel; OAuth tokens for AI Office Suite users sold for USD 2M on BreachForums
- Lesson: the AI tooling your build pipeline trusts is now an attack surface

**Graphic:** Three-step attack-flow arrow diagram.

**Speaker notes:** Now you have the framing, the concepts, and a recent enterprise breach to anchor against. The point of this slide is not "this vendor was bad." Every CISO has a Context-AI-shaped supplier in the build pipeline. The question is: what does your AI-tool intake review look like, and when did you last run it. **This is the bridge to the data: the next slide names what just broke.**

**Sources:**
- Vercel security bulletin - https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
- TechCrunch - https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/
- Trend Micro - https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html

---

## Slide 10 - What just broke - four assumptions

- **Assumption 1 - The developer wrote it.** So you could trust the developer's judgement and accountability. They now accept suggestions from a model, often without reading them deeply
- **Assumption 2 - The reviewer read it.** So you could trust the review. PRs are 51% bigger and review takes 441% longer (DORA 2025) - reviewers are rubber-stamping
- **Assumption 3 - Dependencies were real.** So you could trust the SBOM. Packages get hallucinated and registered by attackers
- **Assumption 4 - The tools were inspectable.** So you could audit the pipeline. Cursor / Claude Code / Copilot / MCP servers are opaque processes with developer-level privileges - and they get RCEs
- *Builds on Shostack's trust-boundary work in threat modelling, SLSA's "trust assumptions" language for build provenance, in-toto's supply-chain provenance model, and the implicit assumptions baked into NIST SSDF practices - extended across the modern SDLC*
- Every control in your secure-development programme depended on at least one of these. Today they all just broke

**Graphic:** Four-quadrant card. Each quadrant has a labelled icon (Writer / Reviewer / Dependency / Tool) and a one-line statement of what broke. This is the **icon legend** for the rest of the deck - the same four icons appear bottom-right of every Segment 2 and Segment 3 slide, with the relevant icon(s) highlighted.

**Icon set introduced (used in lower-right of subsequent slides):**

| Icon | Assumption | One-word handle |
|---|---|---|
| W | 1 - The developer wrote it | **Writer** |
| R | 2 - The reviewer read it | **Reviewer** |
| D | 3 - Dependencies were real | **Dependency** |
| T | 4 - The tools were inspectable | **Tool** |

**Speaker notes:** This is the spine of the talk. Walk it slowly. For each assumption, name what it underwrote in the old SDLC (developer accountability, code review, SBOMs, tool audits). Then name what broke. Don't go deep on the data here - that's the next two segments. End with the through-line: every control you currently rely on depended on at least one of these four assumptions; we're going to walk through where each break shows up, and then how to restore them. *This is a working synthesis I'm proposing for this audience, not a published model - the individual claims trace to NIST SSDF, SLSA, threat-modelling work and the empirical literature; the four-assumption packaging is mine.*

**Sources (anchoring frameworks):**
- Adam Shostack - *Threat Modeling: Designing for Security* (Wiley, 2014). Trust-boundary framework. Author site: https://shostack.org/. Book: https://shostack.org/books/threat-modeling-book
  - *Why relevant: trust boundaries are the conceptual ancestor of "trust assumptions" - when an AI harness sits between the developer and the code, it is a new trust boundary that did not exist before. Assumptions 1 (Writer) and 4 (Tool) are the trust-boundary question reframed.*
- Threat Modeling Manifesto (Shostack, Tarandach et al.) - https://www.threatmodelingmanifesto.org/
  - *Why relevant: frames "what can go wrong" as a continuous practice rather than a one-off exercise. Each of the four broken assumptions is a threat-model premise that has just changed and now needs re-examination.*
- SLSA (Supply-chain Levels for Software Artifacts) v1.2 - explicit "trust assumptions" language for build provenance. https://slsa.dev/spec/v1.2/ (threats overview https://slsa.dev/spec/v1.2/threats-overview)
  - *Why relevant: SLSA literally enumerates trust assumptions in the build pipeline ("build platform is honest", "source is authenticated", etc.). Assumptions 3 (Dependency) and 4 (Tool) sit directly on top of SLSA's framework - and AI just invalidated several of them.*
- in-toto - supply-chain provenance / trust framework. https://in-toto.io/. Founding paper (Torres-Arias et al., USENIX Security 2019) - https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias
  - *Why relevant: in-toto formalises "who did what to which artifact" across the supply chain. Assumption 1 (Writer - who wrote the code) and Assumption 3 (Dependency - where the package came from) both depend on the provenance chain that in-toto encodes; AI breaks that chain at the authorship step.*
- NIST SP 800-218 (SSDF v1.1) - the practices that operationalise these assumptions across the SDLC - https://csrc.nist.gov/pubs/sp/800/218/final
  - *Why relevant: SSDF practices map to all four assumptions - PO.1 (define security requirements) and the developer-accountability premise; PW.7 (review and analyse code) for the reviewer assumption; PW.4 (reuse secure components) for dependencies; PO.3 (implement supporting toolchains) for tool integrity.*
- NIST SP 800-204D (CI/CD supply-chain integration) - https://csrc.nist.gov/pubs/sp/800/204/d/final
  - *Why relevant: directly addresses Assumptions 3 (Dependency) and 4 (Tool) through reproducible builds, signed artifacts, attestation. Where SSDF is generic, 800-204D is the operational manual for the build pipeline that AI tools now sit inside.*
- Saltzer & Schroeder, "The Protection of Information in Computer Systems" (Proceedings of the IEEE, 1975) - foundational design principles including least privilege and complete mediation; underpins the inspectable-tools assumption - https://www.cs.virginia.edu/~evans/cs551/saltzer/
  - *Why relevant: their "complete mediation" principle requires every access to be checked - which is precisely what breaks when an AI tool has un-mediated filesystem and tool-call access (Assumption 4). "Least privilege" similarly underpins why over-permissioned MCP servers are an architectural failure, not just a configuration mistake.*
- Optional deeper cut: Dan Geer on trust and monoculture in software ecosystems - https://geer.tinho.net/
  - *Why relevant: when the same handful of AI assistants writes code across the industry, a single weakness in one model affects the entire population - the monoculture argument applied to AI authorship. Cross-cutting risk that amplifies all four broken assumptions, but particularly Assumption 1 (Writer).*

---

# Segment 1 - What has changed

## Slide 11 - Adoption is near-universal in the enterprise

- Microsoft FY26 Q2 (Jan 28, 2026): 4.7M paid Copilot subscribers (+75% YoY); ~90% of Fortune 100
- DORA 2025 (Sept 2025, n~5,000): 90% of devs use AI at work; 65% rely on it heavily
- McKinsey 2026 (Feb 2026, 4,500 devs / 150 enterprises): 90%+ of software teams use AI; ~6 hrs/week saved
- Microsoft (Nadella, Apr 2025): 20-30% of code in Microsoft repos is now AI-written

**Graphic:** Three-column number card (4.7M / 90% / 90%+) with logos.

**Speaker notes:** Three independent 2025-2026 sources, all converging on near-universal in the enterprise. The headline numbers here are deliberately developer-cohort signals - paid Copilot subscriptions, dev-team adoption, hours-saved-per-developer - not generic "X% of CISOs lack AI visibility" survey framing. Microsoft's audited revenue makes this the strongest possible primary signal. Take the "AI is in your stack" framing as established and move on.

**Sources:**
- DORA 2025 - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (announcement https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- McKinsey - https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development
- Stanford HAI 2026 AI Index - https://hai.stanford.edu/ai-index/2026-ai-index-report
- Nadella 30% - https://techcrunch.com/2025/04/29/microsoft-ceo-says-up-to-30-of-the-companys-code-was-written-by-ai/

---

## Slide 12 - The productivity paradox

- Cui et al. RCT (n=4,867): +26% PRs/week with Copilot
- METR Feb 2026 walkback: original -19% slowdown moderates to -4% (CI -15% to +9%); productivity gains "likely" - but METR explicitly does NOT retract the security/quality concerns
- DORA 2025: PR review time +441%; PR size +51.3%; 30% distrust AI-generated code

**Graphic:** Two-panel chart - left: Cui +26% / METR -4% (with original -19% greyed out); right: DORA PR-size and review-time deltas.

**Speaker notes:** Productivity gains are real on greenfield enterprise tasks. The bottleneck has moved - the reviewer is now the load-bearing role. PRs are bigger and review time is 5x. This is why the rest of the talk is about review and governance, not speed.

**Sources:**
- Cui et al. - https://arxiv.org/abs/2302.06590
- METR original - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (paper https://arxiv.org/abs/2507.09089)
- METR Feb 2026 follow-up - https://metr.org/blog/2026-02-24-uplift-update/
- DORA 2025 - https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf

---

## Slide 13 - Quality on security is materially worse - and not improving

- Veracode Spring 2026 rerun (100+ LLMs): 45% still vulnerable; Java still 72%; newer models show no improvement
- "Broken by Default" arXiv:2604.05292 (Apr 2026): 55.8% of artifacts formally Z3-proven vulnerable; 6 commercial SAST tools combined miss 97.8%
- Pearce et al. IEEE S&P 2022: 40% baseline. 2022 to 2026 - the line is flat

**Graphic:** Three-bar comparison (2022 / 2025 / Spring 2026) showing flat trajectory.

**Speaker notes:** Two messages. One: across four years and a generation of frontier models, the failure rate has not moved. Two: this is not heuristic noise - the formal-verification work proves it, and the SAST tools you bought to catch it miss 97.8%. **And to be precise: this is a build-pipeline gap, not a runtime adversarial-testing gap.** New tooling categories are needed at the build-time perimeter, before code ever reaches a deployed environment that could be pen-tested.

**Sources:**
- Veracode Spring 2026 - https://www.veracode.com/blog/spring-2026-genai-code-security/
- Broken by Default - https://arxiv.org/abs/2604.05292
- Pearce et al. - https://arxiv.org/abs/2108.09293

---

# Segment 2 - Where the risk is piling up

## Slide 14 - Insecure-by-default at scale

- Apiiro Fortune-50 telemetry (7,000+ devs, 62,000 repos): 10,000+ new findings/month from AI-generated code by mid-2025; 10x in six months
- +322% privilege escalation paths; +153% architectural flaws; +40% secret exposures
- Pattern: trivial errors fell, architectural and identity flaws exploded - "shallow up, deep down"

**Icon (bottom-right):** [**W**] R D T   *(assumption 1 - the writer changed)*

**Graphic:** Apiiro hockey-stick of monthly findings.

**Speaker notes:** One Fortune-50 customer, but the most direct enterprise telemetry available. The directional caveat: this is one big data point, not a population estimate. The trend is the story.

**Sources:**
- Apiiro - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/

---

## Slide 15 - Hallucinated dependencies and slopsquatting

- Spracklen et al. USENIX Security 2025: 576,000 samples, 16 LLMs; commercial >=5.2%, open-source >=21.7% hallucination rate; 205,474 unique fake package names
- 43% of hallucinations recur across 10 prompt repeats - perfect repeatability for an attacker
- Lasso registered the hallucinated `huggingface-cli` as an empty PyPI package: 30,000+ downloads in 3 months, including in Alibaba's docs

**Icon (bottom-right):** W R [**D**] T   *(assumption 3 - dependencies are not real)*

**Graphic:** Per-model hallucination chart from the paper.

**Speaker notes:** This is the next typosquatting and it does not need any user error to land. The CI gate to allowlist against a known-good registry is one of the highest-leverage controls in this whole talk.

**Sources:**
- Spracklen et al. - https://arxiv.org/abs/2406.10279 (USENIX https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)
- Lasso huggingface-cli demo - https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks

---

## Slide 16 - Secrets exposure and overly broad permissions

- AI-assisted projects: ~2x rate of cloud-credential exposure vs non-AI baselines (GitGuardian / Snyk via Apiiro)
- 41% of AI-generated backend code ships with default-admin permissions when prompted naively
- Backslash 2025: GPT-4.1 with naive prompts scored 1.5/10 on secure code; Claude 3.7 went from 6/10 to 10/10 with security-focused prompts - the prompt is the control plane

**Icon (bottom-right):** [**W**] [**R**] D T   *(assumptions 1 + 2 - writer changed and reviewer didn't catch)*

**Graphic:** Secure-code-score bar chart - naive prompt vs security-focused prompt.

**Speaker notes:** Two leverage points. The prompt is part of your security perimeter now - prompt engineering for security is a real discipline. And default permissions are still the worst-tested surface in the LLM training set.

**Sources:**
- Apiiro - https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
- Backslash - https://www.backslash.security/press-releases/backslash-security-reveals-in-new-research-that-gpt-4-1-other-popular-llms-generate-insecure-code-unless-explicitly-prompted

---

## Slide 17 - Developer confidence is anti-correlated with secure outcomes

- Perry et al. ACM CCS 2023: AI-assisted developers wrote less secure code on 4 of 5 tasks - and were more likely to believe it was secure
- Snyk RSAC 2026: 48% of AI-generated code contains vulnerabilities; per-developer vuln rate up 2-10x YoY
- Stack Overflow Feb 2026: 84% of developers use AI; only 29% trust it (-11pts YoY); 81% concerned about security

**Icon (bottom-right):** [**W**] R D T   *(assumption 1 - the writer changed, and the dev can't tell)*

**Graphic:** Two-line chart - usage rising, developer trust falling - 2023 to 2026.

**Speaker notes:** Developers, by survey, already know the tool is unreliable. Use is up, trust is down. The job is to make the review structure match the survey instinct - your devs do not need convincing, they need scaffolding.

**Sources:**
- Perry et al. - https://arxiv.org/abs/2211.03622 (ACM https://dl.acm.org/doi/10.1145/3576915.3623157)
- Snyk RSAC 2026 - https://expertinsights.com/industry-perspectives/rsac-2026-manoj-nair-snyk
- Stack Overflow Feb 2026 - https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/

---

## Slide 18 - The toolchain is itself an AI attack surface

- LiteLLM (Mar 24, 2026): backdoored 1.82.7/1.82.8 via Trivy in CI - 3.4M daily downloads, 40,000+ in the exposure window
- 2026 CVEs in the AI tools themselves: Cursor RCE (CVE-2026-26268), Copilot Reprompt (CVE-2026-21516), Claude Code CLI RCE (CVE-2026-35021), Windsurf MCP zero-interaction (CVE-2026-30615)
- MCP servers are now developer-side shadow IT - and most have no authentication

**Icon (bottom-right):** W R D [**T**]   *(assumption 4 - the tools are not inspectable)*

**Graphic:** Pipeline-attack-flow + a small CVE-tile grid for the AI-tool CVEs.

**Speaker notes:** The pipeline runs AI tools that run AI tools. Pinning is policy. This is where you start to see Qualys-shaped data: discovering AI assets, MCP servers, and AI tools across endpoints is a control surface that did not exist 18 months ago. AIP / Hou et al. found ~2,000 production MCP servers, none with authentication. **Worth being precise:** these are build-time supply-chain incidents, on developer endpoints and CI infrastructure - runtime exploitation of deployed AI features is a separate problem with separate controls. This layer is largely uninstrumented and that is the gap.

**Sources:**
- LiteLLM advisory - https://docs.litellm.ai/blog/security-update-march-2026
- Microsoft Security on Trivy/LiteLLM - https://www.microsoft.com/en-us/security/blog/2026/03/24/detecting-investigating-defending-against-trivy-supply-chain-compromise/
- Cursor CVE-2026-26268 - https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
- Copilot Reprompt CVE-2026-21516 - https://www.paperclipped.de/en/blog/github-copilot-cve-2026-21516-reprompt-attack/
- Claude Code CLI CVE-2026-35021 - https://www.sentinelone.com/vulnerability-database/cve-2026-35021/
- "MCP by Design" supply-chain advisory - https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/
- AIP MCP scan paper - https://arxiv.org/abs/2603.24775

---

# Segment 3 - What to do (40/60)

## Slide 19 - Tooling

- Asset and MCP-server inventory as a precondition for the PR gate (you cannot scan what you cannot see)
- IDE-boundary controls: inspect prompts, block secrets, govern context, allowlist tool calls
- PR gates fail-closed: SAST + secret scanning + SCA on every AI-assisted PR; block hallucinated imports
- Pin AI tool versions; treat MCP servers as third-party dependencies

**Icon (bottom-right):** W [**R**] D [**T**]   *(restores 4 - inspectable tools; scaffolds 2 - reviewer relief via gates)*

**Graphic:** Pipeline diagram with four gates: AI-asset inventory -> IDE boundary -> PR gate -> build gate.

**Speaker notes:** Inventory first. Then gates. Spotlighting (Hines et al.) takes prompt-injection ASR from >50% to <2% via delimiting / encoding. AI-asset and MCP-server discovery is the new shadow-IT discovery problem - the same 2010s-era playbook applies, just on new asset types.

**Sources:**
- Hines et al. Spotlighting - https://arxiv.org/abs/2403.14720
- Hou et al. MCP Landscape - https://xinyi-hou.github.io/files/hou2025mcp_1.pdf

---

## Slide 20 - Process

- Mandatory AI-usage disclosure at the PR level - the cheapest, highest-leverage control
- AI-BOM at PR level: which model, which tools, which prompts, which packages
- Third-party AI-tool intake review (the Context AI question)
- AI-specific branch in the IR playbook

**Icon (bottom-right):** [**W**] R [**D**] T   *(restores 1 - writer disclosure; restores 3 - dependency provenance via AI-BOM)*

**Graphic:** PR template mock-up with two new fields highlighted: "AI-assisted? yes/no/which tool" and "AI-BOM attached?".

**Speaker notes:** You cannot improve what you cannot see, and you cannot defend what you cannot inventory. AI-BOM extends SBOM to model and tool provenance - the spec is maturing through OWASP and Linux Foundation work; pair with NIST SP 800-218A practice PO.1.

**Sources:**
- NIST SP 800-218A - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST SP 800-204D supply chain in CI/CD - https://csrc.nist.gov/pubs/sp/800/204/d/final
- SLSA v1.2 - https://slsa.dev/spec/v1.2/

---

## Slide 21 - Culture

- No merge until reviewed by someone who did not write the prompt
- Pair-review for AI-generated code: one used AI, one did not
- Ownership is human, regardless of what wrote it
- Reward catches, not velocity

**Icon (bottom-right):** W [**R**] D T   *(restores 2 - the reviewer reflex)*

**Graphic:** Two-developer review pattern - "the pair, not the prompt."

**Speaker notes:** Sandoval et al. (USENIX 2023, "Lost at C") show review interaction is the primary moderator of LLM-assisted bug rate. The metric trap is rewarding merge-rate while ignoring caught-flaw-rate - that is training the wrong reflex.

**Sources:**
- Sandoval et al., "Lost at C" - https://arxiv.org/abs/2208.09727

---

## Slide 22 - Organisational

- Name an owner: AppSec + engineering lead, not product
- Joint governance body, weekly cadence (49% of orgs run 5+ AI tools - quarterly cannot keep up)
- Redistribute the review workload: seniors review more, write less
- Hire and interview for the review reflex, not the typing reflex

**Icon (bottom-right):** W [**R**] D T   *(restores 2 structurally - review capacity is the bottleneck)*

**Graphic:** Org-chart fragment with the AppSec + engineering joint owner highlighted.

**Speaker notes:** This is the engineering-org slide. ISACA and ISO 42001 are the GRC framing - that gets covered in adjacent webinars. What gets undercovered is the engineering-org change: review capacity is now the bottleneck, and that affects hiring, headcount mix, and how you grade seniority.

**Sources:**
- GitLab DevSecOps 2025 - https://about.gitlab.com/press/releases/2025-11-10-gitlab-survey-reveals-the-ai-paradox/
- ISO/IEC 42001:2023 - https://www.iso.org/standard/42001

---

## Slide 23 - Governance and reporting

- Anchor on NIST SP 800-218A - the SDLC-specific GenAI profile
- Layer NIST AI 600-1 for risk taxonomy, NCSC/CISA Secure AI Development for lifecycle hooks
- Metrics: AI-assisted PR rate, vuln rate AI vs human, secret exposures from AI, MTTR for AI-introduced vulns
- Multi-signal correlation - endpoint + exposure + identity - to detect rogue dev-side AI agents

**Icon (bottom-right):** [**W**] [**R**] [**D**] [**T**]   *(restores all four at the audit layer)*

**Graphic:** Framework-stack diagram (NIST SSDF -> NIST AI RMF / 600-1 -> NCSC/CISA -> OWASP).

**Speaker notes:** Stay SDLC-specific. NIST 800-218A is the spine - it is the only framework that maps cleanly onto the build pipeline. The AI-RMF and ISO 42001 layer above. Multi-signal correlation - asset + vulnerability + identity - is how you actually see a rogue AI agent in your environment; pure runtime detection misses build-time precursors.

**Sources:**
- NIST SP 800-218A - https://csrc.nist.gov/pubs/sp/800/218/a/final
- NIST AI 600-1 - https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- NCSC + CISA Secure AI Development - https://www.ncsc.gov.uk/files/Guidelines-for-secure-AI-system-development.pdf
- OWASP Top 10 for LLM Applications - https://genai.owasp.org/llm-top-10/

---

## Slide 24 - Monday morning - restore the four

Four-row restoration table - one row per broken assumption, one column for the breakage, one column for the Monday action:

| Icon | Assumption broke | What you do Monday |
|---|---|---|
| **W** | The developer wrote it | **Mandate AI-usage disclosure at PR level**, plus AI-BOM (model, tools, prompts, packages) |
| **R** | The reviewer read it | **Redistribute review capacity** - seniors review more, write less; pair-review on AI-assisted PRs |
| **D** | Dependencies were real | **Allowlist your package registry** at CI; block hallucinated imports; pin and verify |
| **T** | The tools were inspectable | **Inventory AI assets and MCP servers** across the build pipeline; pin AI-tool versions; intake-review every new AI tool |

Plus one cross-cutting move:

- **Anchor the programme to NIST SP 800-218A** - the SDLC-specific GenAI profile - and report the four restorations as the metrics that matter

**Icon (bottom-right):** [**W**] [**R**] [**D**] [**T**]   *(restoration map - the close)*

**Graphic:** The four-row table above as the slide. Each row uses the icon from earlier slides as the row marker so the audience instantly recognises the spine.

**Speaker notes:** This is the close. Each row pairs a broken assumption from the opening with one Monday action that starts to restore it. None of these require new spend - they require new policy and new attention. **One framing for the room:** audiences this season are hearing two prescriptions for AI security - "do a maturity assessment" and "do an adversarial pentest." This restoration map is what you do *between* those engagements - the build-pipeline preconditions that determine whether the maturity assessment has anything to grade and whether the pentest finds anything new to report.

---

## Slide 25 - Q&A and Part 2

- Questions
- Bibliography lands in your inbox
- Part 2: Running AI in Production - what you are actually defending now

**Graphic:** Series wordmark with Part 2 title and date.

**Speaker notes:** Once it ships, it is someone else's attack surface. That is Part 2. Take questions.

---

# Production notes

- **Slide count:** 20.
- **Sub-segment mapping to part1-sdlc.md:** opening hook = 4-5; Segment 1 (what changed) = 6-8; Segment 2 (where risk piles up) = 9-13 (one slide per 2.x); Segment 3 (what to do) = 14-18 (one slide per 3.x); close = 19-20.
- **Differentiation from adjacent SASIG webinars:** build-time framing (Slide 2), real CVEs in OSS (Slide 3 opening hook), AI-tool supply chain (Slide 9 bridge, plus Slide 18), AI-BOM (Slide 20), engineering-org redistribution (Slide 22), NIST SP 800-218A spine (Slide 23). All under-served by the workforce-behaviour and runtime-IAM angles in the other talks.
- **Qualys lean-in (organic, non-product):** asset inventory through-line, MCP-server discovery (Slide 18/19), AI-BOM (Slide 20), multi-signal correlation (Slide 23), Monday-morning restoration map (Slide 24).
- **Spine (Slide 10):** four broken assumptions - W (writer), R (reviewer), D (dependency), T (tool). Recurring icon bottom-right of every Segment 2 and Segment 3 slide. Closing restoration table on Slide 24.
- **Charts to pre-build (priority):** Vibe Security Radar trajectory; Veracode Spring 2026 flat-line vs 2022 baseline; METR forecast-vs-observed (with 2026 update); Apiiro hockey-stick; LiteLLM attack-flow; AI-tool CVE tile grid; framework-stack diagram.
