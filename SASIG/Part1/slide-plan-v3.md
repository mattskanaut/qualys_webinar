
 1. Secure software development is a mature, 30-year-old discipline with broad consensus.
 2. Its controls quietly depend on humans doing the work - defining requirements, threat-modelling, reviewing designs, choosing libraries,
  reading code. NIST itself separates this human-judgment layer from the CI/CD pipeline that enforces it (SP 800-204D Appendix B
 explicitly carves out PW.1 - PW.4 and PW.7 as outside pipeline scope).
 3. AI now sits inside every human-judgment control and compresses or removes it. Four assumptions break: the Writer wrote it, the
 Reviewer read it, the Dependency was real, the Tool was inspectable.
 4. The response is mostly not more pipeline tooling - pipelines were never designed to enforce judgment. It is restoring the
 human-judgment layer through process, organisation, and governance, with new pipeline gates added only where AI introduces genuinely new
 attack surface.



# Part 1 - Slide Plan (v3, three-part structure)

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Series:** The New Normal: Software, Security and the AI Stack - Part 1 of 2
**Audience:** SASIG community - CISOs and security leaders (vendors, contractors and press excluded)
**Format:** 55 min content + 5 min Q&A. Non-product. Roughly 40% problem / 60% what to do.
**Style:** Brief, high-level. Speaker carries the content; slides anchor.

---

## Structural rebuild from v2

Two issues with v2 drove this rebuild:

1. **Pacing.** The four-assumption spine landed on slide 10 after a long mental-model detour. The audience held "what is an LLM / harness / MCP / RAG" without an anchoring frame for why it mattered.
2. **Through-line.** "You cannot govern what you cannot inventory" is too obvious for a CISO audience - it states the table-stakes premise rather than carrying the argument.

v3 reorganises around three parts. The four-assumption spine (Writer / Reviewer / Dependency / Tool) survives but moves *into* Part 2 as the framing device for the AI deltas, rather than living as a standalone segment.

| Part | Working title | Job |
|---|---|---|
| **Part 1** | Secure SDLC concepts | Establish the canonical, well-sourced picture of what a secure software development lifecycle actually is - and where CI/CD sits inside it. Ground the audience in 30 years of consensus practice. |
| **Part 2** | How AI is changing the SDLC | Reveal the deltas: AI now writes the code, reviews are bigger, dependencies hallucinate, tools have RCEs. Light AI primer in service of these deltas, not a standalone "what is AI" detour. The four assumptions land here as the punchline. |
| **Part 3** | What to do about it | The 60% of a 40/60 problem-to-solution split. Concrete restoration moves in tooling, process, culture, organisation, and governance. |

---

## How CI/CD fits (framing for Part 1)

CI/CD is the operational *enactment* of the SDLC. The SDLC defines what good development practices are; CI/CD pipelines are where those practices become automated, enforceable gates rather than aspirational policy. The bridge is explicit in the literature:

- **NIST SP 800-218 (SSDF)** defines the practices (the *what*).
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) - *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines* - is the companion publication that maps SSDF practices onto CI/CD pipeline stages: **build, test, package, deployment** (the *how*, in CI/CD terms). Crucially, Appendix B explicitly carves out SSDF practices PW.1 - PW.4, PW.7, and RV.1 - RV.3 as **outside** CI/CD scope - design, threat modelling, code review, and vulnerability response are SDLC-level activities, not pipeline activities.
- **SLSA v1.2** defines build-platform integrity levels (L0 - L3) so "we built it on a trusted system" is provable rather than asserted.
- **DevSecOps** is the cultural framing: every CI/CD stage is also a security stage; shift-left because a CWE caught in a PR is roughly two orders of magnitude cheaper than one caught in production.

This is also the right place to land the build-time framing - this talk owns the build-time / artefact layer, distinct from the workforce and runtime layers in adjacent SASIG sessions.

---

# Part 1 - Secure SDLC concepts

## Slide P1.1 - Secure SDLC is a defined discipline, not a buzzword

- **Microsoft SDL** (origin: Bill Gates Trustworthy Computing memo, January 2002; first published SDL ~2004): five phases - Requirements, Design, Implementation, Verification, Release - plus 10 practices including threat modelling, secure engineering environment, supply-chain security, security testing, monitoring and response.
- **NIST SP 800-218 (SSDF v1.1)**, Feb 2022; **v1.2 in public comment** (Dec 2025 - Jan 2026). Four practice groups: PO (Prepare the Organization), PS (Protect the Software), PW (Produce Well-Secured Software), RV (Respond to Vulnerabilities). The U.S. federal baseline.
- **OWASP SAMM v2** - open-source maturity model. Five business functions (Governance, Design, Implementation, Verification, Operations), 15 security practices, three maturity levels.
- **BSIMM 15** (Black Duck / Synopsys, 2024) - the *measured* practice across 121 firms. 12 practices in 4 domains. Notable in BSIMM 15: +22% adoption of SBOMs, dedicated adversarial-testing teams up ~30%.

**Graphic:** Four-logo / four-card lineup with year established and one-line "what it is" - a visual "these all converge."

**Speaker notes:** Three decades, four mature frameworks, one clear consensus - secure software development has a defined shape. Microsoft SDL is the grandfather, born from the Trustworthy Computing memo; NIST SSDF is the U.S. federal baseline that maps to FedRAMP and cross-references SLSA, in-toto, OWASP and ISO; SAMM is the open-source maturity model; BSIMM is the *empirical* model - what firms actually do, measured. Take this slide as established and move on - the rest of Part 1 distils what they all agree on.

**Sources:**
- Microsoft SDL practices - https://www.microsoft.com/en-us/securityengineering/sdl/practices
- NIST SSDF (project page) - https://csrc.nist.gov/projects/ssdf
- NIST SP 800-218 v1.1 - https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF v1.2 public comment notice (Dec 17, 2025) - https://www.nist.gov/news-events/news/2025/12/secure-software-development-framework-ssdf-version-12-available-public
- OWASP SAMM - https://owaspsamm.org/model/
- BSIMM 15 datasheet - https://www.blackduck.com/content/dam/black-duck/en-us/datasheets/bsimm-datasheet.pdf

---

## Slide P1.2 - What every framework agrees on - the four areas

NIST SSDF's four-group taxonomy is the cleanest spine; the other frameworks line up underneath.

| SSDF group | What it covers | Microsoft SDL maps to | OWASP SAMM maps to |
|---|---|---|---|
| **PO - Prepare the Organization** | Governance, training, secure dev environments, defined security requirements | Establish standards / governance; Provide training; Secure the engineering environment | Governance (Strategy & Metrics, Policy & Compliance, Education & Guidance) |
| **PS - Protect the Software** | Build integrity, code signing, artefact tamper-protection, provenance | Secure the software supply chain | Implementation (Secure Build, Secure Deployment) |
| **PW - Produce Well-Secured Software** | Secure design, threat modelling, secure coding, code review, security testing | Threat modelling; Secure features and frameworks; Crypto standards; Security testing | Design (Threat Assessment, Security Requirements, Security Architecture) + Verification |
| **RV - Respond to Vulnerabilities** | Disclosure, triage, fix, learn-and-prevent | Security monitoring and response | Operations (Incident Management) + Defect Management |

**Graphic:** Four-column / four-row mapping table as above, or a four-quadrant card with the four SSDF verbs as the headlines and the SDL / SAMM mappings underneath.

**Speaker notes:** Don't read the table out loud - it's a reference. The point is convergence: four independent frameworks, same four jobs. If you remember nothing else from this segment, remember those four verbs - prepare, protect, produce, respond. They're the spine of every secure-development programme worth the name. We'll come back to each of these in Part 2 when we look at where AI has changed what each of them depends on.

**Sources:** as Slide P1.1.

---

## Slide P1.3 - The build-time controls everyone agrees on

Six controls every framework lists, in roughly the order they appear in the dev process. Citations are to **verbatim practice titles** in NIST SSDF v1.1 (note: build-time controls span SSDF's PO, PW *and* PS groups - they are not all inside PW). PW.3 was retired in v1.1 and merged into PW.4 / PO.1.3.

1. **Defined security requirements** before code is written
   - SSDF **PO.1** *Define Security Requirements for Software Development*
   - Microsoft SDL: Requirements phase
   - OWASP SAMM: Security Requirements (Design business function)

2. **Threat modelling and risk-driven design**
   - SSDF **PW.1** *Design Software to Meet Security Requirements and Mitigate Security Risks* - PW.1.1 specifies "threat modeling, attack modeling, or attack surface mapping"
   - Microsoft SDL practice 3: "Perform security design review and threat modeling"
   - OWASP SAMM: Threat Assessment

3. **Independent design review** by someone not involved in the design
   - SSDF **PW.2** *Review the Software Design to Verify Compliance with Security Requirements and Risk Information* - PW.2.1 specifies "a qualified person (or people) who were not involved with the design"
   - Microsoft SDL: Design phase review
   - OWASP SAMM: Architecture Assessment

4. **Secure coding practices and reuse of well-secured components**
   - SSDF **PW.5** *Create Source Code by Adhering to Secure Coding Practices*
   - SSDF **PW.4** *Reuse Existing, Well-Secured Software When Feasible Instead of Duplicating Functionality*
   - Microsoft SDL practice 2: "Require use of proven security features, languages, and frameworks"
   - OWASP SAMM: Secure Build

5. **Code review and automated testing in the pipeline** - human review, SAST, DAST, SCA
   - SSDF **PW.7** *Review and/or Analyze Human-Readable Code to Identify Vulnerabilities* (covers human review and SAST)
   - SSDF **PW.8** *Test Executable Code to Identify Vulnerabilities* (covers DAST and dynamic testing)
   - SSDF **PW.4.4** third-party component verification through life cycle (covers SCA)
   - Microsoft SDL: Verification phase ("manual review by a reviewer who isn't the engineer that developed the code") + practice 7 "Perform security testing"
   - OWASP SAMM: Security Testing

6. **Documented dependency provenance** - SBOM-grade record of what you shipped and where it came from
   - SSDF **PS.3.2** "Collect, safeguard, maintain, and share provenance data for all components of each software release (e.g., in a software bill of materials [SBOM])"
   - SSDF **PW.4.4** third-party component verification
   - Microsoft SDL practice 5: "Secure the software supply chain"
   - SLSA v1.2 build-track provenance (Levels 1 - 3)

**Graphic:** Six-step horizontal flow (Requirements -> Threat model -> Independent review -> Secure coding -> SAST/DAST/SCA -> Provenance) with the SSDF practice ID under each step. **Colour-code steps 1 - 4 differently from 5 - 6**: 1 - 4 are mostly human-judgment controls that live above the pipeline; 5 - 6 are the pipeline-enforceable controls. This colour-coding sets up Slide P1.4's "outside the pipeline" framing.

**Speaker notes:** This is what "secure SDLC" actually means in practice. Six controls, all consensus, rooted in the build phase. Notice the spread across SSDF's three relevant practice groups - **PO** for requirements, **PW** for design / coding / review / testing, **PS** for supply-chain provenance. Notice also where the human load falls: steps 1 - 4 are mostly *human-judgment* controls - someone defined the requirement, someone modelled the threat, someone other than the designer reviewed the design, someone chose the secure libraries. Steps 5 - 6 are where the pipeline takes over - automated SAST/DAST/SCA and provenance generation. Hold that distinction; in Part 2 we will look at what happens to each one when an AI is sitting in the loop.

**Sources:**
- NIST SP 800-218 (SSDF v1.1) - verbatim practice titles, https://csrc.nist.gov/pubs/sp/800/218/final - PDF https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf
- Microsoft SDL practices - https://www.microsoft.com/en-us/securityengineering/sdl/practices
- OWASP SAMM model - https://owaspsamm.org/model/
- SLSA v1.2 - https://slsa.dev/spec/v1.2/

---

## Slide P1.4 - Where CI/CD fits - SDLC defines, pipelines enforce

- **SDLC = practices** (NIST SSDF, Microsoft SDL, OWASP SAMM, BSIMM). **CI/CD = enforcement** - where the practices become automated gates or get bypassed.
- **NIST SP 800-204D** (Chandramouli, Kautz, Torres-Arias; Feb 2024) - *Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines* - is the explicit bridge. Pipeline stages it covers: **build, test, package, deployment**. Two stated security goals (Sec. 4.1): (1) actively defend the CI/CD pipeline and build processes; (2) ensure the integrity of upstream sources and artifacts. Appendix A formally maps CI/CD tasks to SSDF practices **PO.1 - 5, PS.1 - 3, and PW.5 / PW.6 / PW.8 / PW.9**.
- **SLSA v1.2 build levels (L0 - L3)** turn build-platform integrity from assertion into evidence (L1 = provenance exists; L2 = hosted, signing platform; L3 = platform isolation and confidentiality).
- **DevSecOps** is the cultural frame; **shift-left** is the operational principle - a CWE caught in a PR is roughly two orders of magnitude cheaper than one caught in production.
- **CISA Secure by Design** (2023, refreshed 2024 RSAC pledge - 100+ signatories) is the policy backdrop: manufacturers own the outcome, secure defaults are baseline, vulnerabilities are disclosed transparently. SDLC + CI/CD is *how* a manufacturer earns that pledge.

**Graphic:** Two-tier diagram - top tier "SDLC practices (SSDF)" with the four PO/PS/PW/RV verbs; bottom tier "CI/CD pipeline stages (build, test, package, deploy)" with arrows from PO.1 - 5, PS.1 - 3, and PW.5 / 6 / 8 / 9 landing on pipeline stages. **A clearly marked region above the pipeline tier holds PW.1 - PW.4, PW.7, and RV.1 - RV.3, labelled "Outside the pipeline - human-judgment SDLC layer"** - this is the visual setup for Part 2. SLSA badge on the build-platform box.

**Speaker notes:** This is where I'd answer the question "but our developers already do CI/CD - isn't that enough?" The pipeline is the *runway* for the SDLC. Without an SDLC defining what the gates need to enforce, you have a fast deployment pipeline that ships insecure code faster. NIST 800-204D exists precisely because so many organisations had pipelines without the SDLC controls plumbed into them.

**The point worth landing slowly - the carve-out.** NIST 800-204D explicitly tells you what the CI/CD pipeline does *not* cover. Appendix B lists SSDF practices PW.1 through PW.4 and PW.7 - secure design, threat modelling, software-reuse decisions, code review - as "secure software design ... rather than CI/CD pipelines." It similarly carves out SSDF RV.1 - RV.3 (vulnerability response) as "at the organization policy level and not specific to CI/CD pipelines." That carve-out is structurally important: pipelines enforce the things that can be codified into automated checks; they cannot enact the human-judgment parts of the SDLC. Hold that distinction - **in Part 2 we are going to see that AI compresses or removes exactly the human-judgment parts that the pipeline cannot enforce, which is why "more pipeline tooling" alone will not save you**.

Take this as the closing frame for Part 1: secure SDLC is the practice definition; CI/CD is where the codifiable practices live; DevSecOps is the cultural commitment to keep them there; the human-judgment parts of the SDLC live *above* the pipeline and depend on actual humans actually doing them. **In Part 2 we look at what AI just changed about every layer of this.**

**Sources:**
- NIST SP 800-204D (Chandramouli, Kautz, Torres-Arias, Feb 2024), DOI https://doi.org/10.6028/NIST.SP.800-204D - landing page https://csrc.nist.gov/pubs/sp/800/204/d/final - PDF https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf
- SLSA v1.2 spec - https://slsa.dev/spec/v1.2/ (build levels https://slsa.dev/spec/v1.0/levels)
- OWASP DevSecOps Guideline - https://owasp.org/www-project-devsecops-guideline/
- CISA Secure by Design - https://www.cisa.gov/securebydesign
- CISA Secure by Design pledge - https://www.cisa.gov/securebydesign/pledge

---

# Part 2 - How AI is changing the SDLC

*To be drafted. The four assumptions (Writer / Reviewer / Dependency / Tool) move here as the framing device.*

---

# Part 3 - What to do about it

*To be drafted.*

---

## Open structural questions for v3

- **Audience-level for Part 1.** SASIG CISOs - some will know SSDF cold, some will know SDL only by name. Current draft assumes "name-recognises the frameworks but doesn't have them at fingertips." Adjust up or down?
- **One slide or two on the frameworks?** P1.1 currently bundles all four frameworks; could split into "the lineage" (SDL -> SSDF) and "the maturity / measurement layer" (SAMM, BSIMM) if more breathing room is wanted.
- **Add a fifth slide for ISO/IEC 27034 and the international standards angle?** The current four lean U.S./industry; an internationally-grounded SASIG audience may want ISO recognition.
