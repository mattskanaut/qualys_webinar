# Outline v7 - problem-first

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot.
**Slide count:** 19

**Structural shift from v6:** Problem-first arc. Open with adoption + real CVEs, walk the audience through the full risk pile (S2), name the discipline that should have prevented it (S1, slimmed to 3 slides), prescribe the response (S3). The W/R/D/T quadrant is dropped - the deck makes its argument from data, not a manufactured frame. Slide 13 (where CI/CD fits) is re-pointed to bridge S1 forward into S3. New top-level slide on shadow AI / IP and secrets exposure - mitigation cue feeds into S3 culture slide.

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product, 40/60. Subtitle previews the argument. Bibliography by email. |
| 2 | Open | From tool to author | Hero: 75% of new code at Google is AI-generated and engineer-approved (Pichai, Alphabet Q1 2026). Trajectory 25 -> 50 -> 75 in two years. Vibe coding - Collins Word of the Year 2025. Board-level beat: 20-40% opex / 12-14pp EBITDA gains for AI-centric orgs. |
| 3 | Open | Real CVEs in real repos | Georgia Tech Vibe Security Radar - AI-attributed CVEs by month (6 / 15 / 35 in Jan / Feb / Mar 2026). 27 traceable to Claude Code. Endor/CMU 17.3% security pass on 200 OSS tasks; Fu et al. 29.5% Copilot Python snippets carry a CWE. The slope is the story. |
| 4 | S2 | The four moving parts of AI dev tooling | LLM, harness, MCP server, RAG. One-slide primer. Mental model needed for the dependency, attack-surface and shadow-AI slides that follow. |
| 5 | S2 | The productivity paradox | Cui RCT +26% PRs/week; METR Feb 2026 walkback (-19% to -4%, security/quality concerns retained); DORA PR review time +441%, PR size +51%. The reviewer is the load-bearing role. |
| 6 | S2 | Quality on security is materially worse - and not improving | Pearce 2022 40% baseline -> Veracode Spring 2026 45% -> Broken-by-Default Apr 2026 55.8% Z3-proven. Flat line across four years and a generation of LLMs. 6 commercial SAST tools miss 97.8%. |
| 7 | S2 | Insecure-by-default at scale | Apiiro Fortune-50 telemetry (mid-2025): 10x new findings/month; +322% privilege escalation; +153% architectural flaws; +40% secret exposures. 41% of AI-generated backend code ships with default-admin permissions (Backslash). Shallow up, deep down. |
| 8 | S2 | Hallucinated dependencies and slopsquatting | Spracklen USENIX 2025: 43% recurrence across 10 prompt repeats; 205,474 fabricated names catalogued. Lasso huggingface-cli: 30,000+ downloads in 3 months; landed in vendor docs (Alibaba GraphTranslator). CI allowlist is the highest-leverage control in the deck. |
| 9 | S2 | The AI toolchain is itself an attack surface | LiteLLM March 2026 backdoor (3.4M daily downloads, 40k in exposure window); 2026 CVEs in Cursor / Copilot / Claude Code / Windsurf; ~2,000 production MCP servers, none authenticated (Prakash AIP 2026). The pipeline runs AI tools that run AI tools. |
| 10 | S2 | Shadow AI and the data exposure problem | 75%+ of knowledge workers already use GenAI; 3 of 4 CISOs find unsanctioned coding tools in their estate (Sysdig / Aikido 2026). Prompts routinely include proprietary code and credentials sent to vendor LLMs. The bind: developers will use whatever makes them effective - if you don't sanction tools, they'll choose for you. Cues S3's organisational response. |
| 11 | S1 | Secure SDLC is a defined discipline | Microsoft SDL, NIST SSDF, OWASP SAMM, BSIMM 15 - 30 years of consensus. Now codified in product law: EU CRA (Dec 2024), UK PSTI (Apr 2024), EU AI Act (Aug 2024). This isn't opinion. |
| 12 | S1 | Secure SDLC is a profession | Buildings analogy. Delegated trust to competent humans - developer, reviewer, maintainer, operator. "Buildings don't fall down because of monitoring. They don't fall down because designers and builders behaved professionally." After S2, this lands as moral indictment. |
| 13 | S1 | SDLC defines, pipelines enforce | NIST SP 800-204D Appendix B carve-out. Top tier - human judgment layer (writer, reviewer, dependencies). Bottom tier - CI/CD pipeline (build, test, package, deploy). The judgment layer lives above the pipeline. You can't fix what you just saw with more pipeline tooling alone - bridges into S3. |
| 14 | S3 | Tooling - what a confidently AI-enabled SDLC looks like | The "yes path" - four gates as the means of confident AI adoption. Inventory first, then IDE-boundary controls (Spotlighting 50% -> 2% ASR), fail-closed PR gates, build-side pinning. AI-aware SAST as the new perimeter category - Snyk DeepCode, Datadog OSS, DryRun, Endor, Semgrep, GitHub CodeQL. |
| 15 | S3 | Process - the human-judgment restorations | AI-usage disclosure on PRs; AI-BOM (extends SBOM to model and tool provenance); third-party AI-tool intake review; AI-specific branch in IR playbook. Disclosure first, provenance second. |
| 16 | S3 | Culture and Organisation - not the department of no | Culture: pair review, no merge until reviewed by someone who didn't write the prompt, ownership is human, reward catches not velocity. Organisation: redistribute review capacity (seniors review more, write less), hire for the review reflex. Closing the shadow-AI loop: sanctioned tooling pathway, fast intake, agile updates - the org that says yes to a sanctioned tool fast beats the one that says no slowly. |
| 17 | S3 | Governance and metrics | NIST SP 800-218A SSDF GenAI profile as the spine. AI 600-1, NCSC + CISA Guidelines for Secure AI System Development, OWASP LLM Top 10. Metrics: AI-assisted PR rate, vuln rate AI vs human, secret exposures, MTTR for AI-introduced vulns. |
| 18 | Close | On the other hand - maybe this is transitional | Steel-man only. Aviation analogy (~70% autopilot, pilots trust it more than humans); frontier-lab evidence (Boris Cherny ships 22 PRs/day, Roon "I don't write code anymore"); generational trajectory; defensive tooling improving alongside; historical analogy (compilers, GC). The deck is the rebuttal. |
| 19 | Close | Q&A and Part 2 preview | Bibliography by email. Part 2: *Running AI in Production* - what you are actually defending now. |

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 3 |
| Section 2 - Where the risk is piling up (the problem) | 4 - 10 |
| Section 1 - The discipline that should have prevented this | 11 - 13 |
| Section 3 - What to do (the response) | 14 - 17 |
| Close | 18 - 19 |
| **Total** | **19 slides** |

19 slides at ~2.4 min each in a 45-min content window.

## Changes vs v6

| v6 slide | Disposition | Reason |
|---|---|---|
| v6 Slide 5 (Four assumptions W/R/D/T) | Cut | Manufactured frame. T (tools were deterministic) doesn't map cleanly to anything in SSDF; the acronym is mnemonic theatre. The talk's argument ("AI breaks foundational assumptions") survives without the quadrant. |
| v6 Slide 7 (From tool to author) | Promoted to Slide 2 | Adoption scale is the "why now" - belongs in the open with the CVE hook. |
| v6 Slide 2 (CVEs) and 8-13 (S2 evidence) | Moved ahead of S1 | Problem-first arc. Audience feels the damage before they hear the discipline that was supposed to prevent it. |
| v6 Slide 13 (Attack surface) - shadow AI footer beat | Promoted to new Slide 10 | Different risk class than CVE-driven attack surface: organisational data exposure vs technical exploitability. Direct mitigation cue into S3's culture slide. |
| v6 Slide 6 (CI/CD fits) | Re-pointed | "Three of four assumptions live above the pipeline" line dies with W/R/D/T. New framing bridges S1 forward into S3, not backward into S2. |
| v6 Slide 16 (Culture and Organisation) | Expanded | "Department of no" / agile sanctioned-tooling thread added to close the shadow-AI loop from new Slide 10. |
