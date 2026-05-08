# Outline v5 - running order

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot.
**Slide count:** 21

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | S1 | Secure SDLC is a defined discipline, not a buzzword (P1.1) | Microsoft SDL, NIST SSDF, OWASP SAMM, BSIMM 15 - 30 years of consensus, now codified in product law (EU CRA, UK PSTI, EU AI Act). |
| 2 | S1 | Secure SDLC is a profession (P1.2) | Buildings analogy. Profession = delegated trust to competent humans. The four assumptions encode that delegation in software. |
| 3 | S1 | The four assumptions every secure SDLC rests on (P1.3) | W/R/D/T introduced with framework citations under each (PW.5, PW.7, PS.3.2/PW.4.4, PO.3/PO.5). Closing pivot: "with AI in the loop, what does the developer actually know?" |
| 4 | S1 | Where CI/CD fits - SDLC defines, pipelines enforce (P1.4) | NIST SP 800-204D Appendix B in NIST's own words: PW.1-PW.4 / PW.7 are the human-judgment layer. Three of four assumptions live above the pipeline; only T rides on it. |
| 5 | S2 | From tool to author (P2.1) | "Vibe coding" / Collins WOTY 2025; Google Q1 2026 earnings: 75% of new code is AI-generated and engineer-approved (up from 50% fall 2025, 25% in 2024). The slope is the story. |
| 6 | S2 | Four moving parts that didn't exist 18 months ago (P2.2) | One-slide AI primer - LLM, harness, MCP server, RAG. Mental model the audience needs to follow Section 2. |
| 7 | S2 | Adoption is near-universal in the enterprise (P2.3) | Microsoft FY26 Q2: 4.7M paid Copilot subs (~90% of Fortune 100); DORA 2025 90%; McKinsey 90%+. AI is established. |
| 8 | S2 | The productivity paradox (P2.4) | Cui RCT +26% PRs/week; METR Feb 2026 walkback (-19% to -4%); DORA: PR review time +441%, PR size +51%. The bottleneck has moved to review. |
| 9 | S2 | Quality on security is materially worse - and not improving (P2.5) | Pearce 2022 40% baseline -> Veracode Spring 2026 45% -> Broken-by-Default 55.8% Z3-proven. 6 SAST tools combined miss 97.8%. Flat line across four years. |
| 10 | S2 | Insecure-by-default at scale (P2.6) [W] | Apiiro Fortune-50 telemetry: 10x findings/month from AI code; +322% priv-esc, +153% architectural flaws. Shallow up, deep down. |
| 11 | S2 | Hallucinated dependencies and slopsquatting (P2.7) [D] | Spracklen et al.: 5.2-21.7% hallucination rate; 205,474 fake names; 43% recur. Lasso huggingface-cli: 30,000+ downloads. CI allowlist is the highest-leverage control. |
| 12 | S2 | Secrets exposure and overly broad permissions (P2.8) [W][R] | ~2x cloud-credential exposure rate; 41% AI-generated backend code ships default-admin. Backslash: prompt is the control plane (1.5/10 -> 10/10 swing). |
| 13 | S2 | Developer confidence is anti-correlated with secure outcomes (P2.9) [W] | Perry CCS 2023: less secure code AND more confident; Snyk RSAC 2026: 48% of AI code vulnerable, vuln rate up 2-10x; Stack Overflow: 84% use, 29% trust. |
| 14 | S2 | The toolchain is itself an AI attack surface (P2.10) [T] | LiteLLM (Mar 2026) backdoor; 2026 CVEs in Cursor / Copilot / Claude Code / Windsurf; ~2,000 production MCP servers, none authenticated. |
| 15 | S3 | Tooling - PR gates, AI-asset inventory, IDE boundary (P3.1) [T] | Pipeline-enforceable controls. Inventory first, then IDE-boundary controls (Spotlighting), then fail-closed PR gates, then build-side pinning. Pipelines reinforce T. |
| 16 | S3 | Process - the human-judgment restorations (P3.2) [W][R][D] | Mandatory AI-usage disclosure on PRs; AI-BOM; third-party AI-tool intake review; AI branch in IR playbook. Disclosure first. Provenance second. |
| 17 | S3 | Culture (P3.3) [R] | Pair review for AI-assisted PRs (one used AI, one didn't). Ownership stays human. Reward catches, not velocity. Sandoval USENIX 2023: review interaction is the primary moderator of bug rate. |
| 18 | S3 | Organisation (P3.4) [R] | Joint AppSec + engineering owner; weekly governance cadence; redistribute review capacity (seniors review more, write less); hire and grade for the review reflex. |
| 19 | S3 | Governance (P3.5) [W][R][D][T] | NIST SP 800-218A as the spine. Layer AI 600-1, NCSC + CISA, OWASP LLM Top 10. Metrics: AI-assisted PR rate, vuln rate AI vs human, secret exposures from AI, MTTR. Multi-signal correlation. |
| 20 | S3 | Restoring the four (P3.6) [W][R][D][T] | Four-row restoration table - one per broken assumption. Closing speaker beat: transitional counter-argument (autopilot, Boris Cherny, system-layer rebuttal). Aviation didn't get safe by trusting one agent. |
| 21 | Close | Q&A and Part 2 preview (P-Close) | Bibliography lands by email. Part 2 is *Running AI in Production*. |

## Section breakdown

| Block | Slides |
|---|---|
| Section 1 - Secure SDLC concepts | 1 - 4 |
| Section 2 - How AI is breaking the SDLC | 5 - 14 |
| Section 3 - What to do | 15 - 20 |
| Close | 21 |
| **Total** | **21 slides** |

---

## Four-assumption risk mapping

Which broken assumption(s) each Section 2 risk slide touches and which Section 3 slide(s) restore them. The W/R/D/T spine is the talk's through-line - it lives in speaker notes and bottom-right icons rather than in the slide titles, but it remains the organising taxonomy.

| Assumption | Risk slides where it shows up | Restoration slides |
|---|---|---|
| **W** - the developer wrote it | 10 (Insecure-by-default), 12 (Secrets/permissions), 13 (Developer confidence) | 16 (Process - disclosure + AI-BOM), 19 (Governance), 20 (Restoring) |
| **R** - the reviewer read it | 8 (Productivity paradox / review-time), 12 (Secrets/permissions) | 16 (Process), 17 (Culture - pair review), 18 (Organisation - review capacity), 20 (Restoring) |
| **D** - the dependencies were vetted | 11 (Hallucinated dependencies / slopsquatting) | 15 (Tooling - allowlist), 16 (Process - AI-BOM), 20 (Restoring) |
| **T** - the tools were deterministic | 14 (Toolchain attack surface) | 15 (Tooling - inventory + pinning), 19 (Governance), 20 (Restoring) |
