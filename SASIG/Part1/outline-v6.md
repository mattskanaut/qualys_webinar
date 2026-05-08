# Outline v6 - running order

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot.
**Slide count:** 19

**Structural shift from v5:** The four-assumptions frame (W/R/D/T) is introduced once on Slide 5 as a *concept* - the four trust delegations the discipline rests on. It is not used as the deck's spine. No icons in slide corners; no four-row "Restoring the four" close. Section 2 follows v2's risk-themed structure verbatim. Section 3 follows v4's response-category structure. The deck closes with an "On the other hand" steel-man of the counter-argument - the rebuttal is the rest of the deck.

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product, 40/60. Subtitle previews the argument. Bibliography by email. |
| 2 | Open | Real CVEs in real repos | Georgia Tech Vibe Security Radar - AI-attributed CVEs by month (6 / 15 / 35 in Jan / Feb / Mar 2026). The slope is the story. |
| 3 | S1 | Secure SDLC is a defined discipline (v4 P1.1) | Microsoft SDL, NIST SSDF, OWASP SAMM, BSIMM 15 - 30 years of consensus, now codified in product law (EU CRA, UK PSTI, EU AI Act). |
| 4 | S1 | Secure SDLC is a profession (v4 P1.2) | Buildings analogy. Delegated trust to competent humans. |
| 5 | S1 | The four assumptions every secure SDLC rests on (v4 P1.3) | W/R/D/T introduced as concept - the four trust delegations the discipline rests on. The *only* slide where this frame is the focus. Closing pivot: "with AI in the loop, what does the developer actually know?" |
| 6 | S1 | Where CI/CD fits - SDLC defines, pipelines enforce (v4 P1.4) | NIST 800-204D Appendix B carve-out. Human-judgment layer lives above the pipeline. Sets up why "more pipeline tooling alone won't save you." |
| 7 | S2 | From tool to author | Merged: trajectory (vibe coding, 75% at Google, 25 -> 50 -> 75 in two years) as hero; adoption headcount (4.7M Copilot, 90% DORA, McKinsey, frontier labs) as footer band. |
| 8 | S2 | The four moving parts of AI dev tooling | LLM, harness, MCP server, RAG primer. Mental model needed for the dependency and tool-attack-surface slides. |
| 9 | S2 | The productivity paradox (v2 Slide 12) | Cui +26% PRs/week; METR Feb 2026 walkback (-19% to -4%); DORA review time +441%, PR size +51%. Trust-gap angle (Stack Overflow 84% use, 29% trust) absorbed in speaker notes. |
| 10 | S2 | Quality on security is materially worse - and not improving (v2 Slide 13) | Pearce 2022 40% baseline -> Veracode Spring 2026 45% -> Broken-by-Default 55.8% Z3-proven. Flat line, four years, generational LLM upgrades. 6 SAST tools miss 97.8%. |
| 11 | S2 | Insecure-by-default at scale (v2 Slide 14) | Apiiro Fortune-50: 10x findings/month; +322% priv-esc; +153% architectural flaws. 41% of AI-generated backend code ships with default-admin perms (Backslash) - absorbed from v2 Slide 16. |
| 12 | S2 | Hallucinated dependencies and slopsquatting (v2 Slide 15) | Spracklen 43% recurrence; Lasso huggingface-cli 30k downloads in 3 months. CI allowlist is the highest-leverage control. |
| 13 | S2 | The AI toolchain is itself an attack surface (v2 Slide 18) | LiteLLM March 2026; 2026 CVEs in Cursor / Copilot / Claude Code / Windsurf; ~2,000 production MCP servers, none authenticated. |
| 14 | S3 | Tooling - PR gates, AI-asset inventory, IDE boundary (v4 P3.1) | Pipeline-enforceable controls. Inventory first, then IDE-boundary controls (Spotlighting 50% -> 2% ASR), then fail-closed PR gates, then build-side pinning. |
| 15 | S3 | Process - the human-judgment restorations (v4 P3.2) | AI-usage disclosure on PRs; AI-BOM; third-party AI-tool intake review; AI branch in IR playbook. Disclosure first, provenance second. |
| 16 | S3 | Culture and Organisation (merge v4 P3.3 + P3.4) | Pair review, ownership, reward catches; redistribute review capacity (seniors review more, write less); hire and grade for the review reflex. |
| 17 | S3 | Governance and metrics (v4 P3.5) | NIST SP 800-218A as the spine. AI 600-1, NCSC + CISA, OWASP LLM Top 10. Metrics: AI-assisted PR rate, vuln rate AI vs human, secret exposures, MTTR. Multi-signal correlation. |
| 18 | Close | On the other hand - maybe this is transitional | Steel-man only. Aviation analogy (~70% autopilot, pilots trust it more than humans); frontier-lab evidence (Boris Cherny, Roon); generational trajectory; defensive tooling improving alongside; historical analogy (compilers, GC). No rebuttal on the slide - the rest of the deck is the rebuttal. |
| 19 | Close | Q&A and Part 2 preview (P-Close) | Bibliography by email. Part 2 is *Running AI in Production*. |

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 2 |
| Section 1 - Secure SDLC concepts | 3 - 6 |
| Section 2 - Where the risk is piling up | 7 - 13 |
| Section 3 - What to do | 14 - 17 |
| Close | 18 - 19 |
| **Total** | **19 slides** |

19 slides at ~2.4 min each in a 45-min content window.

---

## Cuts and merges vs v5

| v5 slide | Disposition | Reason |
|---|---|---|
| v5 Slide 5 (P2.1 trajectory) + v5 Slide 7 (P2.3 adoption) | Merged into new Slide 7 | Trajectory is the lede; adoption headcount becomes a footer band on the same slide. |
| v5 Slide 12 (P2.8 Secrets exposure) | Cut, default-admin bullet absorbed into Slide 11 | Default-admin-perms stat is the one to keep; cloud-credential-exposure overlap with Insecure-by-default. |
| v5 Slide 13 (P2.9 Developer confidence) | Cut, trust-gap absorbed into Slide 9 speaker notes | Survey-data slide that overlapped Productivity paradox and Quality flat slides. |
| v5 Slide 17 (P3.3 Culture) + v5 Slide 18 (P3.4 Organisation) | Merged into new Slide 16 | Both lean on the reviewer/team story; adjacent stories about how the team behaves and how it's staffed. |
| v5 Slide 20 (P3.6 Restoring the four) | Replaced with new Slide 18 (On the other hand) | "Restoring the four" was the most W/R/D/T-spine-forced slide. The new close engages the counter-argument honestly and lets the rest of the deck do the rebutting. |
| New Slide 1 (Title) | Restored from v4 | Was dropped in v5; needed for a 60-min slot. |
| New Slide 2 (Opening hook - real CVEs) | Restored from v4 / v2 Slide 3 | Was dropped in v5; the Georgia Tech Vibe Security Radar grounds the talk in real-world incidents before the framework section. |
