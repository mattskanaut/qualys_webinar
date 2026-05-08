# Outline v4 - running order

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Format:** 60-min slot. Target ~34 min content + Q&A + host preamble.
**Slide count:** 19

| # | Section | Slide title | Content (1 - 2 sentences) | Time |
|---|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product promise stated out loud. Subtitle previews the four assumptions. | 1 min |
| 2 | Open | Opening hook - real CVEs in real repos | Georgia Tech Vibe Security Radar trajectory; the slope is the story. | 1.5 min |
| 3 | S1 | Secure SDLC is a defined discipline | Microsoft SDL, NIST SSDF, OWASP SAMM, BSIMM 15 - 30 years of consensus. Closing bullet: now codified in product law (EU CRA, UK PSTI). | 1.5 min |
| 4 | S1 | Secure SDLC is a profession | Buildings analogy. Profession = delegated trust to competent humans. Four assumptions encode that delegation in software. | 2 min |
| 5 | S1 | The four assumptions every secure SDLC rests on | W/R/D/T introduced with framework citations under each (PW.5, PW.7, PS.3.2/PW.4.4, PO.3/PO.5). Closing pivot: "with AI in the loop, what does the developer actually know?" | 2 min |
| 6 | S1 | Where CI/CD fits - SDLC defines, pipelines enforce | NIST SP 800-204D Appendix B in NIST's own words: PW.1 - PW.4 / PW.7 "pertain to secure software design, review of the design, and software reuse" - the human-judgment layer. Three of four assumptions live here; only T rides on the pipeline. | 2 min |
| 7 | S2 | AI is now in every developer's hands | Microsoft 4.7M Copilot subs, DORA 90%, McKinsey 90%+. "AI is in your stack" - established. | 1.5 min |
| 8 | S2 | What's actually in your build pipeline now | One-slide AI primer - LLM + harness + MCP server + RAG retriever. | 1.5 min |
| 9 | S2 | Writer - the developer wrote it | Apiiro 10x findings, +322% priv-esc, secret exposure, developer-confidence anti-correlation. | 2 min |
| 10 | S2 | Reviewer - the reviewer read it | DORA: PR size +51%, review time +441%, distrust at -11pts YoY (Stack Overflow). | 2 min |
| 11 | S2 | Dependency - the dependencies were vetted | Slopsquatting. Spracklen 43% recurrence, Lasso huggingface-cli, allowlist bypass. | 1.5 min |
| 12 | S2 | Tool - the tools were deterministic | LiteLLM, Cursor / Copilot / Claude Code / Windsurf CVEs, MCP unauth (Hou et al., Prakash AIP), Vercel / Context AI, prompt injection. | 2 min |
| 13 | S3 | Tooling - PR gates, AI-asset inventory, IDE boundary | Pipeline-enforceable controls. Pipelines reinforce T: version pinning, MCP allowlists, signed artefacts; PR gates that fail closed. | 2 min |
| 14 | S3 | Process - the human-judgment restorations | AI-usage disclosure on PRs, AI-BOM, third-party AI-tool intake review, AI branch in IR playbook. | 2 min |
| 15 | S3 | Culture | Pair review for AI-assisted PRs (one used AI, one didn't). Ownership stays human regardless of what wrote it. Reward catches, not velocity. | 2 min |
| 16 | S3 | Organisation | Joint AppSec + engineering owner. Redistribute review capacity - seniors review more, write less. Hire and grade for the review reflex. | 2 min |
| 17 | S3 | Governance | NIST SP 800-218A as the spine. Metrics: AI-assisted PR rate, vuln rate AI vs human, MTTR for AI-introduced vulns. | 2 min |
| 18 | S3 | Restoring the four | Four-row table - one restoration per broken assumption. Speaker beat: transitional counter-argument (autopilot, Boris Cherny, system-layer rebuttal). | 2.5 min |
| 19 | Close | Q&A and Part 2 preview | Bibliography lands by email. Part 2 is *Running AI in Production*. | 1 min |

## Time and section breakdown

| Block | Slides | Time |
|---|---|---|
| Open | 1 - 2 | 2.5 min |
| Section 1 (baseline + spine + carve-out) | 3 - 6 | 7.5 min |
| Section 2 (the deltas) | 7 - 12 | 10.5 min |
| Section 3 (the restorations) | 13 - 18 | 12.5 min |
| Close | 19 | 1 min |
| **Total content** | **19 slides** | **34 min** |

In a 60-min slot: 5 min host preamble + 34 min content + 10 min Q&A + 11 min slack for transitions and audience interaction.

---

## Four-assumption risk count

Rough comparison of how many distinct risk categories each broken assumption carries. Slide 12 (Tool / deterministic) is the heaviest; Slide 11 (Dependency / vetted) is the narrowest but most policy-actionable.

| Slot | Risks captured | Count |
|---|---|---|
| **W - wrote** | Insecure-by-default code, +322% privilege-escalation paths, +153% architectural flaws, secret exposure ~2x, default-admin perms 41%, CWE hotspots, confidence anti-correlation, per-dev vuln rate up 2-10x | ~7 |
| **R - read** | PR size +51%, review time +441%, rubber-stamping, no AI disclosure, can't see model/prompt/RAG context, dev trust at -11pts YoY | ~6 |
| **D - vetted** | Slopsquatting (Spracklen, Lasso huggingface-cli), AI-imported-without-checking, abandoned packages AI suggests, transitive-dep blowups, allowlist bypass, doc pollution | ~5 |
| **T - deterministic** | AI-tool RCEs (Cursor, Copilot, Claude Code, Windsurf), LiteLLM supply-chain compromise, MCP servers as shadow IT, MCP unauth, prompt injection, tool poisoning, agentic loops with dev privileges, cross-server shadowing, AI-vendor breach, indirect prompt injection via RAG | ~10 |
