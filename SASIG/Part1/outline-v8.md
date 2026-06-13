# Outline v8 - problem-first, slimmed, primer cut

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders
**Format:** 60-min slot.
**Slide count:** 17

**Structural shift from v7:** S1 cut from 3 slides to 2 (Defined-discipline name-check absorbed into the Profession slide and the CI/CD-fits slide). The four-moving-parts AI primer is cut entirely - inline glosses on Slides 8, 12, and 13 cover the only terms that matter for a CISO audience. Slide 9 (Shadow AI) is re-heroed around the department-of-no thread; data leakage becomes the consequence, not the headline. Slide 14 (Culture and Organisation) is rewritten so the agility / sanctioned-tooling response carries the slide. Four content additions baked in: prompt injection of coding agents (Slide 8), sycophancy and reproducibility (Slide 5), skill atrophy (Slide 14).

| # | Section | Slide title | Content (1-2 sentences) |
|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product, 40/60. Subtitle previews the argument. Bibliography by email. |
| 2 | Open | From tool to author | Hero: 75% of new code at Google is AI-generated and engineer-approved (Pichai, Alphabet Q1 2026). Trajectory 25 -> 50 -> 75 in two years. Vibe coding - Collins Word of the Year 2025. Board-level beat: 20-40% opex / 12-14pp EBITDA gains for AI-centric orgs. |
| 3 | Open | Real CVEs in real repos | Georgia Tech Vibe Security Radar - AI-attributed CVEs by month (6 / 15 / 35 in Jan / Feb / Mar 2026). 27 traceable to Claude Code. Endor/CMU 17.3% security pass on 200 OSS tasks; Fu et al. 29.5% Copilot Python snippets carry a CWE. The slope is the story. |
| 4 | S2 | The productivity paradox | DORA 2025 +21% tasks / +98% PRs merged (~5,000 devs); METR Feb 2026 walkback (-19% to -4%, security/quality concerns retained); BNY Mellon Feb 2026 (n=2,989) - perceived productivity diverges from measured; DORA cost side: PR review time +441%, PR size +51%. The reviewer is the load-bearing role. |
| 5 | S2 | Quality on security is materially worse - and not improving | Veracode Oct 2025 GenAI report 45% (100+ LLMs) -> Veracode Spring 2026 rerun 45% -> Broken-by-Default Apr 2026 55.8% Z3-proven. Two consecutive Veracode reruns plus formal-verification cross-check converge near 50%. 6 SAST tools miss 97.8%. Sycophancy: 58% sycophantic responses when challenged (SycEval Feb 2025); 48% affirmation in moral-conflict queries (ELEPHANT, ICLR 2026) - which is why generational LLM upgrades have not shifted the failure rate. Reproducibility: same prompt yields different code, so security review of one run is not evidence about another. |
| 6 | S2 | Insecure-by-default at scale | Apiiro Fortune-50 telemetry (mid-2025): 10x new findings/month; +322% privilege escalation; +153% architectural flaws; +40% secret exposures. 41% of AI-generated backend code ships with default-admin permissions (Backslash 2025). Snyk RSAC 2026: per-developer vuln rate up 2-10x YoY. Shallow up, deep down. |
| 7 | S2 | Hallucinated dependencies and slopsquatting | Spracklen USENIX 2025: 43% recurrence across 10 prompt repeats; 205,474 fabricated names catalogued. Lasso huggingface-cli: 30,000+ downloads in 3 months; landed in vendor docs (Alibaba GraphTranslator). CI allowlist is the highest-leverage control in the deck. |
| 8 | S2 | This is not "tools have CVEs" | Banner thesis: your CVE patching cadence is the wrong instrument. Three structural arguments: (1) prompt injection is a vulnerability class, not a CVE - 100% of tested coding agents vulnerable; 2026 defences (PromptArmor, PromptGuard) reduce ASR 67-99%, not eliminate. (2) Attack surface is content, not the network - CamoLeak markdown-image-in-issue, Rules File Backdoor, one PR-title injection made three coding agents post their keys. (3) Agents act, so blast radius is autonomous action - 2026 CVEs in Cursor/Copilot/Claude Code/Windsurf become attacker-driven code pushes and PR opens. Footer evidence the perimeter is missing: ~2,000 unauthenticated MCP servers, LiteLLM Mar 2026 backdoor, Vercel/Context AI Apr 2026 vendor pivot. Runtime prompt injection of production AI features is Part 2. |
| 9 | S2 | Shadow AI - your developers will route around you | Hero: developers will use whatever makes them effective; if security is too slow, they choose for you. 3 of 4 CISOs find unsanctioned coding tools already running in their estate (Aikido 2026); 75%+ of knowledge workers use GenAI (Sysdig 2026). Consequence: prompts routinely include proprietary code and credentials sent to vendor LLMs. Cues Slide 14 directly. |
| 10 | S1 | Secure SDLC is a profession | Buildings analogy. Delegated trust to competent humans - developer, reviewer, maintainer, operator. "Buildings don't fall down because of monitoring. They don't fall down because designers and builders behaved professionally." Footer band names the profession's codifications: SDL (2004), SSDF (2022), SAMM, BSIMM 15. After S2, this lands as moral indictment. |
| 11 | S1 | SDLC defines, pipelines enforce | NIST SP 800-204D Appendix B carve-out. Top tier - human judgment layer (writer, reviewer, dependencies). Bottom tier - CI/CD pipeline (build, test, package, deploy). The judgment layer lives above the pipeline. Footer band: now codified in product law (EU CRA, UK PSTI, EU AI Act). Closing line: you cannot fix what you just saw with more pipeline tooling alone - bridges into S3. |
| 12 | S3 | Tooling - what a confidently AI-enabled SDLC looks like | The "yes path" - four gates as the means of confident AI adoption. Inventory first, then IDE-boundary controls (2026 defences PromptArmor >99% prevention, PromptGuard 67% reduction), fail-closed PR gates, build-side pinning. Inline gloss for "harness" (Cursor / Copilot / Claude Code / Cline) on first reference. AI-aware SAST as the new perimeter category. |
| 13 | S3 | Process - the human-judgment restorations | AI-usage disclosure on PRs; AI-BOM (extends SBOM to model and tool provenance); third-party AI-tool intake review; AI-specific branch in IR playbook. Inline gloss for RAG ("how AI features pull in your private data") on first reference. Disclosure first, provenance second. |
| 14 | S3 | Culture and Organisation - not the department of no | Hero: closing the shadow-AI loop. The org that says yes to a sanctioned tool fast beats the one that says no slowly. Sanctioned tooling pathway, fast intake, agile updates. Supporting culture rules: pair review, no merge until reviewed by someone who didn't write the prompt, ownership is human, reward catches not velocity. Supporting org moves: redistribute review capacity (seniors review more, write less), hire for the review reflex - and the skill atrophy behind it is real (skill decay 2.5 years; 87% Snyk concern). |
| 15 | S3 | Governance - anchor, owner, measure | Three things to walk away with. Anchor: ISO/IEC 42001 or UK CoP / ETSI TS 104 223 - fit by analogy. Owner: joint AppSec + engineering, board-accountable. Measure: AI-assisted PR rate, vuln rate AI vs human, secret exposures, MTTR. Standards lag the practice; measure first. |
| 16 | Close | On the other hand - maybe this is transitional | Steel-man only. Aviation analogy (~70% autopilot, pilots trust it more than humans); frontier-lab evidence (Boris Cherny ships 22 PRs/day, Roon "I don't write code anymore"); generational trajectory; defensive tooling improving alongside; historical analogy (compilers, GC). The deck is the rebuttal. |
| 17 | Close | Q&A and Part 2 preview | Bibliography by email. Part 2: *Running AI in Production* - what you are actually defending now. |

## Section breakdown

| Block | Slides |
|---|---|
| Open | 1 - 3 |
| Section 2 - Where the risk is piling up (the problem) | 4 - 9 |
| Section 1 - The discipline that should have prevented this | 10 - 11 |
| Section 3 - What to do (the response) | 12 - 15 |
| Close | 16 - 17 |
| **Total** | **17 slides** |

17 slides at ~2.6 min each in a 45-min content window.

## Changes vs v7

| v7 slide | Disposition | Reason |
|---|---|---|
| v7 Slide 11 (Defined discipline) | Cut | Frameworks now named in passing on Slide 10 (Profession) footer band; regulatory floor moved to Slide 11 (CI/CD fits) footer band. The standalone credibility slide didn't earn its place in problem-first - audience already cares by the time S1 starts. |
| v7 Slide 4 / v7 Slide 12 (AI primer) | Cut entirely | No good slot. CISO audience does not need a standalone primer. MCP defined inline on Slide 8; harness inline on Slide 12; RAG inline on Slide 13. |
| v7 Slide 10 (Shadow AI / data exposure) | Re-heroed as Slide 9 | Hero shifts from scale-and-bind to "developers will route around you." Data leakage becomes the consequence. Direct setup for Slide 14. |
| v7 Slide 16 (Culture and Organisation) | Rewritten as Slide 14 | Whole slide now hangs off the department-of-no response, not just a closing beat. Culture rules and org moves become supporting structure under the agility hero. |
| v7 Slide 8 (Attack surface) | Prompt injection beat added (now Slide 8) | OWASP LLM01 was the biggest miss in the coverage assessment. Build-time prompt injection of coding agents (CamoLeak, Rules File Backdoor, PR-title key leak) belongs in Part 1; runtime hand-off to Part 2. |
| v7 Slide 6 (Quality) | Sycophancy + reproducibility beats added (now Slide 5) | Sycophancy explains *why* generational LLM upgrades have not shifted the failure rate. Reproducibility closes the orphan from the dropped W/R/D/T "T" frame. |
| v7 Slide 16 (Culture) | Skill atrophy bullet added (now Slide 14) | Anchors "hire for the review reflex" in the trend it responds to (skill decay 2.5 years; 87% Snyk concern). |
