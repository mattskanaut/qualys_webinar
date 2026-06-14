# Part 2 Speaker Notes - Handover / Resume Doc

Last updated: 2026-06-14. Point a fresh session here to resume cleanly.

## What we're doing

Workshopping the spoken speaker notes for Part 2 of the SASIG webinar series,
"The New Normal: Software, Security and the AI Stack - Part 2: Defending AI in
Production". UK CISO audience, non-product, ~40% problem / 60% what-to-do.

- **Deck (source of truth for slide text):** `SASIG/Part2/Running-AI-in-Production.pptx` (19 slides)
- **Working notes doc:** `SASIG/Part2/speaker-notes-v4.md` - each slide has an
  `ON SLIDE:` summary, the spoken `SPEAKER NOTES`, and (where verified) a
  `SOURCES:` line. The ON SLIDE / SOURCES lines are scaffolding, NOT spoken.

## Important: deck vs notes divergence

Matt is copying finished notes into the .pptx **manually**, slide by slide. So
the .pptx speaker notes lag behind `speaker-notes-v4.md`. Treat v4.md as the
live working copy. When copying, he drops the ON SLIDE / SOURCES lines and keeps
the `[CLICK]` markers (they map to slide builds).

## Current display order (deck was reordered)

1 Title -> 2 It's already out there (hook) -> 3 System anatomy -> 4 Autonomous
agents -> 5 What you actually deploy (six-layer) -> 6 ForcedLeak (input hostile)
-> 7 Meta/Lenovo (action unauthorized / output hostile) -> 8 Lab conditions
(Gray Swan ASR) -> 9 Supply chain -> 10 Infra exposed -> 11 Agents act/can't stop
-> 12 Attacker moves second -> 13 Discipline being written -> 14 Discover ->
15 Identity -> 16 Process/red-team -> 17 Governance -> 18 On the other hand
(optimism) -> 19 Questions/close.

NB: the slideN.xml filenames do NOT match display order; display order is in
presentation.xml. To re-extract in display order, see the script approach used
before (parse presentation.xml sldIdLst -> rId -> slide file).

## Progress

- **Notes DONE (warmed into Matt's voice), DISPLAY 1-9.** Slides 4, 7, 8, 9 were
  AI-polished drafts and have been rewritten in his voice. Slides 1, 3, 5, 6 are
  his own writing with targeted edits.
- **Notes TO WRITE: DISPLAY 10-19.** (Matt said he was "only concerned up to 9"
  for now - confirm before starting 10+.)

## How we work (follow this)

- **Discuss before editing.** Propose the change, explain why, get the OK, then
  apply. One slide at a time.
- **Match Matt's OWN voice, not AI-polished prose.** His real voice = warm,
  spoken, run-on comma-spliced sentences, "So,"/"Now," openers, parenthetical
  asides, self-deprecating, generous credit to researchers ("big thanks to
  them"), British spelling. Reference slides 1/3/5 of Part 2 and his Part 1 notes
  (`SASIG/Part1/SASIG1-master-notes.pdf`). Do NOT use the crisp, rhetorical,
  short-sentence register (that was the AI-assisted slide-8 draft he rejected).
  Do not add fake typos.
- **Web-verify every specific statistic before committing it.** The AI-assisted
  drafts contained at least one fabricated detail (a made-up Opus>Sonnet>Haiku
  ranking on slide 8). Always check numbers against the real source.
- **ASCII only** in all output (user's global rule).

## Narrative spine / devices already built (keep consistent)

- **Same-channel concept** ("the model can't tell instructions from data, it all
  arrives down the same channel") is introduced ONCE at DISPLAY 3's close, then
  REFERENCED (not re-explained) on 5, 6, 8.
- **Input/action/output triad** across the breaches: ForcedLeak = hostile input
  (6), Meta = unauthorized action (7), Lenovo = hostile output (7). Slide text
  carries these labels.
- **"New attack, old control"** refrain - every breach lands on a missing control
  you already know how to run.
- **Discovery spine** - "you can't defend what you can't see" recurs: slide-2 poll
  -> slide-5 six-layer self-audit -> slide-9 supply chain. Sets up DISPLAY 14.
- **No roadmap slide** - the slide-2 notes close with a verbal roadmap instead.

## Verified facts (safe to use)

- **DISPLAY 8 (Gray Swan Indirect Prompt Injection Arena, Q1 2026, ran 25 Feb -
  11 Mar 2026, run with CAISI + UK AISI):** 13 frontier models, 464 participants,
  272,000 attempts, 8,648 successful attacks across 41 scenarios. ASR 0.5%
  (Claude Opus 4.5) to 8.5% (Gemini 2.5 Pro). No model at zero. Robustness only
  weakly correlated with capability (Gemini = most capable AND most attackable).
  Sources: arXiv 2603.15714; NIST/CAISI research blog. (CAISI = renamed US AISI,
  do NOT call it "US AI Safety Institute at NIST".)
- **DISPLAY 9 (Koi Security "ClawHavoc" audit, Jan-Feb 2026):** 341 of 2,857
  skills malicious (~11.9%, ~1 in 8); infostealers targeting browser cookies,
  .env files, SSH keys, cloud credentials (count has since grown past 800).
  **OX Security MCP supply-chain advisory (Apr 2026):** benign PoC package
  accepted with no review by 9 of 11 registries. Sources: koi.ai, ox.security.

## Parked deck-level fixes (do when past slide 9)

1. **Slide 16** on-slide text says "as Slide 10 demonstrated" re vendor ASR - now
   wrong (ASR is slides 8 and 12). Re-point, ideally by name not number.
2. **Slides 13 and 18** both cite the Five Eyes/CoSAI/OWASP/ISO "converged in 12
   months" beat - duplication. Decide whether 18 drops it and stays purely about
   defences/products working.
3. **PPTX cleanup** still needed in the deck itself (resolved in v4 notes): change
   "Nova Labs" -> "Noma Labs" (twice, slide 6) and remove the
   `{MORE HERE AND TIE IN}` placeholder.

## Suggested next step on resume

Confirm whether to start DISPLAY 10 notes (infra exposed - "Bleeding Llama"
Ollama, vLLM RCE, unauth MCP servers; theme = uninventoried assets) or address
the parked deck fixes first. Verify all stats on 10-13 before writing.

## Related

Project memory: `sasig-webinar-series-status`. Way-of-working memory:
`sasig-way-of-working`. Voice/feedback memory: `feedback-invented-frames`.
