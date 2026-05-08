# SASIG Webinar Overlap Analysis - Part 1 Positioning

Reference doc for Matt's Part 1 webinar ("The New SDLC: Security When Every Developer Writes With AI"). Compares against four other AI-themed SASIG webinars in the same season. Snapshot date: 2026-05-06.

---

## Webinars compared (in chronological order)

| # | Date | Talk | Speaker(s) | Chair |
|---|---|---|---|---|
| 1 | Fri 1 May | Real-time AI risk telemetry / behavioural nudging | Tim Ward (CEO, Redflags / CybSafe) | John Scott (Wildpark) |
| 2 | Wed 6 May | The Good/Bad/Ugly of securing autonomous AI agents | Florian Pouchet (Partner) + Kaya Raveendran (Manager), Wavestone | Mike Hughes (Prism RA / ISACA Central UK) |
| 3 | Mon 8 June | AI Security & Exposure Survey 2026 (300 CISOs) | Mark Davis (Sr Director) + Siraaj Ahmed (RM), Pentera | Mike Hughes |
| 4 | Wed 10 June | User-reported threats as adaptive control | James Hickey (Principal SE, Cofense) | Kurt Yearwood (BAE Systems) |

Matt's webinar sits between the May talks and the June talks.

---

## Per-webinar product intelligence and likely framing

### 1. Redflags / CybSafe (Tim Ward) - 1 May

**Product:** Redflags is CybSafe's on-device behavioural-nudge agent that detects risky user actions in real time (including AI-tool use) and intervenes with just-in-time prompts. CybSafe is the broader human-risk-management (HRM) platform. Tim Ward is co-founder.

**Likely talk content:**
- Headline stat: ~38-43% of employees share sensitive data with AI tools without employer knowledge (CybSafe / NCA "Oh, Behave! 2025-2026" report)
- Argument: traditional awareness training is dead; behavioural change at the "moment of risk" wins
- Live-style examples of nudges firing on ChatGPT / Copilot paste events
- Repeated framings: *"Adaptive Human Risk Management", "behavioural security", "moments of risk", "point of decision", "science-backed" (SebDB)*

**Overlap with Matt's Part 1: LOW.** Workforce layer, not build-time. Slight cross-fire risk on Slide 16 (developer trust gap) only - Matt's framing is developer-cohort-specific, not workforce-survey, so the overlap stays low.

URLs: https://redflags.io/, https://www.cybsafe.com/, https://www.cybsafe.com/whitepapers/oh-behave-the-annual-cybersecurity-attitudes-and-behaviors-report-2025-2026

---

### 2. Wavestone (Florian Pouchet, Kaya Raveendran) - 6 May

**Product:** Management/technology consultancy. Pouchet leads Cybersecurity & Operational Resilience UK. They sell advisory engagements and run CERT-Wavestone for IR.

**Likely talk content:**
- April 2026 RiskInsight piece *"Securing AI Agents: Why IAM Becomes Central"* (Pouchet co-authored) is the talk's spine
- "Agentic AI Playbook" likely surfaces as the prescriptive framework
- Repeated framings: *"IAM as structural safeguard", "OAuth 2.x / OIDC token propagation for agents", "agent acting with own rights vs user rights vs hybrid", "centralised access control with traceability", "non-human identity"*
- Good / Bad / Ugly maps to: agent identity sprawl (Bad), runaway autonomy via over-permissioned tools (Ugly), governance + IAM controls (Good)

**Overlap with Matt's Part 1: LIGHT (heavy on Part 2).** Wavestone's runtime IAM angle is largely separate from Matt's build-time SDLC focus. Slide 5 (MCP) is the only collision point - same protocol, different layer.

URLs: https://www.wavestone.com/en/insight/agentic-ai-playbook/, https://www.riskinsight-wavestone.com/en/2026/04/securing-ai-agents-why-iam-becomes-central/

---

### 3. Pentera (Mark Davis, Siraaj Ahmed) - 8 June *(highest overlap risk)*

**Product:** Autonomous adversarial exposure validation - production-safe automated pentesting that runs full attack chains across network, identity, cloud, external surfaces. Modules: Pentera Core, Surface, Cloud, Resolve. New: Pentera 8 + Pentera Peer (natural-language agentic interface) launched RSAC 2026, GA Q2 2026. Hit $100M ARR Jan 2026.

**Likely talk content:**
- Will lead with their 300-CISO "AI Security & Exposure Survey 2026" (Feb 2026)
- **Specific stats Pentera will own** (do not cite these on Matt's slides):
  - 67% of CISOs lack AI-usage visibility
  - 75% extend legacy security controls to AI
  - 50% cite a skills gap
  - 78% have no dedicated AI security budget line
  - 0% report full visibility / no shadow AI
- Argument: scanners and CVSS fail for AI workflows; you need *adversarial validation* to know what's actually exploitable
- Repeated framings: *"Adversarial exposure validation", "prove what's exploitable", "deterministic + agentic AI" architecture, "AI visibility gap", "yesterday's tools for tomorrow's workflows"*
- Likely close: live or recorded demo of attacking an AI-enabled environment leading to a Pentera 8 + Peer reveal (the "non-product promise" will probably bend here)

**Overlap with Matt's Part 1: HIGH.** Three specific collision points:

1. **Through-line collision.** Pentera's pillar 1 ("AI visibility gap") thematically duplicates Matt's "you cannot govern what you cannot inventory."
2. **Survey-stat texture.** Pentera's 67% / 75% / 78% numbers are directionally identical to several stats Matt could carelessly invoke. Matt's slides use different evidence (Microsoft 4.7M Copilot subs, DORA 90%, McKinsey 90%+, Stanford HAI 88%) - but speaker notes that drift toward generic CISO-survey framing will sound exactly like Pentera 30 days later.
3. **Solution collision.** Pentera prescribes "do an adversarial pentest." Matt prescribes "build the pipeline gates." Both can't be the headline answer in the same audience's memory.

**Mitigating factor:** Matt presents BEFORE Pentera. Matt sets the tone; Pentera echoes.

URLs: https://pentera.io/resources/reports/ai-security-exposure-survey-2026/, https://pentera.io/press-release/pentera-introduces-adversarial-ai-agent-for-offensive-security-practitioners/

---

### 4. Cofense (James Hickey) - 10 June

**Product:** Phishing detection & response (PDR) - reported-phish triage powered by global "phish reporter button" telemetry, plus SAT, threat intel, managed services.

**Likely talk content:**
- "19 seconds" stat as the lead (one malicious email every 19 seconds in 2026 vs 42s in 2024; .es-domain credential phishing up 51x; conversational attacks 18% of malicious volume - Feb 2026 report "The New Era of Phishing")
- "Employees are not the weakest link, they are an adaptive control" - explicit thesis
- Reporter-button flywheel: report -> analyst triage -> intel -> remediation
- Likely platform demo (Hickey is an SE)
- Repeated framings: *"human-vetted intelligence", "post-delivery defence", "continuous feedback loop", "real phish, not simulated"*

**Overlap with Matt's Part 1: VERY LOW.** Different problem space (phishing / IR). Slight thesis collision with Slide 16 (Culture - reviewer reflex) but different audiences and controls.

URLs: https://cofense.com/blog/cofense-report-reveals-ai-powered-phishing-accelerated-to-one-attack-every-19-seconds, https://cofense.com/predictions-2026

---

## Aggregated risk

| Webinar | Date | Overlap | Action |
|---|---|---|---|
| Redflags / CybSafe | 1 May (before Matt) | LOW | none |
| Wavestone | 6 May (before Matt) | LIGHT on Pt 1 (heavy on Pt 2) | one Slide 5 speaker-note line |
| **Pentera** | **8 June (after Matt)** | **HIGH** | **3 targeted speaker-note tweaks** |
| Cofense | 10 June (after Matt) | VERY LOW | none |

---

## Cross-cutting strategic insight (most useful framing)

Two pairs of vendors, each pitching opposing answers to the same problem:

- **Redflags vs Cofense** both claim *"the human is the control."* Redflags owns the **pre-event nudge**; Cofense owns the **post-event report**. Both will dispute the "weakest link" framing. Matt should not pick a side - acknowledge both layers exist; his developer-reviewer-reflex content (Slide 20 Culture) sits between them and complements both.

- **Wavestone vs Pentera** both claim *"legacy controls don't fit AI."* Wavestone says **fix it with IAM and governance** (advisory engagement). Pentera says **prove it with adversarial validation** (tooling). The CISO audience will hear "do a maturity assessment" and "do a pentest" as the two prescribed answers.

**Matt's positioning play:** the build-time controls are what you do **between** the maturity assessment and the pentest - the preconditions that determine whether the maturity assessment passes and whether the pentest finds anything new. This frames Matt's content as complementary, not competing, with both Wavestone and Pentera. The line is now embedded in Slide 23 (Monday morning) speaker notes.

---

## Slide-level adjustments applied

Five speaker-note edits (no structural changes, no renumbering):

| Slide | Change |
|---|---|
| 5 (MCP) | Handoff line: "we're talking developer-side MCP discovery; runtime agent IAM is the next session's territory" - cedes runtime ground to Wavestone |
| 6 (Adoption) | Speaker note clarifies headline stats are paid-developer-tool subscriptions and dev-team adoption rates, NOT generic CISO-survey "X% lack AI visibility" framing - cedes that genre to Pentera |
| 8 (Quality) | Closes with "the SAST you already have misses 97.8% - this is a build-pipeline gap, not a runtime adversarial-testing gap" - pre-empts Pentera framing |
| 17 (Toolchain) | Speaker note: "these are build-time supply-chain incidents - runtime exploitation is a separate problem with separate controls" - same pre-emption |
| 23 (Monday morning) | Strategic positioning line: "Audiences this season are hearing 'do a maturity assessment' (Wavestone) and 'do an adversarial pentest' (Pentera). Today's checklist is what you do BETWEEN those engagements - the build-pipeline preconditions that determine whether the maturity assessment has anything to grade and whether the pentest has anything new to find." |

---

## Stats Matt should NOT cite (Pentera will own them on 8 June)

- 67% of CISOs lack AI-usage visibility
- 75% extend legacy security controls to AI
- 50% cite a skills gap on AI security
- 78% have no dedicated AI security budget
- 0% report full AI visibility / no shadow AI

If any of these creep into speaker notes during rehearsal, replace with one of Matt's developer-cohort or build-time stats (Apiiro Fortune-50, Veracode Spring 2026, Georgia Tech Vibe Security Radar, Microsoft FY26 Q2 Copilot, McKinsey 2026, Stack Overflow Feb 2026).

---

## Related files

- `SASIG/Part1/slide-plan-v2.md` - the working slide plan, where the 5 speaker-note edits land
- `SASIG/Part1/part1-sdlc.md` - the section-structure source-of-truth document
- `SASIG/otherwebinars.txt` - the raw abstracts for the four other talks
