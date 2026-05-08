# Outline v3 - running order

**Webinar:** The New SDLC: Security When Every Developer Writes With AI
**Target time:** ~30 min content + 5 min Q&A
**Slide count:** 18 (17 if Slide 8 is dropped)

| # | Section | Slide title | Content (1 - 2 sentences) | Time |
|---|---|---|---|---|
| 1 | Open | Title and the promise | Title slide. Non-product promise stated out loud. Subtitle previews the four assumptions. | 1 min |
| 2 | Open | Opening hook - real CVEs in real repos | Georgia Tech Vibe Security Radar trajectory; the slope is the story. Anchors "this is already happening." | 1.5 min |
| 3 | S1 | Secure SDLC is a defined discipline | Microsoft SDL, NIST SSDF, OWASP SAMM, BSIMM 15 - 30 years of consensus. | 2 min |
| 4 | S1 | The four convergent areas | PO / PS / PW / RV - four jobs every framework agrees on. | 1.5 min |
| 5 | S1 | The build-time controls everyone agrees on | Six controls, colour-coded human-judgment vs pipeline-enforceable. | 2 min |
| 6 | S1 | Where CI/CD fits - SDLC defines, pipelines enforce | NIST SP 800-204D bridge; Appendix B carves out PW.1 - PW.4 / PW.7 as outside pipeline scope. | 2 min |
| 7 | S2 | AI is now in every developer's hands | One arresting adoption stat (Microsoft 4.7M Copilot subs, DORA 90%, McKinsey 90%+). Take "AI is in your stack" as established. | 1.5 min |
| 8 | S2 | What's actually in your build pipeline now | One-slide AI primer - LLM + harness + MCP server + RAG retriever as the four moving parts. **Optional** - skip if cutting for time. | 1.5 min |
| 9 | S2 | The four assumptions just broke | The spine slide. (W) The developer wrote it. (R) The reviewer read it. (D) The dependencies were vetted. (T) The tools were deterministic. Icons introduced for use through the rest of the section. | 2 min |
| 10 | S2 | Writer - the developer wrote it | Veracode 2025 headline (100+ models, 80+ tasks): AI code contains 2.74x more vulnerabilities than human-written, 45% OWASP Top 10 failure, Java 72%. Apiiro Fortune-50 telemetry as field complement: +322% privilege-escalation paths, +153% architectural flaws, ~2x credential leakage, 10x findings. Pearce IEEE S&P 2022 in speaker notes as trajectory anchor (~40% CWE Top-25 in 2022 - the result has held up across four years). | 2 min |
| 11 | S2 | Reviewer - the reviewer read it | Two pillars. DORA: PR size +51%, review time +441%, 30% distrust AI-generated code - reviewers have less time. Perry/Stanford CCS 2023: AI-assisted users wrote less-secure code AND were more confident it was secure than the no-AI control - reviewers also have less reason to look, because the writer's misplaced confidence is contagious. | 2 min |
| 12 | S2 | Dependency - the dependencies were vetted | Slopsquatting. Spracklen 16-LLM study, 43% recurrence rate, Lasso huggingface-cli demo (30k downloads). Plus AI-imported-without-checking, abandoned-package suggestions, allowlist bypass. | 1.5 min |
| 13 | S2 | Tool - the tools were deterministic | LiteLLM supply-chain compromise, 2026 CVEs in Cursor / Copilot / Claude Code / Windsurf, MCP servers (Hou et al., Prakash AIP unauth scan), Vercel / Context AI breach, prompt injection. | 2 min |
| 14 | S3 | Tooling - PR gates, AI-asset inventory, IDE boundary | Pipeline-enforceable controls. Block hallucinated imports, pin AI tool versions, MCP-server inventory. | 2 min |
| 15 | S3 | Process - the human-judgment restorations | Mandatory AI-usage disclosure on PRs, AI-BOM, third-party AI-tool intake review, IR playbook update. | 2 min |
| 16 | S3 | Culture and organisation | Pair review for AI-assisted PRs; redistribute review capacity (seniors review more, write less); reward catches not velocity. Empirical anchor: Perry/Stanford CCS 2023 found AI-assisted developers were more confident their code was secure even when measurably less so - cultural moves exist to counteract that documented overconfidence, not just to enforce policy. | 2 min |
| 17 | S3 | Monday morning - restore the four | Four-row table - one Monday action per broken assumption. Anchored to NIST SP 800-218A as the metric spine. The close. | 2 min |
| 18 | Close | Q&A and Part 2 preview | Bibliography lands by email. Part 2 is *Running AI in Production*. | 1 min |

---

## Four-assumption risk count

Rough comparison of how many distinct risk categories each broken assumption carries. Slide 13 (Tool / deterministic) is the heaviest; Slide 12 (Dependency / vetted) is the narrowest but most policy-actionable.

| Slot | Risks captured | Count |
|---|---|---|
| **W - wrote** | Insecure-by-default code, +322% privilege-escalation paths, +153% architectural flaws, secret exposure ~2x, default-admin perms 41%, CWE hotspots, confidence anti-correlation, per-dev vuln rate up 2-10x | ~7 |
| **R - read** | PR size +51%, review time +441%, rubber-stamping, no AI disclosure, can't see model/prompt/RAG context, dev trust at -11pts YoY | ~6 |
| **D - vetted** | Slopsquatting (Spracklen, Lasso huggingface-cli), AI-imported-without-checking, abandoned packages AI suggests, transitive-dep blowups, allowlist bypass, doc pollution | ~5 |
| **T - deterministic** | AI-tool RCEs (Cursor, Copilot, Claude Code, Windsurf), LiteLLM supply-chain compromise, MCP servers as shadow IT, MCP unauth, prompt injection, tool poisoning, agentic loops with dev privileges, cross-server shadowing, AI-vendor breach, indirect prompt injection via RAG | ~10 |
